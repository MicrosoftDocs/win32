---
description: You can query and set the text alignment for a device context by using the GetTextAlign and SetTextAlign functions.
ms.assetid: 7fdfbadb-827a-4b42-9b9a-b9e46389e13c
title: Setting the Text Alignment
ms.topic: article
ms.date: 05/31/2018
---

# Setting the Text Alignment

You can query and set the text alignment for a device context by using the [**GetTextAlign**](/windows/desktop/api/Wingdi/nf-wingdi-gettextalign) and [**SetTextAlign**](/windows/desktop/api/Wingdi/nf-wingdi-settextalign) functions. The text-alignment settings determine how text is positioned relative to a specified location. Text can be aligned to the right or left of the position or centered over it; it can also be aligned above or below the point.

The following example shows a method for determining which horizontal alignment flag is set:


```C++
switch ((TA_LEFT | TA_RIGHT | TA_CENTER) & GetTextAlign(hdc)) 
{ 
    case TA_LEFT: 
       . 
       . 
       . 
    case TA_RIGHT: 
       . 
       . 
       . 
    case TA_CENTER: 
       . 
       . 
       . 
} 
```



You can also use the [**SetTextAlign**](/windows/desktop/api/Wingdi/nf-wingdi-settextalign) function to update the current position when a text-output function is called. For instance, the following example uses the [**SetTextAlign**](/windows/win32/api/wingdi/nf-wingdi-settextalign) function to update the current position when the [**TextOut**](/windows/desktop/api/Wingdi/nf-wingdi-textouta) function is called. In this example, the *cArial* parameter is an integer that specifies the number of Arial fonts.


```C++
UINT uAlignPrev; 
char szCount[8];
HRESULT hr;
size_t * pcch; 
 
uAlignPrev = SetTextAlign(hdc, TA_UPDATECP); 
MoveToEx(hdc, 10, 50, (LPPOINT) NULL); 
TextOut(hdc, 0, 0, "Number of Arial fonts: ", 23); 
itoa(cArial, szCount, 10); 

hr = StringCchLength(szCount, 9, pcch);
if (FAILED(hr))
{
// TODO: write error handler 
}
 
TextOut(hdc, 0, 0, (LPSTR) szCount, *pcch); 
SetTextAlign(hdc, uAlignPrev); 
```



> [!Note]  
> You should not use [**SetTextAlign**](/windows/win32/api/wingdi/nf-wingdi-settextalign) with TA\_UPDATECP when you are using [**ScriptStringOut**](/windows/win32/api/usp10/nf-usp10-scriptstringout), because selected text is not rendered correctly. If you must use this flag, you can unset and reset it as necessary to avoid the problem.

 

 

 
