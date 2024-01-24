---
description: "Learn more about: Api members"
title: Api members
TOCTitle: Api members
ms:assetid: AllMembers.T:Microsoft.Isam.Esent.Interop.Api
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.api_members(v=EXCHG.10)
ms:contentKeyID: 55100778
ms.date: 07/30/2014
ms.topic: article
---

# Api members

Include protected members  
Include inherited members  

Managed versions of the ESENT API. This class contains static methods that correspond to the unmanaged ESENT API. These methods throw exceptions when errors are returned. Helper methods for the ESENT API. These wrap JetMakeKey. Internal-only methods of the API. Helper methods for the ESENT API. These do data conversion for JetMakeKey. Helper methods for the ESENT API. These methods deal with database metadata. Helper methods for the ESENT API. These aren't interop versions of the API, but encapsulate very common uses of the functions. API members that are marked as obsolete. Helper methods for the ESENT API. These aren't interop versions of the API, but encapsulate very common uses of the functions. Helper methods for the ESENT API. These do data conversion for setting columns.

The [Api](./api-class.md) type exposes the following members.

## Methods

<table>
<thead>
<tr class="header">
<th> </th>
<th>Name</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn292138(v=exchg.10).md">DeserializeObjectFromColumn(JET_SESID, JET_TABLEID, JET_COLUMNID)</a></td>
<td>Deserialize an object from a column.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn292115(v=exchg.10).md">DeserializeObjectFromColumn(JET_SESID, JET_TABLEID, JET_COLUMNID, RetrieveColumnGrbit)</a></td>
<td>Deserialize an object from a column.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn292114(v=exchg.10).md">EscrowUpdate</a></td>
<td>Perform atomic addition on one column. The column must be of type <a href="hh577895(v=exchg.10).md">Long</a>. This function allows multiple sessions to update the same record concurrently without conflicts.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn292099(v=exchg.10).md">GetBookmark</a></td>
<td>Retrieves the bookmark for the record that is associated with the index entry at the current position of a cursor. This bookmark can then be used to reposition that cursor back to the same record using JetGotoBookmark.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn292098(v=exchg.10).md">GetColumnDictionary</a></td>
<td>Creates a dictionary which maps column names to their column IDs.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn292101(v=exchg.10).md">GetTableColumnid</a></td>
<td>Get the columnid of the specified column.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn292090(v=exchg.10).md">GetTableColumns(JET_SESID, JET_TABLEID)</a></td>
<td>Iterates over all the columns in the table, returning information about each one.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn292089(v=exchg.10).md">GetTableColumns(JET_SESID, JET_DBID, String)</a></td>
<td>Iterates over all the columns in the table, returning information about each one.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn292093(v=exchg.10).md">GetTableIndexes(JET_SESID, JET_TABLEID)</a></td>
<td>Iterates over all the indexes in the table, returning information about each one.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn292092(v=exchg.10).md">GetTableIndexes(JET_SESID, JET_DBID, String)</a></td>
<td>Iterates over all the indexs in the table, returning information about each one.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn292095(v=exchg.10).md">GetTableNames</a></td>
<td>Returns the names of the tables in the database.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn292094(v=exchg.10).md">IntersectIndexes</a></td>
<td>Intersect a group of index ranges and return the bookmarks of the records which are found in all the index ranges. Also see <a href="dn292212(v=exchg.10).md">JetIntersectIndexes(JET_SESID, [], Int32, JET_RECORDLIST, IntersectIndexesGrbit)</a>.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn292097(v=exchg.10).md">JetAddColumn</a></td>
<td>Add a new column to an existing table.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn292096(v=exchg.10).md">JetAttachDatabase</a></td>
<td>Attaches a database file for use with a database instance. In order to use the database, it will need to be subsequently opened with <a href="dn292219(v=exchg.10).md">JetOpenDatabase(JET_SESID, String, String, JET_DBID, OpenDatabaseGrbit)</a>.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn292100(v=exchg.10).md">JetAttachDatabase2</a></td>
<td>Attaches a database file for use with a database instance. In order to use the database, it will need to be subsequently opened with <a href="dn292219(v=exchg.10).md">JetOpenDatabase(JET_SESID, String, String, JET_DBID, OpenDatabaseGrbit)</a>.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn292102(v=exchg.10).md">JetBackupInstance</a></td>
<td>Performs a streaming backup of an instance, including all the attached databases, to a directory. With multiple backup methods supported by the engine, this is the simplest and most encapsulated function.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn292104(v=exchg.10).md">JetBeginExternalBackupInstance</a></td>
<td>Initiates an external backup while the engine and database are online and active.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn292103(v=exchg.10).md">JetBeginSession</a></td>
<td>Initialize a new ESENT session.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn292105(v=exchg.10).md">JetBeginTransaction</a></td>
<td>Causes a session to enter a transaction or create a new save point in an existing transaction.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn292106(v=exchg.10).md">JetBeginTransaction2</a></td>
<td>Causes a session to enter a transaction or create a new save point in an existing transaction.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn292107(v=exchg.10).md">JetCloseDatabase</a></td>
<td>Closes a database file that was previously opened with <a href="dn292219(v=exchg.10).md">JetOpenDatabase(JET_SESID, String, String, JET_DBID, OpenDatabaseGrbit)</a> or created with <a href="dn292118(v=exchg.10).md">JetCreateDatabase(JET_SESID, String, String, JET_DBID, CreateDatabaseGrbit)</a>.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn292108(v=exchg.10).md">JetCloseFileInstance</a></td>
<td>Closes a file that was opened with JetOpenFileInstance after the data from that file has been extracted using JetReadFileInstance.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn292109(v=exchg.10).md">JetCloseTable</a></td>
<td>Close an open table.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn292110(v=exchg.10).md">JetCommitTransaction</a></td>
<td>Commits the changes made to the state of the database during the current save point and migrates them to the previous save point. If the outermost save point is committed then the changes made during that save point will be committed to the state of the database and the session will exit the transaction.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn292112(v=exchg.10).md">JetCompact</a></td>
<td>Makes a copy of an existing database. The copy is compacted to a state optimal for usage. Data in the copied data will be packed according to the measures chosen for the indexes at index create. In this way, compacted data may be stored as densely as possible. Alternatively, compacted data may reserve space for subsequent record growth or index insertions.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn292113(v=exchg.10).md">JetComputeStats</a></td>
<td>Walks each index of a table to exactly compute the number of entries in an index, and the number of distinct keys in an index. This information, together with the number of database pages allocated for an index and the current time of the computation is stored in index metadata in the database. This data can be subsequently retrieved with information operations.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn292118(v=exchg.10).md">JetCreateDatabase</a></td>
<td>Creates and attaches a database file.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn292120(v=exchg.10).md">JetCreateDatabase2</a></td>
<td>Creates and attaches a database file with a maximum database size specified.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn292121(v=exchg.10).md">JetCreateIndex</a></td>
<td>Creates an index over data in an ESE database. An index can be used to locate specific data quickly.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn292123(v=exchg.10).md">JetCreateIndex2</a></td>
<td>Creates indexes over data in an ESE database.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn292122(v=exchg.10).md">JetCreateInstance</a></td>
<td>Allocates a new instance of the database engine.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn292126(v=exchg.10).md">JetCreateInstance2</a></td>
<td>Allocate a new instance of the database engine for use in a single process, with a display name specified.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn292127(v=exchg.10).md">JetCreateTable</a></td>
<td>Create an empty table. The newly created table is opened exclusively.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn292129(v=exchg.10).md">JetCreateTableColumnIndex3</a></td>
<td>Creates a table, adds columns, and indices on that table.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn292130(v=exchg.10).md">JetDefragment</a></td>
<td>Starts and stops database defragmentation tasks that improves data organization within a database.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn292145(v=exchg.10).md">JetDefragment2</a></td>
<td>Starts and stops database defragmentation tasks that improves data organization within a database.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn292131(v=exchg.10).md">JetDelete</a></td>
<td>Deletes the current record in a database table.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn292133(v=exchg.10).md">JetDeleteColumn</a></td>
<td>Deletes a column from a database table.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn292132(v=exchg.10).md">JetDeleteColumn2</a></td>
<td>Deletes a column from a database table.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn292135(v=exchg.10).md">JetDeleteIndex</a></td>
<td>Deletes an index from a database table.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn292134(v=exchg.10).md">JetDeleteTable</a></td>
<td>Deletes a table from a database.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn292139(v=exchg.10).md">JetDetachDatabase</a></td>
<td>Releases a database file that was previously attached to a database session.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn292136(v=exchg.10).md">JetDetachDatabase2</a></td>
<td>Releases a database file that was previously attached to a database session.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn292137(v=exchg.10).md">JetDupCursor</a></td>
<td>Duplicates an open cursor and returns a handle to the duplicated cursor. If the cursor that was duplicated was a read-only cursor then the duplicated cursor is also a read-only cursor. Any state related to constructing a search key or updating a record is not copied into the duplicated cursor. In addition, the location of the original cursor is not duplicated into the duplicated cursor. The duplicated cursor is always opened on the clustered index and its location is always on the first row of the table.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn292140(v=exchg.10).md">JetDupSession</a></td>
<td>Initialize a new ESE session in the same instance as the given sesid.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn292142(v=exchg.10).md">JetEndExternalBackupInstance</a></td>
<td>Ends an external backup session. This API is the last API in a series of APIs that must be called to execute a successful online (non-VSS based) backup.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn292143(v=exchg.10).md">JetEndExternalBackupInstance2</a></td>
<td>Ends an external backup session. This API is the last API in a series of APIs that must be called to execute a successful online (non-VSS based) backup.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn292144(v=exchg.10).md">JetEndSession</a></td>
<td>Ends a session.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn292148(v=exchg.10).md">JetEnumerateColumns</a></td>
<td>Efficiently retrieves a set of columns and their values from the current record of a cursor or the copy buffer of that cursor. The columns and values retrieved can be restricted by a list of column IDs, itagSequence numbers, and other characteristics. This column retrieval API is unique in that it returns information in dynamically allocated memory that is obtained using a user-provided realloc compatible callback. This new flexibility permits the efficient retrieval of column data with specific characteristics (such as size and multiplicity) that are unknown to the caller. This eliminates the need for the use of the discovery modes of JetRetrieveColumn to determine those characteristics in order to setup a final call to JetRetrieveColumn that will successfully retrieve the desired data.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn292150(v=exchg.10).md">JetEscrowUpdate</a></td>
<td>Performs an atomic addition operation on one column. This function allows multiple sessions to update the same record concurrently without conflicts. Also see <a href="dn292114(v=exchg.10).md">EscrowUpdate(JET_SESID, JET_TABLEID, JET_COLUMNID, Int32)</a>.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn292147(v=exchg.10).md">JetFreeBuffer</a></td>
<td>Frees memory that was allocated by a database engine call.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn292154(v=exchg.10).md">JetGetAttachInfoInstance</a></td>
<td>Used during a backup initiated by <a href="dn292104(v=exchg.10).md">JetBeginExternalBackupInstance(JET_INSTANCE, BeginExternalBackupGrbit)</a> to query an instance for the names of database files that should become part of the backup file set. Only databases that are currently attached to the instance using <a href="dn292096(v=exchg.10).md">JetAttachDatabase(JET_SESID, String, AttachDatabaseGrbit)</a> will be considered. These files may subsequently be opened using <a href="dn292230(v=exchg.10).md">JetOpenFileInstance(JET_INSTANCE, String, JET_HANDLE, Int64, Int64)</a> and read using <a href="dn332987(v=exchg.10).md">JetReadFileInstance(JET_INSTANCE, JET_HANDLE, [], Int32, Int32)</a>.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn292149(v=exchg.10).md">JetGetBookmark</a></td>
<td>Retrieves the bookmark for the record that is associated with the index entry at the current position of a cursor. This bookmark can then be used to reposition that cursor back to the same record using <a href="dn292200(v=exchg.10).md">JetGotoBookmark(JET_SESID, JET_TABLEID, [], Int32)</a>. The bookmark will be no longer than <a href="dn351215(v=exchg.10).md">BookmarkMost</a> bytes. Also see <a href="dn292099(v=exchg.10).md">GetBookmark(JET_SESID, JET_TABLEID)</a>.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn292158(v=exchg.10).md">JetGetColumnInfo(JET_SESID, JET_DBID, String, String, JET_COLUMNBASE)</a></td>
<td>Retrieves information about a column in a table.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn292151(v=exchg.10).md">JetGetColumnInfo(JET_SESID, JET_DBID, String, String, JET_COLUMNDEF)</a></td>
<td>Retrieves information about a table column.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn292152(v=exchg.10).md">JetGetColumnInfo(JET_SESID, JET_DBID, String, String, JET_COLUMNLIST)</a></td>
<td>Retrieves information about all columns in a table.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn292153(v=exchg.10).md">JetGetCurrentIndex</a></td>
<td>Ddetermines the name of the current index of a given cursor. This name is also used to later re-select that index as the current index using <a href="dn334011(v=exchg.10).md">JetSetCurrentIndex(JET_SESID, JET_TABLEID, String)</a>. It can also be used to discover the properties of that index using JetGetTableIndexInfo.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn292155(v=exchg.10).md">JetGetCursorInfo</a></td>
<td>Determine whether an update of the current record of a cursor will result in a write conflict, based on the current update status of the record. It is possible that a write conflict will ultimately be returned even if JetGetCursorInfo returns successfully. because another session may update the record before the current session is able to update the same record.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn292159(v=exchg.10).md">JetGetDatabaseFileInfo(String, JET_DBINFOMISC, JET_DbInfo)</a></td>
<td>Retrieves certain information about the given database.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn292161(v=exchg.10).md">JetGetDatabaseFileInfo(String, Int32, JET_DbInfo)</a></td>
<td>Retrieves certain information about the given database.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn292160(v=exchg.10).md">JetGetDatabaseFileInfo(String, Int64, JET_DbInfo)</a></td>
<td>Retrieves certain information about the given database.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn292162(v=exchg.10).md">JetGetDatabaseInfo(JET_SESID, JET_DBID, JET_DBINFOMISC, JET_DbInfo)</a></td>
<td>Retrieves certain information about the given database.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn292164(v=exchg.10).md">JetGetDatabaseInfo(JET_SESID, JET_DBID, Int32, JET_DbInfo)</a></td>
<td>Retrieves certain information about the given database.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn292167(v=exchg.10).md">JetGetDatabaseInfo(JET_SESID, JET_DBID, String, JET_DbInfo)</a></td>
<td>Retrieves certain information about the given database.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn292168(v=exchg.10).md">JetGetIndexInfo(JET_SESID, JET_DBID, String, String, JET_INDEXLIST)</a></td>
<td><strong>Obsolete.</strong> Retrieves information about indexes on a table.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn292172(v=exchg.10).md">JetGetIndexInfo(JET_SESID, JET_DBID, String, String, JET_INDEXID, JET_IdxInfo)</a></td>
<td>Retrieves information about indexes on a table.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn292166(v=exchg.10).md">JetGetIndexInfo(JET_SESID, JET_DBID, String, String, JET_INDEXLIST, JET_IdxInfo)</a></td>
<td>Retrieves information about indexes on a table.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn292171(v=exchg.10).md">JetGetIndexInfo(JET_SESID, JET_DBID, String, String, Int32, JET_IdxInfo)</a></td>
<td>Retrieves information about indexes on a table.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn292169(v=exchg.10).md">JetGetIndexInfo(JET_SESID, JET_DBID, String, String, String, JET_IdxInfo)</a></td>
<td>Retrieves information about indexes on a table.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn292173(v=exchg.10).md">JetGetIndexInfo(JET_SESID, JET_DBID, String, String, UInt16, JET_IdxInfo)</a></td>
<td>Retrieves information about indexes on a table.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn292170(v=exchg.10).md">JetGetInstanceInfo</a></td>
<td>Retrieves information about the instances that are running.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn292175(v=exchg.10).md">JetGetLock</a></td>
<td>Explicitly reserve the ability to update a row, write lock, or to explicitly prevent a row from being updated by any other session, read lock. Normally, row write locks are acquired implicitly as a result of updating rows. Read locks are usually not required because of record versioning. However, in some cases a transaction may desire to explicitly lock a row to enforce serialization, or to ensure that a subsequent operation will succeed.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn292174(v=exchg.10).md">JetGetLogInfoInstance</a></td>
<td>Used during a backup initiated by <a href="dn292104(v=exchg.10).md">JetBeginExternalBackupInstance(JET_INSTANCE, BeginExternalBackupGrbit)</a> to query an instance for the names of database patch files and logfiles that should become part of the backup file set. These files may subsequently be opened using <a href="dn292230(v=exchg.10).md">JetOpenFileInstance(JET_INSTANCE, String, JET_HANDLE, Int64, Int64)</a> and read using <a href="dn332987(v=exchg.10).md">JetReadFileInstance(JET_INSTANCE, JET_HANDLE, [], Int32, Int32)</a>.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn292177(v=exchg.10).md">JetGetLS</a></td>
<td>Enables the application to retrieve the context handle known as Local Storage that is associated with a cursor or the table associated with that cursor. This context handle must have been previously set using <a href="dn334015(v=exchg.10).md">JetSetLS(JET_SESID, JET_TABLEID, JET_LS, LsGrbit)</a>. JetGetLS can also be used to simultaneously fetch the current context handle for a cursor or table and reset that context handle.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn292179(v=exchg.10).md">JetGetObjectInfo(JET_SESID, JET_DBID, JET_OBJECTLIST)</a></td>
<td>Retrieves information about database objects.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn292178(v=exchg.10).md">JetGetObjectInfo(JET_SESID, JET_DBID, JET_objtyp, String, JET_OBJECTINFO)</a></td>
<td>Retrieves information about database objects.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn292181(v=exchg.10).md">JetGetRecordPosition</a></td>
<td>Returns the fractional position of the current record in the current index in the form of a <a href="dn335256(v=exchg.10).md">JET_RECPOS</a> structure. Also see <a href="dn292207(v=exchg.10).md">JetGotoPosition(JET_SESID, JET_TABLEID, JET_RECPOS)</a>.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn292180(v=exchg.10).md">JetGetSecondaryIndexBookmark</a></td>
<td>Retrieves a special bookmark for the secondary index entry at the current position of a cursor. This bookmark can then be used to efficiently reposition that cursor back to the same index entry using JetGotoSecondaryIndexBookmark. This is most useful when repositioning on a secondary index that contains duplicate keys or that contains multiple index entries for the same record.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn292182(v=exchg.10).md">JetGetSystemParameter(JET_INSTANCE, JET_SESID, JET_param, Int32, String, Int32)</a></td>
<td>Gets database configuration options.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn292185(v=exchg.10).md">JetGetSystemParameter(JET_INSTANCE, JET_SESID, JET_param, IntPtr, String, Int32)</a></td>
<td>Gets database configuration options.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn292186(v=exchg.10).md">JetGetTableColumnInfo(JET_SESID, JET_TABLEID, JET_COLUMNID, JET_COLUMNDEF)</a></td>
<td>Retrieves information about a table column.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn292187(v=exchg.10).md">JetGetTableColumnInfo(JET_SESID, JET_TABLEID, String, JET_COLUMNDEF)</a></td>
<td>Retrieves information about a table column.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn292189(v=exchg.10).md">JetGetTableColumnInfo(JET_SESID, JET_TABLEID, String, JET_COLUMNLIST)</a></td>
<td>Retrieves information about all columns in the table.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn292191(v=exchg.10).md">JetGetTableIndexInfo(JET_SESID, JET_TABLEID, String, JET_INDEXLIST)</a></td>
<td><strong>Obsolete.</strong> Retrieves information about indexes on a table.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn292190(v=exchg.10).md">JetGetTableIndexInfo(JET_SESID, JET_TABLEID, String, JET_INDEXID, JET_IdxInfo)</a></td>
<td>Retrieves information about indexes on a table.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn292196(v=exchg.10).md">JetGetTableIndexInfo(JET_SESID, JET_TABLEID, String, JET_INDEXLIST, JET_IdxInfo)</a></td>
<td>Retrieves information about indexes on a table.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn292193(v=exchg.10).md">JetGetTableIndexInfo(JET_SESID, JET_TABLEID, String, Int32, JET_IdxInfo)</a></td>
<td>Retrieves information about indexes on a table.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn292192(v=exchg.10).md">JetGetTableIndexInfo(JET_SESID, JET_TABLEID, String, String, JET_IdxInfo)</a></td>
<td>Retrieves information about indexes on a table.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn292195(v=exchg.10).md">JetGetTableIndexInfo(JET_SESID, JET_TABLEID, String, UInt16, JET_IdxInfo)</a></td>
<td>Retrieves information about indexes on a table.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn292197(v=exchg.10).md">JetGetTableInfo(JET_SESID, JET_TABLEID, JET_DBID, JET_TblInfo)</a></td>
<td>Retrieves various pieces of information about a table in a database.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn292198(v=exchg.10).md">JetGetTableInfo(JET_SESID, JET_TABLEID, JET_OBJECTINFO, JET_TblInfo)</a></td>
<td>Retrieves various pieces of information about a table in a database.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn292201(v=exchg.10).md">JetGetTableInfo(JET_SESID, JET_TABLEID, Int32, JET_TblInfo)</a></td>
<td>Retrieves various pieces of information about a table in a database.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn292202(v=exchg.10).md">JetGetTableInfo(JET_SESID, JET_TABLEID, [], JET_TblInfo)</a></td>
<td>Retrieves various pieces of information about a table in a database.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn292204(v=exchg.10).md">JetGetTableInfo(JET_SESID, JET_TABLEID, String, JET_TblInfo)</a></td>
<td>Retrieves various pieces of information about a table in a database.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn292199(v=exchg.10).md">JetGetTruncateLogInfoInstance</a></td>
<td>Used during a backup initiated by <a href="dn292104(v=exchg.10).md">JetBeginExternalBackupInstance(JET_INSTANCE, BeginExternalBackupGrbit)</a> to query an instance for the names of the transaction log files that can be safely deleted after the backup has successfully completed.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn292203(v=exchg.10).md">JetGetVersion</a></td>
<td>Retrieves the version of the database engine.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn292200(v=exchg.10).md">JetGotoBookmark</a></td>
<td>Positions a cursor to an index entry for the record that is associated with the specified bookmark. The bookmark can be used with any index defined over a table. The bookmark for a record can be retrieved using <a href="dn292149(v=exchg.10).md">JetGetBookmark(JET_SESID, JET_TABLEID, [], Int32, Int32)</a>.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn292207(v=exchg.10).md">JetGotoPosition</a></td>
<td>Moves a cursor to a new location that is a fraction of the way through the current index. Also see <a href="dn292181(v=exchg.10).md">JetGetRecordPosition(JET_SESID, JET_TABLEID, JET_RECPOS)</a>.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn292205(v=exchg.10).md">JetGotoSecondaryIndexBookmark</a></td>
<td>Positions a cursor to an index entry that is associated with the specified secondary index bookmark. The secondary index bookmark must be used with the same index over the same table from which it was originally retrieved. The secondary index bookmark for an index entry can be retrieved using <a href="dn292205(v=exchg.10).md">JetGotoSecondaryIndexBookmark(JET_SESID, JET_TABLEID, [], Int32, [], Int32, GotoSecondaryIndexBookmarkGrbit)</a>.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn292206(v=exchg.10).md">JetGrowDatabase</a></td>
<td>Extends the size of a database that is currently open.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn292208(v=exchg.10).md">JetIdle</a></td>
<td>Performs idle cleanup tasks or checks the version store status in ESE.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn292209(v=exchg.10).md">JetIndexRecordCount</a></td>
<td>Counts the number of entries in the current index from the current position forward. The current position is included in the count. The count can be greater than the total number of records in the table if the current index is over a multi-valued column and instances of the column have multiple-values. If the table is empty, then 0 will be returned for the count.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn292210(v=exchg.10).md">JetInit</a></td>
<td>Initialize the ESENT database engine.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn292214(v=exchg.10).md">JetInit2</a></td>
<td>Initialize the ESENT database engine.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn292212(v=exchg.10).md">JetIntersectIndexes</a></td>
<td>Computes the intersection between multiple sets of index entries from different secondary indices over the same table. This operation is useful for finding the set of records in a table that match two or more criteria that can be expressed using index ranges. Also see <a href="dn292094(v=exchg.10).md">IntersectIndexes(JET_SESID, [])</a>.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn292216(v=exchg.10).md">JetMakeKey</a></td>
<td>Constructs search keys that may then be used by <a href="dn334003(v=exchg.10).md">JetSeek(JET_SESID, JET_TABLEID, SeekGrbit)</a> and <a href="dn334024(v=exchg.10).md">JetSetIndexRange(JET_SESID, JET_TABLEID, SetIndexRangeGrbit)</a>.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn292218(v=exchg.10).md">JetMove(JET_SESID, JET_TABLEID, JET_Move, MoveGrbit)</a></td>
<td>Navigate through an index. The cursor can be positioned at the start or end of the index and moved backwards and forwards by a specified number of index entries. Also see <a href="dn334150(v=exchg.10).md">TryMoveFirst(JET_SESID, JET_TABLEID)</a>, <a href="dn334140(v=exchg.10).md">TryMoveLast(JET_SESID, JET_TABLEID)</a>, <a href="dn334095(v=exchg.10).md">TryMoveNext(JET_SESID, JET_TABLEID)</a>, <a href="dn334144(v=exchg.10).md">TryMovePrevious(JET_SESID, JET_TABLEID)</a>.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn292217(v=exchg.10).md">JetMove(JET_SESID, JET_TABLEID, Int32, MoveGrbit)</a></td>
<td>Navigate through an index. The cursor can be positioned at the start or end of the index and moved backwards and forwards by a specified number of index entries. Also see <a href="dn334150(v=exchg.10).md">TryMoveFirst(JET_SESID, JET_TABLEID)</a>, <a href="dn334140(v=exchg.10).md">TryMoveLast(JET_SESID, JET_TABLEID)</a>, <a href="dn334095(v=exchg.10).md">TryMoveNext(JET_SESID, JET_TABLEID)</a>, <a href="dn334144(v=exchg.10).md">TryMovePrevious(JET_SESID, JET_TABLEID)</a>.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn292219(v=exchg.10).md">JetOpenDatabase</a></td>
<td>Opens a database previously attached with <a href="dn292096(v=exchg.10).md">JetAttachDatabase(JET_SESID, String, AttachDatabaseGrbit)</a>, for use with a database session. This function can be called multiple times for the same database.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn292230(v=exchg.10).md">JetOpenFileInstance</a></td>
<td>Opens an attached database, database patch file, or transaction log file of an active instance for the purpose of performing a streaming fuzzy backup. The data from these files can subsequently be read through the returned handle using JetReadFileInstance. The returned handle must be closed using JetCloseFileInstance. An external backup of the instance must have been previously initiated using JetBeginExternalBackupInstance.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn292234(v=exchg.10).md">JetOpenTable</a></td>
<td>Opens a cursor on a previously created table.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn292231(v=exchg.10).md">JetOpenTempTable</a></td>
<td>Creates a temporary table with a single index. A temporary table stores and retrieves records just like an ordinary table created using JetCreateTableColumnIndex. However, temporary tables are much faster than ordinary tables due to their volatile nature. They can also be used to very quickly sort and perform duplicate removal on record sets when accessed in a purely sequential manner. Also see <a href="dn292233(v=exchg.10).md">JetOpenTempTable3(JET_SESID, [], Int32, JET_UNICODEINDEX, TempTableGrbit, JET_TABLEID, [])</a>. <a href="dn335326(v=exchg.10).md">JetOpenTemporaryTable(JET_SESID, JET_OPENTEMPORARYTABLE)</a>.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn292232(v=exchg.10).md">JetOpenTempTable2</a></td>
<td>Creates a temporary table with a single index. A temporary table stores and retrieves records just like an ordinary table created using JetCreateTableColumnIndex. However, temporary tables are much faster than ordinary tables due to their volatile nature. They can also be used to very quickly sort and perform duplicate removal on record sets when accessed in a purely sequential manner. Also see <a href="dn292231(v=exchg.10).md">JetOpenTempTable(JET_SESID, [], Int32, TempTableGrbit, JET_TABLEID, [])</a>, <a href="dn292233(v=exchg.10).md">JetOpenTempTable3(JET_SESID, [], Int32, JET_UNICODEINDEX, TempTableGrbit, JET_TABLEID, [])</a>. <a href="dn335326(v=exchg.10).md">JetOpenTemporaryTable(JET_SESID, JET_OPENTEMPORARYTABLE)</a>.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn292233(v=exchg.10).md">JetOpenTempTable3</a></td>
<td>Creates a temporary table with a single index. A temporary table stores and retrieves records just like an ordinary table created using JetCreateTableColumnIndex. However, temporary tables are much faster than ordinary tables due to their volatile nature. They can also be used to very quickly sort and perform duplicate removal on record sets when accessed in a purely sequential manner. Also see <a href="dn292231(v=exchg.10).md">JetOpenTempTable(JET_SESID, [], Int32, TempTableGrbit, JET_TABLEID, [])</a>, <a href="dn335326(v=exchg.10).md">JetOpenTemporaryTable(JET_SESID, JET_OPENTEMPORARYTABLE)</a>.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn332998(v=exchg.10).md">JetOSSnapshotFreeze</a></td>
<td>Starts a snapshot. While the snapshot is in progress, no write-to-disk activity by the engine can take place.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn292235(v=exchg.10).md">JetOSSnapshotPrepare</a></td>
<td>Begins the preparations for a snapshot session. A snapshot session is a short time interval in which the engine does not issue any write IOs to disk, so that the engine can participate in a volume snapshot session (when driven by a snapshot writer).</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn332986(v=exchg.10).md">JetOSSnapshotThaw</a></td>
<td>Notifies the engine that it can resume normal IO operations after a freeze period and a successful snapshot.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn332988(v=exchg.10).md">JetPrepareUpdate</a></td>
<td>Prepare a cursor for update.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn332987(v=exchg.10).md">JetReadFileInstance</a></td>
<td>Retrieves the contents of a file opened with <a href="dn292230(v=exchg.10).md">JetOpenFileInstance(JET_INSTANCE, String, JET_HANDLE, Int64, Int64)</a>.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn332989(v=exchg.10).md">JetRegisterCallback</a></td>
<td>Allows the application to configure the database engine to issue notifications to the application for specific events. These notifications are associated with a specific table and remain in effect only until the instance containing the table is shut down using <a href="dn334020(v=exchg.10).md">JetTerm(JET_INSTANCE)</a>.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn332990(v=exchg.10).md">JetRenameColumn</a></td>
<td>Changes the name of an existing column.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn332993(v=exchg.10).md">JetRenameTable</a></td>
<td>Changes the name of an existing table.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn332991(v=exchg.10).md">JetResetSessionContext</a></td>
<td>Disassociates a session from the current thread. This should be used in conjunction with <a href="dn334027(v=exchg.10).md">JetSetSessionContext(JET_SESID, IntPtr)</a>.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn332994(v=exchg.10).md">JetResetTableSequential</a></td>
<td>Notifies the database engine that the application is no longer scanning the entire index the cursor is positioned on. This call reverses a notification sent by <a href="dn334018(v=exchg.10).md">JetSetTableSequential(JET_SESID, JET_TABLEID, SetTableSequentialGrbit)</a>.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn332992(v=exchg.10).md">JetRestoreInstance</a></td>
<td>Restores and recovers a streaming backup of an instance including all the attached databases. It is designed to work with a backup created with the <a href="dn292102(v=exchg.10).md">JetBackupInstance(JET_INSTANCE, String, BackupGrbit, JET_PFNSTATUS)</a> function. This is the simplest and most encapsulated restore function.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn332995(v=exchg.10).md">JetRetrieveColumn(JET_SESID, JET_TABLEID, JET_COLUMNID, [], Int32, Int32, RetrieveColumnGrbit, JET_RETINFO)</a></td>
<td>Retrieves a single column value from the current record. The record is that record associated with the index entry at the current position of the cursor. Alternatively, this function can retrieve a column from a record being created in the cursor copy buffer. This function can also retrieve column data from an index entry that references the current record. In addition to retrieving the actual column value, JetRetrieveColumn can also be used to retrieve the size of a column, before retrieving the column data itself so that application buffers can be sized appropriately.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn332997(v=exchg.10).md">JetRetrieveColumn(JET_SESID, JET_TABLEID, JET_COLUMNID, [], Int32, Int32, Int32, RetrieveColumnGrbit, JET_RETINFO)</a></td>
<td>Retrieves a single column value from the current record. The record is that record associated with the index entry at the current position of the cursor. Alternatively, this function can retrieve a column from a record being created in the cursor copy buffer. This function can also retrieve column data from an index entry that references the current record. In addition to retrieving the actual column value, JetRetrieveColumn can also be used to retrieve the size of a column, before retrieving the column data itself so that application buffers can be sized appropriately.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn334004(v=exchg.10).md">JetRetrieveColumns</a></td>
<td>Retrieves multiple column values from the current record in a single operation. An array of JET_RETRIEVECOLUMN structures is used to describe the set of column values to be retrieved, and to describe output buffers for each column value to be retrieved.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn334002(v=exchg.10).md">JetRetrieveKey</a></td>
<td>Retrieves the key for the index entry at the current position of a cursor. Also see <a href="dn334085(v=exchg.10).md">RetrieveKey(JET_SESID, JET_TABLEID, RetrieveKeyGrbit)</a>.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn334001(v=exchg.10).md">JetRollback</a></td>
<td>Undoes the changes made to the state of the database and returns to the last save point. JetRollback will also close any cursors opened during the save point. If the outermost save point is undone, the session will exit the transaction.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn334003(v=exchg.10).md">JetSeek</a></td>
<td>Efficiently positions a cursor to an index entry that matches the search criteria specified by the search key in that cursor and the specified inequality. A search key must have been previously constructed using <a href="dn292216(v=exchg.10).md">JetMakeKey(JET_SESID, JET_TABLEID, [], Int32, MakeKeyGrbit)</a>. Also see <a href="dn334145(v=exchg.10).md">TrySeek(JET_SESID, JET_TABLEID, SeekGrbit)</a>.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn334009(v=exchg.10).md">JetSetColumn(JET_SESID, JET_TABLEID, JET_COLUMNID, [], Int32, SetColumnGrbit, JET_SETINFO)</a></td>
<td>The JetSetColumn function modifies a single column value in a modified record to be inserted or to update the current record. It can overwrite an existing value, add a new value to a sequence of values in a multi-valued column, remove a value from a sequence of values in a multi-valued column, or update all or part of a long value (a column of type <a href="hh577895(v=exchg.10).md">LongText</a> or <a href="hh577895(v=exchg.10).md">LongBinary</a>).</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn334008(v=exchg.10).md">JetSetColumn(JET_SESID, JET_TABLEID, JET_COLUMNID, [], Int32, Int32, SetColumnGrbit, JET_SETINFO)</a></td>
<td>The JetSetColumn function modifies a single column value in a modified record to be inserted or to update the current record. It can overwrite an existing value, add a new value to a sequence of values in a multi-valued column, remove a value from a sequence of values in a multi-valued column, or update all or part of a long value (a column of type <a href="hh577895(v=exchg.10).md">LongText</a> or <a href="hh577895(v=exchg.10).md">LongBinary</a>).</td>
</tr>
<tr class="even">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn334010(v=exchg.10).md">JetSetColumnDefaultValue</a></td>
<td>Changes the default value of an existing column.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn334006(v=exchg.10).md">JetSetColumns</a></td>
<td>Allows an application to set multiple column values in a single operation. An array of <a href="dn335260(v=exchg.10).md">JET_SETCOLUMN</a> structures is used to describe the set of column values to be set, and to describe input buffers for each column value to be set.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn334011(v=exchg.10).md">JetSetCurrentIndex</a></td>
<td>Set the current index of a cursor.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn334005(v=exchg.10).md">JetSetCurrentIndex2</a></td>
<td>Set the current index of a cursor.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn334012(v=exchg.10).md">JetSetCurrentIndex3</a></td>
<td>Set the current index of a cursor.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn334013(v=exchg.10).md">JetSetCurrentIndex4</a></td>
<td>Set the current index of a cursor.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn334014(v=exchg.10).md">JetSetDatabaseSize</a></td>
<td>Sets the size of an unopened database file.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn334024(v=exchg.10).md">JetSetIndexRange</a></td>
<td>Temporarily limits the set of index entries that the cursor can walk using <a href="dn292217(v=exchg.10).md">JetMove(JET_SESID, JET_TABLEID, Int32, MoveGrbit)</a> to those starting from the current index entry and ending at the index entry that matches the search criteria specified by the search key in that cursor and the specified bound criteria. A search key must have been previously constructed using <a href="dn292216(v=exchg.10).md">JetMakeKey(JET_SESID, JET_TABLEID, [], Int32, MakeKeyGrbit)</a>. Also see <a href="dn334099(v=exchg.10).md">TrySetIndexRange(JET_SESID, JET_TABLEID, SetIndexRangeGrbit)</a>.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn334015(v=exchg.10).md">JetSetLS</a></td>
<td>Enables the application to associate a context handle known as Local Storage with a cursor or the table associated with that cursor. This context handle can be used by the application to store auxiliary data that is associated with a cursor or table. The application is later notified using a runtime callback when the context handle must be released. This makes it possible to associate dynamically allocated state with a cursor or table.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn334027(v=exchg.10).md">JetSetSessionContext</a></td>
<td>Associates a session with the current thread using the given context handle. This association overrides the default engine requirement that a transaction for a given session must occur entirely on the same thread. Use <a href="dn332991(v=exchg.10).md">JetResetSessionContext(JET_SESID)</a> to remove the association.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn334028(v=exchg.10).md">JetSetSystemParameter(JET_INSTANCE, JET_SESID, JET_param, JET_CALLBACK, String)</a></td>
<td>Sets database configuration options.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn334017(v=exchg.10).md">JetSetSystemParameter(JET_INSTANCE, JET_SESID, JET_param, Int32, String)</a></td>
<td>Sets database configuration options.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn334029(v=exchg.10).md">JetSetSystemParameter(JET_INSTANCE, JET_SESID, JET_param, IntPtr, String)</a></td>
<td>Sets database configuration options.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn334018(v=exchg.10).md">JetSetTableSequential</a></td>
<td>Notifies the database engine that the application is scanning the entire index that the cursor is positioned on. Consequently, the methods that are used to access the index data will be tuned to make this scenario as fast as possible. Also see <a href="dn332994(v=exchg.10).md">JetResetTableSequential(JET_SESID, JET_TABLEID, ResetTableSequentialGrbit)</a>.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn334032(v=exchg.10).md">JetStopBackupInstance</a></td>
<td>Prevents streaming backup-related activity from continuing on a specific running instance, thus ending the streaming backup in a predictable way.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn334035(v=exchg.10).md">JetStopServiceInstance</a></td>
<td>Prepares an instance for termination.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn334020(v=exchg.10).md">JetTerm</a></td>
<td>Terminate an instance that was created with <a href="dn292210(v=exchg.10).md">JetInit(JET_INSTANCE)</a> or <a href="dn292122(v=exchg.10).md">JetCreateInstance(JET_INSTANCE, String)</a>.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn334037(v=exchg.10).md">JetTerm2</a></td>
<td>Terminate an instance that was created with <a href="dn292210(v=exchg.10).md">JetInit(JET_INSTANCE)</a> or <a href="dn292122(v=exchg.10).md">JetCreateInstance(JET_INSTANCE, String)</a>.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn334022(v=exchg.10).md">JetTruncateLogInstance</a></td>
<td>Used during a backup initiated by JetBeginExternalBackup to delete any transaction log files that will no longer be needed once the current backup completes successfully.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn334019(v=exchg.10).md">JetUnregisterCallback</a></td>
<td>Configures the database engine to stop issuing notifications to the application as previously requested through <a href="dn332989(v=exchg.10).md">JetRegisterCallback(JET_SESID, JET_TABLEID, JET_cbtyp, JET_CALLBACK, IntPtr, JET_HANDLE)</a>.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn334036(v=exchg.10).md">JetUpdate(JET_SESID, JET_TABLEID)</a></td>
<td>The JetUpdate function performs an update operation including inserting a new row into a table or updating an existing row. Deleting a table row is performed by calling <a href="dn292131(v=exchg.10).md">JetDelete(JET_SESID, JET_TABLEID)</a>.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn334023(v=exchg.10).md">JetUpdate(JET_SESID, JET_TABLEID, [], Int32, Int32)</a></td>
<td>The JetUpdate function performs an update operation including inserting a new row into a table or updating an existing row. Deleting a table row is performed by calling <a href="dn292131(v=exchg.10).md">JetDelete(JET_SESID, JET_TABLEID)</a>.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn334042(v=exchg.10).md">MakeKey(JET_SESID, JET_TABLEID, Boolean, MakeKeyGrbit)</a></td>
<td>Constructs a search key that may then be used by <a href="dn334003(v=exchg.10).md">JetSeek(JET_SESID, JET_TABLEID, SeekGrbit)</a> and <a href="dn334024(v=exchg.10).md">JetSetIndexRange(JET_SESID, JET_TABLEID, SetIndexRangeGrbit)</a>.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn334026(v=exchg.10).md">MakeKey(JET_SESID, JET_TABLEID, Byte, MakeKeyGrbit)</a></td>
<td>Constructs a search key that may then be used by <a href="dn334003(v=exchg.10).md">JetSeek(JET_SESID, JET_TABLEID, SeekGrbit)</a> and <a href="dn334024(v=exchg.10).md">JetSetIndexRange(JET_SESID, JET_TABLEID, SetIndexRangeGrbit)</a>.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn334044(v=exchg.10).md">MakeKey(JET_SESID, JET_TABLEID, [], MakeKeyGrbit)</a></td>
<td>Constructs a search key that may then be used by <a href="dn334003(v=exchg.10).md">JetSeek(JET_SESID, JET_TABLEID, SeekGrbit)</a> and <a href="dn334024(v=exchg.10).md">JetSetIndexRange(JET_SESID, JET_TABLEID, SetIndexRangeGrbit)</a>.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn334025(v=exchg.10).md">MakeKey(JET_SESID, JET_TABLEID, DateTime, MakeKeyGrbit)</a></td>
<td>Constructs a search key that may then be used by <a href="dn334003(v=exchg.10).md">JetSeek(JET_SESID, JET_TABLEID, SeekGrbit)</a> and <a href="dn334024(v=exchg.10).md">JetSetIndexRange(JET_SESID, JET_TABLEID, SetIndexRangeGrbit)</a>.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn334046(v=exchg.10).md">MakeKey(JET_SESID, JET_TABLEID, Double, MakeKeyGrbit)</a></td>
<td>Constructs a search key that may then be used by <a href="dn334003(v=exchg.10).md">JetSeek(JET_SESID, JET_TABLEID, SeekGrbit)</a> and <a href="dn334024(v=exchg.10).md">JetSetIndexRange(JET_SESID, JET_TABLEID, SetIndexRangeGrbit)</a>.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn334030(v=exchg.10).md">MakeKey(JET_SESID, JET_TABLEID, Guid, MakeKeyGrbit)</a></td>
<td>Constructs a search key that may then be used by <a href="dn334003(v=exchg.10).md">JetSeek(JET_SESID, JET_TABLEID, SeekGrbit)</a> and <a href="dn334024(v=exchg.10).md">JetSetIndexRange(JET_SESID, JET_TABLEID, SetIndexRangeGrbit)</a>.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn334048(v=exchg.10).md">MakeKey(JET_SESID, JET_TABLEID, Int16, MakeKeyGrbit)</a></td>
<td>Constructs a search key that may then be used by <a href="dn334003(v=exchg.10).md">JetSeek(JET_SESID, JET_TABLEID, SeekGrbit)</a> and <a href="dn334024(v=exchg.10).md">JetSetIndexRange(JET_SESID, JET_TABLEID, SetIndexRangeGrbit)</a>.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn334031(v=exchg.10).md">MakeKey(JET_SESID, JET_TABLEID, Int32, MakeKeyGrbit)</a></td>
<td>Constructs a search key that may then be used by <a href="dn334003(v=exchg.10).md">JetSeek(JET_SESID, JET_TABLEID, SeekGrbit)</a> and <a href="dn334024(v=exchg.10).md">JetSetIndexRange(JET_SESID, JET_TABLEID, SetIndexRangeGrbit)</a>.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn334050(v=exchg.10).md">MakeKey(JET_SESID, JET_TABLEID, Int64, MakeKeyGrbit)</a></td>
<td>Constructs a search key that may then be used by <a href="dn334003(v=exchg.10).md">JetSeek(JET_SESID, JET_TABLEID, SeekGrbit)</a> and <a href="dn334024(v=exchg.10).md">JetSetIndexRange(JET_SESID, JET_TABLEID, SetIndexRangeGrbit)</a>.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn334033(v=exchg.10).md">MakeKey(JET_SESID, JET_TABLEID, Single, MakeKeyGrbit)</a></td>
<td>Constructs a search key that may then be used by <a href="dn334003(v=exchg.10).md">JetSeek(JET_SESID, JET_TABLEID, SeekGrbit)</a> and <a href="dn334024(v=exchg.10).md">JetSetIndexRange(JET_SESID, JET_TABLEID, SetIndexRangeGrbit)</a>.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn334052(v=exchg.10).md">MakeKey(JET_SESID, JET_TABLEID, UInt16, MakeKeyGrbit)</a></td>
<td>Constructs a search key that may then be used by <a href="dn334003(v=exchg.10).md">JetSeek(JET_SESID, JET_TABLEID, SeekGrbit)</a> and <a href="dn334024(v=exchg.10).md">JetSetIndexRange(JET_SESID, JET_TABLEID, SetIndexRangeGrbit)</a>.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn334054(v=exchg.10).md">MakeKey(JET_SESID, JET_TABLEID, UInt32, MakeKeyGrbit)</a></td>
<td>Constructs a search key that may then be used by <a href="dn334003(v=exchg.10).md">JetSeek(JET_SESID, JET_TABLEID, SeekGrbit)</a> and <a href="dn334024(v=exchg.10).md">JetSetIndexRange(JET_SESID, JET_TABLEID, SetIndexRangeGrbit)</a>.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn334034(v=exchg.10).md">MakeKey(JET_SESID, JET_TABLEID, UInt64, MakeKeyGrbit)</a></td>
<td>Constructs a search key that may then be used by <a href="dn334003(v=exchg.10).md">JetSeek(JET_SESID, JET_TABLEID, SeekGrbit)</a> and <a href="dn334024(v=exchg.10).md">JetSetIndexRange(JET_SESID, JET_TABLEID, SetIndexRangeGrbit)</a>.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn334038(v=exchg.10).md">MakeKey(JET_SESID, JET_TABLEID, String, Encoding, MakeKeyGrbit)</a></td>
<td>Constructs a search key that may then be used by <a href="dn334003(v=exchg.10).md">JetSeek(JET_SESID, JET_TABLEID, SeekGrbit)</a> and <a href="dn334024(v=exchg.10).md">JetSetIndexRange(JET_SESID, JET_TABLEID, SetIndexRangeGrbit)</a>.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn334058(v=exchg.10).md">MoveAfterLast</a></td>
<td>Position the cursor after the last record in the table. A subsequent move previous will position the cursor on the last record.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn334057(v=exchg.10).md">MoveBeforeFirst</a></td>
<td>Position the cursor before the first record in the table. A subsequent move next will position the cursor on the first record.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn334040(v=exchg.10).md">ResetIndexRange</a></td>
<td>Removes an index range created with <a href="dn334024(v=exchg.10).md">JetSetIndexRange(JET_SESID, JET_TABLEID, SetIndexRangeGrbit)</a> or <a href="dn334099(v=exchg.10).md">TrySetIndexRange(JET_SESID, JET_TABLEID, SetIndexRangeGrbit)</a>. If no index range is present this method does nothing.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn334041(v=exchg.10).md">RetrieveColumn(JET_SESID, JET_TABLEID, JET_COLUMNID)</a></td>
<td>Retrieves a single column value from the current record. The record is that record associated with the index entry at the current position of the cursor.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn334060(v=exchg.10).md">RetrieveColumn(JET_SESID, JET_TABLEID, JET_COLUMNID, RetrieveColumnGrbit, JET_RETINFO)</a></td>
<td>Retrieves a single column value from the current record. The record is that record associated with the index entry at the current position of the cursor. Alternatively, this function can retrieve a column from a record being created in the cursor copy buffer. This function can also retrieve column data from an index entry that references the current record. In addition to retrieving the actual column value, JetRetrieveColumn can also be used to retrieve the size of a column, before retrieving the column data itself so that application buffers can be sized appropriately.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn334045(v=exchg.10).md">RetrieveColumnAsBoolean(JET_SESID, JET_TABLEID, JET_COLUMNID)</a></td>
<td>Retrieves a boolean column value from the current record. The record is that record associated with the index entry at the current position of the cursor.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn334078(v=exchg.10).md">RetrieveColumnAsBoolean(JET_SESID, JET_TABLEID, JET_COLUMNID, RetrieveColumnGrbit)</a></td>
<td>Retrieves a boolean column value from the current record. The record is that record associated with the index entry at the current position of the cursor.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn334047(v=exchg.10).md">RetrieveColumnAsByte(JET_SESID, JET_TABLEID, JET_COLUMNID)</a></td>
<td>Retrieves a byte column value from the current record. The record is that record associated with the index entry at the current position of the cursor.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn334074(v=exchg.10).md">RetrieveColumnAsByte(JET_SESID, JET_TABLEID, JET_COLUMNID, RetrieveColumnGrbit)</a></td>
<td>Retrieves a byte column value from the current record. The record is that record associated with the index entry at the current position of the cursor.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn334077(v=exchg.10).md">RetrieveColumnAsDateTime(JET_SESID, JET_TABLEID, JET_COLUMNID)</a></td>
<td>Retrieves a datetime column value from the current record. The record is that record associated with the index entry at the current position of the cursor.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn334051(v=exchg.10).md">RetrieveColumnAsDateTime(JET_SESID, JET_TABLEID, JET_COLUMNID, RetrieveColumnGrbit)</a></td>
<td>Retrieves a datetime column value from the current record. The record is that record associated with the index entry at the current position of the cursor.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn334053(v=exchg.10).md">RetrieveColumnAsDouble(JET_SESID, JET_TABLEID, JET_COLUMNID)</a></td>
<td>Retrieves a double column value from the current record. The record is that record associated with the index entry at the current position of the cursor.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn334084(v=exchg.10).md">RetrieveColumnAsDouble(JET_SESID, JET_TABLEID, JET_COLUMNID, RetrieveColumnGrbit)</a></td>
<td>Retrieves a double column value from the current record. The record is that record associated with the index entry at the current position of the cursor.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn334056(v=exchg.10).md">RetrieveColumnAsFloat(JET_SESID, JET_TABLEID, JET_COLUMNID)</a></td>
<td>Retrieves a float column value from the current record. The record is that record associated with the index entry at the current position of the cursor.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn334092(v=exchg.10).md">RetrieveColumnAsFloat(JET_SESID, JET_TABLEID, JET_COLUMNID, RetrieveColumnGrbit)</a></td>
<td>Retrieves a float column value from the current record. The record is that record associated with the index entry at the current position of the cursor.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn334093(v=exchg.10).md">RetrieveColumnAsGuid(JET_SESID, JET_TABLEID, JET_COLUMNID)</a></td>
<td>Retrieves a guid column value from the current record. The record is that record associated with the index entry at the current position of the cursor.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn334061(v=exchg.10).md">RetrieveColumnAsGuid(JET_SESID, JET_TABLEID, JET_COLUMNID, RetrieveColumnGrbit)</a></td>
<td>Retrieves a guid column value from the current record. The record is that record associated with the index entry at the current position of the cursor.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn334062(v=exchg.10).md">RetrieveColumnAsInt16(JET_SESID, JET_TABLEID, JET_COLUMNID)</a></td>
<td>Retrieves a single column value from the current record. The record is that record associated with the index entry at the current position of the cursor.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn334098(v=exchg.10).md">RetrieveColumnAsInt16(JET_SESID, JET_TABLEID, JET_COLUMNID, RetrieveColumnGrbit)</a></td>
<td>Retrieves an int16 column value from the current record. The record is that record associated with the index entry at the current position of the cursor.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn334100(v=exchg.10).md">RetrieveColumnAsInt32(JET_SESID, JET_TABLEID, JET_COLUMNID)</a></td>
<td>Retrieves a single column value from the current record. The record is that record associated with the index entry at the current position of the cursor.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn334068(v=exchg.10).md">RetrieveColumnAsInt32(JET_SESID, JET_TABLEID, JET_COLUMNID, RetrieveColumnGrbit)</a></td>
<td>Retrieves an int32 column value from the current record. The record is that record associated with the index entry at the current position of the cursor.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn334066(v=exchg.10).md">RetrieveColumnAsInt64(JET_SESID, JET_TABLEID, JET_COLUMNID)</a></td>
<td>Retrieves a single column value from the current record. The record is that record associated with the index entry at the current position of the cursor.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn334091(v=exchg.10).md">RetrieveColumnAsInt64(JET_SESID, JET_TABLEID, JET_COLUMNID, RetrieveColumnGrbit)</a></td>
<td>Retrieves a single column value from the current record. The record is that record associated with the index entry at the current position of the cursor.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn334067(v=exchg.10).md">RetrieveColumnAsString(JET_SESID, JET_TABLEID, JET_COLUMNID)</a></td>
<td>Retrieves a single column value from the current record. The record is that record associated with the index entry at the current position of the cursor. The Unicode encoding is used.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn334103(v=exchg.10).md">RetrieveColumnAsString(JET_SESID, JET_TABLEID, JET_COLUMNID, Encoding)</a></td>
<td>Retrieves a string column value from the current record. The record is that record associated with the index entry at the current position of the cursor.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn334070(v=exchg.10).md">RetrieveColumnAsString(JET_SESID, JET_TABLEID, JET_COLUMNID, Encoding, RetrieveColumnGrbit)</a></td>
<td>Retrieves a string column value from the current record. The record is that record associated with the index entry at the current position of the cursor.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn334069(v=exchg.10).md">RetrieveColumnAsUInt16(JET_SESID, JET_TABLEID, JET_COLUMNID)</a></td>
<td>Retrieves a uint16 column value from the current record. The record is that record associated with the index entry at the current position of the cursor.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn334106(v=exchg.10).md">RetrieveColumnAsUInt16(JET_SESID, JET_TABLEID, JET_COLUMNID, RetrieveColumnGrbit)</a></td>
<td>Retrieves a uint16 column value from the current record. The record is that record associated with the index entry at the current position of the cursor.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn334108(v=exchg.10).md">RetrieveColumnAsUInt32(JET_SESID, JET_TABLEID, JET_COLUMNID)</a></td>
<td>Retrieves a uint32 column value from the current record. The record is that record associated with the index entry at the current position of the cursor.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn334073(v=exchg.10).md">RetrieveColumnAsUInt32(JET_SESID, JET_TABLEID, JET_COLUMNID, RetrieveColumnGrbit)</a></td>
<td>Retrieves a uint32 column value from the current record. The record is that record associated with the index entry at the current position of the cursor.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn334072(v=exchg.10).md">RetrieveColumnAsUInt64(JET_SESID, JET_TABLEID, JET_COLUMNID)</a></td>
<td>Retrieves a uint64 column value from the current record. The record is that record associated with the index entry at the current position of the cursor.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn334113(v=exchg.10).md">RetrieveColumnAsUInt64(JET_SESID, JET_TABLEID, JET_COLUMNID, RetrieveColumnGrbit)</a></td>
<td>Retrieves a uint64 column value from the current record. The record is that record associated with the index entry at the current position of the cursor.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn334075(v=exchg.10).md">RetrieveColumns</a></td>
<td>Retrieves columns into ColumnValue objects.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn334076(v=exchg.10).md">RetrieveColumnSize(JET_SESID, JET_TABLEID, JET_COLUMNID)</a></td>
<td>Retrieves the size of a single column value from the current record. The record is that record associated with the index entry at the current position of the cursor. Alternatively, this function can retrieve a column from a record being created in the cursor copy buffer. This function can also retrieve column data from an index entry that references the current record.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn334117(v=exchg.10).md">RetrieveColumnSize(JET_SESID, JET_TABLEID, JET_COLUMNID, Int32, RetrieveColumnGrbit)</a></td>
<td>Retrieves the size of a single column value from the current record. The record is that record associated with the index entry at the current position of the cursor. Alternatively, this function can retrieve a column from a record being created in the cursor copy buffer. This function can also retrieve column data from an index entry that references the current record.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn334085(v=exchg.10).md">RetrieveKey</a></td>
<td>Retrieves the key for the index entry at the current position of a cursor.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn334120(v=exchg.10).md">SerializeObjectToColumn</a></td>
<td>Write a serialized form of an object to a column.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn334123(v=exchg.10).md">SetColumn(JET_SESID, JET_TABLEID, JET_COLUMNID, Boolean)</a></td>
<td>Modifies a single column value in a modified record to be inserted or to update the current record.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn334080(v=exchg.10).md">SetColumn(JET_SESID, JET_TABLEID, JET_COLUMNID, Byte)</a></td>
<td>Modifies a single column value in a modified record to be inserted or to update the current record.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn334121(v=exchg.10).md">SetColumn(JET_SESID, JET_TABLEID, JET_COLUMNID, [])</a></td>
<td>Modifies a single column value in a modified record to be inserted or to update the current record.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn334082(v=exchg.10).md">SetColumn(JET_SESID, JET_TABLEID, JET_COLUMNID, DateTime)</a></td>
<td>Modifies a single column value in a modified record to be inserted or to update the current record.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn334125(v=exchg.10).md">SetColumn(JET_SESID, JET_TABLEID, JET_COLUMNID, Double)</a></td>
<td>Modifies a single column value in a modified record to be inserted or to update the current record.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn334081(v=exchg.10).md">SetColumn(JET_SESID, JET_TABLEID, JET_COLUMNID, Guid)</a></td>
<td>Modifies a single column value in a modified record to be inserted or to update the current record.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn334127(v=exchg.10).md">SetColumn(JET_SESID, JET_TABLEID, JET_COLUMNID, Int16)</a></td>
<td>Modifies a single column value in a modified record to be inserted or to update the current record.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn334083(v=exchg.10).md">SetColumn(JET_SESID, JET_TABLEID, JET_COLUMNID, Int32)</a></td>
<td>Modifies a single column value in a modified record to be inserted or to update the current record.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn334130(v=exchg.10).md">SetColumn(JET_SESID, JET_TABLEID, JET_COLUMNID, Int64)</a></td>
<td>Modifies a single column value in a modified record to be inserted or to update the current record.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn334087(v=exchg.10).md">SetColumn(JET_SESID, JET_TABLEID, JET_COLUMNID, Single)</a></td>
<td>Modifies a single column value in a modified record to be inserted or to update the current record.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn334132(v=exchg.10).md">SetColumn(JET_SESID, JET_TABLEID, JET_COLUMNID, UInt16)</a></td>
<td>Modifies a single column value in a modified record to be inserted or to update the current record.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn334086(v=exchg.10).md">SetColumn(JET_SESID, JET_TABLEID, JET_COLUMNID, UInt32)</a></td>
<td>Modifies a single column value in a modified record to be inserted or to update the current record.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn334135(v=exchg.10).md">SetColumn(JET_SESID, JET_TABLEID, JET_COLUMNID, UInt64)</a></td>
<td>Modifies a single column value in a modified record to be inserted or to update the current record.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn334089(v=exchg.10).md">SetColumn(JET_SESID, JET_TABLEID, JET_COLUMNID, [], SetColumnGrbit)</a></td>
<td>Modifies a single column value in a modified record to be inserted or to update the current record.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn334136(v=exchg.10).md">SetColumn(JET_SESID, JET_TABLEID, JET_COLUMNID, String, Encoding)</a></td>
<td>Modifies a single column value in a modified record to be inserted or to update the current record.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn334090(v=exchg.10).md">SetColumn(JET_SESID, JET_TABLEID, JET_COLUMNID, String, Encoding, SetColumnGrbit)</a></td>
<td>Modifies a single column value in a modified record to be inserted or to update the current record.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn334138(v=exchg.10).md">SetColumns</a></td>
<td>Sets columns from ColumnValue objects.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn334139(v=exchg.10).md">TryGetLock</a></td>
<td>Explicitly reserve the ability to update a row, write lock, or to explicitly prevent a row from being updated by any other session, read lock. Normally, row write locks are acquired implicitly as a result of updating rows. Read locks are usually not required because of record versioning. However, in some cases a transaction may desire to explicitly lock a row to enforce serialization, or to ensure that a subsequent operation will succeed.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn334094(v=exchg.10).md">TryMove</a></td>
<td>Try to navigate through an index. If the navigation succeeds this method returns true. If there is no record to navigate to this method returns false; an exception will be thrown for other errors.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn334150(v=exchg.10).md">TryMoveFirst</a></td>
<td>Try to move to the first record in the table. If the table is empty this returns false, if a different error is encountered an exception is thrown.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn334140(v=exchg.10).md">TryMoveLast</a></td>
<td>Try to move to the last record in the table. If the table is empty this returns false, if a different error is encountered an exception is thrown.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn334095(v=exchg.10).md">TryMoveNext</a></td>
<td>Try to move to the next record in the table. If there is not a next record this returns false, if a different error is encountered an exception is thrown.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn334144(v=exchg.10).md">TryMovePrevious</a></td>
<td>Try to move to the previous record in the table. If there is not a previous record this returns false, if a different error is encountered an exception is thrown.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn334096(v=exchg.10).md">TryOpenTable</a></td>
<td>Try to open a table.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn334145(v=exchg.10).md">TrySeek</a></td>
<td>Efficiently positions a cursor to an index entry that matches the search criteria specified by the search key in that cursor and the specified inequality. A search key must have been previously constructed using JetMakeKey.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn334099(v=exchg.10).md">TrySetIndexRange</a></td>
<td>Temporarily limits the set of index entries that the cursor can walk using JetMove to those starting from the current index entry and ending at the index entry that matches the search criteria specified by the search key in that cursor and the specified bound criteria. A search key must have been previously constructed using JetMakeKey. Returns true if the index range is non-empty, false otherwise.</td>
</tr>
</tbody>
</table>


Top

## See also

#### Reference

[Api class](./api-class.md)

[Microsoft.Isam.Esent.Interop namespace](./microsoft.isam.esent.interop-namespace.md)
