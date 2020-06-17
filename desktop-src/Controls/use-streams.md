---
title: How to Use Streams
description: You can use streams to transfer data into or out of a rich edit control. A stream is defined by an EDITSTREAM structure, which specifies a buffer and an application-defined callback function.
ms.assetid: A7ED47F1-968C-4E41-B1E2-4449072D2FC4
ms.topic: article
ms.date: 05/31/2018
---

# How to Use Streams

You can use streams to transfer data into or out of a rich edit control. A stream is defined by an [**EDITSTREAM**](/windows/desktop/api/Richedit/ns-richedit-editstream) structure, which specifies a buffer and an application-defined callback function.

To read data into a rich edit control (that is, stream in the data), use the [**EM\_STREAMIN**](em-streamin.md) message. The control repeatedly calls the application's callback function, which transfers a portion of the data into the buffer each time.

To save the contents of a rich edit control (that is, stream out the data), you can use the [**EM\_STREAMOUT**](em-streamout.md) message. The control repeatedly writes to the buffer and then calls the application's callback function. For each call, the callback function saves the contents of the buffer.

## What you need to know

### Technologies

-   [Windows Controls](window-controls.md)

### Prerequisites

-   C/C++
-   Windows User Interface Programming

## Instructions

### Use a Stream

The following code example shows how to read an .rtf file into a rich edit control. The file handle is passed to the callback function through the **dwCookie** member of the [**EDITSTREAM**](/windows/desktop/api/Richedit/ns-richedit-editstream) structure.


```C++
DWORD CALLBACK EditStreamCallback(DWORD_PTR dwCookie, 
                                  LPBYTE lpBuff,
                                  LONG cb, 
                                  PLONG pcb)
{
    HANDLE hFile = (HANDLE)dwCookie;
    
    if (ReadFile(hFile, lpBuff, cb, (DWORD *)pcb, NULL)) 
    {
        return 0;
    }
    
    return -1;
}

BOOL FillRichEditFromFile(HWND hwnd, LPCTSTR pszFile)
{
    BOOL fSuccess = FALSE;
    
    HANDLE hFile = CreateFile(pszFile, GENERIC_READ, 
                              FILE_SHARE_READ, 0, OPEN_EXISTING,
                              FILE_FLAG_SEQUENTIAL_SCAN, NULL);
        
    if (hFile != INVALID_HANDLE_VALUE) 
    {
        EDITSTREAM es = { 0 };
        
        es.pfnCallback = EditStreamCallback;
        es.dwCookie    = (DWORD_PTR)hFile;
        
        if (SendMessage(hwnd, EM_STREAMIN, SF_RTF, (LPARAM)&es) && es.dwError == 0) 
        {
                fSuccess = TRUE;
        }
        
        CloseHandle(hFile);
    }
    
    return fSuccess;
    
}
```



## Related topics

<dl> <dt>

[Using Rich Edit Controls](using-rich-edit-controls.md)
</dt> <dt>

[Windows common controls demo (CppWindowsCommonControls)](https://github.com/microsoftarchive/msdn-code-gallery-microsoft/tree/master/OneCodeTeam/Windows%20common%20controls%20demo%20(CppWindowsCommonControls)/%5BC++%5D-Windows%20common%20controls%20demo%20(CppWindowsCommonControls)/C++/CppWindowsCommonControls)
</dt> </dl>

 

 




