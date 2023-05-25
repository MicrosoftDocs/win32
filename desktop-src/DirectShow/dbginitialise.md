---
description: The DbgInitialise function initializes the debug library. Ignored in retail builds.
ms.assetid: d4ca739e-cd39-4692-81da-c5a88a09d546
title: DbgInitialise function (Wxdebug.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- DbgInitialise
api_type: 
- LibDef
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# DbgInitialise function

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **DbgInitialise** function initializes the debug library. Ignored in retail builds.

## Syntax


```C++
void DbgInitialise(
   HINSTANCE hInst
);
```



## Parameters

<dl> <dt>

*hInst* 
</dt> <dd>

Handle to the module instance.

</dd> </dl>

## Return value

This function does not return a value.

## Remarks

In an executable, call this method before using the DirectShow debug facilities. Before the executable quits, call the [**DbgTerminate**](dbgterminate.md) function to clean up the debug library.

In a DLL that links to the base-class library (Strmbase.lib), it is not necessary to call this function. The function is called automatically when the DLL is loaded.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Wxdebug.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[Debug Output Functions](debug-output-functions.md)
</dt> </dl>

 

 




