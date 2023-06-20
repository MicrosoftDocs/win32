---
title: Handling MCI Errors
description: Handling MCI Errors
ms.assetid: 01a2ff95-34a2-434f-9c7e-d0cdac826c02
keywords:
- mciSendCommand function
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Handling MCI Errors

\[The feature associated with this page, [MCI](/windows/win32/multimedia/mci), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **MCI**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

You should always check the return value of the [**mciSendCommand**](/previous-versions//dd757160(v=vs.85)) function. If it indicates an error, you can use [**mciGetErrorString**](/previous-versions//dd757158(v=vs.85)) to get a textual description of the error.

The following example passes the MCI error code specified by *dwError* to **mciGetErrorString**, and then displays the resulting textual error description using the [MessageBox](/windows/win32/api/winuser/nf-winuser-messagebox) function.


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
> To interpret an [**mciSendCommand**](/previous-versions//dd757160(v=vs.85)) error return value yourself, mask the high-order word (the low-order word contains the error code). If you pass the error return value to [**mciGetErrorString**](/previous-versions//dd757158(v=vs.85)), however, you must pass the entire doubleword value.

 

 

 