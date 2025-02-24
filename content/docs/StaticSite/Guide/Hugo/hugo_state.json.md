---
title: hugo_state.json
description: ''
summary: ''
date: '2024-06-26T11:20:23.308258'
lastmod: '2024-07-18T09:32:01.354448'
draft: false
weight: 10
categories:
- StaticSite
tags:
- StaticSite
- Guide
- Hugo
contributors: []
toc: true
sidebar:
  collapsed: true
seo:
  title: ''
  description: ''
  canonical: ''
  noindex: false
---
`hugo_stats.json` 파일은 일반적으로 Hugo 사이트의 자산 관리를 최적화하는 데 사용됩니다. 이 파일의 주요 역할과 관리 방법에 대해 설명하겠습니다.

### `hugo_stats.json` 파일의 역할

- **자산 최적화**: `hugo_stats.json` 파일은 Hugo가 빌드 시 생성하는 파일로, 자산(예: CSS, JS 파일) 최적화 정보가 포함되어 있습니다. 이 파일은 Hugo의 Hugo Pipes 기능을 통해 생성되며, 자산의 해시, 크기, 경로 등의 정보를 포함합니다.
- **빌드 성능 향상**: 이 파일을 사용하면 Hugo는 자산을 다시 컴파일할 필요 없이 기존 자산을 재사용할 수 있어 빌드 시간을 단축할 수 있습니다.

### 깃으로 추적해야 하나?

- **추적하지 않음**: 일반적으로 `hugo_stats.json` 파일은 빌드 아티팩트로 간주되므로 Git에서 추적하지 않는 것이 좋습니다. 이 파일은 빌드 시마다 변경되므로, Git에서 추적하면 불필요한 커밋이 많이 발생할 수 있습니다.
- **`.gitignore`에 추가**: `hugo_stats.json` 파일을 Git의 추적에서 제외하려면 프로젝트의 `.gitignore` 파일에 다음 줄을 추가합니다.

```sh
hugo_stats.json
```