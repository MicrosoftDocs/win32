---
title: Service Task Panes
description: Service Task Panes
ms.assetid: 'f626fa85-7590-4e87-bd5c-7ffdcb14be8b'
keywords:
- Windows Media Player online stores,service task panes
- online stores,service task panes
- type 2 online stores,service task panes
- Windows Media Player online stores,task panes
- online stores,task panes
- type 2 online stores,task panes
- Windows Media Player,service task panes
- Windows Media Player,task panes
- service task panes
ms.topic: article
ms.date: 05/31/2018
---

# Service Task Panes

In Windows Media Player 10, online store providers can configure Windows Media Player to display as many as three task panes, called service task panes. Each service task pane is represented by a customizable button that Windows Media Player displays on the right side of the Features taskbar.

Each service task pane hosts a webpage that is the user interface for a particular online store feature.The appearance of the service task panes is defined by the ServiceInfo XML document. In this document, the service task panes are represented by three elements: **ServiceTask1**, **ServiceTask2**, and **ServiceTask3**. These service task panes are intended to provide the following:

-   A music service.
-   A video service.
-   A radio service.

You can position these features in Windows Media Player in any order you like, but **ServiceTask1** must be the primary task pane for engaging in commercial activity.

The webpage hosted in each service task pane has access to the **External** object. This object provides methods, properties, and an event that provide special functionality for webpages in Windows Media Player. For instance, you can use the event and properties from **External** to make the appearance of your webpage match the color scheme that the user has chosen for Windows Media Player.

In Windows Media Player 11, there are no service task panes. Instead, there is a single **Online Stores** tab, which hosts the main webpage for the active online store. In the ServiceInfo document, the **Online Stores** tab is represented by the **ServiceTask1** element; the **ServiceTask2** and **ServiceTask3** elements are ignored.

## Related topics

<dl> <dt>

[**About Type 2 Online Stores**](about-type-2-online-stores.md)
</dt> <dt>

[**External Object for Type 2 Online Stores**](external-object-for-type-2-online-stores.md)
</dt> <dt>

[**ServiceInfo Document for a Type 2 Online Store**](serviceinfo-document-for-a-type-2-online-store.md)
</dt> </dl>

 

 




