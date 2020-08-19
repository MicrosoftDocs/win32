---
title: Sending a Command
description: Sending a Command
ms.assetid: 28c38f36-b6a7-44da-95e2-25b3dccefc84
keywords:
- mciSendString function
ms.topic: article
ms.date: 05/31/2018
---

# Sending a Command

The following example function sends the [**play**](play.md) command with the "from" and "to" flags using the [**mciSendString**](/previous-versions//dd757161(v=vs.85)) function.


```C++
BOOL PlayFromTo(LPTSTR lpstrAlias, DWORD dwFrom, DWORD dwTo) 
{ 
    TCHAR achCommandBuff[128]; 
    int result;
    MCIERROR err;

    // Form the command string.
    result = _stprintf_s(
        achCommandBuff, 
        TEXT("play %s from %u to %u"), 
        lpstrAlias, dwFrom, dwTo); 

    if (result == -1)
    {
        return FALSE;
    }

    // Send the command string.
    err = mciSendString(achCommandBuff, NULL, 0, NULL); 
    if (err != 0)
    {
        return FALSE;
    }

    return TRUE;
} 
```



 

 