---
Description: 'It is sometimes useful to back up and restore only sections of files. VSS provides partial file mechanisms, which, if requesters support it, allows writers to specify partial file backups and restores.'
ms.assetid: '02b74a4e-d69f-4eeb-866a-3399598b7035'
title: Working with Partial Files
---

# Working with Partial Files

It is sometimes useful to back up and restore only sections of files. VSS provides [*partial file*](vssgloss-p.md#base-vssgloss-partial-file-support) mechanisms, which, if requesters support it, allows writers to specify partial file backups and restores.

Partial file operations are frequently of greatest use to writers that maintain very large files, only a small fraction of which change between backup operations. This being the case, it is frequently useful to copy only that section that changed to backup media. For this reason, partial file operations are typically, but not exclusively, used to support incremental backup and restore operations.

If a writer wants to implement a partial file operation, it uses [**CVssWriter::IsPartialFileSupportEnabled**](cvsswriter-ispartialfilesupportenabled.md) to determine whether the requester it is working with supports the operation.

If the requester supports partial file operations, and if it adds the component that manages the file (or the component that defines the component set that contains the file) to the Backup Components Document, a writer indicates which sections of the file to save (typically while handling a [**PrepareForBackup**](ivssbackupcomponents-prepareforbackup.md) or [*PostSnapshot*](vssgloss-p.md#-win32-vssgloss-prepareforbackup-event) event) by calling [**IVssComponent::AddPartialFile**](ivsscomponent-addpartialfile.md).

In addition to a path and file name, the writer supplies the range, optional metadata information to [**IVssComponent::AddPartialFile**](ivsscomponent-addpartialfile.md).

The range information is provided as a string that contains either of the following:

-   Pairs of offsets into the file to be backed up (in bytes) and the length of the section to be backed up (in bytes), the offset and length being separated by a colon, and each pair separated by a comma, for example, *Offset1***:***Length1***,** *Offset2***:***Length2*.

    Each value is a 64-bit integer (in either hexadecimal or decimal format) specifying a byte offset and length in bytes, respectively.

-   The full path, including file name, on the current system of a binary ranges file containing the following:
    -   The number (expressed as a 64-bit integer) of distinct file ranges contained in the file
    -   Each range expressed as a pair of 64-bit integers: the first member of the pair being the offset into the file being backed up (in bytes), and the second member being the length of data to be backed up (in bytes)

If a writer uses a ranges file to specify a partial file operation, a requester must guarantee that either this file is backed up (even if the file is not necessarily part of the default backup set) or that the ranges information is preserved on the backup media in some other way. If the ranges file's information is not backed up, restoring the partially backed up file will be impossible.

The writer can also add a string containing metadata. This metadata can be in a writer-specific format because it is intended to allow the writer to validate any future restores.

With this information, a supporting requester can perform a partial file backup.

As an example, consider a large file whose header (bytes 64-512) contains a record count and other frequently updated information, and whose most recent data is to be found in the file's last 65536 bytes—bytes 0x1239E8577A to 0x1239E7577A.

A writer could specify a range list as the string "**64:448,0x1239E8577A:65536**."

On restore, and prior to actually performing a restore operation, a requester should check to see if any files require partial file support.

To do this, the requester first iterates over the writers with stored components in its Backup Components Document using [**IVssBackupComponents::GetWriterComponentsCount**](ivssbackupcomponents-getwritercomponentscount.md) and [**IVssBackupComponents::GetWriterComponents**](ivssbackupcomponents-getwritercomponents.md).

The [**IVssBackupComponents::GetWriterComponents**](ivssbackupcomponents-getwritercomponents.md) interface is then used to return instances of the [**IVssWriterComponentsExt**](ivsswritercomponentsext.md) interface, which provide [**IVssWriterComponentsExt::GetComponent**](ivsswritercomponents-getcomponent.md) and [**IVssWriterComponentsExt::GetComponentCount**](ivsswritercomponents-getcomponentcount.md), that allow the requester to obtain [**IVssComponent**](ivsscomponent.md) instances.

This allows a requester to obtain information about the partially backed up files to participate in a restore by using [**IVssComponent::GetPartialFileCount**](ivsscomponent-getpartialfilecount.md) and [**IVssComponent::GetPartialFile**](ivsscomponent-getpartialfile.md) for the instance of [**IVssComponent**](ivsscomponent.md) corresponding to the component that manages the file (or the component that defines the component set that contains the file).

If the partial file operation was controlled by a ranges file, that file should be restored prior to copied data back to disk. It may happen that the requester needed to copy the ranges file back to a new location on disk. In this case, it indicates that it has done so through the [**IVssBackupComponents::SetRangesFilePath**](ivssbackupcomponents-setrangesfilepath.md).

The requester then proceeds to copy data into the appropriate locations in the restore destination already on disk.

A writer (while handling a [**PostRestore**](ivssbackupcomponents-postrestore.md) event), by examining [**IVssComponent::GetFileRestoreStatus**](ivsscomponent-getfilerestorestatus.md) for the files indicated by [**IVssComponent::GetPartialFile**](ivsscomponent-getpartialfile.md), determines if the partial file operation was successful. The writer should always attempt to verify the correctness of this restore using the offset information and any metadata included in the Backup Components Document.

If the requester has had to restore the ranges file to a new location, VSS will update this information so that the path returned by [**IVssComponent::GetPartialFile**](ivsscomponent-getpartialfile.md) is correct.

 

 



