---
description: "Learn more about: JetPrereadKeys Function"
title: JetPrereadKeys Function
TOCTitle: JetPrereadKeys Function
ms:assetid: fc2f46bc-1f81-4af2-aa63-9757e819efc2
ms:mtpsurl: https://msdn.microsoft.com/library/Gg294143(v=EXCHG.10)
ms:contentKeyID: 32765757
ms.date: 04/11/2016
ms.topic: reference
api_name: 
- JetPrereadKeys
topic_type: 
- apiref
- kbArticle
api_type: 
- COM
- DLLExport
api_location: 
- ESENT.DLL
ROBOTS: INDEX,FOLLOW

---

# JetPrereadKeys Function


_**Applies to:** Windows | Windows Server_

## JetPrereadKeys Function

The **JetPrereadKeys** function reads key values to improve the performance of version store cleanup.

**Windows 7:  PrereadKeys** function is introduced in Windows 7.

```cpp
    JET_ERR JET_API JetPrereadKeys(
      __in JET_SESID sesid,
      __in JET_TABLEID tableid,
      __in_ecount(ckeys) const void ** rgpvKeys,
      __in_ecount(ckeys) const unsigned long * rgcbKeys,
      __in long ckeys,
      __out_opt long * pckeysPreread,
      __in JET_GRBIT grbit
     );
```

### Parameters

*sesid*

The database session context to use for the API call.

*tableid*

The cursor to use for this call.

*rgpvKeys*

An array of pointers to keys. Keys can be made with [JetMakeKey](./jetmakekey-function.md) or retrieved with [JetGetBookmark](./jetgetbookmark-function.md). The keys must be sorted in ascending or descending order, depending on the grbit passed. Keys can be sorted with memcmp.

*rgcbKeys*

An array of key lengths. rgpvKeys\[n\] should point to a key of length rgcbKeys\[n\]

*ckeys*

The number of keys. rgpvKeys and rgcbKeys must each point to an array with at least ckeys elements.

*pckeysPreread*

Returns the number of keys that prereads were actually issued for. This parameter can be NULL.

*grbit*

This must be either JET_bitPrereadForward or JET_bitPrereadBackward. If grbit is JET_bitPrereadForward, the keys must be sorted in ascending order. If grbit is JET_bitPrereadBackward, the keys must be sorted in descending order.

### Return Value

This function returns the [JET_ERR](./jet-err.md) datatype with one of the following return codes. For more information about the possible ESE errors, see [Extensible Storage Engine Errors](./extensible-storage-engine-errors.md) and [Error Handling Parameters](./error-handling-parameters.md).

Various I/O errors can be returned along with these API usage errors:

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Return code</p></th>
<th><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>JET_errInvalidGrbit</p></td>
<td><p>Grbit was neither JET_bitPrereadForward nor JET_bitPrereadBackward.</p></td>
</tr>
<tr class="even">
<td><p>JET_errInvalidBufferSize</p></td>
<td><p>An incorrect key size has been passed in. Keys can neither be 0 nor longer than the maximum key length for the table.</p></td>
</tr>
<tr class="odd">
<td><p>JET_errInvalidParameter</p></td>
<td><p>An invalid parameter has been passed in. This can be caused by a null value for a required parameter or can indicate that the key array is not sorted properly.</p></td>
</tr>
</tbody>
</table>


**JetPrereadKeys** traverses the internal pages of the b-tree to determine which leaf pages contain the keys specified by rgpvKeys/rgcbKeys. The list of leaf pages is sorted and then prereads are issued for the ranges of pages. The number of pages that can be preread is limited so it is possible that not all keys may be preread. In that case, the number of keys actually preread is returned in pckeysPreread.

#### Requirements

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>Client</strong></p></td>
<td><p>Requires Windows 7.</p></td>
</tr>
<tr class="even">
<td><p><strong>Server</strong></p></td>
<td><p>Requires Windows Server 2008 R2.</p></td>
</tr>
<tr class="odd">
<td><p><strong>Header</strong></p></td>
<td><p>Declared in Esent.h.</p></td>
</tr>
<tr class="even">
<td><p><strong>Library</strong></p></td>
<td><p>Use ESENT.lib.</p></td>
</tr>
<tr class="odd">
<td><p><strong>DLL</strong></p></td>
<td><p>Requires ESENT.dll.</p></td>
</tr>
</tbody>
</table>
