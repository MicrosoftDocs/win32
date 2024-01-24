---
description: The Delete method deletes the media corresponding to the specified index.
ms.assetid: 5fcbd026-75a8-4db2-a701-e080dc222537
title: ITMediaCollection::Delete method (Sdpblb.h)
ms.topic: reference
ms.date: 05/31/2018
---

# ITMediaCollection::Delete method

\[ Rendezvous IP Telephony Conferencing controls and interfaces are not available for use in Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The RTC Client API provides similar functionality.\]

The **Delete** method deletes the media corresponding to the specified index.

## Syntax


```C++
HRESULT Delete(
  [in] LONG Index
);
```



## Parameters

<dl> <dt>

*Index* \[in\]
</dt> <dd>

Index of media to be deleted.

</dd> </dl>

## Return value

This method can return one of these values.



| Return code                                                                                                                              | Description                                                                                              |
|------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                                                     | Method succeeded.<br/>                                                                             |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>                                             | The *Index* parameter has a value less than 1 or greater than the current number of elements.<br/> |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl>                                            | Insufficient memory exists to perform the operation.<br/>                                          |
| <dl> <dt>**E\_FAIL**</dt> </dl>                                                   | Internal error (should only occur if a previous call returned an error).<br/>                      |
| <dl> <dt>**E\_NOTIMPL**</dt> </dl>                                                | This method is not yet implemented.<br/>                                                           |
| <dl> <dt>**HRESULT\_FROM\_ERROR\_CODE(SDPBLB\_CONF\_BLOB\_DESTROYED)**</dt> </dl> | The SDP blob doesn't exist.<br/>                                                                   |



 

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

[**ITMediaCollection**](itmediacollection.md)
</dt> </dl>

 

 




