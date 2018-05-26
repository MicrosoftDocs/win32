---
title: IEnumNetFwV6OpenPortsAsVariants interface
description: The IEnumNetFwV6OpenPortsAsVariants interface is a standard COM enumerator for the INetFwV6OpenPort interface. Unlike IEnumNetFwV6OpenPorts this enumerator yields items of type VARIANT, as is required by the Automation collection model.
ms.assetid: cc6f6328-95d6-4e3b-b1d1-5e9804462711
keywords:
- IEnumNetFwV6OpenPortsAsVariants interface ICS/ICF
- IEnumNetFwV6OpenPortsAsVariants interface ICS/ICF , described
topic_type:
- apiref
api_name:
- IEnumNetFwV6OpenPortsAsVariants
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

# IEnumNetFwV6OpenPortsAsVariants interface

\[The IPv6 Internet Connection Firewall is available for use in the operating systems specified in the Requirements section. Instead, use the [Windows Firewall API](windows-firewall-start-page.md).\]

The **IEnumNetFwV6OpenPortsAsVariants** interface is a standard COM enumerator for the [**INetFwV6OpenPort**](inetfwv6openport.md) interface. Unlike [**IEnumNetFwV6OpenPorts**](ienumnetfwv6openports.md) this enumerator yields items of type **VARIANT**, as is required by the Automation collection model.

## Members

The **IEnumNetFwV6OpenPortsAsVariants** interface inherits from the [**IUnknown**](https://msdn.microsoft.com/library/windows/desktop/ms680509) interface. **IEnumNetFwV6OpenPortsAsVariants** also has these types of members:

-   [Methods](#methods)

### Methods

The **IEnumNetFwV6OpenPortsAsVariants** interface has these methods.



| Method                                                 | Description                               |
|:-------------------------------------------------------|:------------------------------------------|
| [**Clone**](ienumnetfwv6openportsasvariants-clone.md) | Clones open ports enumerators.<br/> |
| [**Next**](ienumnetfwv6openportsasvariants-next.md)   | Gets next open port.<br/>           |
| [**Reset**](ienumnetfwv6openportsasvariants-reset.md) | Resets open ports enumerators.<br/> |
| [**Skip**](ienumnetfwv6openportsasvariants-skip.md)   | Skips next open port.<br/>          |



 

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

[**IEnumNetFwV6OpenPortsAsVariants::Clone**](ienumnetfwv6openportsasvariants-clone.md)
</dt> <dt>

[**IEnumNetFwV6OpenPortsAsVariants::Next**](ienumnetfwv6openportsasvariants-next.md)
</dt> <dt>

[**IEnumNetFwV6OpenPortsAsVariants::Reset**](ienumnetfwv6openportsasvariants-reset.md)
</dt> <dt>

[**IEnumNetFwV6OpenPortsAsVariants::Skip**](ienumnetfwv6openportsasvariants-skip.md)
</dt> <dt>

[**INetFwV6ConnectionCollection::\_NewEnum**](https://msdn.microsoft.com/library/windows/desktop/aa365818)
</dt> <dt>

[**INetFwV6OpenPortsCollection::\_NewEnum**](inetfwv6openportscollection-newenum.md)
</dt> <dt>

[IUnknown](_com_iunknown)
</dt> </dl>

 

 





