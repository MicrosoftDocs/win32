---
title: IMsRdpCameraRedirConfig DeviceExists property
description: Specifies whether or not the camera device currently exists (that is, the camera is connected).
ms.tgt_platform: multiple
keywords:
- DeviceExists property Remote Desktop Services
- DeviceExists property Remote Desktop Services , IMsRdpCameraRedirConfig interface
- IMsRdpCameraRedirConfig interface Remote Desktop Services , DeviceExists property
topic_type:
- apiref
api_name:
- IMsRdpCameraRedirConfig.DeviceExists
- IMsRdpCameraRedirConfig.get_DeviceExists
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 12/16/2020
---

# IMsRdpCameraRedirConfig::DeviceExists property

Specifies whether or not the camera device currently exists (that is, the camera is connected).

This property is read-only.

## Syntax

```C++
HRESULT get_DeviceExists(
    [out, retval] VARIANT_BOOL* pfExists
);
```

## Property value

A value that indicates whether or not the camera device currently exists (that is, the camera is connected).

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