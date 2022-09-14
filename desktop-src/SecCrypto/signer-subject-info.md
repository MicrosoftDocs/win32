---
description: Specifies a subject to sign.
ms.assetid: ba569443-e50f-450b-82cc-b7328f0ca25a
title: SIGNER_SUBJECT_INFO structure
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SIGNER_SUBJECT_INFO
api_type: 
- NA
api_location: 
---

# SIGNER\_SUBJECT\_INFO structure

The **SIGNER\_SUBJECT\_INFO** structure specifies a subject to sign.

> [!Note]  
> This structure is not defined in any header file. To use this structure, you must define it yourself as shown in this topic.

 

## Syntax


```C++
typedef struct _SIGNER_SUBJECT_INFO {
  DWORD cbSize;
  DWORD *pdwIndex;
  DWORD dwSubjectChoice;
  union {
    SIGNER_FILE_INFO *pSignerFileInfo;
    SIGNER_BLOB_INFO *pSignerBlobInfo;
  };
} SIGNER_SUBJECT_INFO, *PSIGNER_SUBJECT_INFO;
```



## Members

<dl> <dt>

**cbSize**
</dt> <dd>

The size, in bytes, of the structure.

</dd> <dt>

**pdwIndex**
</dt> <dd>

This member is reserved. It must be set to zero.

</dd> <dt>

**dwSubjectChoice**
</dt> <dd>

Specifies whether the subject is a file or a [*BLOB*](../secgloss/b-gly.md). This member can be one or more of the following values.



| Value                                                                                                                                                                                                                                         | Meaning                           |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------|
| <span id="SIGNER_SUBJECT_BLOB"></span><span id="signer_subject_blob"></span><dl> <dt>**SIGNER\_SUBJECT\_BLOB**</dt> <dt>2 (0x2)</dt> </dl> | The subject is a BLOB.<br/> |
| <span id="SIGNER_SUBJECT_FILE"></span><span id="signer_subject_file"></span><dl> <dt>**SIGNER\_SUBJECT\_FILE**</dt> <dt>1 (0x1)</dt> </dl> | The subject is a file.<br/> |



 

</dd> <dt>

**pSignerFileInfo**
</dt> <dd>

A pointer to a [**SIGNER\_FILE\_INFO**](signer-file-info.md) structure that specifies the file to sign.

</dd> <dt>

**pSignerBlobInfo**
</dt> <dd>

A pointer to a [**SIGNER\_BLOB\_INFO**](signer-blob-info.md) structure that specifies the BLOB to sign.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>          |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[**SignerSign**](signersign.md)
</dt> <dt>

[**SignerSignEx**](signersignex.md)
</dt> </dl>

 

 
