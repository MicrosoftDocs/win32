---
description: Learn about Windows restrictions on registering and installing security packages (SSPs/APs). Understand supported and unsupported actions for custom security packages.
ms.assetid: E2BF8041-DF2F-4282-A3CC-A15FF2D7F4A2
title: Security Package Registration Restrictions
ms.topic: concept-article
ms.date: 10/28/2025
---

# Restrictions on registering and installing a security package

Windows doesn't support removing, replacing, or wrapping inbox security packages, such as Kerberos or NTLM. As of January 10, 2017, Windows prevents these actions. You can add third-party security packages (SSPs/APs), but Windows doesn't support removing preconfigured SSPs/APs. Specifically, editing the `HKLM\SYSTEM\CurrentControlSet\Control\Lsa\OSConfig\Security Packages` registry setting isn't supported.

Starting in Windows 8.1, you can add security packages to provide extra functionality by using the registry setting `HKLM\SYSTEM\CurrentControlSet\Control\Lsa\Security Packages` ([Registering SSP/AP DLLs](registering-ssp-ap-dlls.md)) and the associated registry setting **SecurityProviders** ([Writing and Installing a Security Support Provider](writing-and-installing-a-security-support-provider.md)), if applicable. The purpose of [Security Packages](../secgloss/s-gly.md#_security_security_package_gly) is to implement new *security protocols* in the form of a security support provider (SSP) or an [authentication package](../secgloss/a-gly.md#_security_authentication_package_gly) (AP). An SSP provides *authenticated connection*, *message integrity*, and *message encryption services* that the system doesn't already support. An AP adds new *authentication logic* to determine whether to permit a user to sign in.

Microsoft is invested in customer security and wants to ensure that critical processes such as SSPs and APs aren't easily removable from the system. To prevent changes, Windows restricted the `HKLM\SYSTEM\CurrentControlSet\Control\Lsa\OSConfig\Security Packages` registry setting starting in Windows 8.1. To facilitate third-party security packages, Windows designated `HKLM\SYSTEM\CurrentControlSet\Control\Lsa\Security Packages` as the setting for custom SSPs/APs. Remove any functionality in custom SSPs/APs that falls outside the scope of security packages defined by Microsoft, and don't remove inbox security packages.

## Related content

This article is for developers creating custom security packages. For information about configuring and administering LSA and security policies on Windows systems, see the following resources:

- [LSA Policy](../secmgmt/lsa-policy.md) - Overview of the Local Security Authority and policy management for administrators
- [Managing Policy Information](../secmgmt/managing-policy-information.md) - How to query and set global policy information for the local computer and domain
- [Configuring additional LSA protection](/windows-server/security/credentials-protection-and-management/configuring-additional-lsa-protection) - Windows Server guidance for LSA protection configuration
