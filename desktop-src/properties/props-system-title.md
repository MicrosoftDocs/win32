---
Description: The title of the item.
ms.assetid: 8fb948d6-2677-4e5d-b283-8757c3df574d
title: System.Title
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# System.Title

The title of the item. For example, the title of a document, the subject of a message, the caption of a photo, or the name of a music track.

## Windows 10, version 1703, Windows 10, version 1607, Windows 10, version 1511, Windows 10, version 1507, Windows 8.1, Windows 8, Windows 7, Windows Vista

```
propertyDescription
   name = System.Title
   shellPKey = PKEY_Title
   formatID = F29F85E0-4FF9-1068-AB91-08002B27B3D9
   propID = 2
   SearchInfo
      InInvertedIndex = true
      IsColumn = true
   typeInfo
      type = String
```

## Remarks

PKEY values are defined in Propkey.h.

This property maps to the OLE document property *Title*. [System.Title](shell.props_System_Title) is a commonly used property, particularly in heterogeneous lists of items where the items can be of many different types. Therefore, it is recommended that property handlers populate this property even if it is redundant; for example, an e-mail, which would populate both System.Title and [System.Subject](shell.props_System_Subject) with the same value.

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

 

 



