---
title: JET_BKINFO Structure
TOCTitle: JET_BKINFO Structure
ms:assetid: dfaf1d72-1d5f-4777-91c1-6affb735b092
ms:mtpsurl: https://msdn.microsoft.com/en-us/library/Gg294120(v=EXCHG.10)
ms:contentKeyID: 32765734
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

# JET\_BKINFO Structure


_**Applies to:** Windows | Windows Server_

## JET\_BKINFO Structure

The **JET\_BKINFO** structure holds a collection of data about a specific backup event.

    typedef struct {
      JET_LGPOS lgposMark;
      union {
        JET_LOGTIME logtimeMark;
        JET_BKLOGTIME bklogtimeMark;
      };
      unsigned long genLow;
      unsigned long genHigh;
    } JET_BKINFO;

### Members

**lgposMark**

The ID of this backup.

**logtimeMark**

The time of this backup event.

**bklogtimeMark**

The time of this backup event, with additional bits to indicate a snapshot backup.

**Windows Vista:  bklogtimeMark** is introduced in Windows Vista.

**genLow**

The low log generation number associated with this backup event.

**genHigh**

The high log generation number associated with this backup event.

### Remarks

This structure is used inside the [JET\_DBINFOMISC](gg294147\(v=exchg.10\).md) structure to represent data about the database backup event.

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

[JET\_LGPOS](gg294113\(v=exchg.10\).md)  
[JET\_LOGTIME](gg294089\(v=exchg.10\).md)  
[JET\_BKLOGTIME](gg269219\(v=exchg.10\).md)  
[JET\_DBINFOMISC](gg294147\(v=exchg.10\).md)

