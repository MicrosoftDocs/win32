---
title: Converting Strings
description: Converting Strings
ms.assetid: 40621c71-4264-40bc-b6c3-6b639d2f28fa
keywords:
- mciSendString function
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Converting Strings

\[The feature associated with this page, [MCI](/windows/win32/multimedia/mci), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **MCI**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

When you use the [**mciSendString**](/previous-versions//dd757161(v=vs.85)) function, all values passed with the command and all return values are text strings, so your application needs conversion routines to translate from variables to strings or back again. The following example retrieves the source rectangle and converts the returned string into rectangle coordinates.


```C++
BOOL GetSourceRect(LPTSTR lpstrAlias, LPRECT lprc) 
{ 
    TCHAR achRetBuff[128]; 
    TCHAR achCommandBuff[128]; 

    int result;
    MCIERROR err;
 
    // Build the command string. 
    result = _stprintf_s(
        achCommandBuff, 
        TEXT("where %s source"), 
        lpstrAlias); 

    if (result == -1)
    {
        return FALSE;
    }
    
    // Clear the RECT.
    SetRectEmpty(lprc);
 
    // Send the MCI command. 
    err = mciSendString(
        achCommandBuff, 
        achRetBuff, 
        sizeof(achRetBuff), 
        NULL);

    if (err != 0)
    {
        return FALSE;
    }
        
    // The rectangle is returned as "x y dx dy". 
    // Translate the string into the RECT structure. 

    // Warning: This example omits error checking
    // for the _tcstok_s and _tstoi functions.
    TCHAR *p; 
    TCHAR *context;

    // Left.
    p = _tcstok_s(achRetBuff, TEXT(" "), &context);
    lprc->left = _tstoi(p);

    // Top.
    p = _tcstok_s(NULL, TEXT(" "), &context);
    lprc->top = _tstoi(p);

    // Right.
    p = _tcstok_s(NULL, TEXT(" "), &context);
    lprc->right = _tstoi(p);
    
    // Bottom.
    p = _tcstok_s(NULL, TEXT(" "), &context);
    lprc->bottom = _tstoi(p);

    return TRUE;
}
 
```



> [!Note]  
> **RECT** structures are handled differently in MCI than in other parts of Windows; in MCI, the **right** member contains the width of the rectangle and the **bottom** member contains its height. In the string interface, a rectangle is specified as *X1*, *Y1*, *X2*, and *Y2*. The coordinates *X1* and *Y1* specify the upper-left corner of the rectangle, and the coordinates *X2* and *Y2* specify the width and height.

 

 

 