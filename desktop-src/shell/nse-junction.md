---
description: The root of a namespace extension is normally displayed by Windows Explorer as a folder in both tree and folder views.
title: Specifying a Namespace Extension's Location
ms.topic: article
ms.date: 05/31/2018
ms.assetid: 2c1fdd5d-b359-4d5c-a20e-0622f3a1cb1d
api_name: 
api_type: 
api_location: 
topic_type: 
 - kbArticle

---

# Specifying a Namespace Extension's Location

The root of a namespace extension is normally displayed by Windows Explorer as a folder in both tree and folder views. For Windows Explorer to display your extension's files and subfolders, you must specify where the root folder is located in the Shell namespace hierarchy. This location is referred to as a *junction point*.

- [Using Virtual Folders as Junction Points](#using-virtual-folders-as-junction-points)
- [Using File System Folders as Junction Points](#using-file-system-folders-as-junction-points)
- [Opening a View of a Namespace Extension](#opening-a-view-of-a-namespace-extension)

## Using Virtual Folders as Junction Points

The simplest way to define an extension's junction point is to make the root folder a subfolder of a system virtual folder. This type of junction point is referred to as a *virtual junction point*. The **Desktop** and **My Computer** folders are the typical locations for virtual junction points, but you can also define a virtual junction point on a remote computer or under the **My Network Places**, **Internet Explorer**, and **Control Panel** folders.

To define a virtual junction point, create a subkey of the key that represents the appropriate virtual folder and name it with the string form of your extension's class identifier (CLSID). The registered CLSID would appear as follows.

```
HKEY_LOCAL_MACHINE or HKEY_CURRENT_USER
   Software
      Microsoft
         Windows
            CurrentVersion
               Explorer
                  Virtual Folder Name
                     NameSpace
                        {Extension CLSID}
                           (Default) = Junction Point Name
```

*Virtual Folder Name* is one of the subkeys in the following table.



| Location          | Virtual Folder Name                        |
|-------------------|--------------------------------------------|
| Control Panel     | **ControlPanel**                           |
| Desktop           | **Desktop**                                |
| Entire Network    | **NetworkNeighborhood**\\**EntireNetwork** |
| My Computer       | **MyComputer**                             |
| My Network Places | **NetworkNeighborhood**                    |
| Remote Computer   | **RemoteComputer**                         |
| Users Files       | **UsersFiles**                             |



 

Remote extensions must be initialized with [**IRemoteComputer**](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-iremotecomputer).

## Using File System Folders as Junction Points

There are two ways to define file system folders as junction points. The simplest approach is to create a folder in the appropriate location and append a period to the folder's name, followed by the string form of the CLSID of your extension. Only the folder name will be visible in Windows Explorer. The following example creates a junction point with a display name of MyFolder.


```
MyFolder.{Extension CLSID}
```



Alternatively, you can define a conventionally named folder as a junction point by:

- Making the folder read-only.
- Making the folder a system folder by calling [**PathMakeSystemFolder**](/windows/desktop/api/Shlwapi/nf-shlwapi-pathmakesystemfoldera).
- Placing a hidden Desktop.ini file in the folder that includes the extension's CLSID.

Desktop.ini is a standard text file that can be added to any folder to customize certain aspects of the folder's behavior. For a general discussion of how to use this file, see [How to Customize Folders with Desktop.ini](how-to-customize-folders-with-desktop-ini.md). To define a folder as a junction point, the \[.ShellClassInfo\] section of Desktop.ini must contain the extension's CLSID as follows:


```
[.ShellClassInfo]
CLSID={Extension CLSID}
```



## Opening a View of a Namespace Extension

When a user browses into a junction point, Windows Explorer automatically creates a view of the root folder. You can also create a view by explicitly launching Explorer.exe with the extension's CLSID as an argument. You can, for instance, use this approach to launch a view of an extension from a shortcut menu or shortcut. For example, to launch a view of MyExtension that includes a tree view, you can use the following command string.


```
%SystemRoot%\Explorer.exe /e,::{MyExtension CLSID}
```



An alternative command string can be used to launch a view of an object within the extension. This feature would be useful, for instance, for an extension that uses a folder view to allow users to view the contents of one of a number of compressed files.


```
%SystemRoot%\Explorer.exe /e,::{MyExtension CLSID},objectname
```



The *objectname* parameter is the name of the object that is to be viewed. Windows Explorer converts the name to its corresponding PIDL and passes the PIDL to the new folder object's [**IPersistFolder::Initialize**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-ipersistfolder-initialize) method.

> [!Note]  
> The CLSID string must be preceded by a pair of colons (::) or the command will fail. The slash-e (/e) flag used in the two sample command lines shown previously instructs Windows Explorer to display a tree view. The flag must be separated from the two colons by a comma. If you do not want a tree view, omit the /e flag and the comma.

 

 

 



