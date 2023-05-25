---
title: LOGURL Element
description: The LOGURL element instructs Windows Media Player to submit any log data to the specified URL.
ms.assetid: fc1895af-c9d7-43ca-9839-7e884cc219f4
keywords:
- LOGURL Element Windows Media Player
topic_type:
- apiref
api_name:
- LOGURL Element
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
api_location: 
ms.custom: UpdateFrequency5
---

# LOGURL Element

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **LOGURL** element instructs Windows Media Player to submit any log data to the specified URL.

``` syntax
<LOGURL
   HREF = "URL"
/>
```

## Attributes

**HREF** (required)

URL to a host that is able to process logging requests.

## Parent/Child Elements



| Hierarchy       | Elements           |
|-----------------|--------------------|
| Parent elements | **ASX**, **ENTRY** |
| Child elements  | None               |



 

## Remarks

The **LOGURL** element enables a client metafile playlist to send additional logging information to specified servers. Logging information is automatically sent to the origin server of a playlist when it is opened and to each **LOGURL** specified for the **ASX** element, if any are present. Logging information is also sent to each **LOGURL** specified for an **ENTRY** element when that entry is reached. The URL specified in the **HREF** attribute of a **LOGURL** element must be the address of a host that is able to process logging requests. The URL can be any valid HTTP URL. The URL can also indicate the location of a CGI script.

The only valid protocols for a **LOGURL** element are HTTP and HTTPS.

A **LOGURL** element within the scope of an **ASX** element is applicable only to the metafile in which it resides, regardless of whether that metafile is referenced from another metafile. A **LOGURL** element forces the submission of log data for all content streamed from within its defined scope and only for content streamed from within its defined scope. Log data will be submitted to the origin server and to all URLs listed in every **LOGURL** element in scope. Log data will be submitted only once to each listed URL, even if the same URL is listed more than once in a given scope. A repeat of an **ENTRY** would result in another submission to the listed URLs.

There is no limit to the number of **LOGURL** elements in a metafile playlist.

## Examples


```XML
<ASX VERSION="3.0">
  <TITLE>Example Media Player Show</TITLE>
  <LOGURL HREF="https://example.microsoft.com/info/showlog.asp?whatsup" />
  <ENTRY>
    <REF href="mms://ucast.proseware.com/Media1.asf" />
    <LOGURL HREF="https://www.proseware.com/cgi-bin/logging.pl?SomeArg=SomeVal"/>
  </ENTRY>
</ASX>
```



The following are examples of valid URLs.

URL of an ISAPI application:


```XML
https://www.proseware.com/logs/WMSLogging.dll
```



URL of a CGI script:


```XML
https://www.proseware.com/cgi-bin/My_WMS_Logging_Script.pl
```



A valid HTTP URL:


```XML
https://www.proseware.com/some/arbitrary/path/My_WMS_Logging_Page.asp?PubPoint=FooPubPoint&AnotherName=AnotherValue
```



## Requirements



| Requirement | Value |
|--------------------|-----------------------------------------------------|
| Version<br/> | Windows Media Player version 70 or later<br/> |



## See also

<dl> <dt>

[**Windows Media Metafile Elements Reference**](windows-media-metafile-elements-reference.md)
</dt> <dt>

[**Windows Media Metafile Reference**](windows-media-metafile-reference.md)
</dt> </dl>

 

 





