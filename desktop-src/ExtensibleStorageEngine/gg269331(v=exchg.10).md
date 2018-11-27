---
title: JET_INSTANCE_INFO Structure
TOCTitle: JET_INSTANCE_INFO Structure
ms:assetid: 8cdd2e48-f1bb-465b-aefc-ffe441bf88a1
ms:mtpsurl: https://msdn.microsoft.com/en-us/library/Gg269331(v=EXCHG.10)
ms:contentKeyID: 32765621
ms.date: 04/11/2016
ms.topic: article
api_name: 
topic_type: 
- kbArticle
- apiref
api_type: 
- COM
api_location: 
ROBOTS: INDEX,FOLLOW

---

# JET\_INSTANCE\_INFO Structure


_**Applies to:** Windows | Windows Server_

## JET\_INSTANCE\_INFO Structure

The **JET\_INSTANCE\_INFO** structure receives information about running database instances when used with the [JetGetInstanceInfo](gg294149\(v=exchg.10\).md) and [JetOSSnapshotFreeze](gg269332\(v=exchg.10\).md) functions.

    typedef struct _JET_INSTANCE_INFO {
      JET_INSTANCE hInstanceId;
      tchar* szInstanceName;
      JET_API_PTR cDatabases;
      tchar** szDatabaseFileName;
      tchar** szDatabaseDisplayName;
      tchar** szDatabaseSLVFileName;
    } JET_INSTANCE_INFO;

### Members

**hInstanceId**

The [JET\_INSTANCE](gg294048\(v=exchg.10\).md) of the given instance.

**szInstanceName**

The name of the database instance. This value can be **NULL** if the instance does not have a name.

**cDatabases**

The number of databases that are attached to the database instance. **cDatabases** also holds the size of the arrays of strings that are returned in **szDatabaseFileName**, **szDatabaseDisplayName**, and **szDatabaseSLVFileName**.

**szDatabaseFileName**

An array of strings, each holding the file name of a database that is attached to the database instance. The array has **cDatabases** elements.

**szDatabaseDisplayName**

An array of strings, each holding the display name of a database. Currently the string can be NULL. The array has **cDatabases** elements.

**szDatabaseSLVFileName**

An array of strings, each holding the file name of the SLV file that is attached to the database instance. The array has **cDatabases** elements. SLV files are not supported, so this field should be ignored.

### Remarks

Each database instance can have several databases attached to it.

For a given **JET\_INSTANCE\_INFO** structure, the array of strings that is returned for the databases are in the same order. For example, "szDatabaseDisplayName\[ i \]" and "szDatabaseFileName\[ i \]" both refer to the same database.

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
<tr class="even">
<td><p><strong>Unicode</strong></p></td>
<td><p>Implemented as <strong>JET_INSTANCE_INFO_W</strong> (Unicode) and <strong>JET_INSTANCE_INFO _A</strong> (ANSI).</p></td>
</tr>
</tbody>
</table>


### See Also

[JET\_API\_PTR](gg269209\(v=exchg.10\).md)  
[JET\_INSTANCE](gg294048\(v=exchg.10\).md)  
[JetGetInstanceInfo](gg294149\(v=exchg.10\).md)  
[JetOSSnapshotFreeze](gg269332\(v=exchg.10\).md)

