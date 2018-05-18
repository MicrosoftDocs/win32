---
Description: 'The CLSID for the event class object.'
ms.assetid: 'eb51a015-cb99-4cbc-8fba-8c4834adcf65'
title: 'IEventClass::EventClassID property'
---

# IEventClass::EventClassID property

The CLSID for the event class object.

This property is read/write.

## Syntax


```C++
HRESULT put_EventClassID(
  [in]          BSTR bstrEventClassID
);

HRESULT get_EventClassID(
  [out, retval] BSTR *pbstrEventClassID
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

[**IEventClass**](ieventclass.md)
</dt> </dl>

 

 




