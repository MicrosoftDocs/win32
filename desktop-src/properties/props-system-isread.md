---
Description: 'Identifies whether the item has been read.'
ms.assetid: '2efa6dd9-8521-48c9-9aff-e2e8f0e2296d'
title: 'System.IsRead'
---

# System.IsRead

Identifies whether the item has been read.

## Windows 10, version 1703, Windows 10, version 1607, Windows 10, version 1511, Windows 10, version 1507, Windows 8.1, Windows 8, Windows 7

```
propertyDescription
   name = System.IsRead
   shellPKey = PKEY_IsRead
   formatID = E3E0584C-B788-4A5A-BB20-7F5A44C9ACDD
   propID = 10
   SearchInfo
      InInvertedIndex = false
      IsColumn = true
   typeInfo
      type = Boolean
      EnumeratedList
         UseValueForDefault = True
         enum
            name = Read
            value = #TRUE#
            text = Read
            defineToken = ISREAD_READ
         enum
            name = NotRead
            value = #FALSE#
            text = Unread
            defineToken = ISREAD_NOTREAD
```

## Windows Vista

```
propertyDescription
   name = System.IsRead
   shellPKey = PKEY_IsRead
   formatID = E3E0584C-B788-4A5A-BB20-7F5A44C9ACDD
   propID = 10
   SearchInfo
      IsColumn = true
   typeInfo
      type = Boolean
      EnumeratedList
         UseValueForDefault = True
         enum
            value = #TRUE#
            text = Read
            mnemonics = read
         enum
            value = #FALSE#
            text = Unread
            mnemonics = unread
```

## Remarks

PKEY values are defined in Propkey.h.

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

 

 



