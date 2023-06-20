---
description: "Learn about the COARefTime.COARefTime constructor (Ctlutil.h) method. This method uses the 'crt' parameter."
ms.assetid: 06a3b452-b5cb-46da-b60e-83d687b386f6
title: COARefTime.COARefTime constructor (Ctlutil.h) - crt parameter
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- COARefTime.COARefTime
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# COARefTime.COARefTime constructor (Ctlutil.h) - crt parameter

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Constructor method.

## Syntax


```C++
COARefTime(
   CRefTime crt
);
```



## Parameters

<dl> <dt>

*crt* 
</dt> <dd>

[**CRefTime**](creftime.md) object that specifies the reference time.

</dd> </dl>

## Requirements

| Requirement                   | Value                                                                                                                                                                                           |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header  | Ctlutil.h (include Streams.h)                                                                                   |
| Library | Strmbase.lib (retail builds); Strmbasd.lib (debug builds) |

## See also

<dl> <dt>

[**COARefTime Class**](coareftime.md)
</dt> </dl>

 

 




