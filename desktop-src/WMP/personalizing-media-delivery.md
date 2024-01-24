---
title: Personalizing Media Delivery
description: Personalizing Media Delivery
ms.assetid: ffd62602-8bfc-4ca7-91fd-c610faa330cd
keywords:
- Windows Media metafile playlists,personalizing media delivery
- playlists,personalizing media delivery
- metafile playlists,personalizing media delivery
- Windows Media metafile playlists,media delivery personalization
- playlists,media delivery personalization
- metafile playlists,media delivery personalization
- media delivery personalization
- personalizing media delivery
ms.topic: article
ms.date: 4/26/2023
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
ms.custom: UpdateFrequency5
---

# Personalizing Media Delivery

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Unlike one-way communication that broadcasts identical content to a mass audience, Windows Media Technologies provides you with the tools to use demographics to individualize broadcasts. With the Internet, two-way communication on a large scale is readily available. This dynamic interchange of information enables content providers to know their audience and respond with customized presentations.

The following example, using a fictional company, illustrates how delivery of streaming content can be personalized. This discussion assumes that you are familiar with Active Server Pages (ASP, or .asp files) and defining variables.

News Network is a fictional broadcast news organization that has expanded its operations to include a website. The main feature of the site is a section where users can create their own personalized newscasts. Instead of viewing a traditional newscast that is aimed at a mass audience, a user views a complete news program that contains only topics of personal interest. The following sequence describes a typical user experience.

1.  A new user goes to the site, and clicks **Create Your Personal Newscast**.
2.  A preference form opens. On this form, the user answers questions regarding personal preferences, such as favorite news stories, least favorite news stories, hobbies, and usual method of receiving daily news.
3.  The user sends this information, and a few seconds later views a complete, 15-minute, personal newscast containing program content, transitions, and commercials. Selection of each media element, including commercials, is based on the user profile, and is accomplished automatically with Windows Media Technologies components and off-the-shelf Internet tools.

The following list describes how the various tools interact to create a personalized newscast.

1.  The preference form that the user fills out is an Active Server Page (ASP) (Choices.asp). Data obtained from the preference form is analyzed by two server components. One component uses the information to query a Microsoft SQL Server database of news stories. The other component is an ad server that uses a complex set of rules based on contractual requirements and demographics to schedule ads appropriate to the user at that time.
2.  The two databases return different portions of a playlist. The news story database returns a set of appropriate story Entries, and the ad server returns a set of appropriate commercial Entries.
3.  A second ASP page (PlayShow.asp) receives the Entries from the news story database and ad server, and combines those with standard show open, close, and transition Entries. All Entries are then laid out according to the template provided by PlayShow.asp, and the ASP page returns a playlist to the user.
4.  The embedded Windows Media Player control on the user's computer plays the playlist from beginning to end, and the user views a personalized newscast.

The following example is a portion of a playlist file that a user might receive. Ad banners, MOREINFO links, and ABSTRACTS have been added to it.


```XML
<ASX Version="3">
<TITLE>MyPersonalized NewsCast</TITLE>
<ENTRY ClientSkip="no">
    <!<entity type="mdash"/>- Commercial Element 1 -->
    <REF HREF="mms://proseware.com/Commercial.wma" />
    <BANNER HREF="https://www.proseware.com/images/MoreInfo.gif" >
        <MOREINFO HREF="https://www.proseware.com" target="_blank" />
    <ABSTRACT>Courtesy of Windows Media Technologies
    </ABSTRACT>
    </BANNER>
</ENTRY>
<ENTRY>
    <!<entity type="mdash"/>- Program Element 1 -->
    <TITLE>A Celebrity's Life</TITLE>
    <COPYRIGHT>Copyright 2004</COPYRIGHT>
    <REF HREF="mms://proseware.com/SomePath/TheFile.wma" />
    <ABSTRACT>
     :: A celebrity looks back on her career after 40 years in public life.
    </ABSTRACT>
    <COPYRIGHT>Copyright 2004-- All Rights
         Reserved
    </COPYRIGHT>
</ENTRY>

<ENTRY>
    <!<entity type="mdash"/>Program Element 2 -->
    <TITLE>City council votes to build new bicycle path</TITLE>
    <COPYRIGHT>Copyright 2004</COPYRIGHT>
    <REF HREF="mms://proseware.com/SomePath/MyFile.wma" />
    <ABSTRACT>
        :: Some residents opposed changing the landscape in the public parks to accommodate bicycles.
    </ABSTRACT>
    <COPYRIGHT>Copyright 2004 -- All Rights Reserved
    </COPYRIGHT>
</ENTRY>
</ASX>

```



-   The example companies, organizations, products, people and events depicted herein are fictitious. No association with any real company, organization, product, person or event is intended or should be inferred.

## Related topics

<dl> <dt>

[**Creating Metafile Playlists**](creating-metafile-playlists.md)
</dt> <dt>

[**Metafile Playlists**](metafile-playlists.md)
</dt> <dt>

[**Using Metafile Playlists**](using-metafile-playlists.md)
</dt> <dt>

[**Windows Media Metafile Elements Reference**](windows-media-metafile-elements-reference.md)
</dt> <dt>

[**Windows Media Metafile Guide**](windows-media-metafile-guide.md)
</dt> </dl>

 

 




