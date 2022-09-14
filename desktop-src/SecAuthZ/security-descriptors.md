---
description: A security descriptor contains the security information associated with a securable object.
ms.assetid: '4ab0e7b1-1b44-4368-b2bd-106c9d2c652c'
title: Security Descriptors
ms.topic: article
ms.date: 05/31/2018
---

# Security Descriptors

A [*security descriptor*](/windows/desktop/SecGloss/s-gly) contains the security information associated with a [securable object](securable-objects.md). A security descriptor consists of a [**SECURITY\_DESCRIPTOR**](/windows/desktop/api/Winnt/ns-winnt-security_descriptor) structure and its associated security information. A security descriptor can include the following security information:

-   [Security identifiers](security-identifiers.md) (SIDs) for the owner and primary group of an object.
-   A [DACL](access-control-lists.md) that specifies the access rights allowed or denied to particular users or groups.
-   A [SACL](access-control-lists.md) that specifies the types of access attempts that generate audit records for the object.
-   A set of control bits that qualify the meaning of a security descriptor or its individual members.

Applications must not directly manipulate the contents of a security descriptor. The Windows API provides functions for setting and retrieving the security information in an object's security descriptor. In addition, there are functions for creating and initializing a security descriptor for a new object.

Applications working with security descriptors on Active Directory objects can use the Windows security functions or the security interfaces provided by the Active Directory Service Interfaces (ADSI). For more information about ADSI security interfaces, see [How Access Control Works in Active Directory](/windows/desktop/AD/how-access-control-works-in-active-directory-domain-services).

 

 
