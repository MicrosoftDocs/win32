---
Description: Null indicates the normal case (file is available offline). The partial case is only for folders where some content may be available offline and some may not.
ms.assetid: 46b03632-702e-46df-8204-33ada85adbee
title: System.FileOfflineAvailabilityStatus
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# System.FileOfflineAvailabilityStatus

Null indicates the normal case (file is available offline). The partial case is only for folders where some content may be available offline and some may not.

## Windows 10, version 1703

```
propertyDescription
   name = System.FileOfflineAvailabilityStatus
   shellPKey = PKEY_FileOfflineAvailabilityStatus
   formatID = FCEFF153-E839-4CF3-A9E7-EA22832094B8
   propID = 100
   SearchInfo
      InInvertedIndex = false
      IsColumn = true
   typeInfo
      type = UInt32
      IsInnate = true
      EnumeratedList
         UseValueForDefault = True
         enum
            name = NotAvailableOffline
            value = 0
            text = NotAvailableOffline
            defineToken = FILEOFFLINEAVAILABILITYSTATUS_NOTAVAILABLEOFFLINE
         enum
            name = PartiallyAvailableOffline
            value = 1
            text = PartiallyAvailableOffline
            defineToken = FILEOFFLINEAVAILABILITYSTATUS_PARTIAL
         enum
            name = Complete
            value = 2
            text = Complete
            defineToken = FILEOFFLINEAVAILABILITYSTATUS_COMPLETE
         enum
            name = CompletePinned
            value = 3
            text = CompletePinned
            defineToken = FILEOFFLINEAVAILABILITYSTATUS_COMPLETE_PINNED
         enum
            name = Excluded
            value = 4
            text = Excluded
            defineToken = FILEOFFLINEAVAILABILITYSTATUS_EXCLUDED
         enum
            name = Empty
            value = 5
            text = Empty
            defineToken = FILEOFFLINEAVAILABILITYSTATUS_FOLDER_EMPTY
```

## Windows 10, version 1607, Windows 10, version 1511, Windows 10, version 1507, Windows 8.1

```
propertyDescription
   name = System.FileOfflineAvailabilityStatus
   shellPKey = PKEY_FileOfflineAvailabilityStatus
   formatID = FCEFF153-E839-4CF3-A9E7-EA22832094B8
   propID = 100
   SearchInfo
      InInvertedIndex = false
      IsColumn = true
   typeInfo
      type = UInt32
      IsInnate = true
      EnumeratedList
         UseValueForDefault = True
         enum
            name = NotAvailableOffline
            value = 0
            text = NotAvailableOffline
            defineToken = FILEOFFLINEAVAILABILITYSTATUS_PROP_NOTAVAILABLEOFFLINE
         enum
            name = PartiallyAvailableOffline
            value = 1
            text = PartiallyAvailableOffline
            defineToken = FILEOFFLINEAVAILABILITYSTATUS_PROP_PARTIALLYAVAILABLEOFFLINE
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

 

 



