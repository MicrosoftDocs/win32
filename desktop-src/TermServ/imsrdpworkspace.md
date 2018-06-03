---
title: IMsRdpWorkspace interface
description: Exposes methods that manage RemoteApp and Desktop Connection credentials and connections.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: cddcdfc2-b30a-4d00-84c2-ad036ab6288f
ms.prod: windows-server-dev
ms.technology: remote-desktop-services
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
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# IMsRdpWorkspace interface

Exposes methods that manage RemoteApp and Desktop Connection credentials and connections. This interface is implemented by the Remote Desktop Services Web Access Control. This control is a wrapper around the Remote Desktop Connection client (MsTscAx.dll) and the RemoteApp and Desktop Connections runtime proxy (Tswbprxy.exe).

## Members

The **IMsRdpWorkspace** interface inherits from the [**IDispatch**](https://msdn.microsoft.com/windows/desktop/ebbff4bc-36b2-4861-9efa-ffa45e013eb5) interface. **IMsRdpWorkspace** also has these types of members:

-   [Methods](#methods)

### Methods

The **IMsRdpWorkspace** interface has these methods.



| Method                                                                                   | Description                                                                                                                                                           |
|:-----------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**ClearWorkspaceCredential**](/windows/desktop/api/workspaceruntime/)             | Deletes the user credentials associated with the specified connection ID.<br/>                                                                                  |
| [**DisconnectWorkspace**](/windows/desktop/api/workspaceruntime/)                       | Disconnects all existing connections associated with the specified connection ID and deletes the corresponding user credentials from the credential store.<br/> |
| [**IsWorkspaceCredentialSpecified**](/windows/desktop/api/workspaceruntime/) | Determines whether user credentials exist for the specified connection ID.<br/>                                                                                 |
| [**IsWorkspaceSSOEnabled**](/windows/desktop/api/workspaceruntime/)                   | Determines whether single sign on (SSO) is enabled for RemoteApp and Desktop Connection.<br/>                                                                   |
| [**OnAuthenticated**](/windows/desktop/api/workspaceruntime/)                               | Marks the authentication of user credentials for the connection ID, and subsequently shows the connect notification in the taskbar notification area. <br/>     |
| [**StartWorkspace**](/windows/desktop/api/workspaceruntime/)                                 | Associates user credentials and certificates with a connection ID.<br/>                                                                                         |



 

## Requirements



|                                     |                                                                                               |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7<br/>                                                                          |
| Minimum supported server<br/> | Windows Server 2008 R2<br/>                                                             |
| DLL<br/>                      | <dl> <dt>MsRdpWebAccess.dll</dt> </dl> |
| IID<br/>                      | IID\_IMsRdpWorkspace is defined as 145D0621-04CF-4FC2-A766-A81A9069CDF8<br/>            |



## See also

<dl> <dt>

[**IMsRdpClientShell2**](imsrdpclientshell2.md)
</dt> </dl>

 

 





