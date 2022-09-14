---
description: The Security WMI providers can be used for wmi scripting and to create a managed security provider.
ms.assetid: c3f7bd91-6cea-43ee-b8a7-1506dbd7926d
title: Security WMI Providers
ms.topic: article
ms.date: 05/31/2018
---

# Security WMI Providers

## Purpose

The Security WMI providers enable administrators and programmers to configure BitLocker Drive Encryption (BDE) and the Trusted Platform Module (TPM) using Windows Management Instrumentation (WMI).

## Developer audience

This document specifies the WMI provider interface for managing and configuring BitLocker Drive Encryption (BDE) and Trusted Platform Module (TPM) on Windows Server 2008 R2 and Windows Server 2008 for servers, and Windows 7 and Windows Vista for client computers. It is intended to be read by those writing scripts, user interface elements, or other administrative tools for BDE or the TPM.

## Run-time requirements

The Security WMI Providers require the .mof file specified with each provider and a supported operating system. The minimum operating system is either Windows Server 2008 or Windows Vista. BitLocker Drive Encryption is only available for the Windows Vista Enterprise and Windows Vista Ultimate versions of Windows Vista. For information about run-time requirements for a particular programming element, see the Requirements section of the reference page for that element.

## In this section



| Topic                                                                               | Description                                                        |
|-------------------------------------------------------------------------------------|--------------------------------------------------------------------|
| [About Security WMI Providers](about-security-wmi-providers.md)<br/>         | Brief overview of the Security WMI Providers.<br/>           |
| [Security WMI Providers Reference](security-wmi-providers-reference.md)<br/> | Reference documentation for the Security WMI Providers.<br/> |



 

## Additional resources

The following are additional resources.



| Resource     | Description                                                                                                                                               |
|--------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Classes      | For more information about the Security WMI providers, see [**Win32\_EncryptableVolume**](win32-encryptablevolume.md) and [**Win32\_Tpm**](win32-tpm.md). |



 

 

 




