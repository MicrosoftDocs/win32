---
Description: 'The ID of the event interface on the event class object. This property is supported only for backward compatibility.'
ms.assetid: '69d24a08-2eca-4204-95ae-1409fe306464'
title: 'IEventClass::FiringInterfaceID property'
---

# IEventClass::FiringInterfaceID property

The ID of the event interface on the event class object. This property is supported only for backward compatibility.

This property is read/write.

## Syntax


```C++
HRESULT put_FiringInterfaceID(
  [in]          BSTR bstrFiringInterfaceID
);

HRESULT get_FiringInterfaceID(
  [out, retval] BSTR *pbstrFiringInterfaceID
);
```



## Property value

The interface identifier.

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

 

 




