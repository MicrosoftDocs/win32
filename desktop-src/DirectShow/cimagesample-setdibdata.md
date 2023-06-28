---
description: The SetDIBData method specifies information about the GDI device-independent bitmap (DIB) that this object is managing. Call this method to initialize the CImageSample object.
ms.assetid: 850fa16b-d4b9-4fe6-b202-7b54c49a4589
title: CImageSample.SetDIBData method (Winutil.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CImageSample.SetDIBData
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CImageSample.SetDIBData method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The `SetDIBData` method specifies information about the GDI device-independent bitmap (DIB) that this object is managing. Call this method to initialize the **CImageSample** object.

## Syntax


```C++
void SetDIBData(
   DIBDATA *pDibData
);
```



## Parameters

<dl> <dt>

*pDibData* 
</dt> <dd>

Pointer to a [**DIBDATA**](dibdata.md) structure.

</dd> </dl>

## Return value

This method does not return a value.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Winutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CImageSample Class**](cimagesample.md)
</dt> </dl>

 

 




