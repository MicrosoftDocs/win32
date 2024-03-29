---
title: IMsRdpCameraRedirConfig FriendlyName property
description: Gets the camera's friendly name. 
ms.tgt_platform: multiple
keywords:
- FriendlyName property Remote Desktop Services
- FriendlyName property Remote Desktop Services , IMsRdpCameraRedirConfig interface
- IMsRdpCameraRedirConfig interface Remote Desktop Services , FriendlyName property
topic_type:
- apiref
api_name:
- IMsRdpCameraRedirConfig.FriendlyName
- IMsRdpCameraRedirConfig.get_FriendlyName
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 12/16/2020
---

# IMsRdpCameraRedirConfig::FriendlyName property

Gets the camera's friendly name.

This property is read-only.

## Syntax

```C++
HRESULT get_FriendlyName(
    [out, retval] BSTR* pFriendlyName
);
```

## Property value

The camera's friendly name.

## Requirements

| Requirement | Value |
|-------------------------------------|---------------------------------------|
| Minimum supported client| Windows 10, version 1803 (build 17134)      |
| Type library            | MsTscAx.dll                        |
| DLL                  | MsTscAx.dll     |
| IID                      | IID\_IMsRdpCameraRedirConfig is defined as 09750604-D625-47C1-9FCD-F09F735705D7            |

## See also

<dl> <dt>

[**IMsRdpCameraRedirConfig**](imsrdpcameraredirconfig.md)
</dt> </dl>