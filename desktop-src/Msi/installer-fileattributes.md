---
description: The FileAttributes property of the Installer object returns a number representing the combined file attributes for the designated path to a file or folder.
ms.assetid: a09ac346-4e4d-440f-bfbe-ff8fb3f69823
title: Installer.FileAttributes property (Windows.storage.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Installer.FileAttributes
api_type: 
- COM
api_location: 
- Msi.dll
---

# Installer.FileAttributes property

The **FileAttributes** property of the [**Installer**](installer-object.md) object returns a number representing the combined file attributes for the designated path to a file or folder.

This property is read-only.

## Syntax


```JScript
propVal = Installer.FileAttributes
```



## Property value

The required path to the file or folder. A partial path assumes the current directory.

## Remarks

The **FileAttributes** property returns the following values.



| File attribute              | Value      | Value |
|-----------------------------|------------|-------|
| FILE\_ATTRIBUTE\_READONLY   | 0x00000001 | 1     |
| FILE\_ATTRIBUTE\_HIDDEN     | 0x00000002 | 2     |
| FILE\_ATTRIBUTE\_SYSTEM     | 0x00000004 | 4     |
| FILE\_ATTRIBUTE\_DIRECTORY  | 0x00000010 | 16    |
| FILE\_ATTRIBUTE\_TEMPORARY  | 0x00000100 | 256   |
| FILE\_ATTRIBUTE\_COMPRESSED | 0x00000800 | 2048  |
| FILE\_ATTRIBUTE\_OFFLINE    | 0x00001000 | 4096  |



 

Returns –1 if the file or folder does not exist or is not accessible.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer on Windows Server 2003 or Windows XP<br/> |
| Header<br/>  | <dl> <dt>Windows.storage.h</dt> </dl>                                                                                                                                                            |
| DLL<br/>     | <dl> <dt>Msi.dll</dt> </dl>                                                                                                                                                                      |
| IID<br/>     | IID\_IInstaller is defined as 000C1090-0000-0000-C000-000000000046<br/>                                                                                                                                                                           |



 

 




