---
description: "Learn more about: JET_SESID"
title: JET_SESID
TOCTitle: JET_SESID
ms:assetid: 56b53532-e0a8-4255-8442-bb90184d91da
ms:mtpsurl: https://msdn.microsoft.com/library/Gg269253(v=EXCHG.10)
ms:contentKeyID: 32765555
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

# JET_SESID


_**Applies to:** Windows | Windows Server_

## JET_SESID

The **JET_SESID** data type contains a handle to the session to use for a call to the JET API.

```cpp
    typedef JET_API_PTR JET_SESID;
```

### Data Types

JET_SESID

Either **NULL** or [JET_sesidNil](./invalid-handle-constants.md) can be used to indicate an invalid session handle.

### Remarks

A session is the transaction context of the database engine. It can be used to begin, commit, or abort transactions that affect the visibility and durability of changes that are made by this or other sessions.

A transaction can be started using [JetBeginTransaction](./jetbegintransaction-function.md). A session may be created using [JetBeginSession](./jetbeginsession-function.md). The maximum number of sessions that can be created at any one time is controlled by [JET_paramMaxSessions](./resource-parameters.md), which can be configured by means of [JetSetSystemParameter](./jetsetsystemparameter-function.md).

A session is explicitly ended by a call to [JetEndSession](./jetendsession-function.md) or implicitly ended by a call to [JetTerm](./jetterm-function.md).

Each session can only be used by one thread at a time. In addition, the default behavior of the engine is to restrict the use of a session to the same thread from the time the first call to [JetBeginTransaction](./jetbegintransaction-function.md) is made until the time when the matching call to [JetCommitTransaction](./jetcommittransaction-function.md) or [JetRollback](./jetrollback-function.md) is made. This behavior can be changed to remove this second restriction by setting a custom session context using [JetSetSessionContext](./jetsetsessioncontext-function.md) and [JetResetSessionContext](./jetresetsessioncontext-function.md).

### Requirements


| 
|
| <p><strong>Client</strong></p> | <p>Requires Windows Vista, Windows XP, or Windows 2000 Professional.</p> | 
| <p><strong>Server</strong></p> | <p>Requires Windows Server 2008, Windows Server 2003, or Windows 2000 Server.</p> | 
| <p><strong>Header</strong></p> | <p>Declared in Esent.h.</p> | 



### See Also

[JET_paramMaxSessions](./resource-parameters.md)  
[JetBeginSession](./jetbeginsession-function.md)  
[JetBeginTransaction](./jetbegintransaction-function.md)  
[JetCommitTransaction](./jetcommittransaction-function.md)  
[JetEndSession](./jetendsession-function.md)  
[JetResetSessionContext](./jetresetsessioncontext-function.md)  
[JetRollback](./jetrollback-function.md)  
[JetSetSessionContext](./jetsetsessioncontext-function.md)  
[JetSetSystemParameter](./jetsetsystemparameter-function.md)  
[JetTerm](./jetterm-function.md)
