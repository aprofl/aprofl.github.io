---
title: Taxonomies
description: ''
summary: ''
date: '2024-06-21T02:01:21.361842'
lastmod: '2024-07-18T09:32:01.363447'
draft: false
weight: 10
categories:
- StaticSite
tags:
- StaticSite
- Guide
- Hugo
- config.toml
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

## Taxonomies

Taxonomies는 Hugo에서 콘텐츠를 분류하고 정리하는 데 사용되는 메커니즘입니다. 
Taxonomies 설정을 통해 Hugo 사이트의 콘텐츠를 더 잘 조직하고 사용자에게 관련 콘텐츠를 쉽게 탐색할 수 있는 방법을 제공합니다. 
만약 이러한 기능이 필요하지 않다면 taxonomies 설정을 생략할 수 있지만, 이는 콘텐츠 관리와 사용자 경험 측면에서 제한이 될 수 있습니다.
일반적으로 태그(tag)와 카테고리(category)가 가장 많이 사용됩니다.

```toml
[taxonomies]
tag = "tags"
category = "categories"
```

이 섹션은 사이트에서 사용할 taxonomies를 정의합니다. 
여기서는 두 가지 taxonomies를 정의하고 있습니다:
- `tag = "tags"`
	- 태그는 여러 게시물에 적용할 수 있는 키워드입니다. 
	- 예를 들어, 특정 주제를 가진 여러 게시물에 같은 태그를 달 수 있습니다. 
	- 여기서 `tag`는 단수형 이름이고 `tags`는 URL에서 사용할 복수형 이름입니다.
- `category = "categories"`
	- 카테고리는 게시물을 분류하는 더 광범위한 그룹입니다. 
	- 예를 들어, 블로그의 큰 주제별로 카테고리를 나눌 수 있습니다. 
	- `category`는 단수형 이름이고 `categories`는 URL에서 사용할 복수형 이름입니다.

## Taxonomies 설정 예시

위와 같이 설정했을 때, 다음과 같이 컨텐츠에 메타데이터를 추가하여 Taxonomies를 적용할 수 있습니다.

```md obsi1.md
옵시디언 기능에 대한 안내 페이지입니다.
```

## params.taxonomy

taxonomies의 추가 설정을 정의합니다.

```toml
[params.taxonomy]
taxonomyCloud = ["tags", "categories"]
taxonomyCloudTitle = ["Tag Cloud", "Categories"]
taxonomyPageHeader = ["tags", "categories"]
```

- `taxonomyCloud = ["tags", "categories"]`
	- 이 설정은 태그 클라우드와 카테고리 클라우드를 표시할 taxonomies를 지정합니다. 
	- 태그 클라우드와 카테고리 클라우드는 해당 항목의 분포를 시각적으로 나타낸 것입니다.
- `taxonomyCloudTitle = ["Tag Cloud", "Categories"]`
	- 이 설정은 태그 클라우드와 카테고리 클라우드의 제목을 지정합니다. 
	- 각 항목은 `taxonomyCloud` 배열의 항목과 일치해야 합니다.
- `taxonomyPageHeader = ["tags", "categories"]`
	- 이 설정은 페이지 헤더에 표시할 taxonomies를 지정합니다.
	- 페이지 헤더에 태그와 카테고리가 표시됩니다.

## Taxonomies 설정 의미

Taxonomies를 설정하지 않으면 Hugo는 기본적으로 콘텐츠를 태그와 카테고리로 분류하지 않습니다. 
이는 사이트 방문자가 콘텐츠를 특정 주제나 그룹으로 쉽게 검색하거나 필터링할 수 없다는 의미입니다. 
구체적으로는 다음과 같은 영향을 미칩니다:
### Taxonomies를 설정하지 않을 경우의 영향
#### 태그와 카테고리 기능 비활성화
- 콘텐츠에 태그나 카테고리를 지정해도, 이를 통해 콘텐츠를 그룹화하거나 검색할 수 없습니다.
- 예를 들어, 블로그 게시물에 여러 태그를 달아도 그 태그를 클릭하여 관련 게시물을 찾을 수 없습니다.
#### 태그 클라우드와 카테고리 클라우드 표시 안 됨
- 사이트에 태그 클라우드나 카테고리 클라우드를 표시하는 부분이 없다면, 사용자가 태그나 카테고리를 통해 콘텐츠를 탐색할 수 없습니다.
#### 페이지 헤더에 태그나 카테고리 표시 안 됨    
- 콘텐츠 페이지의 헤더에 태그나 카테고리가 표시되지 않습니다. 
- 이는 각 콘텐츠가 어떤 주제나 카테고리에 속하는지 사용자에게 명확히 보여주지 않습니다.
#### SEO 및 UX 영향    
- 검색 엔진 최적화(SEO) 측면에서 태그와 카테고리는 중요한 역할을 합니다. 
- 검색 엔진은 태그와 카테고리를 통해 콘텐츠의 주제와 관련성을 더 잘 이해할 수 있습니다.
- 사용자 경험(UX) 측면에서도 사용자가 특정 주제에 대한 콘텐츠를 쉽게 찾을 수 있게 하므로 중요한 요소입니다.