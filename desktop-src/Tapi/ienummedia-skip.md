---
description: IEnumMedia::Skip method - The Skip method skips over the next specified number of elements in the enumeration sequence.
ms.assetid: 825972c9-5303-4c5a-9475-dc67c185af91
title: IEnumMedia::Skip method (Sdpblb.h)
ms.topic: reference
ms.date: 05/31/2018
---

# IEnumMedia::Skip method

\[ Rendezvous IP Telephony Conferencing controls and interfaces are not available for use in Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The RTC Client API provides similar functionality.\]

The **Skip** method skips over the next specified number of elements in the enumeration sequence.

## Syntax


```C++
HRESULT Skip(
  [in] ULONG celt
);
```



## Parameters

<dl> <dt>

*celt* \[in\]
</dt> <dd>

Number of elements to skip.

</dd> </dl>

## Return value

This method can return one of these values.



| Return code                                                                             | Description                                           |
|-----------------------------------------------------------------------------------------|-------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>    | Number of elements skipped was *celt*.<br/>     |
| <dl> <dt>**S\_FALSE**</dt> </dl> | Number of elements skipped was not *celt*.<br/> |



 

## Requirements



| Requirement | Value |
|-------------------------|---------------------------------------------------------------------------------------|
| TAPI version<br/> | Requires TAPI 3.0 or later<br/>                                                 |
| Header<br/>       | <dl> <dt>Sdpblb.h</dt> </dl>   |
| Library<br/>      | <dl> <dt>Uuid.lib</dt> </dl>   |
| DLL<br/>          | <dl> <dt>Sdpblb.dll</dt> </dl> |



## See also

<dl> <dt>

[**IEnumMedia**](ienummedia.md)
</dt> </dl>

 

 




