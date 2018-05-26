---
Description: Windows Server 2008.
ms.assetid: 2f7b62f8-ba1e-42d2-8872-38d4475e4a2a
title: Whats New in VSS in Windows Server 2008 and Windows Vista SP1
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# What's New in VSS in Windows Server 2008 and Windows Vista SP1

Windows Server 2008 and Windows Vista with Service Pack 1 (SP1) introduce the following changes to the Volume Shadow Copy Service.

> [!Note]  
> All changes for Windows Vista apply to Windows Server 2008 and Windows Vista with SP1. For details on those changes, see [What's New in VSS in Windows Vista](what-s-new-in-vss-in-windows-vista.md).

 

-   [New VSS Interfaces](#new-vss-interfaces)
-   [New VSS Enumerations](#new-vss-enumerations)
-   [New VSS Structures](#new-vss-structures)
-   [Existing VSS Enumeration Modifications](#existing-vss-enumeration-modifications)
-   [Existing VSS Interface Modifications](#existing-vss-interface-modifications)
-   [New VSS Writers](#new-vss-writers)

## New VSS Interfaces

<dl>

[**IVssDifferentialSoftwareSnapshotMgmt3**](/windows/win32/VsMgmt/nn-vsmgmt-ivssdifferentialsoftwaresnapshotmgmt3?branch=master)  
[**IVssHardwareSnapshotProviderEx**](/windows/win32/VsProv/nn-vsprov-ivsshardwaresnapshotproviderex?branch=master)  
</dl>

## New VSS Enumerations

<dl>

[**\_VSS\_HARDWARE\_OPTIONS**](/windows/win32/Vss/ne-vss-_vss_hardware_options?branch=master)  
[**VSS\_PROTECTION\_FAULT**](/windows/win32/VsMgmt/ne-vsmgmt-_vss_protection_fault?branch=master)  
[**VSS\_PROTECTION\_LEVEL**](/windows/win32/VsMgmt/ne-vsmgmt-_vss_protection_level?branch=master)  
</dl>

## New VSS Structures

<dl>

[**VSS\_VOLUME\_PROTECTION\_INFO**](/windows/win32/VsMgmt/ns-vsmgmt-_vss_volume_protection_info?branch=master)  
</dl>

## Existing VSS Enumeration Modifications

<dl> <dt>

<span id="VSS_BACKUP_SCHEMA_enumeration"></span><span id="vss_backup_schema_enumeration"></span><span id="VSS_BACKUP_SCHEMA_ENUMERATION"></span>[**VSS\_BACKUP\_SCHEMA**](/windows/win32/Vss/ne-vss-_vss_backup_schema?branch=master) enumeration
</dt> <dd>

<dl> <dt>

<span id="Added_value_"></span><span id="added_value_"></span><span id="ADDED_VALUE_"></span>Added value:
</dt> <dd>

VSS\_BS\_WRITER\_SUPPORTS\_PARALLEL\_RESTORES

</dd> </dl> </dd> </dl>

<dl> <dt>

<span id="_VSS_VOLUME_SNAPSHOT_ATTRIBUTES_enumeration"></span><span id="_vss_volume_snapshot_attributes_enumeration"></span><span id="_VSS_VOLUME_SNAPSHOT_ATTRIBUTES_ENUMERATION"></span>[**\_VSS\_VOLUME\_SNAPSHOT\_ATTRIBUTES**](/windows/win32/Vss/ne-vss-_vss_volume_snapshot_attributes?branch=master) enumeration
</dt> <dd>

<dl> <dt>

<span id="Added_values_"></span><span id="added_values_"></span><span id="ADDED_VALUES_"></span>Added values:
</dt> <dd>

VSS\_VOLSNAP\_ATTR\_DELAYED\_POSTSNAPSHOT

VSS\_VOLSNAP\_ATTR\_TXF\_RECOVERY

</dd> </dl> </dd> </dl>

## Existing VSS Interface Modifications

<dl> <dt>

<span id="IVssBackupComponentsEx2_interface"></span><span id="ivssbackupcomponentsex2_interface"></span><span id="IVSSBACKUPCOMPONENTSEX2_INTERFACE"></span>[**IVssBackupComponentsEx2**](/windows/win32/VsBackup/nl-vsbackup-ivssbackupcomponentsex2?branch=master) interface
</dt> <dd>

<dl> <dt>

<span id="Added_method_"></span><span id="added_method_"></span><span id="ADDED_METHOD_"></span>Added method:
</dt> <dd>

[**BreakSnapshotSetEx**](/windows/win32/VsBackup/nf-vsbackup-ivssbackupcomponentsex2-breaksnapshotsetex?branch=master)

</dd> </dl> </dd> </dl>

## New VSS Writers

Windows Server 2008 and Windows Vista with SP1 introduce the following VSS writers:

-   IIS Configuration Writer
-   IIS Metabase Writer
-   NPS VSS Writer
-   Remote Desktop Services (Terminal Services) Gateway VSS Writer
-   Remote Desktop Services (Terminal Services) Licensing VSS Writer

These writers are documented in [In-Box VSS Writers](in-box-vss-writers.md).

 

 



