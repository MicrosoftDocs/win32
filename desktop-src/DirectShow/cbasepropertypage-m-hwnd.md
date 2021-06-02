---
description: The m\_hwnd member variable contains a handle to the dialog window. This member variable is initialized after the object creates the dialog window, when the CreateDialogParam function returns.
ms.assetid: f985c06f-a1f9-458b-b9f3-cabe9f583313
title: CBasePropertyPage::m_hwnd member (Cprop.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- m_hwnd
api_type: 
- LibDef
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CBasePropertyPage::m\_hwnd member

The `m_hwnd` member variable contains a handle to the dialog window. This member variable is initialized after the object creates the dialog window, when the **CreateDialogParam** function returns.

## Syntax


```C++
HWND m_hwnd;
```



## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Cprop.h (include Streams.h)</dt> </dl>                                                                                     |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBasePropertyPage Class**](cbasepropertypage.md)
</dt> </dl>

 

 




