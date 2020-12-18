---
title: IMsRdpCameraRedirConfig InstanceId property
description: Gets the instance ID of the camera.
ms.tgt_platform: multiple
keywords:
- InstanceId property Remote Desktop Services
- InstanceId property Remote Desktop Services , IMsRdpCameraRedirConfig interface
- IMsRdpCameraRedirConfig interface Remote Desktop Services , InstanceId property
topic_type:
- apiref
api_name:
- IMsRdpCameraRedirConfig.InstanceId
- IMsRdpCameraRedirConfig.get_InstanceId
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 12/16/2020
---

# IMsRdpCameraRedirConfig::InstanceId property

Gets the instance ID of the camera.

This property is read-only.

## Syntax

```C++
HRESULT get_InstanceId(
    [out, retval] BSTR* pInstanceId
);
```

## Property value

The instance ID of the camera.

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