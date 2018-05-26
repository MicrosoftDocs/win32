---
Description: Windows Server 2008 R2 and Windows 7 introduce the following changes to the Volume Shadow Copy Service.
ms.assetid: 1287f175-29e4-40be-804b-d78542e76efc
title: Whats New in VSS in Windows Server 2008 R2 and Windows 7
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# What's New in VSS in Windows Server 2008 R2 and Windows 7

Windows Server 2008 R2 and Windows 7 introduce the following changes to the Volume Shadow Copy Service.

## New VSS Interfaces

<dl>

[**IVssBackupComponentsEx3**](/windows/win32/VsBackup/nl-vsbackup-ivssbackupcomponentsex3?branch=master)  
[**IVssComponentEx2**](/windows/win32/VsWriter/nl-vswriter-ivsscomponentex2?branch=master)  
[**IVssCreateExpressWriterMetadata**](/windows/win32/VsWriter/nl-vswriter-ivsscreateexpresswritermetadata?branch=master)  
[**IVssExpressWriter**](/windows/win32/VsWriter/nl-vswriter-ivssexpresswriter?branch=master)  
</dl>

## New VSS Classes

<dl>

[**CVssWriterEx2**](/windows/win32/VsWriter/nl-vswriter-cvsswriterex2?branch=master)  
</dl>

## New VSS Enumerations

<dl>

[**VSS\_RECOVERY\_OPTIONS**](/windows/win32/Vss/ne-vss-_vss_recovery_options?branch=master)  
</dl>

## New VSS Functions

<dl>

[**CreateVssExpressWriter**](/windows/win32/VsWriter/nf-vswriter-createvssexpresswriter?branch=master)  
</dl>

## Existing VSS Interface Modifications

<dl>

[**IVssHardwareSnapshotProviderEx**](/windows/win32/VsProv/nn-vsprov-ivsshardwaresnapshotproviderex?branch=master) interface<dl> Added method: [**ResyncLuns**](/windows/win32/VsProv/nf-vsprov-ivsshardwaresnapshotproviderex-resyncluns?branch=master)  
</dl> </dd> </dl>

## VSS Event Tracing and Logging

Beginning with Windows Server 2008 R2 and Windows 7, you can use the VssTrace tool, the Logman tool, or the Tracelog tool to collect tracing information for the VSS infrastructure. For more information, see [Using Tracing Tools with VSS](using-tracing-tools-with-vss.md).

## LUN Resynchronization

In Windows Server 2008 R2 and Windows 7, VSS requesters can use a hardware shadow copy provider feature called LUN resynchronization (or "LUN resync"). This is a fast-recovery scheme that allows an application administrator to restore data from a shadow copy to the original logical unit number (LUN) or to a new LUN. The shadow copy can be a full clone or a differential shadow copy. In either case, at the end of the resync operation, the destination LUN will have the same contents as the shadow copy LUN. During the resync operation, the array performs a block-level copy from the shadow copy to the destination LUN. For more information, see the following:

-   [LUN Resync - A fast recovery scenario in Server 2008 R2](http://go.microsoft.com/fwlink/p/?linkid=182212)
-   "How Shadow Copies Are Used" in [Volume Shadow Copy Service](http://go.microsoft.com/fwlink/p/?linkid=182211)
-   [Common LUN Resync gotchas](http://go.microsoft.com/fwlink/p/?linkid=182213)

## Express Writers

In Windows Server 2008 R2 and Windows 7, the VSS express interface allows an application to register the location of its data files without implementing a VSS writer. For more information, see [Volume Shadow Copy Service (VSS) Express Writers](http://go.microsoft.com/fwlink/p/?linkid=182214).

## New VSS Writers

Windows Server 2008 R2 and Windows 7 introduce the following VSS writers:

-   Performance Counters Writer
-   Task Scheduler Writer
-   VSS Metadata Store Writer

These new writers are documented in [In-Box VSS Writers](in-box-vss-writers.md).

 

 



