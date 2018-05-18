---
Description: 'The partition GUID of the event class object.'
ms.assetid: '154849ac-350c-4b2f-bb51-ac6973f0a8fa'
title: 'IEventSubscription3::EventClassPartitionID property'
---

# IEventSubscription3::EventClassPartitionID property

The partition GUID of the event class object.

This property is read/write.

## Syntax


```C++
HRESULT put_EventClassPartitionID(
  [in]          BSTR bstrEventClassPartitionID
);

HRESULT get_EventClassPartitionID(
  [out, retval] BSTR *pbstrEventClassPartitionID
);
```



## Property value

A string containing the GUID of the event class partition.

## Error codes

This method can return the standard return values E\_INVALIDARG, E\_OUTOFMEMORY, E\_UNEXPECTED, E\_FAIL, and S\_OK.

## Requirements



|                                     |                                                            |
|-------------------------------------|------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/> |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>       |



## See also

<dl> <dt>

[**IEventSubscription3**](ieventsubscription3.md)
</dt> </dl>

 

 




