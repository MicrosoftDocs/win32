---
description: The Postpone method specifies a new presentation time for a previously queued command.
ms.assetid: 6201eb18-8180-445c-8d29-980511748fe4
title: CDeferredCommand.Postpone method (Ctlutil.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CDeferredCommand.Postpone
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CDeferredCommand.Postpone method

The `Postpone` method specifies a new presentation time for a previously queued command.

## Syntax


```C++
HRESULT Postpone(
   REFTIME newtime
);
```



## Parameters

<dl> <dt>

*newtime* 
</dt> <dd>

New presentation time.

</dd> </dl>

## Return value

Returns VFW\_E\_TIME\_ALREADY\_PASSED if *newtime* is already passed. Otherwise, returns an **HRESULT** resulting from a call to [**CCmdQueue::Remove**](ccmdqueue-remove.md) (when extracting from the list) or [**CCmdQueue::Insert**](ccmdqueue-insert.md) (when reinserting with the changed time).

## Remarks

This member function implements the [**IDeferredCommand::Postpone**](/windows/desktop/api/Control/nf-control-ideferredcommand-postpone) method.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Ctlutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CDeferredCommand Class**](cdeferredcommand.md)
</dt> </dl>

 

 




