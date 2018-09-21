---
title: JET_LGPOS Structure
TOCTitle: JET_LGPOS Structure
ms:assetid: dbce1a60-b32b-40c1-a215-e93bb77cd8c1
ms:mtpsurl: https://msdn.microsoft.com/en-us/library/Gg294113(v=EXCHG.10)
ms:contentKeyID: 32765727
ms.date: 04/11/2016
mtps_version: v=EXCHG.10
api_name: 
topic_type: 
- apiref
- kbArticle
api_type: 
- COM
api_location: 
ROBOTS: INDEX,FOLLOW

---

# JET\_LGPOS Structure


_**Applies to:** Windows | Windows Server_

## JET\_LGPOS Structure

The **JET\_LGPOS** structure holds data that is internal to the logging mechanism of the database engine. This structure is considered internal.

    typedef struct {
      unsigned short ib;
      unsigned short isec;
      long lGeneration;
    } JET_LGPOS;

### Members

**ib**

Supports the ESE infrastructure and cannot be used from your code.

**isec**

Supports the ESE infrastructure and cannot be used from your code.

**lGeneration**

Supports the ESE infrastructure and cannot be used from your code.

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

[JET\_BKINFO](gg294120\(v=exchg.10\).md)  
[JET\_DBINFOMISC](gg294147\(v=exchg.10\).md)

