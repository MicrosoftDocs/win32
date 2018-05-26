---
title: INetFwV6Connection interface
description: The INetFwV6Connection interface represents an IPv6 connection, and is the main interface to perform actual configuration tasks.
ms.assetid: 80be022a-657f-4ec8-9f78-fa348f8e0c54
keywords:
- INetFwV6Connection interface ICS/ICF
- INetFwV6Connection interface ICS/ICF , described
topic_type:
- apiref
api_name:
- INetFwV6Connection
api_location:
- Netfwv6.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: interface
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# INetFwV6Connection interface

\[The IPv6 Internet Connection Firewall is available for use in the operating systems specified in the Requirements section. Instead, use the [Windows Firewall API](windows-firewall-start-page.md).\]

The **INetFwV6Connection** interface represents an IPv6 connection, and is the main interface to perform actual configuration tasks.

## Members

The **INetFwV6Connection** interface inherits from the [**IDispatch**](ebbff4bc-36b2-4861-9efa-ffa45e013eb5) interface. **INetFwV6Connection** also has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **INetFwV6Connection** interface has these methods.



| Method                                                                                | Description                                                                               |
|:--------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------|
| [**ClosePort**](inetfwv6connection-closeport.md)                                     | Closes a port.<br/>                                                                 |
| [**DisableFirewall**](inetfwv6connection-disablefirewall.md)                         | Disables the IPv6 firewall.<br/>                                                    |
| [**EnableFirewall**](inetfwv6connection-enablefirewall.md)                           | Enables the IPv6 firewall.<br/>                                                     |
| [**EnumerateIgnoredGlobalPorts**](inetfwv6connection-enumerateignoredglobalports.md) | Enumerates the set of port and protocol pairs that ignores the global setting.<br/> |
| [**EnumerateOpenPorts**](inetfwv6connection-enumerateopenports.md)                   | Enumerates the open ports.<br/>                                                     |
| [**get\_Id**](inetfwv6connection-id.md)                                              | Retrieves the contents of the Id property.<br/>                                     |
| [**get\_IgnoredGlobalPorts**](inetfwv6connection-ignoredglobalports.md)              | Retrieves a collection of ignored global ports.<br/>                                |
| [**get\_IgnoredGlobalPorts**](inetfwv6connection-ignoredglobalports.md)              | Retrieves the set of port and protocol pairs that ignore the global setting.<br/>   |
| [**get\_IsFirewalled**](inetfwv6connection-isfirewalled.md)                          | Retrieves the contents of the IsFirewalled property.<br/>                           |
| [**get\_Name**](inetfwv6connection-name.md)                                          | Retrieves the contents of the Name property.<br/>                                   |
| [**get\_OpenPorts**](inetfwv6connection-openports.md)                                | Retrieves the contents of the OpenPorts property.<br/>                              |
| [**IgnoreGlobalPort**](inetfwv6connection-ignoreglobalport.md)                       | Ignore global setting for permitting inbound connections.<br/>                      |
| [**IsPortOpen**](inetfwv6connection-isportopen.md)                                   | Indicates if the port is open.<br/>                                                 |
| [**ObserverGlobalPort**](inetfwv6connection-observeglobalport.md)                    | Allows global port and protocol setting to take precedence.<br/>                    |
| [**OpenPort**](inetfwv6connection-openport.md)                                       | Opens a port.<br/>                                                                  |



 

### Properties

The **INetFwV6Connection** interface has these properties.



| Property                                                                         | Description                                                                             |
|:---------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------|
| [**Id**](inetfwv6connection-id.md)<br/>                                   | The connection's ID (GUID).<br/>                                                  |
| [**IgnoredGlobalPorts**](inetfwv6connection-ignoredglobalports.md)<br/>   | Retrieves the set of port and protocol pairs that ignore the global setting.<br/> |
| [**IsFirewalled**](inetfwv6connection-isfirewalled.md)<br/>               | Indicates whether this connection is firewalled.<br/>                             |
| [**IsGlobalPortIgnored**](inetfwv6connection-isglobalportignored.md)<br/> | Indicates whether the global setting for this port and protocol is ignored.<br/>  |
| [**Name**](inetfwv6connection-name.md)<br/>                               | The connection's name.<br/>                                                       |
| [**OpenPorts**](inetfwv6connection-openports.md)<br/>                     | Collection of open ports.<br/>                                                    |



 

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP with SP1 \[desktop apps only\]<br/>                                   |
| Minimum supported server<br/> | None supported<br/>                                                              |
| End of client support<br/>    | Windows XP with SP1<br/>                                                         |
| Redistributable<br/>          | Advanced Networking Pack for Windows XP<br/>                                     |
| Header<br/>                   | <dl> <dt>Netfwv6.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Netfwv6.dll</dt> </dl> |



## See also

<dl> <dt>

[**IDispatch**](ebbff4bc-36b2-4861-9efa-ffa45e013eb5)
</dt> <dt>

[**IEnumNetFwV6Connections::Next**](ienumnetfwv6connections-next.md)
</dt> <dt>

[**INetFwV6Connection::ClosePort**](inetfwv6connection-closeport.md)
</dt> <dt>

[**INetFwV6Connection::DisableFirewall**](inetfwv6connection-disablefirewall.md)
</dt> <dt>

[**INetFwV6Connection::EnableFirewall**](inetfwv6connection-enablefirewall.md)
</dt> <dt>

[**INetFwV6Connection::EnumerateOpenPorts**](inetfwv6connection-enumerateopenports.md)
</dt> <dt>

[**INetFwV6Connection::Id**](inetfwv6connection-id.md)
</dt> <dt>

[**INetFwV6Connection::IsFirewalled**](inetfwv6connection-isfirewalled.md)
</dt> <dt>

[**INetFwV6Connection::IsPortOpen**](inetfwv6connection-isportopen.md)
</dt> <dt>

[**INetFwV6Connection::Name**](inetfwv6connection-name.md)
</dt> <dt>

[**INetFwV6Connection::OpenPort**](inetfwv6connection-openport.md)
</dt> <dt>

[**INetFwV6Connection::OpenPorts**](inetfwv6connection-openports.md)
</dt> <dt>

[**INetFwV6Mgr::GetConnection**](inetfwv6mgr-getconnection.md)
</dt> <dt>

[**PORT\_PROTOCOL**](port-protocol.md)
</dt> <dt>

[IUnknown](_com_iunknown)
</dt> </dl>

 

 





