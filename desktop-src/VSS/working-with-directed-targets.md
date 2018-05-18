---
Description: 'The directed target mechanism allows writers to remap files at restore time.'
ms.assetid: 'c0b4ab26-2bb6-4b0f-b837-01057983b49b'
title: Working with Directed Targets
---

# Working with Directed Targets

The [*directed target*](vssgloss-d.md#base-vssgloss-directed-targeting) mechanism allows writers to remap files at restore time. This allows writers to do the following:

-   Specify new target locations (analogous to a requester's [**IVssBackupComponents::AddNewTarget**](ivssbackupcomponents-addnewtarget.md)).
-   Reclaim disk space by restoring only needed parts of a file to disk, particularly when a file was backed up using the [*partial file*](vssgloss-p.md#base-vssgloss-partial-file-support) mechanism.
-   Change the file format to meet current needs.

Any file to be used with a directed target operation must have a [*restore target*](vssgloss-r.md#base-vssgloss-restore-target) of VSS\_RT\_DIRECTED.

Once it has been established that a requester can support a directed target operation, a writer (while handling the [**PreRestore**](ivssbackupcomponents-prerestore.md) event) uses the [**IVssComponent::AddDirectedTarget**](ivsscomponent-adddirectedtarget.md) for the instance of [**IVssComponent**](ivsscomponent.md) corresponding to the component that manages the file (or the component that defines the component set that contains the file) to define how the file is to be remapped on restore.

In using [**IVssComponent::AddDirectedTarget**](ivsscomponent-adddirectedtarget.md), writers specify the file name and path used to back up the file, the file name and path of its restore destination (these values can be the same as the original file name and path), and source and destination file ranges.

As with partial file operations, range lists are pairs of offsets into the file to be backed up (in bytes) and the length of the section to be restored (in bytes), the offset and length being separated by a colon, and each pair separated by a comma: *Offset1***:***Length1***,** *Offset2***:***Length2*. Each value is a 64-bit integer in either hexadecimal or decimal format.

If a writer needs to use the directed target mechanism to have the requester restore a file to a new location, it would have called [**IVssComponent::AddDirectedTarget**](ivsscomponent-adddirectedtarget.md) with the original file name and path and the new file name and path, and specify source destination ranges with a zero offset and a length equal to that of the entire file size.

For instance, if a writer needs to have a 200K file, C:\\WriterData\\Index.dat, restored as C:\\WriterData\\OldIndex.dat, the source and destination range string would be "**0:204880**."

To remap a large, partially backed-up file, the requester would use the source range used to back up the file and a destination range that will reduce the file size. The source range information can be obtained by using [**IVssComponent::GetPartialFile**](ivsscomponent-getpartialfile.md) for the instance of [**IVssComponent**](ivsscomponent.md) corresponding to the component that manages the file (or the component that defines the component set that contains the file).

If the partially backed-up file was initially a large file whose header, bytes 64-512, contains a records count and other frequently updated information, and whose most recent data is to be found in the file's last 65536 bytes—bytes 0x1239E8577A to 0x1239E7577A, a writer could specify a source range list as the string "**64:448,0x1239E8577A:65536**."

If the writer wanted to remap the restored file to contain only the header and most recent data, the range list could be the string "**0:488,488:65536**."

Prior to actually performing a restore operation, a requester should check to see if any files require directed target support.

To do this, the requester first iterates over the writers with stored components in its Backup Components Document using [**IVssBackupComponents::GetWriterComponentsCount**](ivssbackupcomponents-getwritercomponentscount.md) and [**IVssBackupComponents::GetWriterComponents**](ivssbackupcomponents-getwritercomponents.md).

The [**IVssBackupComponents::GetWriterComponents**](ivssbackupcomponents-getwritercomponents.md) interface is then used to return instances of the [**IVssWriterComponentsExt**](ivsswritercomponentsext.md) interface, which provides [**IVssWriterComponentsExt::GetComponent**](ivsswritercomponents-getcomponent.md) and [**IVssWriterComponentsExt::GetComponentCount**](ivsswritercomponents-getcomponentcount.md) methods that allow the requester to obtain [**IVssComponent**](ivsscomponent.md) instances.

This allows a requester to obtain directed target candidates by using [**IVssComponent::GetDirectedTargetCount**](ivsscomponent-getdirectedtargetcount.md) and [**IVssComponent::GetDirectedTarget**](ivsscomponent-getdirectedtarget.md) for the instance of [**IVssComponent**](ivsscomponent.md) corresponding to the component that manages the file (or the component that defines the component set that contains the file).

 

 



