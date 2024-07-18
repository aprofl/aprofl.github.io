---
title: Templater
description: ''
summary: ''
date: '2024-06-21T02:01:21.230192'
lastmod: '2024-07-18T09:32:01.330448'
draft: false
weight: 10
categories:
- Obsidian
tags:
- Obsidian
- Guide
- Plugin
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

## Templater 플러그인 설치 및 설정

#### Templater 플러그인 설치 및 활성화
- 옵시디언의 설정(Settings)에서 **Community Plugins** 섹션을 찾습니다.
- **Templater** 플러그인을 검색하여 설치하고 활성화합니다.
#### Template 폴더 생성 및 설정
- 원하는 위치에 폴더를 생성합니다. 
	- 예를 들어 **Resources/Templates**라는 폴더를 생성합니다.
- 설정(Settings)에서 **Templater** 설정을 열고, Template 폴더 위치를 `Resources/Templates` 폴더로 지정합니다.

## Template 작성

Template 파일 생성
- Template 폴더에 새로운 Template 파일을 생성합니다. 
	- 예를 들어, Templates/new_note_template.md.
- Template 내용 작성
	- Template 파일에 원하는 내용과 Template 명령어를 작성합니다.

## Template 적용

Templater는 새로운 파일을 만들 때뿐만 아니라, 기존 파일에 Template을 삽입하거나 Template 명령어를 실행할 때도 사용할 수 있습니다.
### 새로운 파일을 만들 때
Templater를 사용하여 새로운 파일을 만들 때 Template을 자동으로 적용할 수 있습니다. \
이는 일반적으로 새로운 노트를 생성할 때 Template을 적용하는 방식입니다.
 
- 새로운 파일 생성 시 Template 적용
	- 새로운 파일을 만들 때 Template을 선택하여 파일을 생성합니다. 
	- Obsidian에서 Ctrl+P를 눌러 명령 팔레트를 열고, "Templater: Create new note from template"를 선택한 후 원하는 Template을 선택합니다.
### 기존 파일에 Template 삽입
기존 파일에 Template을 삽입할 수도 있습니다. 
이는 특정 내용이나 스니펫을 기존 파일에 추가할 때 유용합니다.
- 기존 파일을 열고, Ctrl+P를 눌러 명령 팔레트를 연 다음 "Templater: Insert template"를 선택합니다. 
- 원하는 Template을 선택하여 내용을 삽입합니다.
### Template 명령어 실행
Templater 명령어를 실행하여 파일 내 특정 작업을 수행할 수 있습니다. 예를 들어, 이미지 링크를 수정하는 작업을 자동화할 수 있습니다.
- 해당 파일을 열고, Ctrl+P를 눌러 명령 팔레트를 연 다음 "Templater: Run command"를 선택하여 원하는 Templater 명령어를 실행합니다.

## 사용 예

### [폴더별 Template 설정](obsidian/guide/setting/글%20생성%20시%20메타데이터%20추가.md)
### 기본 노트 Template

```md
# <% tp.file.title %>
Created on <% tp.date.now("dddd, MMMM Do YYYY") %>.

## Notes
- 

## Tasks
- [ ] 

```

- 새 노트를 생성할 때 제목, 날짜, 태그 등을 자동으로 추가합니다.
### 일간 로그 Template


```md
# Daily Log - <% tp.date.now("dddd, MMMM Do YYYY") %>

## Morning
- [ ] 

## Afternoon
- [ ] 

## Evening
- [ ] 

## Notes

```


- 이 Template은 매일 새로운 로그를 생성할 때 사용됩니다.
### 프로젝트 Template
아래는 프로젝트 노트를 위한 Template 예시입니다. 이 Template은 새 프로젝트 노트를 만들 때 프로젝트 개요, 목표, 작업 목록 등을 자동으로 추가합니다.

```md
# <% tp.file.title %>
**Start Date**: <% tp.date.now("YYYY-MM-DD") %>
**End Date**: 
**Status**: Planned

## Overview

## Goals

## Tasks
- [ ] 

## Notes
```

### 첨부 이미지 이름 기본 설정 Template


```md
<%*
const moment = tp.date.now("YYYYMMDD-HHmmss");
const noteTitle = tp.file.title;
const newFileName = `${noteTitle}-${moment}.png`;
const imageFolderPath = `${app.vault.adapter.basePath}/Resources`;

// Create the image folder if it does not exist
if (!await app.vault.adapter.exists(imageFolderPath)) {
    await app.vault.createFolder(imageFolderPath);
}

// Generate the full path for the new image file
const newFilePath = `${imageFolderPath}/${newFileName}`;

// Return the markdown image link
%>![<% newFileName %>](Resources/<% newFileName %>)
<%*
%>
```

- 이미지 추가 시, 노트 제목과 날짜/시간을 결합하여 새로운 이미지 파일 이름을 생성합니다.
- 볼트 최상위 폴더를 기준으로 'Resources' 폴더 경로를 저장 위치로 설정합니다.
	- 'Resources' 폴더가 존재하지 않으면 생성합니다.
