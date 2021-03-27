---
description: The BreakConnect method releases the input pin from a connection.
ms.assetid: e295cec1-8c8f-471c-8832-075ac7708cb1
title: CBaseRenderer.BreakConnect method (Renbase.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseRenderer.BreakConnect
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CBaseRenderer.BreakConnect method

The `BreakConnect` method releases the input pin from a connection.

## Syntax


```C++
virtual HRESULT BreakConnect();
```



## Parameters

This method has no parameters.

## Return value

Returns one of the **HRESULT** values shown in the following table.



| Return code                                                                                         | Description                            |
|-----------------------------------------------------------------------------------------------------|----------------------------------------|
| <dl> <dt>**S\_FALSE**</dt> </dl>             | The pin was not connected.<br/>  |
| <dl> <dt>**S\_OK**</dt> </dl>                | Success.<br/>                    |
| <dl> <dt>**VFW\_E\_NOT\_STOPPED**</dt> </dl> | The filter is still active.<br/> |



 

## Remarks

The filter's input pin calls this method from inside its own `BreakConnect` method. (For more information, see [**CBasePin::BreakConnect**](cbasepin-breakconnect.md).) The filter performs some internal bookkeeping, such as resetting the end-of-stream flag.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Renbase.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseRenderer Class**](cbaserenderer.md)
</dt> </dl>

 

 




