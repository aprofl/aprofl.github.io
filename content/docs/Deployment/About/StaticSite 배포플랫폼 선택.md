---
title: StaticSite 배포플랫폼 선택
description: ''
summary: ''
date: '2024-06-21T02:01:21.173684'
lastmod: '2024-07-18T09:32:01.304448'
draft: false
weight: 10
categories:
- Deployment
tags:
- Deployment
- About
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

## 비용 안정성

비용을 고려해야 한다면, Cloudflare Pages의 무료 플랜이 비용 안전성이 매우 높습니다. 
Cloudflare Pages의 무료 플랜을 선택하고 추가 기능을 사용하지 않는 경우, 기본적으로 발생하는 트래픽에 대해 비용이 추가로 청구되지 않습니다. 
### Cloudflare Pages 무료 플랜의 장점
- 고정 비용 없음: 무료 플랜은 정적 사이트 호스팅, 자동 배포, SSL 등 기본 기능을 무료로 제공합니다.
- DDoS 보호 포함: 기본적으로 Cloudflare의 DDoS 방어 기능이 포함되어 있어, 갑작스러운 트래픽 증가에도 추가 비용이 발생하지 않습니다.
- 대규모 트래픽 처리: Cloudflare의 글로벌 CDN을 통해 대규모 트래픽도 효율적으로 처리할 수 있습니다.
### 비용 발생에 대한 보장
- 무료 플랜의 확실성
	- 무료 플랜 내에서 제공되는 리소스와 기능을 사용하면 비용이 발생하지 않습니다. 
	- Cloudflare는 무료 플랜의 제한을 명확히 하고 있으며, 사용자가 선택하지 않는 한 추가 비용이 발생하지 않습니다.
- 추가 기능 사용 시 주의
	- Cloudflare Workers, Workers KV 등의 추가 기능을 사용하면 사용량에 따라 비용이 발생할 수 있습니다.
	- 그러나 사용자가 명시적으로 이러한 기능을 활성화하지 않는 한, 추가 비용은 발생하지 않습니다.
### Netlify 및 Vercel의 우려점
- 자동 증가 비용
	- Netlify와 Vercel의 무료 플랜은 사용량에 제한이 있으며, 이를 초과하면 자동으로 비용이 발생할 수 있습니다. 
	- 예를 들어, 빌드 시간 초과, 서버리스 함수 호출 수 초과 등이 이에 해당합니다.
- 예상치 못한 비용
	- 트래픽 급증 시 추가 리소스 사용으로 인해 예기치 않은 비용이 발생할 수 있습니다. 
	- 이 때문에 트래픽 관리가 중요한 사이트 운영자에게는 부담이 될 수 있습니다.