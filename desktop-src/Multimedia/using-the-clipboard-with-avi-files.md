---
title: Using the Clipboard with AVI Files
description: Using the Clipboard with AVI Files
ms.assetid: 76ef7cc9-9afd-462a-b9fe-2b62f8113a9a
keywords:
- AVIPutFileOnClipboard function
- AVIGetFromClipboard function
ms.topic: article
ms.date: 05/31/2018
---

# Using the Clipboard with AVI Files

The clipboard provides convenient, temporary storage that an application can use to copy or transfer AVI files. AVIFile includes clipboard functions that you can use with disk or memory files.

You can copy a file to the clipboard by using the [**AVIPutFileOnClipboard**](/windows/desktop/api/Vfw/nf-vfw-aviputfileonclipboard) function. To write a file that is on the clipboard to memory or disk, use the [**AVIGetFromClipboard**](/windows/desktop/api/Vfw/nf-vfw-avigetfromclipboard) function.

You can clear a file from the clipboard by using the [**AVIClearClipboard**](/windows/desktop/api/Vfw/nf-vfw-aviclearclipboard) function. This function does not clear other types of information, such as text, from the clipboard. If you use clipboard functions in your application, clear the clipboard with **AVIClearClipboard** before closing the application or closing the file on the clipboard. You can call **AVIClearClipboard** in your application whether or not **AVIPutFileOnClipboard** has been used.

> [!Note]  
> If your application copies a file to the clipboard and the file contains stream data that might change, you can create a memory file of cloned streams by using the [**AVIMakeFileFromStreams**](/windows/desktop/api/Vfw/nf-vfw-avimakefilefromstreams) function. You can then place the file on the clipboard and then release the original file without invalidating it.

 

 

 




