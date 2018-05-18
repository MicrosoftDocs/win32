---
Description: 'The ProgID for the event class object.'
ms.assetid: '40565df4-01c8-42fa-baf0-deadad77ef1f'
title: 'IEventClass::EventClassName property'
---

# IEventClass::EventClassName property

The ProgID for the event class object.

This property is read/write.

## Syntax


```C++
HRESULT put_EventClassName(
  [in]          BSTR bstrEventClassName
);

HRESULT get_EventClassName(
  [out, retval] BSTR *pbstrEventClassName
);
```



## Property value

The ProgID.

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

 

 




