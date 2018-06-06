---
Description: Security Support Provider Interface (SSPI) allows an application to use various security models available on a computer or network without changing the interface to the security system.
ms.assetid: 86ffc8c0-727d-437f-ac36-10df6563b0be
title: SSPI Model
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# SSPI Model

[*Security Support Provider Interface*](https://msdn.microsoft.com/3e9d7672-2314-45c8-8178-5a0afcfd0c50) (SSPI) allows an application to use various security models available on a computer or network without changing the interface to the security system. SSPI does not establish logon [*credentials*](https://msdn.microsoft.com/db46def4-bfdc-4801-a57d-d568e94a2dbb) because that is generally a privileged operation handled by the operating system.

A [*security support provider*](https://msdn.microsoft.com/3e9d7672-2314-45c8-8178-5a0afcfd0c50) (SSP) is contained in a [*dynamic-link library*](https://msdn.microsoft.com/d007cbb9-b547-4dc7-bc22-b526f650f7c2) (DLL) that implements SSPI by making one or more [*security packages*](https://msdn.microsoft.com/3e9d7672-2314-45c8-8178-5a0afcfd0c50) available to applications. Each security package provides mappings between the SSPI function calls of an application and the functions of an actual security model. Security packages support [*security protocols*](https://msdn.microsoft.com/3e9d7672-2314-45c8-8178-5a0afcfd0c50) such as [*Kerberos*](https://msdn.microsoft.com/f17042c3-ba1a-408f-af55-5f171b0dee33) authentication and LAN Manager.

The SSPI interface is available in kernel mode as well as user mode. To use SSPI functionality in kernel mode, you must install the Windows Installable File System DDK. The calling model remains the same, but kernel mode considerations are noted on function reference pages. For more information, see [SSPI Functions](authentication-functions.md).

 

 



