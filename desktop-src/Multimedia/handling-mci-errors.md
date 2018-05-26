---
title: Handling MCI Errors
description: Handling MCI Errors
ms.assetid: 01a2ff95-34a2-434f-9c7e-d0cdac826c02
keywords:
- mciSendCommand function
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Handling MCI Errors

You should always check the return value of the [**mciSendCommand**](/windows/win32/Mmsystem/?branch=master) function. If it indicates an error, you can use [**mciGetErrorString**](/windows/win32/Mmsystem/?branch=master) to get a textual description of the error.

The following example passes the MCI error code specified by *dwError* to **mciGetErrorString**, and then displays the resulting textual error description using the [MessageBox](http://go.microsoft.com/fwlink/p/?linkid=17005) function.


```C++
// Use mciGetErrorString to get a textual description of an MCI error.
// Display the error description using MessageBox.

void showError(DWORD dwError)
{
    char szErrorBuf[MAXERRORLENGTH];
    MessageBeep(MB_ICONEXCLAMATION);
    if(mciGetErrorString(dwError, (LPSTR) szErrorBuf, MAXERRORLENGTH))
    {
        MessageBox(hMainWnd, szErrorBuf, "MCI Error",
        MB_ICONEXCLAMATION);
    }
    else
    {
        MessageBox(hMainWnd, "Unknown Error", "MCI Error",
            MB_ICONEXCLAMATION);
    }
}
 
```



> [!Note]  
> To interpret an [**mciSendCommand**](/windows/win32/Mmsystem/?branch=master) error return value yourself, mask the high-order word (the low-order word contains the error code). If you pass the error return value to [**mciGetErrorString**](/windows/win32/Mmsystem/?branch=master), however, you must pass the entire doubleword value.

 

 

 




