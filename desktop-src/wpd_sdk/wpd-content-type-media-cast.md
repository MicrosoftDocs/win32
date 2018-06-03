---
Description: WPD\_CONTENT\_TYPE\_MEDIA\_CAST
ms.assetid: 368e7381-8978-421a-b450-59915f8e70e2
title: WPD\_CONTENT\_TYPE\_MEDIA\_CAST
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# WPD\_CONTENT\_TYPE\_MEDIA\_CAST

An object that describes its type as WPD\_CONTENT\_TYPE\_MEDIA\_CAST represents a collection of related content.

A Mediacast object can be thought of as a container object that groups related content, just as a playlist groups music. Often, a Mediacast object is used to group media content that was published online. For example, an RSS channel can be represented as a Mediacast object whose object references point to content objects that represent each item in the channel.

This type of object supports the following properties.



|                                                                                                                       |                                                                       |
|-----------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------|
| **Property Name**                                                                                                     | **Required or Optional**                                              |
| [WPD\_OBJECT\_ID](https://www.bing.com/search?q=WPD\_OBJECT\_ID)                                                                | Required.                                                             |
| [WPD\_OBJECT\_PARENT\_ID](https://www.bing.com/search?q=WPD\_OBJECT\_PARENT\_ID)                                                 | Required.                                                             |
| [WPD\_OBJECT\_NAME](https://www.bing.com/search?q=WPD\_OBJECT\_NAME)                                                            | Required if the object represents a file.                             |
| [WPD\_OBJECT\_PERSISTENT\_UNIQUE\_ID](https://www.bing.com/search?q=WPD\_OBJECT\_PERSISTENT\_UNIQUE\_ID)                          | Required.                                                             |
| [WPD\_OBJECT\_FORMAT](https://www.bing.com/search?q=WPD\_OBJECT\_FORMAT)                                                        | Required.                                                             |
| [WPD\_OBJECT\_CONTENT\_TYPE](https://www.bing.com/search?q=WPD\_OBJECT\_CONTENT\_TYPE)                                           | Required.                                                             |
| [WPD\_OBJECT\_ISHIDDEN](https://www.bing.com/search?q=WPD\_OBJECT\_ISHIDDEN)                                                    | Required if the object is hidden.                                     |
| [WPD\_OBJECT\_ISSYSTEM](https://www.bing.com/search?q=WPD\_OBJECT\_ISSYSTEM)                                                    | Required if the object is a system object (represents a system file). |
| [WPD\_OBJECT\_SIZE](https://www.bing.com/search?q=WPD\_OBJECT\_SIZE)                                                            | Required if the object has at least one resource.                     |
| [WPD\_OBJECT\_ORIGINAL\_FILE\_NAME](https://www.bing.com/search?q=WPD\_OBJECT\_ORIGINAL\_FILE\_NAME)                              | Required if the object represents a file.                             |
| [WPD\_OBJECT\_NON\_CONSUMABLE](https://www.bing.com/search?q=WPD\_OBJECT\_NON\_CONSUMABLE)                                       | Recommended if the object is not meant for consumption by the device. |
| [WPD\_OBJECT\_REFERENCES](https://www.bing.com/search?q=WPD\_OBJECT\_REFERENCES)                                                | Required if the object has references to other objects.               |
| [WPD\_OBJECT\_KEYWORDS](https://www.bing.com/search?q=WPD\_OBJECT\_KEYWORDS)                                                    | Optional.                                                             |
| [WPD\_OBJECT\_SYNC\_ID](https://www.bing.com/search?q=WPD\_OBJECT\_SYNC\_ID)                                                     | Optional.                                                             |
| [WPD\_OBJECT\_IS\_DRM\_PROTECTED](https://www.bing.com/search?q=WPD\_OBJECT\_IS\_DRM\_PROTECTED)                                  | Required if the object is protected by DRM technology.                |
| [WPD\_OBJECT\_DATE\_CREATED](https://www.bing.com/search?q=WPD\_OBJECT\_DATE\_CREATED)                                           | Optional.                                                             |
| [WPD\_OBJECT\_DATE\_MODIFIED](https://www.bing.com/search?q=WPD\_OBJECT\_DATE\_MODIFIED)                                         | Recommended.                                                          |
| [WPD\_OBJECT\_DATE\_AUTHORED](https://www.bing.com/search?q=WPD\_OBJECT\_DATE\_AUTHORED)                                         | Optional.                                                             |
| [WPD\_OBJECT\_BACK\_REFERENCES](https://www.bing.com/search?q=WPD\_OBJECT\_BACK\_REFERENCES)                                     | Recommended if the object is referenced by another object.            |
| [WPD\_OBJECT\_CONTAINER\_FUNCTIONAL\_OBJECT\_ID](https://www.bing.com/search?q=WPD\_OBJECT\_CONTAINER\_FUNCTIONAL\_OBJECT\_ID)     | Optional.                                                             |
| [WPD\_OBJECT\_GENERATE\_THUMBNAIL\_FROM\_RESOURCE](https://www.bing.com/search?q=WPD\_OBJECT\_GENERATE\_THUMBNAIL\_FROM\_RESOURCE) | Optional.                                                             |
| [WPD\_OBJECT\_CAN\_DELETE](https://www.bing.com/search?q=WPD\_OBJECT\_CAN\_DELETE)                                               | Required if the object can be deleted.                                |
| [WPD\_OBJECT\_LANGUAGE\_LOCALE](object-properties.md)                                                                | Required if the object cannot be deleted.                             |
| [WPD\_MEDIA\_COPYRIGHT](https://www.bing.com/search?q=WPD\_MEDIA\_COPYRIGHT)                                                     | Optional.                                                             |
| [WPD\_MEDIA\_PARENTAL\_RATING](https://www.bing.com/search?q=WPD\_MEDIA\_PARENTAL\_RATING)                                        | Optional.                                                             |
| [WPD\_MEDIA\_META\_GENRE](https://www.bing.com/search?q=WPD\_MEDIA\_META\_GENRE)                                                  | Optional.                                                             |
| [WPD\_MEDIA\_SUB\_TITLE](https://www.bing.com/search?q=WPD\_MEDIA\_SUB\_TITLE)                                                    | Optional.                                                             |
| [WPD\_MEDIA\_RELEASE\_DATE](https://www.bing.com/search?q=WPD\_MEDIA\_RELEASE\_DATE)                                              | Recommended.                                                          |
| [WPD\_MEDIA\_TITLE](https://www.bing.com/search?q=WPD\_MEDIA\_TITLE)                                                             | Recommended.                                                          |
| [WPD\_MEDIA\_OWNER](https://www.bing.com/search?q=WPD\_MEDIA\_OWNER)                                                             | Recommended.                                                          |
| [WPD\_MEDIA\_MANAGING\_EDITOR](https://www.bing.com/search?q=WPD\_MEDIA\_MANAGING\_EDITOR)                                        | Recommended.                                                          |
| [WPD\_MEDIA\_WEBMASTER](https://www.bing.com/search?q=WPD\_MEDIA\_WEBMASTER)                                                     | Recommended.                                                          |
| [WPD\_MEDIA\_SOURCE\_URL](https://www.bing.com/search?q=WPD\_MEDIA\_SOURCE\_URL)                                                  | Recommended.                                                          |
| [WPD\_MEDIA\_DESTINATION\_URL](https://www.bing.com/search?q=WPD\_MEDIA\_DESTINATION\_URL)                                        | Recommended.                                                          |
| [WPD\_MEDIA\_DESCRIPTION](https://www.bing.com/search?q=WPD\_MEDIA\_DESCRIPTION)                                                 | Optional.                                                             |
| [WPD\_MEDIA\_GENRE](https://www.bing.com/search?q=WPD\_MEDIA\_GENRE)                                                             | Optional.                                                             |
| [WPD\_MEDIA\_OBJECT\_BOOKMARK](https://www.bing.com/search?q=WPD\_MEDIA\_OBJECT\_BOOKMARK)                                        | Recommended                                                           |
| [WPD\_MEDIA\_LAST\_BUILD\_DATE](https://www.bing.com/search?q=WPD\_MEDIA\_LAST\_BUILD\_DATE)                                       | Recommended.                                                          |
| [WPD\_MEDIA\_TIME\_TO\_LIVE](https://www.bing.com/search?q=WPD\_MEDIA\_TIME\_TO\_LIVE)                                             | Optional.                                                             |
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



|                     |                          |                                                                                 |
|---------------------|--------------------------|---------------------------------------------------------------------------------|
| **Channel Element** | **RSS Feed Requirement** | **Corresponding Mediacast Property**                                            |
| category            | Optional.                | [WPD\_MEDIA\_GENRE](https://www.bing.com/search?q=WPD\_MEDIA\_GENRE)                       |
| cloud               | Not applicable.          | Not applicable.                                                                 |
| copyright           | Optional.                | [WPD\_MEDIA\_COPYRIGHT](https://www.bing.com/search?q=WPD\_MEDIA\_COPYRIGHT)               |
| description         | Required.                | [WPD\_MEDIA\_DESCRIPTION](https://www.bing.com/search?q=WPD\_MEDIA\_DESCRIPTION)           |
| docs                | Not applicable.          | Not applicable.                                                                 |
| generator           | Not applicable.          | Not applicable.                                                                 |
| language            | Not applicable.          | Not applicable.                                                                 |
| lastBuildDate       | Optional.                | [WPD\_MEDIA\_LAST\_BUILD\_DATE](https://www.bing.com/search?q=WPD\_MEDIA\_LAST\_BUILD\_DATE) |
| link                | Required.                | [WPD\_MEDIA\_DESTINATION\_URL](https://www.bing.com/search?q=WPD\_MEDIA\_DESTINATION\_URL)  |
| managingEditor      | Optional.                | [WPD\_MEDIA\_MANAGING\_EDITOR](https://www.bing.com/search?q=WPD\_MEDIA\_MANAGING\_EDITOR)  |
| pubDate             | Optional.                | [WPD\_MEDIA\_RELEASE\_DATE](https://www.bing.com/search?q=WPD\_MEDIA\_RELEASE\_DATE)        |
| rating              | Not applicable.          | Not applicable.                                                                 |
| skipDays            | Not applicable.          | Not applicable.                                                                 |
| skipHours           | Not applicable.          | Not applicable.                                                                 |
| textInput           | Not applicable.          | Not applicable.                                                                 |
| title               | Required.                | [WPD\_OBJECT\_NAME](https://www.bing.com/search?q=WPD\_OBJECT\_NAME)                      |
| ttl                 | Optional.                | [WPD\_MEDIA\_TIME\_TO\_LIVE](https://www.bing.com/search?q=WPD\_MEDIA\_TIME\_TO\_LIVE)       |
| webMaster           | Optional.                | [WPD\_MEDIA\_WEBMASTER](https://www.bing.com/search?q=WPD\_MEDIA\_WEBMASTER)               |



 

The following table lists the image elements in an RSS feed and the corresponding WPD\_CONTENT\_TYPE\_MEDIA\_CAST properties.



|                   |                          |                                                                                |
|-------------------|--------------------------|--------------------------------------------------------------------------------|
| **Image Element** | **RSS Feed Requirement** | **Mediacast Property**                                                         |
| description       | Optional.                | [WPD\_MEDIA\_DESCRIPTION](https://www.bing.com/search?q=WPD\_MEDIA\_DESCRIPTION)          |
| height            | Optional.                | [WPD\_MEDIA\_HEIGHT](https://www.bing.com/search?q=WPD\_MEDIA\_HEIGHT)                    |
| link              | Optional.                | [WPD\_MEDIA\_DESTINATION\_URL](https://www.bing.com/search?q=WPD\_MEDIA\_DESTINATION\_URL) |
| title             | Optional.                | [WPD\_OBJECT\_NAME](https://www.bing.com/search?q=WPD\_OBJECT\_NAME)                     |
| url               | Optional.                | [WPD\_MEDIA\_SOURCE\_URL](https://www.bing.com/search?q=WPD\_MEDIA\_SOURCE\_URL)           |
| width             | Optional.                | [WPD\_MEDIA\_WIDTH](https://www.bing.com/search?q=WPD\_MEDIA\_WIDTH)                      |



 

The following table lists the item elements in an RSS feed and the corresponding WPD\_CONTENT\_TYPE\_MEDIA\_CAST properties.



|                  |               |                          |                                                                                |
|------------------|---------------|--------------------------|--------------------------------------------------------------------------------|
| **Item Element** | **Attribute** | **RSS Feed Requirement** | **Mediacast Property**                                                         |
| author           |               | Optional.                | [WPD\_MEDIA\_ARTIST](https://www.bing.com/search?q=WPD\_MEDIA\_ARTIST)                    |
| category         |               | Optional.                | [WPD\_MEDIA\_GENRE](https://www.bing.com/search?q=WPD\_MEDIA\_GENRE)                      |
|                  | domain        | Not applicable.          | Not applicable.                                                                |
| description      |               | Optional.                | [WPD\_MEDIA\_DESCRIPTION](https://www.bing.com/search?q=WPD\_MEDIA\_DESCRIPTION)          |
| enclosure        |               | Optional.                |                                                                                |
|                  | url           | Required.                | [WPD\_MEDIA\_SOURCE\_URL](https://www.bing.com/search?q=WPD\_MEDIA\_SOURCE\_URL)           |
|                  | length        | Required.                | [WPD\_OBJECT\_SIZE](https://www.bing.com/search?q=WPD\_OBJECT\_SIZE)                     |
|                  | type          | Required.                | (The MIME type should be mapped to the property content type.)                 |
| guid             |               | Optional.                | [WPD\_MEDIA\_GUID](https://www.bing.com/search?q=WPD\_MEDIA\_GUID)                        |
|                  | isPermaLink   | Not applicable.          | Not applicable.                                                                |
| link             |               | Optional.                | [WPD\_MEDIA\_DESTINATION\_URL](https://www.bing.com/search?q=WPD\_MEDIA\_DESTINATION\_URL) |
| pubDate          |               | Optional.                | [WPD\_MEDIA\_RELEASE\_DATE](https://www.bing.com/search?q=WPD\_MEDIA\_RELEASE\_DATE)       |
| source           |               | Not applicable.          | Not applicable.                                                                |
| title            |               | Optional.                | [WPD\_OBJECT\_NAME](https://www.bing.com/search?q=WPD\_OBJECT\_NAME)                     |



 

The following example shows a complete RSS feed for a fictitious podcast supplied by the CEO of a publishing company.


```C++
<channel>
    <title>The Digital Publication</title>
    <link>http://www.lucernepublishing.com/podcasting</link>
    <description>Lucerne Publishing CEO Peter Bankov takes a look at the latest trends in online publications.</description>
    <language>en-us</language>
    <copyright>2006 Lucerne Publishing LP, LLLP. All Rights Reserved.</copyright>
    <managingEditor>someone@example.com</managingEditor>
    <webMaster>someone@example.com</webMaster>
    <pubDate>Fri, 9 June 2006 14:00:28 EDT</pubDate>
    <lastBuildDate Fri, 9 June 2006 14:00:28 EDT />
    <category>News</category>
    <generator>Podcaster version 1.0</generator>
    <docs>http://www.lucernepublishing.com/tech/rss</docs>
    <cloud />
    <ttl>240</ttl>
    <rating />
    <textInput />
    <skipHours />
    <skipDays />

<image>
     <url>http://www.lucernepublishing.com/images/logo.gif</url>
     <title>Lucerne Publishing</title>
     <link>http://www.lucernepublishing.com/community/podcasts</link>
     <width>300</width>
     <height>300</height>
     <description>Lucerne Logo</description>
</image>

<item>
    <title>The Digital Publication</title>
    <link>http://www.lucernepublishing.com/services/podcasting/digital.publishing/audio/2006/06/digital0601.mp3</link>
    <description>Online publications are rapidly changing. A publishing house CEO examines the trends of the past 5 years and their implications.</description>
    <author>Lucerne</author>
    <category>News</category>
    <comments />
    <enclosure url="http://www.lucernepublishing/services/podcasting/digital.publishing/audio/2006/06/digital0601.mp3" length="10329011" type="audio/mpeg" />
    <guid>http://www.lucernepublishing/services/podcasting/digital.publishing/audio/2006/06/digital0601.mp3</guid>
    <pubDate>Thur, 1 June 2006 14:00:28 EDT</pubDate>
    <source />
</item>

</channel>
```



## Mapping RSS Channel Elements to WPD Property Values

The following table describes how the values in the RSS channel elements in the previous example map to particular WPD properties.



|                                                                                              |                                                                                               |
|----------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|
| **WPD Property**                                                                             | **Value**                                                                                     |
| [WPD\_MEDIA\_COPYRIGHT](https://www.bing.com/search?q=WPD\_MEDIA\_COPYRIGHT)                            | 2006 Lucerne Publishing LP, LLLP. All Rights Reserved.                                        |
| [WPD\_MEDIA\_DESCRIPTION](https://www.bing.com/search?q=WPD\_MEDIA\_DESCRIPTION)                        | Lucerne Publishing CEO Peter Bankov takes a look at the latest trends in online publications. |
| [WPD\_MEDIA\_DESTINATION\_URL](https://www.bing.com/search?q=WPD\_MEDIA\_DESTINATION\_URL)               | http://www.lucernepublishing.com/services/podcasting                                          |
| [WPD\_MEDIA\_GENRE](https://www.bing.com/search?q=WPD\_MEDIA\_GENRE)                                    | News                                                                                          |
| [WPD\_MEDIA\_LAST\_BUILD\_DATE](https://www.bing.com/search?q=WPD\_MEDIA\_LAST\_BUILD\_DATE)              | Fri, 9 June 2006 14:00:28 EDT                                                                 |
| [WPD\_MEDIA\_MANAGING\_EDITOR](https://www.bing.com/search?q=WPD\_MEDIA\_MANAGING\_EDITOR)               | someone@example.com                                                                           |
| [WPD\_MEDIA\_RELEASE\_DATE](https://www.bing.com/search?q=WPD\_MEDIA\_RELEASE\_DATE)                     | Fri, 9 June 2006 14:00:28 EDT                                                                 |
| [WPD\_MEDIA\_TIME\_TO\_LIVE](https://www.bing.com/search?q=WPD\_MEDIA\_TIME\_TO\_LIVE)                    | 240                                                                                           |
| [WPD\_MEDIA\_TITLE](https://www.bing.com/search?q=WPD\_MEDIA\_TITLE)                                    | The Digital Publication                                                                       |
| [WPD\_MEDIA\_SOURCE\_URL](https://www.bing.com/search?q=WPD\_MEDIA\_SOURCE\_URL)                         | http://www.lucernepublishing/services/podcasting/digital.publication/rss.xml                  |
| [WPD\_MEDIA\_WEBMASTER](https://www.bing.com/search?q=WPD\_MEDIA\_WEBMASTER)                            | someone@example.com                                                                           |
| [WPD\_OBJECT\_CONTENT\_TYPE](https://www.bing.com/search?q=WPD\_OBJECT\_CONTENT\_TYPE)                  | WPD\_CONTENT\_TYPE\_MEDIA\_CAST                                                               |
| [WPD\_OBJECT\_DATE\_AUTHORED](https://www.bing.com/search?q=WPD\_OBJECT\_DATE\_AUTHORED)                | Fri, 9 June 2006 14:00:28 EDT                                                                 |
| [WPD\_OBJECT\_DATE\_CREATED](https://www.bing.com/search?q=WPD\_OBJECT\_DATE\_CREATED)                  | Fri, 9 June 2006 14:00:28 EDT                                                                 |
| [WPD\_OBJECT\_DATE\_MODIFIED](https://www.bing.com/search?q=WPD\_OBJECT\_DATE\_MODIFIED)                | Fri, 9 June 2006 14:00:28 EDT                                                                 |
| [WPD\_OBJECT\_FORMAT](https://www.bing.com/search?q=WPD\_OBJECT\_FORMAT)                               | WPD\_OBJECT\_FORMAT\_ABSTRACT\_MEDIA\_CAST                                                    |
| [WPD\_OBJECT\_ID](https://www.bing.com/search?q=WPD\_OBJECT\_ID)                                       | Session dependent value.                                                                      |
| [WPD\_OBJECT\_NAME](https://www.bing.com/search?q=WPD\_OBJECT\_NAME)                                   | The Digital Publication                                                                       |
| [WPD\_OBJECT\_ORIGINAL\_FILE\_NAME](https://www.bing.com/search?q=WPD\_OBJECT\_ORIGINAL\_FILE\_NAME)     | The Digital Publication                                                                       |
| [WPD\_OBJECT\_PARENT\_ID](https://www.bing.com/search?q=WPD\_OBJECT\_PARENT\_ID)                        | MyPodcasts (a fictitious podcast folder on the device). Assume "0A0" for this example.        |
| [WPD\_OBJECT\_PERSISTENT\_UNIQUE\_ID](https://www.bing.com/search?q=WPD\_OBJECT\_PERSISTENT\_UNIQUE\_ID) | Session independent value. (Assume "0A1" for this example.)                                   |
| [WPD\_OBJECT\_REFERENCES](https://www.bing.com/search?q=WPD\_OBJECT\_REFERENCES)                       | 0A2  for N items<br/>                                                                   |
| [WPD\_OBJECT\_SIZE](https://www.bing.com/search?q=WPD\_OBJECT\_SIZE)                                   | 13,790                                                                                        |



 

## Mapping RSS Image Elements to WPD Property Values

The following table describes how the values in the RSS Image elements in the previous example map to particular WPD properties.



|                                                                                                                         |                                                     |
|-------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------|
| **WPD Property**                                                                                                        | **Value**                                           |
| [WPD\_MEDIA\_DESCRIPTION](https://www.bing.com/search?q=WPD\_MEDIA\_DESCRIPTION)                                                   | Lucerne Logo                                        |
| [WPD\_MEDIA\_DESTINATION\_URL](https://www.bing.com/search?q=WPD\_MEDIA\_DESTINATION\_URL)                                          | http://www.lucernepublishing.com/community/podcasts |
| [WPD\_MEDIA\_HEIGHT](https://www.bing.com/search?q=WPD\_MEDIA\_HEIGHT)                                                             | 300                                                 |
| [WPD\_MEDIA\_SOURCE\_URL](https://www.bing.com/search?q=WPD\_MEDIA\_SOURCE\_URL)                                                    | http://www.lucernepublishing.com/images/logo.gif    |
| [WPD\_MEDIA\_WIDTH](https://www.bing.com/search?q=WPD\_MEDIA\_WIDTH)                                                               | 300                                                 |
| [WPD\_OBJECT\_NAME](https://www.bing.com/search?q=WPD\_OBJECT\_NAME)                                                              | Lucerne Publishing                                  |
| [WPD\_RESOURCE\_ATTRIBUTE\_CAN\_DELETE](https://www.bing.com/search?q=WPD\_RESOURCE\_ATTRIBUTE\_CAN\_DELETE)                               | VARIANT\_TRUE                                       |
| [WPD\_RESOURCE\_ATTRIBUTE\_CAN\_READ](https://www.bing.com/search?q=WPD\_RESOURCE\_ATTRIBUTE\_CAN\_READ)                                   | VARIANT\_TRUE                                       |
| [WPD\_RESOURCE\_ATTRIBUTE\_FORMAT](https://www.bing.com/search?q=WPD\_RESOURCE\_ATTRIBUTE\_FORMAT)                     | WPD\_OBJECT\_FORMAT\_GIF                            |
| [WPD\_RESOURCE\_ATTRIBUTE\_OPTIMAL\_READ\_BUFFER\_SIZE](https://www.bing.com/search?q=WPD\_RESOURCE\_ATTRIBUTE\_OPTIMAL\_READ\_BUFFER\_SIZE) | 1024                                                |
| [WPD\_RESOURCE\_ATTRIBUTE\_TOTAL\_SIZE](https://www.bing.com/search?q=WPD\_RESOURCE\_ATTRIBUTE\_TOTAL\_SIZE)            | 512                                                 |



 

## Mapping RSS Item Elements to WPD Property Values

The following table describes how the values in the RSS Item elements in the previous example map to particular WPD properties.



|                                                                                              |                                                                                                                                  |
|----------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|
| **WPD Property**<br/>                                                                  | **Value**                                                                                                                        |
| [WPD\_MEDIA\_TITLE](https://www.bing.com/search?q=WPD\_MEDIA\_TITLE)                                    | The Digital Publication                                                                                                          |
| [WPD\_MEDIA\_DURATION](https://www.bing.com/search?q=WPD\_MEDIA\_DURATION)                              | 10329011                                                                                                                         |
| [WPD\_MEDIA\_ARTIST](https://www.bing.com/search?q=WPD\_MEDIA\_ARTIST)                                  | Lucerne                                                                                                                          |
| [WPD\_MEDIA\_DESCRIPTION](https://www.bing.com/search?q=WPD\_MEDIA\_DESCRIPTION)                        | Online publications are rapidly changing. A publishing house CEO examines the trends of the past 5 years and their implications. |
| [WPD\_MEDIA\_DESTINATION\_URL](https://www.bing.com/search?q=WPD\_MEDIA\_DESTINATION\_URL)               | http://www.lucernepublishing/services/podcasting/digital.publishing/audio/2006/06/digital0601.mp3                                |
| [WPD\_MEDIA\_GENRE](https://www.bing.com/search?q=WPD\_MEDIA\_GENRE)                                    | News                                                                                                                             |
| [WPD\_MEDIA\_GUID](https://www.bing.com/search?q=WPD\_MEDIA\_GUID)                                      | http://www.lucernepublishing/services/podcasting/digital.publishing/audio/2006/06/digital0601.mp3                                |
| [WPD\_MEDIA\_RELEASE\_DATE](https://www.bing.com/search?q=WPD\_MEDIA\_RELEASE\_DATE)                     | Thur, 1 June 2006 14:00:28 EDT                                                                                                   |
| [WPD\_MEDIA\_SOURCE\_URL](https://www.bing.com/search?q=WPD\_MEDIA\_SOURCE\_URL)                         | http://www.lucernepublishing/services/podcasting/digital.publishing/audio/2006/06/digital0601.mp3                                |
| [WPD\_OBJECT\_BACK\_REFERENCES](https://www.bing.com/search?q=WPD\_OBJECT\_BACK\_REFERENCES)            | 0A1                                                                                                                              |
| [WPD\_OBJECT\_CONTENT\_TYPE](https://www.bing.com/search?q=WPD\_OBJECT\_CONTENT\_TYPE)                  | WPD\_CONTENT\_TYPE\_MEDIA\_IMAGE                                                                                                 |
| [WPD\_OBJECT\_DATE\_AUTHORED](https://www.bing.com/search?q=WPD\_OBJECT\_DATE\_AUTHORED)                | Thur, 1 June 2006 14:00:28 EDT                                                                                                   |
| [WPD\_OBJECT\_DATE\_CREATED](https://www.bing.com/search?q=WPD\_OBJECT\_DATE\_CREATED)                  | Thur, 1 June 2006 14:00:28 EDT                                                                                                   |
| [WPD\_OBJECT\_DATE\_MODIFIED](https://www.bing.com/search?q=WPD\_OBJECT\_DATE\_MODIFIED)                | Thur, 1 June 2006 14:00:28 EDT                                                                                                   |
| [WPD\_OBJECT\_FORMAT](https://www.bing.com/search?q=WPD\_OBJECT\_FORMAT)                               | WPD\_OBJECT\_FORMAT\_MP3                                                                                                         |
| [WPD\_OBJECT\_ID](https://www.bing.com/search?q=WPD\_OBJECT\_ID)                                       | Session dependent. (Assume "0A2" for this example.)                                                                              |
| [WPD\_OBJECT\_NAME](https://www.bing.com/search?q=WPD\_OBJECT\_NAME)                                   | The Digital Publication                                                                                                          |
| [WPD\_OBJECT\_ORIGINAL\_FILE\_NAME](https://www.bing.com/search?q=WPD\_OBJECT\_ORIGINAL\_FILE\_NAME)     | digital0601.mp3                                                                                                                  |
| [WPD\_OBJECT\_PARENT\_ID](https://www.bing.com/search?q=WPD\_OBJECT\_PARENT\_ID)                        | 0A0                                                                                                                              |
| [WPD\_OBJECT\_PERSISTENT\_UNIQUE\_ID](https://www.bing.com/search?q=WPD\_OBJECT\_PERSISTENT\_UNIQUE\_ID) | Session independent.                                                                                                             |
| [WPD\_OBJECT\_SIZE](https://www.bing.com/search?q=WPD\_OBJECT\_SIZE)                                   | 10329011                                                                                                                         |



 

## Related topics

<dl> <dt>

[**Requirements for Objects**](requirements-for-objects.md)
</dt> </dl>

 

 




