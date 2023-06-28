---
description: The DbgDumpObjectRegister function displays information about active objects. Ignored in retail builds.
ms.assetid: 362d9912-662c-4a72-95b4-01f3d808e299
title: DbgDumpObjectRegister function (Wxdebug.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- DbgDumpObjectRegister
api_type: 
- LibDef
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# DbgDumpObjectRegister function

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The `DbgDumpObjectRegister` function displays information about active objects. Ignored in retail builds.

## Syntax


```C++
void DbgDumpObjectRegister(void);
```



## Parameters

This function has no parameters.

## Return value

This function does not return a value.

## Remarks

In debug builds, the debug library maintains a list of active objects. The list includes any objects that derive from [**CBaseObject**](cbaseobject.md), were created by the current module, and have not been destroyed. The **CBaseObject** constructor and destructor methods update the list.

This function generates several LOG\_MEMORY messages. At logging level 1, the function displays only the total number of objects. At logging level 2 or higher, it displays a list of the objects.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Wxdebug.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[Debug Output Functions](debug-output-functions.md)
</dt> </dl>

 

 




