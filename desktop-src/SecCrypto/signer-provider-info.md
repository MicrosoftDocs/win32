---
description: Specifies the cryptographic service provider (CSP) and private key information used to create a digital signature.
ms.assetid: 85dc6a06-365a-4591-9d1d-117556a4417d
title: SIGNER_PROVIDER_INFO structure
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SIGNER_PROVIDER_INFO
api_type: 
- NA
api_location: 
---

# SIGNER\_PROVIDER\_INFO structure

The **SIGNER\_PROVIDER\_INFO** structure specifies the [*cryptographic service provider*](../secgloss/c-gly.md) (CSP) and private key information used to create a digital signature.

> [!Note]  
> This structure is not defined in any header file. To use this structure, you must define it yourself as shown in this topic.

 

## Syntax


```C++
typedef struct _SIGNER_PROVIDER_INFO {
  DWORD   cbSize;
  LPCWSTR pwszProviderName;
  DWORD   dwProviderType;
  DWORD   dwKeySpec;
  DWORD   dwPvkChoice;
  union {
    LPWSTR pwszPvkFileName;
    LPWSTR pwszKeyContainer;
  };
} SIGNER_PROVIDER_INFO, *PSIGNER_PROVIDER_INFO;
```



## Members

<dl> <dt>

**cbSize**
</dt> <dd>

The size, in bytes, of the structure.

</dd> <dt>

**pwszProviderName**
</dt> <dd>

The name of the CSP used to create the digital signature. If the value of this member is **NULL**, the default provider is used.

</dd> <dt>

**dwProviderType**
</dt> <dd>

The type of the CSP specified by the **pwszProviderName** member.

</dd> <dt>

**dwKeySpec**
</dt> <dd>

The key specification. If this member is set to zero, the key specification in the **pwszPvkFileName** or **pwszKeyContainer** member is used. If there is more than one key specification in the **pwszKeyContainer** member, **AT\_SIGNATURE** is used. If it fails, **AT\_KEYEXCHANGE** is used.

</dd> <dt>

**dwPvkChoice**
</dt> <dd>

Specifies the type of private key information. This member can be one or more of the following values.



| Value                                                                                                                                                                                                                                               | Meaning                                                    |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------|
| <span id="PVK_TYPE_FILE_NAME"></span><span id="pvk_type_file_name"></span><dl> <dt>**PVK\_TYPE\_FILE\_NAME**</dt> <dt>1 (0x1)</dt> </dl>         | The private key information is a file name.<br/>     |
| <span id="PVK_TYPE_KEYCONTAINER"></span><span id="pvk_type_keycontainer"></span><dl> <dt>**PVK\_TYPE\_KEYCONTAINER**</dt> <dt>2 (0x2)</dt> </dl> | The private key information is a key container.<br/> |



 

</dd> <dt>

**pwszPvkFileName**
</dt> <dd>

The name of the file that contains the private key information.

</dd> <dt>

**pwszKeyContainer**
</dt> <dd>

The name of the key container that contains the private key information.

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

 

 
