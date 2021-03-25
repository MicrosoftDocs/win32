---
description: The GetHResult method retrieves the HRESULT value from the invoked command.
ms.assetid: 7e88a2bd-6b1b-4e59-b185-5dfd501fc37a
title: CDeferredCommand.GetHResult method (Ctlutil.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CDeferredCommand.GetHResult
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CDeferredCommand.GetHResult method

The `GetHResult` method retrieves the **HRESULT** value from the invoked command.

## Syntax


```C++
HRESULT GetHResult(
   HRESULT *phrResult
);
```



## Parameters

<dl> <dt>

*phrResult* 
</dt> <dd>

Pointer to the **HRESULT** value.

</dd> </dl>

## Return value

Returns E\_ABORT if **m\_pQueue** is **NULL**. Otherwise, returns S\_OK.

## Remarks

This member function implements the [**IDeferredCommand::GetHResult**](/windows/desktop/api/Control/nf-control-ideferredcommand-gethresult) method.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Ctlutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CDeferredCommand Class**](cdeferredcommand.md)
</dt> </dl>

 

 




