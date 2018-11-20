---
title: JET_CALLBACK Callback Function
TOCTitle: JET_CALLBACK Callback Function
ms:assetid: d15d4f84-8378-4b4b-9b8b-e89a56be5ead
ms:mtpsurl: https://msdn.microsoft.com/en-us/library/Gg294098(v=EXCHG.10)
ms:contentKeyID: 32765713
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

# JET\_CALLBACK Callback Function


_**Applies to:** Windows | Windows Server_

## JET\_CALLBACK Callback Function

The **JET\_CALLBACK** function is a multi-purpose callback function used by the database engine to inform the application of an event involving online defragmentation and cursor state notifications.

See [JET\_CBTYP](gg294071\(v=exchg.10\).md) for specific settings to use for the parameters of this function, as these settings will differ depending upon the **JET\_CBTYP** option that is selected for use in the *cbtyp* parameter.

    JET_ERR JET_API* JET_CALLBACK(
      [in]                 JET_SESID sesid,
      [in]                 JET_DBID dbid,
      [in]                 JET_TABLEID tableid,
      [in]                 JET_CBTYP cbtyp,
      [in, out]            void* pvArg1,
      [in, out]            void* pvArg2,
      [in]                 void* pvContext,
      [in]                 JET_API_PTR ulUnused
    );

### Parameters

*sesid*

The session for which the callback is being made.

*dbid*

The database for which the callback is being made.

*tableid*

The cursor for which the callback is being made.

*cbtyp*

The point in the operation at which the callback is being made. See [JET\_CBTYP](gg294071\(v=exchg.10\).md) for a list of values and the meaning of the following parameters in each case.

*pvArg1*

A parameter used to communicate with the application using the callback. See [JET\_CBTYP](gg294071\(v=exchg.10\).md) for information on the use of this parameter for each callback supported by the database engine.

*pvArg2*

A parameter used to communicate with the application using the callback. See [JET\_CBTYP](gg294071\(v=exchg.10\).md) for information on the use of this parameter for each callback supported by the database engine.

*pvContext*

A parameter used to communicate with the application using the callback. See [JET\_CBTYP](gg294071\(v=exchg.10\).md) for information on the use of this parameter for each callback supported by the database engine.

*ulUnused*

A parameter used to communicate with the application using the callback. See [JET\_CBTYP](gg294071\(v=exchg.10\).md) for information on the use of this parameter for each callback supported by the database engine.

#### Return Value

The function returns one of the [Extensible Storage Engine error codes](gg269297\(v=exchg.10\).md). For information about how to return these codes as HRESULTs, see [Extensible Storage Engine Errors](gg269184\(v=exchg.10\).md). On success, the operation that issued the callback can proceed normally. In some cases, the callback may return a warning that influences that operation. See [JET\_CBTYP](gg294071\(v=exchg.10\).md) for information on the use of these warnings by the operation.

On failure, the operation that issued the callback may proceed normally or may fail. See [JET\_CBTYP](gg294071\(v=exchg.10\).md) for information on the use of the error code by the operation.

#### Remarks

If the callback passes a cursor to the application then it is important to know that this cursor is intentionally limited to a smaller set of functionality to avoid recursion and other ugliness. The following operations are allowed:

  - [JetDupCursor](gg269193\(v=exchg.10\).md)

  - [JetEnumerateColumns](gg269321\(v=exchg.10\).md)

  - [JetGetBookmark](gg269221\(v=exchg.10\).md)

  - [JetGetCurrentIndex](gg294041\(v=exchg.10\).md)

  - [JetGetCursorInfo](gg294126\(v=exchg.10\).md)

  - [JetGetLS](gg269234\(v=exchg.10\).md)

  - [JetGetRecordPosition](gg269316\(v=exchg.10\).md)

  - [JetGetSecondaryIndexBookmark](gg269285\(v=exchg.10\).md)

  - [JetGetTableColumnInfo](gg294061\(v=exchg.10\).md)

  - [JetGetTableIndexInfo](gg294102\(v=exchg.10\).md)

  - [JetGetTableInfo](gg269177\(v=exchg.10\).md)

  - [JetRegisterCallback](gg269175\(v=exchg.10\).md)

  - [JetRetrieveColumn](gg269198\(v=exchg.10\).md)

  - [JetRetrieveColumns](gg294135\(v=exchg.10\).md)

  - [JetRetrieveKey](gg294051\(v=exchg.10\).md)

  - [JetSetColumn](gg294137\(v=exchg.10\).md)

  - [JetSetColumns](gg294050\(v=exchg.10\).md)

  - [JetSetLS](gg269243\(v=exchg.10\).md)

  - [JetUnregisterCallback](gg294116\(v=exchg.10\).md)

When you design your callback, take into account that even with these restrictions, it is still possible for the callback to fail.

#### Requirements

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

[JET\_API\_PTR](gg269209\(v=exchg.10\).md)  
[JET\_DBID](gg269248\(v=exchg.10\).md)  
[JET\_SESID](gg269253\(v=exchg.10\).md)  
[JET\_TABLEID](gg269182\(v=exchg.10\).md)  
[JET\_CBTYP](gg294071\(v=exchg.10\).md)

