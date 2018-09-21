---
title: JET_SIGNATURE Structure
TOCTitle: JET_SIGNATURE Structure
ms:assetid: 90d3fd56-be65-4126-b50c-b53e3c3f38f6
ms:mtpsurl: https://msdn.microsoft.com/en-us/library/Gg269340(v=EXCHG.10)
ms:contentKeyID: 32765629
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

# JET\_SIGNATURE Structure


_**Applies to:** Windows | Windows Server_

## JET\_SIGNATURE Structure

The **JET\_SIGNATURE** structure contains information that uniquely identifies a database.

    typedef struct {
      unsigned long ulRandom;
      JET_LOGTIME logtimeCreate;
      char szComputerName[JET_MAX_COMPUTERNAME_LENGTH + 1];
    } JET_SIGNATURE;

### Members

**ulRandom**

A randomly assigned number.

**logtimeCreate**

The [JET\_LOGTIME](gg294089\(v=exchg.10\).md) at the time of [JetCreateDatabase](gg269212\(v=exchg.10\).md) is executed.

**szComputerName**

The optional string value of the NetBIOS name for the computer. This value may not be set.

### Remarks

This can be found as an element of [JET\_DBINFOMISC](gg294147\(v=exchg.10\).md).

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

[JET\_DBINFOMISC](gg294147\(v=exchg.10\).md)  
[JET\_LOGTIME](gg294089\(v=exchg.10\).md)  
[JetCreateDatabase](gg269212\(v=exchg.10\).md)

