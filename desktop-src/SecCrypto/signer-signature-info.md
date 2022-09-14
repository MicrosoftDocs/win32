---
description: Contains information about a digital signature.
ms.assetid: 0b86fdf9-533f-4640-8c70-c3c8f4ef2c68
title: SIGNER_SIGNATURE_INFO structure
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SIGNER_SIGNATURE_INFO
api_type: 
- NA
api_location: 
---

# SIGNER\_SIGNATURE\_INFO structure

The **SIGNER\_SIGNATURE\_INFO** structure contains information about a digital signature.

> [!Note]  
> This structure is not defined in any header file. To use this structure, you must define it yourself as shown in this topic.

 

## Syntax


```C++
typedef struct _SIGNER_SIGNATURE_INFO {
  DWORD             cbSize;
  ALG_ID            algidHash;
  DWORD             dwAttrChoice;
  union {
    SIGNER_ATTR_AUTHCODE *pAttrAuthcode;
  };
  PCRYPT_ATTRIBUTES psAuthenticated;
  PCRYPT_ATTRIBUTES psUnauthenticated;
} SIGNER_SIGNATURE_INFO, *PSIGNER_SIGNATURE_INFO;
```



## Members

<dl> <dt>

**cbSize**
</dt> <dd>

The size, in bytes, of the structure.

</dd> <dt>

**algidHash**
</dt> <dd>

The hash algorithm used for the digital signature.

</dd> <dt>

**dwAttrChoice**
</dt> <dd>

Specifies whether the signature has [*Authenticode*](../secgloss/a-gly.md) attributes. This member can be one or more of the following values.



| Value                                                                                                                                                                                                                                      | Meaning                                                                                                                                   |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="SIGNER_AUTHCODE_ATTR"></span><span id="signer_authcode_attr"></span><dl> <dt>**SIGNER\_AUTHCODE\_ATTR**</dt> <dt>1</dt> </dl> | The signature has [*Authenticode*](../secgloss/a-gly.md) attributes.<br/>           |
| <span id="SIGNER_NO_ATTR"></span><span id="signer_no_attr"></span><dl> <dt>**SIGNER\_NO\_ATTR**</dt> <dt>0</dt> </dl>                   | The signature does not have [*Authenticode*](../secgloss/a-gly.md) attributes.<br/> |



 

</dd> <dt>

**pAttrAuthcode**
</dt> <dd>

Specifies attributes for an [*Authenticode*](../secgloss/a-gly.md) signature. This member is required if the value of the **dwAttrChoice** member is **SIGNER\_AUTHCODE\_ATTR**.

</dd> <dt>

**psAuthenticated**
</dt> <dd>

Authenticated user-supplied attributes added to the digital signature.

</dd> <dt>

**psUnauthenticated**
</dt> <dd>

Unauthenticated user-supplied attributes added to the digital signature.

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

 

 
