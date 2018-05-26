---
title: INetFwV6OpenPortsCollection interface
description: The INetFwV6OpenPortsCollection interface is a standard Automation collection for the INetFwV6OpenPort interface.
ms.assetid: 2e8062fc-a91a-4ceb-9529-b38e3fd90eb5
keywords:
- INetFwV6OpenPortsCollection interface ICS/ICF
- INetFwV6OpenPortsCollection interface ICS/ICF , described
topic_type:
- apiref
api_name:
- INetFwV6OpenPortsCollection
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

# INetFwV6OpenPortsCollection interface

\[The IPv6 Internet Connection Firewall is available for use in the operating systems specified in the Requirements section. Instead, use the [Windows Firewall API](windows-firewall-start-page.md).\]

The **INetFwV6OpenPortsCollection** interface is a standard Automation collection for the [**INetFwV6OpenPort**](inetfwv6openport.md) interface.

## Members

The **INetFwV6OpenPortsCollection** interface inherits from the [**IDispatch**](ebbff4bc-36b2-4861-9efa-ffa45e013eb5) interface. **INetFwV6OpenPortsCollection** also has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **INetFwV6OpenPortsCollection** interface has these methods.



| Method                                                        | Description                                              |
|:--------------------------------------------------------------|:---------------------------------------------------------|
| [**get\_\_NewEnum**](inetfwv6openportscollection-newenum.md) | Retrieves an enumerator for the collection.<br/>   |
| [**get\_Count**](inetfwv6openportscollection-count.md)       | Retrieves the contents of the Count property.<br/> |



 

### Properties

The **INetFwV6OpenPortsCollection** interface has these properties.



| Property                                                            | Description                                       |
|:--------------------------------------------------------------------|:--------------------------------------------------|
| [**\_NewEnum**](inetfwv6openportscollection-newenum.md)<br/> | Gets an enumerator for the collection.<br/> |
| [**Count**](inetfwv6openportscollection-count.md)<br/>       | Gets the count for the collection.<br/>     |



 

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

[**INetFwV6Connection::OpenPorts**](inetfwv6connection-openports.md)
</dt> <dt>

[**INetFwV6OpenPortsCollection::\_NewEnum**](inetfwv6openportscollection-newenum.md)
</dt> <dt>

[**INetFwV6OpenPortsCollection::Count**](inetfwv6openportscollection-count.md)
</dt> <dt>

[IUnknown](_com_iunknown)
</dt> </dl>

 

 





