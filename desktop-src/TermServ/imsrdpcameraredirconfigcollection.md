---
title: IMsRdpCameraRedirConfigCollection interface
description: Represents the collection of cameras (and the associated configurations) that are available for redirection.
ms.tgt_platform: multiple
keywords:
- IMsRdpCameraRedirConfigCollection interface Remote Desktop Services
- IMsRdpCameraRedirConfigCollection interface Remote Desktop Services , described
topic_type:
- apiref
api_name:
- IMsRdpCameraRedirConfigCollection
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 12/16/2020
---

# IMsRdpCameraRedirConfigCollection interface

 Represents the collection of cameras (and the associated configurations) that are available for redirection.

## Members

The **IMsRdpCameraRedirConfigCollection** interface inherits from **IUnknown**. **IMsRdpCameraRedirConfigCollection** also has these types of members:

- [Methods](#methods)
- [Properties](#properties)

### Methods

The **IMsRdpCameraRedirConfigCollection** interface has these methods.

| Method            | Description              |
|:------------------|:-------------------------|
| [**AddConfig**](imsrdpcameraredirconfigcollection-addconfig.md)       |  Adds an [IMsRdpCameraRedirConfig](imsrdpcameraredirconfig.md) object to the collection (the corresponding camera does not have to be connected).                   |
| [**Rescan**](imsrdpcameraredirconfigcollection-rescan.md)       |  Enumerates connected camera devices.                   |

### Properties

The **IMsRdpCameraRedirConfigCollection** interface has these properties.

| Property         | Access type           | Description            |
|:-----------------|:----------------------|:-----------------------|
| [**ByIndex**](imsrdpcameraredirconfigcollection-byindex.md)      | Read-only |  Returns an [IMsRdpCameraRedirConfig](imsrdpcameraredirconfig.md) object by its index in the collection.   |
| [**ByInstanceId**](imsrdpcameraredirconfigcollection-byinstanceid.md)                       | Read-only |    Returns an [IMsRdpCameraRedirConfig](imsrdpcameraredirconfig.md) object from the collection that corresponds to the specified instance ID.    |
| [**BySymbolicLink**](imsrdpcameraredirconfigcollection-bysymboliclink.md)      | Read-only |  Returns an [IMsRdpCameraRedirConfig](imsrdpcameraredirconfig.md) object from the collection that corresponds to the given symbolic link of the **KSCATEGORY_VIDEO_CAMERA** interface for the camera.  |
| [**Count**](imsrdpcameraredirconfigcollection-count.md)                       | Read-only |    Returns the number of [IMsRdpCameraRedirConfig](imsrdpcameraredirconfig.md) objects in the collection.   |
| [**EncodeVideo**](imsrdpcameraredirconfigcollection-encodevideo.md)      | Read/Write |  Specifies whether or not the video stream is H.264 encoded.  |
| [**EncodingQuality**](imsrdpcameraredirconfigcollection-encodingquality.md)                       | Read/Write |    Specifies the encoding quality (bit rate).   |
| [**RedirectByDefault**](imsrdpcameraredirconfigcollection-redirectbydefault.md)                       | Read/Write |   Specifies whether or not any new camera gets redirected by default.    |

## Requirements

| Requirement | Value |
|-------------------------------------|---------------------------------------|
| Minimum supported client| Windows 10, version 1803 (build 17134)      |
| Type library            | MsTscAx.dll                        |
| DLL                  | MsTscAx.dll     |
| IID                      | IID\_IMsRdpCameraRedirConfigCollection is defined as AE45252B-AAAB-4504-B681-649D6073A37A            |

## See also

- [**IMsRdpCameraRedirConfig**](imsrdpcameraredirconfig.md)
- [**IMsRdpClientNonScriptable7::CameraRedirConfigCollection**](imsrdpclientnonscriptable7-cameraredirconfigcollection.md)
