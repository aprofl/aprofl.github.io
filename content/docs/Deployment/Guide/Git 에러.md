---
title: Git 에러
description: ''
summary: ''
date: '2024-06-24T07:17:57.756170'
lastmod: '2024-07-18T09:32:01.310448'
draft: false
weight: 10
categories:
- Deployment
tags:
- Deployment
- Guide
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

![git_sefe_directory](/Resources/git_sefe_directory.png)

이 오류 메시지는 Git이 현재 디렉토리의 소유자가 신뢰할 수 없는 사용자라고 인식했기 때문에 발생합니다. 이는 보안상의 이유로 발생하는 경고입니다. 이를 해결하려면 해당 디렉토리를 신뢰할 수 있는 디렉토리로 설정해야 합니다.

오류 메시지에 제시된 명령어를 사용하여 디렉토리를 안전한 디렉토리로 추가하면 됩니다:

```sh
git config --global --add safe.directory D![git_sefe_directory.png](/Resources/git_sefe_directory.png) 작업을 계속 진행할 수 있습니다.
