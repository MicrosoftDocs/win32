---
Description: 'The color attribute specifies the pen''s color.'
ms.assetid: 'ce775359-65fc-40d0-8725-b392cc0464a6'
title: Pen Color
---

# Pen Color

The color attribute specifies the pen's color. An application can create a cosmetic pen with a unique color by using the [**RGB**](rgb.md) macro to store the red, green, blue triplet that specifies the desired color in a [COLORREF](colorref.md) structure and passing this structure's address to the [**CreatePen**](createpen.md), [**CreatePenIndirect**](createpenindirect.md), or [**ExtCreatePen**](extcreatepen.md) function. (The stock pens are limited to black, white, and invisible.) For more information about RGB triplets and color, see [Colors](colors.md).

 

 



