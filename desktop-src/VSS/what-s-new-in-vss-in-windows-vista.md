---
description: Windows Vista.
ms.assetid: 3b16744d-b9c2-4462-a409-de94d9103c39
title: What's New in VSS in Windows Vista
ms.topic: article
ms.date: 05/31/2018
---

# What's New in VSS in Windows Vista

Windows Vista introduces the following changes to the Volume Shadow Copy Service.

Note that all changes for Windows Vista also apply to Windows Server 2008 and Windows Vista with Service Pack 1 (SP1).

## New VSS Interfaces

[**IVssBackupComponentsEx2**](/windows/desktop/api/VsBackup/nl-vsbackup-ivssbackupcomponentsex2)

[**IVssComponentEx**](/windows/desktop/api/VsWriter/nl-vswriter-ivsscomponentex)

[**IVssCreateWriterMetadataEx**](/windows/desktop/api/VsWriter/nl-vswriter-ivsscreatewritermetadataex)

[**IVssDifferentialSoftwareSnapshotMgmt2**](/windows/desktop/api/VsMgmt/nn-vsmgmt-ivssdifferentialsoftwaresnapshotmgmt2)

[**IVssExamineWriterMetadataEx2**](/windows/desktop/api/VsBackup/nl-vsbackup-ivssexaminewritermetadataex2)

## New VSS Classes

[**CVssWriterEx**](/windows/desktop/api/VsWriter/nl-vswriter-cvsswriterex)

## New VSS Enumerations

[**VSS\_ROLLFORWARD\_TYPE**](/windows/desktop/api/Vss/ne-vss-vss_rollforward_type)

## Existing VSS Enumeration Modifications

<dl> <dt>

<span id="VSS_BACKUP_SCHEMA_enumeration"></span><span id="vss_backup_schema_enumeration"></span><span id="VSS_BACKUP_SCHEMA_ENUMERATION"></span>[**VSS\_BACKUP\_SCHEMA**](/windows/desktop/api/Vss/ne-vss-vss_backup_schema) enumeration
</dt> <dd>

<dl> <dt>

<span id="Added_values_"></span><span id="added_values_"></span><span id="ADDED_VALUES_"></span>Added values:
</dt> <dd>

VSS\_BS\_AUTHORITATIVE\_RESTORE

VSS\_BS\_INDEPENDENT\_SYSTEM\_STATE

VSS\_BS\_RESTORE\_RENAME

VSS\_BS\_ROLLFORWARD\_RESTORE

</dd> </dl> </dd> </dl>

<dl> <dt>

<span id="VSS_COMPONENT_FLAGS_enumeration"></span><span id="vss_component_flags_enumeration"></span><span id="VSS_COMPONENT_FLAGS_ENUMERATION"></span>[**VSS\_COMPONENT\_FLAGS**](/windows/desktop/api/VsWriter/ne-vswriter-vss_component_flags) enumeration
</dt> <dd>

<dl> <dt>

<span id="Added_values_"></span><span id="added_values_"></span><span id="ADDED_VALUES_"></span>Added values:
</dt> <dd>

VSS\_CF\_NOT\_SYSTEM\_STATE

</dd> </dl> </dd> </dl>

<dl> <dt>

<span id="_VSS_VOLUME_SNAPSHOT_ATTRIBUTES_enumeration"></span><span id="_vss_volume_snapshot_attributes_enumeration"></span><span id="_VSS_VOLUME_SNAPSHOT_ATTRIBUTES_ENUMERATION"></span>[**\_VSS\_VOLUME\_SNAPSHOT\_ATTRIBUTES**](/windows/desktop/api/Vss/ne-vss-vss_volume_snapshot_attributes) enumeration
</dt> <dd>

<dl> <dt>

<span id="Added_values_"></span><span id="added_values_"></span><span id="ADDED_VALUES_"></span>Added values:
</dt> <dd>

VSS\_VOLSNAP\_ATTR\_NO\_AUTORECOVERY

VSS\_VOLSNAP\_ATTR\_NOT\_TRANSACTED

</dd> </dl> </dd> </dl>

## VSS Event Tracing and Logging

-   The VSS trace file can now be located on any local volume. On versions of Windows prior to Windows Vista, the VSS trace file could not be located on a volume that was in the shadow copy set.
-   Many event log entries have been reworded to make them clearer.
-   All VSS event log entries now contain context information.

## VSS Error Reporting

-   Descriptions of all VSS error codes can now be retrieved by calling the [**FormatMessage**](/windows/win32/api/winbase/nf-winbase-formatmessage) function with the FORMAT\_MESSAGE\_FROM\_HMODULE flag specified in the *dwFlags* parameter.
-   The VSS error code messages are contained in vsstrace.dll. A handle to this module must be specified in the *lpSource* parameter.

## Excluding Files from Shadow Copies

Applications or services can use the FilesNotToSnapshot registry key to specify files to be deleted from newly created shadow copies. For more information, see [Excluding Files from Shadow Copies](excluding-files-from-shadow-copies.md).

## Backup and Restore Application Compatibility

Developers of backup and restore applications need to be aware of certain new features in Windows Vista and Windows Server 2008. For an application compatibility checklist, see [Application Compatibility for Backup and Restore](application-compatibility-for-backup-and-restore.md).

 

 
