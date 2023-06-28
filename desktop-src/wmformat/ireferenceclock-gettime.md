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
ms.date: 4/26/2023
api_location: 
ms.custom: UpdateFrequency5
---

# IReferenceClock::GetTime method

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

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

 

 





