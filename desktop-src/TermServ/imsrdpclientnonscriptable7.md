---
title: IMsRdpClientNonScriptable7 interface
description: Provides access to the nonscriptable properties of a client's remote session on the Remote Desktop ActiveX control. Derives from the IMsRdpClientNonScriptable6 interface.
ms.tgt_platform: multiple
keywords:
- IMsRdpClientNonScriptable7 interface Remote Desktop Services
- IMsRdpClientNonScriptable7 interface Remote Desktop Services , described
topic_type:
- apiref
api_name:
- IMsRdpClientNonScriptable7
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 12/16/2020
---

# IMsRdpClientNonScriptable7 interface

Provides access to the nonscriptable properties of a client's remote session on the Remote Desktop ActiveX control. Derives from the [**IMsRdpClientNonScriptable6**](imsrdpclientnonscriptable6.md) interface. Methods of this interface can only be accessed through the vtable; they are not available for use to scriptable clients.

An instance of this interface is obtained by calling [**QueryInterface**](/windows/desktop/api/unknwn/nf-unknwn-iunknown-queryinterface(q)) on the [**IMsTscAx**](imstscax-interface.md) object, passing **IID\_IMsRdpClientNonScriptable7**.

## Members

The **IMsRdpClientNonScriptable7** interface inherits from [**IMsRdpClientNonScriptable6**](imsrdpclientnonscriptable5.md). **IMsRdpClientNonScriptable7** also has these types of members:

- [Methods](#methods)
- [Properties](#properties)

### Methods

The **IMsRdpClientNonScriptable7** interface has these methods.


| Method            | Description              |
|:------------------|:-------------------------|
| [**DisableDpiCursorScalingForProcess**](imsrdpclientnonscriptable7-disabledpicursorscalingforprocess.md)       |  Disables local scaling of the mouse cursor received from the server, ensuring that the cursor shape is rendered correctly without modification.                   |

### Properties

The **IMsRdpClientNonScriptable7** interface has these properties.

| Property         | Access type           | Description            |
|:-----------------|:----------------------|:-----------------------|
| [**CameraRedirConfigCollection**](imsrdpclientnonscriptable7-cameraredirconfigcollection.md)      | Read-only |  Gets the collection of cameras (and the associated configurations) that are available for redirection.   |
| [**Clipboard**](imsrdpclientnonscriptable7-clipboard.md)                       | Read-only |    Gets the Clipboard controller used to synchronize the local and remote clipboards if manual clipboard sync is enabled.    |

## Requirements

| Requirement | Value |
|-------------------------------------|---------------------------------------|
| Minimum supported client| Windows 10, version 1803 (build 17134)      |
| Type library            | MsTscAx.dll                        |
| DLL                  | MsTscAx.dll     |
| CLSID                    | CLSID\_MsRdpClient12 is defined as 0BDA33B8-9AF1-4065-989E-5A7F1ACF09D8<br/> CLSID\_MsRdpClient12NotSafeForScripting is defined as 3BB805C2-D9E2-4174-8A1E-C87D69563662<br/> CLSID\_MsRdpClient11 is defined as 22A7E88C-5BF5-4DE6-B687-60F7331DF190<br/> CLSID\_MsRdpClient11NotSafeForScripting is defined as 1DF7C823-B2D4-4B54-975A-F2AC5D7CF8B8<br/>  |
| IID                      | IID\_IMsRdpClientNonScriptable7 is defined as 71B4A60A-FE21-46D8-A39B-8E32BA0C5ECC            |

## See also

<dl> <dt>

[**IMsRdpClientNonScriptable6**](imsrdpclientnonscriptable6.md)
</dt> </dl>
