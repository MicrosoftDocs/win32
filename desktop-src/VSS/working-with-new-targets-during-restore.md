---
Description: 'A requester may need to restore files to a location indicated by something other than a file set''s default path or its alternate location mapping.'
ms.assetid: 'ce11485c-da0e-4c16-962e-eeedc2da3de4'
title: Working with New Targets during Restore
---

# Working with New Targets during Restore

A requester may need to restore files to a location indicated by something other than a file set's default path or its [*alternate location mapping*](vssgloss-a.md#base-vssgloss-alternate-location-mapping). There are many reasons why this might happen—for example, neither restore destination was accessible, or a requester user intentionally requests that files be restored to some previously unknown location. In this case, the requester uses the new target mechanism to indicate to writers that it has restored a file to a different area on disk.

Not all writers support a requester changing the restore destination of a file. A requester needs to verify writer support by checking the writer's backup schema mask (returned by [**IVssExamineWriterMetadata::GetBackupSchema**](ivssexaminewritermetadata-getbackupschema.md)) and verifying that it contains the VSS\_BS\_WRITER\_SUPPORTS\_NEW\_TARGET flag.

The requester indicates such a restoration through the [**IVssBackupComponents::AddNewTarget**](ivssbackupcomponents-addnewtarget.md) method. In addition to specifying a file specification and an original and a new restore destination, the requester specifies component information—a logical path and component name.

Which component's information is used depends on whether or not the component managing the file having a new target added was [*explicitly included*](vssgloss-e.md#base-vssgloss-explicit-component-inclusion) or [*implicitly included*](vssgloss-i.md#base-vssgloss-implicit-component-inclusion) in the backup.

If the managing component was explicitly included, then its information is used. If the managing component was implicitly included, it is a subcomponent in a component set. In this case, the component set's defining component's information is used.

While handling the [**PostRestore**](ivssbackupcomponents-postrestore.md) event, writers should check to see if any of its files were restored to a new location. This can be done by using the [**IVssComponent::GetNewTargetCount**](ivsscomponent-getnewtargetcount.md) and [**IVssComponent::GetNewTarget**](ivsscomponent-getnewtarget.md) methods.

The instance of the [**IVssComponent**](ivsscomponent.md) interface that is used depends on whether the file's managing component was explicitly or implicitly added to the backup.

 

 



