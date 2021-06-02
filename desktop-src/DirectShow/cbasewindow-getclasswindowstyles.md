---
description: The GetClassWindowStyles method retrieves the window's class styles and window styles.
ms.assetid: 6eec7912-c654-4e4f-b6f1-ec94c7284575
title: CBaseWindow.GetClassWindowStyles method (Winutil.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseWindow.GetClassWindowStyles
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CBaseWindow.GetClassWindowStyles method

The `GetClassWindowStyles` method retrieves the window's class styles and window styles.

## Syntax


```C++
virtual LPTSTR GetClassWindowStyles(
   DWORD *pClassStyles,
   DWORD *pWindowStyles,
   DWORD *pWindowStylesEx
) = 0;
```



## Parameters

<dl> <dt>

*pClassStyles* 
</dt> <dd>

Pointer to a variable that receives the class styles.

</dd> <dt>

*pWindowStyles* 
</dt> <dd>

Pointer to a variable that receives the window styles.

</dd> <dt>

*pWindowStylesEx* 
</dt> <dd>

Pointer to a variable that receives the extended window styles.

</dd> </dl>

## Return value

Returns a static text string that contains the class name.

## Remarks

The [**CBaseWindow::PrepareWindow**](cbasewindow-preparewindow.md) method calls this method to retrieve the window's class styles and window styles.

This method is pure virtual; the derived class must implement it. The following example shows a possible implementation:


```C++
LPTSTR CMyWindowClass::GetClassWindowStyles(DWORD *pClassStyles,
                                            DWORD *pWindowStyles,
                                            DWORD *pWindowStylesEx)
{
    *pClassStyles = CS_HREDRAW | CS_VREDRAW;
    *pWindowStyles = WS_OVERLAPPEDWINDOW | WS_CLIPCHILDREN;
    *pWindowStylesEx = WS_EX_WINDOWEDGE;
    return TEXT("MyWindowClass");
}
```



The object uses the class style for the **lpszClassName** member of a WNDCLASS structure, which it passes to the **RegisterClass** function. The object uses the window styles for the *dwExStyle* and *dwStyle* parameters of the **CreateWindowEx** function. For more information, see the Platform SDK.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Winutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseWindow Class**](cbasewindow.md)
</dt> </dl>

 

 




