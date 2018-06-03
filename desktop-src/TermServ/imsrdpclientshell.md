---
title: IMsRdpClientShell interface
description: Remote Desktop Connection (RDC) client settings that are used to launch the client from Remote Desktop Web Access (RD Web Access) or from other web portals.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 05ca2e90-656a-40a3-a438-29d7985e9feb
ms.prod: windows-server-dev
ms.technology: remote-desktop-services
ms.tgt_platform: multiple
keywords:
- IMsRdpClientShell interface Remote Desktop Services
- IMsRdpClientShell interface Remote Desktop Services , described
topic_type:
- apiref
api_name:
- IMsRdpClientShell
api_location:
- MsTscAx.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# IMsRdpClientShell interface

Remote Desktop Connection (RDC) client settings that are used to launch the client from Remote Desktop Web Access (RD Web Access) or from other web portals.

## Members

The **IMsRdpClientShell** interface inherits from the [**IDispatch**](https://msdn.microsoft.com/windows/desktop/ebbff4bc-36b2-4861-9efa-ffa45e013eb5) interface. **IMsRdpClientShell** also has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **IMsRdpClientShell** interface has these methods.



| Method                                                     | Description                                                  |
|:-----------------------------------------------------------|:-------------------------------------------------------------|
| [**GetRdpProperty**](/windows/desktop/api/rdpappcontainerclient/) | Retrieves a single RDP property.<br/>                  |
| [**Launch**](imsrdpclientshell-launch.md)                 | Launches remote file content from the web portal.<br/> |
| [**SetRdpProperty**](/windows/desktop/api/rdpappcontainerclient/) | Sets a single RDP property.<br/>                       |



 

### Properties

The **IMsRdpClientShell** interface has these properties.



| Property                                                                                              | Access type           | Description                                                                                               |
|:------------------------------------------------------------------------------------------------------|:----------------------|:----------------------------------------------------------------------------------------------------------|
| [**IsRemoteProgramClientInstalled**](imsrdpclientshell-isremoteprogramclientinstalled.md)<br/> | Read-only<br/>  | Retrieves whether the Remote Desktop Connection (RDC) client supports RemoteApp functionality.<br/> |
| [**PublicMode**](imsrdpclientshell-publicmode.md)<br/>                                         | Read/write<br/> | Retrieves whether public mode is enabled.<br/>                                                      |
| [**RdpFileContents**](imsrdpclientshell-rdpfilecontents.md)<br/>                               | Read/write<br/> | Stream version of the RDP configuration file.<br/>                                                  |



 

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                         |
| Type library<br/>             | <dl> <dt>MsTscAx.dll</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsTscAx.dll</dt> </dl> |
| IID<br/>                      | IID\_IMsRdpClientShell is defined as d012ae6d-c19a-4bfe-b367-201f8911f134<br/>   |



## See also

<dl> <dt>

[**IDispatch**](https://msdn.microsoft.com/windows/desktop/ebbff4bc-36b2-4861-9efa-ffa45e013eb5)
</dt> <dt>

[Remote Desktop Web Connection Reference](remote-desktop-web-connection-reference.md)
</dt> </dl>

 

 





