---
title: IMsRdpClientNonScriptable7 CameraRedirConfigCollection property
description: Gets the collection of cameras (and the associated configurations) that are available for redirection.
ms.tgt_platform: multiple
keywords:
- CameraRedirConfigCollection property Remote Desktop Services
- CameraRedirConfigCollection property Remote Desktop Services , IMsRdpClientNonScriptable7 interface
- IMsRdpClientNonScriptable7 interface Remote Desktop Services , CameraRedirConfigCollection property
topic_type:
- apiref
api_name:
- IMsRdpClientNonScriptable7.CameraRedirConfigCollection
- IMsRdpClientNonScriptable7.get_CameraRedirConfigCollection
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 12/16/2020
---

# IMsRdpClientNonScriptable7::CameraRedirConfigCollection property

Gets the collection of cameras (and the associated configurations) that are available for redirection.

This property is read-only.

## Syntax


```C++
HRESULT get_CameraRedirConfigCollection(
  [out, retval] IMsRdpCameraRedirConfigCollection** ppCameraCollection
);
```

## Property value

An [IMsRdpCameraRedirConfigCollection](imsrdpcameraredirconfigcollection.md) that represents the collection of cameras (and the associated configurations) that are available for redirection.

## Requirements

| Requirement | Value |
|-------------------------------------|---------------------------------------|
| Minimum supported client| Windows 10, version 1803 (build 17134)      |
| Type library            | MsTscAx.dll                        |
| DLL                  | MsTscAx.dll     |
| IID                      | IID\_IMsRdpClientNonScriptable7 is defined as 71B4A60A-FE21-46D8-A39B-8E32BA0C5ECC          |

## See also

<dl> <dt>

[**IMsRdpClientNonScriptable7**](imsrdpclientnonscriptable7.md)
</dt> </dl>