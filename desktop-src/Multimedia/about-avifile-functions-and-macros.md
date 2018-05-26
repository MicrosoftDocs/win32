---
title: About AVIFile Functions and Macros
description: About AVIFile Functions and Macros
ms.assetid: 877f6759-8271-47eb-8a7f-540393e5ae89
keywords:
- AVIFileInit function
- AVIFileExit function
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# About AVIFile Functions and Macros

The AVIFile functions and macros handle the information in time-based files as one or more *data streams* instead of tagged blocks of data called chunks. Data streams refer to the components of a time-based file. An AVI file can contain several different types of data, such as a video sequence, an English soundtrack, and a French soundtrack. Using AVIFile, an application can access each of these components separately.

> [!Note]  
> Although the AVIFile functions and macros work with any RIFF file, this overview demonstrates their use with AVI files only. AVI files are typically the time-based files used with the AVIFile macros and functions.

 

AVIFile functions and macros are contained in a dynamic-link library. To initialize the library, use the [**AVIFileInit**](/windows/win32/Vfw/nf-vfw-avifileinit?branch=master) function. After you initialize the library, you can use any of the AVIFile functions or macros. To release the library, use the [**AVIFileExit**](/windows/win32/Vfw/nf-vfw-avifileexit?branch=master) function. AVIFile maintains a reference count of the applications that are using the library, but not those that have released it. Your applications should balance each use of **AVIFileInit** with a call to **AVIFileExit** to completely release the library after each application finishes using it.

 

 




