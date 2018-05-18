---
Description: 'Resource protection prevents the replacement of system files and folders and registry keys essential to the operating system. Modifying protected resources can cause application or system failure.'
ms.assetid: '27df9300-8bea-4748-9acd-2c1625093ece'
title: Windows Resource Protection
---

# Windows Resource Protection

## Purpose

Windows Resource Protection (WRP) prevents the replacement of essential system files, folders, and registry keys that are installed as part of the operating system. It became available starting with Windows Server 2008 and Windows Vista. Applications should not overwrite these resources because they are used by the system and other applications. Protecting these resources prevents application and operating system failures. WRP is the new name for Windows File Protection (WFP). WRP protects registry keys and folders as well as essential system files.

## Where applicable

All Windows-based applications and their installation programs that run on Windows Server 2008 or Windows Vista, and later operating systems, should be aware of WRP. All Windows-based applications that run on Microsoft Windows Server 2003 or Windows XP and their installation programs should be aware of WFP.

## Developer audience

The WRP API is designed for use by C/C++ programmers. The WRP API has two functions: [**SfcIsFileProtected**](sfcisfileprotected.md) and [**SfcIsKeyProtected**](sfciskeyprotected.md).

## Run-time requirements

Applications that use only the [**SfcIsFileProtected**](sfcisfileprotected.md) function require Windows Server 2008, Windows Vista, Windows Server 2003, or Windows XP. Applications that use the [**SfcIsKeyProtected**](sfciskeyprotected.md) function require Windows Server 2008 or Windows Vista.

## In this section



| Topic                                                                                     | Description                                 |
|-------------------------------------------------------------------------------------------|---------------------------------------------|
| [About Windows Resource Protection](about-windows-file-protection.md)<br/>         | General information about WRP.<br/>   |
| [Windows Resource Protection Reference](windows-file-protection-reference.md)<br/> | Reference documentation for WRP.<br/> |



 

 

 




