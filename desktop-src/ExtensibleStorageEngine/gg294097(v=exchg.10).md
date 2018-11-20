---
title: JET_UNICODEINDEX Structure
TOCTitle: JET_UNICODEINDEX Structure
ms:assetid: d0b8ef74-850e-4e21-9f71-b56ec472aa0f
ms:mtpsurl: https://msdn.microsoft.com/en-us/library/Gg294097(v=EXCHG.10)
ms:contentKeyID: 32765712
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

# JET\_UNICODEINDEX Structure


_**Applies to:** Windows | Windows Server_

## JET\_UNICODEINDEX Structure

The **JET\_UNICODEINDEX** structure customizes how Unicode data gets normalized when an index is created over a Unicode column.

    typedef struct tagJET_UNICODEINDEX {
      unsigned long lcid;
      unsigned long dwMapFlags;
    } JET_UNICODEINDEX;

### Members

**lcid**

The Locale ID to use when normalizing the data. Any locale may be used as long as the appropriate language pack has been installed on the machine. The one exception is that the Language Neutral locale (LCID of zero) is illegal.

**dwMapFlags**

These flags get passed to [LCMapString](http://go.microsoft.com/fwlink/?linkid=180732) when Unicode data gets normalized to a key, which enables user-defined flags to override the default.

**Windows 2000**:  The only two legal values for **dwFlags** are:

  - ( LCMAP\_SORTKEY | NORM\_IGNORECASE | NORM\_IGNOREKANATYPE | NORM\_IGNOREWIDTH | NORM\_IGNORENONSPACE )

<!-- end list -->

  - ( LCMAP\_SORTKEY | NORM\_IGNORECASE | NORM\_IGNOREKANATYPE | NORM\_IGNOREWIDTH )

**dwMapFlags** has the following restrictions.

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Value</p></th>
<th><p>Meaning</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>LCMAP_SORTKEY</p></td>
<td><p>Mandatory.</p></td>
</tr>
<tr class="even">
<td><p>LCMAP_BYTEREV</p></td>
<td><p>Optional.</p></td>
</tr>
<tr class="odd">
<td><p>NORM_IGNORECASE</p></td>
<td><p>Optional.</p></td>
</tr>
<tr class="even">
<td><p>NORM_IGNORENONSPACE</p></td>
<td><p>Optional.</p></td>
</tr>
<tr class="odd">
<td><p>NORM_IGNORESYMBOLS</p></td>
<td><p>Optional.</p></td>
</tr>
<tr class="even">
<td><p>NORM_IGNOREKANATYPE</p></td>
<td><p>Optional.</p></td>
</tr>
<tr class="odd">
<td><p>NORM_IGNOREWIDTH</p></td>
<td><p>Optional.</p></td>
</tr>
<tr class="even">
<td><p>SORT_STRINGSORT</p></td>
<td><p>Optional.</p></td>
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

[JET\_COLTYP](gg269213\(v=exchg.10\).md)  
[JET\_INDEXCREATE](gg269186\(v=exchg.10\).md)  
[JetOpenTempTable3](gg269255\(v=exchg.10\).md)

