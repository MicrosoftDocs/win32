---
title: INetFwV6ConnectionCollection interface
description: The INetFwV6ConnectionCollection interface is a standard Automation collection for the INetFwV6Connection interface.
ms.assetid: '3e9f63f1-a201-4174-934b-62fdfe87ecca'
keywords: ["INetFwV6ConnectionCollection interface ICS/ICF", "INetFwV6ConnectionCollection interface ICS/ICF , described"]
topic_type:
- apiref
api_name:
- INetFwV6ConnectionCollection
api_location:
- Netfwv6.dll
api_type:
- COM
---

# INetFwV6ConnectionCollection interface

\[The IPv6 Internet Connection Firewall is available for use in the operating systems specified in the Requirements section. Instead, use the [Windows Firewall API](windows-firewall-start-page.md).\]

The **INetFwV6ConnectionCollection** interface is a standard Automation collection for the [**INetFwV6Connection**](inetfwv6connection.md) interface.

## Members

The **INetFwV6ConnectionCollection** interface inherits from the [**IDispatch**](ebbff4bc-36b2-4861-9efa-ffa45e013eb5) interface. **INetFwV6ConnectionCollection** also has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **INetFwV6ConnectionCollection** interface has these methods.



| Method                                                         | Description                                                  |
|:---------------------------------------------------------------|:-------------------------------------------------------------|
| [**get\_\_NewEnum**](https://msdn.microsoft.com/library/windows/desktop/aa365818) | Retrieves the contents of the \_NewEnum property.<br/> |
| [**get\_Count**](inetfwv6connectioncollection-count.md)       | Retrieves the contents of the Count property.<br/>     |



 

### Properties

The **INetFwV6ConnectionCollection** interface has these properties.



| Property                                                             | Description                                       |
|:---------------------------------------------------------------------|:--------------------------------------------------|
| [**\_NewEnum**](https://msdn.microsoft.com/library/windows/desktop/aa365818)<br/> | Gets an enumerator for the collection.<br/> |
| [**Count**](inetfwv6connectioncollection-count.md)<br/>       | Gets the count of the collection.<br/>      |



 

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP with SP1 \[desktop apps only\]<br/>                                   |
| Minimum supported server<br/> | None supported<br/>                                                              |
| End of client support<br/>    | Windows XP with SP1<br/>                                                         |
| Redistributable<br/>          | Advanced Networking Pack for Windows XP<br/>                                     |
| Header<br/>                   | <dl> <dt>Netfwv6.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Netfwv6.dll</dt> </dl> |



## See also

<dl> <dt>

[**IDispatch**](ebbff4bc-36b2-4861-9efa-ffa45e013eb5)
</dt> <dt>

[**INetFwV6ConnectionCollection::\_NewEnum**](https://msdn.microsoft.com/library/windows/desktop/aa365818)
</dt> <dt>

[**INetFwV6ConnectionCollection::Count**](inetfwv6connectioncollection-count.md)
</dt> <dt>

[**INetFwV6Mgr::Connections**](inetfwv6mgr-connections.md)
</dt> <dt>

[IUnknown](_com_iunknown)
</dt> </dl>

 

 





