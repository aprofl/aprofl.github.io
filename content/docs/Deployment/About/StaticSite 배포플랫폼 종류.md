---
title: StaticSite 배포플랫폼 종류
description: ''
summary: ''
date: '2024-06-21T02:01:21.174684'
lastmod: '2024-07-18T09:32:01.305448'
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

## 요약

플랫폼 기반 배포는 과정이 간단하고, 정적 사이트에 최적화된 기능을 제공합니다.
- Netlify나 Vercel : 사용하기 쉽고 강력한 기능을 제공하며, 특히 CDN 및 서버리스 기능이 필요하다면 추천합니다.
- GitHub Pages: 무료로 사용하기 좋으며, 간단한 프로젝트에 적합합니다.
- Cloudflare Pages: 빠른 CDN을 제공하여, 기본적인 정적 사이트 배포에 적합하며, [비용안정성](StaticSite%20배포플랫폼%20선택.md)이 높습니다.

## Netlify

#### 장점
- 쉬운 설정: GitHub, GitLab, Bitbucket과 통합하여 간편하게 배포할 수 있습니다.
- 자동 빌드 및 배포: 푸시할 때마다 자동으로 빌드 및 배포가 이루어집니다.
- CDN 제공: 전 세계에 분산된 CDN을 통해 빠른 사이트 로딩 속도를 제공합니다.
- SSL 지원: 무료 SSL 인증서를 자동으로 발급하고 갱신해 줍니다.
- 폼 처리, 서버리스 함수: 정적 사이트에 동적 기능을 쉽게 추가할 수 있습니다.
#### 단점
- 요금제 제한: 무료 요금제의 경우 일부 기능에 제한이 있을 수 있습니다.
- 무료 요금제의 경우도 트래픽이 무료 한도를 넘어서면 유료로 전환됩니다.
#### 요금제
##### 무료 플랜
- 기본 제공: 무료 플랜에서 정적 사이트 호스팅, SSL, 자동 배포 기능을 제공합니다.
- 기본 보호: DDoS 공격에 대한 기본 보호가 있지만, Cloudflare만큼 강력하지 않을 수 있습니다.
- 제한 사항: 빌드 시간, 서버리스 함수 호출 수, 폼 제출 횟수 등에 제한이 있습니다.
##### 유료 플랜
- Pro Plan: 월 $19, 더 많은 빌드 시간과 폼 제출 수, 서버리스 함수 호출 수 제공.
- Business Plan: 월 $99, 팀 기능 및 고급 설정, 더 많은 자원 제공.
- Enterprise Plan: 맞춤형 요금, 모든 기능과 최고 수준의 성능 및 지원 제공.

## Vercel

#### 장점
- Netlify 와 거의 동일
#### 단점
- Netlify 와 거의 동일
#### 요금제
##### 무료 플랜
- Netlify 와 거의 동일
##### 유료 플랜
- Pro Plan: 월 $20, 더 많은 빌드 시간과 서버리스 함수 호출 수 제공.
- Enterprise Plan: 맞춤형 요금, 모든 기능과 최고 수준의 성능 및 지원 제공.

## GitHub Pages

#### 장점
- 무료 제공: GitHub 계정만 있으면 무료로 사용할 수 있습니다.
- 간편한 설정: GitHub 리포지토리 설정에서 간편하게 Pages를 활성화할 수 있습니다.
- 지속적인 통합: GitHub Actions를 사용하여 자동으로 빌드 및 배포할 수 있습니다.
#### 단점
- 기능 제한: Netlify나 Vercel과 같은 고급 기능(예: 서버리스 함수, 폼 처리 등)이 부족합니다.
- 빌드 시간 제한: 큰 프로젝트의 경우 빌드 시간이 오래 걸릴 수 있습니다.

## Cloudflare Pages

#### 장점
- 무료 제공: 기본적으로 무료로 사용할 수 있으며, 유료 플랜도 제공됩니다.
- 고속 CDN: Cloudflare의 글로벌 네트워크를 통해 빠른 사이트 로딩 속도를 제공합니다.
- 자동 빌드 및 배포: GitHub, GitLab과 통합하여 자동으로 빌드 및 배포가 이루어집니다.
- SSL 지원: 무료 SSL 인증서를 자동으로 발급합니다.
#### 단점
- 제한된 서버리스 기능: Netlify나 Vercel과 비교하여 서버리스 기능이 제한적입니다.
#### 요금제
##### 무료 플랜
- 기본 제공: 무료 플랜에서도 정적 사이트 호스팅과 SSL, 자동 배포 기능을 제공합니다.
- DDoS 보호: Cloudflare는 기본적으로 무료 플랜에서도 **DDoS 공격 방어 기능을 제공**합니다. 
- 갑작스러운 트래픽 폭증에 대해 **추가 비용이 발생하지 않습니다**.
- 제한 사항: Workers KV, Durable Objects 등 고급 기능은 사용 제한이 있습니다.
##### 유료 플랜
- Pro Plan: 월 $20, 더 높은 성능 및 우선 지원 제공.
- Business Plan: 월 $200, 더 많은 기능 및 성능 최적화, 고급 DDoS 보호 제공.
- Enterprise Plan: 맞춤형 요금, 모든 기능과 최고 수준의 성능 및 지원 제공.
