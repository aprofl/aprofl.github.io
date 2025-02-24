---
title: Front Matter
description: ''
summary: ''
date: '2024-06-21T02:01:21.348842'
lastmod: '2024-07-18T09:32:01.352448'
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

## 메타데이터

메타데이터를 각 문서의 시작 부분에 추가하면, Hugo는 이를 기반으로 문서를 렌더링하고 SEO 최적화 작업을 수행합니다. 
필수 필드는 아니지만, 각 필드를 적절하게 채워 넣으면 사이트의 품질과 검색 엔진 최적화에 도움이 됩니다.
- 다음은 doks theme 용 Front Matter 입니다.
- 테마에 따라 내용이 달라질 수 있습니다.

## 주요 필드

- title: 섹션의 제목을 정의합니다. 이는 섹션의 인덱스 페이지에 표시됩니다.
- description: 섹션에 대한 설명입니다. 주로 검색 엔진이나 미리보기에서 사용됩니다.
- summary: 섹션의 요약입니다. 페이지나 게시물의 요약으로 표시되며, 검색 결과나 목록에서 사용될 수 있습니다.
- date: 섹션의 생성 날짜와 시간입니다.
- lastmod: 섹션의 마지막 수정 날짜와 시간입니다.
- draft: 섹션이 초안 상태인지 여부를 나타냅니다. `true`로 설정하면 섹션이 사이트 빌드 시 포함되지 않습니다.
- weight: 섹션의 정렬 순서를 제어합니다. 낮은 숫자가 더 높은 우선 순위를 가집니다.
- toc: 섹션의 목차(Table of Contents) 표시 여부를 제어합니다.
- seo: SEO 최적화를 위한 설정을 포함합니다.
    - title: SEO를 위한 맞춤 제목입니다.
    - description: SEO를 위한 맞춤 설명입니다.
    - canonical: SEO를 위한 맞춤 캐노니컬 URL입니다.
    - noindex: 검색 엔진에서 인덱싱하지 않도록 설정합니다.