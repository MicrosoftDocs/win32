---
description: Binaries from Windows Server 2003 with Service Pack 1 (SP1) are compatible with Windows Vista and Windows Server 2008. However, binaries from earlier versions of Windows must be recompiled.
ms.assetid: ef40fdf6-b039-4664-bafb-b88c9286c010
title: Porting Backup Applications
ms.topic: article
ms.date: 05/31/2018
---

# Porting Backup Applications

Binaries from Windows Server 2003 with Service Pack 1 (SP1) are compatible with Windows Vista and Windows Server 2008. However, binaries from earlier versions of Windows must be recompiled.

## Porting Windows XP Backup Applications to Windows Vista

Several VSS interfaces have changed since Windows XP. At a minimum, Windows XP applications must be recompiled using header files and libraries from the VSS 7.2 SDK or the Windows Vista or Windows Server 2008 SDK.

## Porting Windows Server 2003 SP1 Backup Applications to Windows Vista

Binaries from Windows Server 2003 with SP1 are compatible with Windows Vista and Windows Server 2008. However, most Windows Server 2003 with SP1 backup applications must be updated to account for new features, which are described in the following sections.

## Compiling Backup Applications for Windows Vista

Applications that use interfaces available in Windows Server 2003 can be compiled using header files and libraries provided in the VSS 7.2 SDK. To use new interfaces, applications must be recompiled using the header files and libraries included in the Windows Vista SDK.

> [!Note]  
> Binaries compiled using Windows Vista or Windows Server 2008 are not compatible with Windows Server 2003 with SP1 or earlier versions of Windows.

 

 

 



