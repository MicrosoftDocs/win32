---
description: Specify a custom icon and label for a drive.
ms.assetid: B6EF7F84-7747-4689-B740-A91CA8E394D7
title: Assign a Custom Icon and Label to a Drive Letter
ms.topic: article
ms.date: 05/31/2018
---

# How to Assign a Custom Icon and Label to a Drive Letter

Specify a custom icon and label for a drive.

## Instructions

### Step 1: Replacing the standard drive icon with a custom icon in Windows 2000

To replace the standard drive icon with a custom icon in Windows 2000, add a subkey named for the drive letter to the following key.

```
HKEY_CLASSES_ROOT
   Applications
      Explorer.exe
         Drives
```

The following example specifies a custom icon and label for the E: drive. The icon is in the C:\\MyDir\\MyDrive.exe file with a zero-based index of three.

For Windows 2000:

```
HKEY_CLASSES_ROOT
   Applications
      Explorer.exe
         Drives
            E
               DefaultIcon
                  (Default) = C:\MyDir\MyDrive.exe,3
               DefaultLabel
                  (Default) = MyDrive
```

### Step 2: Replacing the standard drive icon with a custom icon in all other versions of Windows

To replace the standard drive icon with a custom icon in all versions of Windows other than Windows 2000, add a subkey named for the drive letter to the following key.

```
HKEY_LOCAL_MACHINE
   Software
      Microsoft
         Windows
            CurrentVersion
               Explorer
                  DriveIcons
```

The following example specifies a custom icon and label for the E: drive. The icon is in the C:\\MyDir\\MyDrive.exe file with a zero-based index of three.

For all other versions of Windows:

```
HKEY_LOCAL_MACHINE
   Software
      Microsoft
         Windows
            CurrentVersion
               Explorer
                  DriveIcons
                     E
                        DefaultIcon
                           (Default) = C:\MyDir\MyDrive.exe,3
                        DefaultLabel
                           (Default) = MyDrive
```

### Step 3: Calling the SHUpdateImage Event

In all versions of Windows, if you change a file type or drive icon you must also call SHUpdateImage to notify the Shell to update any icons that are currently displayed.

## Remarks

The drive letter should not be followed by a colon (:). Add a **DefaultIcon** subkey to the drive letter subkey and set its default value to a string that contains the location of the icon. The first part of the string contains the fully-qualified path of the icon's file. If there is more than one icon in the file, the path is followed by a comma, and then by the zero-based index of the icon.

 

 



