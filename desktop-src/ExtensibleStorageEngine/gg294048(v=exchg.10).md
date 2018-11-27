---
title: JET_INSTANCE
TOCTitle: JET_INSTANCE
ms:assetid: a4136bec-95b3-42d7-b21b-1df09197bb11
ms:mtpsurl: https://msdn.microsoft.com/en-us/library/Gg294048(v=EXCHG.10)
ms:contentKeyID: 32765647
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

# JET\_INSTANCE


_**Applies to:** Windows | Windows Server_

## JET\_INSTANCE

The **JET\_INSTANCE** data type contains a handle to the instance of the database to use for a call to the JET API.

    typedef JET_API_PTR JET_INSTANCE;

### Data Types

JET\_INSTANCE

Either **NULL** or [JET\_instanceNil](gg269256\(v=exchg.10\).md) can be used to indicate an invalid instance handle.

### Remarks

This handle is obtained when you create an instance of the database by calling the [JetCreateInstance](gg269354\(v=exchg.10\).md), [JetCreateInstance2](gg269202\(v=exchg.10\).md), [JetInit](gg294068\(v=exchg.10\).md), or [JetInit2](gg294065\(v=exchg.10\).md) functions.

**Windows XP:**  The explicit use of instances is only supported on Windows XP and later releases.

**Windows 2000:**  Only one global instance is supported per process.

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

[JetCreateInstance](gg269354\(v=exchg.10\).md)  
[JetCreateInstance2](gg269202\(v=exchg.10\).md)  
[JetInit](gg294068\(v=exchg.10\).md)  
[JetInit2](gg294065\(v=exchg.10\).md)

