---
title: INetFwV6OpenPortsCollection \_NewEnum property
description: Retrieves a read-only element yielding an IEnumNetV6OpenPortsAsVariants enumerator for the items in the collection.
ms.assetid: 995c86c5-8f21-4554-972f-424e2266af6f
keywords:
- _NewEnum property ICS/ICF
- _NewEnum property ICS/ICF , INetFwV6OpenPortsCollection interface
- INetFwV6OpenPortsCollection interface ICS/ICF , _NewEnum property
topic_type:
- apiref
api_name:
- INetFwV6OpenPortsCollection._NewEnum
- INetFwV6OpenPortsCollection.get__NewEnum
api_location:
- Netfwv6.dll
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# INetFwV6OpenPortsCollection::\_NewEnum property

\[The IPv6 Internet Connection Firewall is available for use in the operating systems specified in the Requirements section. Instead, use the [Windows Firewall API](windows-firewall-start-page.md).\]

Retrieves a read-only element yielding an [**IEnumNetV6OpenPortsAsVariants**](ienumnetfwv6openportsasvariants.md) enumerator for the items in the collection.

This property is read-only.

## Syntax


```C++
HRESULT get__NewEnum(
  [out] IUknown **ppEnum
);
```



## Property value

The enumerator for the items in the collection.

## Error codes

If the method succeeds, the return value is S\_OK.

If the method fails, the return value is one of the following error codes.



| Name                                                                                      | Meaning                                                       |
|-------------------------------------------------------------------------------------------|---------------------------------------------------------------|
| <dl> <dt>E\_ABORT</dt> </dl>       | The operation was aborted.<br/>                         |
| <dl> <dt>E\_FAIL</dt> </dl>        | An unspecified error occurred.<br/>                     |
| <dl> <dt>E\_INVALIDARG</dt> </dl>  | The parameter is invalid.<br/>                          |
| <dl> <dt>E\_NOINTERFACE</dt> </dl> | A specified interface is not supported.<br/>            |
| <dl> <dt>E\_NOTIMPL</dt> </dl>     | A specified method is not implemented.<br/>             |
| <dl> <dt>E\_OUTOFMEMORY</dt> </dl> | The method was unable to allocate required memory.<br/> |
| <dl> <dt>E\_POINTER</dt> </dl>     | A pointer passed as a parameter is not valid.<br/>      |
| <dl> <dt>E\_UNEXPECTED</dt> </dl>  | The method failed for unknown reasons.<br/>             |



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

[**INetFwV6OpenPortsCollection**](https://msdn.microsoft.com/library/windows/desktop/aa365923)
</dt> </dl>

 

 





