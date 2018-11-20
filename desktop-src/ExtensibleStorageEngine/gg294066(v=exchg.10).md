---
title: JET_GRBIT
TOCTitle: JET_GRBIT
ms:assetid: b72548cf-3ca2-4ba5-b07a-35eb7e85ed2b
ms:mtpsurl: https://msdn.microsoft.com/en-us/library/Gg294066(v=EXCHG.10)
ms:contentKeyID: 32765681
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

# JET\_GRBIT


_**Applies to:** Windows | Windows Server_

## JET\_GRBIT

The **JET\_GRBIT** data type is a group of bits that contain constants that are specific to the functions and structures in which it is used.

    typedef unsigned long JET_GRBIT;

### Data Types

JET\_GRBIT

In general, the constants that are used as values for this data type reflect the name of the API element in which they are used. For example, all constants passed to [JetRetrieveColumn](gg269198\(v=exchg.10\).md) begin with "JET\_bitRetrieve". Similarly, all constants passed to [JetSetColumn](gg294137\(v=exchg.10\).md) begin with "JET\_bitSet".

A value of zero causes the parameter to be ignored.

### Remarks

For more information, see the specific function or structure. The options are usually passed as a set of flags that can be combined.

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

[JetRetrieveColumn](gg269198\(v=exchg.10\).md)  
[JetSetColumn](gg294137\(v=exchg.10\).md)

