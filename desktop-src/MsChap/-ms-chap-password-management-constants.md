---
title: MS-CHAP Password Management Constants
description: The MS-CHAP Password Management API uses the following constants.
ms.assetid: 25a703e7-943b-4670-8dd4-64ff9ab4568a
topic_type:
- apiref
api_name:
- CYPHER_BLOCK_LENGTH
api_location:
- MsChapp.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MS-CHAP Password Management Constants

The MS-CHAP Password Management API uses the following constants.



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th style="text-align: left;">Constant/value</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td style="text-align: left;"><span id="CYPHER_BLOCK_LENGTH"></span><span id="cypher_block_length"></span><dl> <dt><strong>CYPHER_BLOCK_LENGTH</strong></dt> <dt>8</dt> </dl></td>
<td style="text-align: left;">The defined length of the [<strong>CYPHER_BLOCK</strong>](/windows/previous-versions/MsChapp/ns-mschapp-_cypher_block?branch=master) structure, in bytes.
<blockquote>
[!Note]<br />
The value of <strong>CYPHER_BLOCK_LENGTH</strong> is determined by the minimum number of bytes used by the Data Encryption Standard (DES) cipher in MS-CHAP password management.
</blockquote>
<br/></td>
</tr>
</tbody>
</table>



## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>MsChapp.h</dt> </dl> |



 

 





