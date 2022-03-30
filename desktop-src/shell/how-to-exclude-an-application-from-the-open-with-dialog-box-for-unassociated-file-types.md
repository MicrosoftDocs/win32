---
description: How to exclude an application from the open with dialog box for unassociated file type.
title: How to Exclude an Application from the Open With Dialog Box for Unassociated File Types
ms.topic: article
ms.date: 05/31/2018
---

# How to Exclude an Application from the Open With Dialog Box for Unassociated File Types

When a user attempts to open a file that is not a member of any registered file type (that is, an unknown file type), or when a user selects **Open with** or **Open with -> Choose default program** from a file's shortcut menu, the Shell presents a submenu or dialog box that enables the user to specify the program used to open the file.

By default, any application registered as a subkey of **HKEY\_CLASSES\_ROOT**\\**Applications** is presented in the **Open with** dialog box. These applications are presented in **Open with** regardless of whether the application is registered to handle the file type.

To prevent an application from appearing in the **Open with** dialog box when the application should not or cannot be used to open certain file types, use one of the two techniques described in this topic.

## Instructions

### Step 1:

Add a NoOpenWith entry to the application's subkey. When an application uses a file type, Windows records that information to build the **Recommended Programs** list. This list is presented in the **Open with** submenu as shown in the following screen shot.

![screen shot of shortcut menu with the open with submenu shown](images/file-assoc/openwithsubmenu.png)

These recommended applications are also shown in the **Recommended Programs** portion of the **Open with** dialog box as shown in the following screen shot.

![screen shot of the open with dialog box with recommended programs](images/file-assoc/openwithdialog.png)

> [!Note]  
> If an application has registered itself in the [OpenWithList](fa-file-types.md) or OpenWithProgIDs for the file type, it will appear in the **Recommended Programs** list even if the NoOpenWith entry is set. Also, remember that regardless of whether an application is offered in a list of recommended programs, a user can manually browse to any executable file.

 

Applications can disable this tracking by specifying a NoOpenWith value under the application's subkey.

The NoOpenWith entry is an empty **REG\_SZ** value as shown in the following example.

```
HKEY_CLASSES_ROOT
   Applications
      MyProgram.exe
         NoOpenWith
```

Setting the NoOpenWith entry also has these effects:

- Prevents pinning a file to the application's Jump List through drag-and-drop, unless the application is specifically registered to handle that file type.
- Prevents the common file dialog box and any call to the [**SHAddToRecentDocs**](/windows/desktop/api/shlobj_core/nf-shlobj_core-shaddtorecentdocs) function from adding any file to the application's Jump List, unless the application is specifically registered to handle that file type.

### Step 2:

The second way to prevent an application from appearing in the **Open with** dialog box is to use the **SupportedTypes** subkey to explicitly list the extensions of file types that the application can open. This prevents the application from appearing in the **Open with** dialog box for file types that it cannot open. It also causes the application to appear in the **Recommended Programs** list as discussed previously.

This method is particularly useful if an application can save a file as a certain file type but cannot open that file type. An application should also set the FOS\_DONTADDTORECENT flag through [**IFileDialog::SetOptions**](/windows/win32/api/shobjidl_core/nf-shobjidl_core-ifiledialog-setoptions) when calling the **Save** dialog box. This keeps the item from being added to the **Recent** or **Frequent** portions of a Jump List. It also blocks the application from being tracked under [OpenWithList](fa-file-types.md).

Each supported extension is added as an entry under the **SupportedTypes** subkey as shown in the following example. The entries are of type **REG\_SZ** or **REG\_NULL**, with no associated values.

```
HKEY_CLASSES_ROOT
   Applications
      ApplicationName
         SupportedTypes
            .ext1
            .ext2
            .ext3
```

If a **SupportedTypes** subkey is provided, only files with those extensions are eligible for pinning to the application's Jump List or for being tracked in an application's **Recent** or **Frequent** destinations list.

The NoOpenWith entry overrides the **SupportedTypes** subkey and hides the application in the **Open with** dialog box.

 

 
