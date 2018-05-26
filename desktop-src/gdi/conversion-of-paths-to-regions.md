---
Description: An application can convert a path into a region by calling the PathToRegion function.
ms.assetid: c4261516-7872-4118-99e2-138f0ac3c38a
title: Conversion of Paths to Regions
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Conversion of Paths to Regions

An application can convert a path into a region by calling the [**PathToRegion**](/windows/win32/Wingdi/nf-wingdi-pathtoregion?branch=master) function. Like [**SelectClipPath**](/windows/win32/Wingdi/nf-wingdi-selectclippath?branch=master), **PathToRegion** is useful in the creation of special graphics effects. For example, there are no functions that allow an application to offset a path; however, there is a function that enables an application to offset a region ([**OffsetRgn**](/windows/win32/Wingdi/nf-wingdi-offsetrgn?branch=master)). Using **PathToRegion** , an application can create the effect of animating a complex shape by creating a path that defines the shape, converting the path into a region (by calling **PathToRegion**), and then repeatedly painting, moving, and erasing the region (by calling functions in a sequence, such as [**FillRgn**](/windows/win32/Wingdi/nf-wingdi-fillrgn?branch=master), **OffsetRgn** , and **FillRgn**).

 

 



