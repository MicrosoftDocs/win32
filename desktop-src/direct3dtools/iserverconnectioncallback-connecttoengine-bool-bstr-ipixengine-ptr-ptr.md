---
Description: Connect to another instance of a remote engine on the local machine.
MS-HAID: vspixengine.IServerConnectionCallback\_ConnectToEngine\_BOOL\_BSTR\_IPixEngine\_ptr\_ptr
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/desktop
title: IServerConnectionCallback::ConnectToEngine method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# <span id="vspixengine.iserverconnectioncallback_connecttoengine_bool_bstr_ipixengine_ptr_ptr"></span>IServerConnectionCallback::ConnectToEngine method

Connect to another instance of a remote engine on the local machine.

## Syntax


```C++
);
```

## Parameters

*bLegacyConnection*   
true if the engine uses is legacy, otherwise false.

*runAddress*   
A COM string containing the name of the local machine.

*ppEngineCreated*   
On return, the address of the engine instance.

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements

<table><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td><p>Header</p></td><td>Vspixengine.h</td></tr></tbody></table>

## <span id="see_also"></span>See also

[**IServerConnectionCallback**](https://msdn.microsoft.com/library/windows/desktop/mt432796)

 

 



