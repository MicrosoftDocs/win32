---
description: You can control whether a child namespace inherits the security descriptor of the parent namespace.
ms.assetid: d4fbd5af-69e2-4c60-907a-cb2a1506b7c9
ms.tgt_platform: multiple
title: Establishing Inheritance of Namespace Security
ms.topic: article
ms.date: 05/31/2018
---

# Establishing Inheritance of Namespace Security

You can control whether a child namespace inherits the security descriptor of the parent namespace.

WMI namespaces have security descriptors that control who can access the namespace and the data of the namespace. Each security descriptor has a discretionary access control list (DACL) and a security access control list (SACL). These lists contain access control entries (ACE).

Depending on the [**Namespace ACE Flag Constants**](namespace-ace-flag-constants.md) that are set, permissions that are applied to a namespace may be inherited by all the child namespaces of that namespace. A child namespace inherits the security descriptor of its parent namespace when the child namespace is created if the **CONTAINER\_INHERIT\_ACE** flag is in the parent namespace security descriptor. If **CONTAINER\_INHERIT\_ACE\|NO\_PROPOGATE\_INHERIT\_ACE** is set, then only the child namespace inherits the security descriptor, not grandchild namespaces. Child namespaces can override the security permissions of their parent by calling methods of the [**\_\_SystemSecurity**](--systemsecurity.md) class to write a new security descriptor. The default security settings cannot be changed. For more information, see [Setting Namepace Security Descriptors](setting-namespace-security-descriptors.md).For more information about DACLs, see [Access Control Lists (ACL)](/windows/desktop/SecAuthZ/access-control-lists) and [**Namespace ACE Type Constants**](namespace-ace-type-constants.md).

Note that the default permissions cannot be changed. Furthermore, setting the **SE\_DACL\_PROTECTED** flag while setting the security descriptor (SD) is not used to add a specialized SD to a child namespace. To override an inherited SD, simply set a new one. To inherit that SD to a child namespace, pass the **CONTAINER\_INHERIT\_ACE** flag in the namespace security descriptor. To inherit to just the child, and not the descendants, pass `CONTAINER_INHERIT_ACE|NO_PROPOGATE_INHERIT_ACE`

.

## Related topics

<dl> <dt>

[Setting Namepace Security Descriptors](setting-namespace-security-descriptors.md)
</dt> <dt>

[**\_\_SystemSecurity**](--systemsecurity.md)
</dt> </dl>

 

 
