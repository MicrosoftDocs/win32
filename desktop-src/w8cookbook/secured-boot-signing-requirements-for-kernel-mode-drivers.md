---
title: Secure boot feature signing requirements for kernel-mode drivers
description: Secure boot feature signing requirements for kernel-mode drivers
ms.assetid: 7FF64BA2-89E3-4E6F-B542-7BC7BF7F4FB2
ms.topic: article
ms.date: 05/31/2018
---

# Secure boot feature signing requirements for kernel-mode drivers

## Platforms

**Clients** – Windows 8  
**Servers** – Windows Server 2012  


## Description

In Windows 8 and Windows Server 2012, including WinPE, the kernel has been locked down to prevent malware introduced by boot or root kits from circumventing Windows operating system security requirements for signed drivers.

This change affects all kernel-mode drivers for devices that support unified extensible firmware interface (UEFI) Secure Boot; UEFI Secure Boot is required for Windows 8 certification for client machines, and optional for servers. It does not affect user-mode drivers.

Standard development for kernel-mode drivers involves either the use of kernel mode debugging or the boot configuration data (BCD) &lt;testsigning&gt; setting. Both of these are disabled when Secured Boot is on.

## Manifestation

Kernel-mode drivers will not run if they are not properly signed by a trusted certification authority (CA). The operating system will not allow untrusted drivers to run and standard mechanisms like kernel debugging and testsigning will not be permitted.

## Mitigation

To test drivers, you must disable Secure Boot in BIOS as well as meet the other test-signing requirements (see below).

When distributing drivers more widely they must be properly signed by a trusted CA.

## Resources

-   [Signing Drivers](/previous-versions/windows/hardware/design/dn653563(v=vs.85))

 

 
