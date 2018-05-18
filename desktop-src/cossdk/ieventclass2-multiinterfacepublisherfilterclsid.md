---
Description: 'The CLSID of the object implementing IMultiInterfacePublisherFilter.'
ms.assetid: '09583b2f-a43e-4afd-9709-c34bb3a98fe3'
title: 'IEventClass2::MultiInterfacePublisherFilterCLSID property'
---

# IEventClass2::MultiInterfacePublisherFilterCLSID property

The CLSID of the object implementing [**IMultiInterfacePublisherFilter**](imultiinterfacepublisherfilter.md).

This property is read/write.

## Syntax


```C++
HRESULT put_MultiInterfacePublisherFilterCLSID(
  [in]          BSTR bstrPubFilCLSID
);

HRESULT get_MultiInterfacePublisherFilterCLSID(
  [out, retval] BSTR *pbstrPubFilCLSID
);
```



## Property value

The CLSID of the object.

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

 

 




