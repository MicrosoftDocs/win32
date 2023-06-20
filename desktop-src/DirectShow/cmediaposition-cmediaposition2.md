---
description: "Learn about the CMediaPosition.CMediaPosition (Ctlutil.h) constructor method. This method uses 'pName', 'pUnk', and 'phr' parameters."
ms.assetid: 4074f513-d1e7-4311-8732-4d755e621e55
title: CMediaPosition.CMediaPosition constructor (Ctlutil.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CMediaPosition.CMediaPosition
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CMediaPosition.CMediaPosition constructor (Ctlutil.h) - pName, pUnk, phr parameters

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Constructor method.

## Syntax


```C++
CMediaPosition(
   const TCHAR     *pName,
         LPUNKNOWN pUnk,
         HRESULT   *phr
);
```



## Parameters

<dl> <dt>

*pName* 
</dt> <dd>

Pointer to the name of the object, for debugging purposes. Allocate this parameter in static memory.

</dd> <dt>

*pUnk* 
</dt> <dd>

Pointer to the owner of this object, or **NULL** if the object is not aggregated.

</dd> <dt>

*phr* 
</dt> <dd>

Pointer to an **HRESULT** value.

</dd> </dl>

## Requirements

| Requirement | Value |
|-|-|
| Header | Ctlutil.h (include Streams.h) |
| Library| Strmbase.lib (retail builds); Strmbasd.lib (debug builds) |

## See also

<dl> <dt>

[**CMediaPosition Class**](cmediaposition.md)
</dt> </dl>

 

 




