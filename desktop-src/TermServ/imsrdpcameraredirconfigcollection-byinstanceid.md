---
title: IMsRdpCameraRedirConfigCollection ByInstanceId property
description: Returns an IMsRdpCameraRedirConfig object from the collection that corresponds to the specified instance ID.
ms.tgt_platform: multiple
keywords:
- ByInstanceId property Remote Desktop Services
- ByInstanceId property Remote Desktop Services , IMsRdpCameraRedirConfigCollection interface
- IMsRdpCameraRedirConfigCollection interface Remote Desktop Services , ByInstanceId property
topic_type:
- apiref
api_name:
- IMsRdpCameraRedirConfigCollection.ByInstanceId
- IMsRdpCameraRedirConfigCollection.get_ByInstanceId
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 12/16/2020
---

# IMsRdpCameraRedirConfigCollection::ByInstanceId property

Returns an [IMsRdpCameraRedirConfig](imsrdpcameraredirconfig.md) object from the collection that corresponds to the specified instance ID.

This property is read-only.

## Syntax

```C++
HRESULT get_ByInstanceId(
    [in]          BSTR instanceId,
    [out, retval] IMsRdpCameraRedirConfig** ppConfig
);
```

## Property value

The [IMsRdpCameraRedirConfig](imsrdpcameraredirconfig.md) object that corresponds to the specified instance ID.

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