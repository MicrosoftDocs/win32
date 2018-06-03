---
Description: The acquisition date of the file or media.
ms.assetid: 7c673d21-5243-4e41-91df-c5d84aaf620a
title: System.DateAcquired
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
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

[DateAcquired](https://www.bing.com/search?q=DateAcquired) is stored as a value in the main stream of the file, but it may not always be present. In those instances, the acquisition date can be approximated based on other known dates for the content. The metadata handler should use a set of rules to determine the date to return. The following example demonstrates this for music files.

-   For purchased music, the file's creation time should be used if no acquired date is present. However, the download provider should set the [DateAcquired](https://www.bing.com/search?q=DateAcquired) property in the file.
-   For music files that the user or group "ripped" (copying music or video from a CD or DVD to a hard disk), the acquisition date should be the date that action took place. For instance, the [WM/EncodingTime](https://msdn.microsoft.com/windows/desktop/264f379a-0bec-4143-bc23-ab45fb725af6) attribute.
-   For music copied from another location, the file's creation time should be used as the acquisition date.

Examples of [System.DateAcquired](https://www.bing.com/search?q=System.DateAcquired) are the date and time when pictures are acquired from a camera or when music is purchased online. This is not the same as [System.DateImported](https://www.bing.com/search?q=System.DateImported).

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

 

 



