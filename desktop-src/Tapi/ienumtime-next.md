---
description: The Next method gets the next specified number of elements in the enumeration sequence.
ms.assetid: e8ca77b8-0322-43b4-9996-26f584cf878a
title: IEnumTime::Next method (Sdpblb.h)
ms.topic: reference
ms.date: 05/31/2018
---

# IEnumTime::Next method

\[ Rendezvous IP Telephony Conferencing controls and interfaces are not available for use in Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The RTC Client API provides similar functionality.\]

The **Next** method gets the next specified number of elements in the enumeration sequence.

## Syntax


```C++
HRESULT Next(
  [in]  ULONG  celt,
  [out] ITTime **pVal,
  [out] ULONG  *pceltFetched
);
```



## Parameters

<dl> <dt>

*celt* \[in\]
</dt> <dd>

Number of elements requested.

</dd> <dt>

*pVal* \[out\]
</dt> <dd>

Pointer to the [**ITTime**](ittime.md) interface.

</dd> <dt>

*pceltFetched* \[out\]
</dt> <dd>

Pointer to the number of elements actually supplied. May be **NULL** if *celt* is 1.

</dd> </dl>

## Return value

This method can return one of these values.



| Value                                                                                     | Meaning                                                       |
|-------------------------------------------------------------------------------------------|---------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>      | Method returned *celt* number of elements.<br/>         |
| <dl> <dt>**S\_FALSE**</dt> </dl>   | Number of elements remaining was less than *celt*.<br/> |
| <dl> <dt>**E\_POINTER**</dt> </dl> | The *pVal* parameter is not a valid pointer.<br/>       |



 

## Remarks

TAPI calls the **AddRef** method on the [**ITTime**](ittime.md) interface returned by **IEnumTime::Next**. The application must call **Release** on the **ITTime** interface to free resources associated with it.

## Requirements



| Requirement | Value |
|-------------------------|---------------------------------------------------------------------------------------|
| TAPI version<br/> | Requires TAPI 3.0 or later<br/>                                                 |
| Header<br/>       | <dl> <dt>Sdpblb.h</dt> </dl>   |
| Library<br/>      | <dl> <dt>Uuid.lib</dt> </dl>   |
| DLL<br/>          | <dl> <dt>Sdpblb.dll</dt> </dl> |



## See also

<dl> <dt>

[**IEnumTime**](ienumtime.md)
</dt> </dl>

 

 




