---
title: Default Networking Settings
description: Default Networking Settings
ms.assetid: 07464107-9cf7-4ed0-a76b-17ea153399a1
keywords:
- Windows Media Format SDK,default networking settings
- Advanced Systems Format (ASF),default networking settings
- ASF (Advanced Systems Format),default networking settings
- Windows Media Format SDK,networking settings
- Advanced Systems Format (ASF),networking settings
- ASF (Advanced Systems Format),networking settings
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Default Networking Settings

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The following tables describe the default settings of the networking parameters in the Windows Media Format SDK, grouped by interface.



| IWMReaderNetworkConfig                | Default setting              |
|---------------------------------------|------------------------------|
| Buffering time                        | 5 seconds                    |
| UseFixedUDPPort                       | FALSE                        |
| FixedUDPPort                          | 0 (not valid)                |
| ProxySetting: HTTP                    | WMT\_PROXY\_SETTING\_BROWSER |
| ProxySetting: MMS                     | WMT\_PROXY\_SETTING\_NONE    |
| ProxySetting: RTSP                    | WMT\_PROXY\_SETTING\_NONE    |
| ProxyHostName (HTTP, MMS, RTSP)       | ""                           |
| ProxyPort: HTTP                       | 80                           |
| ProxyPort: MMS                        | 1755                         |
| ProxtPort: RTSP                       | 554                          |
| ProxyExceptionList (HTTP, MMS, RTSP)  | ""                           |
| ProxyBypassForLocal (HTTP, MMS, RTSP) | FALSE                        |
| ForceRerunAutoDetection               | FALSE                        |
| EnableMulticast                       | TRUE                         |
| EnableHTTP                            | TRUE                         |
| EnableTCP                             | TRUE                         |
| EnableUDP                             | TRUE                         |
| Connection Bandwidth                  | 0 (auto-detect)              |



 



| IWMReaderNetworkConfig2        | Default setting        |
|--------------------------------|------------------------|
| Accelerated streaming duration | 100000000 (10 seconds) |
| Enable content caching         | TRUE                   |
| Enable fast cache              | TRUE                   |
| Enable resends                 | TRUE                   |
| Enable content thinning        | TRUE                   |
| Reconnect limit                | 25                     |



 



| IWMWriterNetworkSink | Default setting         |
|----------------------|-------------------------|
| Maximum clients      | 5                       |
| Network protocol     | 0 (WMT\_PROTOCOL\_HTTP) |
| Host URL             | 0 (not valid)           |



 



| IWMWriterAdvanced2  | Default setting             |
|---------------------|-----------------------------|
| Maximum packet size | 1400                        |
| Log client ID       | FALSE                       |
| Play mode           | WMT\_PLAY\_MODE\_AUTOSELECT |



 

## Related topics

<dl> <dt>

[**Implementing Network Functionality**](implementing-network-functionality.md)
</dt> </dl>

 

 




