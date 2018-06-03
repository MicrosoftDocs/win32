---
title: IEnumNetFwV6Connections interface
description: The IEnumNetFwV6Connections interface is a standard COM enumerator for the INetFwV6Connection interface.
ms.assetid: 4598525a-980a-4cc0-bc39-6c4fad2875ff
keywords:
- IEnumNetFwV6Connections interface ICS/ICF
- IEnumNetFwV6Connections interface ICS/ICF , described
topic_type:
- apiref
api_name:
- IEnumNetFwV6Connections
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

# IEnumNetFwV6Connections interface

\[The IPv6 Internet Connection Firewall is available for use in the operating systems specified in the Requirements section. Instead, use the [Windows Firewall API](windows-firewall-start-page.md).\]

The **IEnumNetFwV6Connections** interface is a standard COM enumerator for the [**INetFwV6Connection**](inetfwv6connection.md) interface.

## Members

The **IEnumNetFwV6Connections** interface inherits from the [**IUnknown**](https://msdn.microsoft.com/library/windows/desktop/ms680509) interface. **IEnumNetFwV6Connections** also has these types of members:

-   [Methods](#methods)

### Methods

The **IEnumNetFwV6Connections** interface has these methods.



| Method                                         | Description                                             |
|:-----------------------------------------------|:--------------------------------------------------------|
| [**Clone**](ienumnetfwv6connections-clone.md) | Clones the enumerator.<br/>                       |
| [**Next**](ienumnetfwv6connections-next.md)   | Gets the next connection in the enumerator.<br/>  |
| [**Reset**](ienumnetfwv6connections-reset.md) | Resets the enumerator.<br/>                       |
| [**Skip**](ienumnetfwv6connections-skip.md)   | Skips the next connection in the enumerator.<br/> |



 

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

[**IEnumNetFwV6Connections::Clone**](ienumnetfwv6connections-clone.md)
</dt> <dt>

[**IEnumNetFwV6Connections::Next**](ienumnetfwv6connections-next.md)
</dt> <dt>

[**IEnumNetFwV6Connections::Reset**](ienumnetfwv6connections-reset.md)
</dt> <dt>

[**IEnumNetFwV6Connections::Skip**](ienumnetfwv6connections-skip.md)
</dt> <dt>

[**INetFwV6ConnectionCollection::\_NewEnum**](https://msdn.microsoft.com/library/windows/desktop/aa365818)
</dt> <dt>

[**INetFwV6Mgr::EnumerateConnections**](inetfwv6mgr-enumerateconnections.md)
</dt> <dt>

[**INetFwV6OpenPortsCollection::\_NewEnum**](inetfwv6openportscollection-newenum.md)
</dt> <dt>

[IUnknown](https://www.bing.com/search?q=IUnknown)
</dt> </dl>

 

 





