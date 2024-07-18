---
title: NextCloud를 이용한 동기화 방법
description: ''
summary: ''
date: '2024-06-21T02:01:21.250192'
lastmod: '2024-07-18T09:32:01.335448'
draft: false
weight: 10
categories:
- Obsidian
tags:
- Obsidian
- Guide
- Setting
- Sync
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

## 요약

-  Nextcloud 클라이언트를 각 기기에 설치하고 설정합니다.
-  Nextcloud에 Obsidian 볼트를 저장할 폴더를 생성합니다.
-  Obsidian 볼트 폴더를 Nextcloud의 폴더와 동기화 합니다.4. 
-  동기화가 정상적으로 작동하는지 테스트합니다.

## Nextcloud 설정

####  Nextcloud 서버 설정
- Nextcloud 서버 설치 및 설정을 완료합니다.
- Nextcloud 웹 인터페이스에 로그인하여 필요한 경우 SSL 인증서를 설정하고 보안을 강화합니다.
#### Nextcloud 클라이언트 설치
- [Nextcloud 클라이언트 다운로드 페이지](https://nextcloud.com/install/)에서 운영체제에 맞는 클라이언트를 다운로드하여 설치합니다.

## Obsidian 볼트 동기화 설정

#### Nextcloud에 Obsidian 볼트 폴더 생성
- Nextcloud 웹 인터페이스나 클라이언트에서 Obsidian 볼트를 저장할 폴더를 생성합니다.
#### Obsidian 볼트 폴더를 Nextcloud와 동기화
- 각 기기에서 Nextcloud 클라이언트를 열고 동기화할 폴더를 설정합니다.
 
![nextcloud_setting](/Resources/nextcloud_setting.png)

- Obsidian 볼트를 저장할 로컬 폴더를 선택하고, Nextcloud 서버의 대응하는 폴더를 선택합니다.
    - 예를 들어, `Nextcloud/obsidian`폴더를 로컬 Obsidian 볼트 폴더와 연결합니다.

## Obsidian 설정

#### Obsidian 볼트 위치 설정
- 현재 사용 중인 Obsidian 폴더를 동기화 하였다면, 추가적인 설정이 필요하지 않습니다.
- 별개의 폴더를 동기화 폴더로 설정한 경우, 
	- Obsidian에서 사용하고 있는 볼트를 Nextcloud와 동기화되는 로컬 폴더로 이동합니다.
	- Obsidian을 실행합니다..`Open another vault`를 선택하고, Nextcloud 동기화 폴더 내의 볼트를 선택합니다.

## 테스트 및 확인

- 각 기기에서 Obsidian을 열고 노트를 작성하거나 편집한 후, Nextcloud를 통해 변경사항이 다른 기기로 동기화되는지 확인합니다.
