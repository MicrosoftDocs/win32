---
title: IMsRdpClientNonScriptable8 StartWorkspaceExtension method
description: Coordinates the client's remote session with the RemoteApp and Desktop Connections control panel.
ms.tgt_platform: multiple
keywords:
- StartWorkspaceExtension method Remote Desktop Services
- StartWorkspaceExtension method Remote Desktop Services, IMsRdpClientNonScriptable8 interface
- IMsRdpClientNonScriptable8 interface Remote Desktop Services, StartWorkspaceExtension method
topic_type:
- apiref
api_name:
- IMsRdpClientNonScriptable8.StartWorkspaceExtension
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 09/12/2023
---

# IMsRdpClientNonScriptable8::StartWorkspaceExtension method

Coordinates the client's remote session with the RemoteApp and Desktop Connections control panel.

> [!NOTE]
> The RemoteApp and Desktop Connections control panel is no longer in active development. It may be altered or unavailable in future versions of Windows. The use of this API is discouraged. 


## Syntax

```C++
HRESULT StartWorkspaceExtension( 
    [in] VARIANT_BOOL isWebHosted,
    [in] BSTR workspaceId,
    [in] BYTE *publisherThumbPrint,
    [in] UINT publisherThumbPrintLength
);
```

## Parameters

### isWebHosted

A value indicating whether the connection is hosted from a website.

### workspaceId

A string that contains the ID of a connection in the RemoteApp and Desktop Connections control panel.

### publisherThumbPrint

An array of bytes representing the thumbprint in binary format to pass to [IWorkspaceScriptable3::StartWorkspaceEx2](/windows/win32/api/workspaceruntime/nf-workspaceruntime-iworkspacescriptable3-startworkspaceex2) as *bstrWorkspaceParams*. See Remarks.

### publisherThumbPrintLength

The number of bytes pointed to by *publisherThumbPrint*.

## Return value

Return **S\_OK** if successful.

## Remarks

This function handles the following scenarios:

* Upon connection with the remote session:
  * After prompting the user for credentials, it associates them with a connection in the RemoteApp and Desktop Connections control panel via **IWorkspaceScriptable3::StartWorkspaceEx2**
  * It notifies the RemoteApp and Desktop Connections control panel of the existence of the remote session via [IWorkspaceRegistration2::AddResourceEx](/windows/win32/api/workspaceruntime/nf-workspaceruntime-iworkspaceregistration2-addresourceex).
* Upon disconnection from the remote session:
  * It alerts the user that the remote session has been dismissed via [IWorkspaceScriptable2::ResourceDismissed](/windows/win32/api/workspaceruntime/nf-workspaceruntime-iworkspacescriptable2-resourcedismissed)
  * It notifies the RemoteApp and Desktop Connections control panel of the disconnection via [IWorkspaceRegistration2::RemoveResourceEx](/windows/win32/api/workspaceruntime/nf-workspaceruntime-iworkspaceregistration2-removeresourceex).


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
