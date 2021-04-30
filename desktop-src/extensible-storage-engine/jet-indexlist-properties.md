---
description: "Learn more about: JET_INDEXLIST properties"
title: JET_INDEXLIST properties
TOCTitle: JET_INDEXLIST properties
ms:assetid: Properties.T:Microsoft.Isam.Esent.Interop.JET_INDEXLIST
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.jet_indexlist_properties(v=EXCHG.10)
ms:contentKeyID: 55103599
ms.date: 07/30/2014
ms.topic: article
---

# JET_INDEXLIST properties

Include protected members  
Include inherited members  

The [JET_INDEXLIST](./jet-indexlist-class.md) type exposes the following members.

## Properties

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
<td><img src="../images/dn292128.pubproperty(exchg.10).gif" title="Public property" alt="Public property" /></td>
<td><a href="dn335125(v=exchg.10).md">columnidcColumn</a></td>
<td>Gets the columnid of the column in the temporary table which stores the number of columns in the index key. The column is of type <a href="hh577895(v=exchg.10).md">Long</a>.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292128.pubproperty(exchg.10).gif" title="Public property" alt="Public property" /></td>
<td><a href="dn335126(v=exchg.10).md">columnidcEntry</a></td>
<td>Gets the columnid of the column in the temporary table which stores the number of entries in the index. This value is not current and is only is updated by &quot;Api.JetComputeStats&quot;. The column is of type <a href="hh577895(v=exchg.10).md">Long</a>.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292128.pubproperty(exchg.10).gif" title="Public property" alt="Public property" /></td>
<td><a href="dn335127(v=exchg.10).md">columnidcKey</a></td>
<td>Gets the columnid of the column in the temporary table which stores the number of unique keys in the index. This value is not current and is only is updated by &quot;Api.JetComputeStats&quot;. The column is of type <a href="hh577895(v=exchg.10).md">Long</a>.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292128.pubproperty(exchg.10).gif" title="Public property" alt="Public property" /></td>
<td><a href="dn335129(v=exchg.10).md">columnidcoltyp</a></td>
<td>Gets the columnid of the column in the temporary table which stores the column type of the column being indexed. The column is of type <a href="hh577895(v=exchg.10).md">Long</a>.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292128.pubproperty(exchg.10).gif" title="Public property" alt="Public property" /></td>
<td><a href="dn335130(v=exchg.10).md">columnidcolumnid</a></td>
<td>Gets the columnid of the column in the temporary table which stores the columnid of the column being indexed. The column is of type <a href="hh577895(v=exchg.10).md">Long</a>.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292128.pubproperty(exchg.10).gif" title="Public property" alt="Public property" /></td>
<td><a href="dn335167(v=exchg.10).md">columnidcolumnname</a></td>
<td>Gets the columnid of the column in the temporary table which stores the grbit that apply to the indexed column. See <a href="hh579266(v=exchg.10).md">IndexKeyGrbit</a>. The column is of type <a href="hh577895(v=exchg.10).md">Text</a>.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292128.pubproperty(exchg.10).gif" title="Public property" alt="Public property" /></td>
<td><a href="dn335168(v=exchg.10).md">columnidCp</a></td>
<td>Gets the columnid of the column in the temporary table which stores the code page of the indexed column. The column is of type <a href="hh577895(v=exchg.10).md">Short</a>.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292128.pubproperty(exchg.10).gif" title="Public property" alt="Public property" /></td>
<td><a href="dn335136(v=exchg.10).md">columnidcPage</a></td>
<td>Gets the columnid of the column in the temporary table which stores the number of pages in the index. This value is not current and is only is updated by &quot;Api.JetComputeStats&quot;. The column is of type <a href="hh577895(v=exchg.10).md">Long</a>.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292128.pubproperty(exchg.10).gif" title="Public property" alt="Public property" /></td>
<td><a href="dn335169(v=exchg.10).md">columnidgrbitColumn</a></td>
<td>Gets the columnid of the column in the temporary table which stores the grbit that apply to the indexed column. See <a href="hh579266(v=exchg.10).md">IndexKeyGrbit</a>. The column is of type <a href="hh577895(v=exchg.10).md">Long</a>.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292128.pubproperty(exchg.10).gif" title="Public property" alt="Public property" /></td>
<td><a href="dn335134(v=exchg.10).md">columnidgrbitIndex</a></td>
<td>Gets the columnid of the column in the temporary table which stores the grbits used on the index. See <a href="hh578433(v=exchg.10).md">CreateIndexGrbit</a>. The column is of type <a href="hh577895(v=exchg.10).md">Long</a>.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292128.pubproperty(exchg.10).gif" title="Public property" alt="Public property" /></td>
<td><a href="dn335170(v=exchg.10).md">columnidiColumn</a></td>
<td>Gets the columnid of the column in the temporary table which stores the index of of this column in the index key. The column is of type <a href="hh577895(v=exchg.10).md">Long</a>.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292128.pubproperty(exchg.10).gif" title="Public property" alt="Public property" /></td>
<td><a href="dn335138(v=exchg.10).md">columnidindexname</a></td>
<td>Gets the columnid of the column in the temporary table which stores the name of the index. The column is of type <a href="hh577895(v=exchg.10).md">Text</a>.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292128.pubproperty(exchg.10).gif" title="Public property" alt="Public property" /></td>
<td><a href="dn335171(v=exchg.10).md">columnidLangid</a></td>
<td>Gets the columnid of the column in the temporary table which stores the language id (LCID) of the index. The column is of type <a href="hh577895(v=exchg.10).md">Short</a>.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292128.pubproperty(exchg.10).gif" title="Public property" alt="Public property" /></td>
<td><a href="dn335172(v=exchg.10).md">columnidLCMapFlags</a></td>
<td>Gets the columnid of the column in the temporary table which stores the unicode normalization flags for the index. The column is of type <a href="hh577895(v=exchg.10).md">Long</a>.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292128.pubproperty(exchg.10).gif" title="Public property" alt="Public property" /></td>
<td><a href="dn335173(v=exchg.10).md">cRecord</a></td>
<td>Gets the number of records in the temporary table.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292128.pubproperty(exchg.10).gif" title="Public property" alt="Public property" /></td>
<td><a href="dn335174(v=exchg.10).md">tableid</a></td>
<td>Gets tableid of the temporary table. This should be closed when the table is no longer needed.</td>
</tr>
</tbody>
</table>


Top

## See also

#### Reference

[JET_INDEXLIST class](./jet-indexlist-class.md)

[Microsoft.Isam.Esent.Interop namespace](./microsoft.isam.esent.interop-namespace.md)
