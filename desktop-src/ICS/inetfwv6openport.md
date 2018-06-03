---
title: INetFwV6OpenPort interface
description: The INetFwV6OpenPort interface represents a port and protocol pair for which inbound connection attempts are permitted. It is intended for use only by the open port enumerations and collections.
ms.assetid: 5c016b7d-5d4d-4645-b28c-a8fa89bda8ef
keywords:
- INetFwV6OpenPort interface ICS/ICF
- INetFwV6OpenPort interface ICS/ICF , described
topic_type:
- apiref
api_name:
- INetFwV6OpenPort
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

# INetFwV6OpenPort interface

\[The IPv6 Internet Connection Firewall is available for use in the operating systems specified in the Requirements section. Instead, use the [Windows Firewall API](windows-firewall-start-page.md).\]

The **INetFwV6OpenPort** interface represents a port and protocol pair for which inbound connection attempts are permitted. It is intended for use only by the open port enumerations and collections.

## Members

The **INetFwV6OpenPort** interface inherits from the [**IDispatch**](https://msdn.microsoft.com/windows/desktop/ebbff4bc-36b2-4861-9efa-ffa45e013eb5) interface. **INetFwV6OpenPort** also has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **INetFwV6OpenPort** interface has these methods.



| Method                                             | Description                                                 |
|:---------------------------------------------------|:------------------------------------------------------------|
| [**get\_Name**](inetfwv6openport-name.md)         | Retrieves the contents of the Name property.<br/>     |
| [**get\_Port**](inetfwv6openport-port.md)         | Retrieves the contents of the Port property.<br/>     |
| [**get\_Protocol**](inetfwv6openport-protocol.md) | Retrieves the contents of the Protocol property.<br/> |



 

### Properties

The **INetFwV6OpenPort** interface has these properties.



| Property                                                 | Description                                    |
|:---------------------------------------------------------|:-----------------------------------------------|
| [**Name**](inetfwv6openport-name.md)<br/>         | Returns display name for this pair.<br/> |
| [**Port**](inetfwv6openport-port.md)<br/>         | Returns port for this pair.<br/>         |
| [**Protocol**](inetfwv6openport-protocol.md)<br/> | Returns protocol for this pair.<br/>     |



 

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

[**IEnumNetFwV6OpenPorts::Next**](ienumnetfwv6openports-next.md)
</dt> <dt>

[**INetFwV6OpenPort::Name**](inetfwv6openport-name.md)
</dt> <dt>

[**INetFwV6OpenPort::Port**](inetfwv6openport-port.md)
</dt> <dt>

[**INetFwV6OpenPort::Protocol**](inetfwv6openport-protocol.md)
</dt> <dt>

[IUnknown](https://www.bing.com/search?q=IUnknown)
</dt> </dl>

 

 





