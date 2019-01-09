---
title: JET_SESID
TOCTitle: JET_SESID
ms:assetid: 56b53532-e0a8-4255-8442-bb90184d91da
ms:mtpsurl: https://msdn.microsoft.com/en-us/library/Gg269253(v=EXCHG.10)
ms:contentKeyID: 32765555
ms.date: 04/11/2016
ms.topic: article
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

Either **NULL** or [JET_sesidNil](gg269256\(v=exchg.10\).md) can be used to indicate an invalid session handle.

### Remarks

A session is the transaction context of the database engine. It can be used to begin, commit, or abort transactions that affect the visibility and durability of changes that are made by this or other sessions.

A transaction can be started using [JetBeginTransaction](gg294083\(v=exchg.10\).md). A session may be created using [JetBeginSession](gg294131\(v=exchg.10\).md). The maximum number of sessions that can be created at any one time is controlled by [JET_paramMaxSessions](gg269201\(v=exchg.10\).md), which can be configured by means of [JetSetSystemParameter](gg294044\(v=exchg.10\).md).

A session is explicitly ended by a call to [JetEndSession](gg294054\(v=exchg.10\).md) or implicitly ended by a call to [JetTerm](gg269298\(v=exchg.10\).md).

Each session can only be used by one thread at a time. In addition, the default behavior of the engine is to restrict the use of a session to the same thread from the time the first call to [JetBeginTransaction](gg294083\(v=exchg.10\).md) is made until the time when the matching call to [JetCommitTransaction](gg269191\(v=exchg.10\).md) or [JetRollback](gg269273\(v=exchg.10\).md) is made. This behavior can be changed to remove this second restriction by setting a custom session context using [JetSetSessionContext](gg294124\(v=exchg.10\).md) and [JetResetSessionContext](gg269250\(v=exchg.10\).md).

### Requirements

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>Client</strong></p></td>
<td><p>Requires Windows Vista, Windows XP, or Windows 2000 Professional.</p></td>
</tr>
<tr class="even">
<td><p><strong>Server</strong></p></td>
<td><p>Requires Windows Server 2008, Windows Server 2003, or Windows 2000 Server.</p></td>
</tr>
<tr class="odd">
<td><p><strong>Header</strong></p></td>
<td><p>Declared in Esent.h.</p></td>
</tr>
</tbody>
</table>


### See Also

[JET_paramMaxSessions](gg269201\(v=exchg.10\).md)  
[JetBeginSession](gg294131\(v=exchg.10\).md)  
[JetBeginTransaction](gg294083\(v=exchg.10\).md)  
[JetCommitTransaction](gg269191\(v=exchg.10\).md)  
[JetEndSession](gg294054\(v=exchg.10\).md)  
[JetResetSessionContext](gg269250\(v=exchg.10\).md)  
[JetRollback](gg269273\(v=exchg.10\).md)  
[JetSetSessionContext](gg294124\(v=exchg.10\).md)  
[JetSetSystemParameter](gg294044\(v=exchg.10\).md)  
[JetTerm](gg269298\(v=exchg.10\).md)

