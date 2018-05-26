---
title: The Picture Object
description: Picture objects provide a language-neutral abstraction for bitmaps, icons, and metafiles.
ms.assetid: 1698b203-ab3d-4385-b008-7b661b62fd76
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# The Picture Object

Picture objects provide a language-neutral abstraction for bitmaps, icons, and metafiles. As with the standard font object, the system provides a standard implementation of the picture object. Its primary interfaces are **IPicture** and **IPictureDisp**, the latter being derived from [**IDispatch**](/windows/previous-versions/oaidl/nn-oaidl-idispatch?branch=master) to provide access to the picture's properties through Automation.

> [!Note]  
> When saving pictures for the Picture Object, Automation can only save in the bitmap format. For example, if a developer loads a JPEG or GIF, then saves it back to the same filename, they will now have a bitmap format picture with the original extension (.jpg or .gif).

 

For more information on picture object properties see [**IPicture**](https://msdn.microsoft.com/library/windows/desktop/ms680761) and [**IPictureDisp**](https://msdn.microsoft.com/library/windows/desktop/ms680762).

 

 




