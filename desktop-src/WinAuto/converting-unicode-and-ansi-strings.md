---
title: Converting Unicode and ANSI Strings
description: Microsoft Active Accessibility uses Unicode strings as defined by the BSTR data type.
ms.assetid: 47f525fe-6d18-43b9-a706-e49afa796830
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Converting Unicode and ANSI Strings

Microsoft Active Accessibility uses Unicode strings as defined by the **BSTR** data type. If your application does not use Unicode strings, or if you want to convert strings for certain API calls, use the [**MultiByteToWideChar**](https://msdn.microsoft.com/library/windows/desktop/dd319072) and [**WideCharToMultiByte**](https://msdn.microsoft.com/library/windows/desktop/dd374130) Microsoft Win32 functions to perform the necessary conversion.

Use [**WideCharToMultiByte**](https://msdn.microsoft.com/library/windows/desktop/dd374130) to convert a Unicode string to an ANSI string. The [**MultiByteToWideChar**](https://msdn.microsoft.com/library/windows/desktop/dd319072) function converts an ANSI string to a Unicode string.

Use [**SysAllocString**](https://msdn.microsoft.com/library/windows/desktop/ms221458) and [**SysFreeString**](https://msdn.microsoft.com/library/windows/desktop/ms221481) to allocate and free **BSTR** data types.

For more information about these string functions, see their references in the Windows Software Development Kit (SDK).

 

 




