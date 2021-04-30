---
description: "Learn more about: JET_CBTYP"
title: JET_CBTYP
TOCTitle: JET_CBTYP
ms:assetid: babbfa11-01a7-477b-a525-cff27a983b60
ms:mtpsurl: https://msdn.microsoft.com/library/Gg294071(v=EXCHG.10)
ms:contentKeyID: 32765686
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

# JET_CBTYP


_**Applies to:** Windows | Windows Server_

## JET_CBTYP

The **JET_CBTYP** group of constants describes all possible points in an operation that the database engine will notify an application by calling the [JET_CALLBACK](./jet-callback-callback-function.md) callback function. The database engine passes one of these constants in the *cbtyp* parameter of the callback function. The meaning of the other parameters passed by the database engine in this call depend on the specific **JET_CBTYP** passed.

**Windows XP:**  The **JET_CBTYP** group of constants are introduced in Windows XP.

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Constant/value</p></th>
<th><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>JET_cbtypNull<br />
0x00000000</p></td>
<td><p>This callback is reserved and always considered invalid.</p></td>
</tr>
<tr class="even">
<td><p>JET_cbtypFinalize<br />
0x00000001</p></td>
<td><p>This callback is reserved for future use.</p></td>
</tr>
<tr class="odd">
<td><p>JET_cbtypBeforeInsert<br />
0x00000002</p></td>
<td><p>This callback will occur just before a new record is inserted into a table by a call to <a href="gg269288(v=exchg.10).md">JetUpdate</a>.</p>
<p>The function pointer for this callback reason is either passed to <a href="gg269343(v=exchg.10).md">JetCreateTableColumnIndex</a> by means of <a href="gg294146(v=exchg.10).md">JET_TABLECREATE</a> or is configured at runtime by means of <a href="gg269175(v=exchg.10).md">JetRegisterCallback</a>. For more information, see <a href="gg294146(v=exchg.10).md">JET_TABLECREATE</a> or <a href="gg269175(v=exchg.10).md">JetRegisterCallback</a>.</p>
<p>The callback parameters will have the following values:</p>
<ul>
<li><p><em>sesid</em>: The session that has the record to be inserted.</p></li>
<li><p><em>dbid</em>: The database ID of the table that contains the record to be inserted.</p></li>
<li><p><em>tableid</em>: The cursor that has prepared the new record to be inserted. It is important to note that the value of any version or auto-increment columns may not be correct at this time.</p></li>
<li><p><em>pvArg1</em>: <strong>NULL</strong></p></li>
<li><p><em>pvArg2</em>: <strong>NULL</strong></p></li>
<li><p><em>pvContext</em>: The context pointer passed to <a href="gg269175(v=exchg.10).md">JetRegisterCallback</a> or <strong>NULL</strong>.</p></li>
<li><p><em>ulUnused</em>: <strong>NULL</strong> If an error is returned by the callback, the operation originating the callback will fail with that error.</p></li>
</ul></td>
</tr>
<tr class="even">
<td><p>JET_cbtypAfterInsert<br />
0x00000004</p></td>
<td><p>This callback will occur just after a new record has been inserted into a table by a call to <a href="gg269288(v=exchg.10).md">JetUpdate</a> but before <a href="gg269288(v=exchg.10).md">JetUpdate</a> returns to its caller.</p>
<p>The function pointer for this callback reason is either passed to <a href="gg269343(v=exchg.10).md">JetCreateTableColumnIndex</a> by means of <a href="gg294146(v=exchg.10).md">JET_TABLECREATE</a> or is configured at runtime by means of <a href="gg269175(v=exchg.10).md">JetRegisterCallback</a>. For more information, see <a href="gg294146(v=exchg.10).md">JET_TABLECREATE</a> or <a href="gg269175(v=exchg.10).md">JetRegisterCallback</a>.</p>
<p>The callback parameters will have the following values:</p>
<ul>
<li><p><em>sesid</em>: The session that has the record that was just inserted.</p></li>
<li><p><em>dbid</em>: The database ID of the table that contains the record that was just inserted.</p></li>
<li><p><em>tableid</em>: A cursor on the table into which the record that was just inserted. Note that the cursor is still positioned on the same index entry as it was in the before insert callback. Further note that this index entry may not be related in any way to the record being inserted.</p></li>
<li><p><em>pvArg1</em>: <strong>NULL</strong></p></li>
<li><p><em>pvArg2</em>: <strong>NULL</strong></p></li>
<li><p><em>pvContext</em>: The context pointer passed to <a href="gg269175(v=exchg.10).md">JetRegisterCallback</a> or <strong>NULL</strong>.</p></li>
<li><p><em>ulUnused</em>: <strong>NULL</strong> If an error is returned by the callback, it will be ignored.</p></li>
</ul></td>
</tr>
<tr class="odd">
<td><p>JET_cbtypBeforeReplace<br />
0x00000008</p></td>
<td><p>This callback will occur just prior to an existing record in a table being changed by a call to <a href="gg269288(v=exchg.10).md">JetUpdate</a>.</p>
<p>The function pointer for this callback reason is either passed to <a href="gg269343(v=exchg.10).md">JetCreateTableColumnIndex</a> by means of <a href="gg294146(v=exchg.10).md">JET_TABLECREATE</a> or is configured at runtime by means of <a href="gg269175(v=exchg.10).md">JetRegisterCallback</a>. For more information, see <a href="gg294146(v=exchg.10).md">JET_TABLECREATE</a> or <a href="gg269175(v=exchg.10).md">JetRegisterCallback</a>.</p>
<p>The callback parameters will have the following values:</p>
<ul>
<li><p><em>sesid</em>: The session that has the record to be changed.</p></li>
<li><p><em>dbid</em>: The database ID of the table that contains the record to be changed.</p></li>
<li><p><em>tableid</em>: A cursor positioned on an index entry associated with the record to be changed. It is important to note that the value of any version or auto-increment columns may not be correct at this time.</p></li>
<li><p><em>pvArg1</em>: <strong>NULL</strong></p></li>
<li><p><em>pvArg2</em>: <strong>NULL</strong></p></li>
<li><p><em>pvContext</em>: The context pointer passed to <a href="gg269175(v=exchg.10).md">JetRegisterCallback</a> or <strong>NULL</strong>.</p></li>
<li><p><em>ulUnused</em>: <strong>NULL</strong> If an error is returned by the callback, the operation originating the callback will fail with that error.</p></li>
</ul></td>
</tr>
<tr class="even">
<td><p>JET_cbtypAfterReplace<br />
0x00000010</p></td>
<td><p>This callback will occur just after an existing record in a table has been changed by a call to <a href="gg269288(v=exchg.10).md">JetUpdate</a> but prior to <a href="gg269288(v=exchg.10).md">JetUpdate</a> returning to its caller.</p>
<p>The function pointer for this callback reason is either passed to <a href="gg269343(v=exchg.10).md">JetCreateTableColumnIndex</a> by means of <a href="gg294146(v=exchg.10).md">JET_TABLECREATE</a> or is configured at runtime by means of <a href="gg269175(v=exchg.10).md">JetRegisterCallback</a>. For more information, see <a href="gg294146(v=exchg.10).md">JET_TABLECREATE</a> or <a href="gg269175(v=exchg.10).md">JetRegisterCallback</a>.</p>
<p>The callback parameters will have the following values:</p>
<ul>
<li><p><em>sesid</em>: The session that has the record that was just changed.</p></li>
<li><p><em>dbid</em>: The database ID of the table that contains the record that was just changed.</p></li>
<li><p><em>tableid</em>: A cursor positioned on an index entry associated with the record that was just changed.</p></li>
<li><p><em>pvArg1</em>: <strong>NULL</strong></p></li>
<li><p><em>pvArg2</em>: <strong>NULL</strong></p></li>
<li><p><em>pvContext</em>: The context pointer passed to <a href="gg269175(v=exchg.10).md">JetRegisterCallback</a> or <strong>NULL</strong>.</p></li>
<li><p><em>ulUnused</em>: <strong>NULL</strong> If an error is returned by the callback, it will be ignored.</p></li>
</ul></td>
</tr>
<tr class="odd">
<td><p>JET_cbtypBeforeDelete<br />
0x00000020</p></td>
<td><p>This callback will occur just before an existing record in a table is deleted by a call to <a href="gg269315(v=exchg.10).md">JetDelete</a>.</p>
<p>The function pointer for this callback reason is either passed to <a href="gg269343(v=exchg.10).md">JetCreateTableColumnIndex</a> by means of <a href="gg294146(v=exchg.10).md">JET_TABLECREATE</a> or is configured at runtime by means of <a href="gg269175(v=exchg.10).md">JetRegisterCallback</a>. For more information, see <a href="gg294146(v=exchg.10).md">JET_TABLECREATE</a> or <a href="gg269175(v=exchg.10).md">JetRegisterCallback</a>.</p>
<p>The callback parameters will have the following values:</p>
<ul>
<li><p><em>sesid</em>: The session that has the record to be deleted.</p></li>
<li><p><em>dbid</em>: The database ID of the table that contains the record to be deleted.</p></li>
<li><p><em>tableid</em>: A cursor positioned on an index entry associated with the record to be deleted.</p></li>
<li><p><em>pvArg1</em>: <strong>NULL</strong></p></li>
<li><p><em>pvArg2</em>: <strong>NULL</strong></p></li>
<li><p><em>pvContext</em>: The context pointer passed to <a href="gg269175(v=exchg.10).md">JetRegisterCallback</a> or <strong>NULL</strong>.</p></li>
<li><p><em>ulUnused</em>: <strong>NULL</strong> If an error is returned by the callback, the operation originating the callback will fail with that error.</p></li>
</ul></td>
</tr>
<tr class="even">
<td><p>JET_cbtypAfterDelete<br />
0x00000040</p></td>
<td><p>This callback will occur just after an existing record in a table has been deleted by a call to <a href="gg269315(v=exchg.10).md">JetDelete</a> but before <a href="gg269315(v=exchg.10).md">JetDelete</a> returns to its caller.</p>
<p>The function pointer for this callback reason is either passed to <a href="gg269343(v=exchg.10).md">JetCreateTableColumnIndex</a> by means of <a href="gg294146(v=exchg.10).md">JET_TABLECREATE</a> or is configured at runtime by means of <a href="gg269175(v=exchg.10).md">JetRegisterCallback</a>. For more information, see <a href="gg294146(v=exchg.10).md">JET_TABLECREATE</a> or <a href="gg269175(v=exchg.10).md">JetRegisterCallback</a>.</p>
<p>The callback parameters will have the following values:</p>
<ul>
<li><p><em>sesid</em>: The session that has the record that was just deleted.</p></li>
<li><p><em>dbid</em>: The database ID of the table that contains the record that was just deleted.</p></li>
<li><p><em>tableid</em>: A cursor positioned on an index entry associated with the record that was just deleted.</p></li>
<li><p><em>pvArg1</em>: <strong>NULL</strong></p></li>
<li><p><em>pvArg2</em>: <strong>NULL</strong></p></li>
<li><p><em>pvContext</em>: the context pointer passed to <a href="gg269175(v=exchg.10).md">JetRegisterCallback</a> or <strong>NULL</strong>.</p></li>
<li><p><em>ulUnused</em>: <strong>NULL</strong></p></li>
</ul>
<p>If an error is returned by the callback, it will be ignored.</p></td>
</tr>
<tr class="odd">
<td><p>JET_cbtypUserDefinedDefaultValue<br />
0x00000080</p></td>
<td><p>This callback will occur when the engine needs to retrieve the user defined default value of a column from the application. This callback is essentially a limited implementation of <a href="gg269198(v=exchg.10).md">JetRetrieveColumn</a> that is evaluated by the application. A maximum of one column value can be returned for a user defined default value.</p>
<p>The function pointer for this callback reason is either passed to <a href="gg294122(v=exchg.10).md">JetAddColumn</a> by means of a <a href="gg269200(v=exchg.10).md">JET_USERDEFINEDDEFAULT</a> structure or passed to <a href="gg269343(v=exchg.10).md">JetCreateTableColumnIndex</a> by means of a <a href="gg269200(v=exchg.10).md">JET_USERDEFINEDDEFAULT</a> structure in a <a href="gg269252(v=exchg.10).md">JET_COLUMNCREATE</a> structure in a <a href="gg294146(v=exchg.10).md">JET_TABLECREATE</a> structure.</p>
<p>The callback parameters will have the following values:</p>
<ul>
<li><p><em>sesid</em>: The session that is computing the user defined default value</p></li>
<li><p><em>dbid</em>: The database ID of the table that contains the user defined default value</p></li>
<li><p><em>tableid</em>: A cursor positioned on the record for which the user defined default value is being retrieved</p></li>
<li><p><em>pvArg1</em>: The output buffer for the user defined default value</p></li>
<li><p><em>pvArg2</em>: On input, this is the size of the output buffer. On output, this is the actual size of the user defined default value. in either case, the size is a 32-bit unsigned integer.</p></li>
<li><p><em>pvContext</em>: A pointer to a buffer containing the user data specified in the <a href="gg269200(v=exchg.10).md">JET_USERDEFINEDDEFAULT</a> structure when the column was created or NULL if no context was provided.</p></li>
<li><p><em>ulUnused</em>: The column ID of the column for which the user defined default value is being retrieved.</p></li>
</ul>
<p>If an error is returned by the callback then the operation originating the callback will fail with that error.</p>
<p>If JET_wrnBufferTruncated is returned by the callback, the operation will continue, but the entire value is not retrieved during the callback.</p>
<p>If JET_wrnColumnNull is returned by the callback, the operation will continue, but the user defined default value for the column is NULL.</p></td>
</tr>
<tr class="even">
<td><p>JET_cbtypOnlineDefragCompleted<br />
0x00000100</p></td>
<td><p>This callback will occur when the online defragmentation of a database as initiated by <a href="gg269317(v=exchg.10).md">JetDefragment</a> has stopped due to either the process being completed or the time limit being reached.</p>
<p>The function pointer for this callback reason is passed to <a href="gg269317(v=exchg.10).md">JetDefragment</a>. For more information, see <a href="gg269317(v=exchg.10).md">JetDefragment</a>.</p>
<p>The callback parameters will have the following values:</p>
<ul>
<li><p><em>sesid</em>: The session used to perform online defragmentation for the database or JET_sesidNil for a streaming file.</p></li>
<li><p><em>dbid</em>: The database ID of the database being defragmented or JET_dbidNil for a streaming file.</p></li>
<li><p><em>tableid</em>: JET_tableidNil</p></li>
<li><p><em>pvArg1</em>: <strong>NULL</strong></p></li>
<li><p><em>pvArg2</em>: <strong>NULL</strong></p></li>
<li><p><em>pvContext</em>: <strong>NULL</strong></p></li>
<li><p><em>ulUnused</em>: <strong>NULL</strong></p></li>
</ul>
<p>If an error is returned by the callback, it will be ignored.</p></td>
</tr>
<tr class="odd">
<td><p>JET_cbtypFreeCursorLS<br />
0x00000200</p></td>
<td><p>This callback will occur when the application needs to clean up the context handle for the Local Storage associated with a cursor that is being released by the database engine. For more information, see <a href="gg269243(v=exchg.10).md">JetSetLS</a>.</p>
<p>The function pointer for this callback reason is configured by means of <a href="gg294044(v=exchg.10).md">JetSetSystemParameter</a> with <a href="gg269310(v=exchg.10).md">JET_paramRuntimeCallback</a>.</p>
<p>The callback parameters will have the following values:</p>
<ul>
<li><p><em>sesid</em>: JET_sesidNil</p></li>
<li><p><em>dbid</em>: JET_dbidNil</p></li>
<li><p><em>tableid</em>: JET_tableidNil</p></li>
<li><p><em>pvArg1</em>: The context handle set using <a href="gg269243(v=exchg.10).md">JetSetLS</a></p></li>
<li><p><em>pvArg2</em>: <strong>NULL</strong></p></li>
<li><p><em>pvContext</em>: <strong>NULL</strong></p></li>
<li><p><em>ulUnused</em>: <strong>NULL</strong></p></li>
</ul>
<p>If an error is returned by the callback, it will be ignored.</p></td>
</tr>
<tr class="even">
<td><p>JET_cbtypFreeTableLS<br />
0x00000400</p></td>
<td><p>This callback will occur as the result of the need for the application to cleanup the context handle for the Local Storage associated with a table that is being released by the database engine. For more information, see <a href="gg269243(v=exchg.10).md">JetSetLS</a>.</p>
<p>The function pointer for this callback reason is configured by means of <a href="gg294044(v=exchg.10).md">JetSetSystemParameter</a> with <a href="gg269310(v=exchg.10).md">JET_paramRuntimeCallback</a>.</p>
<p>The callback parameters will have the following values:</p>
<ul>
<li><p><em>sesid</em>: JET_sesidNil</p></li>
<li><p><em>dbid</em>: JET_dbidNil</p></li>
<li><p><em>tableid</em>: JET_tableidNil</p></li>
<li><p><em>pvArg1</em>: The context handle set using <a href="gg269243(v=exchg.10).md">JetSetLS</a>.</p></li>
<li><p><em>pvArg2</em>: <strong>NULL</strong></p></li>
<li><p><em>pvContext</em>: <strong>NULL</strong></p></li>
<li><p><em>ulUnused</em>: <strong>NULL</strong></p></li>
</ul>
<p>If an error is returned by the callback, it will be ignored.</p></td>
</tr>
</tbody>
</table>


### Requirements

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>Client</strong></p></td>
<td><p>Requires Windows Vista or Windows XP.</p></td>
</tr>
<tr class="even">
<td><p><strong>Server</strong></p></td>
<td><p>Requires Windows Server 2008 or Windows Server 2003.</p></td>
</tr>
<tr class="odd">
<td><p><strong>Header</strong></p></td>
<td><p>Declared in Esent.h.</p></td>
</tr>
</tbody>
</table>


### See Also

[JET_CALLBACK](./jet-callback-callback-function.md)
