---
Description: Wait for shutdown of the specified engine (Blocking call).
MS-HAID: vspixengine.IServerConnectionCallback\_WaitForShutdown\_IPixEngine\_ptr
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/desktop
title: IServerConnectionCallback::WaitForShutdown method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# <span id="vspixengine.iserverconnectioncallback_waitforshutdown_ipixengine_ptr"></span>IServerConnectionCallback::WaitForShutdown method

Wait for shutdown of the specified engine (Blocking call).

## Syntax


```C++
);
```

## Parameters

*pEngine*   
The engine to shut down.

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements

<table><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td><p>Header</p></td><td>Vspixengine.h</td></tr></tbody></table>

## <span id="see_also"></span>See also

[**IServerConnectionCallback**](https://msdn.microsoft.com/library/windows/desktop/mt432796)

 

 



