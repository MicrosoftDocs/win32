---
description: A trustee is the user account, group account, or logon session to which an access control entry (ACE) applies. Each ACE in an access control list (ACL) has one security identifier (SID) that identifies a trustee.
ms.assetid: 1c34faa0-936a-433a-9280-a94033f3f815
title: Trustees
ms.topic: article
ms.date: 05/31/2018
---

# Trustees

A trustee is the user account, group account, or [*logon session*](/windows/desktop/SecGloss/l-gly) to which an [*access control entry*](/windows/desktop/SecGloss/a-gly) (ACE) applies. Each ACE in an [*access control list*](/windows/desktop/SecGloss/a-gly) (ACL) has one [*security identifier*](/windows/desktop/SecGloss/s-gly) (SID) that identifies a trustee.

User accounts include accounts that human users or programs such as Windows Services use to log on to the local computer.

Group accounts cannot be used to log on to a computer, but they are useful in ACEs to allow or deny a set of access rights to one or more user accounts.

A [*logon SID*](/windows/desktop/SecGloss/l-gly) that identifies the current logon session is useful to allow or deny access rights only until the user logs off.

The access control functions use the [**TRUSTEE**](/windows/desktop/api/AccCtrl/ns-accctrl-trustee_a) structure to identify a trustee. The **TRUSTEE** structure enables you to use a name string or a SID to identify a trustee. If you use a name, the functions that create an ACE from the **TRUSTEE** structure perform the task of allocating the SID buffers and looking up the SID that corresponds to the account name. There are two helper functions, [**BuildTrusteeWithSid**](/windows/desktop/api/Aclapi/nf-aclapi-buildtrusteewithsida) and [**BuildTrusteeWithName**](/windows/desktop/api/Aclapi/nf-aclapi-buildtrusteewithnamea), that initialize a **TRUSTEE** structure with a specified SID or name. [**BuildTrusteeWithObjectsAndSid**](/windows/desktop/api/Aclapi/nf-aclapi-buildtrusteewithobjectsandsida) and [**BuildTrusteeWithObjectsAndName**](/windows/desktop/api/Aclapi/nf-aclapi-buildtrusteewithobjectsandnamea) allow you to initialize a **TRUSTEE** structure with object-specific ACE information. Three other helper functions, [**GetTrusteeForm**](/windows/desktop/api/Aclapi/nf-aclapi-gettrusteeforma), [**GetTrusteeName**](/windows/desktop/api/Aclapi/nf-aclapi-gettrusteenamea), and [**GetTrusteeType**](/windows/desktop/api/Aclapi/nf-aclapi-gettrusteetypea), retrieve the values of the various members of a **TRUSTEE** structure.

The **ptstrName** member of the [**TRUSTEE**](/windows/desktop/api/AccCtrl/ns-accctrl-trustee_a) structure can be a pointer to an [**OBJECTS\_AND\_NAME**](/windows/desktop/api/AccCtrl/ns-accctrl-objects_and_name_a) or [**OBJECTS\_AND\_SID**](/windows/desktop/api/AccCtrl/ns-accctrl-objects_and_sid) structure. These structures specify information about an [object-specific ACE](object-specific-aces.md) in addition to a trustee name or SID. This enables functions such as [**SetEntriesInAcl**](/windows/desktop/api/Aclapi/nf-aclapi-setentriesinacla) and [**GetExplicitEntriesFromAcl**](/windows/desktop/api/Aclapi/nf-aclapi-getexplicitentriesfromacla) to store object-specific ACE information in the **Trustee** member of the [**EXPLICIT\_ACCESS**](/windows/desktop/api/AccCtrl/ns-accctrl-explicit_access_a) structure.

 

 
