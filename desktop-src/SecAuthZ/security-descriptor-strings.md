---
Description: A valid functional security descriptor contains security information in binary format.
ms.assetid: 8f802652-b2bf-45cf-8186-1ac31eef1fe1
title: Security Descriptor Strings
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Security Descriptor Strings

A valid functional [*security descriptor*](https://msdn.microsoft.com/library/windows/desktop/ms721625#-security-security-descriptor-gly) contains security information in binary format. The Windows API provides functions for converting binary security descriptors to and from text strings. Security descriptors in string format are not functional, but they can be useful for storing or transporting security descriptor information.

To convert a security descriptor to a string format, call the [**ConvertSecurityDescriptorToStringSecurityDescriptor**](/windows/win32/Sddl/nf-sddl-convertsecuritydescriptortostringsecuritydescriptora?branch=master) function. To convert a string-format security descriptor back to a valid functional security descriptor, call the [**ConvertStringSecurityDescriptorToSecurityDescriptor**](/windows/win32/Sddl/nf-sddl-convertstringsecuritydescriptortosecuritydescriptora?branch=master) function.

For more information, see [Security Descriptor Definition Language](security-descriptor-definition-language.md).

 

 



