---
description: In Windows 7 and later, you can add verbs to a folder by using Desktop.ini. For more information about Desktop.ini files, see How to Customize Folders with Desktop.ini.
ms.assetid: F03AB35D-FBFE-46C2-A37F-F70C18219B9A
title: How to Implement Custom Verbs for Folders through Desktop.ini
ms.topic: article
ms.date: 05/31/2018
---

# How to Implement Custom Verbs for Folders through Desktop.ini

In Windows 7 and later, you can add verbs to a folder by using Desktop.ini. For more information about Desktop.ini files, see [How to Customize Folders with Desktop.ini](how-to-customize-folders-with-desktop-ini.md).

> [!Note]  
> Desktop.ini files should always be marked **System** + **Hidden** so they won't be displayed to users.

 

To add custom verbs for folders through a Desktop.ini file, perform the following steps.

## Instructions

### Step 1:

Create a folder that is marked **Read-only** or **System**.

### Step 2:

Create a Desktop.ini file that includes a \[.ShellClassInfo\] DirectoryClass=Folder ProgID.

### Step 3:

In the registry, create **HKEY\_CLASSES\_ROOT**\\**Folder ProgID** with a value of CanUseForDirectory. The CanUseForDirectory value avoids the misuse of ProgIDs that are set not to participate in implementing custom verbs for folders through Desktop.ini.

### Step 4:

Add verbs under the **Folder** ProgID subkey, for example:

```
HKEY_CLASSES_ROOT
   CustomFolderType
      Shell
         MyVerb
            command
               (Default) = %SystemRoot%\system32\notepad.exe %1\desktop.ini
```

## Remarks

> [!Note]  
> These verbs can be the default verbs, in which case double-clicking the folder activates the verb.

 

 

 



