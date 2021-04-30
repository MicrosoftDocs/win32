---
description: Actions by security packages that are not supported in Windows.
ms.assetid: E2BF8041-DF2F-4282-A3CC-A15FF2D7F4A2
title: Restrictions around Registering and Installing a Security Package
ms.topic: article
ms.date: 05/31/2018
---

# Restrictions around Registering and Installing a Security Package

The removal, replacement, or wrapping of inbox Security Packages (for example, Kerberos or NTLM) is not a supported action in Windows, and as of January 10, 2017, it is prevented. Third party Security Packages (SSPs/APs) can be added; however, Windows does not support the removal of preconfigured SSPs/APs. Specifically, editing the **HKLM\\SYSTEM\\CurrentControlSet\\Control\\Lsa\\OSConfig\\Security Packages** registry setting has never been supported.

Starting in Windows 8.1, customers who want to provide additional functionality can add their Security Packages using the registry setting **HKLM\\SYSTEM\\CurrentControlSet\\Control\\Lsa\\Security Packages** ([Registering SSP/AP DLLs](registering-ssp-ap-dlls.md)) and the associated registry setting **SecurityProviders** ([Writing and Installing a Security Support Provider](writing-and-installing-a-security-support-provider.md)), if applicable. Furthermore, the purpose of [Security Packages](../secgloss/s-gly.md#_security_security_package_gly) is to implement new *security protocols* which can be in the form of a security support provider (SSP) or an [authentication package](../secgloss/a-gly.md#_security_authentication_package_gly) (AP). The purpose of an SSP is to provide *authenticated connection*, *message integrity*, and *message encryption services* that are not already supported in the system, while an AP is used to add new *authentication logic* used to determine whether to permit a user to log on.

Microsoft is invested in customer security, and is trying to ensure that critical processes such as SSPs and APs are not easily removable from the system. Hence, the **HKLM\\SYSTEM\\CurrentControlSet\\Control\\Lsa\\OSConfig\\Security Packages** registry setting was restricted starting in Windows 8.1 in order to prevent changes to it. In order to facilitate third party Security Packages, **HKLM\\SYSTEM\\CurrentControlSet\\Control\\Lsa\\Security Packages** was made the designated setting for custom SSPs/APs. It is further recommended that any functionality in custom SSPs/APs that is outside the scope of Security Packages defined by Microsoft be removed from such custom SSPs/APs, and that inbox Security Packages are not removed by any product.

 

 
