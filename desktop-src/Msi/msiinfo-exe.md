---
description: Msiinfo.exe is a command line utility that uses Database Functions and Installer Functions to edit or display the summary information stream of a database.
ms.assetid: 3f60146e-12bf-4755-bbca-93bb1c300fb7
title: Msiinfo.exe
ms.topic: article
ms.date: 05/31/2018
---

# Msiinfo.exe

Msiinfo.exe is a command line utility that uses [Database Functions](database-functions.md) and [Installer Functions](installer-functions.md) to edit or display the [summary information stream](summary-information-stream.md) of a database.

## Syntax

**MsiInfo** *{database}\[\[/B\] /D\]{option}{data}*

-   The database cannot be a read-only database.
-   If no data follows an option, the corresponding property is removed.
-   A maximum of 20 options may be specified on the command line. The same properties can be specified multiple times.
-   If the data contains a space, enclose the data with quote marks. For example, such as /T "MY TITLE".

## Command Line Options

Msiinfo.exe uses the following case-insensitive command line options. A slash delimiter may also be used in place of a dash. For more information see [Summary Information Stream Property Set](summary-information-stream-property-set.md).



| Option | Description                                                                                                                                                                                                                                                                                                                                                      | Property ID        | PID |
|--------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------|-----|
| *none* | If no options are specified, the utility displays the current values of the Summary Information properties.                                                                                                                                                                                                                                                      |                    |     |
| -b     | Display information about every string in the string pool. The -b option is only valid if -d is also used and -b must come before the -d option.                                                                                                                                                                                                                 |                    |     |
| -d     | Display information about the string pool. Validates the string pool and provides information about the codepage of the database. Note that the codepage of the database is different than the codepage of the Summary Information stream (PID\_CODEPAGE). This option also checks every string for characters that are invalid in the codepage of the database. |                    |     |
| -i     | Not applicable. Reserved.                                                                                                                                                                                                                                                                                                                                        | PID\_DICTIONARY    | 0   |
| -c     | Sets the [**Codepage Summary Property**](codepage-summary.md).                                                                                                                                                                                                                                                                                                  | PID\_CODEPAGE      | 1   |
| -t     | Sets the [**Title Summary Property**](title-summary.md).                                                                                                                                                                                                                                                                                                        | PID\_TITLE         | 2   |
| -j     | Sets the [**Subject Summary Property**](subject-summary.md).                                                                                                                                                                                                                                                                                                    | ID PID\_SUBJECT    | 3   |
| -a     | Sets the [**Author Summary Property**](author-summary.md).                                                                                                                                                                                                                                                                                                      | PID\_AUTHOR        | 4   |
| -k     | Sets the [**Keywords Summary Property**](keywords-summary.md).                                                                                                                                                                                                                                                                                                  | PID\_KEYWORDS      | 5   |
| -o     | Sets the [**Comments Summary Property**](comments-summary.md).                                                                                                                                                                                                                                                                                                  | PID\_COMMENTS      | 6   |
| -p     | Sets the [**Template Summary Property**](template-summary.md).                                                                                                                                                                                                                                                                                                  | PID\_TEMPLATE      | 7   |
| -l     | Sets the [**Last Saved By Summary Property**](last-saved-by-summary.md).                                                                                                                                                                                                                                                                                        | PID\_LASTAUTHOR    | 8   |
| -v     | Sets the [**Revision Number Summary Property**](revision-number-summary.md).                                                                                                                                                                                                                                                                                    | PID\_REVNUMBER     | 9   |
| -e     | Not applicable. Reserved.                                                                                                                                                                                                                                                                                                                                        | PID\_EDITTIME      | 10  |
| -s     | Sets the [**Last Printed Summary Property**](last-printed-summary.md). To specify the year, month, day, hour, minute, and second, use the format "yyyy/mm/dd hh:mm:ss." For example, "1997/06/20 03:25:59".                                                                                                                                                     | PID\_LASTPRINTED   | 11  |
| -r     | Sets the [**Create Time/Date Summary Property**](create-time-date-summary.md). To specify the year, month, day, hour, minute, and second, use the format "yyyy/mm/dd hh:mm:ss." For example, "1997/06/20 03:25:59".                                                                                                                                             | PID\_CREATE\_DTM   | 12  |
| -q     | Sets the [**Last Saved Time/Date Summary Property**](last-saved-time-date-summary.md). To specify the year, month, day, hour, minute, and second, use the format "yyyy/mm/dd hh:mm:ss." For example, "1997/06/20 03:25:59".                                                                                                                                     | PID\_LASTSAVE\_DTM | 13  |
| -g     | Sets the [**Page Count Summary Property**](page-count-summary.md).                                                                                                                                                                                                                                                                                              | PID\_PAGECOUNT     | 14  |
| -w     | Sets the [**Word Count Summary Property**](word-count-summary.md).                                                                                                                                                                                                                                                                                              | PID\_WORDCOUNT     | 15  |
| -h     | Sets the [**Character Count Summary Property**](character-count-summary.md).                                                                                                                                                                                                                                                                                    | PID\_CHARCOUNT     | 16  |
|        | Not applicable. Reserved.                                                                                                                                                                                                                                                                                                                                        | PID\_THUMBNAIL     | 17  |
| -n     | Sets the [**Creating Application Summary Property**](creating-application-summary.md).                                                                                                                                                                                                                                                                          | PID\_APPNAME       | 18  |
| -u     | Sets the [**Security Summary Property**](security-summary.md).                                                                                                                                                                                                                                                                                                  | PID\_SECURITY      | 19  |



 

This tool is only available in the [Windows SDK Components for Windows Installer Developers](platform-sdk-components-for-windows-installer-developers.md).

## Related topics

<dl> <dt>

[Windows Installer Development Tools](windows-installer-development-tools.md)
</dt> <dt>

[Released Versions, Tools, and Redistributables](released-versions-tools-and-redistributables.md)
</dt> </dl>

 

 



