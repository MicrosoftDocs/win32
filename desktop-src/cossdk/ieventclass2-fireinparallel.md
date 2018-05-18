---
Description: 'Indicates whether events of this class can be fired in parallel.'
ms.assetid: '83db1bcd-8b41-4036-9073-c417e97826ed'
title: 'IEventClass2::FireInParallel property'
---

# IEventClass2::FireInParallel property

Indicates whether events of this class can be fired in parallel.

This property is read/write.

## Syntax


```C++
HRESULT put_FireInParallel(
  [in]          BOOL fFireInParallel
);

HRESULT get_FireInParallel(
  [out, retval] BOOL *pfFireInParallel
);
```



## Property value

Indicates whether the events of this class can fire in parallel.

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

 

 




