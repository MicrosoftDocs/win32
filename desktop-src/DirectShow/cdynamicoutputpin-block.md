---
description: The Block method blocks or unblocks the flow of data from the pin. This method implements the IPinFlowControl::Block method.
ms.assetid: 8281cd8c-7543-42b5-9a4a-11bdfcb659e3
title: CDynamicOutputPin.Block method (Amfilter.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CDynamicOutputPin.Block
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CDynamicOutputPin.Block method

The `Block` method blocks or unblocks the flow of data from the pin. This method implements the [**IPinFlowControl::Block**](/windows/desktop/api/Strmif/nf-strmif-ipinflowcontrol-block) method.

## Syntax


```C++
HRESULT Block(
   DWORD  dwBlockFlags,
   HANDLE hEvent
);
```



## Parameters

<dl> <dt>

*dwBlockFlags* 
</dt> <dd>

Flag that indicates whether to block or unblock the pin. Must be one of the following values:

Zero: Unblock data flow from the pin.

AM\_PIN\_FLOW\_CONTROL\_BLOCK: Block data flow from the pin.

</dd> <dt>

*hEvent* 
</dt> <dd>

Handle to an event object, or **NULL**.

</dd> </dl>

## Return value

Returns an **HRESULT** value. Possible values include those shown in the following table.



| Return code                                                                                                                    | Description                                              |
|--------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------|
| <dl> <dt>**S\_FALSE**</dt> </dl>                                        | Pin is already unblocked.<br/>                     |
| <dl> <dt>**S\_OK**</dt> </dl>                                           | Success.<br/>                                      |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>                                   | Invalid argument.<br/>                             |
| <dl> <dt>**VFW\_E\_PIN\_ALREADY\_BLOCKED**</dt> </dl>                   | Pin is already blocked on another thread.<br/>     |
| <dl> <dt>**VFW\_E\_PIN\_ALREADY\_BLOCKED\_ON\_THIS\_THREAD**</dt> </dl> | Pin is already blocked on the calling thread.<br/> |



 

## Remarks

For more information about this method, see [**IPinFlowControl::Block**](/windows/desktop/api/Strmif/nf-strmif-ipinflowcontrol-block). Internally, this method calls one of the following protected methods:

-   Block (asynchronous): [**CDynamicOutputPin::AsynchronousBlockOutputPin**](cdynamicoutputpin-asynchronousblockoutputpin.md)
-   Block (synchronous): [**CDynamicOutputPin::SynchronousBlockOutputPin**](cdynamicoutputpin-synchronousblockoutputpin.md)
-   Unblock: [**CDynamicOutputPin::UnblockOutputPin**](cdynamicoutputpin-unblockoutputpin.md)

Unblocking is always performed synchronously.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CDynamicOutputPin Class**](cdynamicoutputpin.md)
</dt> </dl>

 

 




