---
title: The Default Handler and Custom Handlers
description: The Default Handler and Custom Handlers
ms.assetid: b64617e8-3a71-449d-8948-fd997c1550b3
ms.topic: article
ms.date: 05/31/2018
---

# The Default Handler and Custom Handlers

The default handler, an implementation provided by OLE, is used by most applications as the handler. An application implements a custom handler when the default handler's capabilities are insufficient. A custom handler can either completely replace the default handler or use parts of the functionality it provides where appropriate. In the latter case, the application handler is implemented as an aggregate object composed of a new control object and the default handler. Combination application/default handlers are also known as *in-process handlers*. The *remoting handler* is used for objects that are not assigned a CLSID in the system registry or that have no specified handler. All that is required from a handler for these types of objects is that they pass information across the process boundary.

## Related topics

<dl> <dt>

[Object Handlers](object-handlers.md)
</dt> </dl>

 

 




