---
UID: NN:proofofpossessioncookieinfo.IProofOfPossessionCookieInfoManager4
tech.root: wininet
title: IProofOfPossessionCookieInfoManager4
ms.date: 04/07/2023
targetos: Windows
description: Supports the creation of proof-of-possession cookies, for a WebAccount and a client id.
prerelease: false
req.assembly: 
req.construct-type: iface
req.ddi-compliance: 
req.header: proofofpossessioncookieinfo.h
req.idl: 
req.include-header: 
req.max-support: 
req.namespace: 
req.redist: 
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.target-type: 
req.unicode-ansi: 
topic_type:
 - apiref
api_type:
 - COM
api_location:
 - proofofpossessioncookieinfo.h
api_name:
 - IProofOfPossessionCookieInfoManager4
f1_keywords:
 - IProofOfPossessionCookieInfoManager4
 - proofofpossessioncookieinfo/IProofOfPossessionCookieInfoManager4
dev_langs:
 - c++
helpviewer_keywords:
 - IProofOfPossessionCookieInfoManager4
ms.topic: reference
---

# IProofOfPossessionCookieInfoManager4 interface (proofofpossessioncookieinfo.h)

> [!NOTE]
> **Some information relates to pre-released product, which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.**

Supports the creation of proof-of-possession cookies, for a [WebAccount](/uwp/api/windows.security.credentials.webaccount) and a client id.

## Inheritance

The **IProofOfPossessionCookieInfoManager4** interface derives from the **IUknown** interface.

## Methods

The **IProofOfPossessionCookieInfoManager4** interface has these methods.

| &nbsp; |
| ---- |
| [IProofOfPossessionCookieInfoManager4::GetCookieInfoForUriWithUserAgentId](../proofofpossessioncookieinfo/nf-proofofpossessioncookieinfo-getcookieinfoforuriwithuseragentid.md) <br><br> Retrieves cookie information for the supplied URI, with a user id.|
| [IProofOfPossessionCookieInfoManager4::GetCookieInfoWithUriAndUserAgentIdForAccount](../proofofpossessioncookieinfo/nf-proofofpossessioncookieinfo-getcookieinfowithurianduseragentidforaccount.md) <br><br> Retrieves cookie information for the supplied [WebAccount](/uwp/api/windows.security.credentials.webaccount) and URI, with a user id.|

## Requirements

| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | proofofpossessioncookieinfo.h |
