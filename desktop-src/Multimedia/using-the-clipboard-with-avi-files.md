---
title: Using the Clipboard with AVI Files
description: Using the Clipboard with AVI Files
ms.assetid: 76ef7cc9-9afd-462a-b9fe-2b62f8113a9a
keywords:
- AVIPutFileOnClipboard function
- AVIGetFromClipboard function
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Using the Clipboard with AVI Files

The clipboard provides convenient, temporary storage that an application can use to copy or transfer AVI files. AVIFile includes clipboard functions that you can use with disk or memory files.

You can copy a file to the clipboard by using the [**AVIPutFileOnClipboard**](/windows/win32/Vfw/nf-vfw-aviputfileonclipboard?branch=master) function. To write a file that is on the clipboard to memory or disk, use the [**AVIGetFromClipboard**](/windows/win32/Vfw/nf-vfw-avigetfromclipboard?branch=master) function.

You can clear a file from the clipboard by using the [**AVIClearClipboard**](/windows/win32/Vfw/nf-vfw-aviclearclipboard?branch=master) function. This function does not clear other types of information, such as text, from the clipboard. If you use clipboard functions in your application, clear the clipboard with **AVIClearClipboard** before closing the application or closing the file on the clipboard. You can call **AVIClearClipboard** in your application whether or not **AVIPutFileOnClipboard** has been used.

> [!Note]  
> If your application copies a file to the clipboard and the file contains stream data that might change, you can create a memory file of cloned streams by using the [**AVIMakeFileFromStreams**](/windows/win32/Vfw/nf-vfw-avimakefilefromstreams?branch=master) function. You can then place the file on the clipboard and then release the original file without invalidating it.

 

 

 




