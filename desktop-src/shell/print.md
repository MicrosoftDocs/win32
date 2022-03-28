---
description: The Shell API provides functions that you can use to manage networked printers. If a file has the print verb associated with it, you can use the ShellExecuteEx command to print it.
ms.assetid: b94fca60-237a-43b1-a75a-faccf9dc63fb
title: Managing Printers
ms.topic: article
ms.date: 05/31/2018
---

# Managing Printers

The Shell API provides functions that you can use to manage networked printers. If a file has the **print** verb associated with it, you can use the [**ShellExecuteEx**](/windows/desktop/api/Shellapi/nf-shellapi-shellexecuteexa) command to print it.

- [Printer Management](#printer-management)
- [Printing Files with ShellExecuteEx](#printing-files-with-shellexecuteex)

## Printer Management

You can manage printers on a system with the [**SHInvokePrinterCommand**](/windows/desktop/api/Shellapi/nf-shellapi-shinvokeprintercommanda) function. This function allows you to:

-   Install printers.
-   Open printers.
-   Get printer properties.
-   Create printer links.
-   Print a test page.

## Printing Files with ShellExecuteEx

If a file type has a print command associated with it, you can print the file by calling [**ShellExecuteEx**](/windows/desktop/api/Shellapi/nf-shellapi-shellexecuteexa) with **print** as the verb. This command is often the same as that used for the **open** verb, with the addition of a flag to tell the application to print the file. For instance, .txt files can be printed by Microsoft WordPad. The **open** verb for a .txt file would thus correspond to something like the following command:


```C++
"C:\Program Files\Windows NT\Accessories\Wordpad.exe" /p "%1"
```



When you use [**ShellExecuteEx**](/windows/desktop/api/Shellapi/nf-shellapi-shellexecuteexa) to print a .txt file, WordPad opens the file, prints it, and then closes, returning control to the application. The following sample function takes a fully qualified path, and uses **ShellExecuteEx** to print it, using the print command associated with its file name extension.


```C++
#include <shlobj.h>

HINSTANCE PrintFile(LPCTSTR pszFileName)
{
    SHELLEXECUTEINFO ShExecInfo;
    HINSTANCE hInst;

    // Fill the SHELLEXECUTEINFO array.

    ShExecInfo.cbSize = sizeof(SHELLEXECUTEINFO);
    ShExecInfo.fMask = NULL;
    ShExecInfo.hwnd = NULL;
    ShExecInfo.lpVerb = "print";
    ShExecInfo.lpFile = pszFileName;  // a fully qualified path
    ShExecInfo.lpParameters = NULL;
    ShExecInfo.lpDirectory = NULL;    
    ShExecInfo.nShow = SW_MAXIMIZE;
    ShExecInfo.hInstApp = NULL;

    hInst = ShellExecuteEx(&ShExecInfo);
    
    return hInst;
}
```



 

 



