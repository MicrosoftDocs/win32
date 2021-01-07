---
description: The directed target mechanism allows writers to remap files at restore time.
ms.assetid: c0b4ab26-2bb6-4b0f-b837-01057983b49b
title: Working with Directed Targets
ms.topic: article
ms.date: 05/31/2018
---

# Working with Directed Targets

The [*directed target*](vssgloss-d.md) mechanism allows writers to remap files at restore time. This allows writers to do the following:

-   Specify new target locations (analogous to a requester's [**IVssBackupComponents::AddNewTarget**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-addnewtarget)).
-   Reclaim disk space by restoring only needed parts of a file to disk, particularly when a file was backed up using the [*partial file*](vssgloss-p.md) mechanism.
-   Change the file format to meet current needs.

Any file to be used with a directed target operation must have a [*restore target*](vssgloss-r.md) of VSS\_RT\_DIRECTED.

Once it has been established that a requester can support a directed target operation, a writer (while handling the [**PreRestore**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-prerestore) event) uses the [**IVssComponent::AddDirectedTarget**](/windows/desktop/api/VsWriter/nf-vswriter-ivsscomponent-adddirectedtarget) for the instance of [**IVssComponent**](/windows/desktop/api/VsWriter/nl-vswriter-ivsscomponent) corresponding to the component that manages the file (or the component that defines the component set that contains the file) to define how the file is to be remapped on restore.

In using [**IVssComponent::AddDirectedTarget**](/windows/desktop/api/VsWriter/nf-vswriter-ivsscomponent-adddirectedtarget), writers specify the file name and path used to back up the file, the file name and path of its restore destination (these values can be the same as the original file name and path), and source and destination file ranges.

As with partial file operations, range lists are pairs of offsets into the file to be backed up (in bytes) and the length of the section to be restored (in bytes), the offset and length being separated by a colon, and each pair separated by a comma: *Offset1***:***Length1***,** *Offset2***:***Length2*. Each value is a 64-bit integer in either hexadecimal or decimal format.

If a writer needs to use the directed target mechanism to have the requester restore a file to a new location, it would have called [**IVssComponent::AddDirectedTarget**](/windows/desktop/api/VsWriter/nf-vswriter-ivsscomponent-adddirectedtarget) with the original file name and path and the new file name and path, and specify source destination ranges with a zero offset and a length equal to that of the entire file size.

For instance, if a writer needs to have a 200K file, C:\\WriterData\\Index.dat, restored as C:\\WriterData\\OldIndex.dat, the source and destination range string would be "**0:204880**."

To remap a large, partially backed-up file, the requester would use the source range used to back up the file and a destination range that will reduce the file size. The source range information can be obtained by using [**IVssComponent::GetPartialFile**](/windows/desktop/api/VsWriter/nf-vswriter-ivsscomponent-getpartialfile) for the instance of [**IVssComponent**](/windows/desktop/api/VsWriter/nl-vswriter-ivsscomponent) corresponding to the component that manages the file (or the component that defines the component set that contains the file).

If the partially backed-up file was initially a large file whose header, bytes 64-512, contains a records count and other frequently updated information, and whose most recent data is to be found in the file's last 65536 bytes—bytes 0x1239E8577A to 0x1239E7577A, a writer could specify a source range list as the string "**64:448,0x1239E8577A:65536**."

If the writer wanted to remap the restored file to contain only the header and most recent data, the range list could be the string "**0:488,488:65536**."

Prior to actually performing a restore operation, a requester should check to see if any files require directed target support.

To do this, the requester first iterates over the writers with stored components in its Backup Components Document using [**IVssBackupComponents::GetWriterComponentsCount**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-getwritercomponentscount) and [**IVssBackupComponents::GetWriterComponents**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-getwritercomponents).

The [**IVssBackupComponents::GetWriterComponents**](/windows/desktop/api/VsBackup/nf-vsbackup-ivssbackupcomponents-getwritercomponents) interface is then used to return instances of the [**IVssWriterComponentsExt**](/windows/win32/api/vsbackup/nl-vsbackup-ivsswritercomponentsext) interface, which provides [**IVssWriterComponentsExt::GetComponent**](/windows/desktop/api/VsWriter/nf-vswriter-ivsswritercomponents-getcomponent) and [**IVssWriterComponentsExt::GetComponentCount**](/windows/desktop/api/VsWriter/nf-vswriter-ivsswritercomponents-getcomponentcount) methods that allow the requester to obtain [**IVssComponent**](/windows/desktop/api/VsWriter/nl-vswriter-ivsscomponent) instances.

This allows a requester to obtain directed target candidates by using [**IVssComponent::GetDirectedTargetCount**](/windows/desktop/api/VsWriter/nf-vswriter-ivsscomponent-getdirectedtargetcount) and [**IVssComponent::GetDirectedTarget**](/windows/desktop/api/VsWriter/nf-vswriter-ivsscomponent-getdirectedtarget) for the instance of [**IVssComponent**](/windows/desktop/api/VsWriter/nl-vswriter-ivsscomponent) corresponding to the component that manages the file (or the component that defines the component set that contains the file).

 

 
