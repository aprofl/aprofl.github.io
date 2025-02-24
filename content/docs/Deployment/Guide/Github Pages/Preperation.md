---
title: Preperation
description: ''
summary: ''
date: '2024-07-18T04:07:29.969696'
lastmod: '2024-07-18T09:40:35.043886'
draft: false
weight: 10
categories:
- Deployment
tags:
- Deployment
- Guide
- Github Pages
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
Hugo 사이트를 빌드합니다. 기본적으로 `public` 디렉토리에 빌드 결과가 생성됩니다.

### 2. GitHub Pages 설정

GitHub Pages를 사용하여 사이트를 호스팅하기 위해서는 GitHub에 저장소를 만들어야 합니다.

1. GitHub에서 새로운 저장소를 생성합니다. 
2. 저장소 이름을 `username.github.io`로 설정합니다. 
	1. 여기서 `username`은 GitHub 사용자 이름입니다.
    

### 사용자 페이지 vs 프로젝트 페이지

#### 사용자 페이지

사용자 페이지는 GitHub 사용자 이름에 따라 고유한 도메인을 갖게 됩니다. 이는 하나의 고유한 웹사이트로 사용되며, 저장소 이름은 다음과 같은 형식을 따라야 합니다:

- **형식**: `username.github.io`
- **예시**: 사용자가 `aprofl`인 경우, 저장소 이름은 `aprofl.github.io`

#### 프로젝트 페이지

프로젝트 페이지는 특정 프로젝트에 대한 웹사이트를 제공할 때 사용됩니다. 프로젝트 페이지는 여러 개 만들 수 있으며, 저장소 이름은 자유롭게 설정할 수 있습니다. 그러나 프로젝트 페이지를 사용하기 위해서는 `gh-pages` 브랜치를 설정해야 합니다.