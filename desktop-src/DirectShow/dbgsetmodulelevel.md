---
description: The DbgSetModuleLevel function sets the logging level for one or more message types. Ignored in retail builds.
ms.assetid: 89d25106-8018-4089-8b77-d3c87529e984
title: DbgSetModuleLevel function (Wxdebug.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- DbgSetModuleLevel
api_type: 
- LibDef
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# DbgSetModuleLevel function

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **DbgSetModuleLevel** function sets the logging level for one or more message types. Ignored in retail builds.

## Syntax


```C++
void DbgSetModuleLevel(
   DWORD Types,
   DWORD Level
);
```



## Parameters

<dl> <dt>

*Types* 
</dt> <dd>

Bitwise combination of one or more message types.

</dd> <dt>

*Level* 
</dt> <dd>

Logging level for the specified message types.

</dd> </dl>

## Return value

This function does not return a value.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Wxdebug.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[Debug Output Functions](debug-output-functions.md)
</dt> </dl>

 

 




