---
Description: The MIME type.
ms.assetid: 9f8f42f8-af90-4f2d-a58c-f892139e86b7
title: System.MIMEType
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# System.MIMEType

The MIME type.

## Windows 10, version 1703, Windows 10, version 1607, Windows 10, version 1511, Windows 10, version 1507, Windows 8.1, Windows 8, Windows 7, Windows Vista

```
propertyDescription
   name = System.MIMEType
   shellPKey = PKEY_MIMEType
   formatID = 0B63E350-9CCC-11D0-BCDB-00805FCCCE04
   propID = 5
   SearchInfo
      InInvertedIndex = true
      IsColumn = true
   typeInfo
      type = String
```

## Remarks

PKEY values are defined in Propkey.h.

For example, an EML file would have a [System.MIMEType](shell.props_System_MIMEType) value of `message/rfc822`.

For media files that are compatible with multiple MIME types, this property may have a bias towards indicating a MIME type that is suitable for Digital Living Network Alliance (DLNA).

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

 

 



