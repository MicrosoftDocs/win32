---
description: Learn about client logging for Microsoft Media Foundation. Logging provides a way for the media server to track the activity of the clients that connect to it.
ms.assetid: f91b48ae-3989-4c1d-929c-8ab28d7c8177
title: Client Logging (Microsoft Media Foundation)
ms.topic: article
ms.date: 05/31/2018
---

# Client Logging (Microsoft Media Foundation)

The network source supports client logging, which provides a way for the media server to track the activity of the clients that connect to it. Client logs enable a server to record connection, rendering, and streaming statistics. These logs can be used by content providers in various scenarios, such as, to trace media server usage and generate billing, or to deliver suitable-quality content depending on the speed of the client's network.

A log file contains several client event entries. Each log entry contains a number of space-delimited fields. There are two types of client logs: *rendering* (playing) and *streaming* (receiving). Because content can be played and streamed simultaneously, the client can send a combination of both types of log data. In certain cases, two log entries can exist for the same session. For example, when Fast Cache is enabled, the client can finish receiving the streamed content before it finishes rendering it. In that case, the streaming log data would be sent before the rendering log data.

The client sends rendering log data to the server when the client changes from any playing state (play, fast-forward, or rewind) to a non-playing state (stop, pause, end of stream, and beginning of stream). When data for a rendering log is submitted, a connection is made directly to the media server or a configured proxy server.

If the content is stored in a temporary local cache file on the computer that is running the client, the client can read a file from its local cache and submit the rendering log data to indicate that it has played the content. In this case, the client reads a file from its local cache, the rendering log entry does not contain any network statistics, and the protocol is set to Cache.

The client sends streaming log data to the server to indicate how the client received the content, but not how it was rendered. The client can send the streaming log long before the client finishes rendering the content.

This topic does not provide information about all the log fields. For a complete reference, see [Windows Media Log Data Structure](/openspecs/windows_protocols/ms-wmlog/42c620eb-0d77-4350-b070-bcd1e182fe84).

## Configuring Log Fields

Media Foundation enables the client to configure the network source by using properties. The application must set the appropriate properties in a property store and pass it to one of the source resolver methods. The source resolver creates the network source as requested and opens a connection with the server. If the connection is successful, the client sends information about itself.

The following table describes the log fields and the corresponding properties that an application can set through the source resolver. This information does not change during the session.




| Logging field | Description | 
|---------------|-------------|
| c-playerid | Unique identification of the player. This information is sent at the beginning of the connection. Typically, this is a GUID of the client. The client can send this information to the server in the <a href="mfnetsource-playerid-property.md"><strong>MFNETSOURCE_PLAYERID</strong></a> property.<br /> The client sends this information to the server at the beginning of the connection.<br /> Sample value: "{c579d042-cecc-11d1-bb31-00a0c9603954}"<br /> | 
| c-playerversion | The version number of the player that is sent at the beginning of the connection. The client can send this information to the server in the <a href="mfnetsource-playerversion-property.md"><strong>MFNETSOURCE_PLAYERVERSION</strong></a> property.<br /> The client sends this information to the server at the beginning of the connection.<br /> | 
| cs(User-Agent) | Browser type used if the player was embedded in a browser. This value can be set by the client in the <a href="mfnetsource-browseruseragent-property.md"><strong>MFNETSOURCE_BROWSERUSERAGENT</strong></a> property.<br /> If the player was not embedded, this field refers to the user agent of the client that generated the log. In this case, the client must set the <a href="mfnetsource-playeruseragent-property.md"><strong>MFNETSOURCE_PLAYERUSERAGENT</strong></a> property.<br /> The client sends this information to the server at the beginning of the connection.<br /> Sample value: "Mozilla/4.0_(compatible;_MSIE_4.01;_Windows_98)"<br /> | 
| cs(Referer) | URL of the webpage in which the player was embedded (if it was embedded). The client can send this information to the server in the <a href="mfnetsource-browserwebpage-property.md"><strong>MFNETSOURCE_BROWSERWEBPAGE</strong></a> property.<br /> The client sends this information to the server at the end of the connection.<br /> Sample value: "https://www.example.microsoft.com"<br /> | 
| c-hostexe | For player log entries, the host program (.exe) that was run. For example, a webpage in a browser, a Microsoft Visual Basic applet, or a stand-alone player. The client can send this information to the server in the <a href="mfnetsource-hostexe-property.md"><strong>MFNETSOURCE_HOSTEXE</strong></a> property.<br /> The client sends this information to the server at the end of the connection.<br /> Sample values:<br /><ul><li>"iexplore.exe"</li><li>"myplayer.exe"</li></ul> | 
| c-hostexever | Host program (.exe) version number. The client can send this information to the server in the <a href="mfnetsource-hostversion-property.md"><strong>MFNETSOURCE_HOSTVERSION</strong></a> property.<br /> The client sends this information to the server at the end of the connection.<br /> | 




 

The following code example shows how a client application configures the network source. This example sets the "c-hostexe" log field.


```C++
// Creates a media source from a URL.
//
// This example demonstrates how to set the MFNETSOURCE_HOSTEXE
// configuration property on the network source.

HRESULT CreateMediaSourceWithLogParams(
    PCWSTR pszURL, 
    IMFMediaSource **ppSource
    )
{
    IPropertyStore *pConfig = NULL;

    // Configure the property store.
    HRESULT hr = PSCreateMemoryPropertyStore(IID_PPV_ARGS(&pConfig));

    if (SUCCEEDED(hr))
    {
        PROPERTYKEY key;
        key.fmtid =  MFNETSOURCE_HOSTEXE;
        key.pid = 0;

        PROPVARIANT var;
        var.vt = VT_LPWSTR;
        var.pwszVal = L"MyPlayer.exe";

        hr = pConfig->SetValue(key, var);
    }

    // Create the source media source.
    if (SUCCEEDED(hr))
    {
        hr = CreateMediaSource(pszURL, pConfig, ppSource);
    }

    SafeRelease(&pConfig);
    return hr;
}
```



## Retrieving Network Statistics

When the application calls one of the source resolver methods, it creates the network source, sets the properties specified in the property store, and opens a session with the media server. In addition to the configurable information described in the previous section, additional data is transferred between the server and the client at the beginning of the session, during streaming, and when the session is closed.

The application can retrieve network statistics by using the **MFNETSOURCE\_STATISTICS\_SERVICE** service identifier. To use this service, the application can call the [**MFGetService**](/windows/desktop/api/mfidl/nf-mfidl-mfgetservice) function to get the property store that contains network statistics in the [**MFNETSOURCE\_STATISTICS**](/windows/desktop/api/mfidl/ne-mfidl-mfnetsource_statistics_ids) property. Specific values can be retrieved by providing the corresponding identifier defined in the **MFNETSOURCE\_STATISTICS\_IDS** enumeration.

The following code example shows how to use the service to get the number of packets received by the client.


```C++
HRESULT GetPacketsReceived(IMFMediaSession *pSession, DWORD *pcPackets)
{
    IPropertyStore *pProp = NULL;
    PROPVARIANT var;

    // Get the property store from the media session.
    HRESULT hr = MFGetService(
        pSession, 
        MFNETSOURCE_STATISTICS_SERVICE, 
        IID_PPV_ARGS(&pProp)
        );

    // Get the number of packets received by the client.

    if (SUCCEEDED(hr))
    {
        PROPERTYKEY key;
        key.fmtid = MFNETSOURCE_STATISTICS;
        key.pid = MFNETSOURCE_RECVPACKETS_ID;

        hr = pProp->GetValue(key, &var);
    }

    if (SUCCEEDED(hr))
    {
        *pcPackets = var.lVal;
    }

    PropVariantClear(&var);
    SafeRelease(&pProp);
    return hr;
}
```



The following list describes some of the network statistics identifiers defined in [**MFNETSOURCE\_STATISTICS\_IDS**](/windows/desktop/api/mfidl/ne-mfidl-mfnetsource_statistics_ids).



| Network statistics identifier              | Description                                                                                                                                                                                                                |
|--------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **MFNETSOURCE\_AVGBANDWIDTHBPS\_ID**       | Average bandwidth (in bits per second) at which the client was connected to the server. The value is calculated across the entire duration of the connection.                                                              |
| **MFNETSOURCE\_BUFFERINGCOUNT\_ID**        | Number of times the client buffered while playing the stream.                                                                                                                                                              |
| **MFNETSOURCE\_BYTESRECEIVED\_ID**         | Number of bytes received by the client from the server. The value does not include any overhead that is added by the network stack. The same content streamed by using different protocols can result in different values. |
| **MFNETSOURCE\_LINKBANDWIDTH\_ID**         | Maximum available bandwidth of the client in bits per second.                                                                                                                                                              |
| **MFNETSOURCE\_LOSTPACKETS\_ID**           | Number of packets sent by the server but lost during transmission, and never played by the client. The value does not include TCP or UDP packets.                                                                          |
| **MFNETSOURCE\_RECVPACKETS\_ID**           | Number of packets received from the server The value does not include TCP or UDP packets.                                                                                                                                  |
| **MFNETSOURCE\_RECOVEREDBYECCPACKETS\_ID** | Packets lost in the network that were repaired and recovered at the client layer. This value does not include TCP or UDP packets.                                                                                          |
| **MFNETSOURCE\_RESENDSREQUESTED\_ID**      | The number of requests made by the client to receive new packets. This value does not include TCP or UDP packets.                                                                                                          |
| **MFNETSOURCE\_RECOVEREDPACKETS\_ID**      | Number of packets recovered because they were resent through UDP. This value does not include TCP or UDP packets. This field contains a zero unless the client is using UDP resend.                                        |
| **MFNETSOURCE\_BUFFERPROGRESS\_ID**        | The percentage of the playout buffer filled during buffering.                                                                                                                                                              |
| **MFNETSOURCE\_PROTOCOL\_ID**              | Protocol used to access the stream. This may differ from the protocol requested by the client.                                                                                                                             |
| **MFNETSOURCE\_TRANSPORT\_ID**             | Transport protocol used to deliver the stream. This must be either UDP or TCP.                                                                                                                                             |



 

## Related topics

<dl> <dt>

[Network Source Features](network-source-features.md)
</dt> <dt>

[Networking in Media Foundation](networking-in-media-foundation.md)
</dt> </dl>

 

