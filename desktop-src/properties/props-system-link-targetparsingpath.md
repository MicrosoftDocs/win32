---
Description: 'The Shell namespace path to the target of the link item.'
ms.assetid: '05bd6cae-68b2-49ce-ad4f-e395ec88407a'
title: 'System.Link.TargetParsingPath'
---

# System.Link.TargetParsingPath

The Shell namespace path to the target of the link item.

## Windows 10, version 1703, Windows 10, version 1607, Windows 10, version 1511, Windows 10, version 1507, Windows 8.1, Windows 8, Windows 7, Windows Vista

```
propertyDescription
   name = System.Link.TargetParsingPath
   shellPKey = PKEY_Link_TargetParsingPath
   formatID = B9B4B3FC-2B51-4A42-B5D8-324146AFCF25
   propID = 2
   SearchInfo
      InInvertedIndex = false
      IsColumn = true
   typeInfo
      type = String
      IsInnate = true
```

## Remarks

PKEY values are defined in Propkey.h.

This path can be passed to [**SHParseDisplayName**](shell.SHParseDisplayName) to parse the path to the correct Shell folder. If the target item is a file, the value is identical to [System.ItemPathDisplay](shell.props_System_ItemPathDisplay).If the target item cannot be accessed through the Shell namespace, this value is VT\_EMPTY.

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

 

 



