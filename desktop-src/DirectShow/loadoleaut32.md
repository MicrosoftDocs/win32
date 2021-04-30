---
description: The LoadOLEAut32 function loads the Automation dynamic-link library (OleAut32.dll).
ms.assetid: af907341-1e2c-4c63-bf4e-d6c49b4f6a6e
title: LoadOLEAut32 function (Combase.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- LoadOLEAut32
api_type: 
- LibDef
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# LoadOLEAut32 function

The **LoadOLEAut32** function loads the Automation dynamic-link library (OleAut32.dll).

## Syntax


```C++
HINSTANCE LoadOLEAut32(void);
```



## Parameters

This function has no parameters.

## Return value

Returns a handle to an Automation DLL instance.

## Remarks

When the [**CBaseObject**](cbaseobject.md) destructor destroys the object that loaded OleAut32.dll, it will unload the library if it is still loaded.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Combase.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**COM Helper Functions**](com-helper-functions.md)
</dt> </dl>

 

 




