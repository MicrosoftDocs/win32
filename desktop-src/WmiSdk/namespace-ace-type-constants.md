---
description: The Type field in an access control entry (ACE) that determines whether the ACE is an ACE that allows access or denies access.
ms.assetid: a78c72f7-0bc0-4bda-9012-4abe45342d8d
ms.tgt_platform: multiple
title: Namespace ACE Type Constants (Winnt.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Allow
- Deny
api_type: 
- HeaderDef
api_location: 
- Winnt.h
---

# Namespace ACE Type Constants

The **Type** field in an access control entry (ACE) that determines whether the ACE is an ACE that allows access or denies access.

<dl> <dt>

<span id="Allow"></span><span id="allow"></span><span id="ALLOW"></span>**Allow**
</dt> <dd> <dl> <dt>

0
</dt> <dt>



The ACE allows access to the namespace.


</dt> </dl> </dd> <dt>

<span id="Deny"></span><span id="deny"></span><span id="DENY"></span>**Deny**
</dt> <dd> <dl> <dt>

1
</dt> <dt>



The ACE denies access to the namespace.


</dt> </dl> </dd> </dl>

## Requirements



| Requirement | Value |
|-------------------|------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Winnt.h</dt> </dl> |



## See also

<dl> <dt>

[WMI Security Constants](wmi-security-constants.md)
</dt> <dt>

[Setting Namepace Security Descriptors](setting-namespace-security-descriptors.md)
</dt> <dt>

[Establishing Inheritance of Namespace Security](establishing-inheritance-of-namespace-security.md)
</dt> <dt>

[**\_\_SystemSecurity**](--systemsecurity.md)
</dt> </dl>

 

 




