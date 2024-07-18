---
title: Tips
description: ''
summary: ''
date: '2024-06-21T02:01:21.381844'
lastmod: '2024-07-18T09:32:01.373448'
draft: false
weight: 10
categories:
- StaticSite
tags:
- StaticSite
- Guide
- MkDocs
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
다크모드를 기본으로 바꾸는 법

```yml
theme:
  name: material
  palette:
    - scheme: slate # 다크 모드를 기본으로 설정
      primary: indigo
      accent: indigo
      toggle:
        icon: material/brightness-4
        name: Switch to light mode
    - scheme: default
      primary: indigo
      accent: indigo
      toggle:
        icon: material/brightness-7
        name: Switch to dark mode
  font:
    text: Roboto
    code: Roboto Mono  
  extra_css:
    - css/custom.css
```
