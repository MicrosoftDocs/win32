---
title: IMsRdpCameraRedirConfig interface
description: Represents the configurations for a camera that is available for redirection.
ms.tgt_platform: multiple
keywords:
- IMsRdpCameraRedirConfig interface Remote Desktop Services
- IMsRdpCameraRedirConfig interface Remote Desktop Services , described
topic_type:
- apiref
api_name:
- IMsRdpCameraRedirConfig
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 12/16/2020
---

# IMsRdpCameraRedirConfig interface

Represents the configurations for a camera that is available for redirection.

## Members

The **IMsRdpCameraRedirConfig** interface inherits from **IUnknown**. **IMsRdpCameraRedirConfig** also has these types of members:

- [Properties](#properties)

### Properties

The **IMsRdpCameraRedirConfig** interface has these properties.

| Property         | Access type           | Description            |
|:-----------------|:----------------------|:-----------------------|
| [**DeviceExists**](imsrdpcameraredirconfig-deviceexists.md)      | Read-only | Specifies whether or not the camera device currently exists (that is, the camera is connected).   |
| [**FriendlyName**](imsrdpcameraredirconfig-friendlyname.md)                       | Read-only |    Gets the camera’s friendly name.    |
| [**InstanceId**](imsrdpcameraredirconfig-instanceid.md)      | Read-only |  Gets the instance ID of the camera.  |
| [**ParentInstanceId**](imsrdpcameraredirconfig-parentinstanceid.md)                       | Read-only |    Gets the parent device instance ID of the camera.   |
| [**Redirected**](imsrdpcameraredirconfig-redirected.md)      | Read/Write |  Specifies whether or not the camera is redirected.  |
| [**SymbolicLink**](imsrdpcameraredirconfig-symboliclink.md)                       | Read-only |   Gets the symbolic link of the **KSCATEGORY_VIDEO_CAMERA** interface for the camera.   |

## Requirements

| Requirement | Value |
|-------------------------------------|---------------------------------------|
| Minimum supported client| Windows 10, version 1803 (build 17134)      |
| Type library            | MsTscAx.dll                        |
| DLL                  | MsTscAx.dll     |
| IID                      | IID\_IMsRdpCameraRedirConfig is defined as 09750604-D625-47C1-9FCD-F09F735705D7            |

## See also

- [**IMsRdpCameraRedirConfigCollection**](imsrdpcameraredirconfigcollection.md)
- [**IMsRdpClientNonScriptable7::CameraRedirConfigCollection**](imsrdpclientnonscriptable7-cameraredirconfigcollection.md)