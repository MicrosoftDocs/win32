---
description: Offline Registry Library
ms.assetid: 5861e0a9-6a3f-4bc8-ae8b-d51c9de28217
title: Offline Registry Library
ms.topic: article
ms.date: 05/31/2018
---

# Offline Registry Library

## Purpose

The offline registry library (Offreg.dll) is used to modify a registry hive outside the active system registry. This library is intended for registry update scenarios such as servicing an operating system image. The library supports registry hive formats starting with Windows Vista.

## Developer audience

This technology is for original equipment manufacturers (OEMs), antivirus and antimalware software vendors, and other application developers who must be able to parse registry hive files without loading them into the active registry.

## Run-time requirements

The offline registry library is provided as a binary redistributable dynamic-link library (DLL). This library runs on the following versions of Windows:

<dl> Windows Server 2016  
Windows 10  
Windows 8.1  
Windows Server 2012 R2  
Windows 8  
Windows Server 2012  
Windows 7  
Windows Server 2008 R2  
Windows Server 2008  
Windows Vista  
</dl>

Applications should link to Offreg.dll using dynamic linking.

Offreg.dll is provided in the Windows Driver Kit (WDK) for Windows 10 and earlier versions of the Windows operating system.

For information about obtaining the WDK, see [How to Get the WDK and the WLK](/windows-hardware/drivers/download-the-wdk) or visit the [MSDN Subscriptions](https://msdn.microsoft.com/subscriptions/default.aspx) website.

## In this section

-   [**About the Offline Registry Library**](about-the-offline-registry-library.md)
-   [**Offline Registry Library Functions**](offline-registry-library-functions.md)

 

 
