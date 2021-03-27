---
description: The get\_Item method gets an ITMedia pointer corresponding to the specified index.
ms.assetid: ad218357-82c8-4fcb-b71b-ba17564a5ca5
title: ITMediaCollection::get_Item method (Sdpblb.h)
ms.topic: reference
ms.date: 05/31/2018
---

# ITMediaCollection::get\_Item method

\[ Rendezvous IP Telephony Conferencing controls and interfaces are not available for use in Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The RTC Client API provides similar functionality.\]

The **get\_Item** method gets an [**ITMedia**](itmedia.md) pointer corresponding to the specified index.

## Syntax


```C++
HRESULT get_Item(
  [in]  LONG    Index,
  [out] ITMedia **pVal
);
```



## Parameters

<dl> <dt>

*Index* \[in\]
</dt> <dd>

Index of media item to get.

</dd> <dt>

*pVal* \[out\]
</dt> <dd>

Pointer to the [**ITMedia**](itmedia.md) interface for the desired item.

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

Most C and C++ lists are 0-based, but this index is 1-based for Visual Basic compatibility, meaning the first item has an index number of 1.

## Requirements



| Requirement | Value |
|-------------------------|---------------------------------------------------------------------------------------|
| TAPI version<br/> | Requires TAPI 3.0 or later<br/>                                                 |
| Header<br/>       | <dl> <dt>Sdpblb.h</dt> </dl>   |
| Library<br/>      | <dl> <dt>Uuid.lib</dt> </dl>   |
| DLL<br/>          | <dl> <dt>Sdpblb.dll</dt> </dl> |



## See also

<dl> <dt>

[**ITMedia**](itmedia.md)
</dt> <dt>

[**ITMediaCollection**](itmediacollection.md)
</dt> </dl>

 

 




