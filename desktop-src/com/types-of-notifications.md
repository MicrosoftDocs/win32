---
title: Types of Notifications
description: Types of Notifications
ms.assetid: 1e7f44ea-f4ac-457e-96a3-94036508d7b7
ms.topic: article
ms.date: 05/31/2018
---

# Types of Notifications

Notifications fall into three groups: compound document, data, and view. An object sends compound document notifications in response to being renamed, saved, closed or, in the case of a link, having its link source renamed. As you would expect, objects send data notifications in response to changes in their data and send view notifications in response to changes in their presentation. Container applications must register separately for each of these notification types, but all can be handled by a single advisory sink.

All containers, the object handler, and the linked object register for compound document notifications. The typical container also registers for view notifications. Data notifications are usually sent to both the linked object and object handler. A special purpose container, such as one that renders the data itself, might benefit from receiving data notifications instead of view notifications. For example, an embedded chart container with a link to a table can register for data notifications. Because a change to the table affects the chart, the receipt of a data notification would direct the container to get the new tabular data.

## Related topics

<dl> <dt>

[Notifications](notifications.md)
</dt> </dl>

 

 




