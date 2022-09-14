---
description: Specifies a file to sign.
ms.assetid: 5b45d855-ede8-43eb-9253-e3fe1716686b
title: SIGNER_FILE_INFO structure
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SIGNER_FILE_INFO
api_type: 
- NA
api_location: 
---

# SIGNER\_FILE\_INFO structure

The **SIGNER\_FILE\_INFO** structure specifies a file to sign.

> [!Note]  
> This structure is not defined in any header file. To use this structure, you must define it yourself as shown in this topic.

 

## Syntax


```C++
typedef struct _SIGNER_FILE_INFO {
  DWORD   cbSize;
  LPCWSTR pwszFileName;
  HANDLE  hFile;
} SIGNER_FILE_INFO, *PSIGNER_FILE_INFO;
```



## Members

<dl> <dt>

**cbSize**
</dt> <dd>

The size, in bytes, of the structure.

</dd> <dt>

**pwszFileName**
</dt> <dd>

A pointer to a null-terminated string that contains the name of the file to sign.

</dd> <dt>

**hFile**
</dt> <dd>

An open handle to the file specified by the **pwszFileName** member. If this member contains a valid handle, this handle is used to access the file. This member can be set to **NULL**.

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

 

 




