---
description: Illustrates how to ensure your application appears in the Open With menu and dialog box for desktop apps, and is available as a default Windows Store app for specified file types.
ms.assetid: DFCC07A6-BED5-41A8-86DC-130082AE665A
title: How to Include an Application in the Open With Dialog Box
ms.topic: article
ms.date: 05/31/2018
---

# How to Include an Application in the Open With Dialog Box

Illustrates how to ensure your application appears in the **Open With** menu and dialog box for desktop apps, and is available as a default Windows Store app for specified file types.

## Instructions

### For each file type, add your application to the OpenWithProgIds registry subkey.

Add your ProgID as a value name, with the value type of either REG\_NONE or REG\_SZ and an empty string as the data value.

The following registry examples show entries associating InfoPath and for Microsoft Visual Studio with the XML file type.

```
HKEY_CLASSES_ROOT
   .xml
      OpenWithProgids
         InfoPath.Document.3 REG_SZ
         VisualStudio.xml.10.0 REG_SZ
```

## Remarks

The **OpenWithProgids** subkey is preferred to **OpenWithList** to identify an application. For more information on these subkeys, see [Setting Optional Subkeys and File Type Extension Attributes](fa-file-types.md).

**OpenWithList** is intended only for legacy apps (must be .exe only) on operating systems prior to Windows XP.

```
HKEY_CLASSES_ROOT
   .xml
      OpenWithList
         AlternateProgram1.exe
         AlternateProgram2.exe
```

 

 



