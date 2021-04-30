---
title: IMsRdpCameraRedirConfig Redirected property
description: Specifies whether or not the camera is redirected. 
ms.tgt_platform: multiple
keywords:
- Redirected property Remote Desktop Services
- Redirected property Remote Desktop Services , IMsRdpCameraRedirConfig interface
- IMsRdpCameraRedirConfig interface Remote Desktop Services , Redirected property
topic_type:
- apiref
api_name:
- IMsRdpCameraRedirConfig.Redirected
- IMsRdpCameraRedirConfig.put_Redirected
- IMsRdpCameraRedirConfig.get_Redirected
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 12/16/2020
---

# IMsRdpCameraRedirConfig::Redirected property

Specifies whether or not the camera is redirected.

This property is read/write.

## Syntax

```C++
HRESULT put_Redirected(
    [in] VARIANT_BOOL fRedirected
);

HRESULT get_Redirected(
    [out, retval] VARIANT_BOOL* pfRedirected
);
```

## Property value

A value that specifies whether or not the camera is redirected.

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