---
description: Security Support Provider Interface (SSPI) allows an application to use various security models available on a computer or network without changing the interface to the security system.
ms.assetid: 86ffc8c0-727d-437f-ac36-10df6563b0be
title: SSPI Model
ms.topic: article
ms.date: 05/31/2018
---

# SSPI Model

[*Security Support Provider Interface*](../secgloss/s-gly.md) (SSPI) allows an application to use various security models available on a computer or network without changing the interface to the security system. SSPI does not establish logon [*credentials*](../secgloss/c-gly.md) because that is generally a privileged operation handled by the operating system.

A [*security support provider*](../secgloss/s-gly.md) (SSP) is contained in a [*dynamic-link library*](../secgloss/d-gly.md) (DLL) that implements SSPI by making one or more [*security packages*](../secgloss/s-gly.md) available to applications. Each security package provides mappings between the SSPI function calls of an application and the functions of an actual security model. Security packages support [*security protocols*](../secgloss/s-gly.md) such as [*Kerberos*](../secgloss/k-gly.md) authentication and LAN Manager.

The SSPI interface is available in kernel mode as well as user mode. To use SSPI functionality in kernel mode, you must install the Windows Installable File System DDK. The calling model remains the same, but kernel mode considerations are noted on function reference pages. For more information, see [SSPI Functions](authentication-functions.md).

 

 
