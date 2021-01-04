---
title: IMsRdpCameraRedirConfigCollection BySymbolicLink property
description: Returns an IMsRdpCameraRedirConfig object from the collection that corresponds to the given symbolic link of the **KSCATEGORY_VIDEO_CAMERA** interface for the camera.
ms.tgt_platform: multiple
keywords:
- BySymbolicLink property Remote Desktop Services
- BySymbolicLink property Remote Desktop Services , IMsRdpCameraRedirConfigCollection interface
- IMsRdpCameraRedirConfigCollection interface Remote Desktop Services , BySymbolicLink property
topic_type:
- apiref
api_name:
- IMsRdpCameraRedirConfigCollection.BySymbolicLink
- IMsRdpCameraRedirConfigCollection.get_BySymbolicLink
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 12/16/2020
---

# IMsRdpCameraRedirConfigCollection::.BySymbolicLink property

Returns an [IMsRdpCameraRedirConfig](imsrdpcameraredirconfig.md) object from the collection that corresponds to the given symbolic link of the **KSCATEGORY_VIDEO_CAMERA** interface for the camera.

This property is read-only.

## Syntax

```C++
HRESULT get_BySymbolicLink(
    [in]          BSTR symbolicLink,
    [out, retval] IMsRdpCameraRedirConfig** ppConfig
);
```

## Property value

The [IMsRdpCameraRedirConfig](imsrdpcameraredirconfig.md) object that corresponds to the specified symbolic link.

## Requirements

| Requirement | Value |
|-------------------------------------|---------------------------------------|
| Minimum supported client| Windows 10, version 1803 (build 17134)      |
| Type library            | MsTscAx.dll                        |
| DLL                  | MsTscAx.dll     |
| IID                      | IID\_IMsRdpCameraRedirConfigCollection is defined as AE45252B-AAAB-4504-B681-649D6073A37A          |

## See also

<dl> <dt>

[**IMsRdpCameraRedirConfigCollection**](imsrdpcameraredirconfigcollection.md)
</dt> </dl>