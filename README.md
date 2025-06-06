# Trigger Mirai

> 自动化的番剧命名与元数据匹配系统 | Anime Tagging & Metadata Automation Tool

---

## 🧠 项目简介

**Trigger Mirai** 是一个面向本地番剧管理者的实用工具，致力于为本地番剧文件自动匹配 **Bangumi 元数据**、提取字幕组信息、清洗命名噪声、生成可用于媒体服务器（如 Jellyfin）的结构化元数据。

项目支持 **整部作品连播模式** 和 **季节分组模式**，并支持以 **绝对编号（absolute numbering）** 的方式串联所有正篇内容，同时排除 OP/ED/NCOP/NCED/特典等非主线剧集内容。

---

## ✨ 核心功能

- 🔍 自动提取文件夹 / 文件名中的关键词
- 🔗 接入 **Bangumi API** 获取对应条目信息
- 🧼 清洗命名信息（去除字幕组标记、分辨率、编码等无关信息）
- 📋 提取并保留字幕组信息用于标注归属
- 🧠 智能识别季数、集数、剧集绝对编号
- 🔄 支持将所有季合并为一部作品进行连播编号
- 🗂️ 分类输出元数据（主线剧集 / 额外内容）
- ✅ 可用于生成媒体库、剧集封面匹配、连播序列等二次开发场景

---
🧾 关于 OP/ED/NOP/特典等处理
Trigger Mirai 会自动识别以下关键字并将其归类为 "extra" 类型：

OP / ED / NCOP / NCED / Opening / Ending

Bonus / 特典 / Preview / Trailer / PV / MV / CM

这些文件不会被自动编号或参与主线剧集连播排序。
.

├── step1.py        # 文件夹名清洗与 Bangumi 条目匹配
├── step2.py        # 文件匹配、集数提取与剧集元数据绑定
├── filters.py      # 文件名关键字识别与清洗策略
├── bangumi_api.py  # Bangumi API 交互模块
├── tag_utils.py    # 标签生成与字幕组提取
└── config.json     # 配置项（未来支持自定义过滤规则）

🔮 规划中的功能
 支持 Shoko 风格的独立季节剧集列表

 支持合并所有季节剧集为一体并持续编号

 支持解析 OVA 并决定插入策略（独立 / 接续 / 标记跳过）

 提供 Jellyfin 等媒体服务器格式的 .nfo 或 .xml 输出

 可视化 Web UI 接口（开发后期）

 可选与 TMDB、AniDB 对接，拓展信息来源

⚠️ 法律声明
本项目仅用于本地媒体整理学习用途，不提供任何下载资源、不涉及侵权内容的传播或链接。

版权说明：
本项目使用的所有 API 数据来源为 Bangumi 开放平台，仅作数据对接使用。

所有片源及文件请用户自行合法获取，Trigger Mirai 不存储、传输、索引任何音视频内容。

部分代码逻辑与自动匹配策略由 OpenAI ChatGPT 参与协作完成。

如有不当使用行为或触犯法律责任，与作者无关，请勿用于商业化场景。

💰 支持与赞助
Trigger Mirai 正在积极开发中，如果你希望本项目继续维护，未来将考虑开通捐赠渠道。欢迎 PR、欢迎建议。

🧑‍💻 项目发起人
开发者 ID: mirai

灵感来源于个人管理本地番剧资源的经验与痛点，为了解决「命名混乱、元数据缺失、难以整合」的问题。

This is the tag filter system, from the future — Trigger Mirai.
