---
description: A valid functional security descriptor contains security information in binary format.
ms.assetid: 8f802652-b2bf-45cf-8186-1ac31eef1fe1
title: Security Descriptor Strings
ms.topic: article
ms.date: 05/31/2018
---

# Security Descriptor Strings

A valid functional [*security descriptor*](/windows/desktop/SecGloss/s-gly) contains security information in binary format. The Windows API provides functions for converting binary security descriptors to and from text strings. Security descriptors in string format are not functional, but they can be useful for storing or transporting security descriptor information.

To convert a security descriptor to a string format, call the [**ConvertSecurityDescriptorToStringSecurityDescriptor**](/windows/desktop/api/Sddl/nf-sddl-convertsecuritydescriptortostringsecuritydescriptora) function. To convert a string-format security descriptor back to a valid functional security descriptor, call the [**ConvertStringSecurityDescriptorToSecurityDescriptor**](/windows/desktop/api/Sddl/nf-sddl-convertstringsecuritydescriptortosecuritydescriptora) function.

For more information, see [Security Descriptor Definition Language](security-descriptor-definition-language.md).

 

 
