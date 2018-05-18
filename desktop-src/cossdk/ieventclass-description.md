---
Description: 'A displayable text description of the event class object.'
ms.assetid: '2232fd7e-2015-466f-afd1-15e5b546239a'
title: 'IEventClass::Description property'
---

# IEventClass::Description property

A displayable text description of the event class object.

This property is read/write.

## Syntax


```C++
HRESULT put_Description(
  [in]          BSTR bstrDescription
);

HRESULT get_Description(
  [out, retval] BSTR *pbstrDescription
);
```



## Property value

The description.

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

 

 




