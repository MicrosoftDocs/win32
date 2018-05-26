---
Description: CSourcePosition is an abstract class for implementing the IMediaPosition interface on a source filter.
ms.assetid: 838d2efd-6870-4412-98e2-fb2628e14bf3
title: CSourcePosition class
ms.date: 05/31/2018
ms.topic: interface
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CSourcePosition class

`CSourcePosition` is an abstract class for implementing the [**IMediaPosition**](/windows/win32/Control/nn-control-imediaposition?branch=master) interface on a source filter.

This class is obsolete. If your source filter is seekable, it should expose the [**IMediaSeeking**](/windows/win32/Strmif/nn-strmif-imediaseeking?branch=master) interface instead of **IMediaPosition**. You can use the [**CSourceSeeking**](csourceseeking.md) base class for this purpose.

 

 



