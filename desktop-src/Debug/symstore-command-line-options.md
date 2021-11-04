---
description: The following syntax forms are supported for SymStore transactions. The first parameter must always be add or del. The order of the other parameters does not matter.
ms.assetid: d6d10adb-cb17-4ce3-b0e5-493b313ebdba
title: SymStore Command-Line Options
ms.topic: article
ms.date: 05/31/2018
---

# SymStore Command-Line Options

The following syntax forms are supported for SymStore transactions. The first parameter must always be add or del. The order of the other parameters does not matter.

**symstore add** \[**/l** **/o** **/p** **/r** **/compress**\] \[**-:MSG** *Message*\] \[**-:REL**\] \[**-:NOREFS**\] **/f** *File* **/s** *Store* **/t** *Product* \[**/v** *Version*\] \[**/c** *Comment*\] \[**/d** *LogFile*\]

**symstore add** \[**/a** **/l** **/o** **/p** **/r**\] \[**-:REL**\] \[**-:NOREFS**\] **/g** *Share* **/f** *File* **/x** *IndexFile* \[**/d** *LogFile*\]

**symstore add** \[**/o** **/compress**\] \[ **/p** \[**-:MSG** \|*Message*\] \[**-:REL**\] \[**-:NOREFS**\]\] **/y** *IndexFile* **/g** *Share* **/s** *Store* **/t** *Product* \[**/v** *Version*\] \[**/c** *Comment*\] \[**/d** *LogFile*\]

**symstore query** \[**/o** **/r**\] **/f** *File* **/s** *Store* \[**/d** *LogFile*\]

**symstore del** **/i** *ID* **/s** *Store* \[**/o**\] \[**/d** *LogFile*\]

**symstore** **/?**



| Parameter      | Meaning                                                                                                                                                                                                                                                                                                                                                                                                      |
|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| /a             | Causes SymStore to append new indexing information to an existing index file. (This option is only used with the /x option.)                                                                                                                                                                                                                                                                                 |
| /c *Comment*   | Specifies a comment for the transaction.                                                                                                                                                                                                                                                                                                                                                                     |
| /compress      | Causes SymStore to create a compressed version of each file copied to the symbol store instead of using an uncompressed copy of the file. This option is only valid when storing files and not pointers, and cannot be used with the /p option.                                                                                                                                                              |
| /d *LogFile*   | Specifies a log file to be used for command output. If this is not included, transaction information and other output is sent to stdout.                                                                                                                                                                                                                                                                     |
| /f *File*      | Specifies one or more file paths (or directories) to add. If a specified file path begins with an '@' symbol, a [response file](../midl/response-files.md) containing a list of files to be added (one file path per line) is expected.                                                                                                                                             |
| /g *Share*     | Specifies the server and share where the symbol files were originally stored. When used with /f, *Share* should be identical to the beginning of the *File* specifier. When used with /y, *Share* should be the location of the original symbol files (not the index file). This allows you to later change this portion of the file path in case you move the symbol files to a different server and share. |
| /i *ID*        | Specifies the transaction ID string.                                                                                                                                                                                                                                                                                                                                                                         |
| /l             | Allows the file to be in a local directory rather than a network path. (This option is only used with the /p option.)                                                                                                                                                                                                                                                                                        |
| /o             | Causes SymStore to display verbose output.                                                                                                                                                                                                                                                                                                                                                                   |
| /p             | Causes SymStore to store a pointer to the file, rather than the file itself.                                                                                                                                                                                                                                                                                                                                 |
| /r             | Causes SymStore to add files or directories recursively.                                                                                                                                                                                                                                                                                                                                                     |
| /s *Store*     | Specifies the root directory for the symbol store.                                                                                                                                                                                                                                                                                                                                                           |
| /t *Product*   | Specifies the name of the product.                                                                                                                                                                                                                                                                                                                                                                           |
| /v *Version*   | Specifies the version of the product.                                                                                                                                                                                                                                                                                                                                                                        |
| /x *IndexFile* | Causes SymStore not to store the actual symbol files. Instead, SymStore records information in the *IndexFile* that will enable SymStore to access the symbol files at a later time.                                                                                                                                                                                                                         |
| /y *IndexFile* | Causes SymStore to read the data from a file created with /x.                                                                                                                                                                                                                                                                                                                                                |
| -:MSG Message  | Adds the specified Message to each file. (This option can only be used when /p is used.)                                                                                                                                                                                                                                                                                                                     |
| -:REL          | Allows the paths in the file pointers to be relative. This option implies the /l option. (This option can only be used when /p is used.)                                                                                                                                                                                                                                                                     |
| -:NOREFS       | Omits the creation of reference pointer files for the files and pointers being stored. This option is only valid during the initial creation of a symbol store if the store being changed was created with this option.                                                                                                                                                                                      |
| /?             | Displays help text for the SymStore command.                                                                                                                                                                                                                                                                                                                                                                 |



 

 

 



