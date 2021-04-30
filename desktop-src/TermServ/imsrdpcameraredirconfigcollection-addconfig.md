---
title: IMsRdpCameraRedirConfigCollection AddConfig method
description: Adds an IMsRdpCameraRedirConfig object to the collection (the corresponding camera does not have to be connected).
ms.tgt_platform: multiple
keywords:
- AddConfig method Remote Desktop Services
- AddConfig method Remote Desktop Services, IMsRdpCameraRedirConfigCollection interface
- IMsRdpCameraRedirConfigCollection interface Remote Desktop Services, AddConfig method
topic_type:
- apiref
api_name:
- IMsRdpCameraRedirConfigCollection.AddConfig
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 12/16/2020
---

# IMsRdpCameraRedirConfigCollection::AddConfig method

Adds an [IMsRdpCameraRedirConfig](imsrdpcameraredirconfig.md) object to the collection (the corresponding camera does not have to be connected).

## Syntax

```C++
HRESULT AddConfig(
    [in] BSTR symbolicLink,
    [in] VARIANT_BOOL fRedirected
);
```

## Parameters

*symbolicLink* \[in\]

The symbolic link for the new [IMsRdpCameraRedirConfig](imsrdpcameraredirconfig.md) object.

*fRedirected* \[in\]

Specifies whether or not the new camera gets redirected by default.

## Return value

Return **S\_OK** if successful.

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