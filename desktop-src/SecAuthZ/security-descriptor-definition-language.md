---
description: Explains the security descriptor definition language (SDDL).
ms.assetid: 2b15325e-34ed-497b-ae6d-3ec3ac168232
title: Security Descriptor Definition Language
ms.topic: concept-article
ms.date: 07/08/2025
# customer intent: As a Windows app developer, I want to understand the security descriptor definition language (SDDL), so that I can work with security descriptors in my app.
---

# Security descriptor definition language

The security descriptor definition language (SDDL) defines the string format that the [ConvertSecurityDescriptorToStringSecurityDescriptor](/windows/win32/api/Sddl/nf-sddl-convertsecuritydescriptortostringsecuritydescriptora) and [ConvertStringSecurityDescriptorToSecurityDescriptor](/windows/win32/api/Sddl/nf-sddl-convertstringsecuritydescriptortosecuritydescriptora) functions use to describe a [security descriptor](/windows/win32/SecGloss/s-gly) as a text string. The language also defines string elements for describing information in the components of a security descriptor.

> [!NOTE]
> Conditional [access control entries](/windows/win32/SecGloss/a-gly) (ACEs) have a different SDDL format than other ACE types. For ACEs, see [ACE Strings](ace-strings.md). For conditional ACEs, see [Security Descriptor Definition Language for Conditional ACEs](security-descriptor-definition-language-for-conditional-aces-.md).

## Related content

[Security Descriptor String Format](security-descriptor-string-format.md)

[SID Strings](sid-strings.md)

[\[MS-DTYP\]: Security Descriptor Description Language](/openspecs/windows_protocols/ms-dtyp/4f4251cc-23b6-44b6-93ba-69688422cb06)
