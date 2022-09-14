---
description: The Create method creates a new media with default properties, adds it to the collection at the specified index, and returns a pointer to the ITMedia interface.
ms.assetid: f0036556-d2e7-4589-8bb4-e2c5559902fe
title: ITMediaCollection::Create method (Sdpblb.h)
ms.topic: reference
ms.date: 05/31/2018
---

# ITMediaCollection::Create method

\[ Rendezvous IP Telephony Conferencing controls and interfaces are not available for use in Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The RTC Client API provides similar functionality.\]

The **Create** method creates a new media with default properties, adds it to the collection at the specified index, and returns a pointer to the [**ITMedia**](itmedia.md) interface.

## Syntax


```C++
HRESULT Create(
  [in]  LONG    Index,
  [out] ITMedia **ppMedia
);
```



## Parameters

<dl> <dt>

*Index* \[in\]
</dt> <dd>

Index for the new item. The minimum value for the index is 1, and the maximum value for the index is the current number of items + 1.

</dd> <dt>

*ppMedia* \[out\]
</dt> <dd>

Pointer to [**ITMedia**](itmedia.md) interface created.

</dd> </dl>

## Return value

This method can return one of these values.



| Value                                                                                         | Meaning                                                         |
|-----------------------------------------------------------------------------------------------|-----------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | Method succeeded.<br/>                                    |
| <dl> <dt>**E\_POINTER**</dt> </dl>     | The *ppMedia* parameter is not a valid pointer.<br/>      |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>  | The *Index* parameter is not valid.<br/>                  |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | Insufficient memory exists to perform the operation.<br/> |
| <dl> <dt>**E\_FAIL**</dt> </dl>        | Unspecified error.<br/>                                   |
| <dl> <dt>**E\_NOTIMPL**</dt> </dl>     | This method is not yet implemented.<br/>                  |



 

## Remarks

Most C and C++ lists are 0-based, but this index is 1-based for Visual Basic compatibility, meaning the first item has an index number of 1.

TAPI calls the **AddRef** method on the [**ITMedia**](itmedia.md) interface returned by **ITMediaCollection::Create**. The application must call **Release** on the [**ITMedia**](itmedia.md) interface to free resources associated with it.

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

 

 




