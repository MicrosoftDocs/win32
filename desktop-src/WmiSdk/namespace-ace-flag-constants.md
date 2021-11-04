---
description: The following list lists the possible values of the Flags field in a WMI Access Control Entry (ACE).
ms.assetid: bd09691d-e285-40e0-8686-edd5a132a06e
ms.tgt_platform: multiple
title: Namespace ACE Flag Constants (Winnt.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- OBJECT_INHERIT_ACE
- CONTAINER_INHERIT_ACE
- NO_PROPAGATE_INHERIT_ACE
- INHERIT_ONLY_ACE
- INHERITED_ACE
api_type: 
- HeaderDef
api_location: 
- Winnt.h
---

# Namespace ACE Flag Constants

The following list lists the possible values of the **Flags** field in a WMI Access Control Entry (ACE).

<dl> <dt>

<span id="OBJECT_INHERIT_ACE"></span><span id="object_inherit_ace"></span>**OBJECT\_INHERIT\_ACE**
</dt> <dd> <dl> <dt>

1 (0x1)
</dt> <dt>



Non-container child objects inherit the ACE as an effective ACE.


</dt> </dl> </dd> <dt>

<span id="CONTAINER_INHERIT_ACE"></span><span id="container_inherit_ace"></span>**CONTAINER\_INHERIT\_ACE**
</dt> <dd> <dl> <dt>

2 (0x2)
</dt> <dt>



The ACE has an effect on child namespaces as well as the current namespace.


</dt> </dl> </dd> <dt>

<span id="NO_PROPAGATE_INHERIT_ACE"></span><span id="no_propagate_inherit_ace"></span>**NO\_PROPAGATE\_INHERIT\_ACE**
</dt> <dd> <dl> <dt>

4 (0x4)
</dt> <dt>



The ACE applies only to the current namespace and immediate children .


</dt> </dl> </dd> <dt>

<span id="INHERIT_ONLY_ACE"></span><span id="inherit_only_ace"></span>**INHERIT\_ONLY\_ACE**
</dt> <dd> <dl> <dt>

8 (0x8)
</dt> <dt>



The ACE applies only to child namespaces.


</dt> </dl> </dd> <dt>

<span id="INHERITED_ACE"></span><span id="inherited_ace"></span>**INHERITED\_ACE**
</dt> <dd> <dl> <dt>

16 (0x10)
</dt> <dt>



This is not set by clients, but is reported to clients when the source of an ACE is a parent namespace.


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

 

 




