---
title: IAgent Register
description: IAgent Register
ms.assetid: 3592e8ba-979e-4914-8197-17e645806f97
ms.topic: article
ms.date: 05/31/2018
---

# IAgent::Register

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

``` syntax
HRESULT Register(
   IUnknown * punkNotifySink  // IUnknown address for client notification sink
   long * pdwSinkID           // address of the notification sink ID
);
```

Registers a notification sink for the client application.

-   Returns S\_OK to indicate the operation was successful.

<dl> <dt>

<span id="IUnknown"></span><span id="iunknown"></span><span id="IUNKNOWN"></span>*IUnknown*
</dt> <dd>

Address of [**IUnknown**](https://www.bing.com/search?q=**IUnknown**) for your notification sink interface.

</dd> <dt>

<span id="pdwSinkID"></span><span id="pdwsinkid"></span><span id="PDWSINKID"></span>*pdwSinkID*
</dt> <dd>

Address of notification sink ID (used to unregister the notification sink).

</dd> </dl>

You need to register your notification sink (also known as a notify sink or event sink) to receive events from the Microsoft Agent server.

## See Also

[**IAgent::Unregister**](iagent--unregister.md)


 

 




