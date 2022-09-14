---
description: The File table contains a complete list of all the source files for the installation.
ms.assetid: 481fdc45-82db-4128-93de-388562f636e9
title: Ordering File Sequence Numbers in a Cabinet, File Table and Media Table
ms.topic: article
ms.date: 05/31/2018
---

# Ordering File Sequence Numbers in a Cabinet, File Table and Media Table

The [File table](file-table.md) contains a complete list of all the source files for the installation. Files can be stored on the source media as individual files or compressed within [cabinet files](cabinet-files.md). The sequence numbers in the Sequence column of the File table, together with the LastSequence field of the [Media table](media-table.md), specify both the order of installation for files and the source media on which each file is located. Each record in the Media table identifies the source disk containing all the files with sequence numbers less than or equal to the value shown in the LastSequence column and greater than the LastSequence value of the previous disk.

For example, suppose a file has a sequence number of 92 entered in the Sequence column of the File table. To determine on which source disk this file resides, the installer checks the record of the Media table for the entry with the smallest LastSequence value that is larger than 92. The DiskId column is the primary key for the Media table and this field uniquely identifies the disk in the table.

The maximum limit on the number of files that can be listed in the File table of a Windows Installer package is 32767 files. To create a Windows Installer package containing more files, see [Authoring a Large Package](authoring-a-large-package.md).

Package authors can reduce the size of their installation packages by compressing the source files and including them in cabinet files. The source file image can be compressed, uncompressed, or a mixture of both types. For more information about compressed and uncompressed sources see [Compressed and Uncompressed Sources](compressed-and-uncompressed-sources.md). Compressed source files must be stored inside of a cabinet file. The compressed files inside a cabinet have their own internal sequence numbers. The values of these internal sequence numbers do not need to match the value of the sequence numbers within the File table. However, the sequence of the files specified in the File table must be identical to the actual sequence of the files within the cabinets. The sequence numbers of uncompressed files need not be unique. For example, if all the files are uncompressed and reside on one disk, all the files can have the same sequence number in the File table.

The Media table describes the set of disks that make up the source media for the installation. The first entry in the Media table must always have a 1 in the DiskId field. Files should be organized on the source media such that all the files on disk 1 have File table sequence numbers that are smaller than the sequence numbers of files on disk 2, and all of the sequence numbers on disk 2 should be smaller than on disk 3, and so on. This requirement also applies to a disk that contains both compressed and uncompressed sources. For example, if the media sources for the installation are located on two source disks, and if disk 1 contains both uncompressed files and a cabinet file, then both of the uncompressed files and the files in the cabinet must have sequence numbers smaller than the smallest file sequence number of any file stored on disk 2. If all files on disk 1 are compressed in a cabinet file, the Media table could be authored as shown in the following table.

[Media Table](media-table.md) (partial)



| DiskId | LastSequence | DiskPrompt | Cabinet   | VolumeLabel |
|--------|--------------|------------|-----------|-------------|
| 1      | 5            | 1          | mycab.cab | Disk 1      |
| 2      | 10           | 2          |           | Disk 2      |



 

If some files on disk 1 are compressed in a cabinet and some are uncompressed, the Media table could be authored as follows.

[Media Table](media-table.md) (partial)



| DiskId | LastSequence | DiskPrompt | Cabinet   | VolumeLabel |
|--------|--------------|------------|-----------|-------------|
| 1      | 5            | 1          |           | Disk 1      |
| 2      | 10           | 1          | mycab.cab | Disk 1      |
| 3      | 15           | 2          |           | Disk 2      |



 

Note that the authoring in the following Media table is incorrect because it specifies some file sequence numbers on disk 2 that are smaller than some files inside the cabinet on disk 1.

[Media Table](media-table.md)



| DiskId | LastSequence | DiskPrompt | Cabinet   | VolumeLabel |
|--------|--------------|------------|-----------|-------------|
| 1      | 5            | 1          |           | Disk 1      |
| 2      | 10           | 2          |           | Disk 2      |
| 3      | 15           | 1          | mycab.cab | Disk 1      |



 

Large files can be split between two or more cabinet files. There can be no more than 15 files in any one cabinet file that spans to the next cabinet file. For example, if you have three cabinet files, the first cabinet can have 15 files that span to the second cabinet file, and the second cabinet can have 15 files that span to the third cabinet file. When you add a record to the File table for a file multiple cabinets, use the first part of the file to specify the file sequence number you enter in the Sequence column.

The File and Media tables could be authored as follows if there are three files, two cabinets, and two disks. In this example, c1.cab resides on disk1 and c2.cab resides on disk2. The file f2 spans both cabinets. The c1.cab cabinet contains the entire f1 file and the first part of file f2. The c2.cab cabinet contains the second part of f2 and the entire f3 file.

[Media Table](media-table.md) (partial)



| DiskId | LastSequence | DiskPrompt | Cabinet | VolumeLabel |
|--------|--------------|------------|---------|-------------|
| 1      | 5            | 1          | c1.cab  | Disk 1      |
| 2      | 10           | 2          | c2.cab  | Disk 2      |



 

[File Table](file-table.md) (partial)



| File | Sequence |
|------|----------|
| f1   | 1        |
| f2   | 2        |
| f3   | 6        |



 

 

 



