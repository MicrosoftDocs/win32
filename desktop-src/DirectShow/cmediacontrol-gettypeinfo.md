---
description: CMediaControl.GetTypeInfo method - Retrieves a type-information object, which can retrieve the type information for an interface.
ms.assetid: 2014485f-d937-415d-a2fc-0c69269b5237
title: CMediaControl.GetTypeInfo method (Ctlutil.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CMediaControl.GetTypeInfo
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CMediaControl.GetTypeInfo method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Retrieves a type-information object, which can retrieve the type information for an interface.

## Syntax


```C++
HRESULT GetTypeInfo(
   UINT      itinfo,
   LCID      lcid,
   ITypeInfo **pptinfo
);
```



## Parameters

<dl> <dt>

*itinfo* 
</dt> <dd>

Type information to return. Pass zero to retrieve type information for the **IDispatch** implementation.

</dd> <dt>

*lcid* 
</dt> <dd>

Locale ID for the type information. For classes that support localized member names, an object might be able to return different type information for different languages. For classes that do not support localized member names, this parameter can be ignored.

</dd> <dt>

*pptinfo* 
</dt> <dd>

Address of a pointer to the type-information object requested.

</dd> </dl>

## Return value

Returns an E\_POINTER if *pptinfo* is invalid. Returns TYPE\_E\_ELEMENTNOTFOUND if *itinfo* is not zero. Returns S\_OK if is successful. Otherwise, returns an **HRESULT** from one of the calls to retrieve the type.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Ctlutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CMediaControl Class**](cmediacontrol.md)
</dt> </dl>

 

 




