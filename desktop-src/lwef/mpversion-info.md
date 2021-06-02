---
title: MPVERSION_INFO structure (MpClient.h)
description: Version information for the malware protection manager's components.
ms.assetid: C18EE6FE-57E1-4814-85CA-19C3ACE275D2
keywords:
- MPVERSION_INFO structure Legacy Windows Environment Features
- PMPVERSION_INFO structure pointer Legacy Windows Environment Features
topic_type:
- apiref
api_name:
- MPVERSION_INFO
api_location:
- MpClient.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# MPVERSION\_INFO structure

Version information for the malware protection manager's components.

## Syntax


```C++
typedef struct tagMPVERSION_INFO {
  MPCOMPONENT_VERSION Product;
  MPCOMPONENT_VERSION Service;
  MPCOMPONENT_VERSION FileSystemFilter;
  MPCOMPONENT_VERSION Engine;
  MPCOMPONENT_VERSION ASSignature;
  MPCOMPONENT_VERSION AVSignature;
  MPCOMPONENT_VERSION NISEngine;
  MPCOMPONENT_VERSION NISSignature;
  MPCOMPONENT_VERSION Reserved[4];
} MPVERSION_INFO, *PMPVERSION_INFO;
```



## Members

<dl> <dt>

**Product**
</dt> <dd>

Type: **[**MPCOMPONENT\_VERSION**](mpcomponent-version.md)**

</dd> <dd>

Product version.

</dd> <dt>

**Service**
</dt> <dd>

Type: **[**MPCOMPONENT\_VERSION**](mpcomponent-version.md)**

</dd> <dd>

Service component version.

</dd> <dt>

**FileSystemFilter**
</dt> <dd>

Type: **[**MPCOMPONENT\_VERSION**](mpcomponent-version.md)**

</dd> <dd>

File system filter component version.

</dd> <dt>

**Engine**
</dt> <dd>

Type: **[**MPCOMPONENT\_VERSION**](mpcomponent-version.md)**

</dd> <dd>

Engine component version.

</dd> <dt>

**ASSignature**
</dt> <dd>

Type: **[**MPCOMPONENT\_VERSION**](mpcomponent-version.md)**

</dd> <dd>

Antispyware signature component version.

</dd> <dt>

**AVSignature**
</dt> <dd>

Type: **[**MPCOMPONENT\_VERSION**](mpcomponent-version.md)**

</dd> <dd>

Antivirus signature component version.

</dd> <dt>

**NISEngine**
</dt> <dd>

Type: **[**MPCOMPONENT\_VERSION**](mpcomponent-version.md)**

</dd> <dd>

NIS engine version.

</dd> <dt>

**NISSignature**
</dt> <dd>

Type: **[**MPCOMPONENT\_VERSION**](mpcomponent-version.md)**

</dd> <dd>

NIS Signature signature component version.

</dd> <dt>

**Reserved**
</dt> <dd>

Type: **[**MPCOMPONENT\_VERSION**](mpcomponent-version.md)\[4\]**

</dd> <dd>

Reserved fields.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                            |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>MpClient.h</dt> </dl> |



## See also

<dl> <dt>

[**MPCOMPONENT\_VERSION**](mpcomponent-version.md)
</dt> </dl>

 

 





