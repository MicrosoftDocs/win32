---
title: IMsRdpWorkspace2 interface
description: Exposes a method that associates RemoteApp and Desktop Connection credentials with a connection.
ms.assetid: 7E09AF14-2D6C-4D6E-8033-C691D9DC8057
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

# IMsRdpWorkspace2 interface

Exposes a method that associates RemoteApp and Desktop Connection credentials with a connection. This interface is implemented by the Remote Desktop Services Web Access Control. This control is a wrapper around the Remote Desktop Connection client (MsTscAx.dll) and the RemoteApp and Desktop Connections runtime proxy (Tswbprxy.exe).

## Members

The **IMsRdpWorkspace** interface inherits from [**IMsRdpWorkspace**](imsrdpworkspace.md). **IMsRdpWorkspace2** also has these types of members:

-   [Methods](#methods)

### Methods

The **IMsRdpWorkspace** interface has these methods.



| Method                                                        | Description                                                                    |
|:--------------------------------------------------------------|:-------------------------------------------------------------------------------|
| [**StartWorkspaceEx**](/previous-versions/windows/desktop/legacy/dn123459(v=vs.85)) | Associates user credentials and certificates with a connection ID. <br/> |



 

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                          |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                |
| DLL<br/>                      | <dl> <dt>MsRdpWebAccess.dll</dt> </dl> |
| IID<br/>                      | IID\_IMsRdpWorkspace2 is defined as 145D0622-04CF-4FC3-A776-A82A9169CDF8<br/>           |



## See also

<dl> <dt>

[**IMsRdpClientShell2**](imsrdpclientshell2.md)
</dt> <dt>

[**IMsRdpWorkspace**](imsrdpworkspace.md)
</dt> </dl>

 

