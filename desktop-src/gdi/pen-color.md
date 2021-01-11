---
description: The color attribute specifies the pen's color.
ms.assetid: ce775359-65fc-40d0-8725-b392cc0464a6
title: Pen Color
ms.topic: article
ms.date: 05/31/2018
---

# Pen Color

The color attribute specifies the pen's color. An application can create a cosmetic pen with a unique color by using the [**RGB**](/windows/desktop/api/Wingdi/nf-wingdi-rgb) macro to store the red, green, blue triplet that specifies the desired color in a [COLORREF](colorref.md) structure and passing this structure's address to the [**CreatePen**](/windows/desktop/api/Wingdi/nf-wingdi-createpen), [**CreatePenIndirect**](/windows/desktop/api/Wingdi/nf-wingdi-createpenindirect), or [**ExtCreatePen**](/windows/desktop/api/Wingdi/nf-wingdi-extcreatepen) function. (The stock pens are limited to black, white, and invisible.) For more information about RGB triplets and color, see [Colors](colors.md).

 

 



