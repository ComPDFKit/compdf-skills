![ComPDF-Comprehensive PDF Solutions](images/ComPDF-ComprehensivePDFSolutions.png)

[English](README.md) | [繁體中文](README_TW.md) | [日本語](README_JA.md) | [简体中文](README_CN.md)

# ComPDF Skills

**ComPDF Skills** 为 AI Agent 提供 **PDF/图片解析、数据提取、文档格式转换及 PDF 处理能力**，帮助 Agent 构建完整的自动化文档处理流程。在大模型推理前，ComPDF Skills 可完成文档解析、OCR、数据提取及结构化预处理，将非结构化文件转换为 AI 可直接理解的数据，仅将必要内容传递给模型，从而减少 Token 消耗、降低模型调用成本，并显著提升 Agent 的文档处理效率与回答质量。

> - 如果 ComPDF Skills 对你的工作流有帮助，欢迎在 GitHub 给我们一个 ⭐ **Star**。
> - 如果你有问题、建议或集成需求，欢迎通过 **Issues** 和 **Discussions** 与我们交流。

<p align="center">
  <a href="https://github.com/ComPDFKit/compdf-skills"><img src="https://img.shields.io/github/stars/ComPDFKit/compdf-skills?style=social" alt="GitHub Stars"></a>
  <a href="#"><img src="https://img.shields.io/badge/Agent%20Skills-Ready-3863F1" alt="Agent Skills Ready"></a>
  <a href="#"><img src="https://img.shields.io/badge/License-Free%20to%20Start-FF8A00" alt="Free to Start"></a>
</p>

<p align="center">
  <a href="#为什么选择-compdf-skills"><b>为什么选择 ComPDF Skills</b></a> •
  <a href="#支持功能"><b>支持功能</b></a> •
  <a href="#license-与免费使用"><b>License 与免费使用</b></a> •
  <a href="#安装与启用"><b>安装与启用</b></a> •
  <a href="#适用场景与示例指令"><b>适用场景</b></a> •
  <a href="#支持"><b>支持</b></a>
</p>

## 为什么选择 ComPDF Skills

- 专业的 AI 文档处理能力：提供 PDF/图片解析、OCR、数据提取、格式转换、页面处理等能力，将非结构化文档转换为 AI 可直接理解的结构化数据，帮助 Agent 更准确地处理复杂文档。

- 更高效、更低成本的 AI 工作流：在模型推理前完成文档解析与预处理，仅将必要内容传递给大模型，减少 Token 消耗，降低模型调用成本，同时提升 Agent 的响应速度与处理效率。

- 丰富的文档格式支持：支持 Word、Excel、PowerPoint、HTML、Markdown、JSON、CSV、RTF、TXT、图片等输出格式，满足不同 Agent 工作流和业务系统的数据交换需求。

- 免费开始，轻松验证价值：提供每月免费文档处理资产，完全满足日常文档处理需求。

## 支持功能

ComPDF Skills 为 Agent 提供文档转换、PDF 操作，以及智能解析与数据提取功能，详情如下：

### 1. PDF 解析与数据提取

| 能力          | 说明                                             |
| ----------- | ---------------------------------------------- |
| 图片解析与数据提取   | 从图片文件中提取文本、表格、字段和结构化内容，便于进入后续 AI 工作流与自动化处理。    |
| PDF 解析与数据提取 | 从 PDF 文件中提取文本、表格、字段和结构化内容，便于进入后续 AI 工作流与自动化处理。 |

### 2. PDF 与图片转换

| 能力             | 说明                                                                         |
| -------------- | -------------------------------------------------------------------------- |
| PDF 转 Word     | 将 PDF 文件转换为可编辑的 Word 文档，并尽可能保留原始版式、文本、图片和格式。                               |
| PDF 转 Excel    | 将 PDF 文件转换为 Excel，支持表格、数字和结构化业务数据。                                         |
| PDF 转 PPT      | 将 PDF 页面转换为可编辑的 PowerPoint 幻灯片，并尽量保留原始版式和视觉结构。                             |
| PDF 转 HTML     | 将 PDF 文件转换为 HTML，用于网页展示与内容复用，同时保留文本、图片、表格和版式。                              |
| PDF 转 RTF      | 将 PDF 文件转换为 RTF 文档，支持文本和图片内容。                                              |
| PDF 转图片        | 将 PDF 页面转换为 PNG、JPG、JPEG、JPEG2000、BMP、TIFF、TGA、GIF、WEBP 图片，并支持分辨率与 DPI 配置。 |
| PDF 转 CSV      | 从 PDF 文件中提取表格并导出为 CSV，可按单表导出，也可合并导出。                                       |
| PDF 转 TXT      | 从 PDF 或扫描版 PDF 中提取文本，并保存为纯文本文件。                                            |
| PDF 转 JSON     | 从 PDF 文件中提取文本、表格和图片，并保存为结构化 JSON。                                          |
| PDF 转 Markdown | 将 PDF 文件转换为 Markdown，便于在知识库、开发文档、博客系统和 AI 工作流中继续编辑、检索与复用。                  |
| PDF 转可搜索 PDF   | 对扫描版 PDF 执行 OCR 识别，生成可搜索、可复制、可高亮文本的 PDF 文档，便于检索、归档与后续处理。                   |
| PDF 转可搜索 OFD   | 对扫描版 PDF 执行 OCR 识别，并转换为可搜索的 OFD 文件，便于在 OFD 归档、流转与本地化办公场景中使用。               |
| Word 转 PDF     | 将 Word 文档转换为 PDF，尽量保留原始排版、字体、图片和页面结构，适合正式分享、归档和打印。                         |
| PNG 转 PDF      | 将 PNG 图片转换为 PDF，便于将截图、设计图或证据图片统一整理、传输和归档。                                  |
| RTF 转 PDF      | 将 RTF 文档转换为 PDF，在保留基础文本样式和版面的同时，便于跨设备查看与正式输出。                              |
| Excel 转 PDF    | 将 Excel 工作簿或表格转换为 PDF，便于报表共享、打印、归档和防止公式被误改。                                |
| TXT 转 PDF      | 将 TXT 纯文本文件转换为 PDF，适合将日志、笔记、说明文档等内容整理为固定版式文件。                              |
| CSV 转 PDF      | 将 CSV 表格数据转换为 PDF，便于数据快照分享、审阅、打印和业务归档。                                     |
| PPT 转 PDF      | 将 PowerPoint 演示文稿转换为 PDF，便于演示材料分发、跨设备查看和正式留档。                              |
| HTML 转 PDF     | 将 HTML 网页或内容片段转换为 PDF，适合网页留存、报告导出、邮件内容存档和可打印输出。                            |
| 图片转 Word       | 将 JPG、JPEG、PNG、BMP 图片文件转换为可编辑的 Word 文档。                                    |
| 图片转 Excel      | 将图片文件转换为 Excel 工作簿，支持表格、文本和数字内容。                                           |
| 图片转 PPT        | 将图片文件转换为可编辑的 PowerPoint 幻灯片，并尽量保留可见版式和内容结构。                                |
| 图片转 PDF        | 将 JPG、JPEG、PNG、BMP 等图片文件转换为 PDF，便于多张图片统一汇总、分享、打印和归档。                       |
| 图片转 HTML       | 将图片文件转换为 HTML，并尽量保留文本、版式、表格和主要视觉元素。                                        |
| 图片转 RTF        | 将图片文件转换为 RTF 文档，支持提取文本和图片内容。                                               |
| 图片转 CSV        | 从图片文件中提取表格并导出为 CSV。                                                        |
| 图片转 TXT        | 从图片文件中提取文本并保存为纯文本文件。                                                       |
| 图片转 JSON       | 从图片文件中提取文本、表格和图片，并保存为结构化 JSON。                                             |

### 3. PDF 编辑与保护

| 能力        | 说明                               |
| --------- | -------------------------------- |
| 合并 PDF 文件 | 将多个 PDF 文件合并为一个 PDF 文档。          |
| 拆分 PDF 文件 | 将一个 PDF 文件拆分成多个更小的 PDF 文件。       |
| 旋转 PDF 页面 | 将选定的 PDF 页面旋转 90、180 或 270 度。    |
| 插入 PDF 页面 | 在现有 PDF 中插入空白页、图片页或来自其他 PDF 的页面。 |
| 删除 PDF 页面 | 删除 PDF 文件中的一个或多个页面。              |
| 提取 PDF 页面 | 提取选定页面或页码范围，并另存为新文件。             |
| 添加水印      | 为 PDF 文件添加文字或图片水印，用于品牌展示或使用控制。   |
| 删除水印      | 从支持的 PDF 文件中删除文字或图片水印。           |
| 加密 PDF    | 使用 AES 加密和权限控制保护 PDF 文件。         |
| 解密 PDF    | 在授权前提下移除 PDF 文件密码，便于内部处理或复用。     |

## License 与免费使用

安装 ComPDF Skills 后，[注册获取 License](https://www.compdf.com/compdf-portal/signin?utm_source=github&utm_medium=referral&utm_campaign=compdf_skills_repo_cn&ref_platform_id=github_compdfkit_skills_cn) 并将 API Key 发给 Agents，即可开始免费使用。

![get-license](images/get-license.png)

## 安装与启用

建议优先通过 GitHub Skills 仓库安装，并将单个 Skill 目录连同 `SKILL.md`、`docs/`、`scripts/` 等配套文件一起保留。若正式对外仓库 URL 尚未确定，请先将下述命令中的占位符替换为真实仓库地址或仓库路径。

### 1. 从 GitHub 获取 Skills

方式一：支持 Agent Skills 标准的平台，可直接通过仓库路径安装：

```bash
npx skills add <owner>/<repo>/skills -y
```

方式二：手动从 GitHub 下载或克隆仓库，再复制目标 Skill 文件夹：

```bash
git clone https://github.com/ComPDFKit/compdf-skills.git
```

将目标 Skill 目录复制到各 Agent 支持的 Skills / Rules 目录中，并保留完整目录结构。

### 2. 主流 Agent 产品启用方式

#### Claude Code

1. 先安装并登录 Claude Code。
2. 通过 GitHub Skills 安装，或使用已发布的 Skill 安装命令。
3. 如使用仓库目录方式，请将 Skill 文件夹放入 Claude Code 的 skills 目录后重启会话。
4. 在对话中直接输入任务，或显式提及对应 Skill 名称开始调用。

如平台侧已发布安装入口，可参考以下命令形态：

```bash
claude skill add <namespace>/<skill-name>
claude skill install <skill-url>
```

#### Windsurf

1. 打开项目工作区。
2. 将从 GitHub 获取的 Skill 文件夹放入 `.windsurf/skills/compdf-skills/`，或放入跨平台代理兼容目录 `.agents/skills/compdf-skills/`。
3. 确保目录内包含 `SKILL.md` 及所需附属文件。
4. 打开 Cascade 面板后，Windsurf 会自动发现该 Skill。
5. 可直接描述任务让 Cascade 自动调用，或使用 `@compdf-skills` 手动启用。

#### Cline

1. 安装并打开 Cline。
2. 将从 GitHub 获取的 Skill 文件夹放入项目级 `.cline/skills/compdf-skills/`，或全局目录 `~/.cline/skills/compdf-skills/`。
3. 打开 Cline 面板，点击底部的 Skills 入口确认 Skill 已被发现并启用。
4. 在聊天中直接输入任务，或使用 `/compdf-skills` 显式调用。

#### Cursor

Cursor 当前官方文档更推荐通过 Rules 与 `AGENTS.md` 提供持久化指令，而不是直接使用独立 Skills 目录。

1. 从 GitHub 获取 ComPDF Skills 仓库中的核心说明文件。
2. 将通用说明整理为项目级规则文件，放入 `.cursor/rules/compdf-skills.mdc`，或在项目根目录放置 `AGENTS.md` 作为兼容层。
3. 打开 Cursor Agent / CLI，规则会按配置自动加载。
4. 在 Agent 中输入任务，例如转换、提取、OCR、加水印等请求即可开始使用。

#### 企业内部 Agent 平台

1. 将 ComPDF Skills GitHub 仓库镜像到企业内部代码仓或制品仓。
2. 统一维护 `SKILL.md`、版本号、License 文件和支持脚本。
3. 在企业 Agent 平台中按目录挂载 Skills，或将核心说明转为平台规则模板。
4. 推荐采用“ComPDF 预处理 + AI 推理”工作流：先做解析、转换、提取，再交给大模型分析与生成。

## 适用场景与示例指令

上传 PDF、图片或其他源文件。输入任务指令，例如提取表格、转换格式、合并 PDF、添加水印。Agent 调用对应的 ComPDF Skill 并返回结果。如需进一步分析，再将处理结果交给 AI。

示例场景：

* 用户在 ChatGPT、自定义 Agent、企业 Agent 平台等平台中上传行业报告、白皮书或方案 PDF，先转成 Markdown / Word，再让 AI 输出摘要、重点观点或内容重组结果
* 用户在 Skills 工作流中处理发票、对账单、图片表格和扫描件时，先提取表格与结构化数据，再进入财务审核、报销整理、系统录入或自动化流转
* 用户在 Agent 中整理合同、投标书、报价单、交付文件或归档资料时，先完成 PDF 合并、拆分、加水印和格式转换，再交给 AI 做整理、命名或对外发送准备
* 用户在多步骤工作流中，先把 PDF 或图片转换成 CSV、JSON、TXT、Markdown 等轻量结果，再交给后续 Agent 做字段归纳、知识入库、审批流处理或自动化编排

**示例指令：**

* 把这份 PDF 转成 Word，并尽量保留排版。
* 提取这份 PDF 中的所有表格并导出为 CSV。
* 把这张图片转成 JSON，输出结构化内容。
* 合并这些 PDF，添加水印，然后返回最终文件。
* 先把这份报告转成 Markdown，再帮我总结重点。

## 支持

如果你有任何问题或建议，欢迎：

- 提交 `Issue`
- 参与 `Discussions`
- [联系 ComPDF 团队](https://www.compdf.com/contact-sales?utm_source=github&utm_medium=referral&utm_campaign=compdf_skills_repo_cn&ref_platform_id=github_compdfkit_skills_cn)，咨询商业授权、企业部署或规模化落地

如果 ComPDF Skills 对你的工作流有帮助，欢迎给我们一个 ⭐ **Star**。

---

<p align="center">
  <b>由 ComPDF 团队打造。</b><br>
  <a href="https://www.compdf.com/?utm_source=github&utm_medium=referral&utm_campaign=compdf_skills_repo_cn&ref_platform_id=github_compdfkit_skills_cn">官网</a> ·
  <a href="https://www.compdf.com/contact-sales?utm_source=github&utm_medium=referral&utm_campaign=compdf_skills_repo_cn&ref_platform_id=github_compdfkit_skills_cn">联系销售</a> ·
  <a href="#安装与启用">安装与启用</a>
</p>
