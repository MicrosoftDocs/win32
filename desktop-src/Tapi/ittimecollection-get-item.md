---
description: The get\_Item method gets an item from the collection using an index.
ms.assetid: 7401ae21-190d-479c-aebc-51bf8a953b94
title: ITTimeCollection::get_Item method (Sdpblb.h)
ms.topic: reference
ms.date: 05/31/2018
---

# ITTimeCollection::get\_Item method

\[ Rendezvous IP Telephony Conferencing controls and interfaces are not available for use in Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The RTC Client API provides similar functionality.\]

The **get\_Item** method gets an item from the collection using an index.

## Syntax


```C++
HRESULT get_Item(
  [in]  LONG   Index,
  [out] ITTime **pVal
);
```



## Parameters

<dl> <dt>

*Index* \[in\]
</dt> <dd>

Index of the item to get.

</dd> <dt>

*pVal* \[out\]
</dt> <dd>

Pointer to [**ITTime**](ittime.md) desired interface.

</dd> </dl>

## Return value

This method can return one of these values.



| Value                                                                                         | Meaning                                                         |
|-----------------------------------------------------------------------------------------------|-----------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | Method succeeded.<br/>                                    |
| <dl> <dt>**E\_POINTER**</dt> </dl>     | The *pVal* parameter is not a valid pointer.<br/>         |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>  | The *Index* parameter is not valid.<br/>                  |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | Insufficient memory exists to perform the operation.<br/> |
| <dl> <dt>**E\_FAIL**</dt> </dl>        | Unspecified error.<br/>                                   |
| <dl> <dt>**E\_NOTIMPL**</dt> </dl>     | This method is not yet implemented.<br/>                  |



 

## Remarks

TAPI calls the **AddRef** method on the [**ITTime**](ittime.md) interface returned by I**TTimeCollection::get\_Item**. The application must call **Release** on the **ITTime** interface to free resources associated with it.

## Requirements



| Requirement | Value |
|-------------------------|---------------------------------------------------------------------------------------|
| TAPI version<br/> | Requires TAPI 3.0 or later<br/>                                                 |
| Header<br/>       | <dl> <dt>Sdpblb.h</dt> </dl>   |
| Library<br/>      | <dl> <dt>Uuid.lib</dt> </dl>   |
| DLL<br/>          | <dl> <dt>Sdpblb.dll</dt> </dl> |



## See also

<dl> <dt>

[**ITTimeCollection**](ittimecollection.md)
</dt> <dt>

[**ITTime**](ittime.md)
</dt> </dl>

 

 




