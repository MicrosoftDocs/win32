---
UID: NF:proofofpossessioncookieinfo.IProofOfPossessionCookieInfoManager4.GetCookieInfoForUriWithUserAgentId
tech.root: wininet
title: IProofOfPossessionCookieInfoManager4::GetCookieInfoForUriWithUserAgentId
ms.date: 04/07/2023
targetos: Windows
description: Retrieves cookie information for the supplied URI, with a user id.
prerelease: false
req.assembly: 
req.construct-type: function
req.ddi-compliance: 
req.dll: 
req.header: proofofpossessioncookieinfo.h
req.idl: 
req.include-header: 
req.irql: 
req.kmdf-ver: 
req.lib: 
req.max-support: 
req.namespace: 
req.redist: 
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.target-type: 
req.type-library: 
req.umdf-ver: 
req.unicode-ansi: 
topic_type:
 - apiref
api_type:
 - COM
api_location:
 - proofofpossessioncookieinfo.h
api_name:
 - IProofOfPossessionCookieInfoManager4::GetCookieInfoForUriWithUserAgentId
f1_keywords:
 - IProofOfPossessionCookieInfoManager4::GetCookieInfoForUriWithUserAgentId
 - proofofpossessioncookieinfo/IProofOfPossessionCookieInfoManager4::GetCookieInfoForUriWithUserAgentId
dev_langs:
 - c++
helpviewer_keywords:
 - GetCookieInfoForUriWithUserAgentId
ms.topic: reference
---

# IProofOfPossessionCookieInfoManager4::GetCookieInfoForUriWithUserAgentId method (proofofpossessioncookieinfo.h)

> [!NOTE]
> **Some information relates to pre-released product, which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.**

Retrieves cookie information for the supplied URI, with a user id. A case-sensitive string search is performed on the supplied URI. You should free the returned array by using [FreeProofOfPossessionCookieInfoArray](/windows/win32/api/proofofpossessioncookieinfo/nf-proofofpossessioncookieinfo-freeproofofpossessioncookieinfoarray).

## Syntax

```cpp
HRESULT GetCookieInfoForUriWithUserAgentId(
  [in] LPCWSTR uri,
  [in] LPCWSTR uaClientId,
  [out] DWORD* cookieInfoCount,
  [out, size_is(, *cookieInfoCount)] ProofOfPossessionCookieInfo** cookieInfo
);
```

## Parameters

`uri`

The URI to retrieve cookie information for. The URI is case-sensitive.

`uaClientId`

A client id, which will be added to the returned cookie.

`cookieInfoCount`

The number of cookies found. `*cookieInfoCount` contains the number of elements in *cookieInfo*.

`cookieInfo`

A returned array of cookie information objects. You should free the returned array by using [FreeProofOfPossessionCookieInfoArray](/windows/win32/api/proofofpossessioncookieinfo/nf-proofofpossessioncookieinfo-freeproofofpossessioncookieinfoarray).

## Return value

If this method succeeds, it returns **S_OK**. Otherwise, it returns an **HRESULT** error code.

## See also

[IProofOfPossessionCookieInfoManager4](./nn-proofofpossessioncookieinfo-iproofofpossessioncookieinfomanager4.md)

## Requirements

| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | proofofpossessioncookieinfo.h |
