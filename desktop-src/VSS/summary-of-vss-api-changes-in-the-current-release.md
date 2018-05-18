---
Description: Summary of VSS API Changes in Windows Server 2003
ms.assetid: '35572fc6-9147-4726-ae7a-d78292683ba0'
title: Summary of VSS API Changes in Windows Server 2003
---

# Summary of VSS API Changes in Windows Server 2003

## Changes in the VSS Service

<dl> <dt>

<span id="Events_added_"></span><span id="events_added_"></span><span id="EVENTS_ADDED_"></span>Events added:
</dt> <dd>

[*BackupShutdown*](vssgloss-b.md#base-vssgloss-backupshutdown-event)

</dd> </dl>

## Changes in VSS Functionality

<dl> <dt>

<span id="Additional_functionality_"></span><span id="additional_functionality_"></span><span id="ADDITIONAL_FUNCTIONALITY_"></span>Additional functionality:
</dt> <dd>

[*partial file support*](vssgloss-p.md#base-vssgloss-partial-file-support)

[*directed targeting*](vssgloss-d.md#base-vssgloss-directed-targeting)

</dd> </dl>

## New VSS Interfaces

[**IVssWMDependency**](ivsswmdependency.md)

## Existing VSS Interface Modifications

<dl> <dt>

<span id="IVssAsync_interface"></span><span id="ivssasync_interface"></span><span id="IVSSASYNC_INTERFACE"></span>[**IVssAsync**](ivssasync.md) interface
</dt> <dd>

<dl> <dt>

<span id="Methods_modified_"></span><span id="methods_modified_"></span><span id="METHODS_MODIFIED_"></span>Methods modified:
</dt> <dd>

[**IVssAsync::Wait**](ivssasync-wait.md)

</dd> </dl> </dd> <dt>

<span id="IVssBackupComponents_interface"></span><span id="ivssbackupcomponents_interface"></span><span id="IVSSBACKUPCOMPONENTS_INTERFACE"></span>[**IVssBackupComponents**](ivssbackupcomponents.md) interface
</dt> <dd>

<dl> <dt>

<span id="Methods_added_"></span><span id="methods_added_"></span><span id="METHODS_ADDED_"></span>Methods added:
</dt> <dd>

[**IVssBackupComponents::AddNewTarget**](ivssbackupcomponents-addnewtarget.md)

[**IVssBackupComponents::QueryRevertStatus**](ivssbackupcomponents-queryrevertstatus.md)

[**IVssBackupComponents::RevertToSnapshot**](ivssbackupcomponents-reverttosnapshot.md)

[**IVssBackupComponents::SetRangesFilePath**](ivssbackupcomponents-setrangesfilepath.md)

[**IVssBackupComponents::SetRestoreState**](ivssbackupcomponents-setrestorestate.md)

</dd> </dl> </dd> <dt>

<span id="IVssCreateWriterMetadata_interface"></span><span id="ivsscreatewritermetadata_interface"></span><span id="IVSSCREATEWRITERMETADATA_INTERFACE"></span>[**IVssCreateWriterMetadata**](ivsscreatewritermetadata.md) interface
</dt> <dd>

<dl> <dt>

<span id="Methods_added_"></span><span id="methods_added_"></span><span id="METHODS_ADDED_"></span>Methods added:
</dt> <dd>

[**IVssCreateWriterMetadata::AddComponentDependency**](ivsscreatewritermetadata-addcomponentdependency.md)

[**IVssCreateWriterMetadata::SetBackupSchema**](ivsscreatewritermetadata-setbackupschema.md)

</dd> <dt>

<span id="Methods_modified_"></span><span id="methods_modified_"></span><span id="METHODS_MODIFIED_"></span>Methods modified:
</dt> <dd>

[**IVssCreateWriterMetadata::AddComponent**](ivsscreatewritermetadata-addcomponent.md)

[**IVssCreateWriterMetadata::AddDatabaseFiles**](ivsscreatewritermetadata-adddatabasefiles.md)

[**IVssCreateWriterMetadata::AddDatabaseLogFiles**](ivsscreatewritermetadata-adddatabaselogfiles.md)

[**IVssCreateWriterMetadata::AddFilesToFileGroup**](ivsscreatewritermetadata-addfilestofilegroup.md)

</dd> </dl> </dd> <dt>

<span id="IVssExamineWriterMetadata_interface"></span><span id="ivssexaminewritermetadata_interface"></span><span id="IVSSEXAMINEWRITERMETADATA_INTERFACE"></span>[**IVssExamineWriterMetadata**](ivssexaminewritermetadata.md) interface
</dt> <dd>

<dl> <dt>

<span id="Methods_added_"></span><span id="methods_added_"></span><span id="METHODS_ADDED_"></span>Methods added:
</dt> <dd>

[**IVssExamineWriterMetadata::GetBackupSchema**](ivssexaminewritermetadata-getbackupschema.md)

</dd> </dl> </dd> <dt>

<span id="IVssComponent_interface"></span><span id="ivsscomponent_interface"></span><span id="IVSSCOMPONENT_INTERFACE"></span>[**IVssComponent**](ivsscomponent.md) interface
</dt> <dd>

<dl> <dt>

<span id="Methods_removed_"></span><span id="methods_removed_"></span><span id="METHODS_REMOVED_"></span>Methods removed:
</dt> <dd>

**IVssComponent::AddNewTarget**

</dd> <dt>

<span id="Methods_added_"></span><span id="methods_added_"></span><span id="METHODS_ADDED_"></span>Methods added:
</dt> <dd>

[**IVssComponent::AddDifferencedFilesByLastModifyTime**](ivsscomponent-adddifferencedfilesbylastmodifytime.md)

[**IVssComponent::GetDifferencedFile**](ivsscomponent-getdifferencedfile.md)

[**IVssComponent::GetDifferencedFilesCount**](ivsscomponent-getdifferencedfilescount.md)

</dd> <dt>

<span id="Methods_no_longer_reserved_"></span><span id="methods_no_longer_reserved_"></span><span id="METHODS_NO_LONGER_RESERVED_"></span>Methods no longer reserved:
</dt> <dd>

[**IVssComponent::AddDirectedTarget**](ivsscomponent-adddirectedtarget.md)

[**IVssComponent::GetDirectedTarget**](ivsscomponent-getdirectedtarget.md)

</dd> </dl> </dd> <dt>

<span id="IVssWMComponent_interface"></span><span id="ivsswmcomponent_interface"></span><span id="IVSSWMCOMPONENT_INTERFACE"></span>[**IVssWMComponent**](ivsswmcomponent.md) interface
</dt> <dd>

<dl> <dt>

<span id="Methods_added_"></span><span id="methods_added_"></span><span id="METHODS_ADDED_"></span>Methods added:
</dt> <dd>

[**IVssWMComponent::GetDependency**](ivsswmcomponent-getdependency.md)

</dd> </dl> </dd> <dt>

<span id="IVssWMFiledesc_interface"></span><span id="ivsswmfiledesc_interface"></span><span id="IVSSWMFILEDESC_INTERFACE"></span>[**IVssWMFiledesc**](ivsswmfiledesc.md) interface
</dt> <dd>

<dl> <dt>

<span id="Methods_added_"></span><span id="methods_added_"></span><span id="METHODS_ADDED_"></span>Methods added:
</dt> <dd>

[**IVssWMFiledesc::GetBackupTypeMask**](ivsswmfiledesc-getbackuptypemask.md)

</dd> </dl> </dd> </dl>

## Existing VSS Class Modifications

<dl> <dt>

<span id="CVssWriter_class"></span><span id="cvsswriter_class"></span><span id="CVSSWRITER_CLASS"></span>[**CVssWriter**](cvsswriter.md) class
</dt> <dd>

<dl> <dt>

<span id="Methods_modified_"></span><span id="methods_modified_"></span><span id="METHODS_MODIFIED_"></span>Methods modified:
</dt> <dd>

[**CVssWriter::Initialize**](cvsswriter-initialize.md)

</dd> <dt>

<span id="Methods_added_"></span><span id="methods_added_"></span><span id="METHODS_ADDED_"></span>Methods added:
</dt> <dd>

[**CVssWriter::GetContext**](cvsswriter-getcontext.md)

[**CVssWriter::GetRestoreType**](cvsswriter-getrestoretype.md)

[**CVssWriter::GetSnapshotDeviceName**](cvsswriter-getsnapshotdevicename.md)

[**CVssWriter::OnBackupShutdown**](cvsswriter-onbackupshutdown.md)

</dd> </dl> </dd> </dl>

## New VSS Enumerations

<dl> <dt>

<span id="VSS_BACKUP_SCHEMA"></span><span id="vss_backup_schema"></span>[**VSS\_BACKUP\_SCHEMA**](vss-backup-schema.md)
</dt> <dd></dd> <dt>

<span id="VSS_COMPONENT_FLAGS"></span><span id="vss_component_flags"></span>[**VSS\_COMPONENT\_FLAGS**](vss-component-flags.md)
</dt> <dd></dd> <dt>

<span id="VSS_FILE_SPEC_BACKUP_TYPE"></span><span id="vss_file_spec_backup_type"></span>[**VSS\_FILE\_SPEC\_BACKUP\_TYPE**](vss-file-spec-backup-type.md)
</dt> <dd></dd> <dt>

<span id="VSS_RESTORE_TYPE"></span><span id="vss_restore_type"></span>[**VSS\_RESTORE\_TYPE**](vss-restore-type.md)
</dt> <dd></dd> </dl>

## Existing VSS Enumeration Modifications

<dl> <dt>

<span id="VSS_BACKUP_TYPE_enumeration"></span><span id="vss_backup_type_enumeration"></span><span id="VSS_BACKUP_TYPE_ENUMERATION"></span>[**VSS\_BACKUP\_TYPE**](vss-backup-type.md) enumeration
</dt> <dd>

<dl> <dt>

<span id="Added_values_"></span><span id="added_values_"></span><span id="ADDED_VALUES_"></span>Added values:
</dt> <dd>

VSS\_BT\_COPY

</dd> </dl> </dd> <dt>

<span id="VSS_RESTORE_TARGET_enumeration"></span><span id="vss_restore_target_enumeration"></span><span id="VSS_RESTORE_TARGET_ENUMERATION"></span>[**VSS\_RESTORE\_TARGET**](vss-restore-target.md) enumeration
</dt> <dd>

<dl> <dt>

<span id="Removed_values_"></span><span id="removed_values_"></span><span id="REMOVED_VALUES_"></span>Removed values:
</dt> <dd>

VSS\_RT\_NEW

</dd> </dl> </dd> <dt>

<span id="VSS_RESTOREMETHOD_ENUM_enumeration"></span><span id="vss_restoremethod_enum_enumeration"></span><span id="VSS_RESTOREMETHOD_ENUM_ENUMERATION"></span>[**VSS\_RESTOREMETHOD\_ENUM**](vss-restoremethod-enum.md) enumeration
</dt> <dd>

<dl> <dt>

<span id="Added_values_"></span><span id="added_values_"></span><span id="ADDED_VALUES_"></span>Added values:
</dt> <dd>

VSS\_RME\_RESTORE\_AT\_REBOOT\_IF\_CANNOT\_REPLACE

</dd> </dl> </dd> <dt>

<span id="VSS_SNAPSHOT_STATE_enumeration"></span><span id="vss_snapshot_state_enumeration"></span><span id="VSS_SNAPSHOT_STATE_ENUMERATION"></span>[**VSS\_SNAPSHOT\_STATE**](vss-snapshot-state.md) enumeration
</dt> <dd>

<dl> <dt>

<span id="Added_values_"></span><span id="added_values_"></span><span id="ADDED_VALUES_"></span>Added values:
</dt> <dd>

VSS\_SS\_PROCESSING\_POSTCOMMIT

VSS\_SS\_PROCESSING\_PREFINALCOMMIT

VSS\_SS\_PREFINALCOMMITTED

VSS\_SS\_PROCESSING\_POSTFINALCOMMIT

</dd> </dl> </dd> <dt>

<span id="_VSS_VOLUME_SNAPSHOT_ATTRIBUTES_enumeration"></span><span id="_vss_volume_snapshot_attributes_enumeration"></span><span id="_VSS_VOLUME_SNAPSHOT_ATTRIBUTES_ENUMERATION"></span>[**\_VSS\_VOLUME\_SNAPSHOT\_ATTRIBUTES**](-vss-volume-snapshot-attributes.md) enumeration
</dt> <dd>

<dl> <dt>

<span id="Added_values_"></span><span id="added_values_"></span><span id="ADDED_VALUES_"></span>Added values:
</dt> <dd>

VSS\_VOLSNAP\_ATTR\_AUTORECOVER

</dd> <dt>

<span id="Reserved_values_now_support_"></span><span id="reserved_values_now_support_"></span><span id="RESERVED_VALUES_NOW_SUPPORT_"></span>Reserved values now support:
</dt> <dd>

VSS\_VOLSNAP\_ATTR\_HARDWARE\_ASSISTED

VSS\_VOLSNAP\_ATTR\_IMPORTED

VSS\_VOLSNAP\_ATTR\_EXPOSED\_LOCALLY

VSS\_VOLSNAP\_ATTR\_EXPOSED\_REMOTELY

</dd> </dl> </dd> <dt>

<span id="VSS_WRITER_STATE_enumeration"></span><span id="vss_writer_state_enumeration"></span><span id="VSS_WRITER_STATE_ENUMERATION"></span>[**VSS\_WRITER\_STATE**](vss-writer-state.md) enumeration
</dt> <dd>

<dl> <dt>

<span id="Added_values_"></span><span id="added_values_"></span><span id="ADDED_VALUES_"></span>Added values:
</dt> <dd>

VSS\_WS\_FAILED\_AT\_BACKUPSHUTDOWN

</dd> </dl> </dd> </dl>

## Changes to VSS Structures

<dl> <dt>

<span id="VSS_COMPONENTINFO_structure"></span><span id="vss_componentinfo_structure"></span><span id="VSS_COMPONENTINFO_STRUCTURE"></span>[**VSS\_COMPONENTINFO**](vss-componentinfo.md) structure
</dt> <dd>

<dl> <dt>

<span id="Added_members_"></span><span id="added_members_"></span><span id="ADDED_MEMBERS_"></span>Added members:
</dt> <dd>

**bSelectableForRestore**

**dwComponentFlags**

**cDependencies**

</dd> </dl> </dd> </dl>

 

 



