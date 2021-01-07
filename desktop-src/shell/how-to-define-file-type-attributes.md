---
description: Defining file type attributes in the registry.
ms.assetid: EE35E3E7-0573-45CA-A21A-89E50B86487D
title: How to Define File Type Attributes
ms.topic: article
ms.date: 05/31/2018
---

# How to Define File Type Attributes

Assigning file type attributes to an associated ProgID enables you to control some aspects of the file type's behavior. Prior to Windows Vista, these attributes could enable you to limit the extent to which the user could use the **Folder Options** property tab to modify various aspects of the file type, such as its icon or verbs.

File type attributes are binary flags specified as **REG\_DWORD** or **REG\_BINARY** values in the file type's associated ProgID subkey.

To assign attributes for a file type, follow these steps.

## Instructions

### Step 1:

Add an EditFlags entry to the file type's associated ProgID subkey.

### Step 2:

Set the entry to the appropriate attribute value.

The following example shows the FTA\_NoRemove (0x00000010) and FTA\_NoNewVerb (0x00000020) attributes set for the .myp file type.

```
HKEY_CLASSES_ROOT
   .myp-file
      (Default) = ApplicationVendor.MyProgram
   ApplicationVendor.MyProgram
      (Default) = MyProgram Application
      EditFlags = 0x00000030
```

## Remarks

The flags can be combined with a logical OR to form the single attribute value.

For a list of possible file type attributes and their hexadecimal values, and more details on programmatically retrieving and setting these values, see [**FILETYPEATTRIBUTEFLAGS**](/windows/desktop/api/Shlwapi/ne-shlwapi-filetypeattributeflags).

 

 



