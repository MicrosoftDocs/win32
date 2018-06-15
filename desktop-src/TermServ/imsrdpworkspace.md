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

The **IMsRdpWorkspace** interface inherits from the [**IDispatch**](https://msdn.microsoft.com/en-us/library/ms221608(v=VS.71).aspx) interface. **IMsRdpWorkspace** also has these types of members:

-   [Methods](#methods)

### Methods

The **IMsRdpWorkspace** interface has these methods.



| Method                                                                                   | Description                                                                                                                                                           |
|:-----------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**ClearWorkspaceCredential**](https://msdn.microsoft.com/en-us/library/Ee351596(v=VS.85).aspx)             | Deletes the user credentials associated with the specified connection ID.<br/>                                                                                  |
| [**DisconnectWorkspace**](https://msdn.microsoft.com/en-us/library/Ee351597(v=VS.85).aspx)                       | Disconnects all existing connections associated with the specified connection ID and deletes the corresponding user credentials from the credential store.<br/> |
| [**IsWorkspaceCredentialSpecified**](https://msdn.microsoft.com/en-us/library/Ee351598(v=VS.85).aspx) | Determines whether user credentials exist for the specified connection ID.<br/>                                                                                 |
| [**IsWorkspaceSSOEnabled**](https://msdn.microsoft.com/en-us/library/Ee351599(v=VS.85).aspx)                   | Determines whether single sign on (SSO) is enabled for RemoteApp and Desktop Connection.<br/>                                                                   |
| [**OnAuthenticated**](https://msdn.microsoft.com/en-us/library/Ee351600(v=VS.85).aspx)                               | Marks the authentication of user credentials for the connection ID, and subsequently shows the connect notification in the taskbar notification area. <br/>     |
| [**StartWorkspace**](https://msdn.microsoft.com/en-us/library/Ee351601(v=VS.85).aspx)                                 | Associates user credentials and certificates with a connection ID.<br/>                                                                                         |



 

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

 

 





