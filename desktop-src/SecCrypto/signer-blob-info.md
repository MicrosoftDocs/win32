---
description: Specifies a BLOB to sign.
ms.assetid: 214c9c05-5c95-4803-8993-23a87266f991
title: SIGNER_BLOB_INFO structure
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SIGNER_BLOB_INFO
api_type: 
- NA
api_location: 
---

# SIGNER\_BLOB\_INFO structure

\[The **SIGNER\_BLOB\_INFO** structure is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

The **SIGNER\_BLOB\_INFO** structure specifies a [*BLOB*](../secgloss/b-gly.md) to sign.

> [!Note]  
> This structure is not defined in any header file. To use this structure, you must define it yourself as shown in this topic.

 

## Syntax


```C++
typedef struct _SIGNER_BLOB_INFO {
  DWORD   cbSize;
  GUID    *pGuidSubject;
  DWORD   cbBlob;
  BYTE    *pbBlob;
  LPCWSTR pwszDisplayName;
} SIGNER_BLOB_INFO, *PSIGNER_BLOB_INFO;
```



## Members

<dl> <dt>

**cbSize**
</dt> <dd>

The size, in bytes, of the structure.

</dd> <dt>

**pGuidSubject**
</dt> <dd>

A pointer to a **GUID** that specifies the Subject Interface Package (SIP) to load.

</dd> <dt>

**cbBlob**
</dt> <dd>

The size, in bytes, of the BLOB to sign.

</dd> <dt>

**pbBlob**
</dt> <dd>

A pointer to the BLOB to sign.

</dd> <dt>

**pwszDisplayName**
</dt> <dd>

The display name of the BLOB. This member can be set to **NULL**.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>          |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[**SIGNER\_SUBJECT\_INFO**](signer-subject-info.md)
</dt> </dl>

 

 
