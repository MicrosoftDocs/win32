---
title: Common Errors
description: The following table contains a list of common errors that can occur based on the scope of the group being nested.
ms.assetid: 844d4280-a943-4906-b0c6-0c650ef9c114
ms.tgt_platform: multiple
keywords:
- Common Errors AD
ms.topic: article
ms.date: 05/31/2018
---

# Common Errors

The following table contains a list of common errors that can occur based on the scope of the group being nested.



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>HRESULT</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>0x8007001F</td>
<td>General failure. This error occurs if you attempt to:
<ul>
<li>Add a domain local group to a global or universal group or a domain local group in another domain. Domain local groups can only be added as members to other domain local groups in the same domain.</li>
<li>Add a universal group to a global group. Universal groups can be added to universal and domain local groups, but not global groups.</li>
</ul></td>
</tr>
<tr class="even">
<td>0x8007202F</td>
<td><strong>ERROR_DS_CONSTRAINT_VIOLATION</strong>. This error occurs if you attempt to add a security group to another group in a domain running in mixed mode. Security groups cannot be nested in mixed mode; security groups can only be nested in native mode.</td>
</tr>
</tbody>
</table>



 

 

 




