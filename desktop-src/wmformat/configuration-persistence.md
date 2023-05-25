---
title: Configuration Persistence
description: Configuration Persistence
ms.assetid: 0ef1a0a1-767d-4f34-91d8-9d15c46f3954
keywords:
- Windows Media Format SDK,persistence
- Windows Media Format SDK,configuration persistence
- Advanced Systems Format (ASF),persistence
- ASF (Advanced Systems Format),persistence
- Advanced Systems Format (ASF),configuration persistence
- ASF (Advanced Systems Format),configuration persistence
- configuration persistence
- persistence
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Configuration Persistence

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

None of the write-enabled properties described in this documentation are saved by the Windows Media SDK. Each application that uses the SDK must provide its own persistence procedures as needed and invoke the appropriate set method upon each instance of the SDK. In this way, configuration changes made by one application do not affect another application. For example, changing the buffering time in one player does not affect another player.

The one exception to this rule is for the credentials information. If the application indicates, in its return from the **AcquireCredentials** call, that the user ID and password information must be persisted, the SDK saves this information.

## Related topics

<dl> <dt>

[**Implementing Network Functionality**](implementing-network-functionality.md)
</dt> <dt>

[**IWMCredentialCallback Interface**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmcredentialcallback)
</dt> </dl>

 

 




