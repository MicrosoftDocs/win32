---
title: Handling MCI Errors
description: Handling MCI Errors
ms.assetid: 01a2ff95-34a2-434f-9c7e-d0cdac826c02
keywords:
- mciSendCommand function
ms.topic: article
ms.date: 05/31/2018
---

# Handling MCI Errors

You should always check the return value of the [**mciSendCommand**](https://msdn.microsoft.com/library/Dd757160(v=VS.85).aspx) function. If it indicates an error, you can use [**mciGetErrorString**](https://msdn.microsoft.com/library/Dd757158(v=VS.85).aspx) to get a textual description of the error.

The following example passes the MCI error code specified by *dwError* to **mciGetErrorString**, and then displays the resulting textual error description using the [MessageBox](https://msdn.microsoft.com/library/ms645505.aspx) function.


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
> To interpret an [**mciSendCommand**](https://msdn.microsoft.com/library/Dd757160(v=VS.85).aspx) error return value yourself, mask the high-order word (the low-order word contains the error code). If you pass the error return value to [**mciGetErrorString**](https://msdn.microsoft.com/library/Dd757158(v=VS.85).aspx), however, you must pass the entire doubleword value.

 

 

 




