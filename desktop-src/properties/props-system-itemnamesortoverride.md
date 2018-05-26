---
Description: This string should be set to the phonetic version of the display name as defined in System.ItemNameDisplay in CJK locales(CHS Pinyin, JPN Hiragana, KOR Hangul, etc.).
ms.assetid: eb491644-bf59-4439-9e9b-bcafde619d66
title: System.ItemNameSortOverride
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# System.ItemNameSortOverride

This string should be set to the phonetic version of the display name as defined in System.ItemNameDisplay in CJK locales(CHS Pinyin, JPN Hiragana, KOR Hangul, etc.). The first character of this field is also used for grouping names by firstletter. For most non-CJK languages, this field does not need to be set (in which case System.ItemNameDisplay will be used).However, if it is desirable to override the grouping letter (for example, to remove leading articles such as "a" and "the"),an alternate string can be provided here.

## Windows 10, version 1703, Windows 10, version 1607, Windows 10, version 1511, Windows 10, version 1507, Windows 8.1, Windows 8

```
propertyDescription
   name = System.ItemNameSortOverride
   shellPKey = PKEY_ItemNameSortOverride
   formatID = B725F130-47EF-101A-A5F1-02608C9EEBAC
   propID = 23
   SearchInfo
      InInvertedIndex = false
      IsColumn = false
   typeInfo
      type = String
      IsInnate = true
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

 

 



