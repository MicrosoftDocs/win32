---
title: INetFwV6Mgr interface
description: The INetFwV6Mgr is the entry point interface for the IPv6 Internet Connection Firewall Configuration API.
ms.assetid: 9f7f1f03-f951-4017-9112-7452b879413f
keywords:
- INetFwV6Mgr interface ICS/ICF
- INetFwV6Mgr interface ICS/ICF , described
topic_type:
- apiref
api_name:
- INetFwV6Mgr
api_location:
- Netfwv6.dll
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# INetFwV6Mgr interface

\[The IPv6 Internet Connection Firewall is available for use in the operating systems specified in the Requirements section. Instead, use the [Windows Firewall API](windows-firewall-start-page.md).\]

The **INetFwV6Mgr** is the entry point interface for the IPv6 Internet Connection Firewall Configuration API. A caller can obtain this interface by creating an object with CLSID CLSID\_NetFwV6Mgr. This is the only interface for which there is an object that can be created; all other interfaces can only be obtained through method calls within the API's object model.

## Members

The **INetFwV6Mgr** interface inherits from the [**IDispatch**](https://msdn.microsoft.com/windows/desktop/ebbff4bc-36b2-4861-9efa-ffa45e013eb5) interface. **INetFwV6Mgr** also has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **INetFwV6Mgr** interface has these methods.



| Method                                                                       | Description                                                                           |
|:-----------------------------------------------------------------------------|:--------------------------------------------------------------------------------------|
| [**CloseGlobalPort**](inetfwv6mgr-closeglobalport.md)                       | Closes a firewall port/protocol.<br/>                                           |
| [**EnumerateConnections**](inetfwv6mgr-enumerateconnections.md)             | Enumerates IPv6 connections.<br/>                                               |
| [**EnumerateGloballyOpenPorts**](inetfwv6mgr-enumerategloballyopenports.md) | Returns an enumerator of globally open port/protocol pairs.<br/>                |
| [**get\_Connections**](inetfwv6mgr-connections.md)                          | Retrieves the contents of the Connections property.<br/>                        |
| [**get\_GloballyOpenPorts**](inetfwv6mgr-globallyopenports.md)              | Retrieves a collection of the port/protocol pairs which are globally open.<br/> |
| [**get\_LogConnections**](inetfwv6mgr-logconnections.md)                    | Retrieves the contents of the LogConnections property.<br/>                     |
| [**get\_LogDroppedPackets**](inetfwv6mgr-logdroppedpackets.md)              | Retrieves the contents of the LogDroppedPackets property.<br/>                  |
| [**get\_LogfileMaximumSize**](inetfwv6mgr-logfilemaximumsize.md)            | Retrieves the contents of the LogfileMaximumSize property.<br/>                 |
| [**get\_LogfilePath**](inetfwv6mgr-logfilepath.md)                          | Retrieves the contents of the LogfilePath property.<br/>                        |
| [**GetConnection**](inetfwv6mgr-getconnection.md)                           | Retrieves an IPv6 connection given its ID.<br/>                                 |
| [**IsPortGloballyOpen**](inetfwv6mgr-isportgloballyopen.md)                 | Tests if inbound connections are allowed.<br/>                                  |
| [**OpenGlobalPort**](inetfwv6mgr-openglobalport.md)                         | Opens a firewall port/protocol for inbound connections.<br/>                    |
| [**put LogfilePath**](inetfwv6mgr-logfilepath.md)                           | Sets the contents of the LogfilePath property.<br/>                             |
| [**put\_LogConnections**](inetfwv6mgr-logconnections.md)                    | Sets the contents of the LogConnections property.<br/>                          |
| [**put\_LogDroppedPackets**](inetfwv6mgr-logdroppedpackets.md)              | Sets the contents of the LogDroppedPackets property.<br/>                       |
| [**put\_LogfileMaximumSize**](inetfwv6mgr-logfilemaximumsize.md)            | Sets the contents of the LogfileMaximumSize property.<br/>                      |



 

### Properties

The **INetFwV6Mgr** interface has these properties.



| Property                                                                | Access type           | Description                                                                                                        |
|:------------------------------------------------------------------------|:----------------------|:-------------------------------------------------------------------------------------------------------------------|
| [**Connections**](inetfwv6mgr-connections.md)<br/>               | Read-only<br/>  | Access a collection of the IPv6 connections.<br/> (Inherited from **INetFwV6Mgr**)                           |
| [**GloballyOpenPorts**](inetfwv6mgr-globallyopenports.md)<br/>   | Read-only<br/>  | Access a collection of the port/protocol pairs that are globally open.<br/> (Inherited from **INetFwV6Mgr**) |
| [**LogConnections**](inetfwv6mgr-logconnections.md)<br/>         | Read/write<br/> | Enables or disables the logging of connection information.<br/> (Inherited from **INetFwV6Mgr**)             |
| [**LogDroppedPackets**](inetfwv6mgr-logdroppedpackets.md)<br/>   | Read/write<br/> | Enables or disables the logging of dropped packets.<br/> (Inherited from **INetFwV6Mgr**)                    |
| [**LogfileMaximumSize**](inetfwv6mgr-logfilemaximumsize.md)<br/> | Read/write<br/> | Sets the maximum size for log file.<br/> (Inherited from **INetFwV6Mgr**)                                    |
| [**LogfilePath**](inetfwv6mgr-logfilepath.md)<br/>               | Read/write<br/> | Sets the path of the log file.<br/> (Inherited from **INetFwV6Mgr**)                                         |



 

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

[**IDispatch**](https://msdn.microsoft.com/windows/desktop/ebbff4bc-36b2-4861-9efa-ffa45e013eb5)
</dt> <dt>

[**INetFwV6Mgr.Connections**](inetfwv6mgr-connections.md)
</dt> <dt>

[**INetFwV6Mgr::EnumerateConnections**](inetfwv6mgr-enumerateconnections.md)
</dt> <dt>

[**INetFwV6Mgr::GetConnection**](inetfwv6mgr-getconnection.md)
</dt> <dt>

[**INetFwV6Mgr.LogConnections**](inetfwv6mgr-logconnections.md)
</dt> <dt>

[**INetFwV6Mgr.LogDroppedPackets**](inetfwv6mgr-logdroppedpackets.md)
</dt> <dt>

[**INetFwV6Mgr.LogfilePath**](inetfwv6mgr-logfilepath.md)
</dt> <dt>

[**INetFwV6Mgr.LogfileMaximumSize**](inetfwv6mgr-logfilemaximumsize.md)
</dt> <dt>

[IUnknown](https://www.bing.com/search?q=IUnknown)
</dt> </dl>

 

 





