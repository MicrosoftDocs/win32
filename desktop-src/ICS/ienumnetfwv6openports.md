---
title: IEnumNetFwV6OpenPorts interface
description: The IEnumNetFwV6OpenPorts interface is a standard COM enumerator for the INetFwV6OpenPort interface.
ms.assetid: 1723454e-c22d-44a8-9860-198a584653ef
keywords:
- IEnumNetFwV6OpenPorts interface ICS/ICF
- IEnumNetFwV6OpenPorts interface ICS/ICF , described
topic_type:
- apiref
api_name:
- IEnumNetFwV6OpenPorts
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

# IEnumNetFwV6OpenPorts interface

\[The IPv6 Internet Connection Firewall is available for use in the operating systems specified in the Requirements section. Instead, use the [Windows Firewall API](windows-firewall-start-page.md).\]

The **IEnumNetFwV6OpenPorts** interface is a standard COM enumerator for the [**INetFwV6OpenPort**](inetfwv6openport.md) interface.

## Members

The **IEnumNetFwV6OpenPorts** interface inherits from the [**IUnknown**](https://msdn.microsoft.com/library/windows/desktop/ms680509) interface. **IEnumNetFwV6OpenPorts** also has these types of members:

-   [Methods](#methods)

### Methods

The **IEnumNetFwV6OpenPorts** interface has these methods.



| Method                                       | Description                                            |
|:---------------------------------------------|:-------------------------------------------------------|
| [**Clone**](ienumnetfwv6openports-clone.md) | Clones the enumerator.<br/>                      |
| [**Next**](ienumnetfwv6openports-next.md)   | Gets the next open port in the enumerator.<br/>  |
| [**Reset**](ienumnetfwv6openports-reset.md) | Resets the enumerator.<br/>                      |
| [**Skip**](ienumnetfwv6openports-skip.md)   | Skips the next open port in the enumerator.<br/> |



 

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

[**IEnumNetFwV6OpenPorts::Clone**](ienumnetfwv6openports-clone.md)
</dt> <dt>

[**IEnumNetFwV6OpenPorts::Next**](ienumnetfwv6openports-next.md)
</dt> <dt>

[**IEnumNetFwV6OpenPorts::Reset**](ienumnetfwv6openports-reset.md)
</dt> <dt>

[**IEnumNetFwV6OpenPorts::Skip**](ienumnetfwv6openports-skip.md)
</dt> <dt>

[**INetFwV6Connection::EnumerateOpenPorts**](inetfwv6connection-enumerateopenports.md)
</dt> <dt>

[**INetFwV6ConnectionCollection::\_NewEnum**](https://msdn.microsoft.com/library/windows/desktop/aa365818)
</dt> <dt>

[**INetFwV6OpenPortsCollection::\_NewEnum**](inetfwv6openportscollection-newenum.md)
</dt> <dt>

[IUnknown](https://www.bing.com/search?q=IUnknown)
</dt> </dl>

 

 





