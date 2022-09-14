---
title: MP_HASH_TYPE enumeration (MpClient.h)
description: Possible hash types.
ms.assetid: 46432C40-6DE1-4FB8-B7C1-C2712CCEB208
keywords:
- MP_HASH_TYPE enumeration Legacy Windows Environment Features
- PMP_HASH_TYPE enumeration pointer Legacy Windows Environment Features
topic_type:
- apiref
api_name:
- MP_HASH_TYPE
api_location:
- MpClient.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# MP\_HASH\_TYPE enumeration

Possible hash types.

## Syntax


```C++
typedef enum tagMP_HASH_TYPE { 
  MP_HASH_TYPE_NONE    = 0,
  MP_HASH_TYPE_CRC32   = 2,
  MP_HASH_TYPE_MD5     = 4,
  MP_HASH_TYPE_SHA1    = 8,
  MP_HASH_TYPE_SHA256  = 16
} MP_HASH_TYPE, *PMP_HASH_TYPE;
```



## Constants

<dl> <dt>

<span id="MP_HASH_TYPE_NONE"></span><span id="mp_hash_type_none"></span>**MP\_HASH\_TYPE\_NONE**
</dt> <dd>

No hash.

</dd> <dt>

<span id="MP_HASH_TYPE_CRC32"></span><span id="mp_hash_type_crc32"></span>**MP\_HASH\_TYPE\_CRC32**
</dt> <dd>

CRC32

</dd> <dt>

<span id="MP_HASH_TYPE_MD5"></span><span id="mp_hash_type_md5"></span>**MP\_HASH\_TYPE\_MD5**
</dt> <dd>

MD5

</dd> <dt>

<span id="MP_HASH_TYPE_SHA1"></span><span id="mp_hash_type_sha1"></span>**MP\_HASH\_TYPE\_SHA1**
</dt> <dd>

SHA1

</dd> <dt>

<span id="MP_HASH_TYPE_SHA256"></span><span id="mp_hash_type_sha256"></span>**MP\_HASH\_TYPE\_SHA256**
</dt> <dd>

SHA 256

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                            |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>MpClient.h</dt> </dl> |



 

 





