---
Description: .
ms.assetid: ad20504c-4920-4d72-86ef-04c82d71be70
title: System.Sensitivity
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# System.Sensitivity

## Windows 10, version 1703, Windows 10, version 1607, Windows 10, version 1511, Windows 10, version 1507, Windows 8.1, Windows 8, Windows 7

```
propertyDescription
   name = System.Sensitivity
   shellPKey = PKEY_Sensitivity
   formatID = F8D3F6AC-4874-42CB-BE59-AB454B30716A
   propID = 100
   SearchInfo
      InInvertedIndex = false
      IsColumn = true
   typeInfo
      type = UInt16
      EnumeratedList
         UseValueForDefault = True
         enum
            name = Normal
            value = 0
            text = Normal
            defineToken = SENSITIVITY_PROP_NORMAL
         enum
            name = Personal
            value = 1
            text = Personal
            defineToken = SENSITIVITY_PROP_PERSONAL
         enum
            name = Private
            value = 2
            text = Private
            defineToken = SENSITIVITY_PROP_PRIVATE
         enum
            name = Confidential
            value = 3
            text = Confidential
            defineToken = SENSITIVITY_PROP_CONFIDENTIAL
```

## Windows Vista

```
propertyDescription
   name = System.Sensitivity
   shellPKey = PKEY_Sensitivity
   formatID = F8D3F6AC-4874-42CB-BE59-AB454B30716A
   propID = 100
   SearchInfo
      IsColumn = true
   typeInfo
      type = UInt16
      EnumeratedList
         UseValueForDefault = True
         enum
            value = 0
            text = Normal
            defineName = SENSITIVITY_PROP_NORMAL
         enum
            value = 1
            text = Personal
            defineName = SENSITIVITY_PROP_PERSONAL
         enum
            value = 2
            text = Private
            defineName = SENSITIVITY_PROP_PRIVATE
         enum
            value = 3
            text = Confidential
            defineName = SENSITIVITY_PROP_CONFIDENTIAL
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

 

 



