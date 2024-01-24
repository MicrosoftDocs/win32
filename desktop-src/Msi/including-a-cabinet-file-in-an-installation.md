---
description: This section describes including cabinet files in installations. For more information, see Using Cabinets and Compressed Sources.
ms.assetid: 17ea7f76-90b2-48fb-8187-64dc6d294443
title: Including a Cabinet File in an Installation
ms.topic: article
ms.date: 05/31/2018
---

# Including a Cabinet File in an Installation

This section describes including cabinet files in installations. For more information, see [Using Cabinets and Compressed Sources](using-cabinets-and-compressed-sources.md).

**To include a cabinet file in a installation package**

1.  Use a cabinet creation tool to compress the source files into a cabinet file. See [Cabinet Files](cabinet-files.md).
2.  The cabinet file must either be located in a data stream inside the .msi file or in a separate cabinet file located at the root of the source tree specified by the [Directory Table](directory-table.md).
3.  Determine whether the source is to be a compressed type or a mixed type that has both uncompressed and compressed files. See [Compressed and Uncompressed Sources](compressed-and-uncompressed-sources.md). Depending on the type of source image, set the compressed or uncompressed flag bits of the [**Word Count Summary**](word-count-summary.md) Property.
4.  Add a record to the [File table](file-table.md) for each of the files in the cabinet. Enter a file key in the File column that exactly matches the file key of the file in the cabinet. The file keys are case-sensitive. The file installation sequence in the File table and the cabinet must also be the same. The file sequence is specified by the sequence number in the Sequence column. To arrive at the sequence number for the first file in the cabinet, do the following. Find the existing record in the [Media table](media-table.md) having the greatest value in the DiskID column. The LastSequence field of this record gives the last file sequence number used on the media. In the File table, assign the first file of the new cabinet a sequence number that is greater than this. Assign sequence numbers to all of the remaining files in the same order as in the cabinet file. For a description of the remaining record fields, see [File table](file-table.md).
5.  Add a record to the [Media table](media-table.md) for the cabinet. Specify a value in the DiskID field of this new record that is greater than the largest DiskID value already existing in the table. Put the name of the cabinet into the Cabinet field. This name must be in the form of a [Cabinet](cabinet.md) data type. Prefix the name with a number sign "\#" if the cabinet is a data stream stored in the .msi file. Note that if the cabinet is a data stream, the name of the cabinet is case-sensitive. If the cabinet is a separate file, the name of the file is not case-sensitive.
6.  Determine the greatest file sequence number in the new cabinet by checking the Sequence column of the updated File table. Enter a value that is greater than this into the LastSequence field of the new record of the Media table. For a description of the remaining record fields, see [Media table](media-table.md).
7.  You can store the cabinet file in the installation package either by using a tool such as Msidb.exe or by using the installer's [Database Functions](database-functions.md). The following four steps explain how to add the cabinet from a program by using the database functions.
8.  To add the cabinet to the installation package from a program open a view on the [\_Streams table](-streams-table.md) of the database using [**MsiDatabaseOpenView**](/windows/desktop/api/Msiquery/nf-msiquery-msidatabaseopenviewa).
9.  Use [**MsiRecordSetString**](/windows/desktop/api/Msiquery/nf-msiquery-msirecordsetstringa) to set the Name column of the \_Streams table to the name appearing in the Cabinet column of the [Media table](media-table.md). Omit the number sign: \#.
10. Use [**MsiRecordSetStream**](/windows/desktop/api/Msiquery/nf-msiquery-msirecordsetstreama) to set the Data column of the \_Streams table to the cabinet's data.
11. Use [**MsiViewModify**](/windows/desktop/api/Msiquery/nf-msiquery-msiviewmodify) to update the record in the \_Streams table.
12. To use Msidb.exe to add the cabinet file Mycab.cab to the installation package named Mydatabase.msi, use the following command line: Msidb.exe -d mydatabase.msi -a mycab.cab. In this case, the Cabinet column of the Media table should contain the string: \#mycab.cab.

 

 



