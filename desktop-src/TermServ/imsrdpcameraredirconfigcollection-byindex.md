---
title: IMsRdpCameraRedirConfigCollection ByIndex property
description: Returns an IMsRdpCameraRedirConfig object by its index in the collection.
ms.tgt_platform: multiple
keywords:
- ByIndex property Remote Desktop Services
- ByIndex property Remote Desktop Services , IMsRdpCameraRedirConfigCollection interface
- IMsRdpCameraRedirConfigCollection interface Remote Desktop Services , ByIndex property
topic_type:
- apiref
api_name:
- IMsRdpCameraRedirConfigCollection.ByIndex
- IMsRdpCameraRedirConfigCollection.get_ByIndex
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 12/16/2020
---

# IMsRdpCameraRedirConfigCollection::ByIndex property

Returns an [IMsRdpCameraRedirConfig](imsrdpcameraredirconfig.md) object by its index in the collection.

This property is read-only.

## Syntax

```C++
HRESULT get_ByIndex(
    [in]            ULONG index,
    [out, retval]   IMsRdpCameraRedirConfig** ppConfig
);
```

## Property value

The [IMsRdpCameraRedirConfig](imsrdpcameraredirconfig.md) object that corresponds to the specified index.

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