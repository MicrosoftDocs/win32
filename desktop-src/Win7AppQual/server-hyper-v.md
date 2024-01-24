---
description: Server Hyper-V
ms.assetid: 6a31cca3-f47c-4663-b2e8-aad6b4a6f28f
title: Server Hyper-V
ms.topic: article
ms.date: 05/31/2018
---

# Server Hyper-V

## Platforms

 **Clients** - Windows XP \| Windows Vista \| Windows 7  
**Servers** - Windows Server 2008 \| Windows Server 2008 R2  

## Feature Impact

 **Severity** - Low  
**Frequency** - Low  





## Description

Server virtualization enables multiple operating systems to run on a single physical machine as virtual machines (VMs), allowing you to consolidate workloads of underutilized server machines onto a smaller number of fully utilized machines. Windows 7 includes several enhancements to the Windows Server 2008 version:

-   **Live Migration:** In Windows Server 2008, we had Quick Migration. With Live Migration, we improved migration speed and storage flexibility.
-   **Logical Processor Support:** We increased logical host processors from 16LP to 64LP.
-   **Storage Hot Add:** Now you can add additional VHD or Pass-through disks to a running virtual machine without turning off the virtual machine.
-   **New Hardware Support:** We have added support for the technologies included in new processors and network cards coming to market, including Second Level Translation (SLAT), TCP Offload (Chimney), and VMdQ.
-   **Terminal Services virtualization (TSv):** We centralized desktop solution for Hyper-V.

## Manifestation of Impact

-   **Live Migration:** You may need to change the way you have architected your storage systems in order to fully leverage this technology. Though these changes may not be required, you may choose to implement them in order to fully leverage the benefits. You may need a management application to orchestrate Live Migration.
-   **Logical Processor Support:** This feature will have no impact on customers or ISVs when migrating from Windows Server 2008 to Windows Server 2008 R2.
-   **Storage Hot Add:** This feature will have no impact to customers or ISVs when migrating from Windows Server 2008 to Windows Server 2008 R2. Management applications that configure the settings of a virtual machine may require updating in order to manage this new feature.
-   **New Hardware Support:** These features apply only to new hardware that is being introduced to the market. Because it will not have build-in support for these features, it is not likely that a physical server that is being migrated from Windows Server 2008 to Windows Server 2008 R2 will be impacted. If these features are available on the server that is being migrated, no direct changes are anticipated.
-   **Terminal Services virtualization:** This feature will have no impact to customers or ISVs when migrating from Windows Server 2008 to Windows Server 2008 R2. Applications that leverage Terminal Services (TS) may be impacted. This feature directly integrates with TS and therefore applications that configure TS may require updating in order to manage this new feature.

## Mitigation

-   **Live Migration:** Provide prescriptive Guidance to end users with best practices and recommendations for storage system design. You must inform the end user about the options and recommendations.

## Leveraging Capabilitities

-   **Live Migration:** This feature enables the Dynamic IT environment. Virtualization Management Application Developers must modify their application to leverage this new feature. Microsoft will make WMI interfaces publically available to allow a developer to integrate applications with this feature.
-   **Terminal Services virtualization:** This feature enables a new virtualization scenario. Applications that leverage Terminal Services (TS) may be impacted. This feature directly integrates with TS and therefore applications that configure TS may require updating in order to manage this new feature.

## Links to Other Resources

[WMI management interfaces for Hyper-V v1](/previous-versions/windows/desktop/virtual/windows-virtualization-portal). While most of this content will apply to v2 of Hyper-V, an updated version with v2-specific information should be available closer to the Windows 7 launch.

 

 
