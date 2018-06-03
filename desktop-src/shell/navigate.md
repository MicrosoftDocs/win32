---
Description: You now have all the essential elements needed to navigate anywhere in the namespace.
ms.assetid: b65bc979-db32-48b3-b71f-fd389957b265
title: Navigating the Namespace
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Navigating the Namespace

You now have all the essential elements needed to navigate anywhere in the namespace. The simplest way to start is to have your application call [**SHGetDesktopFolder**](/windows/desktop/api/shlobj_core/nf-shlobj_core-shgetdesktopfolder) to retrieve the desktop's [**IShellFolder**](/windows/desktop/api/Shobjidl/nn-shobjidl_core-ishellfolder) interface. Then, to navigate downward through the namespace, your application can follow these steps:

1.  Enumerate the folder's contents.
2.  Determine which objects are subfolders, and select one.
3.  Bind to the subfolder to retrieve its [**IShellFolder**](/windows/desktop/api/Shobjidl/nn-shobjidl_core-ishellfolder) interface.

Repeat these steps as often as necessary to reach the target.

## A Simple Example of Namespace Navigation

The following piece of sample code is a simple console application that illustrates a number of the procedures discussed in the preceding sections. Error checking has been omitted for clarity. The application performs the following tasks:

1.  Retrieves the Program Files folder's [**IShellFolder**](/windows/desktop/api/Shobjidl/nn-shobjidl_core-ishellfolder) interface ([Using the IShellFolder Interface](folder-info.md)).
2.  Enumerates the contents of the folder ([Enumerating the Contents of a Folder](folder-info.md)).
3.  Determines all the display names and prints them ([Determining Display Names and Other Properties](folder-info.md)).
4.  Looks for a subfolder ([Getting a Pointer to a Subfolder's IShellFolder Interface](folder-info.md)).
5.  Binds to the first subfolder it finds ([Getting a Pointer to a Subfolder's IShellFolder Interface](folder-info.md)).
6.  Prints the display names of the objects in the subfolder.


```
#include <shlobj.h>
#include <shlwapi.h>
#include <iostream.h>

main()
{
    LPITEMIDLIST pidlProgFiles = NULL;
    LPITEMIDLIST pidlItems = NULL;
    IShellFolder *psfFirstFolder = NULL;
    IShellFolder *psfDeskTop = NULL;
    IShellFolder *psfProgFiles = NULL;
    LPENUMIDLIST ppenum = NULL;
    ULONG celtFetched;
    HRESULT hr;
    STRRET strDispName;
    TCHAR pszDisplayName[MAX_PATH];
    ULONG uAttr;
   
    CoInitialize( NULL );
    
    hr = SHGetFolderLocation(NULL, CSIDL_PROGRAM_FILES, NULL, NULL, &amp;pidlProgFiles);

    hr = SHGetDesktopFolder(&amp;psfDeskTop);

    hr = psfDeskTop->BindToObject(pidlProgFiles, NULL, IID_IShellFolder, (LPVOID *) &amp;psfProgFiles);
    psfDeskTop->Release();

    hr = psfProgFiles->EnumObjects(NULL,SHCONTF_FOLDERS | SHCONTF_NONFOLDERS, &amp;ppenum);

    while( hr = ppenum->Next(1,&amp;pidlItems, &amp;celtFetched) == S_OK &amp;&amp; (celtFetched) == 1)
    {
        psfProgFiles->GetDisplayNameOf(pidlItems, SHGDN_INFOLDER, &amp;strDispName);
        StrRetToBuf(&amp;strDispName, pidlItems, pszDisplayName, MAX_PATH);
        cout << pszDisplayName << '\n';
        if(!psfFirstFolder)
        {
            uAttr = SFGAO_FOLDER;
            psfProgFiles->GetAttributesOf(1, (LPCITEMIDLIST *) &amp;pidlItems, &amp;uAttr);
            if(uAttr & SFGAO_FOLDER)
            {
                hr = psfProgFiles->BindToObject(pidlItems, NULL, IID_IShellFolder, (LPVOID *) &amp;psfFirstFolder);
            }
        }
        CoTaskMemFree(pidlItems);
    }

    cout << "\n\n";

    ppenum->Release();

    if(psfFirstFolder)
    {
        hr = psfFirstFolder->EnumObjects(NULL,SHCONTF_FOLDERS | SHCONTF_NONFOLDERS, &amp;ppenum);

        while( hr = ppenum->Next(1,&amp;pidlItems, &amp;celtFetched) == S_OK &amp;&amp; (celtFetched) == 1)
        {
            psfFirstFolder->GetDisplayNameOf(pidlItems, SHGDN_INFOLDER, &amp;strDispName);
            StrRetToBuf(&amp;strDispName, pidlItems, pszDisplayName, MAX_PATH);
            cout << pszDisplayName << '\n';
            CoTaskMemFree(pidlItems);
        }
    }

    ppenum->Release();
    CoTaskMemFree(pidlProgFiles);
    psfProgFiles->Release();
    psfFirstFolder->Release();

    CoUninitialize();
    return 0;
}
```



 

 



