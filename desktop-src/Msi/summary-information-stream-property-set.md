---
description: The following table shows the summary information stream property set, which includes the properties, their corresponding property IDs, PIDs, and types.
ms.assetid: a5dd014f-21af-41f9-be75-1b139946179d
title: Summary Information Stream Property Set
ms.topic: article
ms.date: 05/31/2018
---

# Summary Information Stream Property Set

The following table shows the summary information stream property set, which includes the properties, their corresponding property IDs, PIDs, and types. For more information about how the installer uses these properties, see [Summary Property Descriptions](summary-property-descriptions.md). For information about the Window Installer functions that are used to configure the summary information properties, see [Using the Summary Information Stream](using-the-summary-information-stream.md).



| Property name                                                | Property ID        | PID | Type         |
|--------------------------------------------------------------|--------------------|-----|--------------|
| [**Codepage**](codepage-summary.md)                         | PID\_CODEPAGE      | 1   | VT\_I2       |
| [**Title**](title-summary.md)                               | PID\_TITLE         | 2   | VT\_LPSTR    |
| [**Subject**](subject-summary.md)                           | PID\_SUBJECT       | 3   | VT\_LPSTR    |
| [**Author**](author-summary.md)                             | PID\_AUTHOR        | 4   | VT\_LPSTR    |
| [**Keywords**](keywords-summary.md)                         | PID\_KEYWORDS      | 5   | VT\_LPSTR    |
| [**Comments**](comments-summary.md)                         | PID\_COMMENTS      | 6   | VT\_LPSTR    |
| [**Template**](template-summary.md)                         | PID\_TEMPLATE      | 7   | VT\_LPSTR    |
| [**Last Saved By**](last-saved-by-summary.md)               | PID\_LASTAUTHOR    | 8   | VT\_LPSTR    |
| [**Revision Number**](revision-number-summary.md)           | PID\_REVNUMBER     | 9   | VT\_LPSTR    |
| [**Last Printed**](last-printed-summary.md)                 | PID\_LASTPRINTED   | 11  | VT\_FILETIME |
| [**Create Time/Date**](create-time-date-summary.md)         | PID\_CREATE\_DTM   | 12  | VT\_FILETIME |
| [**Last Save Time/Date**](last-saved-time-date-summary.md)  | PID\_LASTSAVE\_DTM | 13  | VT\_FILETIME |
| [**Page Count**](page-count-summary.md)                     | PID\_PAGECOUNT     | 14  | VT\_I4       |
| [**Word Count**](word-count-summary.md)                     | PID\_WORDCOUNT     | 15  | VT\_I4       |
| [**Character Count**](character-count-summary.md)           | PID\_CHARCOUNT     | 16  | VT\_I4       |
| [**Creating Application**](creating-application-summary.md) | PID\_APPNAME       | 18  | VT\_LPSTR    |
| [**Security**](security-summary.md)                         | PID\_SECURITY      | 19  | VT\_I4       |



 

The installer currently maintains three storage formats for installation packages, transforms, and patch packages. The CLSID for the storage is set to the appropriate format class for the particular format, independent of the summary information for the storage.

 

 



