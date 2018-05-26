---
Description: The acquisition date of the file or media.
ms.assetid: 7c673d21-5243-4e41-91df-c5d84aaf620a
title: System.DateAcquired
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# System.DateAcquired

The acquisition date of the file or media. This property is related to a particular user or group of users. For example, this data is used as the main sorting axis for the virtual folder **New Music**, which enables people to browse the latest additions to their collection.

## Windows 10, version 1703, Windows 10, version 1607, Windows 10, version 1511, Windows 10, version 1507, Windows 8.1, Windows 8, Windows 7

```
propertyDescription
   name = System.DateAcquired
   shellPKey = PKEY_DateAcquired
   formatID = 2CBAA8F5-D81F-47CA-B17A-F8D822300131
   propID = 100
   SearchInfo
      InInvertedIndex = false
      IsColumn = true
   typeInfo
      type = DateTime
```

## Windows Vista

```
propertyDescription
   name = System.DateAcquired
   shellPKey = PKEY_DateAcquired
   formatID = 2CBAA8F5-D81F-47CA-B17A-F8D822300131
   propID = 100
   SearchInfo
      IsColumn = true
   typeInfo
      type = DateTime
```

## Remarks

PKEY values are defined in Propkey.h.

[DateAcquired](shell.props_System_DateAcquired) is stored as a value in the main stream of the file, but it may not always be present. In those instances, the acquisition date can be approximated based on other known dates for the content. The metadata handler should use a set of rules to determine the date to return. The following example demonstrates this for music files.

-   For purchased music, the file's creation time should be used if no acquired date is present. However, the download provider should set the [DateAcquired](shell.props_System_DateAcquired) property in the file.
-   For music files that the user or group "ripped" (copying music or video from a CD or DVD to a hard disk), the acquisition date should be the date that action took place. For instance, the [WM/EncodingTime](wmp.wm_encodingtime_attribute) attribute.
-   For music copied from another location, the file's creation time should be used as the acquisition date.

Examples of [System.DateAcquired](shell.props_System_DateAcquired) are the date and time when pictures are acquired from a camera or when music is purchased online. This is not the same as [System.DateImported](shell.props_System_DateImported).

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

 

 



