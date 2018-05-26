---
Description: The m\_hwnd member variable contains a handle to the dialog window. This member variable is initialized after the object creates the dialog window, when the CreateDialogParam function returns.
ms.assetid: f985c06f-a1f9-458b-b9f3-cabe9f583313
title: CBasePropertyPagem\_hwnd member
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CBasePropertyPage::m\_hwnd member

The `m_hwnd` member variable contains a handle to the dialog window. This member variable is initialized after the object creates the dialog window, when the **CreateDialogParam** function returns.

## Syntax


```C++
HWND m_hwnd;
```



## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Cprop.h (include Streams.h)</dt> </dl>                                                                                     |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBasePropertyPage Class**](cbasepropertypage.md)
</dt> </dl>

 

 




