---
title: Application Directory Partition Security
description: The security and access control model for application directory partitions is the same as that for other partitions in Active Directory Domain Services.
ms.assetid: 3e14b31a-524e-4b38-957f-166e80b35b31
ms.tgt_platform: multiple
keywords:
- Application Directory Partition Security AD
- Application directory partitions AD , Security
ms.topic: article
ms.date: 05/31/2018
---

# Application Directory Partition Security

The security and access control model for application directory partitions is the same as that for other partitions in Active Directory Domain Services. Normal users can access objects in an application directory partition subject to the ACLs placed on those objects. For more information, see [Controlling Access to Objects in Active Directory Domain Services](controlling-access-to-objects-in-active-directory-domain-services.md).

However, because application directory partitions can span multiple security domains in a directory service, there arises the question of how to interpret domain-relative well-known SID string constants in the [**defaultSecurityDescriptor**](/windows/desktop/ADSchema/a-defaultsecuritydescriptor) of an object's schema class at the time of object creation in an application directory partition. For example, if "DA" refers to the domain administrators group, but in an application directory partition, it is not known which domain the "DA" group refers to.

To solve this problem, the [**crossRef**](/windows/desktop/ADSchema/c-crossref) object of an application directory partition has an [**msDS-SDReferenceDomain**](/windows/desktop/ADSchema/a-msds-sdreferencedomain) attribute that contains the distinguished name of the reference domain for that application directory partition. The security system uses the specified domain to interpret local domain references for default security descriptors attached to objects created in that application directory partition. The reference domain can be specified when the **crossRef** object for an application directory partition is created. This requires, however, that a **crossRef** object be pre-created for the application directory partition. If no reference domain is specified, the system automatically sets the reference domain based on one of the following conditions:

-   If the parent of the application directory partition object is another application directory partition, then the [**msDS-SDReferenceDomain**](/windows/desktop/ADSchema/a-msds-sdreferencedomain) attribute of the parent application directory partition is used for the reference domain.
-   If the parent object is a domain, then that domain is used for the reference domain.
-   If there is no parent object, then the forest root domain is used for the reference domain.

The **crossRef** attribute can also be changed to the reference domain after the partition is created, but this is not recommended.

A similar issue arises if a local group is specified in an ACL for an object in an application directory partition. In this case, the [**msDS-SDReferenceDomain**](/windows/desktop/ADSchema/a-msds-sdreferencedomain) attribute cannot be used to interpret the reference domain for a local group. To avoid this problem, local groups should not be used in the ACLs of application directory partition objects.

 

 