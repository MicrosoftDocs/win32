---
description: Once your application has located a file object, the next step is often to act on it in some way.
ms.assetid: d774c3b2-4caf-460a-ac32-0ed603491d5f
title: Launching Applications (ShellExecute, ShellExecuteEx, SHELLEXECUTEINFO)
ms.topic: article
ms.date: 05/31/2018
---

# Launching Applications (ShellExecute, ShellExecuteEx, SHELLEXECUTEINFO)

Once your application has located a file object, the next step is often to act on it in some way. For instance, your application might want to launch another application that allows the user to modify a data file. If the file of interest is an executable, your application might want to simply launch it. This document discusses how to use [**ShellExecute**](/windows/desktop/api/Shellapi/nf-shellapi-shellexecutea) or [**ShellExecuteEx**](/windows/desktop/api/Shellapi/nf-shellapi-shellexecuteexa) to perform these tasks.

-   [Using ShellExecute and ShellExecuteEx](#using-shellexecute-and-shellexecuteex)
    -   [Object Verbs](#object-verbs)
    -   [Using ShellExecuteEx to Provide Activation Services from a Site](#using-shellexecuteex-to-provide-activation-services-from-a-site)
    -   [Using ShellExecute to Launch the Search Dialog Box](#using-shellexecute-to-launch-the-search-dialog-box)
-   [A Simple Example of How to Use ShellExecuteEx](#a-simple-example-of-how-to-use-shellexecuteex)

## Using ShellExecute and ShellExecuteEx

To use [**ShellExecute**](/windows/desktop/api/Shellapi/nf-shellapi-shellexecutea) or [**ShellExecuteEx**](/windows/desktop/api/Shellapi/nf-shellapi-shellexecuteexa), your application must specify the file or folder object that is to be acted on, and a *verb* that specifies the operation. For **ShellExecute**, assign these values to the appropriate parameters. For **ShellExecuteEx**, fill in the appropriate members of a [**SHELLEXECUTEINFO**](/windows/desktop/api/Shellapi/ns-shellapi-shellexecuteinfoa) structure. There are also several other members or parameters that can be used to fine-tune the behavior of the two functions.

File and folder objects can be part of the file system or virtual objects, and they can be identified by either paths or pointers to item identifier lists (PIDLs).

### Object Verbs

The verbs available for an object are essentially the items that you find on an object's shortcut menu. To find which verbs are available, look in the registry under

**HKEY\_CLASSES\_ROOT**\\**CLSID**\\*{object\_clsid}*\\**Shell**\\*verb*

where *object\_clsid* is the class identifier (CLSID) of the object, and *verb* is the name of the available verb. The *verb*\\**command** subkey contains the data indicating what happens when that verb is invoked.

To find out which verbs are available for [predefined Shell objects](handlers.md), look in the registry under

**HKEY\_CLASSES\_ROOT**\\*object\_name*\\**shell**\\*verb*

where *object\_name* is the name of the predefined Shell object. Again, the *verb*\\**command** subkey contains the data indicating what happens when that verb is invoked.

Commonly available verbs include:



| Verb       | Description                                                                                              |
|------------|----------------------------------------------------------------------------------------------------------|
| edit       | Launches an editor and opens the document for editing.                                                   |
| find       | Initiates a search starting from the specified directory.                                                |
| open       | Launches an application. If this file is not an executable file, its associated application is launched. |
| print      | Prints the document file.                                                                                |
| properties | Displays the object's properties.                                                                        |
| runas      | Launches an application as Administrator. User Account Control (UAC) will prompt the user for consent to |
|            | run the application elevated or enter the credentials of an administrator account used to run the        |
|            | application.                                                                                             |

 

Each verb corresponds to the command that would be used to launch the application from a console window. The **open** verb is a good example, as it is commonly supported. For .exe files, **open** simply launches the application. However, it is more commonly used to launch an application that operates on a particular file. For instance, .txt files can be opened by Microsoft WordPad. The **open** verb for a .txt file would thus correspond to something like the following command:


```C++
C:\Program Files\Windows NT\Accessories\Wordpad.exe" "%1"
```



When you use [**ShellExecute**](/windows/desktop/api/Shellapi/nf-shellapi-shellexecutea) or [**ShellExecuteEx**](/windows/desktop/api/Shellapi/nf-shellapi-shellexecuteexa) to open a .txt file, Wordpad.exe is launched with the specified file as its argument. Some commands can have additional arguments, such as flags, that can be added as needed to launch the application properly. For further discussion of shortcut menus and verbs, see [Extending Shortcut Menus](context.md).

In general, trying to determine the list of available verbs for a particular file is somewhat complicated. In many cases, you can simply set the *lpVerb* parameter to **NULL**, which invokes the default command for the file type. This procedure is usually equivalent to setting *lpVerb* to "open", but some file types may have a different default command. For further information, see [Extending Shortcut Menus](context.md) and the [**ShellExecuteEx**](/windows/desktop/api/Shellapi/nf-shellapi-shellexecuteexa) reference documentation.

### Using ShellExecuteEx to Provide Activation Services from a Site

A site chain's services can control many behaviors of item activation. As of Windows 8, you can provide a pointer to the site chain to [**ShellExecuteEx**](/windows/desktop/api/Shellapi/nf-shellapi-shellexecuteexa) to enable these behaviors. To provide the site to **ShellExecuteEx**:

-   Specify the SEE\_MASK\_FLAG\_HINST\_IS\_SITE flag in the **fMask** member of [**SHELLEXECUTEINFO**](/windows/desktop/api/Shellapi/ns-shellapi-shellexecuteinfoa).
-   Provide the [**IUnknown**](/windows/win32/api/unknwn/nn-unknwn-iunknown) in the **hInstApp** member of [**SHELLEXECUTEINFO**](/windows/desktop/api/Shellapi/ns-shellapi-shellexecuteinfoa).

### Using ShellExecute to Launch the Search Dialog Box

When a user right-clicks a folder icon in Windows Explorer, one of the menu items is "Search". If they select that item, the Shell launches its Search utility. This utility displays a dialog box that can be used to search files for a specified text string. An application can programmatically launch the Search utility for a directory by calling [**ShellExecute**](/windows/desktop/api/Shellapi/nf-shellapi-shellexecutea), with "find" as the *lpVerb* parameter, and the directory path as the *lpFile* parameter. For instance, the following line of code launches the Search utility for the c:\\MyPrograms directory.


```C++
ShellExecute(hwnd, "find", "c:\\MyPrograms", NULL, NULL, 0);
```



## A Simple Example of How to Use ShellExecuteEx

The following sample console application illustrates the use of [**ShellExecuteEx**](/windows/desktop/api/Shellapi/nf-shellapi-shellexecuteexa). Most error checking code has been omitted for clarity.


```C++
#include <shlobj.h>
#include <shlwapi.h>
#include <objbase.h>

main()
{
    LPITEMIDLIST pidlWinFiles = NULL;
    LPITEMIDLIST pidlItems = NULL;
    IShellFolder *psfWinFiles = NULL;
    IShellFolder *psfDeskTop = NULL;
    LPENUMIDLIST ppenum = NULL;
    STRRET strDispName;
    TCHAR pszParseName[MAX_PATH];
    ULONG celtFetched;
    SHELLEXECUTEINFO ShExecInfo;
    HRESULT hr;
    BOOL fBitmap = FALSE;

    hr = SHGetFolderLocation(NULL, CSIDL_WINDOWS, NULL, NULL, &pidlWinFiles);

    hr = SHGetDesktopFolder(&psfDeskTop);

    hr = psfDeskTop->BindToObject(pidlWinFiles, NULL, IID_IShellFolder, (LPVOID *) &psfWinFiles);
    hr = psfDeskTop->Release();

    hr = psfWinFiles->EnumObjects(NULL,SHCONTF_FOLDERS | SHCONTF_NONFOLDERS, &ppenum);

    while( hr = ppenum->Next(1,&pidlItems, &celtFetched) == S_OK && (celtFetched) == 1)
    {
        psfWinFiles->GetDisplayNameOf(pidlItems, SHGDN_FORPARSING, &strDispName);
        StrRetToBuf(&strDispName, pidlItems, pszParseName, MAX_PATH);
        CoTaskMemFree(pidlItems);
        if(StrCmpI(PathFindExtension(pszParseName), TEXT( ".bmp")) == 0)
        {
            fBitmap = TRUE;
            break;
        }
    }

    ppenum->Release();

    if(fBitmap)
    {
        ShExecInfo.cbSize = sizeof(SHELLEXECUTEINFO);
        ShExecInfo.fMask = NULL;
        ShExecInfo.hwnd = NULL;
        ShExecInfo.lpVerb = NULL;
        ShExecInfo.lpFile = pszParseName;
        ShExecInfo.lpParameters = NULL;
        ShExecInfo.lpDirectory = NULL;
        ShExecInfo.nShow = SW_MAXIMIZE;
        ShExecInfo.hInstApp = NULL;

        ShellExecuteEx(&ShExecInfo);
    }

    CoTaskMemFree(pidlWinFiles);
    psfWinFiles->Release();

    return 0;
}
```



The application first retrieves the PIDL of the Windows directory, and enumerates its contents until it finds the first .bmp file. Unlike the earlier example, [**IShellFolder::GetDisplayNameOf**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ishellfolder-getdisplaynameof) is used to retrieve the file's parsing name instead of its display name. Because this is a file system folder, the parsing name is a fully qualified path, which is what is needed for [**ShellExecuteEx**](/windows/desktop/api/Shellapi/nf-shellapi-shellexecuteexa).

Once the first .bmp file has been located, appropriate values are assigned to the members of a [**SHELLEXECUTEINFO**](/windows/desktop/api/Shellapi/ns-shellapi-shellexecuteinfoa) structure. The **lpFile** member is set to the parsing name of the file, and the **lpVerb** member to **NULL**, to begin the default operation. In this case, the default operation is "open". The structure is then passed to [**ShellExecuteEx**](/windows/desktop/api/Shellapi/nf-shellapi-shellexecuteexa), which launches the default handler for bitmap files, typically MSPaint.exe, to open the file. After the function returns, the PIDLs are freed and the Windows folder's [**IShellFolder**](/windows/win32/api/shobjidl_core/nn-shobjidl_core-ishellfolder) interface is released.

 

 
