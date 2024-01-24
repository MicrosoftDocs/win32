---
title: IMsRdpWorkspace interface
description: Exposes methods that manage RemoteApp and Desktop Connection credentials and connections.
ms.assetid: cddcdfc2-b30a-4d00-84c2-ad036ab6288f
ms.tgt_platform: multiple
keywords:
- IMsRdpWorkspace interface Remote Desktop Services
- IMsRdpWorkspace interface Remote Desktop Services , described
topic_type:
- apiref
api_name:
- IMsRdpWorkspace
api_location:
- MsRdpWebAccess.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IMsRdpWorkspace interface

Exposes methods that manage RemoteApp and Desktop Connection credentials and connections. This interface is implemented by the Remote Desktop Services Web Access Control. This control is a wrapper around the Remote Desktop Connection client (MsTscAx.dll) and the RemoteApp and Desktop Connections runtime proxy (Tswbprxy.exe).

## Members

The **IMsRdpWorkspace** interface inherits from the [**IDispatch**](/windows/win32/api/oaidl/nn-oaidl-idispatch) interface. **IMsRdpWorkspace** also has these types of members:

-   [Methods](#methods)

### Methods

The **IMsRdpWorkspace** interface has these methods.



| Method                                                                                   | Description                                                                                                                                                           |
|:-----------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**ClearWorkspaceCredential**](/previous-versions/windows/desktop/legacy/ee351596(v=vs.85))             | Deletes the user credentials associated with the specified connection ID.<br/>                                                                                  |
| [**DisconnectWorkspace**](/previous-versions/windows/desktop/legacy/ee351597(v=vs.85))                       | Disconnects all existing connections associated with the specified connection ID and deletes the corresponding user credentials from the credential store.<br/> |
| [**IsWorkspaceCredentialSpecified**](/previous-versions/windows/desktop/legacy/ee351598(v=vs.85)) | Determines whether user credentials exist for the specified connection ID.<br/>                                                                                 |
| [**IsWorkspaceSSOEnabled**](/previous-versions/windows/desktop/legacy/ee351599(v=vs.85))                   | Determines whether single sign on (SSO) is enabled for RemoteApp and Desktop Connection.<br/>                                                                   |
| [**OnAuthenticated**](/previous-versions/windows/desktop/legacy/ee351600(v=vs.85))                               | Marks the authentication of user credentials for the connection ID, and subsequently shows the connect notification in the taskbar notification area. <br/>     |
| [**StartWorkspace**](/previous-versions/windows/desktop/legacy/ee351601(v=vs.85))                                 | Associates user credentials and certificates with a connection ID.<br/>                                                                                         |



 

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7<br/>                                                                          |
| Minimum supported server<br/> | Windows Server 2008 R2<br/>                                                             |
| DLL<br/>                      | <dl> <dt>MsRdpWebAccess.dll</dt> </dl> |
| IID<br/>                      | IID\_IMsRdpWorkspace is defined as 145D0621-04CF-4FC2-A766-A81A9069CDF8<br/>            |



## See also

<dl> <dt>

[**IMsRdpClientShell2**](imsrdpclientshell2.md)
</dt> </dl>

 

