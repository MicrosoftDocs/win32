---
Description: The Shell namespace name of an item relative to a parent folder.
ms.assetid: 8d17d99f-a4c2-489e-97b3-74586b191cf2
title: System.ParsingName
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# System.ParsingName

The Shell namespace name of an item relative to a parent folder.

## Windows 10, version 1703, Windows 10, version 1607, Windows 10, version 1511, Windows 10, version 1507, Windows 8.1, Windows 8, Windows 7, Windows Vista

```
propertyDescription
   name = System.ParsingName
   shellPKey = PKEY_ParsingName
   formatID = 28636AA6-953D-11D2-B5D6-00C04FD918D0
   propID = 24
   SearchInfo
      InInvertedIndex = true
      IsColumn = true
   typeInfo
      type = String
      IsInnate = true
```

## Remarks

PKEY values are defined in Propkey.h.

This value can be passed to the [**ParseDisplayName**](shell.IShellFolder_ParseDisplayName) method of the [**IShellFolder**](shell.IShellFolder) object that represents the parent Shell folder.

## Related topics

<dl> <dt>

[propertyDescription](shell.propdesc_schema_propertyDescription)
</dt> <dt>

[searchInfo](shell.propdesc_schema_searchInfo)
</dt> <dt>

[labelInfo](shell.propdesc_schema_labelInfo)
</dt> <dt>

[typeInfo](shell.propdesc_schema_typeInfo)
</dt> <dt>

[displayInfo](shell.propdesc_schema_displayInfo)
</dt> <dt>

[stringFormat](shell.propdesc_schema_stringFormat)
</dt> <dt>

[booleanFormat](shell.propdesc_schema_booleanFormat)
</dt> <dt>

[numberFormat](shell.propdesc_schema_numberFormat)
</dt> <dt>

[dateTimeFormat](shell.propdesc_schema_dateTimeFormat)
</dt> <dt>

[enumeratedList](shell.propdesc_schema_enumeratedList)
</dt> <dt>

[drawControl](shell.propdesc_schema_drawControl)
</dt> <dt>

[editControl](shell.propdesc_schema_editControl)
</dt> <dt>

[filterControl](shell.propdesc_schema_filterControl)
</dt> <dt>

[queryControl](shell.propdesc_schema_queryControl)
</dt> </dl>

 

 



