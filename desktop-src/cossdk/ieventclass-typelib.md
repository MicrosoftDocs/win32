---
Description: 'The path of the type library that contains the description of the event interface.'
ms.assetid: '5cf94f0f-94fd-46d2-91e5-50d5d57f8ceb'
title: 'IEventClass::TypeLib property'
---

# IEventClass::TypeLib property

The path of the type library that contains the description of the event interface.

This property is read/write.

## Syntax


```C++
HRESULT put_TypeLib(
  [in]          BSTR bstrTypeLib
);

HRESULT get_TypeLib(
  [out, retval] BSTR *pbstrTypeLib
);
```



## Property value

The path of the type library.

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

[**IEventClass**](ieventclass.md)
</dt> </dl>

 

 




