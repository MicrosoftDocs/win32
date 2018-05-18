---
Description: 'The security ID of the event class object's creator. This property is supported only for backward compatibility.'
ms.assetid: '3e1b91db-ee1f-42cd-a59d-69cec08f1a91'
title: 'IEventClass::OwnerSID property'
---

# IEventClass::OwnerSID property

The security ID of the event class object's creator. This property is supported only for backward compatibility.

This property is read/write.

## Syntax


```C++
HRESULT put_OwnerSID(
  [in]          BSTR bstrOwnerSID
);

HRESULT get_OwnerSID(
  [out, retval] BSTR *pbstrOwnerSID
);
```



## Property value

The owner SID.

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

 

 




