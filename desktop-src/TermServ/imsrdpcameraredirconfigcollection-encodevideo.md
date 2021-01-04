---
title: IMsRdpCameraRedirConfigCollection EncodeVideo property
description: Specifies whether or not the video stream is H.264 encoded.
ms.tgt_platform: multiple
keywords:
- EncodeVideo property Remote Desktop Services
- EncodeVideo property Remote Desktop Services , IMsRdpCameraRedirConfigCollection interface
- IMsRdpCameraRedirConfigCollection interface Remote Desktop Services , EncodeVideo property
topic_type:
- apiref
api_name:
- IMsRdpCameraRedirConfigCollection.EncodeVideo
- IMsRdpCameraRedirConfigCollection.put_EncodeVideo
- IMsRdpCameraRedirConfigCollection.get_EncodeVideo
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 12/16/2020
---

# IMsRdpCameraRedirConfigCollection::EncodeVideo property

Specifies whether or not the video stream is H.264 encoded.

This property is read/write.

## Syntax

```C++
HRESULT put_EncodeVideo(
    [in] VARIANT_BOOL fEncode
);

HRESULT get_EncodeVideo(
    [out, retval] VARIANT_BOOL* pfEncode
);
```

## Property value

A value that indicates whether or not the video stream is H.264 encoded.

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