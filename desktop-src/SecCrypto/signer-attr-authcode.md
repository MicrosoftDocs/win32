---
Description: 'Specifies attributes for an Authenticode signature.'
ms.assetid: '1c1052c3-c5c5-48ae-8266-0b367800a84a'
title: 'SIGNER\_ATTR\_AUTHCODE structure'
---

# SIGNER\_ATTR\_AUTHCODE structure

The **SIGNER\_ATTR\_AUTHCODE** structure specifies attributes for an [*Authenticode*](security.a_gly#-security-authenticode-gly) signature.

> [!Note]  
> This structure is not defined in any header file. To use this structure, you must define it yourself as shown in this topic.

 

## Syntax


```C++
typedef struct _SIGNER_ATTR_AUTHCODE {
  DWORD   cbSize;
  BOOL    fCommercial;
  BOOL    fIndividual;
  LPCWSTR pwszName;
  LPCWSTR pwszInfo;
} SIGNER_ATTR_AUTHCODE, *PSIGNER_ATTR_AUTHCODE;
```



## Members

<dl> <dt>

**cbSize**
</dt> <dd>

The size, in bytes, of the structure.

</dd> <dt>

**fCommercial**
</dt> <dd>

**TRUE** to sign the subject as a commercial publisher; otherwise, **FALSE**.

</dd> <dt>

**fIndividual**
</dt> <dd>

**TRUE** to sign the subject as an individual publisher; otherwise, **FALSE**.

</dd> <dt>

**pwszName**
</dt> <dd>

The display name of the file upon download.

</dd> <dt>

**pwszInfo**
</dt> <dd>

The display name of the URL of the file upon download.

</dd> </dl>

## Requirements



|                                     |                                                      |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>          |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[**SIGNER\_SIGNATURE\_INFO**](signer-signature-info.md)
</dt> </dl>

 

 




