---
title: How to Use Progress Bar Controls
description: This topic explains how to use a progress bar to indicate the progress of a lengthy file-parsing operation.
ms.assetid: 4CC25F3A-9CAF-4ADC-B29C-3FACDD73D5A0
ms.topic: article
ms.date: 05/31/2018
---

# How to Use Progress Bar Controls

This topic explains how to use a progress bar to indicate the progress of a lengthy file-parsing operation.

## What you need to know

### Technologies

-   [Windows Controls](window-controls.md)

### Prerequisites

-   C/C++
-   Windows User Interface Programming

## Instructions

### Create a Progress Bar Control

The following example code creates a progress bar and positions it along the bottom of the parent window's client area. The height of the progress bar is based on the height of the arrow bitmap used in a scroll bar. The range is based on the size of the file divided by 2,048, which is the size of each "chunk" of data that is read from the file. The example also sets an increment and advances the current position of the progress bar by the increment after parsing each chunk.


```C++
// ParseALargeFile - uses a progress bar to indicate the progress of a parsing operation.
//
// Returns TRUE if successful, or FALSE otherwise.
//
// hwndParent - parent window of the progress bar.
//
// lpszFileName - name of the file to parse. 
// 
// Global variable 
//     g_hinst - instance handle.
//

extern HINSTANCE g_hinst; 

BOOL ParseALargeFile(HWND hwndParent, LPTSTR lpszFileName) 
{ 
    RECT rcClient;  // Client area of parent window.
    int cyVScroll;  // Height of scroll bar arrow.
    HWND hwndPB;    // Handle of progress bar.
    HANDLE hFile;   // Handle of file.
    DWORD cb;       // Size of file and count of bytes read.
    LPCH pch;       // Address of data read from file.
    LPCH pchTmp;    // Temporary pointer.

    // Ensure that the common control DLL is loaded, and create a progress bar 
    // along the bottom of the client area of the parent window. 
    //
    // Base the height of the progress bar on the height of a scroll bar arrow.
    
    InitCommonControls(); 
    
    GetClientRect(hwndParent, &rcClient); 
    
    cyVScroll = GetSystemMetrics(SM_CYVSCROLL); 

    hwndPB = CreateWindowEx(0, PROGRESS_CLASS, (LPTSTR) NULL, 
                            WS_CHILD | WS_VISIBLE, rcClient.left, 
                            rcClient.bottom - cyVScroll, 
                            rcClient.right, cyVScroll, 
                            hwndParent, (HMENU) 0, g_hinst, NULL);

    // Open the file for reading, and retrieve the size of the file. 

    hFile = CreateFile(lpszFileName, GENERIC_READ, FILE_SHARE_READ, 
                       (LPSECURITY_ATTRIBUTES) NULL, OPEN_EXISTING, 
                       FILE_ATTRIBUTE_NORMAL, (HANDLE) NULL); 

    if (hFile == (HANDLE) INVALID_HANDLE_VALUE)
        return FALSE; 

    cb = GetFileSize(hFile, (LPDWORD) NULL); 

    // Set the range and increment of the progress bar. 

    SendMessage(hwndPB, PBM_SETRANGE, 0, MAKELPARAM(0, cb / 2048));
    
    SendMessage(hwndPB, PBM_SETSTEP, (WPARAM) 1, 0); 

    // Parse the file. 
    pch = (LPCH) LocalAlloc(LPTR, sizeof(char) * 2048); 
    
    pchTmp = pch; 
    
    do { 
        ReadFile(hFile, pchTmp, sizeof(char) * 2048, &cb, (LPOVERLAPPED) NULL);
        
        // TODO: Write an error handler to check that all the
        // requested data was read.
        //
        // Include here any code that parses the
        // file. 
        //  
        //  
        //  
        // Advance the current position of the progress bar by the increment.
        
        SendMessage(hwndPB, PBM_STEPIT, 0, 0); 
        
    } while (cb); 

    CloseHandle((HANDLE) hFile);
    
    DestroyWindow(hwndPB);

    return TRUE; 
}
```



## Remarks

You must make sure to use the [**ReadFile**](/windows/desktop/api/fileapi/nf-fileapi-readfile) function correctly, to ensure the security of your application. For instance, in the example code, you should check to make sure that `ReadFile` actually reads all of the requested data.

Also notice that the fourth parameter of [**CreateFile**](/windows/desktop/api/fileapi/nf-fileapi-createfilea)—(LPSECURITY\_ATTRIBUTES)**NULL**—sets default security values. If you need specific security settings, you must set the appropriate values in the structure's members. Call **sizeof** to set the correct size of the **LPSECURITY\_ATTRIBUTES** structure.

For more information, see [Security Considerations: Microsoft Windows Controls](sec-comctls.md).

## Related topics

<dl> <dt>

[Using Progress Bar Controls](using-progress-bar-controls.md)
</dt> <dt>

[Security Considerations: Microsoft Windows Controls](sec-comctls.md)
</dt> </dl>

 

 