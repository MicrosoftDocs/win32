---
title: IMsRdpClientNonScriptable8 interface
description: Provides access to the nonscriptable properties of a client's remote session on the Remote Desktop ActiveX control. Derives from the IMsRdpClientNonScriptable7 interface.
ms.tgt_platform: multiple
keywords:
- IMsRdpClientNonScriptable8 interface Remote Desktop Services
- IMsRdpClientNonScriptable8 interface Remote Desktop Services , described
topic_type:
- apiref
api_name:
- IMsRdpClientNonScriptable8
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 09/12/2023
---

# IMsRdpClientNonScriptable8 interface

Provides access to the nonscriptable properties of a client's remote session on the Remote Desktop ActiveX control. Derives from the [**IMsRdpClientNonScriptable7**](imsrdpclientnonscriptable7.md) interface. Methods of this interface can only be accessed through the vtable; they are not available for use to scriptable clients.

An instance of this interface is obtained by calling [**QueryInterface**](/windows/desktop/api/unknwn/nf-unknwn-iunknown-queryinterface(q)) on the [**IMsTscAx**](imstscax-interface.md) object, passing **IID\_IMsRdpClientNonScriptable8**.

## Members

The **IMsRdpClientNonScriptable8** interface inherits from [**IMsRdpClientNonScriptable6**](imsrdpclientnonscriptable5.md). **IMsRdpClientNonScriptable8** also has these types of members:

- [Methods](#methods)
- [Properties](#properties)

### Methods

The **IMsRdpClientNonScriptable8** interface has these methods.


| Method            | Description              |
|:------------------|:-------------------------|
| [**StartWorkspaceExtension**](imsrdpclientnonscriptable8-startworkspaceextension.md)       |  Coordinates the client's remote session with the RemoteApp and Desktop Connections control panel. |

### Properties

The **IMsRdpClientNonScriptable8** interface has these properties.

| Property         | Access type           | Description            |
|:-----------------|:----------------------|:-----------------------|
| [**CorrelationId**](imsrdpclientnonscriptable8-correlationid.md)      | Read-only |  Gets a GUID uniquely identifying the client's remote session.   |
| [**SupportsWorkspaceReconnect**](imsrdpclientnonscriptable8-supportsworkspacereconnect.md)                       | Write-only |    Informs the Remote Desktop ActiveX control that the client's remote session is part of a connection in the RemoteApp and Desktop Connections control panel that supports reconnect.     |

## Requirements

| Requirement | Value |
|-------------------------------------|---------------------------------------|
| Minimum supported client| Windows 11 Version 23H2      |
| Type library            | MsTscAx.dll                        |
| DLL                  | MsTscAx.dll     |
| IID                      | IID\_IMsRdpClientNonScriptable8 is defined as B2B3FA47-3F11-4148-AD24-DFF8684A16D0            |

## See also

<dl> <dt>

[**IMsRdpClientNonScriptable6**](imsrdpclientnonscriptable6.md)
</dt> </dl>
