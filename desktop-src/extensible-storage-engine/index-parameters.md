---
description: "Learn more about: Index Parameters"
title: Index Parameters
TOCTitle: Index Parameters
ms:assetid: df3dfbc7-71fb-4ae2-a94a-b00eaa1572ec
ms:mtpsurl: https://msdn.microsoft.com/library/Gg294119(v=EXCHG.10)
ms:contentKeyID: 32765733
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

# Index Parameters


_**Applies to:** Windows | Windows Server_

## Index Parameters

This topic contains parameters that are used for the index.

*JET_paramIndexTupleIncrement*  
132  

This parameter specifies the default for the offset increment used to step through the source column value while generating each tuple. For more information, see the [JET_TUPLELIMITS](./jet-tuplelimits-structure.md) structure.


| 
|
| <p>Default Value:</p> | <p>1</p> | 
| <p>Type:</p> | <p>Integer</p> | 
| <p>Valid Range:</p> | <p>0 - 32767</p> | 
| <p>Scope:</p> | <p>Instance</p> | 
| <p>Set After <a href="gg269354(v=exchg.10).md">JetCreateInstance</a>:</p> | <p>Yes</p> | 
| <p>Set after <a href="gg294068(v=exchg.10).md">JetInit</a>:</p> | <p>No</p> | 
| <p>Affects Physical Layout:</p> | <p>No</p> | 
| <p>Affects Reliability:</p> | <p>No</p> | 
| <p>Affects Performance:</p> | <p>No</p> | 
| <p>Affects Resources:</p> | <p>No</p> | 
| <p>Availability:</p> | <p>Windows Vista and later releases</p> | 



*JET_paramIndexTupleStart*  
133  

This parameter specifies the default for the offset in the source column value at which tuple generation will start. For more information, see the [JET_TUPLELIMITS](./jet-tuplelimits-structure.md) structure.


| 
|
| <p>Default Value:</p> | <p>0</p> | 
| <p>Type:</p> | <p>Integer</p> | 
| <p>Valid Range:</p> | <p>0 - 32767</p> | 
| <p>Scope:</p> | <p>Instance</p> | 
| <p>Set After <a href="gg269354(v=exchg.10).md">JetCreateInstance</a>:</p> | <p>Yes</p> | 
| <p>Set after <a href="gg294068(v=exchg.10).md">JetInit</a>:</p> | <p>No</p> | 
| <p>Affects Physical Layout:</p> | <p>No</p> | 
| <p>Affects Reliability:</p> | <p>No</p> | 
| <p>Affects Performance:</p> | <p>No</p> | 
| <p>Affects Resources:</p> | <p>No</p> | 
| <p>Availability:</p> | <p>Windows Vista and later releases</p> | 



*JET_paramIndexTuplesLengthMax*  
111  

This parameter specifies the default for the maximum tuple length in a tuple index. For more information, see the [JET_TUPLELIMITS](./jet-tuplelimits-structure.md) structure.

**Windows Vista:**  Prior to Windows Vista, setting this parameter to zero would set it back to its default value. For Windows Vista, this is no longer supported.


| 
|
| <p>Default Value:</p> | <p>10</p> | 
| <p>Type:</p> | <p>Integer</p> | 
| <p>Valid Range:</p> | <p><strong>Windows 2000, Windows XP and Windows Server 2003: </strong>  0, 2-255</p><p><strong>Windows Vista:</strong>  2-255</p> | 
| <p>Scope:</p> | <p>Instance</p> | 
| <p>Set After <a href="gg269354(v=exchg.10).md">JetCreateInstance</a>:</p> | <p>Yes</p> | 
| <p>Set after <a href="gg294068(v=exchg.10).md">JetInit</a>:</p> | <p>No</p> | 
| <p>Affects Physical Layout:</p> | <p>No</p> | 
| <p>Affects Reliability:</p> | <p>No</p> | 
| <p>Affects Performance:</p> | <p>No</p> | 
| <p>Affects Resources:</p> | <p>No</p> | 
| <p>Availability:</p> | <p>Windows XP and later releases</p> | 



*JET_paramIndexTuplesLengthMin*  
110  

This parameter specifies the default for the minimum tuple length in a tuple index. See [JET_TUPLELIMITS](./jet-tuplelimits-structure.md) for more information.

**Windows Vista:**  Prior to Windows Vista, setting this parameter to zero would set it back to its default value. For Windows Vista, this is no longer supported.


| 
|
| <p>Default Value:</p> | <p>3</p> | 
| <p>Type:</p> | <p>Integer</p> | 
| <p>Valid Range:</p> | <p><strong>Windows 2000, Windows XP and Windows Server 2003: </strong>  0, 2-255</p><p><strong>Windows Vista:</strong>  2-255</p> | 
| <p>Scope:</p> | <p>Instance</p> | 
| <p>Set After <a href="gg269354(v=exchg.10).md">JetCreateInstance</a>:</p> | <p>Yes</p> | 
| <p>Set after <a href="gg294068(v=exchg.10).md">JetInit</a>:</p> | <p>No</p> | 
| <p>Affects Physical Layout:</p> | <p>No</p> | 
| <p>Affects Reliability:</p> | <p>No</p> | 
| <p>Affects Performance:</p> | <p>No</p> | 
| <p>Affects Resources:</p> | <p>No</p> | 
| <p>Availability:</p> | <p>Windows XP and later releases</p> | 



*JET_paramIndexTuplesToIndexMax*  
112  

This parameter specifies the default for the maximum length of a source string to break into tuples for a tuple index. See [JET_TUPLELIMITS](./jet-tuplelimits-structure.md) for more information.

**Windows Vista:**  Prior to Windows Vista, setting this parameter to zero would set it back to its default value. For Windows Vista, this is no longer supported.


| 
|
| <p>Default Value:</p> | <p>32767</p> | 
| <p>Type:</p> | <p>Integer</p> | 
| <p>Valid Range:</p> | <p><strong>Windows 2000, Windows XP and Windows Server 2003:</strong>  0 – 32767</p><p><strong>Windows Vista:</strong>  1 – 32767</p> | 
| <p>Scope:</p> | <p>Instance</p> | 
| <p>Set After <a href="gg269354(v=exchg.10).md">JetCreateInstance</a>:</p> | <p>Yes</p> | 
| <p>Set after <a href="gg294068(v=exchg.10).md">JetInit</a>:</p> | <p>No</p> | 
| <p>Affects Physical Layout:</p> | <p>No</p> | 
| <p>Affects Reliability:</p> | <p>No</p> | 
| <p>Affects Performance:</p> | <p>No</p> | 
| <p>Affects Resources:</p> | <p>No</p> | 
| <p>Availability:</p> | <p>Windows XP and later releases</p> | 



*JET_paramUnicodeIndexDefault*  
72  

This parameter controls the default Unicode parameters used by any index over a Unicode key column. The type of this parameter is [JET_UNICODEINDEX](./jet-unicodeindex-structure.md) and is actually passed using a buffer pointer stored in the integer parameter of [JetGetSystemParameter](./jetgetsystemparameter-function.md) and [JetSetSystemParameter](./jetsetsystemparameter-function.md). The size of the buffer must equal the size of [JET_UNICODEINDEX](./jet-unicodeindex-structure.md) and must be passed to [JetGetSystemParameter](./jetgetsystemparameter-function.md) using the string buffer size parameter. This is clearly inconsistent but that is the behavior of this parameter.

The default value of this parameter contains an LCID for the U.S. English locale and the following [LCMapStringW](/windows/win32/api/winnls/nf-winnls-lcmapstringa)flags: LCMAP_SORTKEY, NORM_IGNORECASE, NORM_IGNOREKANATYPE, and NORM_IGNOREWIDTH.

**Windows 2000:**  The SORTID in the LCID is ignored. A SORTID of SORT_DEFAULT is always used.

**Windows 2000:**  The [LCMapStringW](/windows/win32/api/winnls/nf-winnls-lcmapstringa) flags must contain the following flags: LCMAP_SORTKEY, NORM_IGNORECASE, NORM_IGNOREKANATYPE, and NORM_IGNOREWIDTH. In addition, the [LCMapStringW](/windows/win32/api/winnls/nf-winnls-lcmapstringa)flags may contain the following flags: NORM_IGNORENONSPACE.

**Note**  If your application wishes to store Unicode data, then it is strongly recommended that you do not rely on the default Unicode parameters for your indexes. The use of U.S. English is tantamount to using the invariant locale and the default [LCMapStringW](/windows/win32/api/winnls/nf-winnls-lcmapstringa)flags are known to seriously interfere with some languages. You should always specify your own settings for the Unicode parameters to JetCreateIndex2 using [JET_INDEXCREATE](./jet-indexcreate-structure.md).


| 
|
| <p>Default Value:</p> | <p>Special</p> | 
| <p>Type:</p> | <p>JET_UNICODEINDEX* (JET_UNICODEINDEX)</p> | 
| <p>Valid Range:</p> | <p>Special</p> | 
| <p>Scope:</p> | <p>Instance</p> | 
| <p>Set After <a href="gg269354(v=exchg.10).md">JetCreateInstance</a>:</p> | <p>Yes</p> | 
| <p>Set after <a href="gg294068(v=exchg.10).md">JetInit</a>:</p> | <p>No</p> | 
| <p>Affects Physical Layout:</p> | <p>No</p> | 
| <p>Affects Reliability:</p> | <p>No</p> | 
| <p>Affects Performance:</p> | <p>No</p> | 
| <p>Affects Resources:</p> | <p>No</p> | 
| <p>Availability:</p> | <p>All</p> | 



### Requirements


| Requirement | Value |
|------------|----------|
| <p><strong>Client</strong></p> | <p>Requires Windows Vista, Windows XP, or Windows 2000 Professional.</p> | 
| <p><strong>Server</strong></p> | <p>Requires Windows Server 2008, Windows Server 2003, or Windows 2000 Server.</p> | 
| <p><strong>Header</strong></p> | <p>Declared in Esent.h.</p> | 



### See Also

[JET_INDEXCREATE](./jet-indexcreate-structure.md)  
[JET_TUPLELIMITS](./jet-tuplelimits-structure.md)  
[JET_UNICODEINDEX](./jet-unicodeindex-structure.md)  
[JetCreateInstance](./jetcreateinstance-function.md)  
[JetGetSystemParameter](./jetgetsystemparameter-function.md)  
[JetInit](./jetinit-function.md)  
[JetSetSystemParameter](./jetsetsystemparameter-function.md)
