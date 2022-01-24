---
description: WPD\_CONTENT\_TYPE\_MEDIA\_CAST
ms.assetid: 368e7381-8978-421a-b450-59915f8e70e2
title: WPD_CONTENT_TYPE_MEDIA_CAST
ms.topic: article
ms.date: 05/31/2018
---

# WPD\_CONTENT\_TYPE\_MEDIA\_CAST

An object that describes its type as WPD\_CONTENT\_TYPE\_MEDIA\_CAST represents a collection of related content.

A Mediacast object can be thought of as a container object that groups related content, just as a playlist groups music. Often, a Mediacast object is used to group media content that was published online. For example, an RSS channel can be represented as a Mediacast object whose object references point to content objects that represent each item in the channel.

This type of object supports the following properties.



| Property Name             |  Required or Optional         |
|-----------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------|
| [WPD\_OBJECT\_ID](object-properties.md)                                                                | Required.                                                             |
| [WPD\_OBJECT\_PARENT\_ID](object-properties.md)                                                 | Required.                                                             |
| [WPD\_OBJECT\_NAME](object-properties.md)                                                            | Required if the object represents a file.                             |
| [WPD\_OBJECT\_PERSISTENT\_UNIQUE\_ID](object-properties.md)                          | Required.                                                             |
| [WPD\_OBJECT\_FORMAT](object-properties.md)                                                        | Required.                                                             |
| [WPD\_OBJECT\_CONTENT\_TYPE](object-properties.md)                                           | Required.                                                             |
| [WPD\_OBJECT\_ISHIDDEN](object-properties.md)                                                    | Required if the object is hidden.                                     |
| [WPD\_OBJECT\_ISSYSTEM](object-properties.md)                                                    | Required if the object is a system object (represents a system file). |
| [WPD\_OBJECT\_SIZE](object-properties.md)                                                            | Required if the object has at least one resource.                     |
| [WPD\_OBJECT\_ORIGINAL\_FILE\_NAME](object-properties.md)                              | Required if the object represents a file.                             |
| [WPD\_OBJECT\_NON\_CONSUMABLE](object-properties.md)                                       | Recommended if the object is not meant for consumption by the device. |
| [WPD\_OBJECT\_REFERENCES](object-properties.md)                                                | Required if the object has references to other objects.               |
| [WPD\_OBJECT\_KEYWORDS](object-properties.md)                                                    | Optional.                                                             |
| [WPD\_OBJECT\_SYNC\_ID](object-properties.md)                                                     | Optional.                                                             |
| [WPD\_OBJECT\_IS\_DRM\_PROTECTED](object-properties.md)                                  | Required if the object is protected by DRM technology.                |
| [WPD\_OBJECT\_DATE\_CREATED](object-properties.md)                                           | Optional.                                                             |
| [WPD\_OBJECT\_DATE\_MODIFIED](object-properties.md)                                         | Recommended.                                                          |
| [WPD\_OBJECT\_DATE\_AUTHORED](object-properties.md)                                         | Optional.                                                             |
| [WPD\_OBJECT\_BACK\_REFERENCES](object-properties.md)                                     | Recommended if the object is referenced by another object.            |
| [WPD\_OBJECT\_CONTAINER\_FUNCTIONAL\_OBJECT\_ID](object-properties.md)     | Optional.                                                             |
| [WPD\_OBJECT\_GENERATE\_THUMBNAIL\_FROM\_RESOURCE](object-properties.md) | Optional.                                                             |
| [WPD\_OBJECT\_CAN\_DELETE](object-properties.md)                                               | Required if the object can be deleted.                                |
| [WPD\_OBJECT\_LANGUAGE\_LOCALE](object-properties.md)                                                                | Required if the object cannot be deleted.                             |
| [WPD\_MEDIA\_COPYRIGHT](media-properties.md)                                                     | Optional.                                                             |
| [WPD\_MEDIA\_PARENTAL\_RATING](media-properties.md)                                        | Optional.                                                             |
| [WPD\_MEDIA\_META\_GENRE](media-properties.md)                                                  | Optional.                                                             |
| [WPD\_MEDIA\_SUB\_TITLE](media-properties.md)                                                    | Optional.                                                             |
| [WPD\_MEDIA\_RELEASE\_DATE](media-properties.md)                                              | Recommended.                                                          |
| [WPD\_MEDIA\_TITLE](media-properties.md)                                                             | Recommended.                                                          |
| [WPD\_MEDIA\_OWNER](media-properties.md)                                                             | Recommended.                                                          |
| [WPD\_MEDIA\_MANAGING\_EDITOR](media-properties.md)                                        | Recommended.                                                          |
| [WPD\_MEDIA\_WEBMASTER](media-properties.md)                                                     | Recommended.                                                          |
| [WPD\_MEDIA\_SOURCE\_URL](media-properties.md)                                                  | Recommended.                                                          |
| [WPD\_MEDIA\_DESTINATION\_URL](media-properties.md)                                        | Recommended.                                                          |
| [WPD\_MEDIA\_DESCRIPTION](media-properties.md)                                                 | Optional.                                                             |
| [WPD\_MEDIA\_GENRE](media-properties.md)                                                             | Optional.                                                             |
| [WPD\_MEDIA\_OBJECT\_BOOKMARK](media-properties.md)                                        | Recommended                                                           |
| [WPD\_MEDIA\_LAST\_BUILD\_DATE](media-properties.md)                                       | Recommended.                                                          |
| [WPD\_MEDIA\_TIME\_TO\_LIVE](media-properties.md)                                             | Optional.                                                             |
| [WPD\_MEDIA\_SUB\_DESCRIPTION](object-properties.md)                                                                 | Optional.                                                             |



 

## Typical Resources

These objects typically include the following resources.



| Resource Name                                               | Required or Optional | Description                                                                                                                 |
|-------------------------------------------------------------|----------------------|-----------------------------------------------------------------------------------------------------------------------------|
| [**WPD\_RESOURCE\_DEFAULT**](wpd-resource-default.md)      | Optional.            | Contains the mediacast file data. For example, if this mediacast represents an RSS channel, this might be the RSS document. |
| [**WPD\_RESOURCE\_THUMBNAIL**](wpd-resource-thumbnail.md)  | Optional.            | Contains the thumbnail representing this mediacast.                                                                         |
| [**WPD\_RESOURCE\_ALBUM\_ART**](wpd-resource-album-art.md) | Optional.            | Contains the artwork for this mediacast.                                                                                    |



 

## Mapping of RSS Elements and Mediacast properties

An RSS channel can be represented as a Mediacast object whose references point to content objects representing each item in a given channel.

The elements in an RSS feed have the following hierarchy and attributes.


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



The following table lists the channel elements in an RSS feed and the corresponding WPD\_CONTENT\_TYPE\_MEDIA\_CAST properties.



| Channel Element | RSS Feed Requirement | Corresponding Mediacast Property      |
|---------------------|--------------------------|---------------------------------------------------------------------------------|
| category            | Optional.                | [WPD\_MEDIA\_GENRE](media-properties.md)                       |
| cloud               | Not applicable.          | Not applicable.                                                                 |
| copyright           | Optional.                | [WPD\_MEDIA\_COPYRIGHT](media-properties.md)               |
| description         | Required.                | [WPD\_MEDIA\_DESCRIPTION](media-properties.md)           |
| docs                | Not applicable.          | Not applicable.                                                                 |
| generator           | Not applicable.          | Not applicable.                                                                 |
| language            | Not applicable.          | Not applicable.                                                                 |
| lastBuildDate       | Optional.                | [WPD\_MEDIA\_LAST\_BUILD\_DATE](media-properties.md) |
| link                | Required.                | [WPD\_MEDIA\_DESTINATION\_URL](media-properties.md)  |
| managingEditor      | Optional.                | [WPD\_MEDIA\_MANAGING\_EDITOR](media-properties.md)  |
| pubDate             | Optional.                | [WPD\_MEDIA\_RELEASE\_DATE](media-properties.md)        |
| rating              | Not applicable.          | Not applicable.                                                                 |
| skipDays            | Not applicable.          | Not applicable.                                                                 |
| skipHours           | Not applicable.          | Not applicable.                                                                 |
| textInput           | Not applicable.          | Not applicable.                                                                 |
| title               | Required.                | [WPD\_OBJECT\_NAME](object-properties.md)                      |
| ttl                 | Optional.                | [WPD\_MEDIA\_TIME\_TO\_LIVE](media-properties.md)       |
| webMaster           | Optional.                | [WPD\_MEDIA\_WEBMASTER](media-properties.md)               |



 

The following table lists the image elements in an RSS feed and the corresponding WPD\_CONTENT\_TYPE\_MEDIA\_CAST properties.



| Image Element | RSS Feed Requirement | Mediacast Property                     |
|-------------------|--------------------------|--------------------------------------------------------------------------------|
| description       | Optional.                | [WPD\_MEDIA\_DESCRIPTION](media-properties.md)          |
| height            | Optional.                | [WPD\_MEDIA\_HEIGHT](media-properties.md)                    |
| link              | Optional.                | [WPD\_MEDIA\_DESTINATION\_URL](media-properties.md) |
| title             | Optional.                | [WPD\_OBJECT\_NAME](object-properties.md)                     |
| url               | Optional.                | [WPD\_MEDIA\_SOURCE\_URL](media-properties.md)           |
| width             | Optional.                | [WPD\_MEDIA\_WIDTH](media-properties.md)                      |



 

The following table lists the item elements in an RSS feed and the corresponding WPD\_CONTENT\_TYPE\_MEDIA\_CAST properties.



| Item Element | Attribute | RSS Feed Requirement | Mediacast Property  |
|------------------|---------------|--------------------------|--------------------------------------------------------------------------------|
| author           |               | Optional.                | [WPD\_MEDIA\_ARTIST](media-properties.md)                    |
| category         |               | Optional.                | [WPD\_MEDIA\_GENRE](media-properties.md)                      |
|                  | domain        | Not applicable.          | Not applicable.                                                                |
| description      |               | Optional.                | [WPD\_MEDIA\_DESCRIPTION](media-properties.md)          |
| enclosure        |               | Optional.                |                                                                                |
|                  | url           | Required.                | [WPD\_MEDIA\_SOURCE\_URL](media-properties.md)           |
|                  | length        | Required.                | [WPD\_OBJECT\_SIZE](object-properties.md)                     |
|                  | type          | Required.                | (The MIME type should be mapped to the property content type.)                 |
| guid             |               | Optional.                | [WPD\_MEDIA\_GUID](media-properties.md)                        |
|                  | isPermaLink   | Not applicable.          | Not applicable.                                                                |
| link             |               | Optional.                | [WPD\_MEDIA\_DESTINATION\_URL](media-properties.md) |
| pubDate          |               | Optional.                | [WPD\_MEDIA\_RELEASE\_DATE](media-properties.md)       |
| source           |               | Not applicable.          | Not applicable.                                                                |
| title            |               | Optional.                | [WPD\_OBJECT\_NAME](object-properties.md)                     |



 

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
    <link>https://www.lucernepublishing.com/services/podcasting/digital.publishing/audio/2006/06/digital0601.mp3</link>
    <description>Online publications are rapidly changing. A publishing house CEO examines the trends of the past 5 years and their implications.</description>
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



## Mapping RSS Channel Elements to WPD Property Values

The following table describes how the values in the RSS channel elements in the previous example map to particular WPD properties.



| WPD Property | Value |
|----------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|
| [WPD\_MEDIA\_COPYRIGHT](media-properties.md)                            | 2006 Lucerne Publishing LP, LLLP. All Rights Reserved.                                        |
| [WPD\_MEDIA\_DESCRIPTION](media-properties.md)                        | Lucerne Publishing CEO Peter Bankov takes a look at the latest trends in online publications. |
| [WPD\_MEDIA\_DESTINATION\_URL](media-properties.md)               | `https://www.lucernepublishing.com/services/podcasting`                                          |
| [WPD\_MEDIA\_GENRE](media-properties.md)                                    | News                                                                                          |
| [WPD\_MEDIA\_LAST\_BUILD\_DATE](media-properties.md)              | Fri, 9 June 2006 14:00:28 EDT                                                                 |
| [WPD\_MEDIA\_MANAGING\_EDITOR](media-properties.md)               | someone@example.com                                                                           |
| [WPD\_MEDIA\_RELEASE\_DATE](media-properties.md)                     | Fri, 9 June 2006 14:00:28 EDT                                                                 |
| [WPD\_MEDIA\_TIME\_TO\_LIVE](media-properties.md)                    | 240                                                                                           |
| [WPD\_MEDIA\_TITLE](media-properties.md)                                    | The Digital Publication                                                                       |
| [WPD\_MEDIA\_SOURCE\_URL](media-properties.md)                         | `https://www.lucernepublishing/services/podcasting/digital.publication/rss.xml`                  |
| [WPD\_MEDIA\_WEBMASTER](media-properties.md)                            | someone@example.com                                                                           |
| [WPD\_OBJECT\_CONTENT\_TYPE](object-properties.md)                  | WPD\_CONTENT\_TYPE\_MEDIA\_CAST                                                               |
| [WPD\_OBJECT\_DATE\_AUTHORED](object-properties.md)                | Fri, 9 June 2006 14:00:28 EDT                                                                 |
| [WPD\_OBJECT\_DATE\_CREATED](object-properties.md)                  | Fri, 9 June 2006 14:00:28 EDT                                                                 |
| [WPD\_OBJECT\_DATE\_MODIFIED](object-properties.md)                | Fri, 9 June 2006 14:00:28 EDT                                                                 |
| [WPD\_OBJECT\_FORMAT](object-properties.md)                               | WPD\_OBJECT\_FORMAT\_ABSTRACT\_MEDIA\_CAST                                                    |
| [WPD\_OBJECT\_ID](object-properties.md)                                       | Session dependent value.                                                                      |
| [WPD\_OBJECT\_NAME](object-properties.md)                                   | The Digital Publication                                                                       |
| [WPD\_OBJECT\_ORIGINAL\_FILE\_NAME](object-properties.md)     | The Digital Publication                                                                       |
| [WPD\_OBJECT\_PARENT\_ID](object-properties.md)                        | MyPodcasts (a fictitious podcast folder on the device). Assume "0A0" for this example.        |
| [WPD\_OBJECT\_PERSISTENT\_UNIQUE\_ID](object-properties.md) | Session independent value. (Assume "0A1" for this example.)                                   |
| [WPD\_OBJECT\_REFERENCES](object-properties.md)                       | 0A2  for N items<br/>                                                                   |
| [WPD\_OBJECT\_SIZE](object-properties.md)                                   | 13,790                                                                                        |



 

## Mapping RSS Image Elements to WPD Property Values

The following table describes how the values in the RSS Image elements in the previous example map to particular WPD properties.



| WPD Property               |                         Value                                           |
|-------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------|
| [WPD\_MEDIA\_DESCRIPTION](media-properties.md)                                                   | Lucerne Logo                                        |
| [WPD\_MEDIA\_DESTINATION\_URL](media-properties.md)                                          | `https://www.lucernepublishing.com/community/podcasts` |
| [WPD\_MEDIA\_HEIGHT](media-properties.md)                                                             | 300                                                 |
| [WPD\_MEDIA\_SOURCE\_URL](media-properties.md)                                                    | `https://www.lucernepublishing.com/images/logo.gif`    |
| [WPD\_MEDIA\_WIDTH](media-properties.md)                                                               | 300                                                 |
| [WPD\_OBJECT\_NAME](object-properties.md)                                                              | Lucerne Publishing                                  |
| [WPD\_RESOURCE\_ATTRIBUTE\_CAN\_DELETE](attributes.md)                               | VARIANT\_TRUE                                       |
| [WPD\_RESOURCE\_ATTRIBUTE\_CAN\_READ](attributes.md)                                   | VARIANT\_TRUE                                       |
| [WPD\_RESOURCE\_ATTRIBUTE\_FORMAT](resource-attribute-properties.md)                     | WPD\_OBJECT\_FORMAT\_GIF                            |
| [WPD\_RESOURCE\_ATTRIBUTE\_OPTIMAL\_READ\_BUFFER\_SIZE](attributes.md) | 1024                                                |
| [WPD\_RESOURCE\_ATTRIBUTE\_TOTAL\_SIZE](resource-attribute-properties.md)            | 512                                                 |



 

## Mapping RSS Item Elements to WPD Property Values

The following table describes how the values in the RSS Item elements in the previous example map to particular WPD properties.



| WPD Property  | Value                   |
|----------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|
| [WPD\_MEDIA\_TITLE](media-properties.md)                                    | The Digital Publication                                                                                                          |
| [WPD\_MEDIA\_DURATION](media-properties.md)                              | 10329011                                                                                                                         |
| [WPD\_MEDIA\_ARTIST](media-properties.md)                                  | Lucerne                                                                                                                          |
| [WPD\_MEDIA\_DESCRIPTION](media-properties.md)                        | Online publications are rapidly changing. A publishing house CEO examines the trends of the past 5 years and their implications. |
| [WPD\_MEDIA\_DESTINATION\_URL](media-properties.md)               | `https://www.lucernepublishing/services/podcasting/digital.publishing/audio/2006/06/digital0601.mp3`                                |
| [WPD\_MEDIA\_GENRE](media-properties.md)                                    | News                                                                                                                             |
| [WPD\_MEDIA\_GUID](media-properties.md)                                      | `https://www.lucernepublishing/services/podcasting/digital.publishing/audio/2006/06/digital0601.mp3`                                |
| [WPD\_MEDIA\_RELEASE\_DATE](media-properties.md)                     | Thur, 1 June 2006 14:00:28 EDT                                                                                                   |
| [WPD\_MEDIA\_SOURCE\_URL](media-properties.md)                         | `https://www.lucernepublishing/services/podcasting/digital.publishing/audio/2006/06/digital0601.mp3`                                |
| [WPD\_OBJECT\_BACK\_REFERENCES](object-properties.md)            | 0A1                                                                                                                              |
| [WPD\_OBJECT\_CONTENT\_TYPE](object-properties.md)                  | WPD\_CONTENT\_TYPE\_MEDIA\_IMAGE                                                                                                 |
| [WPD\_OBJECT\_DATE\_AUTHORED](object-properties.md)                | Thur, 1 June 2006 14:00:28 EDT                                                                                                   |
| [WPD\_OBJECT\_DATE\_CREATED](object-properties.md)                  | Thur, 1 June 2006 14:00:28 EDT                                                                                                   |
| [WPD\_OBJECT\_DATE\_MODIFIED](object-properties.md)                | Thur, 1 June 2006 14:00:28 EDT                                                                                                   |
| [WPD\_OBJECT\_FORMAT](object-properties.md)                               | WPD\_OBJECT\_FORMAT\_MP3                                                                                                         |
| [WPD\_OBJECT\_ID](object-properties.md)                                       | Session dependent. (Assume "0A2" for this example.)                                                                              |
| [WPD\_OBJECT\_NAME](object-properties.md)                                   | The Digital Publication                                                                                                          |
| [WPD\_OBJECT\_ORIGINAL\_FILE\_NAME](object-properties.md)     | digital0601.mp3                                                                                                                  |
| [WPD\_OBJECT\_PARENT\_ID](object-properties.md)                        | 0A0                                                                                                                              |
| [WPD\_OBJECT\_PERSISTENT\_UNIQUE\_ID](object-properties.md) | Session independent.                                                                                                             |
| [WPD\_OBJECT\_SIZE](object-properties.md)                                   | 10329011                                                                                                                         |



 

## Related topics

<dl> <dt>

[**Requirements for Objects**](requirements-for-objects.md)
</dt> </dl>

 

 




