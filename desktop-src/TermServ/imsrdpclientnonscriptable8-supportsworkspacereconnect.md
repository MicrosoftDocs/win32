---
title: IMsRdpClientNonScriptable8 SupportsWorkspaceReconnect property
description: Informs the Remote Desktop ActiveX control that the client's remote session is part of a connection in the RemoteApp and Desktop Connections control panel that supports reconnect.
ms.tgt_platform: multiple
keywords:
- SupportsWorkspaceReconnect property Remote Desktop Services
- SupportsWorkspaceReconnect property Remote Desktop Services , IMsRdpClientNonScriptable8 interface
- IMsRdpClientNonScriptable8 interface Remote Desktop Services , SupportsWorkspaceReconnect property
topic_type:
- apiref
api_name:
- IMsRdpClientNonScriptable8.SupportsWorkspaceReconnect
- IMsRdpClientNonScriptable8.get_SupportsWorkspaceReconnect
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 09/12/2023
---

# IMsRdpClientNonScriptable8::SupportsWorkspaceReconnect property

Informs the Remote Desktop ActiveX control that the client's remote session is part of a connection in the RemoteApp and Desktop Connections control panel that supports reconnect. This avoids showing redundant dialogs when a reconnection is triggered from the RemoteApp and Desktop Connection control panel as they can contain remote sessions in multiple computers.

The RemoteApp and Desktop Connections control panel is no longer in active development. It may be altered or unavailable in future versions of Windows. The use of this API is discouraged.

The property is write-only. By default, this is disabled.


## Syntax

```C++
HRESULT put_SupportsWorkspaceReconnect(
    [in] VARIANT_BOOL supportsReconnect
);
```

## Property value

`VARIANT_TRUE` if the connection in the RemoteApp and Desktop Connections control panel supports reconnect; otherwise, `VARIANT_FALSE`.

## Requirements

| Requirement | Value |
|-------------------------------------|---------------------------------------|
| Minimum supported client| Windows 11 Version 23H2      |
| Type library            | MsTscAx.dll                        |
| DLL                  | MsTscAx.dll     |
| IID                      | IID\_IMsRdpClientNonScriptable8 is defined as B2B3FA47-3F11-4148-AD24-DFF8684A16D0           |

## See also

<dl> <dt>

[**IMsRdpClientNonScriptable8**](IMsRdpClientNonScriptable8.md)
</dt> </dl>