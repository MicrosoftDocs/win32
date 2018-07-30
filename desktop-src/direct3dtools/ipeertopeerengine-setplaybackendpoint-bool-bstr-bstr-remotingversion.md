---
Description: Sets the endpoint address used to connect to a remote engine.
MS-HAID: vspixengine.IPeerToPeerEngine\_SetPlaybackEndpoint\_BOOL\_BSTR\_BSTR\_RemotingVersion
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/desktop
title: IPeerToPeerEngine::SetPlaybackEndpoint method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# <span id="vspixengine.ipeertopeerengine_setplaybackendpoint_bool_bstr_bstr_remotingversion"></span>IPeerToPeerEngine::SetPlaybackEndpoint method

Sets the endpoint address used to connect to a remote engine.

## Syntax


```C++
);
```

## Parameters

*bUseAuthentication*   
true to use authentication; otherwise, false.

*endpoint*   
A COM string containing the endpoint address.

*sessionKey*   
A COM string containing the session key used for encryption.

*remoteVersion*   
Specifies the version of the remote engine to use.

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements

<table><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td><p>Header</p></td><td>Vspixengine.h</td></tr></tbody></table>

## <span id="see_also"></span>See also

[**IPeerToPeerEngine**](https://msdn.microsoft.com/library/windows/desktop/mt432712)

 

 



