---
Description: 'An application can convert a path into a region by calling the PathToRegion function.'
ms.assetid: 'c4261516-7872-4118-99e2-138f0ac3c38a'
title: Conversion of Paths to Regions
---

# Conversion of Paths to Regions

An application can convert a path into a region by calling the [**PathToRegion**](pathtoregion.md) function. Like [**SelectClipPath**](selectclippath.md), **PathToRegion** is useful in the creation of special graphics effects. For example, there are no functions that allow an application to offset a path; however, there is a function that enables an application to offset a region ([**OffsetRgn**](offsetrgn.md)). Using **PathToRegion** , an application can create the effect of animating a complex shape by creating a path that defines the shape, converting the path into a region (by calling **PathToRegion**), and then repeatedly painting, moving, and erasing the region (by calling functions in a sequence, such as [**FillRgn**](fillrgn.md), **OffsetRgn** , and **FillRgn**).

 

 



