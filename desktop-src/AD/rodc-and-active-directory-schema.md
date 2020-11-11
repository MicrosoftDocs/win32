---
title: Read-Only DCs and the Active Directory Schema
description: Windows Server 2008 introduces a new type of domain controller, the Read-only Domain Controller (RODC).
ms.assetid: 9d9082d2-6f7f-4ffa-b8c7-6414be764d0c
ms.tgt_platform: multiple
ms.topic: article
ms.date: 05/31/2018
---

# Read-Only DCs and the Active Directory Schema

Windows Server 2008 introduces a new type of domain controller, the Read-only Domain Controller (RODC). This provides a domain controller for use at branch offices where a full domain controller cannot be placed. The intent is to allow users in the branch offices to logon and perform tasks like file/printer sharing even when there is no network connectivity to hub sites.

RODC does not change the way schema is used. However, it is worthwhile to mention that the schema supports a Read-Only Partial Attribute Set (RO-PAS), also referred to as an RODC filtered attribute set, which is a special attribute set that is NOT replicated to RODCs for security reasons. RO-PAS are defined in the schema via the [**searchFlags**](/windows/desktop/ADSchema/a-searchflags) attribute.

## RODC filtered attribute set

Some applications that use [Active Directory Domain Services](active-directory-domain-services.md) as a data store may have credential-like data (such as passwords, credentials, or encryption keys) that should not be stored on a Read-Only Domain Controller in case the RODC is stolen or compromised. For this type of application, you can add the attribute to the RODC filtered attribute set to prevent it from replicating to RODCs in the forest, and mark the attribute as confidential, which removes the ability to read the data for members of the Authenticated Users group (including any RODCs).

## Adding attributes to the RODC filtered attribute set

The RODC filtered attribute set is a dynamic set of attributes that is not replicated to any RODCs in the forest. You can configure the RODC filtered attribute set on a schema master that runs Windows Server 2008. When the attributes are prevented from replicating to RODCs, that data cannot be exposed unnecessarily if an RODC is stolen or compromised.

You cannot add system-critical attributes to the RODC filtered attribute set. An attribute is system critical if it is required for AD DS, Local Security Authority (LSA), Security Accounts Manager (SAM), and any of Microsoft-specific Security Service Providers, such as the Kerberos authentication protocol, to function properly. In releases of Windows Server 2008 after Beta 3, a system-critical attribute has a schemaFlagsEx attribute value of (schemaFlagsEx attribute value & 0x1 = **TRUE**).

For step by step instructions to adding attributes to the RODC filtered attribute set, see [Appendix D of the step-by-step guide for RODCs]( /previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/cc772331(v=ws.10)).

## Marking attributes as confidential

In addition, it is recommended that you also mark as confidential any attributes that you configure as part of the RODC filtered attribute set. To mark an attribute confidential, you have to remove the Read permission for the attribute for the Authenticated Users group. Marking the attribute as confidential provides an additional safeguard against an RODC that is compromised by removing the permissions that are necessary to read the credential-like data. For more information about marking attributes as confidential, see [article 922836 in the Microsoft Knowledge Base]( https://support.microsoft.com/kb/922836).

## Related topics

<dl> <dt>

[Step-by-Step Guide for Read-only Domain Controllers]( https://support.microsoft.com/kb/922836)
</dt> </dl>

 

 