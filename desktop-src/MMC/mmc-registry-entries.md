---
title: MMC 2.0 Registry Entries
description: To enable a snap-in to be added to a console file, the snap-in (or the snap-ins setup program) must add the appropriate entries in the MMC registry key (HKEY\_LOCAL\_MACHINE\\Software\\Microsoft\\MMC).
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: e1db8f4a-5420-4f67-b47b-8f0c3a734a9a
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- registry entries MMC 2.0
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# MMC 2.0 Registry Entries

To enable a snap-in to be added to a console file, the snap-in (or the snap-in's setup program) must add the appropriate entries in the MMC registry key (**HKEY\_LOCAL\_MACHINE\\Software\\Microsoft\\MMC**). Usually, you implement registry code to make the appropriate MMC entries for your snap-in in the **DllRegisterServer** function (or in a registrar script if you are using the ATL Registrar) of your snap-in's in-process server DLL.

The entries are determined by the type of snap-in (stand-alone or extension).

There are two main keys:

<dl> <dt>

<span id="HKEY_LOCAL_MACHINE_Software_Microsoft_MMC_Snapins"></span><span id="hkey_local_machine_software_microsoft_mmc_snapins"></span><span id="HKEY_LOCAL_MACHINE_SOFTWARE_MICROSOFT_MMC_SNAPINS"></span>[HKEY\_LOCAL\_MACHINE\\Software\\Microsoft\\MMC\\Snapins](snapins-key.md)
</dt> <dd>

Contains information about each snap-in that can be added to an MMC console file. Both stand-alone and extension snap-ins must be added here.

</dd> <dt>

<span id="HKEY_LOCAL_MACHINE_Software_Microsoft_MMC_NodeTypes"></span><span id="hkey_local_machine_software_microsoft_mmc_nodetypes"></span><span id="HKEY_LOCAL_MACHINE_SOFTWARE_MICROSOFT_MMC_NODETYPES"></span>[HKEY\_LOCAL\_MACHINE\\Software\\Microsoft\\MMC\\NodeTypes](nodetypes-key.md)
</dt> <dd>

Contains information about the extensions for each node type.

</dd> </dl>

 

 




