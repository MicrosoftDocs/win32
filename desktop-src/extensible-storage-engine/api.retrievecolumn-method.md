---
description: "Learn more about: Api.RetrieveColumn method"
title: Api.RetrieveColumn method 
TOCTitle: 'RetrieveColumn method '
ms:assetid: Overload:Microsoft.Isam.Esent.Interop.Api.RetrieveColumn
ms:mtpsurl: https://msdn.microsoft.com/library/microsoft.isam.esent.interop.api.retrievecolumn(v=EXCHG.10)
ms:contentKeyID: 55100835
ms.date: 07/30/2014
ms.topic: article
f1_keywords:
- Microsoft.Isam.Esent.Interop.Api.RetrieveColumn
dev_langs:
- CSharp
- JScript
- VB
- other
---

# Api.RetrieveColumn method

Include protected members  
Include inherited members  

## Overload list

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
<td><a href="dn334041(v=exchg.10).md">RetrieveColumn(JET_SESID, JET_TABLEID, JET_COLUMNID)</a></td>
<td>Retrieves a single column value from the current record. The record is that record associated with the index entry at the current position of the cursor.</td>
</tr>
<tr class="even">
<td><img src="../images/dn292146.pubmethod(exchg.10).gif" title="Public method" alt="Public method" /><img src="../images/dn292146.static(exchg.10).gif" title="Static member" alt="Static member" /></td>
<td><a href="dn334060(v=exchg.10).md">RetrieveColumn(JET_SESID, JET_TABLEID, JET_COLUMNID, RetrieveColumnGrbit, JET_RETINFO)</a></td>
<td>Retrieves a single column value from the current record. The record is that record associated with the index entry at the current position of the cursor. Alternatively, this function can retrieve a column from a record being created in the cursor copy buffer. This function can also retrieve column data from an index entry that references the current record. In addition to retrieving the actual column value, JetRetrieveColumn can also be used to retrieve the size of a column, before retrieving the column data itself so that application buffers can be sized appropriately.</td>
</tr>
</tbody>
</table>


Top

## See also

#### Reference

[Api class](./api-class.md)

[Api members](./api-members.md)

[Microsoft.Isam.Esent.Interop namespace](./microsoft.isam.esent.interop-namespace.md)
