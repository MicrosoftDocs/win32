---
title: SEEKROWSETTYPE enumeration
description: Do not use. Used as a parameter to IDatabase SeekRowset to specify the starting location of the seek.
ms.assetid: 'cddd8f37-261e-4c54-9df0-d194cb7593b2'
keywords: ["SEEKROWSETTYPE enumeration Windows Mail (formerly Outlook Express)", "ACCESSTYPE enumeration Windows Mail (formerly Outlook Express)"]
topic_type:
- apiref
api_name:
- ACCESSTYPE
api_location:
- Directdb.idl
api_type:
- IDLDef
---

# SEEKROWSETTYPE enumeration

Do not use. Used as a parameter to IDatabase::SeekRowset to specify the starting location of the seek.

## Syntax


```C++
typedef enum  { 
  SEEK_ROWSET_BEGIN,
  SEEK_ROWSET_CURRENT,
  SEEK_ROWSET_END
} ACCESSTYPE;
```



## Constants

<dl> <dt>

<span id="SEEK_ROWSET_BEGIN"></span><span id="seek_rowset_begin"></span>**SEEK\_ROWSET\_BEGIN**
</dt> <dd>

The cursor is repositioned relative to the beginning of the Database.

</dd> <dt>

<span id="SEEK_ROWSET_CURRENT"></span><span id="seek_rowset_current"></span>**SEEK\_ROWSET\_CURRENT**
</dt> <dd>

The cursor is repositioned relative to its current location.

</dd> <dt>

<span id="SEEK_ROWSET_END"></span><span id="seek_rowset_end"></span>**SEEK\_ROWSET\_END**
</dt> <dd>

The cursor is repositioned relative to the end of the database.

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Product<br/>                  | Outlook Express 6.0<br/>                                                          |
| IDL<br/>                      | <dl> <dt>Directdb.idl</dt> </dl> |



 

 





