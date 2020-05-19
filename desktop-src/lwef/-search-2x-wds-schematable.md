---
title: Schema (Legacy Windows Environment Features)
description: The schema documents the values and properties that the index uses to store data for indexing or sorting.
ms.assetid: dfd8862c-8f84-441e-a4b4-4af3c76c48f9
ms.topic: article
ms.date: 05/31/2018
---

# Schema

> [!NOTE]
> Windows Desktop Search 2.x is an obsolete technology that was originally available as an add-in for Windows XP and Windows Server 2003. On later releases, use [Windows Search](../search/-search-3x-wds-overview.md) instead.

The schema documents the values and properties that the index uses to store data for indexing or sorting. The Schema table lists the columns and their properties (type and propid) included in the schema for Microsoft Windows Desktop Search (WDS) 2.6.5.

## Schema



| Column Name                  | Description                                                                                                             | Propid                                                            |
|------------------------------|-------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------|
| DocComments                  | Comments                                                                                                                | F29F85E0-4FF9-1068-AB91-08002B27B3D9/6                            |
| Create                       | Date and time the file was created                                                                                      | B725F130-47EF-101A-A5F1-02608C9EEBAC/15                           |
| DisplayFolder                | User-friendly folder for item                                                                                           | D5CDD505-2E9C-101B-9397-08002B2CF9AE/DisplayFolder                |
| DocAuthor                    | Author of the document                                                                                                  | F29F85E0-4FF9-1068-AB91-08002B27B3D9/4                            |
| DocCategory                  | Category                                                                                                                | D5CDD502-2E9C-101B-9397-08002B2CF9AE/2                            |
| DocKeywords                  | Keywords                                                                                                                | F29F85E0-4FF9-1068-AB91-08002B27B3D9/5                            |
| DocTitlePrefix               | Prefix of subject (Re:, Fw:, etc.)                                                                                      | D5CDD505-2E9C-101B-9397-08002B2CF9AE/DocTitlePrefix               |
| DocTitle                     | Title                                                                                                                   | F29F85E0-4FF9-1068-AB91-08002B27B3D9/2                            |
| FileExtDesc                  | User-friendly description of the file type from the registry (Ex: .psq --> Product Studio Query File)                | D5CDD505-2E9C-101B-9397-08002B2CF9AE/FileExtDesc                  |
| FolderName                   | Name of the parent folder                                                                                               | D5CDD505-2E9C-101B-9397-08002B2CF9AE/FolderName                   |
| IsAttachment                 | Indicates item is an attachment                                                                                         | D5CDD505-2E9C-101B-9397-08002B2CF9AE/IsAttachment                 |
| IsDeleted                    | Indicates item is marked for deletion (Recycle bin, deleted items, etc.)                                                | D5CDD505-2E9C-101B-9397-08002B2CF9AE/IsDeleted                    |
| LastViewed                   | Date the item was last viewed by user                                                                                   | D5CDD505-2E9C-101B-9397-08002B2CF9AE/LastViewed                   |
| People                       | People involved with this item                                                                                          | D5CDD505-2E9C-101B-9397-08002B2CF9AE/People                       |
| PerceivedType                | PerceivedType of the object NOTE: This is only for retrieval.                                                           | D5CDD505-2E9C-101B-9397-08002B2CF9AE/PerceivedType                |
| PerceivedTypeName            | Display name of the PerceivedType.  Never displayed or queried                                                          | D5CDD505-2E9C-101B-9397-08002B2CF9AE/PerceivedTypeName            |
| PrimaryDate                  | Most interesting date (Last write time for files, date received for email)                                              | D5CDD505-2E9C-101B-9397-08002B2CF9AE/PrimaryDate                  |
| Size                         | Size of a file.                                                                                                         | B725F130-47EF-101A-A5F1-02608C9EEBAC/12                           |
| DocSubject                   | Subject of file. NOTE: Currently, email subjects map to PrimaryTitle today and don't get duplicated due to their length | F29F85E0-4FF9-1068-AB91-08002B27B3D9/3                            |
| URL                          | Query-based URL                                                                                                         | 49691C90-7E17-101A-A91C-08002B2ECDA9/9                            |
| Write                        | Date and time of the last write to the file                                                                             | B725F130-47EF-101A-A5F1-02608C9EEBAC/14                           |
| DueDate                      | Date an item is due                                                                                                     | D5CDD505-2E9C-101B-9397-08002B2CF9AE/DueDate                      |
| IsIncomplete                 | Indicates item is not fully available                                                                                   | D5CDD505-2E9C-101B-9397-08002B2CF9AE/IsIncomplete                 |
| IsFlaggedCompleted           | Indicates item is flagged as completed                                                                                  | D5CDD505-2E9C-101B-9397-08002B2CF9AE/IsFlaggedCompleted           |
| IsFlagged                    | Indicates item is flagged                                                                                               | D5CDD505-2E9C-101B-9397-08002B2CF9AE/IsFlagged                    |
| FlagText                     | Text displayed for the flag, e.g., Review, Follow up, etc.                                                              | D5CDD505-2E9C-101B-9397-08002B2CF9AE/FlagText                     |
| Identity                     | Identity for OE users                                                                                                   | D5CDD505-2E9C-101B-9397-08002B2CF9AE/Identity                     |
| IsRead                       | Indicates item has been read                                                                                            | D5CDD505-2E9C-101B-9397-08002B2CF9AE/IsRead                       |
| Importance                   | MAPI importance or priority                                                                                             | D5CDD505-2E9C-101B-9397-08002B2CF9AE/Importance                   |
| ContainerHash                | Hash code that identifies attachments to be deleted based on a common container URL                                     | D5CDD505-2E9C-101B-9397-08002B2CF9AE/ContainerHash                |
| DocFormat                    | Document format or MIMETYPE (for example 'message/rfc822' for an EML file)                                              | 0B63E350-9CCC-11D0-BCDB-00805FCCCE04/5                            |
| GatherTimeModified           | Time the indexer last crawled the document for catalog update                                                           | 0b63e350-9ccc-11d0-bcdb-00805fccce04/4                            |
| Store                        | The store or protocol handler (FILE, MAIL, OUTLOOKEXPRESS)                                                              | D5CDD505-2E9C-101B-9397-08002B2CF9AE/Store                        |
| FileExt                      | File extension                                                                                                          | D5CDD505-2E9C-101B-9397-08002B2CF9AE/FileExt                      |
| FileName                     | Name of the file                                                                                                        | B725F130-47EF-101A-A5F1-02608C9EEBAC/10                           |
| ShortName                    | Short (8.3) file name for the file                                                                                      | B725F130-47EF-101A-A5F1-02608C9EEBAC/20                           |
| AttachmentNames              | Names of attachments in a message                                                                                       | D5CDD505-2E9C-101B-9397-08002B2CF9AE/AttachmentNames              |
| BccAddress                   | Addresses in Bcc: field                                                                                                 | D5CDD505-2E9C-101B-9397-08002B2CF9AE/BccAddress                   |
| BccName                      | Person names in Bcc: field                                                                                              | D5CDD505-2E9C-101B-9397-08002B2CF9AE/BccName                      |
| CcAddress                    | Addresses in Cc: field                                                                                                  | D5CDD505-2E9C-101B-9397-08002B2CF9AE/CcAddress                    |
| CcName                       | Person names in Cc: field                                                                                               | D5CDD505-2E9C-101B-9397-08002B2CF9AE/CcName                       |
| ConversationID               | Unique ID for a conversation in email threads                                                                           | D5CDD505-2E9C-101B-9397-08002B2CF9AE/ConversationID               |
| FromAddress                  | Addresses in From: field                                                                                                | D5CDD505-2E9C-101B-9397-08002B2CF9AE/FromAddress                  |
| FromName                     | Person name in From: field                                                                                              | D5CDD505-2E9C-101B-9397-08002B2CF9AE/FromName                     |
| FwdRply                      | Indicates mail was replied to or forwarded (cdoPR\_ACTION=261 262)                                                      | D5CDD505-2E9C-101B-9397-08002B2CF9AE/FwdRply                      |
| HasAttach                    | Indicates mail has an attachment (T or F)                                                                               | D5CDD505-2E9C-101B-9397-08002B2CF9AE/HasAttach                    |
| ReceivedDate                 | Delivery time                                                                                                           | D5CDD505-2E9C-101B-9397-08002B2CF9AE/ReceivedDate                 |
| ToAddress                    | Addresses in To: field                                                                                                  | D5CDD505-2E9C-101B-9397-08002B2CF9AE/ToAddress                    |
| ToName                       | Person names in To: field                                                                                               | D5CDD505-2E9C-101B-9397-08002B2CF9AE/ToName                       |
| TaskStatus                   | Status of a task                                                                                                        | D5CDD505-2E9C-101B-9397-08002B2CF9AE/TaskStatus                   |
| EndDate                      | End time (usually for meetings/events)                                                                                  | D5CDD505-2E9C-101B-9397-08002B2CF9AE/EndDate                      |
| IsRecurring                  | Indicates item is recurring (e.g., meetings)                                                                            | D5CDD505-2E9C-101B-9397-08002B2CF9AE/IsRecurring                  |
| StartDate                    | Start time (usually for meetings/events)                                                                                | D5CDD505-2E9C-101B-9397-08002B2CF9AE/StartDate                    |
| Duration                     | Length of meeting in minutes                                                                                            | D5CDD505-2E9C-101B-9397-08002B2CF9AE/Duration                     |
| Location                     | Location where item (like a meeting) occurs                                                                             | D5CDD505-2E9C-101B-9397-08002B2CF9AE/Location                     |
| Anniversary                  | Anniversary date                                                                                                        | D5CDD505-2E9C-101B-9397-08002B2CF9AE/Anniversary                  |
| AssistantName                | Assistant name                                                                                                          | D5CDD505-2E9C-101B-9397-08002B2CF9AE/AssistantName                |
| AssistantTelephone           | Assistant telephone                                                                                                     | D5CDD505-2E9C-101B-9397-08002B2CF9AE/AssistantTelephone           |
| Birthday                     | Birthday of contact                                                                                                     | D5CDD505-2E9C-101B-9397-08002B2CF9AE/Birthday                     |
| BusinessAddressCity          | Business address info                                                                                                   | D5CDD505-2E9C-101B-9397-08002B2CF9AE/BusinessAddressCity          |
| BusinessAddressPostalCode    | Business address info                                                                                                   | D5CDD505-2E9C-101B-9397-08002B2CF9AE/BusinessAddressPostalCode    |
| BusinessAddressPostOfficeBox | Business address info                                                                                                   | D5CDD505-2E9C-101B-9397-08002B2CF9AE/BusinessAddressPostOfficeBox |
| BusinessAddressState         | Business address info                                                                                                   | D5CDD505-2E9C-101B-9397-08002B2CF9AE/BusinessAddressState         |
| BusinessAddressStreet        | Business address info                                                                                                   | D5CDD505-2E9C-101B-9397-08002B2CF9AE/BusinessAddressStreet        |
| BusinessAddressCountry       | Business address info                                                                                                   | D5CDD505-2E9C-101B-9397-08002B2CF9AE/BusinessAddressCountry       |
| CallbackTelephone            | Call back telephone info                                                                                                | D5CDD505-2E9C-101B-9397-08002B2CF9AE/CallbackTelephone            |
| CarTelephone                 | Telephone info                                                                                                          | D5CDD505-2E9C-101B-9397-08002B2CF9AE/CarTelephone                 |
| Children                     | Children's names for contact                                                                                            | D5CDD505-2E9C-101B-9397-08002B2CF9AE/Children                     |
| CompanyMainTelephone         | Telephone info                                                                                                          | D5CDD505-2E9C-101B-9397-08002B2CF9AE/CompanyMainTelephone         |
| EmailAddress                 | Contact email name                                                                                                      | D5CDD505-2E9C-101B-9397-08002B2CF9AE/EmailAddress                 |
| EmailName                    | Display name for email address                                                                                          | D5CDD505-2E9C-101B-9397-08002B2CF9AE/EmailName                    |
| FirstName                    | Contact's first name                                                                                                    | D5CDD505-2E9C-101B-9397-08002B2CF9AE/FirstName                    |
| FullName                     | Contact's full name                                                                                                     | D5CDD505-2E9C-101B-9397-08002B2CF9AE/FullName                     |
| Gender                       | Male/female/other                                                                                                       | D5CDD505-2E9C-101B-9397-08002B2CF9AE/Gender                       |
| Hobby                        | Contact info                                                                                                            | D5CDD505-2E9C-101B-9397-08002B2CF9AE/Hobby                        |
| HomeAddressCity              | Home address info                                                                                                       | D5CDD505-2E9C-101B-9397-08002B2CF9AE/HomeAddressCity              |
| HomeAddressCountry           | Home address info                                                                                                       | D5CDD505-2E9C-101B-9397-08002B2CF9AE/HomeAddressCountry           |
| HomeAddressPostalCode        | Home address info                                                                                                       | D5CDD505-2E9C-101B-9397-08002B2CF9AE/HomeAddressPostalCode        |
| HomeAddressState             | Home address info                                                                                                       | D5CDD505-2E9C-101B-9397-08002B2CF9AE/HomeAddressState             |
| HomeAddressStreet            | Home address info                                                                                                       | D5CDD505-2E9C-101B-9397-08002B2CF9AE/HomeAddressStreet            |
| HomeFaxNumber                | Facsimile info                                                                                                          | D5CDD505-2E9C-101B-9397-08002B2CF9AE/HomeFaxNumber                |
| BusinessFaxNumber            | Facsimile info                                                                                                          | D5CDD505-2E9C-101B-9397-08002B2CF9AE/BusinessFaxNumber            |
| HomeTelephone                | Telephone info                                                                                                          | D5CDD505-2E9C-101B-9397-08002B2CF9AE/HomeTelephone                |
| IMAddress                    | Instant message info                                                                                                    | D5CDD505-2E9C-101B-9397-08002B2CF9AE/IMAddress                    |
| JobTitle                     | Contact's job title                                                                                                     | D5CDD505-2E9C-101B-9397-08002B2CF9AE/JobTitle                     |
| MiddleName                   | Contact info                                                                                                            | D5CDD505-2E9C-101B-9397-08002B2CF9AE/MiddleName                   |
| MobileTelephone              | Telephone info                                                                                                          | D5CDD505-2E9C-101B-9397-08002B2CF9AE/MobileTelephone              |
| NickName                     | Contact info                                                                                                            | D5CDD505-2E9C-101B-9397-08002B2CF9AE/NickName                     |
| Office                       | Contact info                                                                                                            | D5CDD505-2E9C-101B-9397-08002B2CF9AE/Office                       |
| OfficeTelephone              | Telephone info                                                                                                          | D5CDD505-2E9C-101B-9397-08002B2CF9AE/OfficeTelephone              |
| PagerTelephone               | Telephone info                                                                                                          | D5CDD505-2E9C-101B-9397-08002B2CF9AE/PagerTelephone               |
| LastName                     | Contact info                                                                                                            | D5CDD505-2E9C-101B-9397-08002B2CF9AE/LastName                     |
| PersonalTitle                | Profession title (Dr., Mr., Mrs., Ms.)                                                                                  | D5CDD505-2E9C-101B-9397-08002B2CF9AE/PersonalTitle                |
| PrimaryTelephone             | Telephone info                                                                                                          | D5CDD505-2E9C-101B-9397-08002B2CF9AE/PrimaryTelephone             |
| Profession                   | Contact info                                                                                                            | D5CDD505-2E9C-101B-9397-08002B2CF9AE/Profession                   |
| Spouse                       | Contact info                                                                                                            | D5CDD505-2E9C-101B-9397-08002B2CF9AE/Spouse                       |
| Suffix                       | Contact info                                                                                                            | D5CDD505-2E9C-101B-9397-08002B2CF9AE/Suffix                       |
| TelexNumber                  | Telex info                                                                                                              | D5CDD505-2E9C-101B-9397-08002B2CF9AE/TelexNumber                  |
| TTYTDDTelephone              | TTY/TDD info                                                                                                            | D5CDD505-2E9C-101B-9397-08002B2CF9AE/TTYTDDTelephone              |
| WebPage                      | Contact web page                                                                                                        | D5CDD505-2E9C-101B-9397-08002B2CF9AE/WebPage                      |
| DocCompany                   | Company                                                                                                                 | D5CDD502-2E9C-101B-9397-08002B2CF9AE/15                           |
| DocLastAuthor                | User the doc wa last saved by                                                                                           | F29F85E0-4FF9-1068-AB91-08002B27B3D9/8                            |
| DocLastPrinted               | Last Printed                                                                                                            | F29F85E0-4FF9-1068-AB91-08002B27B3D9/11                           |
| DocManager                   | Manager                                                                                                                 | D5CDD502-2E9C-101B-9397-08002B2CF9AE/14                           |
| DocPresentationFormat        | PresentationTarget                                                                                                      | D5CDD502-2E9C-101B-9397-08002B2CF9AE/3                            |
| DocSlideCount                | Slides                                                                                                                  | D5CDD502-2E9C-101B-9397-08002B2CF9AE/7                            |
| AudioAvgDataRate             | Average data rate in Kbps for the audio file                                                                            | 64440490-4C8B-11D1-8B70-080036B11A03/4                            |
| AudioTimeLength              | Length in milliseconds of the audio file                                                                                | 56A3372E-CE9C-11D2-9F0E-006097C686F6/8                            |
| MusicAlbum                   | Album name                                                                                                              | 56A3372E-CE9C-11D2-9F0E-006097C686F6/4                            |
| MusicArtist                  | Name of the artist                                                                                                      | 56A3372E-CE9C-11D2-9F0E-006097C686F6/2                            |
| MusicGenre                   | Genre of the album                                                                                                      | 56A3372E-CE9C-11D2-9F0E-006097C686F6/11                           |
| MusicTrack                   | Number of tracks in the album                                                                                           | 56A3372E-CE9C-11D2-9F0E-006097C686F6/7                            |
| MusicYear                    | Year in which the album was recorded                                                                                    | 56A3372E-CE9C-11D2-9F0E-006097C686F6/5                            |
| ExifCameraMake               | Manufacturer of camera                                                                                                  | 14B81DA1-0135-4D31-96D9-6CBFC9671A99/271                          |
| ExifCameraModel              | Model of camera                                                                                                         | 14B81DA1-0135-4D31-96D9-6CBFC9671A99/272                          |
| DateTaken                    | FILETIME of data taken                                                                                                  | D5CDD505-2E9C-101B-9397-08002B2CF9AE/DateTaken                    |
| ExifOrientation              | Orientation                                                                                                             | 14B81DA1-0135-4D31-96D9-6CBFC9671A99/274                          |
| ImageDimensions              | Dimensions of the image                                                                                                 | 6444048F-4C8B-11D1-8B70-080036B11A03/13                           |
| ImageResX                    | X resolution for the image                                                                                              | 6444048F-4C8B-11D1-8B70-080036B11A03/5                            |
| ImageResY                    | Y resolution for the image                                                                                              | 6444048F-4C8B-11D1-8B70-080036B11A03/6                            |
| VideoFrameHeight             | Frame height for the video stream                                                                                       | 64440491-4C8B-11D1-8B70-080036B11A03/4                            |
| VideoFrameRate               | Frame rate in frames per millisecond for the video stream                                                               | 64440491-4C8B-11D1-8B70-080036B11A03/6                            |
| VideoFrameWidth              | Frame width for the video stream                                                                                        | 64440491-4C8B-11D1-8B70-080036B11A03/3                            |
| Class                        | Class name                                                                                                              | 8dee0300-16c2-101b-b121-08002b2ecda9/class                        |
| Function                     | Function name                                                                                                           | 8dee0300-16c2-101b-b121-08002b2ecda9/func                         |
| Struct                       | Structure name                                                                                                          | 8dee0300-16c2-101b-b121-08002b2ecda9/struct                       |
| Interface                    | Interface name                                                                                                          | 8dee0300-16c2-101b-b121-08002b2ecda9/interface                    |
| Delegate                     | Delegate name                                                                                                           | 8dee0300-16c2-101b-b121-08002b2ecda9/delegate                     |
| Property                     | Property name                                                                                                           | 8dee0300-16c2-101b-b121-08002b2ecda9/property                     |
| Enum                         | Enum name                                                                                                               | 8dee0300-16c2-101b-b121-08002b2ecda9/enum                         |
| Const                        | Const name                                                                                                              | 8dee0300-16c2-101b-b121-08002b2ecda9/const                        |
| Event                        | Event name                                                                                                              | 8dee0300-16c2-101b-b121-08002b2ecda9/event                        |
| Field                        | Field name                                                                                                              | 8dee0300-16c2-101b-b121-08002b2ecda9/field                        |
| Define                       | Define name                                                                                                             | 8dee0300-16c2-101b-b121-08002b2ecda9/def                          |
| Component                    | Component name                                                                                                          | 8dee0300-16c2-101b-b121-08002b2ecda9/component                    |
| Project                      | Project name                                                                                                            | 8dee0300-16c2-101b-b121-08002b2ecda9/project                      |
| Solution                     | Solution name                                                                                                           | 8dee0300-16c2-101b-b121-08002b2ecda9/solution                     |



 

## Related topics

<dl> <dt>

**Reference**
</dt> <dt>

[Developing IFilter Add-ins](-search-2x-wds-ifilteraddins.md)
</dt> <dt>

[Developing Protocol Handlers](-search-2x-wds-phaddins.md)
</dt> <dt>

[Advanced Query Syntax](-search-2x-wds-aqsreference.md)
</dt> <dt>

[Perceived Types](-search-2x-wds-perceivedtype.md)
</dt> </dl>

 

 




