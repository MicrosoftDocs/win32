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
ms.date: 05/31/2018
---

# Configuration Persistence

None of the write-enabled properties described in this documentation are saved by the Windows Media SDK. Each application that uses the SDK must provide its own persistence procedures as needed and invoke the appropriate set method upon each instance of the SDK. In this way, configuration changes made by one application do not affect another application. For example, changing the buffering time in one player does not affect another player.

The one exception to this rule is for the credentials information. If the application indicates, in its return from the **AcquireCredentials** call, that the user ID and password information must be persisted, the SDK saves this information.

## Related topics

<dl> <dt>

[**Implementing Network Functionality**](implementing-network-functionality.md)
</dt> <dt>

[**IWMCredentialCallback Interface**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmcredentialcallback)
</dt> </dl>

 

 




