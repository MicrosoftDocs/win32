---
description: The CoInitializeHelper method calls the CoInitializeEx function at the start of the thread.
ms.assetid: 1a981e1e-c059-4e51-81d8-33bcb39ee580
title: CAMThread.CoInitializeHelper method (Wxutil.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CAMThread.CoInitializeHelper
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CAMThread.CoInitializeHelper method

The `CoInitializeHelper` method calls the CoInitializeEx function at the start of the thread.

## Syntax


```C++
static HRESULT CoInitializeHelper();
```



## Parameters

This method has no parameters.

## Return value

Returns an **HRESULT** value. The following are possible values.



| Return code                                                                             | Description                                              |
|-----------------------------------------------------------------------------------------|----------------------------------------------------------|
| <dl> <dt>**S\_FALSE**</dt> </dl> | The CoInitializeEx function is not available.<br/> |
| <dl> <dt>**S\_OK**</dt> </dl>    | Success.<br/>                                      |
| <dl> <dt>**E\_FAIL**</dt> </dl>  | Failure.<br/>                                      |



 

## Remarks

The [**CAMThread::InitialThreadProc**](camthread-initialthreadproc.md) method calls this helper method, which calls the CoInitializeEx function. It uses the COINIT\_DISABLE\_OLE1DDE flag, to disable Dynamic Data Exchange (DDE). For more information, see the Platform SDK.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Wxutil.h (include Streams.h)</dt> </dl>                                                                                    |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CAMThread Class**](camthread.md)
</dt> </dl>

 

 




