---
title: Using Rectangles (Windows Media Player SDK)
description: Using Rectangles
ms.assetid: b3fc16b4-dc93-43c0-a97d-5234e36437c8
keywords:
- visualizations,rectangles
- custom visualizations,rectangles
- visualizations,Render function
- custom visualizations,Render function
- Render function,rectangles
ms.topic: article
ms.date: 05/31/2018
---

# Using Rectangles (Windows Media Player SDK)

Rectangles are used to specify rectangular areas in Microsoft Windows. You can create many rectangles in your window, but Windows Media Player supplies the values of one rectangle through the [IWMPEffects::Render](/previous-versions/windows/desktop/api/effects/nf-effects-iwmpeffects-render) function. If your plug-in renders using a window, the rectangle is the client area of the window. This is called the prc rectangle, and it defines the rectangle that Windows Media Player will display your visualization through. Use this frequently to be sure you do not draw beyond the extents of the rectangle supplied by Windows Media Player.

A rectangle has four values that define it. They are left, top, right, and bottom. The top, left corner of the rectangle is defined by left and top, and the bottom, right corner of the rectangle is defined by bottom and right.

Use the following code to get the extents of your drawing rectangle. You need to do this because the user may resize the window, and you want to be sure that you are always drawing in an area the user can see.


```C++
int leftside = prc->left;
int rightside = prc->right;
int topside = prc->top;
int bottomside = prc->bottom;

```



For example, to draw from left to right, along the top of the window, use code like this:


```C++
::MoveToEx( hdc, prc->left, prc->top, NULL );  
::LineTo(hdc, prc->right, prc->top);

```



## Related topics

<dl> <dt>

[**Implementing Render**](implementing-render.md)
</dt> </dl>

 

 




