---
description: Platform Path Override
ms.assetid: f430fd9a-f865-4cdb-b0ea-4e6d79913308
title: Platform Path Override
ms.topic: article
ms.date: 05/31/2018
---

# Platform Path Override

The [**SetupSetPlatformPathOverride**](/windows/desktop/api/Setupapi/nf-setupapi-setupsetplatformpathoverridea) function is used to set a platform path override for a target machine when working with INF files from a different machine. As such, it can refer to a different platform than the one it is currently running on. For dealing with media sources, it can refer to platforms that are no longer supported, such as Alpha, MIPS, and PPC. It removes the platform path override if none is specified.

After a platform path override is set by a call to [**SetupSetPlatformPathOverride**](/windows/desktop/api/Setupapi/nf-setupapi-setupsetplatformpathoverridea), any setup function that queues file copy operations will examine the final component of the source path. If the final component matches the name of the user's platform, the setup function will replace it with the override string set by **SetupSetPlatformPathOverride**.

For example, when installing printer drivers onto a MIPS server, you might want to install drivers for all supported platforms. Queuing the files normally would install the files specified in the MIPS-dependent sections of the INF file, with source paths such as \\\\root\\source\\mips. To install the files for a second platform, you must call [**SetupSetPlatformPathOverride**](/windows/desktop/api/Setupapi/nf-setupapi-setupsetplatformpathoverridea) with *Override* indicating the replacement platform. If the location indicated by *Override* contains the string value "alpha", file copy operations sent to the queue with a source path of \\\\root\\source\\mips would have their source path changed to \\\\root\\source\\alpha. You would repeat this process for each platform of interest.

 

 



