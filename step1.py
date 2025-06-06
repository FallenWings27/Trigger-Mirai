import os
import re
import json
import requests

# === Bangumi 配置 ===
BANGUMI_TOKEN = "你的API"
BANGUMI_SEARCH_URL = "https://api.bgm.tv/v0/search/subjects"
HEADERS_BANGUMI = {
    "User-Agent": "TriggerMirai/1.0",
    "Content-Type": "application/json",
    "Authorization": f"Bearer {BANGUMI_TOKEN}"
}

# === 净化目录名 ===
def clean_title(folder_name):
    # 去除常见的干扰信息
    pattern = r"(\[.*?\])|((1080|720|480)p)|((x|X)264|(x|X)265)|HEVC|10bit|WebRip|BDrip|S\d+|Season\s?\d+|全集|字幕组|简体|繁体|BIG5|GB|CHS|CHT|MP4|AAC|FLAC"
    cleaned = re.sub(pattern, '', folder_name, flags=re.IGNORECASE)
    cleaned = re.sub(r'\s+', ' ', cleaned).strip()
    return cleaned

# === Bangumi 搜索 ===
def query_bangumi(keyword: str):
    payload = {
        "keyword": keyword,
        "filter": { "type": [2] },  # 2 = 动画
        "limit": 5
    }
    try:
        resp = requests.post(BANGUMI_SEARCH_URL, headers=HEADERS_BANGUMI, json=payload, timeout=10)
        resp.raise_for_status()
        data = resp.json()
        return data.get("data", [])
    except Exception as e:
        print(f"Bangumi 搜索失败: {e} (keyword: {keyword})")
        return []

# === 主程序 ===
def main():
    root_path = input("Enter your anime root directory path: ").strip('" ')
    if not os.path.exists(root_path):
        print("目录不存在！")
        return

    results = {}

    folders = [f for f in os.listdir(root_path) if os.path.isdir(os.path.join(root_path, f))]
    print(f"发现 {len(folders)} 个番剧目录。\n")

    for folder in folders:
        print(f"正在处理目录: {folder}")
        cleaned = clean_title(folder)
        print(f"  净化后关键词：'{cleaned}'")

        matches = query_bangumi(cleaned)
        if matches:
            top = matches[0]
            print(f"  ✅ 匹配成功: {top['name']} / {top.get('name_cn', '')} (ID: {top['id']})")
            results[folder] = {
                "matched_name": top["name"],
                "matched_cn": top.get("name_cn"),
                "bangumi_id": top["id"]
            }
        else:
            print("  ❌ 未匹配到任何结果。")
            results[folder] = None

    # 输出到结果文件
    output_path = os.path.join(root_path, "bangumi_match_results.json")
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)

    print("\n处理完毕，结果已保存到：", output_path)

if __name__ == "__main__":
    main()
