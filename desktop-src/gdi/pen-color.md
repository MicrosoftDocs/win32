---
Description: The color attribute specifies the pens color.
ms.assetid: ce775359-65fc-40d0-8725-b392cc0464a6
title: Pen Color
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Pen Color

The color attribute specifies the pen's color. An application can create a cosmetic pen with a unique color by using the [**RGB**](/windows/win32/Wingdi/nf-wingdi-rgb?branch=master) macro to store the red, green, blue triplet that specifies the desired color in a [COLORREF](colorref.md) structure and passing this structure's address to the [**CreatePen**](/windows/win32/Wingdi/nf-wingdi-createpen?branch=master), [**CreatePenIndirect**](/windows/win32/Wingdi/nf-wingdi-createpenindirect?branch=master), or [**ExtCreatePen**](/windows/win32/Wingdi/nf-wingdi-extcreatepen?branch=master) function. (The stock pens are limited to black, white, and invisible.) For more information about RGB triplets and color, see [Colors](colors.md).

 

 



