---
title: _index.md
description: ''
summary: ''
date: '2024-06-21T02:01:21.350842'
lastmod: '2024-07-18T10:02:53.203737'
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

## 개요

`_index.md` 파일은 Hugo에서 섹션(폴더)의 인덱스 페이지를 정의하는 데 사용되는 특별한 Markdown 파일입니다. 이 파일은 폴더의 메타데이터와 콘텐츠를 설정하며, 각 섹션의 인덱스 페이지에 대한 다양한 설정을 정의할 수 있습니다. `_index.md` 파일은 주로 섹션의 제목, 설명, 정렬 순서, SEO 설정 등을 지정하는 데 사용됩니다.

## 역할과 기능

#### 섹션의 [메타데이터](Front%20Matter.md) 설정    
`_index.md` 파일을 통해 섹션의 제목, 설명, 날짜, 수정 날짜, 드래프트 상태, 가중치, 목차 등의 [메타데이터](Front%20Matter.md)를 설정할 수 있습니다.
#### SEO 최적화
- SEO 관련 메타데이터를 설정하여 검색 엔진 최적화를 도울 수 있습니다. 예를 들어, 제목, 설명, 캐노니컬 URL, 인덱스 여부 등을 지정할 수 있습니다.
#### 콘텐츠 포함    
- 섹션의 인덱스 페이지에 표시될 콘텐츠를 `_index.md` 파일에 직접 작성할 수 있습니다.
#### 테마와의 연동    
- 특정 테마, 특히 Doks와 같은 고급 테마는 `_index.md` 파일을 사용하여 섹션의 레이아웃과 스타일을 커스터마이즈할 수 있습니다. 이를 통해 일관된 디자인과 사용자 경험을 제공할 수 있습니다.
### 언제 `_index.md` 파일이 필요하지 않을 수 있는가?
#### 단순한 사이트 구조
- 모든 폴더가 단순히 콘텐츠 파일(`.md` 파일)만 포함하고 있고, 추가적인 메타데이터나 정렬이 필요하지 않은 경우 `_index.md` 파일이 필요하지 않을 수 있습니다.
#### 테마의 기본 설정
- 일부 테마는 기본적으로 모든 섹션에 대해 특정 레이아웃과 메타데이터를 제공하므로 `_index.md` 파일이 없어도 기본 설정이 적용됩니다.
### `_index.md` 파일이 없는 경우
특정 테마에서 `_index.md` 파일이 없으면, 해당 섹션의 기본 설정이 적용되지만, 다음과 같은 문제를 겪을 수 있습니다:
#### 메타데이터 누락
- 섹션의 SEO 최적화나 기타 메타데이터 설정이 누락될 수 있습니다.
#### 기본 레이아웃 적용
- 특정 섹션의 인덱스 페이지가 기본 레이아웃으로 표시될 수 있습니다.

## `_index.md` 파일의 예제

```yaml file:_index.md
---
title: About
description: ''
summary: ''
date: '2024-07-18T10:05:44.418495+00:00'
lastmod: '2024-07-18T10:05:44.418495+00:00'
draft: false
weight: 10
categories: []
tags: []
contributors: []
toc: true
sidebar:
  collapsed: true
seo:
  title: ''
  description: ''
  canonical: ''
  noindex: true
---

```

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