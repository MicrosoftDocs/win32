---
description: If this per-machine system policy is set to &\#0034;1&\#0034;, the installer prevents non-administrators from using User Account Control (UAC) Patching for any application installed on the computer.
ms.assetid: b122d6f4-2be6-4b9b-b8e0-ca08fe9c4f94
title: DisableLUAPatching
ms.topic: article
ms.date: 05/31/2018
---

# DisableLUAPatching

If this per-machine system policy is set to "1", the installer prevents non-administrators from using [User Account Control (UAC) Patching](user-account-control--uac--patching.md) for any application installed on the computer. When the per-machine system policy is not set or set to 0, non-administrators can apply least-privilege user patches to applications that are enabled for least-privilege user account patching.

Use the [**MSIDISABLELUAPATCHING**](msidisableluapatching.md) property to prevent the least-privilege patching of an application.

The DisableLUAPatching policy is available beginning with Windows Installer version 3.0.

## Registry Key

**HKEY\_LOCAL\_MACHINE**\\**Software**\\**Policies**\\**Microsoft**\\**Windows**\\**Installer**

## Data Type

**REG\_DWORD**

## Related topics

<dl> <dt>

[Not Supported in Windows Installer 2.0 and earlier](not-supported-in-windows-installer-version-2-0.md)
</dt> </dl>

 

 



