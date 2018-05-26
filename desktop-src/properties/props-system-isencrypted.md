---
Description: Identifies whether the item is encrypted.
ms.assetid: fd93f915-6af3-4bde-982e-6774a1ca83af
title: System.IsEncrypted
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# System.IsEncrypted

Identifies whether the item is encrypted.

## Windows 10, version 1703, Windows 10, version 1607, Windows 10, version 1511, Windows 10, version 1507, Windows 8.1, Windows 8, Windows 7

```
propertyDescription
   name = System.IsEncrypted
   shellPKey = PKEY_IsEncrypted
   formatID = 90E5E14E-648B-4826-B2AA-ACAF790E3513
   propID = 10
   SearchInfo
      InInvertedIndex = false
      IsColumn = true
   typeInfo
      type = Boolean
      EnumeratedList
         UseValueForDefault = True
         enum
            name = Encrypted
            value = #TRUE#
            text = Encrypted
            defineToken = ISENCRYPTED_ENCRYPTED
         enum
            name = NotEncrypted
            value = #FALSE#
            text = Unencrypted
            defineToken = ISENCRYPTED_NOTENCRYPTED
```

## Windows Vista

```
propertyDescription
   name = System.IsEncrypted
   shellPKey = PKEY_IsEncrypted
   formatID = 90E5E14E-648B-4826-B2AA-ACAF790E3513
   propID = 10
   SearchInfo
      IsColumn = true
   typeInfo
      type = Boolean
      EnumeratedList
         UseValueForDefault = True
         enum
            value = #TRUE#
            text = Encrypted
            mnemonics = encrypted
         enum
            value = #FALSE#
            text = Unencrypted
            mnemonics = unencrypted
```

## Remarks

PKEY values are defined in Propkey.h.

This property was introduced with the release of Windows Search 4.0.

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

 

 



