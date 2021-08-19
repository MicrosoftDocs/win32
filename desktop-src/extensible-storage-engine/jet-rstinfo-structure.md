---
description: "Learn more about: JET_RSTINFO Structure"
title: JET_RSTINFO Structure
TOCTitle: JET_RSTINFO Structure
ms:assetid: 2f144d68-dcd9-4d0d-9d9e-a7d2a5c350fe
ms:mtpsurl: https://msdn.microsoft.com/library/Gg269216(v=EXCHG.10)
ms:contentKeyID: 32765519
ms.date: 04/11/2016
ms.topic: reference
api_name: 
topic_type: 
- apiref
- kbArticle
api_type: 
- COM
api_location: 
ROBOTS: INDEX,FOLLOW

---

# JET_RSTINFO Structure


_**Applies to:** Windows | Windows Server_

## JET_RSTINFO Structure

The **JET_RSTINFO** structure contains control information for the recovery process like database relocation information and ability to control stopping recovery.

**Windows Vista:** The **JET_RSTINFO** structure is introduced in Windows Vista.

```cpp
    typedef struct {
      unsigned long cbStruct;
      JET_RSTMAP* rgrstmap;
      long crstmap;
      JET_LGPOS lgposStop;
      JET_LOGTIME logtimeStop;
      JET_PFNSTATUS pfnStatus;
    } JET_RSTINFO;
```

### Members

**cbStruct**

The size of the structure.

**rgrstmap**

The structure that describes the old and new path of a restored database.

**crstmap**

Count of array entries in the rgrstmap.

**lgposStop**

The log position to stop recovery at. No undo will be done.

**logtimeStop**

Reserved for future use.

**pfnStatus**

A status function for reporting status of recovery.

### Requirements


| 
|
| <p><strong>Client</strong></p> | <p>Requires Windows Vista, Windows XP, or Windows 2000 Professional.</p> | 
| <p><strong>Server</strong></p> | <p>Requires Windows Server 2008, Windows Server 2003, or Windows 2000 Server.</p> | 
| <p><strong>Header</strong></p> | <p>Declared in Esent.h.</p> | 
| <p><strong>Unicode</strong></p> | <p>Implemented as <strong>JET_RSTINFO_W</strong> (Unicode) and <strong>JET_RSTINFO_A</strong> (ANSI).</p> | 



### See Also

[JetInit3](./jetinit3-function.md)
