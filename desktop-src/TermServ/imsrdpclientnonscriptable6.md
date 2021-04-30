---
title: IMsRdpClientNonScriptable6 interface
description: Provides access to the nonscriptable properties of a client's remote session on the Remote Desktop ActiveX control. Derives from the IMsRdpClientNonScriptable5 interface.
ms.tgt_platform: multiple
keywords:
- IMsRdpClientNonScriptable6 interface Remote Desktop Services
- IMsRdpClientNonScriptable6 interface Remote Desktop Services , described
topic_type:
- apiref
api_name:
- IMsRdpClientNonScriptable6
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 12/16/2020
---

# IMsRdpClientNonScriptable6 interface

Provides access to the nonscriptable properties of a client's remote session on the Remote Desktop ActiveX control. Derives from the [**IMsRdpClientNonScriptable5**](imsrdpclientnonscriptable5.md) interface. Methods of this interface can only be accessed through the vtable; they are not available for use to scriptable clients.

An instance of this interface is obtained by calling [**QueryInterface**](/windows/desktop/api/unknwn/nf-unknwn-iunknown-queryinterface(q)) on the [**IMsTscAx**](imstscax-interface.md) object, passing **IID\_IMsRdpClientNonScriptable6**.

## Members

The **IMsRdpClientNonScriptable6** interface inherits from [**IMsRdpClientNonScriptable5**](imsrdpclientnonscriptable5.md). **IMsRdpClientNonScriptable6** also has these types of members:

- [Methods](#methods)

### Methods

The **IMsRdpClientNonScriptable6** interface has these methods.


| Method            | Description                   |
|:-----------------------------|:-----------------|
| [**SendLocation2D**](imsrdpclientnonscriptable6-sendlocation2d.md)     |  Sends a latitude and longitude value to the server so the client’s geographic location can be reflected in the remote session.                   |
| [**SendLocation3D**](imsrdpclientnonscriptable6-sendlocation3d.md)     | Sends a latitude, longitude and altitude value to the server so the client’s geographic location can be reflected in the remote session.                 |

## Requirements

| Requirement | Value |
|-------------------------------------|---------------------------------------|
| Minimum supported client| Windows 10, version 1709 (build 16299)      |
| Type library            | MsTscAx.dll                        |
| DLL                  | MsTscAx.dll     |
| CLSID                    | CLSID\_MsRdpClient12 is defined as 0BDA33B8-9AF1-4065-989E-5A7F1ACF09D8<br/> CLSID\_MsRdpClient12NotSafeForScripting is defined as 3BB805C2-D9E2-4174-8A1E-C87D69563662<br/> CLSID\_MsRdpClient11 is defined as 22A7E88C-5BF5-4DE6-B687-60F7331DF190<br/> CLSID\_MsRdpClient11NotSafeForScripting is defined as 1DF7C823-B2D4-4B54-975A-F2AC5D7CF8B8<br/>  |
| IID                      | IID\_IMsRdpClientNonScriptable6 is defined as 05293249-B28B-4DB8-BE64-1B2F496B910E            |

## See also

<dl> <dt>

[**IMsRdpClientNonScriptable5**](imsrdpclientnonscriptable5.md)
</dt> </dl>
