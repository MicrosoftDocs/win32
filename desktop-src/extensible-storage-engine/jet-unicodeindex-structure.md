---
description: "Learn more about: JET_UNICODEINDEX Structure"
title: JET_UNICODEINDEX Structure
TOCTitle: JET_UNICODEINDEX Structure
ms:assetid: d0b8ef74-850e-4e21-9f71-b56ec472aa0f
ms:mtpsurl: https://msdn.microsoft.com/library/Gg294097(v=EXCHG.10)
ms:contentKeyID: 32765712
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

# JET_UNICODEINDEX Structure


_**Applies to:** Windows | Windows Server_

## JET_UNICODEINDEX Structure

The **JET_UNICODEINDEX** structure customizes how Unicode data gets normalized when an index is created over a Unicode column.

```cpp
typedef struct tagJET_UNICODEINDEX {
  unsigned long lcid;
  unsigned long dwMapFlags;
} JET_UNICODEINDEX;
```

### Members

**lcid**

The Locale ID to use when normalizing the data. Any locale may be used as long as the appropriate language pack has been installed on the machine. The one exception is that the Language Neutral locale (LCID of zero) is illegal.

**dwMapFlags**

These flags get passed to [LCMapString](/windows/win32/api/winnls/nf-winnls-lcmapstringa) when Unicode data gets normalized to a key, which enables user-defined flags to override the default.

**Windows 2000**:  The only two legal values for **dwFlags** are:

  - ( LCMAP_SORTKEY | NORM_IGNORECASE | NORM_IGNOREKANATYPE | NORM_IGNOREWIDTH | NORM_IGNORENONSPACE )

<!-- end list -->

  - ( LCMAP_SORTKEY | NORM_IGNORECASE | NORM_IGNOREKANATYPE | NORM_IGNOREWIDTH )

**dwMapFlags** has the following restrictions.


| <p>Value</p> | <p>Meaning</p> | 
|--------------|----------------|
| <p>LCMAP_SORTKEY</p> | <p>Mandatory.</p> | 
| <p>LCMAP_BYTEREV</p> | <p>Optional.</p> | 
| <p>NORM_IGNORECASE</p> | <p>Optional.</p> | 
| <p>NORM_IGNORENONSPACE</p> | <p>Optional.</p> | 
| <p>NORM_IGNORESYMBOLS</p> | <p>Optional.</p> | 
| <p>NORM_IGNOREKANATYPE</p> | <p>Optional.</p> | 
| <p>NORM_IGNOREWIDTH</p> | <p>Optional.</p> | 
| <p>SORT_STRINGSORT</p> | <p>Optional.</p> | 



### Requirements


| Requirement | Value |
|------------|----------|
| <p><strong>Client</strong></p> | <p>Requires Windows Vista, Windows XP, or Windows 2000 Professional.</p> | 
| <p><strong>Server</strong></p> | <p>Requires Windows Server 2008, Windows Server 2003, or Windows 2000 Server.</p> | 
| <p><strong>Header</strong></p> | <p>Declared in Esent.h.</p> | 



### See Also

[JET_COLTYP](./jet-coltyp.md)  
[JET_INDEXCREATE](./jet-indexcreate-structure.md)  
[JetOpenTempTable3](./jetopentemptable3-function.md)
