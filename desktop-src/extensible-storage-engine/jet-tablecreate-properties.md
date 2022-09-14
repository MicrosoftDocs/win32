---
description: "Learn more about: JET_TABLECREATE properties"
title: JET_TABLECREATE properties
TOCTitle: JET_TABLECREATE properties
ms:assetid: Properties.T:Microsoft.Isam.Esent.Interop.JET_TABLECREATE
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.jet_tablecreate_properties(v=EXCHG.10)
ms:contentKeyID: 55103995
ms.date: 07/30/2014
ms.topic: article
---

# JET_TABLECREATE properties

Include protected members  
Include inherited members  

The [JET_TABLECREATE](./jet-tablecreate-class.md) type exposes the following members.

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
<td><a href="dn351077(v=exchg.10).md">cbSeparateLV</a></td>
<td>Gets or sets the heuristic size to separate a intrinsic LV from the primary record.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292128.pubproperty(exchg.10).gif" title="Public property" alt="Public property" /></td>
<td><a href="dn351078(v=exchg.10).md">cbtyp</a></td>
<td>Gets or sets a type of the callback function.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292128.pubproperty(exchg.10).gif" title="Public property" alt="Public property" /></td>
<td><a href="dn351080(v=exchg.10).md">cColumns</a></td>
<td>Gets or sets the number of columns to create.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292128.pubproperty(exchg.10).gif" title="Public property" alt="Public property" /></td>
<td><a href="dn351079(v=exchg.10).md">cCreated</a></td>
<td>Gets or sets the count of objects created (columns+table+indexes+callbacks).</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292128.pubproperty(exchg.10).gif" title="Public property" alt="Public property" /></td>
<td><a href="dn351081(v=exchg.10).md">cIndexes</a></td>
<td>Gets or sets the number of indices to create.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292128.pubproperty(exchg.10).gif" title="Public property" alt="Public property" /></td>
<td><a href="dn351082(v=exchg.10).md">grbit</a></td>
<td>Gets or sets the table options.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292128.pubproperty(exchg.10).gif" title="Public property" alt="Public property" /></td>
<td><a href="dn351087(v=exchg.10).md">pLVSpacehints</a></td>
<td>Gets or sets space allocation, maintenance, and usage hints for Separated LV tree, of type <a href="dn351095(v=exchg.10).md">JET_SPACEHINTS</a>.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292128.pubproperty(exchg.10).gif" title="Public property" alt="Public property" /></td>
<td><a href="dn351083(v=exchg.10).md">pSeqSpacehints</a></td>
<td>Gets or sets space allocation, maintenance, and usage hints for default sequential index.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292128.pubproperty(exchg.10).gif" title="Public property" alt="Public property" /></td>
<td><a href="dn351086(v=exchg.10).md">rgcolumncreate</a></td>
<td>Gets or sets an array of column creation info, of type <a href="dn335028(v=exchg.10).md">JET_COLUMNCREATE</a>.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292128.pubproperty(exchg.10).gif" title="Public property" alt="Public property" /></td>
<td><a href="dn351089(v=exchg.10).md">rgindexcreate</a></td>
<td>Gets or sets an array of indices to create, of type <a href="dn335112(v=exchg.10).md">JET_INDEXCREATE</a>.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292128.pubproperty(exchg.10).gif" title="Public property" alt="Public property" /></td>
<td><a href="dn351090(v=exchg.10).md">szCallback</a></td>
<td>Gets or sets a callback function to use for the table. This is in the form &quot;module!functionName&quot;, and assumes unmanaged code. See <strong>JetRegisterCallback(JET_SESID, JET_TABLEID, JET_cbtyp, JET_CALLBACK, IntPtr, JET_HANDLE)</strong> for an alternative.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292128.pubproperty(exchg.10).gif" title="Public property" alt="Public property" /></td>
<td><a href="dn351092(v=exchg.10).md">szTableName</a></td>
<td>Gets or sets the name of the table to create.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292128.pubproperty(exchg.10).gif" title="Public property" alt="Public property" /></td>
<td><a href="dn351093(v=exchg.10).md">szTemplateTableName</a></td>
<td>Gets or sets the name of the table from which to inherit base DDL.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292128.pubproperty(exchg.10).gif" title="Public property" alt="Public property" /></td>
<td><a href="dn351099(v=exchg.10).md">tableid</a></td>
<td>Gets or sets the returned tabledid.</td>
</tr>
<tr class="odd">
<td><img src="../images/dn292128.pubproperty(exchg.10).gif" title="Public property" alt="Public property" /></td>
<td><a href="dn351101(v=exchg.10).md">ulDensity</a></td>
<td>Gets or sets the table density.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292128.pubproperty(exchg.10).gif" title="Public property" alt="Public property" /></td>
<td><a href="dn351102(v=exchg.10).md">ulPages</a></td>
<td>Gets or sets the initial pages to allocate for table.</td>
</tr>
</tbody>
</table>


Top

## See also

#### Reference

[JET_TABLECREATE class](./jet-tablecreate-class.md)

[Microsoft.Isam.Esent.Interop namespace](./microsoft.isam.esent.interop-namespace.md)
