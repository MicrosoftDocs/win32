---
Description: 'Indicates whether the event class can be activated in-process.'
ms.assetid: 'ac043e5c-4f63-4f01-bc60-8c7a6bd08640'
title: 'IEventClass2::AllowInprocActivation property'
---

# IEventClass2::AllowInprocActivation property

Indicates whether the event class can be activated in-process.

This property is read/write.

## Syntax


```C++
HRESULT put_AllowInprocActivation(
  [in]          BOOL fAllowInprocActivation
);

HRESULT get_AllowInprocActivation(
  [out, retval] BOOL *pfAllowInprocActivation
);
```



## Property value

Indicates whether in-process activation is allowed.

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

 

 




