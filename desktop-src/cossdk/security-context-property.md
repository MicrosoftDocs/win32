---
description: Security Context Property
ms.assetid: 7ffae145-be13-4a2c-beb1-eaa1d11ad9a7
title: Security Context Property
ms.topic: article
ms.date: 05/31/2018
---

# Security Context Property

As with every automatic service provided by COM+, automatic role checking is based on properties included on the object context. The determination of whether a security check must be carried out on a call into a component is based on the security property on the object context created when the configured component is instantiated.

You generally don't need to be concerned with this property; it is used directly by COM+, not you. However, in some circumstances, you might want strict control over the activation of an object. In this case, the security property can affect which context your object is activated in. That is, if an object has a configuration incompatible with the context of its creator, it will be activated in its own context. The security property can influence this, as can any property on the object context.

If you don't want security settings to influence activation, you can choose process-level access checking only. This suppresses the security property on the object context, although it effectively disables role-based checking and makes [security call context information](security-call-context-information.md) unavailable.

For more information about process-level access checks, see [Security Boundaries](security-boundaries.md). To see how to set process-level security, see [Setting a Security Level for Access Checks](setting-a-security-level-for-access-checks.md).

For more information about object context, see [Contexts](com--contexts.md).

## Related topics

<dl> <dt>

[Designing Roles Effectively](designing-roles-effectively.md)
</dt> <dt>

[Security Boundaries](security-boundaries.md)
</dt> <dt>

[Security Call Context Information](security-call-context-information.md)
</dt> <dt>

[Using Roles for Client Authorization](using-roles-for-client-authorization.md)
</dt> </dl>

 

 



