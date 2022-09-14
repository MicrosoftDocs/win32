---
title: IReferenceClock GetTime method
description: The GetTime method retrieves the current reference time.
ms.assetid: 9bf5050a-ae09-4a72-a3f2-3df8339d99b9
keywords:
- GetTime method windows Media Format
- GetTime method windows Media Format , IReferenceClock interface
- IReferenceClock interface windows Media Format , GetTime method
topic_type:
- apiref
api_name:
- IReferenceClock.GetTime
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# IReferenceClock::GetTime method

The **GetTime** method retrieves the current reference time.

## Syntax


```C++
HRESULT GetTime(
  [out] REFERENCE_TIME *pTime
);
```



## Parameters

<dl> <dt>

*pTime* \[out\]
</dt> <dd>

Pointer to a variable that receives the current time, in 100-nanosecond units.

</dd> </dl>

## Return value

The method returns an **HRESULT**. Possible values include, but are not limited to, those in the following table.



| Return code                                                                               | Description                                   |
|-------------------------------------------------------------------------------------------|-----------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>      | The method succeeded.<br/>              |
| <dl> <dt>**E\_POINTER**</dt> </dl> | The *pTime* parameter is **NULL**.<br/> |



 

## See also

<dl> <dt>

[**IReferenceClock Interface**](ireferenceclock.md)
</dt> </dl>

 

 





