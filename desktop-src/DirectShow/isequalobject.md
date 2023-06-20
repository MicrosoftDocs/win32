---
description: The IsEqualObject function checks if two interfaces are on the same object.
ms.assetid: 51325e05-5a7f-4a80-a12e-2e7dedc028e2
title: IsEqualObject function (Wxutil.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IsEqualObject
api_type: 
- LibDef
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# IsEqualObject function

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The `IsEqualObject` function checks if two interfaces are on the same object.

## Syntax


```C++
BOOL WINAPI IsEqualObject(
   IUnknown *pFirst,
   IUnknown *pSecond
);
```



## Parameters

<dl> <dt>

*pFirst* 
</dt> <dd>

Pointer to one interface.

</dd> <dt>

*pSecond* 
</dt> <dd>

Pointer to the other interface.

</dd> </dl>

## Return value

Returns **TRUE** if the interfaces are both on the same object, or **FALSE** otherwise.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Wxutil.h (include Streams.h)</dt> </dl>                                                                                    |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[Miscellaneous Helper Functions](miscellaneous-helper-functions.md)
</dt> </dl>

 

 




