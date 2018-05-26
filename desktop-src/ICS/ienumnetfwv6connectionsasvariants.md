---
title: IEnumNetFwV6ConnectionsAsVariants interface
description: The IEnumNetFwV6ConnectionsAsVariants interface is a standard COM enumerator for the INetFwV6Connection interface. Unlike IEnumNetFwV6Connections this enumerator yields items of type VARIANT, as is required by the Automation collection model.
ms.assetid: 5411d865-48fb-4058-bb38-3e895d243803
keywords:
- IEnumNetFwV6ConnectionsAsVariants interface ICS/ICF
- IEnumNetFwV6ConnectionsAsVariants interface ICS/ICF , described
topic_type:
- apiref
api_name:
- IEnumNetFwV6ConnectionsAsVariants
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

# IEnumNetFwV6ConnectionsAsVariants interface

\[The IPv6 Internet Connection Firewall is available for use in the operating systems specified in the Requirements section. Instead, use the [Windows Firewall API](windows-firewall-start-page.md).\]

The **IEnumNetFwV6ConnectionsAsVariants** interface is a standard COM enumerator for the INetFwV6Connection interface. Unlike IEnumNetFwV6Connections this enumerator yields items of type **VARIANT**, as is required by the Automation collection model.

## Members

The **IEnumNetFwV6ConnectionsAsVariants** interface inherits from the [**IUnknown**](https://msdn.microsoft.com/library/windows/desktop/ms680509) interface. **IEnumNetFwV6ConnectionsAsVariants** also has these types of members:

-   [Methods](#methods)

### Methods

The **IEnumNetFwV6ConnectionsAsVariants** interface has these methods.



| Method                                                   | Description                                    |
|:---------------------------------------------------------|:-----------------------------------------------|
| [**Clone**](ienumnetfwv6connectionsasvariants-clone.md) | Clones the connections enumerators.<br/> |
| [**Next**](ienumnetfwv6connectionsasvariants-next.md)   | Gets next connection.<br/>               |
| [**Reset**](ienumnetfwv6connectionsasvariants-reset.md) | Resets the connections enumerators.<br/> |
| [**Skip**](ienumnetfwv6connectionsasvariants-skip.md)   | Skips next connection.<br/>              |



 

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

[**IEnumNetFwV6ConnectionsAsVariants::Clone**](ienumnetfwv6connectionsasvariants-clone.md)
</dt> <dt>

[**IEnumNetFwV6ConnectionsAsVariants::Next**](ienumnetfwv6connectionsasvariants-next.md)
</dt> <dt>

[**IEnumNetFwV6ConnectionsAsVariants::Reset**](ienumnetfwv6connectionsasvariants-reset.md)
</dt> <dt>

[**IEnumNetFwV6ConnectionsAsVariants::Skip**](ienumnetfwv6connectionsasvariants-skip.md)
</dt> <dt>

[**INetFwV6ConnectionCollection::\_NewEnum**](https://msdn.microsoft.com/library/windows/desktop/aa365818)
</dt> <dt>

[**INetFwV6OpenPortsCollection::\_NewEnum**](inetfwv6openportscollection-newenum.md)
</dt> <dt>

[IUnknown](_com_iunknown)
</dt> </dl>

 

 





