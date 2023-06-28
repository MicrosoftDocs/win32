---
description: CBaseOutputPin.Active method - The Active method notifies the pin that the filter is now active.
ms.assetid: 35df4305-0e2c-4ee1-bc63-db5aec864c46
title: CBaseOutputPin.Active method (Amfilter.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseOutputPin.Active
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CBaseOutputPin.Active method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The `Active` method notifies the pin that the filter is now active.

## Syntax


```C++
HRESULT Active();
```



## Parameters

This method has no parameters.

## Return value

Returns an **HRESULT** value. Possible values include those listed in the following table.



| Return code                                                                                          | Description                           |
|------------------------------------------------------------------------------------------------------|---------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                 | Success.<br/>                   |
| <dl> <dt>**VFW\_E\_NO\_ALLOCATOR**</dt> </dl> | No allocator is available.<br/> |



 

## Remarks

This method overrides the [**CBasePin::Active**](cbasepin-active.md) method. It calls the [**IMemAllocator::Commit**](/windows/desktop/api/Strmif/nf-strmif-imemallocator-commit) method on the allocator, to allocate memory for buffers.

If you override this method, call the base-class method from your overriding method.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseOutputPin Class**](cbaseoutputpin.md)
</dt> </dl>

 

 




