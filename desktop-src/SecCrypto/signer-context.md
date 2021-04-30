---
description: Contains a signed BLOB.
ms.assetid: c12d9007-c779-4363-8e28-6387a665a0d6
title: SIGNER_CONTEXT structure
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SIGNER_CONTEXT
api_type: 
- NA
api_location: 
---

# SIGNER\_CONTEXT structure

The **SIGNER\_CONTEXT** structure contains a signed [*BLOB*](../secgloss/b-gly.md).

> [!Note]  
> This structure is not defined in any header file. To use this structure, you must define it yourself as shown in this topic.

 

## Syntax


```C++
typedef struct _SIGNER_CONTEXT {
  DWORD cbSize;
  DWORD cbBlob;
  BYTE  *pbBlob;
} SIGNER_CONTEXT, *PSIGNER_CONTEXT;
```



## Members

<dl> <dt>

**cbSize**
</dt> <dd>

The size, in bytes, of the structure.

</dd> <dt>

**cbBlob**
</dt> <dd>

The size, in bytes, of the **pbBlob** member.

</dd> <dt>

**pbBlob**
</dt> <dd>

A pointer to the signed BLOB.

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

 

 
