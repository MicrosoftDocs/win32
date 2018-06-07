---
Description: Indicates the current status of the task.
ms.assetid: 76bb9bb7-3383-4e5a-ae75-a11c40f318e2
title: System.Communication.TaskStatus
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# System.Communication.TaskStatus

Indicates the current status of the task.

## Windows 10, version 1703, Windows 10, version 1607, Windows 10, version 1511, Windows 10, version 1507, Windows 8.1, Windows 8, Windows 7

```
propertyDescription
   name = System.Communication.TaskStatus
   shellPKey = PKEY_Communication_TaskStatus
   formatID = BE1A72C6-9A1D-46B7-AFE7-AFAF8CEF4999
   propID = 100
   SearchInfo
      InInvertedIndex = false
      IsColumn = true
   typeInfo
      type = UInt16
      EnumeratedList
         UseValueForDefault = True
         enum
            name = NotStarted
            value = 0
            text = Not Started
            defineToken = TASKSTATUS_NOTSTARTED
         enum
            name = InProgress
            value = 1
            text = In Progress
            defineToken = TASKSTATUS_INPROGRESS
         enum
            name = Complete
            value = 2
            text = Complete
            defineToken = TASKSTATUS_COMPLETE
         enum
            name = Waiting
            value = 3
            text = Waiting
            defineToken = TASKSTATUS_WAITING
         enum
            name = Deferred
            value = 4
            text = Deferred
            defineToken = TASKSTATUS_DEFERRED
```

## Windows Vista

```
propertyDescription
   name = System.Communication.TaskStatus
   shellPKey = PKEY_Communication_TaskStatus
   formatID = BE1A72C6-9A1D-46B7-AFE7-AFAF8CEF4999
   propID = 100
   SearchInfo
      InInvertedIndex = false
      IsColumn = true
   typeInfo
      type = UInt16
      EnumeratedList
         UseValueForDefault = True
         enum
            value = 0
            text = Not Started
            defineName = TASKSTATUS_NOTSTARTED
         enum
            value = 1
            text = In Progress
            defineName = TASKSTATUS_INPROGRESS
         enum
            value = 2
            text = Complete
            defineName = TASKSTATUS_COMPLETE
         enum
            value = 3
            text = Waiting
            defineName = TASKSTATUS_WAITING
         enum
            value = 4
            text = Deferred
            defineName = TASKSTATUS_DEFERRED
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

 

 



