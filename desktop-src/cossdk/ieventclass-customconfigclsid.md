---
Description: 'The CLSID of a component that can assist in adding properties into the property bag of a subscription object. This property is supported only for backward compatibility.'
ms.assetid: '54452bfb-063d-4f0e-a63d-a54de97106e7'
title: 'IEventClass::CustomConfigCLSID property'
---

# IEventClass::CustomConfigCLSID property

The CLSID of a component that can assist in adding properties into the property bag of a subscription object. This property is supported only for backward compatibility.

This property is read/write.

## Syntax


```C++
HRESULT put_CustomConfigCLSID(
  [in]          BSTR bstrCustomConfigCLSID
);

HRESULT get_CustomConfigCLSID(
  [out, retval] BSTR *pbstrCustomConfigCLSID
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

 

 




