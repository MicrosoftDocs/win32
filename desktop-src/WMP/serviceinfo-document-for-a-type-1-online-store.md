---
title: ServiceInfo Document for a Type 1 Online Store
description: ServiceInfo Document for a Type 1 Online Store
ms.assetid: '9ca424a1-c29a-4078-8d56-9d0fea52f150'
keywords:
- Windows Media Player online stores,ServiceInfo document
- online stores,ServiceInfo document
- type 1 online stores,ServiceInfo document
- ServiceInfo document
ms.topic: article
ms.date: 05/31/2018
---

# ServiceInfo Document for a Type 1 Online Store

Type 1 online stores must provide Microsoft with the URL of an XML document that describes the online store. Windows Media Player 11 uses this document to determine how to configure the user interface to host the online store.

The ServiceInfo document for a type 1 store provides the following information to Windows Media Player:

-   Information used to configure the **Online Stores** button (also called a tab), such as the button text, the button color, and the tooltip for the button.
-   URLs for images that Windows Media Player displays to identify the online store.
-   URLs of webpages, provided by the online store, that Windows Media Player hosts in its user interface.
-   URL where Windows Media Player can retrieve the online store's plug-in so that the plug-in can be installed on the user's computer.

When Windows Media Player retrieves the ServiceInfo document from the Web, it appends a query string to the URL. The query string contains parameters that provide information about the user's locale and geographic location and the version of Windows Media Player.

## Related topics

<dl> <dt>

[**About Type 1 Online Stores**](about-type-1-online-stores.md)
</dt> <dt>

[**Creating the ServiceInfo Document Dynamically**](creating-the-serviceinfo-document-dynamically.md)
</dt> <dt>

[**Example ServiceInfo Document for a Type 1 Online Store**](example-serviceinfo-document-for-a-type-1-online-store.md)
</dt> <dt>

[**ServiceInfo Document**](serviceinfo-document.md)
</dt> </dl>

 

 




