---
title: Sending a Command
description: Sending a Command
ms.assetid: '28c38f36-b6a7-44da-95e2-25b3dccefc84'
keywords: ["mciSendString function"]
---

# Sending a Command

The following example function sends the [**play**](play.md) command with the "from" and "to" flags using the [**mciSendString**](mcisendstring.md) function.


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



 

 




