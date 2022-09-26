---
description: Starting in Windows 8, the AppInit\_DLLs infrastructure is disabled when secure boot is enabled.
ms.assetid: 3ADE71C7-7113-4D26-8D6D-5609CAF13397
title: AppInit DLLs and Secure Boot
ms.topic: article
ms.date: 05/31/2018
---

# AppInit DLLs and Secure Boot

Starting in Windows 8, the AppInit\_DLLs infrastructure is disabled when secure boot is enabled.

## About AppInit\_DLLs

The AppInit\_DLLs infrastructure provides an easy way to hook system APIs by allowing custom DLLs to be loaded into the address space of every interactive application. Applications and malicious software both use AppInit DLLs for the same basic reason, which is to hook APIs; after the custom DLL is loaded, it can hook a well-known system API and implement alternate functionality. Only a small set of modern legitimate applications use this mechanism to load DLLs, while a large set of malware use this mechanism to compromise systems. Even legitimate AppInit\_DLLs can unintentionally cause system deadlocks and performance problems, therefore usage of AppInit\_DLLs is not recommended.

## AppInit\_DLLs and secure boot

Windows 8 adopted UEFI and secure boot to improve the overall system integrity and to provide strong protection against sophisticated threats. When secure boot is enabled, the AppInit\_DLLs mechanism is disabled as part of a no-compromise approach to protect customers against malware and threats.

Please note that secure boot is a UEFI protocol and not a Windows 8 feature. More info on UEFI and the secure boot protocol specification can be found at [https://www.uefi.org](https://www.uefi.org/).

## AppInit\_DLLs certification requirement for Windows 8 desktop apps

One of the certification requirements for Windows 8 desktop apps is that the app must not load arbitrary DLLs to intercept Win32 API calls using the AppInit\_DLLs mechanism. For more detailed information about the certification requirements, refer to section 1.1 of [Certification requirements for Windows 8 desktop apps](../win_cert/certification-requirements-for-windows-desktop-apps.md).

## Summary

-   The AppInit\_DLLs mechanism is not a recommended approach for legitimate applications because it can lead to system deadlocks and performance problems.
-   The AppInit\_DLLs mechanism is disabled by default when secure boot is enabled.
-   Using AppInit\_DLLs in a Windows 8 desktop app is a Windows desktop app certification failure.

See the following whitepaper for info about AppInit\_DLLs on Windows 7 and Windows Server 2008 R2: [AppInit DLLs in Windows 7 and Windows Server 2008 R2](https://learn.microsoft.com/en-us/windows/win32/win7appqual/appinit-dlls-in-windows-7-and-windows-server-2008-r2).

 

 
