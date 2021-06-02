---
description: These functions provide support for implementing the IUnknown interface in DirectShow.
ms.assetid: 991e4c69-7d30-4ecf-9ccf-4920452c21d6
title: COM Helper Functions (Combase.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- COM
api_type: 
- LibDef
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# COM Helper Functions

These functions provide support for implementing the **IUnknown** interface in DirectShow.



| Function                                               | Description                                                           |
|--------------------------------------------------------|-----------------------------------------------------------------------|
| [**DECLARE\_IUNKNOWN**](declare-iunknown.md)          | Declares the three methods of the base interface for a new interface. |
| [**GetInterface**](getinterface.md)                   | Retrieves an interface pointer to the requested client.               |
| [**INonDelegatingUnknown**](inondelegatingunknown.md) | Nondelegating version of the **IUnknown** interface.                  |
| [**LoadOLEAut32**](loadoleaut32.md)                   | Loads the Automation DLL (OleAut32.dll).                              |



 

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Combase.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[Utility Functions](utility-functions.md)
</dt> </dl>

 

 




