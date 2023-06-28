---
title: Logging Stream Data
description: Logging Stream Data
ms.assetid: c902a755-afdd-4dea-bc3e-036555fdff10
keywords:
- Windows Media metafile playlists,logging stream data
- playlists,logging stream data
- metafile playlists,logging stream data
- Windows Media metafile playlists,stream data logging
- playlists,stream data logging
- metafile playlists,stream data logging
- logging stream data
- stream data logging
- Windows Media Player,logging stream data
- Windows Media Player,stream data logging
ms.topic: article
ms.date: 4/26/2023
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
ms.custom: UpdateFrequency5
---

# Logging Stream Data

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Logged information can be acquired and used to determine viewer behavior, for example, how often a stream is viewed, or if a specific user viewed a stream and for how long at what quality.

Logging information is automatically sent to the server from which the playlist originated. You can also send logging information to additional servers, including web servers you use exclusively for logging. To do this, use the **LOGURL** element, specifying a valid URL for the **HREF** attribute. You can include **LOGURL** elements as children of the **ASX** element and as children of individual **ENTRY** elements. When the playlist is first opened, logging information is sent to the origin server and to each URL specified in **LOGURL** children of the **ASX** element. Then, as each entry is reached, logging information specific to that entry is sent to each URL specified in **LOGURL** children of the **ENTRY** element.

The Windows Media Format SDK supports the **LOGURL** element through the **IWMSReaderNetworkConfig** interface and the following methods:


```XML
HRESULT AddLoggingUrl(LPCWSTR pwszUrl);
HRESULT GetLoggingUrl(DWORD dwIndex, LPCWSTR pwszUrl, DWORD *pcchUrl);
HRESULT GetLoggingUrlCount(DWORD *pdwUrlCount);
HRESULT ResetLoggingUrlList();

```



In addition to the information that is automatically logged, a metafile playlist can log custom information through the use of the **PARAM** element. To use the **PARAM** element in this way, set the **NAME** attribute to "log:" followed by a log field name and an optional XML namespace separated from the field name by another colon (":"). Everything after the second colon is treated as a namespace, so the field name should not contain a colon.

The log field specified in the **NAME** attribute is set to the value of the **VALUE** attribute. If the log does not already contain a field with the specified name, it will be added.

**Example Code**


```XML

    <ASX version="3.0">
      <LOGURL href="https://www.proseware.com/log.asp?SomeArg=SomeVal" />
      <ENTRY>
        <REF href="mms://ucast.proseware.com/Media1.wma" />
        <LOGURL href="https://www.proseware.com/cgi-bin/logging.pl?SomeArg=SomeVal" />
        <LOGURL href="https://www.proseware.com/WMLogging.dll?SomeArg=SomeVal" />
        <PARAM name="log:cs-media-role" value="Advertisement"/>
        <PARAM name="log:cs-media-name:namespace" value="Music"/>
        <REF href=rtsp://ucast.proseware.com/Media1.wma"/>
      </ENTRY>
      <ENTRY>
        <REF href="mms://ucast.proseware.com/Media2.wma"/>
      </ENTRY>
    </ASX>
    

```



## Related topics

<dl> <dt>

[**Metafile Playlists**](metafile-playlists.md)
</dt> <dt>

[**Windows Media Metafile Elements Reference**](windows-media-metafile-elements-reference.md)
</dt> </dl>

 

 




