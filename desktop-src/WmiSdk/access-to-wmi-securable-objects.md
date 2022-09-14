---
description: WMI relies on standard Windows security descriptors to control and protect access to securable objects like WMI namespaces, printers, services, and DCOM applications.
ms.assetid: 5893457d-3fc2-4d64-a6c2-0f410052ce52
ms.tgt_platform: multiple
title: Access to WMI Securable Objects
ms.topic: article
ms.date: 05/31/2018
---

# Access to WMI Securable Objects

WMI relies on standard Windows [*security descriptors*](/windows/desktop/SecGloss/s-gly) to control and protect access to securable objects like WMI namespaces, printers, services, and DCOM applications. For more information, see [Access to WMI Namespaces](access-to-wmi-namespaces.md).

The following topics are discussed in this section:

-   [Security Descriptors and SIDs](#security-descriptors-and-sids)
-   [Access Control](#access-control)
-   [Changing Access Security](#changing-access-security)
-   [Related topics](#related-topics)

## Security Descriptors and SIDs

WMI maintains access security by comparing the [*access token*](/windows/desktop/SecGloss/a-gly) of the user that attempts to access a securable object with the security descriptor of the object.

When a user or group is created on a system, the account is given a [*security identifier (SID)*](/windows/desktop/SecGloss/s-gly) The SID ensures that an account created with the same name as a previously deleted account does not inherit the previous security settings. An access token is created by combining the SID, the list of groups of which the user is a member, and the list of enabled or disabled privileges. These tokens are assigned to all processes and threads owned by the user.

## Access Control

When the user wants to use a secured object, the access token is compared with the [*discretionary access control list (DACL)*](/windows/desktop/SecGloss/d-gly) in the security descriptor on the object. The DACL contains permissions called [*access control entries (ACE)*](/windows/desktop/SecGloss/a-gly). [*System access control lists (SACL)*](/windows/desktop/SecGloss/s-gly) do the same thing as DACLs, but can generate security audit events. Starting with Windows Vista, WMI can make auditing entries in the Windows Security Log. For more information about auditing in WMI, see [Access to WMI Namespaces](access-to-wmi-namespaces.md).

Both the DACL and the SACL consist of a list of ACEs that describe which users have specific access rights, including writing to the WMI repository, remote access and execution, and logon permissions. WMI stores these ACLs in the WMI repository.

ACEs hold three types of access levels or grant/deny rights: allow, deny for DACL, and system audit (for SACLs). Deny ACEs precede allow ACEs in the DACL or SACL. When checking the user access rights, WMI runs consecutively through the access control list until it finds an allow ACE that applies to the requesting access token. The remaining ACEs are not checked after this point. If no appropriate allow ACE is found, then access is denied. For more information, see [Order of ACEs in a DACL](/windows/desktop/SecAuthZ/order-of-aces-in-a-dacl) and [Creating a DACL](/windows/desktop/SecBP/creating-a-dacl).

## Changing Access Security

With appropriate permissions, you can change the security on a securable object with a script or application. You can also change the security settings on WMI namespaces using the [*WMI Control*](gloss-w.md) or by adding a [Security Descriptor Definition Language (SDDL)](/windows/desktop/SecAuthZ/security-descriptor-definition-language) string in the [*Managed Object Format (MOF)*](gloss-m.md) file that defines classes for the namespace. For more information, see [Access to WMI Namespaces](access-to-wmi-namespaces.md), [Securing WMI Namespaces](securing-wmi-namespaces.md), and [Changing Access Security on Securable Objects](changing-access-security-on-securable-objects.md).

## Related topics

<dl> <dt>

[WMI Security Descriptor Objects](wmi-security-descriptor-objects.md)
</dt> <dt>

[WMI Security Constants](wmi-security-constants.md)
</dt> <dt>

[User Account Control and WMI](user-account-control-and-wmi.md)
</dt> <dt>

[WMI Security Descriptor Objects](wmi-security-descriptor-objects.md)
</dt> <dt>

[Access to WMI Namespaces](access-to-wmi-namespaces.md)
</dt> </dl>

 

 
