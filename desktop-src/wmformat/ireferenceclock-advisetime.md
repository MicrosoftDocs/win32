---
title: IReferenceClock AdviseTime method
description: The AdviseTime method requests an asynchronous notification that a time has elapsed.
ms.assetid: 8f3f8713-b53c-4110-ac7a-724bbc49368e
keywords:
- AdviseTime method windows Media Format
- AdviseTime method windows Media Format , IReferenceClock interface
- IReferenceClock interface windows Media Format , AdviseTime method
topic_type:
- apiref
api_name:
- IReferenceClock.AdviseTime
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
api_location: 
ms.custom: UpdateFrequency5
---

# IReferenceClock::AdviseTime method

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **AdviseTime** method requests an asynchronous notification that a time has elapsed.

## Syntax


```C++
HRESULT AdviseTime(
  [in]  REFERENCE_TIME rtBaseTime,
  [in]  REFERENCE_TIME rtStreamTime,
  [in]  HEVENT         hEvent,
  [out] DWORD          *pdwAdviseCookie
);
```



## Parameters

<dl> <dt>

*rtBaseTime* \[in\]
</dt> <dd>

Base reference time, in 100-nanosecond units.

</dd> <dt>

*rtStreamTime* \[in\]
</dt> <dd>

Stream offset time, in 100-nanosecond units.

</dd> <dt>

*hEvent* \[in\]
</dt> <dd>

Handle to an event, created by the caller. This event will be signaled when the time specified elapses.

</dd> <dt>

*pdwAdviseCookie* \[out\]
</dt> <dd>

Pointer to a variable that receives an identifier for the request. This is used to identify this call to **AdviseTime** in the future for example, to cancel the request.

</dd> </dl>

## Return value

The method returns an **HRESULT**. Possible values include, but are not limited to, those in the following table.



| Return code                                                                               | Description                                             |
|-------------------------------------------------------------------------------------------|---------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>      | The method succeeded.<br/>                        |
| <dl> <dt>**E\_POINTER**</dt> </dl> | The *pdwAdviseCookie* parameter is **NULL**.<br/> |
| <dl> <dt>**E\_FAIL**</dt> </dl>    | Unspecified failure.<br/>                         |



 

## See also

<dl> <dt>

[**IReferenceClock Interface**](ireferenceclock.md)
</dt> </dl>

 

 





