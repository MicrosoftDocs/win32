---
Description: Null indicates the normal case (file is available offline). The partial case is only for folders where some content may be available offline and some may not.
ms.assetid: 46b03632-702e-46df-8204-33ada85adbee
title: System.FileOfflineAvailabilityStatus
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
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

[propertyDescription](https://www.bing.com/search?q=propertyDescription)
</dt> <dt>

[searchInfo](https://www.bing.com/search?q=searchInfo)
</dt> <dt>

[labelInfo](https://www.bing.com/search?q=labelInfo)
</dt> <dt>

[typeInfo](https://www.bing.com/search?q=typeInfo)
</dt> <dt>

[displayInfo](https://www.bing.com/search?q=displayInfo)
</dt> <dt>

[stringFormat](https://www.bing.com/search?q=stringFormat)
</dt> <dt>

[booleanFormat](https://www.bing.com/search?q=booleanFormat)
</dt> <dt>

[numberFormat](https://www.bing.com/search?q=numberFormat)
</dt> <dt>

[dateTimeFormat](https://www.bing.com/search?q=dateTimeFormat)
</dt> <dt>

[enumeratedList](https://www.bing.com/search?q=enumeratedList)
</dt> <dt>

[drawControl](https://www.bing.com/search?q=drawControl)
</dt> <dt>

[editControl](https://www.bing.com/search?q=editControl)
</dt> <dt>

[filterControl](https://www.bing.com/search?q=filterControl)
</dt> <dt>

[queryControl](https://www.bing.com/search?q=queryControl)
</dt> </dl>

 

 



