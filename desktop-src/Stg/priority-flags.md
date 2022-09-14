---
title: Priority Flags
description: The priority flag opens a storage object in priority mode.
ms.assetid: 85f2df6f-9219-4752-8c17-f219c37a4037
keywords:
- Priority Flags
ms.topic: article
ms.date: 05/31/2018
---

# Priority Flags

The priority flag opens a storage object in priority mode. When it opens an object, an application usually works from a snapshot copy because other applications may also be using the object at the same time. When opening a storage object in priority mode, however, the application has exclusive rights to commit changes to the object.

Priority mode enables an application to read some streams from storage before opening the object in a mode that would require the system to make a snapshot copy. Because the application has exclusive access, it does not have to make a snapshot copy of the object. When the application subsequently opens the object in a mode where a snapshot copy is required, the application can exclude the streams it has already read from the snapshot, thereby reducing the overhead of opening the object.

Because other applications cannot commit changes to an object while it is open in priority mode, applications should keep the object in that mode for as short a time as possible.

 

 




