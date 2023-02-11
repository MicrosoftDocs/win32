---
title: Advanced Query Syntax
description: Advanced Query Syntax (AQS) is used by Microsoft Windows Desktop Search (WDS) to help users and programmers better define and narrow their searches.
ms.assetid: 8e55bd40-c7cf-44a6-bc18-24bc7a267779
ms.topic: article
ms.date: 02/10/2023
---

# Advanced Query Syntax

> [!NOTE]
> Windows Desktop Search 2.x is an obsolete technology that was originally available as an add-in for Windows XP and Windows Server 2003. On later releases, use [Windows Search](../search/-search-3x-wds-overview.md) instead.

Advanced Query Syntax (AQS) is used by Microsoft Windows Desktop Search (WDS) to help users and programmers better define and narrow their searches. Using AQS is an easy way to deliver more meaningful result sets. Searches can be narrowed by the following parameters:

- File kinds: Folders, documents, presentations, pictures, and so on.
- File stores: Specific databases and locations.
- File properties: File metadata, such as size, date, and title.
- File contents: Keywords like *project deliverables*, *AQS*, *blue suede shoes*, and so on.

Furthermore, you can combine search parameters by using search operators. The remainder of this section explains query syntax, parameters and operators, and how they can be combined to offer targeted search results. The tables describe the syntax to use with WDS, and the properties that can be queried for each file kind displayed in the **Windows Desktop Search** results window.

## Desktop search syntax

A search query can include one or more keywords, with Boolean operators and optional criteria. You can use these optional criteria to refine a search with the following syntax:

- `<scope name>:<value>`: Scope or data store in which files reside
- `<file kind>:<value>`: Kinds of files
- `<property name>:<value>`: Managed properties of files

Suppose a user wants to search for a document containing the phrase *last quarter*, created by John or Joanne, and saved to the folder *mydocuments*. The query might look like this:

`"last quarter" author:(john OR joanne) foldername:mydocuments`

### Scope: Locations and data stores

Users can limit the scope of their searches to specific folder locations or data stores. For example, if you use several email accounts, and you want to limit a query to either Microsoft Outlook or Microsoft Outlook Express, you can use `store:outlook` or `store:oe` respectively.

| Location or file store        | AQS Keyword      | Example                                  |
|-------------------------------|------------------|------------------------------------------|
| Desktop                       | desktop          | store:desktop                            |
| Files                         | files            | store:files                              |
| Outlook                       | outlook          | store:outlook                            |
| Outlook Express               | oe               | store:oe                                 |
| Specific folder               | foldername or in | foldername:MyDocuments or in:MyDocuments |

If you have a protocol handler in place to crawl custom stores, like Lotus Notes, you can use the name of the store or protocol handler for the store. For example, if you implemented a protocol handler to include a Lotus Notes data store as "notes," the query syntax would be `store:notes`.

### Common file types

Users can also limit their searches to specific types of files, called file kinds. The following table lists the file kinds and offers examples of the AQS syntax used to search for these kinds of files.

| File type to search             | AQS Keyword      | Example                        |
|---------------------------------|------------------|--------------------------------|
| All file types                  | everything       | kind:everything                |
| Communications                  | communications   | kind:communications            |
| Contacts                        | contacts         | kind:contacts                  |
| E-mail                          | email            | kind:email                     |
| Instant Messenger conversations | im               | kind:im                        |
| Meetings                        | meetings         | kind:meetings                  |
| Tasks                           | tasks            | kind:tasks                     |
| Notes                           | notes            | kind:notes                     |
| Documents                       | docs             | kind:docs                      |
| Text documents                  | text             | kind:text                      |
| Spreadsheets                    | spreadsheets     | kind:spreadsheets              |
| Presentations                   | presentations    | kind:presentations             |
| Music                           | music            | kind:music                     |
| Pictures                        | pics             | kind:pics                      |
| Videos                          | videos           | kind:videos                    |
| Folders                         | folders          | kind:folders                   |
| Folder name                     | foldername or in | foldername:mydocs or in:mydocs |
| Favorites                       | favorites        | kind:favorites                 |
| Programs                        | programs         | kind:programs                  |

### Boolean operators

Users can combine search keywords and file properties with operators to broaden or narrow a search. The following table describes common search query operators.

| Operator  | Example | Result |
|-----------------|----------|----------|
| NOT             | social NOT security | Finds items that contain *social*, but not *security*. |
| Space           | social  security    | Finds items that contain *social* and *security*. |
| OR              | social OR security  | Finds items that contain *social* or *security*. |
| Quotation marks | "social security"   | Finds items that contain the exact phrase *social security*. |
| Parentheses     | (social security)   | Finds items that contain *social* and *security* in any order. |
| >               | date:>11/13/21<br/> size:>500<br/>  | Finds items with a date after MM/DD/YY. <br/> Finds items with a size greater than 500 bytes.<br/> |
| <               | date:<11/13/21 <br/> size:<500<br/> | Finds items with a date before MM/DD/YY. <br/> Finds items with a size less than 500 bytes.<br/> |
| ..              | date:11/13/21..11/15/21 | Finds items with a date beginning on MM/DD/YY and ending on MM/DD/YY. |

> [!NOTE]
> The operators **NOT** and **OR** must be in uppercase and can't be combined in the same query. For example, `social OR security NOT retirement` is not allowed.

### Boolean properties

Some file types let users search for files by using Boolean properties, as described in the following table.

| Property | Example | Result |
|---|---|---|
| is:attachment  | report is:attachment      | Finds items that have attachments that contain *report*. Same as `isattachment:true`.                           |
| isonline:      | report isonline:true      | Finds items that are online and which contain *report*.                                                         |
| isrecurring:   | report isrecurring:true   | Finds items that are recurring and which contain *report*.                                                       |
| isflagged:     | report isflagged:true     | Finds items that are flagged (for example, Review, Follow up) and which contain *report*.                       |
| isdeleted:     | report isdeleted:true     | Finds items that are flagged as deleted (for example, moved to the Recycle Bin or deleted items) and which contain *report*. |
| iscompleted:   | report iscompleted:false  | Finds items that are not flagged as complete and which contain *report*.                                        |
| hasattachment: | report hasattachment:true | Finds items that contain *report* and have attachments                                                          |
| hasflag:       | report hasflag:true       | Finds items that contain *report* and have flags.                                                                |

### Dates

In addition to being able to search on specific dates and date ranges with the operators described previously, AQS allows relative date values (like `today`, `tomorrow`, or `next week`), day values (such as `Tuesday` or `Monday..Wednesday`), and month values (such as `February`).

| Relative to:    | Example | Result |
|----|---|---|
| Day | date:today<br/> date:tomorrow<br/> date:yesterday<br/> | Finds items with today's date.<br/> Finds items with tomorrow's date.<br/> Finds items with yesterday's date. <br/> |
| Week/Month/Year | date:this week<br/> date:last week<br/> date:next month<br/> date:past month<br/> date:coming year <br/> | Finds items with a date falling within the current week.<br/> Finds items with a date falling within the previous week.<br/> Finds items with a date falling within the upcoming week.<br/> Finds items with a date falling within the previous month.<br/> Finds items with a date falling within the upcoming year. <br/> |

## Properties by file kind

Users can search on specific properties of different file kinds. Some properties (like file size) are common to all files, while others are limited to a specific kind. Slide count, for example, is specific to presentations. The following tables list these properties by file kind.

### Everything

These properties are common to all file kinds. To include all types of files in a query, use this syntax:

`kind:everything <property>:<value>`

where `<property>` is an AQS property keyword from the following table and `<value>` is the specified search term.

| Property       | AQS keyword              | Example                        |
|----------------|--------------------------|--------------------------------|
| Title          | title, subject or about  | title:"Quarterly Financial"    |
| Status         | status                   | status:complete                |
| Date           | date                     | date:last week                 |
| Date modified  | datemodified or modified | modified:last week             |
| Importance     | importance or priority   | importance:high                |
| Size           | size                     | size:> 50                   |
| Deleted        | deleted or isdeleted     | isdeleted:true                 |
| Is attachment  | isattachment             | isattachment:true              |
| To             | to or toname             | to:bob                         |
| Cc             | cc or ccname             | cc:john                        |
| Company        | company                  | company:Microsoft              |
| Location       | location                 | location:"Conference Room 102" |
| Category       | category                 | category:Business              |
| Keywords       | keywords                 | keywords:"sales projections"   |
| Album          | album                    | album:"Fly by Night"           |
| File name      | filename or file         | filename:MyResume              |
| Genre          | genre                    | genre:rock                     |
| Author         | author or by             | author:"Stephen King"          |
| People         | people or with           | with:(sonja or david)          |
| Folder         | folder, under or path    | folder:downloads               |
| File extension | ext or fileext           | ext:.txt                       |

### Attachment

These properties are common to all attachment file kinds. To limit the search to attachment files only, use this syntax:

`kind:attachment <property>:<value>`

where `<property>` is an AQS property keyword from the following table and `<value>` is the specified search term.

| Property | AQS keyword | Example |
|----------|-------------|---------|
| People   | people or with | people:john or with:john |

### Contacts

These properties are common to all contacts file kinds. To limit a search to contact files only, use this syntax:

`kind:contacts <property>:<value>`

where `<property>` is an AQS property keyword from the following table and `<value>` is the specified search term.

| Property              | AQS keyword         | Example                            |
|-----------------------|---------------------|------------------------------------|
| Job title             | jobtitle            | jobtitle:CFO                       |
| IM address            | imaddress           | imaddress:john\_doe@msn.com        |
| Assistant's phone     | assistantsphone     | assistantsphone:555-3323           |
| Assistant name        | assistantname       | assistantname:Paul                 |
| Profession            | profession          | profession:plumber                 |
| Nickname              | nickname            | nickname:Tex                       |
| Spouse                | spouse              | spouse:Debbie                      |
| Business city         | businesscity        | businesscity:Seattle               |
| Business postal code  | businesspostalcode  | businesspostalcode:98006           |
| Business home page    | businesshomepage    | businesshomepage:www.office.com |
| Callback phone number | callbackphonenumber | callbackphonenumber:555-555-2121   |
| Car phone             | carphone            | carphone:555-555-2121              |
| Children              | children            | children:Timmy                     |
| First name            | firstname           | firstname:John                     |
| Last name             | lastname            | lastname:Doe                       |
| Home fax              | homefax             | homefax:555-555-2121               |
| Manager's name        | managersname        | managersname:John                  |
| Pager                 | pager               | pager:555-555-2121                 |
| Business phone        | businessphone       | businessphone:555-555-2121         |
| Home phone            | homephone           | homephone:555-555-2121             |
| Mobile phone          | mobilephone         | mobilephone:555-555-2121           |
| Office                | office              | office:sample                      |
| Anniversary           | anniversary         | anniversary:1/1/06                 |
| Birthday              | birthday            | birthday:1/1/06                    |
| Web page              | webpage             | webpage:www.microsoft.com          |

> [!NOTE]
> Phone numbers are indexed as entered. For example, if a country code or area code was omitted in a contact's phone number, users won't be able to find that contact if they search with a country code or area code in the phone number.

### Communications

These properties are common to all communications file kinds. To limit the search to communication files only, use this syntax:

`kind:communications <property>:<value>`

where `<property>` is an AQS property keyword from the following table and `<value>` is the specified search term.

| Property       | AQS keyword                   | Example                         |
|----------------|-------------------------------|---------------------------------|
| From           | from or organizer             | from:john                       |
| Received       | received or sent              | sent:yesterday                  |
| Subject        | subject or title              | subject:"Quarterly Financial"   |
| Has attachment | hasattachments, hasattachment | hasattachment:true              |
| Attachments    | attachments or attachment     | attachment:presentation.ppt     |
| Bcc            | bcc, bccname or bccaddress    | bcc:dave                        |
| Cc address     | ccaddress or cc               | ccaddress:john\_doe@outlook.com |
| Follow-up flag | followupflag                  | followupflag:2                  |
| Due date       | duedate or due                | due:last week                   |
| Read           | read or isread                | is:read                         |
| Is completed   | iscompleted                   | is:completed                    |
| Incomplete     | incomplete or isincomplete    | is:incomplete                   |
| Has flag       | hasflag or isflagged          | has:flag                        |
| Duration       | duration                      | duration:> 50                   |

### Calendar

These properties are common to all calendar file kinds. To limit the search to calendar files only, use this syntax:

`kind:calendar <property>:<value>`

where `<property>` is an AQS property keyword from the following table and `<value>` is the specified search term.

| Property  | AQS keyword              | Example          |
|-----------|--------------------------|------------------|
| Recurring | recurring or isrecurring | is:recurring     |
| Organizer | organizer, by or from    | organizer:debbie |

### Documents

These properties are common to all documents file kinds. To limit the search to document files only, use this syntax:

`kind:documents <property>:<value>`

where `<property>` is an AQS property keyword from the following table and `<value>` is the specified search term.

| Property          | AQS keyword     | Example                       |
|-------------------|-----------------|-------------------------------|
| Comments          | comments        | comments:"needs final review" |
| Last saved by     | lastsavedby     | lastsavedby:john              |
| Document manager  | documentmanager | documentmanager:john          |
| Revision number   | revisionnumber  | revisionnumber:1.0.3          |
| Document format   | documentformat  | documentformat:MIMETYPE       |
| Date last printed | datelastprinted | datelastprinted:last week     |

### Presentation

These properties are common to all presentation file kinds. To limit the search to presentation files only, use this syntax:

`kind:presentation <property>:<value>`

where `<property>` is an AQS property keyword from the following table and `<value>` is the specified search term.

| Property    | AQS keyword | Example           |
|-------------|-------------|-------------------|
| Slide count | slidecount  | slidecount:>20 |

### Music

These properties are common to all music file kinds. To limit the search to music files only, use this syntax:

`kind:music <property>:<value>`

where `<property>` is an AQS property keyword from the following table and `<value>` is the specified search term.

| Property | AQS keyword        | Example                  |
|----------|--------------------|--------------------------|
| Bit rate | bitrate, rate      | bitrate:192              |
| Artist   | artist, by or from | artist:John Singer       |
| Duration | duration           | duration:3               |
| Album    | album              | album:"greatest hits"    |
| Genre    | genre              | genre:rock               |
| Track    | track              | track:12                 |
| Year     | year               | year:> 1980 < 1990 |

### Picture

These properties are common to all picture file kinds. To limit the search to picture files only, use this syntax:

`kind:picture <property>:<value>`

where `<property>` is an AQS property keyword from the following table and `<value>` is the specified search term.

| Property     | AQS keyword | Example               |
|--------------|-------------|-----------------------|
| Camera make  | cameramake  | cameramake:sample     |
| Camera model | cameramodel | cameramodel:sample    |
| Dimensions   | dimensions  | dimensions:8X10       |
| Orientation  | orientation | orientation:landscape |
| Date taken   | datetaken   | datetaken:yesterday   |
| Width        | width       | width:1600            |
| Height       | height      | height:1200           |

### Video

These properties are common to all video file kinds. To limit the search to video files only, use this syntax:

`kind:video <property>:<value>`

where `<property>` is an AQS property keyword from the following table and `<value>` is the specified search term.

| Property | AQS keyword   | Example                                |
|----------|---------------|----------------------------------------|
| Name     | name, subject | name:"Family Vacation to the Beach 05" |
| Ext      | ext, fileext  | ext:.avi                               |

## See also

[Perceived Types](-search-2x-wds-perceivedtype.md)

[Schema table](-search-2x-wds-schematable.md)

[Calling WDS from the command line](-search-2x-wds-fromcommandline.md)

[Calling WDS from web pages](-search-2x-wds-browserhelpobject.md)
