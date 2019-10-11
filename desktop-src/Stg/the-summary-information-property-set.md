---
title: The Summary Information Property Set
description: COM defines a standard common property set for storing summary information about documents.
ms.assetid: 'ceed6d66-7327-4781-a5dc-9058e671138a'
ms.topic: article
ms.date: 05/31/2018
---

# The Summary Information Property Set

COM defines a standard common property set for storing summary information about documents. The Summary Information property set must be stored in a stream object. That is, this property set must be stored as a simple property set. For more information, see [Storage and Stream Objects for a Property Set](storage-vs--stream-for-a-property-set.md).

For example, to create an ANSI simple property set, you would call [**IPropertySetStorage::Create**](/windows/desktop/api/Propidl/nf-propidl-ipropertysetstorage-create) to create the property set, specifying **PROPSETFLAG\_ANSI** (simple is the default type of property set), then write to it with a call to [**IPropertyStorage::WriteMultiple**](/windows/desktop/api/Propidl/nf-propidl-ipropertystorage-writemultiple). To read the property set, you would call [**IPropertyStorage::ReadMultiple**](/windows/desktop/api/Propidl/nf-propidl-ipropertystorage-readmultiple).

All shared property sets are identified by a stream or storage name with the prefix "\\005" (or 0x05) to show that it is a property set that can be shared among applications. The Summary Information property set is no exception. The name of the stream that contains the Summary Information property set is: **"\\005SummaryInformation"**

It is not necessary to know the stream name of the property set when accessing it by means of the [**Create**](/windows/desktop/api/Propidl/nf-propidl-ipropertysetstorage-create) or [**Open**](/windows/desktop/api/Propidl/nf-propidl-ipropertysetstorage-open) methods of the [**IPropertySetStorage**](/windows/desktop/api/Propidl/nn-propidl-ipropertysetstorage) interface; in this case only the format identifier (FMTID) need be known. The FMTID for the Summary Information property set is: **F29F85E0-4FF9-1068-AB91-08002B27B3D9**

The declaration for this value is available in the header file as **FMTID\_SummaryInformation**. For more information, see the FMTIDS in the [Predefined Property Set Format Identifiers](predefined-property-set-format-identifiers.md).

The following table lists the string property names for the Summary Information property set, along with the respective property identifiers and variable type (VT) indicators. The names are not typically stored in the property set, but are inferred from the Property ID value. The Property ID String entries shown here correspond to definitions found in the header files.

| Name | Property ID string | Property ID | VT type |
|------|--------------------|-------------|---------|
| Title | PIDSI\_TITLE | 0x00000002 | VT\_LPSTR  |
| Subject | PIDSI\_SUBJECT | 0x00000003 | VT\_LPSTR |
| Author | PIDSI\_AUTHOR | 0x00000004 | VT\_LPSTR |
| Keywords | PIDSI\_KEYWORDS | 0x00000005 | VT\_LPSTR |
| Comments | PIDSI\_COMMENTS | 0x00000006 | VT\_LPSTR |
| Template | PIDSI\_TEMPLATE | 0x00000007 | VT\_LPSTR |
| Last Saved By | PIDSI\_LASTAUTHOR | 0x00000008 | VT\_LPSTR |
| Revision Number | PIDSI\_REVNUMBER | 0x00000009 | VT\_LPSTR |
| Total Editing Time | PIDSI\_EDITTIME | 0x0000000A | VT\_FILETIME (UTC) |
| Last Printed | PIDSI\_LASTPRINTED | 0x0000000B | VT\_FILETIME (UTC) |
| Create Time/Date (see note below) | PIDSI\_CREATE\_DTM | 0x0000000C | VT\_FILETIME (UTC) |
| Last saved Time/Date (see note below) | PIDSI\_LASTSAVE\_DTM | 0x0000000D | VT\_FILETIME (UTC) |
| Number of Pages | PIDSI\_PAGECOUNT | 0x0000000E | VT\_I4 |
| Number of Words | PIDSI\_WORDCOUNT | 0x0000000F | VT\_I4 |
| Number of Characters | PIDSI\_CHARCOUNT | 0x00000010 | VT\_I4 |
| Thumbnail | PIDSI\_THUMBNAIL | 0x00000011 | VT\_CF |
| Name of Creating Application | PIDSI\_APPNAME | 0x00000012 | VT\_LPSTR |
| Security | PIDSI\_SECURITY | 0x00000013 | VT\_I4 |

> [!NOTE]
> For **Create Time/Date** and **Last saved Time/Date**, some methods of file transfer, such as a download from a BBS, do not maintain the file system version of this information correctly.

## Related topics

<dl> <dt>

[Implementing the Summary Information Property Set](implementing-the-summary-information-property-set.md)
</dt> </dl>

 

 




