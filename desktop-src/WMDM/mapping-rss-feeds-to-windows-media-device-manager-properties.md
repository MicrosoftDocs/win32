---
title: Mapping RSS Feeds to Windows Media Device Manager Properties
description: Mapping RSS Feeds to Windows Media Device Manager Properties
ms.assetid: 354c98ab-1392-476f-a650-75b948dc971a
keywords:
- Windows Media Device Manager,RSS feeds
- Device Manager,RSS feeds
- programming guide,RSS feeds
- desktop applications,RSS feeds
- creating Windows Media Device Manager applications,RSS feeds
- RSS feeds
ms.topic: article
ms.date: 05/31/2018
---

# Mapping RSS Feeds to Windows Media Device Manager Properties

Windows Media Player 11 provides an RSS aggregator feature that enables users to store content obtained from podcasts on their computers. This topic describes the XML elements found in an RSS feed. In addition, it maps these RSS elements to Windows Media Device Manager properties.

The elements in an RSS feed have the following hierarchy and attributes:


```C++
<channel>
    <title />
    <link />
    <description />
    <language />
    <copyright />
    <managingEditor />
    <webMaster />
    <pubDate />
    <lastBuildDate />
    <category />
    <generator />
    <docs />
    <cloud />
    <ttl />

    <image>
        <url />
        <title />
        <link />
        <width />
        <height />
        <description />
    </image>

    <rating />

    <textInput>
        <title />
        <description />
        <name />
        <link />
    </textInput>

    <skipHours />
    <skipDays />

    <item>
        <title />
        <link />
        <description />
        <author />
        <category domain = " "/>
        <comments />
        <enclousure url = " " length = " " type = " "/>
        <guid isPermaLink = " "/>
        <pubDate />
        <source url = " " />
    </item>
</channel>
```



The following table lists the channel elements in an RSS feed and the corresponding Windows Media Device Manager properties.



| Channel element | Status         | Corresponding Windows Media Device Manager property   |
|-----------------|----------------|-------------------------------------------------------|
| category        | Optional       | [g\_wszWMDMGenre](metadata-constants.md)             |
| cloud           | Not applicable | Not applicable                                        |
| copyright       | Optional       | [g\_wszWMDMProviderCopyright](metadata-constants.md) |
| description     | Required       | [g\_wszWMDMDescription](metadata-constants.md)       |
| docs            | Not applicable | Not applicable                                        |
| generator       | Not applicable | Not applicable                                        |
| language        | Not applicable | Not applicable                                        |
| lastBuildDate   | Optional       | [g\_wszWMDMLastModifiedDate](metadata-constants.md)  |
| link            | Required       | [g\_wszWMDMDestinationURL](metadata-constants.md)    |
| managingEditor  | Optional       | [g\_wszWMDMEditor](metadata-constants.md)            |
| pubDate         | Optional       | [g\_wszWMDMYear](metadata-constants.md)              |
| rating          | Not applicable | Not applicable                                        |
| skipDays        | Not applicable | Not applicable                                        |
| skipHours       | Not applicable | Not applicable                                        |
| textInput       | Not applicable | Not applicable                                        |
| title           | Required       | [g\_wszWMDMTitle](metadata-constants.md)             |
| ttl             | Optional       | [g\_wszWMDMTimeToLive](metadata-constants.md)        |
| webMaster       | Optional       | [g\_wszWMDMWebMaster](metadata-constants.md)         |



 

The following table lists the image elements in an RSS feed and the corresponding WMDM properties.



| Image element | Status   | Corresponding Windows Media Device Manager property |
|---------------|----------|-----------------------------------------------------|
| description   | Optional | [g\_wszWMDMDescription](metadata-constants.md)     |
| height        | Optional | [g\_wszWMDMHeight](metadata-constants.md)          |
| link          | Optional | [g\_wszWMDMDestinationURL](metadata-constants.md)  |
| title         | Optional | [g\_wszWMDMTitle](metadata-constants.md)           |
| url           | Optional | [g\_wszWMDMSourceURL](metadata-constants.md)       |
| width         | Optional | [g\_wszWMDMWidth](metadata-constants.md)           |



 

The following table lists the item elements in an RSS feed and the corresponding Windows Media Device Manager properties.



| Item element | Attribute   | Status         | Corresponding Windows Media Device Manager property            |
|--------------|-------------|----------------|----------------------------------------------------------------|
| author       |             | Optional       | [g\_wszWMDMAuthor](metadata-constants.md)                     |
| category     |             | Optional       | [g\_wszWMDMGenre](metadata-constants.md)                      |
|              | domain      | Not applicable | Not applicable                                                 |
| description  |             | Optional       | [g\_wszWMDMDescription](metadata-constants.md)                |
| enclosure    |             | Optional       | Not applicable                                                 |
|              | length      | Required       | [g\_wszWMDMFileSize](metadata-constants.md)                   |
|              | type        | Required       | (The MIME type should be mapped to the property content type.) |
|              | url         | Required       | [g\_wszWMDMSourceURL](metadata-constants.md)                  |
| guid         |             | Optional       | [g\_wszWMDMediaGuid](metadata-constants.md)                   |
|              | isPermaLink | Not applicable | Not applicable                                                 |
| link         |             | Optional       | [g\_wszWMDMDestinationURL](metadata-constants.md)             |
| pubDate      |             | Optional       | [g\_wszWMDMYear](metadata-constants.md)                       |
| source       |             | Not applicable | Not applicable                                                 |
| title        |             | Optional       | [g\_wszWMDMTitle](metadata-constants.md)                      |



 

Example

The following example shows a complete RSS feed for a fictitious podcast supplied by the CEO of a publishing company.


```C++
<channel>
    <title>The Digital Publication</title>
    <link>https://www.lucernepublishing.com/podcasting</link>
    <description>Lucerne Publishing CEO Peter Bankov takes a look at the latest trends in online publications.</description>
    <language>en-us</language>
    <copyright>2006 Lucerne Publishing LP, LLLP. All Rights Reserved.</copyright>
    <managingEditor>someone@example.com</managingEditor>
    <webMaster>someone@example.com</webMaster>
    <pubDate>Fri, 9 June 2006 14:00:28 EDT</pubDate>
    <lastBuildDate Fri, 9 June 2006 14:00:28 EDT />
    <category>News</category>
    <generator>Podcaster version 1.0</generator>
    <docs>https://www.lucernepublishing.com/tech/rss</docs>
    <cloud />
    <ttl>240</ttl>
    <rating />
    <textInput />
    <skipHours />
    <skipDays />

<image>
     <url>https://www.lucernepublishing.com/images/logo.gif</url>
     <title>Lucerne Publishing</title>
     <link>https://www.lucernepublishing.com/community/podcasts</link>
     <width>300</width>
     <height>300</height>
     <description>Lucerne Logo</description>
</image>

<item>
    <title>The Digital Publication</title>
    <link>https://www.lucernepublishing/services/podcasting/digital.publishing/audio/2006/06/digital0601.mp3</link>
    <description>Online publications are rapidly changing. A publishing house CEO examines the trends of the past five years and their implications.</description>
    <author>Lucerne</author>
    <category>News</category>
    <comments />
    <enclosure url="https://www.lucernepublishing/services/podcasting/digital.publishing/audio/2006/06/digital0601.mp3" length="10329011" type="audio/mpeg" />
    <guid>https://www.lucernepublishing/services/podcasting/digital.publishing/audio/2006/06/digital0601.mp3</guid>
    <pubDate>Thur, 1 June 2006 14:00:28 EDT</pubDate>
    <source />
</item>

</channel>
```



Mapping of RSS Channel Elements to Windows Media Device Manager Property Values

The following table describes how the values in the RSS Channel elements in the previous example map to particular Windows Media Device Manager properties.



| Windows Media Device Manager property                    | Value                                                                                         |
|----------------------------------------------------------|-----------------------------------------------------------------------------------------------|
| [g\_wszWMDMAuthorDate](metadata-constants.md)           | Fri, 9 June 2006 14:00:28 EDT                                                                 |
| [g\_wszWMDMDESCRIPTION](metadata-constants.md)          | Lucerne Publishing CEO Peter Bankov takes a look at the latest trends in online publications. |
| [g\_wszWMDMDESTINATION\_URL](metadata-constants.md)     | `https://www.lucernepublishing/services/podcasting`                                              |
| [g\_wszWMDMEDITOR](metadata-constants.md)               | someone@example.com                                                                           |
| [g\_wszWMDMFileCreationDate](metadata-constants.md)     | Fri, 9 June 2006 14:00:28 EDT                                                                 |
| [g\_wszWMDMFileName](metadata-constants.md)             | The Digital Publication                                                                       |
| [g\_wszWMDMFileSize](metadata-constants.md)             | 13,790                                                                                        |
| [g\_wszWMDMFormatCode](metadata-constants.md)           | WMDM\_FORMATCODE\_MEDIA\_CAST                                                                 |
| [g\_wszWMDMGENRE](metadata-constants.md)                | News                                                                                          |
| [g\_wszWMDMLAST\_MODIFIED\_DATE](metadata-constants.md) | Fri, 9 June 2006 14:00:28 EDT                                                                 |
| [g\_wszWMDMLastModifiedDate](metadata-constants.md)     | Fri, 9 June 2006 14:00:28 EDT                                                                 |
| [g\_wszWMDMProviderCopyright](metadata-constants.md)    | 2006 Lucerne Publishing LP, LLLP. All Rights Reserved.                                        |
| [g\_wszWMDMTimeToLive](metadata-constants.md)           | 240                                                                                           |
| [g\_wszWMDMTitle](metadata-constants.md)                | The Digital Publication                                                                       |
| [g\_wszWMDMWEBMASTER](metadata-constants.md)            | someone@example.com                                                                           |
| [g\_wszWMDMYear](metadata-constants.md)                 | Fri, 9 June 2006 14:00:28 EDT                                                                 |



 

Mapping of RSS Image Elements to Windows Media Device Manager Property Values

The following table describes how the values in the RSS Image elements in the previous example map to particular Windows Media Device Manager properties.



| Windows Media Device Manager property                | Value                                            |
|------------------------------------------------------|--------------------------------------------------|
| [g\_wszWMDMAlbumCoverFormat](metadata-constants.md) | WPD\_OBJECT\_FORMAT\_GIF                         |
| [g\_wszWMDMAlbumCoverSize](metadata-constants.md)   | 512                                              |
| [g\_wszWMDMDescription](metadata-constants.md)      | Lucerne Logo                                     |
| [g\_wszWMDMDestinationURL](metadata-constants.md)   | //www.lucernepublishing.com/community/podcasts   |
| [g\_wszWMDMHeight](metadata-constants.md)           | 300                                              |
| [g\_wszWMDMSourceURL](metadata-constants.md)        | `https://www.lucernepublishing.com/images/logo.gif` |
| [g\_wszWMDMTitle](metadata-constants.md)            | Lucerne Publishing                               |
| [g\_wszWMDMWidth](metadata-constants.md)            | 300                                              |



 

Mapping of RSS Item Elements to Windows Media Device Manager Property Values

The following table describes how the values in the RSS Item elements in the previous example map to particular Windows Media Device Manager properties.



| Windows Media Device Manager property                | Value                                                                                                                               |
|------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| [g\_wszWMDMAuthor](metadata-constants.md)           | Lucerne                                                                                                                             |
| [g\_wszWMDMAuthorDate](metadata-constants.md)       | Thur, 1 June 2006 14:00:28 EDT                                                                                                      |
| [g\_wszWMDMDescription](metadata-constants.md)      | Online publications are rapidly changing. A publishing house CEO examines the trends of the past five years and their implications. |
| [g\_wszWMDMDestinationURL](metadata-constants.md)   | `https://www.lucernepublishing/services/podcasting/digital.publishing/audio/2006/06/digital0601.mp3`                                  |
| [g\_wszWMDMDuration](metadata-constants.md)         | 120325445                                                                                                                           |
| [g\_wszWMDMFileCreationDate](metadata-constants.md) | Thur, 1 June 2006 14:00:28 EDT                                                                                                      |
| [g\_wszWMDMFileSize](metadata-constants.md)         | 10329011                                                                                                                            |
| [g\_wszWMDMFormatCode](metadata-constants.md)       | WMDM\_FORMATCODE\_MP3                                                                                                               |
| [g\_wszWMDMGenre](metadata-constants.md)            | News                                                                                                                                |
| [g\_wszWMDMLastModifiedDate](metadata-constants.md) | Thur, 1 June 2006 14:00:28 EDT                                                                                                      |
| [g\_wszWMDMMediaGuid](metadata-constants.md)        | `https://www.lucernepublishing/services/podcasting/digital.publishing/audio/2006/06/digital0601.mp3`                                 |
| [g\_wszWMDMSourceURL](metadata-constants.md)        | `https://www.lucernepublishing/services/podcasting/digital.publishing/audio/2006/06/digital0601.mp3`                                  |
| [g\_wszWMDMTitle](metadata-constants.md)            | The Digital Publication                                                                                                             |
| [g\_wszWMDMYear](metadata-constants.md)             | Thur, 1 June 2006 14:00:28 EDT                                                                                                      |



 

## Related topics

<dl> <dt>

[**Metadata Constants**](metadata-constants.md)
</dt> </dl>

 

 




