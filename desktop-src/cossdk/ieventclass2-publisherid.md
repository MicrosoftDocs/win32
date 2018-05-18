---
Description: 'The CLSID for the event publisher.'
ms.assetid: 'b54799a3-612d-44a8-9f65-5e2243d99344'
title: 'IEventClass2::PublisherID property'
---

# IEventClass2::PublisherID property

The CLSID for the event publisher.

This property is read/write.

## Syntax


```C++
HRESULT put_PublisherID(
  [in]          BSTR bstrPublisherID
);

HRESULT get_PublisherID(
  [out, retval] BSTR *pbstrPublisherID
);
```



## Property value

The CLSID.

## Error codes

This method can return the standard return values E\_INVALIDARG, E\_OUTOFMEMORY, E\_UNEXPECTED, E\_FAIL, and S\_OK.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                              |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                    |
| IDL<br/>                      | <dl> <dt>Eventsys.idl</dt> </dl> |



## See also

<dl> <dt>

[**IEventClass2**](ieventclass2.md)
</dt> </dl>

 

 




