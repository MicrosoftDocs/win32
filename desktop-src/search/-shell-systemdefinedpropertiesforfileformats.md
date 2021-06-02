---
description: Microsoft Windows supplies a number of system properties that you can use for your file formats.
ms.assetid: 3a25c4fb-ffea-4524-b59b-912416b2fc7d
title: System-Defined Properties for Custom File Formats
ms.topic: article
ms.date: 05/31/2018
---

# System-Defined Properties for Custom File Formats

Microsoft Windows supplies a number of system properties that you can use for your file formats. If you are creating a custom file format, you should support as many system-defined properties as you can. Before creating a custom property handler, you should review the system-supplied handlers to see if you can use one instead of writing your own.

The following table categorizes file formats and then lists the most important system properties your file format should support. To provide a good user experience, you should support all priority 1 and 2 properties for your category of file format.

-   [Communications](#communications)
-   [Contacts](#contacts)
-   [Documents](#documents)
-   [Generic](#generic)
-   [Music](#music)
-   [Pictures](#pictures)
-   [Videos](#videos)
-   [Related topics](#related-topics)

## Communications



| Name            | Property                               | Priority |
|-----------------|----------------------------------------|----------|
| Date received   | System.Message.DateReceived            | 1        |
| From names      | System.Message.FromName                | 1        |
| Has attachments | System.Message.HasAttachments          | 1        |
| Mailbox         | System.Communication.storeddisplayname | 1        |
| Name            | System.FileName                        | 1        |
| Subject         | System.Subject                         | 1        |
| To names        | System.Message.ToName                  | 1        |
| Category        | System.Category                        | 2        |
| Type            | System.PerceivedType                   | 2        |



 

## Contacts



| Name             | Property                           | Priority |
|------------------|------------------------------------|----------|
| Account Name     | System.Communication.AccountName   | 1        |
| Business Phone   | System.Contact.BusinessTelephone   | 1        |
| Company          | System.Company                     | 1        |
| Email Address    | System.Contact.PrimaryEmailAddress | 1        |
| Importance       | System.ImportanceText              | 1        |
| Mobile Phone     | System.Contact.MobileTelephone     | 1        |
| Business address | System.Contact.BusinessAddress     | 2        |
| Business fax     | System.Contact.BusinessFaxNumber   | 2        |
| Category         | System.Category                    | 2        |
| Home address     | System.Contact.HomeAddress         | 2        |
| Home phone       | System.Contact.HomeTelephone       | 2        |
| Title            | System.Title                       | 2        |



 

## Documents



| Name      | Property             | Priority |
|-----------|----------------------|----------|
| Authors   | System.Author        | 1        |
| Full Text | System.FullText      | 1        |
| Tags      | System.Keywords      | 1        |
| Type      | System.PerceivedType | 1        |
| Category  | System.Category      | 2        |
| Title     | System.Title         | 2        |



 

## Generic



| Name     | Property             | Priority |
|----------|----------------------|----------|
| Authors  | System.Author        | 1        |
| Title    | System.Title         | 1        |
| Type     | System.PerceivedType | 1        |
| Category | System.Category      | 2        |
| Tags     | System.Keywords      | 2        |



 

## Music



| Name         | Property                     | Priority |
|--------------|------------------------------|----------|
| \#           | System.Music.TrackNumber     | 1        |
| Album        | System.Music.AlbumTitle      | 1        |
| Artists      | System.Music.Artist          | 1        |
| Genre        | System.Music.Genre           | 1        |
| Rating       | System.Rating                | 1        |
| Title        | System.Title                 | 1        |
| Album Artist | System.Music.AlbumArtist     | 2        |
| Bit Rate     | System.Audio.EncodingBitrate | 2        |
| Conductors   | System.Music.Conductor       | 2        |
| Length       | System.Media.Duration        | 2        |
| Protected    | System.DRM.IsProtected       | 2        |
| Year         | System.Media.Year            | 2        |



 

## Pictures



| Name          | Property                        | Priority |
|---------------|---------------------------------|----------|
| Date imported | System.DateImported             | 1        |
| Date Taken    | System.Photo.DateTaken          | 1        |
| Rating        | System.Rating                   | 1        |
| Tags          | System.Keywords                 | 1        |
| Type          | System.PerceivedType            | 1        |
| Authors       | System.Author                   | 2        |
| Camera maker  | System.Photo.CameraManufacturer | 2        |
| Camera model  | System.Photo.CameraModel        | 2        |
| Comments      | System.Comment                  | 2        |
| Dimensions    | System.Image.Dimensions         | 2        |



 

## Videos



| Name         | Property                 | Priority |
|--------------|--------------------------|----------|
| Length       | System.Media.Duration    | 1        |
| Rating       | System.Rating            | 1        |
| Tags         | System.Keywords          | 1        |
| Type         | System.PerceivedType     | 1        |
| Frame height | System.Video.FrameHeight | 2        |
| Frame width  | System.Video.FrameWidth  | 2        |



 

## Related topics

<dl> <dt>

**Conceptual**
</dt> <dt>

[Developing Property Handlers for Windows Search](-search-3x-wds-extidx-propertyhandlers.md)
</dt> <dt>

**Other Resources**
</dt> <dt>

[Property System](../properties/building-property-handlers.md)
</dt> <dt>

[System Properties](https://msdn.microsoft.com/library/bb763010(VS.85).aspx)
</dt> </dl>

 

 
