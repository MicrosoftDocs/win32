---
description: The Shell provides a number of ways to manage file systems.
ms.assetid: d9ffda6f-adc0-44a3-b410-e23bf5f4f165
title: Managing the File System
ms.topic: article
ms.date: 05/31/2018
---

# Managing the File System

The Shell provides a number of ways to manage file systems. The Shell provides a function, [**SHFileOperation**](/windows/desktop/api/Shellapi/nf-shellapi-shfileoperationa), that allows an application to programmatically move, copy, rename, and delete files. The Shell also supports some additional file management capabilities.

-   HTML documents can be *connected* to related files, such as graphics files or style sheets. When the document is moved or copied, the connected files are automatically moved or copied as well.
-   For systems that are available to more than one user, files can be managed on a per-user basis. Users have easy access to their data files, but not to files belonging to other users.
-   If document files are added or modified, they can be added to the Shell's list of recent documents. When the user clicks the **Documents** command on the Start menu, a list of links to the documents appears.

This document discusses how these file management technologies work. It then outlines how to use the Shell to move, copy, rename, and delete files, and how to manage objects in the Recycle Bin.

-   [Per-User File Management](#per-user-file-management)
-   [My Documents and My Pictures Folders](#my-documents-and-my-pictures-folders)
-   [Connected Files](#connected-files)
-   [Moving, Copying, Renaming, and Deleting Files](#moving-copying-renaming-and-deleting-files)
    -   [Notifying the Shell](#notifying-the-shell)
-   [Simple Example of Managing Files with SHFileOperation](#simple-example-of-managing-files-with-shfileoperation)
-   [Adding Files to the Shell's List of Recent Documents](#adding-files-to-the-shells-list-of-recent-documents)

## Per-User File Management

The Windows 2000 Shell allows files to be associated with a particular user so the files remain hidden from other users. In terms of the file system, the files are stored under the user's profile folder, typically C:\\Documents and Settings\\*Username*\\ on Windows 2000 systems. This feature allows many individuals to use the same computer, while maintaining the privacy of their files from other users. Different users can have different programs available. It also provides a straightforward way for administrators and applications to store such things as initialization (.ini) or link (.lnk) files. Applications can thus preserve a different state for each user and easily recover that particular state when needed. There is also a profile folder for storing information that is common to all users.

Because it is inconvenient to determine which user is logged in and where their files are located, the standard per-user folders are special folders and are identified by a [**CSIDL**](csidl.md). For instance, the CSIDL for the per-user Program Files folder is CSIDL\_PROGRAMS. If your application calls [**SHGetFolderLocation**](/windows/desktop/api/shlobj_core/nf-shlobj_core-shgetfolderlocation) or [**SHGetFolderPath**](/windows/desktop/api/shlobj_core/nf-shlobj_core-shgetfolderpatha) with one of the per-user CSIDLs, the function returns the pointer to an item identifier list (PIDL) or path appropriate to the currently logged-in user. If your application needs to retrieve the path or PIDL of the profile folder, its CSIDL is **CSIDL\_PROFILE**.

## My Documents and My Pictures Folders

One of the standard icons found on the desktop is **My Documents**. When you open this folder, it contains the current user's document files. The desktop instance of My Documents is a virtual folder—an alias to the file system location used to physically store the user's documents—located immediately below the desktop in the namespace hierarchy.

The purpose of the My Documents and My Pictures folders is to provide a straightforward and secure way for users to access their document and picture files on a system that might have multiple users. Each user is assigned separate file system folders for his or her files. For example, the location of a user's documents folder in the file system is typically something like C:\\Documents and Settings\\*username*\\My Documents. There is no need for users to know anything about the physical location of their file system folders. They simply access their files through the My Documents icon.

> [!Note]  
> My Documents allows a user to access his or her own files but not those of any other user. If multiple individuals use the same computer, an administrator can lock users out of the part of the file system where the actual files are stored. Users will thus be able to work on their own documents through the My Documents folder but not on documents that belong to any other users.

 

There is usually no need for an application to know which user is logged in or where in the file system that user's My Documents folder is located. Instead, your application can retrieve the PIDL of the My Documents desktop icon by calling the desktop's [**IShellFolder::ParseDisplayName**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ishellfolder-parsedisplayname) method. The parsing name used to identify the My Documents folder is not a file path but rather ::{450d8fba-ad25-11d0-98a8-0800361b1103}. The bracketed expression is the text form of the My Documents GUID. For example, to retrieve the PIDL of My Documents, your application should use this call to **IShellFolder::ParseDisplayName**.


```C++
hr = psfDeskTop->ParseDisplayName(NULL, 
                                  NULL, 
                                  L"::{450d8fba-ad25-11d0-98a8-0800361b1103}", 
                                  &chEaten, 
                                  &pidlDocFiles, 
                                  NULL);
```



Once your application has the My Documents PIDL, it can handle the folder just as it would a normal file system folder—enumerating items, parsing, binding, and performing any other valid folder operations. The Shell automatically maps changes in My Documents or its subfolders to the appropriate file system folders.

If your application needs access to the actual file system folder that contains the current user's documents, pass CSIDL\_PERSONAL to [**SHGetFolderLocation**](/windows/desktop/api/shlobj_core/nf-shlobj_core-shgetfolderlocation). The function returns the PIDL of the file system folder that is displayed in the current user's My Documents folder.

## Connected Files

HTML documents often have a number of associated graphics files, a style sheet file, several Microsoft JScript (compatible with ECMA 262 language specification ) files, and so on. When you move or copy the primary HTML document, you also usually want to move or copy its associated files to avoid breaking links. Unfortunately, there has been no easy way until now to determine which files are related to any given HTML document other than by analyzing their contents. To alleviate this problem, Windows 2000 provides a simple way to *connect* a primary HTML document to its group of associated files. If file connection is enabled, when the document is moved or copied all its connected files go with it.

To create a group of connected files, the primary document must have an .htm or .html file name extension. Create a subfolder of the primary document's parent folder. The subfolder's name must be the name of the primary document, minus the .htm or .html extension, followed by one of the extensions listed below. The most commonly used extensions are ".files" or "\_files". For instance, if the primary document is named MyDoc.htm, naming the subfolder "MyDoc\_files" defines the subfolder as the container for the document's connected files. If the primary document is moved or copied, the subfolder and its files are moved or copied as well.

For some languages, it is possible to use a localized equivalent of "\_files" to create a subfolder for connected files. The following table lists the valid strings that can be appended to a document name to create a connected files subfolder. Note that some of these strings have '-' as their first character rather than '\_' or '.'.



|              |               |                 |               |
|--------------|---------------|-----------------|---------------|
| "\_archivos" | "\_arquivos"  | "\_bestanden"   | "\_bylos"     |
| "-Dateien"   | "\_datoteke"  | "\_dosyalar"    | "\_elemei"    |
| "\_failid"   | "\_fails"     | "\_fajlovi"     | "\_ficheiros" |
| "\_fichiers" | "-filer"      | ".files"        | "\_files"     |
| "\_file"     | "\_fitxers"   | "\_fitxategiak" | "\_pliki"     |
| "\_soubory"  | "\_tiedostot" |                 |               |



 

> [!Note]  
> This feature is sensitive to the case of the extension. For instance, for the example given above, a subfolder named "MyDoc\_Files" will not be connected to MyDoc.htm.

 

Whether file connection is enabled or disabled is controlled by a **REG\_DWORD** value, NoFileFolderConnection, of the following registry key.

```
HKEY_CURRENT_USER
   Software
      Microsoft
         Windows
            CurrentVersion
               Explorer
```

This value normally is not defined, and file connection is enabled. If necessary, you can disable file connection by adding this value to the key and setting it to 1. To enable file connection again, set NoFileFolderConnection to zero.

> [!Note]  
> File connection should normally be enabled because other applications might depend on it. Disable file connection only if absolutely necessary.

 

## Moving, Copying, Renaming, and Deleting Files

The namespace is not static, and applications commonly need to manage the file system by performing one of the following operations.

-   Copying an object to another folder.
-   Moving an object to another folder.
-   Deleting an object.
-   Renaming an object.

These operations are all performed with [**SHFileOperation**](/windows/desktop/api/Shellapi/nf-shellapi-shfileoperationa). This function takes one or more source files and produces corresponding destination files. In the case of the delete operation, the system attempts to put the deleted files into the Recycle Bin.

It is also possible to move files using the [drag-and-drop](dragdrop.md) functionality.

To use the function, you must fill in the members of an [**SHFILEOPSTRUCT**](/windows/desktop/api/Shellapi/ns-shellapi-shfileopstructa) structure and pass it to [**SHFileOperation**](/windows/desktop/api/Shellapi/nf-shellapi-shfileoperationa). The key members of the structure are **pFrom** and **pTo**.

The **pFrom** member is a double **null**-terminated string that contains one or more source file names. These names can be either fully qualified paths or standard DOS wildcards such as \*.\*. Although this member is declared as a **null**-terminated string, it is used as a buffer to hold multiple file names. Each file name must be terminated by the usual single **NULL** character. An additional **NULL** character must be appended to the end of the final name to indicate the end of **pFrom**.

The **pTo** member is a double **null**-terminated string, much like **pFrom**. The **pTo** member contains the names of one or more fully qualified destination names. They are packed into **pTo** in the same way as they are for **pFrom**. If **pTo** contains multiple names, you must also set the **FOF\_MULTIDESTFILES** flag in the **fFlags** member. The usage of **pTo** depends on the operation as described here.

-   For copy and move operations, if all the files are going to a single directory, **pTo** contains the fully qualified directory name. If the files are going to different destinations, **pTo** can also contain one fully qualified directory or file name for each source file. If a directory does not exist, the system creates it.
-   For rename operations, **pTo** contains one fully qualified path for each source file in **pFrom**.
-   For delete operations, **pTo** is not used.

### Notifying the Shell

Notify the Shell of the change after using [**SHFileOperation**](/windows/desktop/api/Shellapi/nf-shellapi-shfileoperationa) to move, copy, rename, or delete files, or after taking any other action that affects the namespace. Actions that should be accompanied by notification include the following:

-   Adding or deleting files or folders.
-   Moving, copying, or renaming files or folders.
-   Changing a file association.
-   Changing file attributes.
-   Adding or removing drives or storage media.
-   Creating or disabling a shared folder.
-   Changing the system image list.

An application notifies the Shell by calling [**SHChangeNotify**](/windows/desktop/api/shlobj_core/nf-shlobj_core-shchangenotify) with the details of what has changed. The Shell can then update its image of the namespace to accurately reflect its new state.

## Simple Example of Managing Files with SHFileOperation

The following sample console application illustrates the use of [**SHFileOperation**](/windows/desktop/api/Shellapi/nf-shellapi-shfileoperationa) to copy files from one directory to another. The source and destination directories, C:\\My\_Docs and C:\\My\_Docs2, are hard-coded into the application for simplicity.


```C++
#include <shlobj.h>
#include <shlwapi.h>
#include <strsafe.h>

int main(void)
{
    IShellFolder *psfDeskTop = NULL;
    IShellFolder *psfDocFiles = NULL;
    LPITEMIDLIST pidlDocFiles = NULL;
    LPITEMIDLIST pidlItems = NULL;
    IEnumIDList *ppenum = NULL;
    SHFILEOPSTRUCT sfo;
    STRRET strDispName;
    TCHAR szParseName[MAX_PATH];
    TCHAR szSourceFiles[256];
    int i;
    int iBufPos = 0;
    ULONG chEaten;
    ULONG celtFetched;
    size_t ParseNameSize = 0;
    HRESULT hr;
    

    szSourceFiles[0] = '\0';
    hr = SHGetDesktopFolder(&psfDeskTop);

    hr = psfDeskTop->ParseDisplayName(NULL, NULL, L"c:\\My_Docs", 
         &chEaten, &pidlDocFiles, NULL);
    hr = psfDeskTop->BindToObject(pidlDocFiles, NULL, IID_IShellFolder, 
         (LPVOID *) &psfDocFiles);
    hr = psfDeskTop->Release();

    hr = psfDocFiles->EnumObjects(NULL,SHCONTF_FOLDERS | SHCONTF_NONFOLDERS, 
         &ppenum);

    while( (hr = ppenum->Next(1,&pidlItems, &celtFetched)) == S_OK 
       && (celtFetched) == 1)
    {
        psfDocFiles->GetDisplayNameOf(pidlItems, SHGDN_FORPARSING, 
            &strDispName);
        StrRetToBuf(&strDispName, pidlItems, szParseName, MAX_PATH);
        
        hr = StringCchLength(szParseName, MAX_PATH, &ParseNameSize);
        
        if (SUCCEEDED(hr))
        {
            for(i=0; i<=ParseNameSize; i++)
            {
                szSourceFiles[iBufPos++] = szParseName[i];
            }
            CoTaskMemFree(pidlItems);
        }
    }
    ppenum->Release();
    
    szSourceFiles[iBufPos] = '\0';

    sfo.hwnd = NULL;
    sfo.wFunc = FO_COPY;
    sfo.pFrom = szSourceFiles;
    sfo.pTo = "c:\\My_Docs2\0";
    sfo.fFlags = FOF_SILENT | FOF_NOCONFIRMATION | FOF_NOCONFIRMMKDIR;

    hr = SHFileOperation(&sfo);
    
    SHChangeNotify(SHCNE_UPDATEDIR, SHCNF_PATH, (LPCVOID) "c:\\My_Docs2", 0);

    CoTaskMemFree(pidlDocFiles);
    psfDocFiles->Release();

    return 0;
}
```



The application first retrieves a pointer to the desktop's [**IShellFolder**](/windows/win32/api/shobjidl_core/nn-shobjidl_core-ishellfolder) interface. It then retrieves the source directory's PIDL by passing its fully qualified path to [**IShellFolder::ParseDisplayName**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ishellfolder-parsedisplayname). Note that **IShellFolder::ParseDisplayName** requires the directory's path to be a Unicode string. The application then binds to the source directory and uses its **IShellFolder** interface to retrieve an enumerator object's [**IEnumIDList**](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-ienumidlist) interface.

As each file in the source directory is enumerated, [**IShellFolder::GetDisplayNameOf**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ishellfolder-getdisplaynameof) is used to retrieve its name. The SHGDN\_FORPARSING flag is set, which causes **IShellFolder::GetDisplayNameOf** to return the file's fully qualified path. The file paths, including the terminating **NULL** characters, are concatenated into a single array, *szSourceFiles*. A second **NULL** character is appended to the final path to terminate the array properly.

Once the enumeration is complete, the application assigns values to an [**SHFILEOPSTRUCT**](/windows/desktop/api/Shellapi/ns-shellapi-shfileopstructa) structure. Note that the array assigned to **pTo** to specify the destination must also be terminated by a double **NULL**. In this case, it is simply included in the string that is assigned to **pTo**. Because this is a console application, the FOF\_SILENT, FOF\_NOCONFIRMATION, and FOF\_NOCONFIRMMKDIR flags are set to suppress any dialog boxes that might appear. After [**SHFileOperation**](/windows/desktop/api/Shellapi/nf-shellapi-shfileoperationa) returns, [**SHChangeNotify**](/windows/desktop/api/shlobj_core/nf-shlobj_core-shchangenotify) is called to notify the Shell of the change. Then the application performs the usual cleanup and returns.

## Adding Files to the Shell's List of Recent Documents

The Shell maintains a list of recently added or modified documents for each user. The user can display a list of links to these files by clicking Documents on the Start menu. As with My Documents, each user has a file system directory to hold the actual links. To retrieve the PIDL of the current user's Recent directory, your application can call [**SHGetFolderLocation**](/windows/desktop/api/shlobj_core/nf-shlobj_core-shgetfolderlocation) with CSIDL\_RECENT, or call [**SHGetFolderPath**](/windows/desktop/api/shlobj_core/nf-shlobj_core-shgetfolderpatha) to retrieve its path.

Your application can enumerate the contents of the Recent folder using the techniques discussed earlier in this document. However, an application should not modify the contents of the folder as if it were a normal file system folder. If it does so, the Shell's list of recent documents will not be updated properly, and the changes will not be reflected in the Start menu. Instead, to add a document link to a user's Recent folder, your application can call [**SHAddToRecentDocs**](/windows/desktop/api/shlobj_core/nf-shlobj_core-shaddtorecentdocs). The Shell will add a link to the appropriate file system folder, as well as updating its list of recent documents and the Start menu. You can also use this function to clear the folder.

 

 
