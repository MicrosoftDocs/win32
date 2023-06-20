---
description: The Postpone method specifies a new presentation time for a previously queued command.
ms.assetid: 6201eb18-8180-445c-8d29-980511748fe4
title: CDeferredCommand.Postpone method (Ctlutil.h)
ms.topic: reference
ms.date: 4/26/2023
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
ms.custom: UpdateFrequency5
---

# CDeferredCommand.Postpone method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

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

 

 




