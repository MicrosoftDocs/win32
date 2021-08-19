---
description: "Learn more about: JET_SPACEHINTS Structure"
title: JET_SPACEHINTS Structure
TOCTitle: JET_SPACEHINTS Structure
ms:assetid: 23328993-93c9-4a23-892b-e6a9f434d1d6
ms:mtpsurl: https://msdn.microsoft.com/library/Gg269205(v=EXCHG.10)
ms:contentKeyID: 32765508
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

# JET_SPACEHINTS Structure


_**Applies to:** Windows | Windows Server_

## JET_SPACEHINTS Structure

The **JET_SPACEHINTS** structure contains information about space allocation patterns when a b-tree grows through append or hotpoint splits. Append splits happen when records are added to the end of a b-tree and hotpoint splits happen when multiple records are added to the same virtual insertion point (for example, adding 'Marie', 'Mark', 'Martin', 'Mary' to the middle of a b-tree that is sorted alphabetically).

**Windows 7:** The **JET_SPACEHINTS** structure is introduced in Windows 7.

```cpp
    typedef struct tagJET_SPACEHINTS {
      unsigned long cbStruct;
      unsigned long ulInitialDensity;
      unsigned long cbInitial;
      JET_GRBIT grbit;
      unsigned long ulMaintDensity;
      unsigned long ulGrowth;
      unsigned long cbMinExtent;
      unsigned long cbMaxExtent;
    } JET_SPACEHINTS;
```

### Members

**cbStruct**

The size, in bytes, of this structure. Set this member to sizeof( JET_SPACEHINTS ).

**ulInitialDensity**

The density at (append) layout.

**cbInitial**

The initial size (in bytes) of the object being created. This must be a multiple of the database page size.

**grbit**

A group of bits that contain the options to be used for this structure, which include zero or more of the following.


| <p>Value</p> | <p>Meaning</p> | 
|--------------|----------------|
| <p>JET_bitSpaceHintsUtilizeParentSpace<br />0x00000001</p> | <p>Changes the internal allocation policy to get space heirarchically from the immediate parent of a b-tree.</p> | 
| <p>JET_bitCreateHintAppendSequential<br />0x00000002</p> | <p>Enables append split behavior to grow according to the growth dynamics of the table (set by cbMinExtent, ulGrowth, cbMaxExtent).</p> | 
| <p>JET_bitCreateHintHotpointSequential<br />0x00000004</p> | <p>Enables hotpoint split behavior to grow according to the growth dynamics of the table (set by cbMinExtent, ulGrowth, cbMaxExtent).</p> | 
| <p>JET_bitRetrieveHintTableScanForward<br />0x00000010</p> | <p>If set, the client indicates that forward sequential scan is the predominant usage pattern of this table.</p> | 
| <p>JET_bitRetrieveHintTableScanBackward<br />0x00000020</p> | <p>If set, the client indicates that backward sequential scan is the predominant usage pattern of this table.</p> | 
| <p>JET_bitDeleteHintTableSequential<br />0x00000100</p> | <p>If set, the application expects this table to be cleaned up in sequential order, from lowest key to highest key.</p> | 



**ulMaintDensity**

density to mulMaintDensity

Density to maintain at. If the space hints specify JET_bitRetrieveHintTableScanForward or JET_bitRetrieveHintTableScanBackward, table defragmentation will be triggered when the used space in the table drops below this threshold. Table defragmentation can be disabled by setting this member to zero. Setting this member to 100 will cause table defragmentation to run as soon as a page is freed.

**ulGrowth**

The percent growth from the last growth or initial size, rounded to nearest native JET allocation size.

**cbMinExtent too small**

This overrides ulGrowth if too small.

**cbMaxExtent**

The maximum value for growth in bytes. This caps ulGrowth.

### When a b-tree grows through append or hotpoint splits (as opposed to random record insertions), the amount of space the table will grow by is calculated as follows:

1.  At creation, we give the b-tree cbInitial, always.

2.  During the first allocation of a given area, we will allocate: cbInitial \* ulGrowth / 100 (rounded to the DB's page size), or cbMinExtent if larger.

3.  During the next allocation, cbLastAlloc \* ulGrowth / 100 (rounded to the page size of the DB), or cbMinExtent if larger.

4.  At some allocation (which could be the first allocation), the calculated size will exceed cbMaxExtent, and that will be the growth size thereafter.

### Requirements


| 
|
| <p><strong>Client</strong></p> | <p>Requires Windows Vista, Windows XP, or Windows 2000 Professional.</p> | 
| <p><strong>Server</strong></p> | <p>Requires Windows Server 2008, Windows Server 2003, or Windows 2000 Server.</p> | 
| <p><strong>Header</strong></p> | <p>Declared in Esent.h.</p> | 



### See Also

[JET_TABLECREATE2](./jet-tablecreate2-structure.md)  
[JET_TABLECREATE3](./jet-tablecreate3-structure.md)
