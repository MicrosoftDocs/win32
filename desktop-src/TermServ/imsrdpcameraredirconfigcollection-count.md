---
title: IMsRdpCameraRedirConfigCollection Count property
description: Returns the number of IMsRdpCameraRedirConfig objects in the collection.
ms.tgt_platform: multiple
keywords:
- Count property Remote Desktop Services
- Count property Remote Desktop Services , IMsRdpCameraRedirConfigCollection interface
- IMsRdpCameraRedirConfigCollection interface Remote Desktop Services , Count property
topic_type:
- apiref
api_name:
- IMsRdpCameraRedirConfigCollection.Count
- IMsRdpCameraRedirConfigCollection.get_Count
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 12/16/2020
---

# IMsRdpCameraRedirConfigCollection::Count property

Returns the number of [IMsRdpCameraRedirConfig](imsrdpcameraredirconfig.md) objects in the collection.

This property is read-only.

## Syntax

```C++
HRESULT get_Count(
    [out, retval] ULONG *pCount
);
```

## Property value

The number of [IMsRdpCameraRedirConfig](imsrdpcameraredirconfig.md) objects in the collection.

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