---
Description: The fax service provider (FSP) functions return a Boolean value that indicates the success or failure of the function. If the function fails, the fax service calls the GetLastError function to retrieve extended error information.
ms.assetid: 0adab0ad-923e-462e-9ac1-29e4d1cc1f4d
title: Setting the Last-Error Code
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Setting the Last-Error Code

The fax service provider (FSP) functions return a Boolean value that indicates the success or failure of the function. If the function fails, the fax service calls the [GetLastError](http://msdn.microsoft.com/library/en-us/debug/base/getlasterror.asp) function to retrieve extended error information.

When a function fails, the FSP must call [SetLastError](http://msdn.microsoft.com/library/en-us/debug/base/setlasterror.asp) immediately to set the last-error code. If the FSP calls another Microsoft Win32 function after setting the last-error code, that function can overwrite the FSP's last-error code.

 

 



