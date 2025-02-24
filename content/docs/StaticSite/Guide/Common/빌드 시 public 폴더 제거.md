---
title: 빌드 시 public 폴더 제거
description: ''
summary: ''
date: '2024-06-21T02:45:00.020829'
lastmod: '2024-07-18T09:32:01.345448'
draft: false
weight: 10
categories:
- StaticSite
tags:
- StaticSite
- Guide
- Common
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

빌드 시 `public` 폴더를 제거하는 것은 장단점이 있습니다. 
깨끗한 빌드 환경을 유지하고 정확한 배포를 보장한다는 점은 유용하지만, 빌드 시간이 증가하고 리소스 낭비가 발생할 수 있습니다. 따라서 프로젝트의 규모와 빌드 시간을 고려하여 적절히 선택하는 것이 중요합니다. 개인적으로는 웹 게시 전 로컬 서버로 작업할 때 스크립트를 통해 자동 제거하도록 설정하여 사용하고 있습니다.

## 장점

#### 깨끗한 빌드 환경 유지    
- 기존의 파일들이 남아 있어서 발생할 수 있는 문제를 방지합니다. 특히, 파일 삭제나 이름 변경이 있었을 경우, 이전 파일이 남아있어 혼란을 줄 수 있습니다.
- 빌드 과정에서 불필요한 파일이 포함될 가능성을 줄여 배포 파일 크기를 최소화합니다.
#### 디버깅 용이    
- 불필요한 파일이 남아 있어 발생할 수 있는 오류를 예방할 수 있습니다. 빌드 후에 예상하지 못한 파일이 남아 있지 않으므로 디버깅이 수월합니다.
#### 정확한 배포
- 변경된 파일만 덮어쓰는 것이 아니라 모든 파일을 새로 생성하기 때문에, 배포 시 항상 최신 상태를 유지할 수 있습니다.
- 잘못된 캐시나 오래된 파일로 인한 배포 문제를 줄일 수 있습니다.

## 단점

#### 빌드 시간 증가    
- `public` 폴더를 삭제하고 모든 파일을 다시 생성하기 때문에, 빌드 시간이 늘어날 수 있습니다.
- 대규모 프로젝트의 경우 빌드 시간이 상당히 증가할 수 있습니다.
#### 리소스 낭비    
- 변경되지 않은 파일들도 다시 생성하기 때문에, 일부 리소스가 낭비될 수 있습니다.
- 네트워크 배포 시 변경되지 않은 파일도 재업로드되어 불필요한 트래픽이 발생할 수 있습니다.
#### 배포 오류 위험
- 빌드 중 문제가 발생하여 중단되면, `public` 폴더가 비어 있을 수 있어 배포 시 문제가 생길 수 있습니다.
- `public` 폴더가 삭제된 상태에서 빌드가 실패하면, 원래의 파일들이 모두 손실될 수 있습니다.

## 자동화

### 스크립트

```bat
@echo off

:: public 폴더 삭제
rmdir /s /q public

:: 휴고 빌드
hugo
```

### NPM 스크립트

만약 Node.js 프로젝트로 관리 중이라면, `package.json` 파일의 스크립트 섹션에 아래와 같이 추가할 수 있습니다.

```json
{
  "scripts": {
    "clean": "rimraf public",
    "build": "hugo",
    "prebuild": "npm run clean"
  }
}
```

여기서 `rimraf` 패키지를 사용하여 cross-platform으로 `public` 폴더를 삭제할 수 있습니다. `rimraf` 패키지를 설치하려면 다음 명령어를 실행하세요.

```sh
npm install rimraf --save-dev
```

이제제 `npm run build` 명령어를 실행하면, `public` 폴더를 삭제한 후 휴고 빌드가 실행됩니다.
