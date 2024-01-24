---
title: IMsRdpCameraRedirConfig ParentInstanceId property
description: Gets the parent device instance ID of the camera.
ms.tgt_platform: multiple
keywords:
- ParentInstanceId property Remote Desktop Services
- ParentInstanceId property Remote Desktop Services , IMsRdpCameraRedirConfig interface
- IMsRdpCameraRedirConfig interface Remote Desktop Services , ParentInstanceId property
topic_type:
- apiref
api_name:
- IMsRdpCameraRedirConfig.ParentInstanceId
- IMsRdpCameraRedirConfig.get_ParentInstanceId
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 12/16/2020
---

# IMsRdpCameraRedirConfig::ParentInstanceId property

Gets the parent device instance ID of the camera.

This property is read-only.

## Syntax

```C++
HRESULT get_ParentInstanceId(
    [out, retval] BSTR* pParentInstanceId
);
```

## Property value

The parent device instance ID of the camera.

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