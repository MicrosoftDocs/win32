---
description: Dynamic Memory
ms.assetid: 0ea1de35-34ea-4e94-b90d-0f89503cb3fb
title: Dynamic Memory
ms.topic: article
ms.date: 05/31/2018
---

# Dynamic Memory

## Affected Platforms

**Clients (running as virtual machines)** - Windows Vista \| Windows 7  
**Servers** - Windows Server 2008 R2 Hyper-V SP1  


## Feature Impact

 **Severity** - Low  
**Frequency** - High  






## Description

At a high level, Hyper-V Dynamic Memory is a memory management enhancement for the Hyper-V role included in Windows Server 2008 R2 SP1. It is designed for production use and enables customers to achieve higher consolidation/virtual machine (VM) density ratios while optimizing the memory utilization in the physical machine. The static memory allocation is reduced and additional memory is allocated on an as needed basis. Dynamic Memory impacts software developers who want to ensure that their software works correctly in a virtual machine environment.

## Usage Scenario

There are two key usage scenarios where Dynamic Memory comes into play, host-side applications and guest-side applications.

**Host-side applications (management tools)**

Old tools managing a new Windows Server 2008 R2 SP1 server will not be able to access the new Dynamic Memory settings. New WMI APIs and performance counters have been developed to manage the new Dynamic Memory settings for Hyper-V virtual machines. Software developers working on management tools should take advantage of these APIs and counters for use with Windows Server 2008 R2 SP1 with the Hyper-V role installed. Details about these new APIs will be available via [Hyper-V WMI Provider documentation on MSDN](/previous-versions/windows/desktop/virtual/using-the-virtualization-wmi-provider).

**Guest-side applications**

Developers writing software for use inside a virtual machine configured to use Dynamic Memory need to keep in mind that VM system memory is no longer constant. Consequently, their application should free memory when it is no longer needed to allow other applications to take advantage of the resource.

Memory allocations and de-allocations continue to work as normal for user applications. Dynamic Memory is completely transparent to most end user applications. However if the software being developed makes use of memory performance counters in the virtual machine then careful testing should be performed in a Dynamic Memory enabled environment to ensure that the software takes the changes that are made to the Guest operating system memory allocation into account. Available memory is no longer "static" from the virtual machine?s perspective.

## Solutions

Virtual machines must have updated integration services (SP1) installed in order to take advantage of Dynamic Memory. Ensure that all machines used in the management of Hyper-V virtual machines are using the latest Windows Server 2008 R2 SP1 bits.

## Links to Other Resources

-   [Dynamic Memory Coming To Hyper-V blog](https://blogs.technet.com/b/virtualization/archive/2010/03/18/dynamic-memory-coming-to-hyper-v.aspx)
-   [Using the Hyper-V WMI Provider](/previous-versions/windows/desktop/virtual/using-the-virtualization-wmi-provider)

## Disclaimer

The information contained in this document relates to prerelease software product that may be substantially modified before its first commercial release. Accordingly, the information may not accurately describe or reflect the software product when first commercially released. This document is for informational purposes only. MICROSOFT MAKES NO WARRANTIES, EXPRESS OR IMPLIED, IN THIS DOCUMENT.

 

 
