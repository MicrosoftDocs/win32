---
Description: Explains the security descriptor definition language (SDDL).
ms.assetid: 2b15325e-34ed-497b-ae6d-3ec3ac168232
title: Security Descriptor Definition Language
ms.topic: article
ms.date: 05/31/2018
---

# Security Descriptor Definition Language

The security descriptor definition language (SDDL) defines the string format that the [**ConvertSecurityDescriptorToStringSecurityDescriptor**](/windows/desktop/api/Sddl/nf-sddl-convertsecuritydescriptortostringsecuritydescriptora) and [**ConvertStringSecurityDescriptorToSecurityDescriptor**](/windows/desktop/api/Sddl/nf-sddl-convertstringsecuritydescriptortosecuritydescriptora) functions use to describe a [*security descriptor*](https://msdn.microsoft.com/library/windows/desktop/ms721625#-security-security-descriptor-gly) as a text string. The language also defines string elements for describing information in the components of a security descriptor.

> [!Note]  
> Conditional [*access control entries*](https://msdn.microsoft.com/library/windows/desktop/ms721532#-security-access-control-entry-gly) (ACEs) have a different SDDL format than other ACE types. For ACEs, see [ACE Strings](ace-strings.md). For conditional ACEs, see [Security Descriptor Definition Language for Conditional ACEs](security-descriptor-definition-language-for-conditional-aces-.md).

 

## Related topics

<dl> <dt>

[Security Descriptor String Format](security-descriptor-string-format.md)
</dt> <dt>

[Security Descriptor Definition Language for Conditional ACEs](security-descriptor-definition-language-for-conditional-aces-.md)
</dt> <dt>

[ACE Strings](ace-strings.md)
</dt> <dt>

[SID Strings](sid-strings.md)
</dt> <dt>

[\[MS-DTYP\]: Security Descriptor Description Language](http://msdn.microsoft.com/library/cc230368(PROT.10).aspx)
</dt> </dl>

 

 



