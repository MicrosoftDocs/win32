---
description: The GetInterface function retrieves an interface pointer.
ms.assetid: 75fe8849-c779-4d47-a5ff-5a23308c8a21
title: GetInterface function (Combase.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- GetInterface
api_type: 
- LibDef
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# GetInterface function

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The `GetInterface` function retrieves an interface pointer.

## Syntax


```C++
HRESULT GetInterface(
   LPUNKNOWN pUnk,
   void      **ppv
);
```



## Parameters

<dl> <dt>

*pUnk* 
</dt> <dd>

Pointer to the **IUnknown** interface.

</dd> <dt>

*ppv* 
</dt> <dd>

Address of a pointer to the retrieved interface.

</dd> </dl>

## Return value

Returns an **HRESULT** value.

## Remarks

This member function performs a thread-safe increment of the reference count. To retrieve the interface and add a reference, call this function from your overriding implementation of the **INonDelegatingUnknown::NonDelegatingQueryInterface** method.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Combase.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**COM Helper Functions**](com-helper-functions.md)
</dt> <dt>

[**INonDelegatingUnknown**](inondelegatingunknown.md)
</dt> </dl>

 

 




