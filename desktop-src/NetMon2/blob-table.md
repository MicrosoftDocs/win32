---
description: Contains an array of BLOBs.
ms.assetid: e87f493b-f160-4316-b369-75d20c735213
title: BLOB_TABLE structure (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- BLOB_TABLE
api_type: 
- HeaderDef
api_location: 
- Netmon.h
---

# BLOB\_TABLE structure

The **BLOB\_TABLE** structure contains an array of BLOBs.

## Syntax


```C++
typedef struct {
  DWORD dwNumBlobs;
  HBLOB hBlobs[];
} BLOB_TABLE, *PBLOB_TABLE;
```



## Members

<dl> <dt>

**dwNumBlobs**
</dt> <dd>

Indicator that many BLOBs follow.

</dd> <dt>

**hBlobs**
</dt> <dd>

Handle to the BLOB array.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                          |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Netmon.h</dt> </dl> |



 

 




