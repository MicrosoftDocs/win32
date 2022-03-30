---
description: A Shell link is a data object that contains information used to access another object in the Shell's namespace&\#8212;that is, any object visible through Windows Explorer.
ms.assetid: '32ad306d-54bd-4130-ad30-08db50ef106e'
title: Shell Links
ms.topic: article
ms.date: 05/31/2018
---

# Shell Links

A *Shell link* is a data object that contains information used to access another object in the Shell's namespace—that is, any object visible through Windows Explorer. The types of objects that can be accessed through Shell links include files, folders, disk drives, and printers. A Shell link allows a user or an application to access an object from anywhere in the namespace. The user or application does not need to know the current name and location of the object.

- [About Shell Links](#about-shell-links)
    - [Link Resolution](#link-resolution)
    - [Link Files](#link-files)
    - [Item Identifiers and Identifier Lists](#item-identifiers-and-identifier-lists)
- [Using Shell Links](#using-shell-links)
    - [Creating a Shortcut and a Folder Shortcut to a File](#creating-a-shortcut-and-a-folder-shortcut-to-a-file)
    - [Resolving a Shortcut](#resolving-a-shortcut)
    - [Creating a Shortcut to a Nonfile Object](#creating-a-shortcut-to-a-nonfile-object)

## About Shell Links

The user creates a Shell link by choosing the **Create Shortcut** command from an object's shortcut menu. The system automatically creates an icon for the Shell link by combining the object's icon with a small arrow (known as the system-defined link overlay icon) that appears in the lower left corner of the icon. A Shell link that has an icon is called a shortcut; however, the terms Shell link and shortcut are often used interchangeably. Typically, the user creates shortcuts to gain quick access to objects stored in subfolders or in shared folders on other computers. For example, a user can create a shortcut to a Microsoft Word document that is located in a subfolder and place the shortcut icon on the desktop. The user can then open the document by double-clicking the shortcut icon. If the document is moved or renamed after the shortcut is created, the system will attempt to update the shortcut the next time the user selects it.

Applications can also create and use Shell links and shortcuts. For example, a word processing application might create a Shell link to implement a list of the most recently used documents. An application creates a Shell link by using the [**IShellLink**](/windows/desktop/api/Shobjidl_core/nn-shobjidl_core-ishelllinka) interface to create a Shell link object. The application uses the [**IPersistFile**](/windows/win32/api/objidl/nn-objidl-ipersistfile) or [**IPersistStream**](/windows/win32/api/objidl/nn-objidl-ipersiststream) interface to store the object in a file or stream.

> [!Note]  
> You cannot use [**IShellLink**](/windows/desktop/api/Shobjidl_core/nn-shobjidl_core-ishelllinka) to create a link to a URL.

 

This overview describes the [**IShellLink**](/windows/desktop/api/Shobjidl_core/nn-shobjidl_core-ishelllinka) interface and explains how to use it to create and resolve Shell links from within a Microsoft Win32-based application. Because the design of Shell links is based on the OLE Component Object Model (COM), you should be familiar with the basic concepts of COM and OLE programming before reading this overview.

### Link Resolution

If a user creates a shortcut to an object and the name or location of the object is later changed, the system automatically takes steps to update, or resolve, the shortcut the next time the user selects it. However, if an application creates a Shell link and stores it in a stream, the system does not automatically attempt to resolve the link. The application must resolve the link by calling the [**IShellLink::Resolve**](/windows/win32/api/shobjidl_core/nf-shobjidl_core-ishelllinka-resolve) method.

When a Shell link is created, the system saves information about the link. When resolving a link—either automatically or with an [**IShellLink::Resolve**](/windows/win32/api/shobjidl_core/nf-shobjidl_core-ishelllinka-resolve) call—the system first retrieves the path associated with the Shell link by using a pointer to the Shell link's identifier list. For more information about the identifier list, see [Item Identifiers and Identifier Lists](#item-identifiers-and-identifier-lists). The system searches for the associated object in that path and, if it finds the object, resolves the link. If the system cannot find the object, it calls on the [Distributed Link Tracking and Object Identifiers](../fileio/distributed-link-tracking-and-object-identifiers.md) (DLT) service, if available, to locate the object. If the DLT service is not available or cannot find the object, the system looks in the same directory for an object with the same file creation time and attributes but with a different name. This type of search resolves a link to an object that has been renamed.

If the system still cannot find the object, it searches the directories, the desktop, and local volumes, looking recursively though the directory tree for an object with either the same name or creation time. If the system still does not find a match, it displays a dialog box prompting the user for a location. An application can suppress the dialog box by specifying the **SLR\_NO\_UI** value in a call to [**IShellLink::Resolve**](/windows/win32/api/shobjidl_core/nf-shobjidl_core-ishelllinka-resolve).

### Initialization of the Component Object Library

Before an application can create and resolve shortcuts, it must initialize the component object library by calling the [**CoInitialize**](/windows/win32/api/objbase/nf-objbase-coinitialize) function. Each call to **CoInitialize** requires a corresponding call to the [**CoUninitialize**](/windows/win32/api/combaseapi/nf-combaseapi-couninitialize) function, which an application should call when it terminates. The call to **CoUninitialize** ensures that the application does not terminate until it has received all of its pending messages.

### Location-Independent Names

The system provides location-independent names for Shell links to objects stored in shared folders. If the object is stored locally, the system provides the local path and file name for the object. If the object is stored remotely, the system provides a Universal Naming Convention (UNC) network resource name for the object. Because the system provides location-independent names, a Shell link can serve as a universal name for a file that can be transferred to other computers.

### Link Files

When the user creates a shortcut to an object by choosing the **Create Shortcut** command from the object's shortcut menu, Windows stores the information it needs to access the object in a link file—a binary file that has the .lnk file name extension. A link file contains the following information:

- The location (path) of the object referenced by the shortcut (called the corresponding object).
- The working directory of the corresponding object.
- The list of arguments that the system passes to the corresponding object when the [**IContextMenu::InvokeCommand**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-icontextmenu-invokecommand) method is activated for the shortcut.
- The show command used to set the initial show state of the corresponding object. This is one of the SW\_ values described in [**ShowWindow**](/windows/win32/api/winuser/nf-winuser-showwindow).
- The location (path and index) of the shortcut's icon.
- The shortcut's description string.
- The keyboard shortcut for the shortcut.

When a link file is deleted, the corresponding object is not affected.

If you create a shortcut to another shortcut, the system simply copies the link file rather than creating a new link file. In this case, the shortcuts will not be independent of each other.

An application can register a file name extension as a shortcut file type. If a file has a file name extension that has been registered as a shortcut file type, the system automatically adds the system-defined link overlay icon (a small arrow) to the file's icon. To register a file name extension as a shortcut file type, you must add the IsShortcut value to the registry description of the file name extension, as shown in the example below. Note that the Shell must be restarted for the overlay icon to take effect. IsShortcut has no data value.

```
HKEY_CLASSES_ROOT
   .xyz
      (Default) = XYZApp
   XYZApp
      IsShortcut
```

### Shortcut names

The shortcut's name, which is a string that appears below the Shell link icon, is actually the file name of the shortcut itself. The user can edit the description string by selecting it and entering a new string.

### Location of shortcuts in the namespace

A shortcut can exist on the desktop or anywhere in the Shell's namespace. Similarly, the object that is associated with the shortcut can also exist anywhere in the Shell's namespace. An application can use the [**IShellLink::SetPath**](/windows/win32/api/shobjidl_core/nf-shobjidl_core-ishelllinka-setpath) method to set the path and file name for the associated object, and the [**IShellLink::GetPath**](/windows/win32/api/shobjidl_core/nf-shobjidl_core-ishelllinka-getpath) method to retrieve the current path and file name for the object.

### Shortcut working directory

The working directory is the directory where the corresponding object of a shortcut loads or stores files when the user does not identify a specific directory. A link file contains the name of the working directory for the corresponding object. An application can set the name of the working directory for the corresponding object by using the [**IShellLink::SetWorkingDirectory**](/windows/win32/api/shobjidl_core/nf-shobjidl_core-ishelllinka-setworkingdirectory) method and can retrieve the name of the current working directory for the corresponding object by using the [**IShellLink::GetWorkingDirectory**](/windows/win32/api/shobjidl_core/nf-shobjidl_core-ishelllinka-getworkingdirectory) method.

### Shortcut command-line arguments

A link file contains command-line arguments that the Shell passes to the corresponding object when the user selects the link. An application can set the command-line arguments for a shortcut by using the [**IShellLink::SetArguments**](/windows/win32/api/shobjidl_core/nf-shobjidl_core-ishelllinka-setarguments) method. It is useful to set command-line arguments when the corresponding application, such as a linker or compiler, takes special flags as arguments. An application can retrieve the command-line arguments from a shortcut by using the [**IShellLink::GetArguments**](/windows/desktop/api/Shobjidl_core/nf-shobjidl_core-ishelllinka-getarguments) method.

### Shortcut show commands

When the user double-clicks a shortcut, the system starts the application associated with the corresponding object and sets the initial show state of the application based on the show command specified by the shortcut. The show command can be any of the SW\_ values included in the description of the [**ShowWindow**](/windows/win32/api/winuser/nf-winuser-showwindow) function. An application can set the show command for a shortcut by using the [**IShellLink::SetShowCmd**](/windows/win32/api/shobjidl_core/nf-shobjidl_core-ishelllinka-setshowcmd) method and can retrieve the current show command by using the [**IShellLink::GetShowCmd**](/windows/win32/api/shobjidl_core/nf-shobjidl_core-ishelllinka-getshowcmd) method.

### Shortcut icons

Like other Shell objects, a shortcut has an icon. The user accesses the object associated with a shortcut by double-clicking the shortcut's icon. When the system creates an icon for a shortcut, it uses the bitmap of the corresponding object and adds the system-defined link overlay icon (a small arrow) to the lower left corner. An application can set the location (path and index) of a shortcut's icon by using the [**IShellLink::SetIconLocation**](/windows/win32/api/shobjidl_core/nf-shobjidl_core-ishelllinka-seticonlocation) method. An application can retrieve this location by using the [**IShellLink::GetIconLocation**](/windows/win32/api/shobjidl_core/nf-shobjidl_core-ishelllinka-geticonlocation) method.

### Shortcut descriptions

Shortcuts have descriptions, but the user never sees them. An application can use a description to store any text information. Descriptions are set using the [**IShellLink::SetDescription**](/windows/win32/api/shobjidl_core/nf-shobjidl_core-ishelllinka-setdescription) method and retrieved using the [**IShellLink::GetDescription**](/windows/win32/api/shobjidl_core/nf-shobjidl_core-ishelllinka-getdescription) method.

### Shortcut Keyboard Shortcuts

A shortcut object can have a keyboard shortcut associated with it. Keyboard shortcuts allow a user to press a combination of keys to activate a shortcut. An application can set the keyboard shortcut for a shortcut by using the [**IShellLink::SetHotkey**](/windows/win32/api/shobjidl_core/nf-shobjidl_core-ishelllinka-sethotkey) method and can retrieve the current keyboard shortcut by using the [**IShellLink::GetHotkey**](/windows/win32/api/shobjidl_core/nf-shobjidl_core-ishelllinka-gethotkey) method.

### Item Identifiers and Identifier Lists

The Shell uses object identifiers within the Shell's namespace. All objects visible in the Shell (files, directories, servers, workgroups, and so on) have unique identifiers among the objects within their parent folder. These identifiers are called item identifiers, and they have the [**SHITEMID**](/windows/desktop/api/Shtypes/ns-shtypes-shitemid) data type as defined in the Shtypes.h header file. An item identifier is a variable-length byte stream that contains information that identifies an object within a folder. Only the creator of an item identifier knows the content and format of the identifier. The only part of an item identifier that the Shell uses is the first two bytes, which specify the size of the identifier.

Each parent folder has its own item identifier that identifies it within its own parent folder. Thus, any Shell object can be uniquely identified by a list of item identifiers. A parent folder keeps a list of identifiers for the items it contains. The list has the [**ITEMIDLIST**](/windows/desktop/api/Shtypes/ns-shtypes-itemidlist) data type. Item identifier lists are allocated by the Shell and may be passed across Shell interfaces, such as [**IShellFolder**](/windows/win32/api/shobjidl_core/nn-shobjidl_core-ishellfolder). It is important to remember that each identifier in an item identifier list is only meaningful within the context of its parent folder.

An application can set a shortcut's item identifier list by using the [**IShellLink::SetIDList**](/windows/win32/api/shobjidl_core/nf-shobjidl_core-ishelllinka-setidlist) method. This method is useful when setting a shortcut to an object that is not a file, such as a printer or disk drive. An application can retrieve a shortcut's item identifier list by using the [**IShellLink::GetIDList**](/windows/win32/api/shobjidl_core/nf-shobjidl_core-ishelllinka-getidlist) method.

## Using Shell Links

This section contains examples that demonstrate how to create and resolve shortcuts from within a Win32-based application. This section assumes you are familiar with Win32, C++, and OLE COM programming.

### Creating a Shortcut and a Folder Shortcut to a File

The CreateLink sample function in the following example creates a shortcut. The parameters include a pointer to the name of the file to link to, a pointer to the name of the shortcut that you are creating, and a pointer to the description of the link. The description consists of the string, "Shortcut to **file name**," where **file name** is the name of the file to link to.

To create a folder shortcut using the CreateLink sample function, call [**CoCreateInstance**](/windows/win32/api/combaseapi/nf-combaseapi-cocreateinstance) using CLSID\_FolderShortcut, instead of CLSID\_ShellLink (CLSID\_FolderShortcut supports IShellLink). All other code remains the same.

Because CreateLink calls the [**CoCreateInstance**](/windows/win32/api/combaseapi/nf-combaseapi-cocreateinstance) function, it is assumed that the [**CoInitialize**](/windows/win32/api/objbase/nf-objbase-coinitialize) function has already been called. CreateLink uses the [**IPersistFile**](/windows/win32/api/objidl/nn-objidl-ipersistfile) interface to save the shortcut and the [**IShellLink**](/windows/desktop/api/Shobjidl_core/nn-shobjidl_core-ishelllinka) interface to store the file name and description.


```C++
// CreateLink - Uses the Shell's IShellLink and IPersistFile interfaces 
//              to create and store a shortcut to the specified object. 
//
// Returns the result of calling the member functions of the interfaces. 
//
// Parameters:
// lpszPathObj  - Address of a buffer that contains the path of the object,
//                including the file name.
// lpszPathLink - Address of a buffer that contains the path where the 
//                Shell link is to be stored, including the file name.
// lpszDesc     - Address of a buffer that contains a description of the 
//                Shell link, stored in the Comment field of the link
//                properties.

#include "stdafx.h"
#include "windows.h"
#include "winnls.h"
#include "shobjidl.h"
#include "objbase.h"
#include "objidl.h"
#include "shlguid.h"

HRESULT CreateLink(LPCWSTR lpszPathObj, LPCSTR lpszPathLink, LPCWSTR lpszDesc) 
{ 
    HRESULT hres; 
    IShellLink* psl; 
 
    // Get a pointer to the IShellLink interface. It is assumed that CoInitialize
    // has already been called.
    hres = CoCreateInstance(CLSID_ShellLink, NULL, CLSCTX_INPROC_SERVER, IID_IShellLink, (LPVOID*)&psl); 
    if (SUCCEEDED(hres)) 
    { 
        IPersistFile* ppf; 
 
        // Set the path to the shortcut target and add the description. 
        psl->SetPath(lpszPathObj); 
        psl->SetDescription(lpszDesc); 
 
        // Query IShellLink for the IPersistFile interface, used for saving the 
        // shortcut in persistent storage. 
        hres = psl->QueryInterface(IID_IPersistFile, (LPVOID*)&ppf); 
 
        if (SUCCEEDED(hres)) 
        { 
            WCHAR wsz[MAX_PATH]; 
 
            // Ensure that the string is Unicode. 
            MultiByteToWideChar(CP_ACP, 0, lpszPathLink, -1, wsz, MAX_PATH); 
            
            // Add code here to check return value from MultiByteWideChar 
            // for success.
 
            // Save the link by calling IPersistFile::Save. 
            hres = ppf->Save(wsz, TRUE); 
            ppf->Release(); 
        } 
        psl->Release(); 
    } 
    return hres; 
```



### Resolving a Shortcut

An application may need to access and manipulate a shortcut that was previously created. This operation is referred to as resolving the shortcut.

The application-defined ResolveIt function in the following example resolves a shortcut. Its parameters include a window handle, a pointer to the path of the shortcut, and the address of a buffer that receives the new path to the object. The window handle identifies the parent window for any message boxes that the Shell may need to display. For example, the Shell can display a message box if the link is on unshared media, if network problems occur, if the user needs to insert a floppy disk, and so on.

The ResolveIt function calls the [**CoCreateInstance**](/windows/win32/api/combaseapi/nf-combaseapi-cocreateinstance) function and assumes that the [**CoInitialize**](/windows/win32/api/objbase/nf-objbase-coinitialize) function has already been called. Note that ResolveIt needs to use the [**IPersistFile**](/windows/win32/api/objidl/nn-objidl-ipersistfile) interface to store the link information. **IPersistFile** is implemented by the [**IShellLink**](/windows/desktop/api/Shobjidl_core/nn-shobjidl_core-ishelllinka) object. The link information must be loaded before the path information is retrieved, which is shown later in the example. Failing to load the link information causes the calls to the [**IShellLink::GetPath**](/windows/win32/api/shobjidl_core/nf-shobjidl_core-ishelllinka-getpath) and [**IShellLink::GetDescription**](/windows/win32/api/shobjidl_core/nf-shobjidl_core-ishelllinka-getdescription) member functions to fail.


```C++
// ResolveIt - Uses the Shell's IShellLink and IPersistFile interfaces 
//             to retrieve the path and description from an existing shortcut. 
//
// Returns the result of calling the member functions of the interfaces. 
//
// Parameters:
// hwnd         - A handle to the parent window. The Shell uses this window to 
//                display a dialog box if it needs to prompt the user for more 
//                information while resolving the link.
// lpszLinkFile - Address of a buffer that contains the path of the link,
//                including the file name.
// lpszPath     - Address of a buffer that receives the path of the link
                  target, including the file name.
// lpszDesc     - Address of a buffer that receives the description of the 
//                Shell link, stored in the Comment field of the link
//                properties.

#include "stdafx.h"
#include "windows.h"
#include "shobjidl.h"
#include "shlguid.h"
#include "strsafe.h"
                            
HRESULT ResolveIt(HWND hwnd, LPCSTR lpszLinkFile, LPWSTR lpszPath, int iPathBufferSize) 
{ 
    HRESULT hres; 
    IShellLink* psl; 
    WCHAR szGotPath[MAX_PATH]; 
    WCHAR szDescription[MAX_PATH]; 
    WIN32_FIND_DATA wfd; 
 
    *lpszPath = 0; // Assume failure 

    // Get a pointer to the IShellLink interface. It is assumed that CoInitialize
    // has already been called. 
    hres = CoCreateInstance(CLSID_ShellLink, NULL, CLSCTX_INPROC_SERVER, IID_IShellLink, (LPVOID*)&psl); 
    if (SUCCEEDED(hres)) 
    { 
        IPersistFile* ppf; 
 
        // Get a pointer to the IPersistFile interface. 
        hres = psl->QueryInterface(IID_IPersistFile, (void**)&ppf); 
        
        if (SUCCEEDED(hres)) 
        { 
            WCHAR wsz[MAX_PATH]; 
 
            // Ensure that the string is Unicode. 
            MultiByteToWideChar(CP_ACP, 0, lpszLinkFile, -1, wsz, MAX_PATH); 
 
            // Add code here to check return value from MultiByteWideChar 
            // for success.
 
            // Load the shortcut. 
            hres = ppf->Load(wsz, STGM_READ); 
            
            if (SUCCEEDED(hres)) 
            { 
                // Resolve the link. 
                hres = psl->Resolve(hwnd, 0); 

                if (SUCCEEDED(hres)) 
                { 
                    // Get the path to the link target. 
                    hres = psl->GetPath(szGotPath, MAX_PATH, (WIN32_FIND_DATA*)&wfd, SLGP_SHORTPATH); 

                    if (SUCCEEDED(hres)) 
                    { 
                        // Get the description of the target. 
                        hres = psl->GetDescription(szDescription, MAX_PATH); 

                        if (SUCCEEDED(hres)) 
                        {
                            hres = StringCbCopy(lpszPath, iPathBufferSize, szGotPath);
                            if (SUCCEEDED(hres))
                            {
                                // Handle success
                            }
                            else
                            {
                                // Handle the error
                            }
                        }
                    }
                } 
            } 

            // Release the pointer to the IPersistFile interface. 
            ppf->Release(); 
        } 

        // Release the pointer to the IShellLink interface. 
        psl->Release(); 
    } 
    return hres; 
}
```



### Creating a Shortcut to a Nonfile Object

Creating a shortcut to a nonfile object, such as a printer, is similar to creating a shortcut to a file except that rather than setting the path to the file, you must set the identifier list to the printer. To set the identifier list, call the [**IShellLink::SetIDList**](/windows/win32/api/shobjidl_core/nf-shobjidl_core-ishelllinka-setidlist) method, specifying the address of an identifier list.

Each object within the Shell's namespace has an item identifier. The Shell often concatenates item identifiers into null-terminated lists consisting of any number of item identifiers. For more information about item identifiers, see [Item Identifiers and Identifier Lists](#item-identifiers-and-identifier-lists).

In general, if you need to set a shortcut to an item that does not have a file name, such as a printer, you will already have a pointer to the object's [**IShellFolder**](/windows/win32/api/shobjidl_core/nn-shobjidl_core-ishellfolder) interface. **IShellFolder** is used to create namespace extensions.

Once you have the class identifier for [**IShellFolder**](/windows/win32/api/shobjidl_core/nn-shobjidl_core-ishellfolder), you can call the [**CoCreateInstance**](/windows/win32/api/combaseapi/nf-combaseapi-cocreateinstance) function to retrieve the address of the interface. Then you can call the interface to enumerate the objects in the folder and retrieve the address of the item identifier for the object that you are searching for. Finally, you can use the address in a call to the [**IShellLink::SetIDList**](/windows/win32/api/shobjidl_core/nf-shobjidl_core-ishelllinka-setidlist) member function to create a shortcut to the object.

 

 
