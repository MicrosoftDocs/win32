---
title: SMIME\_SECURITY\_LABEL structure
description: SMIME\_SECURITY\_LABEL structure
ms.assetid: 6d21255f-ff5b-4e92-9686-01bf1d3c1571
keywords:
- SMIME_SECURITY_LABEL structure Windows Mail (formerly Outlook Express)
- PSMIME_SECURITY_LABEL structure pointer Windows Mail (formerly Outlook Express)
topic_type:
- apiref
api_name:
- SMIME_SECURITY_LABEL
api_location:
- Imnact.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# SMIME\_SECURITY\_LABEL structure

\[The **SMIME\_SECURITY\_LABEL** structure is available for use in Windows XP. It might be altered or unavailable in subsequent versions.\]

## Syntax


```C++
typedef struct _SMIME_SECURITY_LABEL {
  LPSTR                      pszObjIdSecurityPolicy;
  DWORD                      fHasClassification;
  DWORD                      dwClassification;
  LPWSTR                     wszPrivacyMark;
  DWORD                      cCategories;
  CRYPT_ATTRIBUTE_TYPE_VALUE *rgCategories;
} SMIME_SECURITY_LABEL, *PSMIME_SECURITY_LABEL;
```



## Members

<dl> <dt>

**pszObjIdSecurityPolicy**
</dt> <dd>

Type: **LPSTR**

</dd> <dd></dd> <dt>

**fHasClassification**
</dt> <dd>

Type: **DWORD**

</dd> <dd>

TRUE if dwClassification is set

</dd> <dt>

**dwClassification**
</dt> <dd>

Type: **DWORD**

</dd> <dd></dd> <dt>

**wszPrivacyMark**
</dt> <dd>

Type: **LPWSTR**

</dd> <dd>

Optional

</dd> <dt>

**cCategories**
</dt> <dd>

Type: **DWORD**

</dd> <dd></dd> <dt>

**rgCategories**
</dt> <dd>

Type: **[CRYPT\_ATTRIBUTE\_TYPE\_VALUE](http://msdn.microsoft.com/library/seccrypto/security/crypt_attribute_type_value.asp)\***

</dd> <dd></dd> </dl>

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Product<br/>                  | Outlook Express 6.0<br/>                                                        |
| Header<br/>                   | <dl> <dt>Imnact.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Imnact.idl</dt> </dl> |



 

 





