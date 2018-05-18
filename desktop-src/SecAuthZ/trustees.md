---
Description: 'A trustee is the user account, group account, or logon session to which an access control entry (ACE) applies. Each ACE in an access control list (ACL) has one security identifier (SID) that identifies a trustee.'
ms.assetid: '1c34faa0-936a-433a-9280-a94033f3f815'
title: Trustees
---

# Trustees

A trustee is the user account, group account, or [*logon session*](https://msdn.microsoft.com/library/windows/desktop/ms721592#-security-logon-session-gly) to which an [*access control entry*](https://msdn.microsoft.com/library/windows/desktop/ms721532#-security-access-control-entry-gly) (ACE) applies. Each ACE in an [*access control list*](https://msdn.microsoft.com/library/windows/desktop/ms721532#-security-access-control-list-gly) (ACL) has one [*security identifier*](https://msdn.microsoft.com/library/windows/desktop/ms721625#-security-security-identifier-gly) (SID) that identifies a trustee.

User accounts include accounts that human users or programs such as Windows Services use to log on to the local computer.

Group accounts cannot be used to log on to a computer, but they are useful in ACEs to allow or deny a set of access rights to one or more user accounts.

A [*logon SID*](https://msdn.microsoft.com/library/windows/desktop/ms721592#-security-logon-sid-gly) that identifies the current logon session is useful to allow or deny access rights only until the user logs off.

The access control functions use the [**TRUSTEE**](trustee.md) structure to identify a trustee. The **TRUSTEE** structure enables you to use a name string or a SID to identify a trustee. If you use a name, the functions that create an ACE from the **TRUSTEE** structure perform the task of allocating the SID buffers and looking up the SID that corresponds to the account name. There are two helper functions, [**BuildTrusteeWithSid**](buildtrusteewithsid.md) and [**BuildTrusteeWithName**](buildtrusteewithname.md), that initialize a **TRUSTEE** structure with a specified SID or name. [**BuildTrusteeWithObjectsAndSid**](buildtrusteewithobjectsandsid.md) and [**BuildTrusteeWithObjectsAndName**](buildtrusteewithobjectsandname.md) allow you to initialize a **TRUSTEE** structure with object-specific ACE information. Three other helper functions, [**GetTrusteeForm**](gettrusteeform.md), [**GetTrusteeName**](gettrusteename.md), and [**GetTrusteeType**](gettrusteetype.md), retrieve the values of the various members of a **TRUSTEE** structure.

The **ptstrName** member of the [**TRUSTEE**](trustee.md) structure can be a pointer to an [**OBJECTS\_AND\_NAME**](objects-and-name.md) or [**OBJECTS\_AND\_SID**](objects-and-sid.md) structure. These structures specify information about an [object-specific ACE](object-specific-aces.md) in addition to a trustee name or SID. This enables functions such as [**SetEntriesInAcl**](setentriesinacl.md) and [**GetExplicitEntriesFromAcl**](getexplicitentriesfromacl.md) to store object-specific ACE information in the **Trustee** member of the [**EXPLICIT\_ACCESS**](explicit-access.md) structure.

 

 



