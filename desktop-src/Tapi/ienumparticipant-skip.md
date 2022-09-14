---
description: The Skip method skips over the next specified number of elements in the enumeration sequence. This method is hidden from Visual Basic and scripting languages.
ms.assetid: 7f641354-c3f5-4eb3-ad1c-98abf7694106
title: IEnumParticipant::Skip method (Confpriv.h)
ms.topic: reference
ms.date: 05/31/2018
---

# IEnumParticipant::Skip method

\[**Skip** is not available for use in Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The RTC Client API provides similar functionality.\]

The **Skip** method skips over the next specified number of elements in the enumeration sequence. This method is hidden from Visual Basic and scripting languages.

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



| Return code                                                                                   | Description                                                     |
|-----------------------------------------------------------------------------------------------|-----------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | Number of elements skipped was *celt*.<br/>               |
| <dl> <dt>**S\_FALSE**</dt> </dl>       | Number of elements skipped was not *celt*.<br/>           |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | Insufficient memory exists to perform the operation.<br/> |



 

## Requirements



| Requirement | Value |
|-------------------------|---------------------------------------------------------------------------------------|
| TAPI version<br/> | Requires TAPI 3.0 or later<br/>                                                 |
| Header<br/>       | <dl> <dt>Confpriv.h</dt> </dl> |
| Library<br/>      | <dl> <dt>Uuid.lib</dt> </dl>   |
| DLL<br/>          | <dl> <dt>Tapi3.dll</dt> </dl>  |



## See also

<dl> <dt>

[**IEnumParticipant**](ienumparticipant.md)
</dt> <dt>

[**ITParticipant**](itparticipant.md)
</dt> </dl>

 

 




