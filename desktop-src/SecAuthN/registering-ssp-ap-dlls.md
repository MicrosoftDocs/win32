---
description: After developing a security support provider/authentication package dynamic-link library (SSP/AP DLL) containing one or more custom security packages, you must register it.
ms.assetid: db0d899e-dbd4-40d3-98d8-4d9668c01453
title: Registering SSP/AP DLLs
ms.topic: article
ms.date: 05/31/2018
---

# Registering SSP/AP DLLs

After developing a [*security support provider*](../secgloss/s-gly.md)/[*authentication package*](../secgloss/a-gly.md) dynamic-link library (SSP/AP DLL) containing one or more custom [*security packages*](../secgloss/s-gly.md), you must register it. To do so, add the name of your custom SSP/AP DLL to the data of the following registry value:

**HKEY\_LOCAL\_MACHINE**\\**System**\\**CurrentControlSet**\\**Control**\\**Lsa**\\**Security Packages**

The data for this registry value is a list of the names of SSP/AP DLLs, without the ".dll" extension. The data type for this list is **REG\_MULTI\_SZ** so there must be a null character ('\\0') between each DLL name in the list.

Typically, SSP/AP DLLs are stored in the %systemroot%/system32 directory. If this is the path to your custom SSP/AP DLL then do not include the path as part of the DLL name. If, however, the DLL is in a different path, include the complete path to the DLL in the name.

Each time the system starts, the LSA loads the SSP/AP DLLs in this list and performs the initialization sequence described in [LSA-Mode Initialization](lsa-mode-initialization.md).

### Registering a custom security package as the default TLS SSP

After developing a custom TLS security support provider and registering it as described above, you must also register it as the “default TLS SSP.” To do so, populate the package name of your custom SSP to the data of the following registry value:

**HKEY\_LOCAL\_MACHINE**\\**System**\\**CurrentControlSet**\\**Control**\\**Lsa**\\**Default TLS SSP**

The data for this registry value is the package name of SSP, not the dll name. The data type for this is **REG\_SZ**.

User mode applications which use “default TLS SSP” will use the default registered here. Kernel mode applications or user mode applications which use “Microsoft Unified Security Protocol Provider” or other specific TLS SSP names will not be impacted by this change.

> [!Note]  
> This registry information pertains to SSP/AP DLL's only. For information about registering security support providers (SSPs), see [Writing and Installing a Security Support Provider](writing-and-installing-a-security-support-provider.md). For information about the differences between SSP/AP and SSP DLLs, see [SSP/APs vs. SSPs](ssp-aps-versus-ssps.md).

 

## Related topics

<dl> <dt>

[Restrictions around Registering and Installing a Security Package](restrictions-around-registering-and-installing-a-security-package.md)
</dt> </dl>

 

 
