---
title: Using BITS
description: Using BITS
ms.assetid: '65b69ccb-b413-4690-ac0d-774d88608bdf'
keywords:
- Background Intelligent Transfer Service
- Background Intelligent Transfer Service,tasks
- file transfer BITS
- Using BITS BITS
ms.topic: article
ms.date: 05/31/2018
---

# Using BITS

The following steps show how to perform a file transfer using the Background Intelligent Transfer Service (BITS)  [interfaces](bits-interfaces.md).

**To perform a file transfer**

1.  [Connect to the BITS service](connecting-to-the-bits-service.md)
2.  [Create a transfer job](creating-a-job.md)
3.  [Add files to the job](adding-files-to-a-job.md)
4.  [Start the job](/windows/desktop/api/Bits/nf-bits-ibackgroundcopyjob-resume)
5.  [Determine if BITS successfully transferred the files](determining-the-status-of-a-job.md)
6.  [Complete the job](completing-and-canceling-a-job.md)

The previous steps show how to transfer files using the default property values for a job. You can change the default behavior by changing one or more of the job's property values. For example, you can change the priority that the job is processed relative to other jobs in the queue, specify your own proxy setting, and register to receive event notification when BITS has transferred the files. For more information, see [Setting and Retrieving the Properties of a Job](setting-and-retrieving-the-properties-of-a-job.md).

Windows PowerShell provides a simple mechanism to manage many BITS tasks. This section contains the following topics that show how to use Windows PowerShell cmdlets with BITS:

-   [Using Windows PowerShell to Create BITS Transfer Jobs](using-windows-powershell-to-create-bits-transfer-jobs.md)
-   [Using WinRM Windows PowerShell Cmdlets to Manage BITS Transfer Jobs](using-winrm-windows-powershell-cmdlets-to-manage-bits-transfer-jobs.md)
-   [Using WMI Windows PowerShell Cmdlets to Manage the BITS Compact Server](using-wmi-windows-powershell-cmdlets-to-manage-the-bits-compact-server.md)

> [!Note]
>
> Starting with Windows 10, version 1607, you can also run PowerShell Cmdlets and use BITSAdmin or other applications that use the BITS [interfaces](bits-interfaces.md) from a PowerShell Remote command line connected to another machine (physical or virtual). This capability is not available when using a [PowerShell Direct](/virtualization/hyper-v-on-windows/user_guide/vmsession) command line to a virtual machine on the same physical machine, and it is not available when using WinRM cmdlets.
>
> A BITS Job created from a Remote PowerShell session will run under that session’s user account context and will only make progress when there is at least one active local logon session or Remote PowerShell session associated with that user account. For more information, see [To manage PowerShell Remote sessions](using-windows-powershell-to-create-bits-transfer-jobs.md).

 

This section also contains the following topics:

-   [Best Practices When Using BITS](best-practices-when-using-bits.md)
-   [Enumerating jobs in the transfer queue](enumerating-jobs-in-the-transfer-queue.md)
-   [Enumerating files in a job](enumerating-files-in-a-job.md)
-   [Handling errors](handling-errors.md)
-   [Retrieve the reply from an upload-reply job](retrieving-the-reply-from-an-upload-reply-job.md)

For sample code that uses the BITS interfaces, see [BITS Samples and Tools](bits-samples-and-tools.md).

 

 