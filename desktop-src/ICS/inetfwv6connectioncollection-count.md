---
title: INetFwV6ConnectionCollection Count property
description: Retrieves a read-only element yielding the number of items in the collection.
ms.assetid: '54bbb308-7e31-4319-ab6c-256365c1e5c2'
keywords: ["Count property ICS/ICF", "Count property ICS/ICF , INetFwV6ConnectionCollection interface", "INetFwV6ConnectionCollection interface ICS/ICF , Count property"]
topic_type:
- apiref
api_name:
- INetFwV6ConnectionCollection.Count
- INetFwV6ConnectionCollection.get_Count
api_location:
- Netfwv6.dll
api_type:
- COM
---

# INetFwV6ConnectionCollection::Count property

\[The IPv6 Internet Connection Firewall is available for use in the operating systems specified in the Requirements section. Instead, use the [Windows Firewall API](windows-firewall-start-page.md).\]

Retrieves a read-only element yielding the number of items in the collection.

This property is read-only.

## Syntax


```C++
HRESULT get_Count(
  [out] INetFwV6ConnectionCollection *plCount
);
```



## Property value

Count of the items in the collection.

## Error codes

If the method succeeds the return value is S\_OK.

If the method fails, the return value is one of the following error codes.



| Name                                                                                      | Meaning                                                       |
|-------------------------------------------------------------------------------------------|---------------------------------------------------------------|
| <dl> <dt>E\_ABORT</dt> </dl>       | The operation was aborted.<br/>                         |
| <dl> <dt>E\_FAIL</dt> </dl>        | An unspecified error occurred.<br/>                     |
| <dl> <dt>E\_INVALIDARG</dt> </dl>  | The parameter is invalid.<br/>                          |
| <dl> <dt>E\_NOINTERFACE</dt> </dl> | A specified interface is not supported.<br/>            |
| <dl> <dt>E\_NOTIMPL</dt> </dl>     | A specified method is not implemented.<br/>             |
| <dl> <dt>E\_OUTOFMEMORY</dt> </dl> | The method was unable to allocate required memory.<br/> |
| <dl> <dt>E\_UNEXPECTED</dt> </dl>  | The method failed for unknown reasons.<br/>             |



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

[**INetFwV6ConnectionCollection**](https://msdn.microsoft.com/library/windows/desktop/aa365806)
</dt> </dl>

 

 





