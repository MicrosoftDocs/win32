---
title: ServiceInfo Document for a Type 2 Online Store
description: ServiceInfo Document for a Type 2 Online Store
ms.assetid: 'ca83e9bf-c7fb-4212-8fa2-1fae11ed26e9'
keywords:
- Windows Media Player online stores,ServiceInfo document
- online stores,ServiceInfo document
- type 2 online stores,ServiceInfo document
- ServiceInfo document
ms.topic: article
ms.date: 05/31/2018
---

# ServiceInfo Document for a Type 2 Online Store

Type 2 online store providers must provide Microsoft with the URL of an XML document that describes the online store. Windows Media Player 10 and Windows Media Player 11 use this document to determine how to configure the user interface to host the online store.

In Windows Media Player 10, the ServiceInfo document provides the following:

-   Information about how to configure the task panes that Windows Media Player displays when the online store is active. An online store can have one, two, or three task panes.
-   Information used to configure the task pane buttons, such as the button text, the button color, and tool tips for the buttons.
-   URLs for images that Windows Media Player displays to identify the online store.
-   URLs of webpages, provided by the online store, that Windows Media Player hosts in its user interface.
-   Information about how Windows Media Player setup should configure the first online store the user sees.

In Windows Media Player 11, the ServiceInfo document provides the following:

-   Information used to configure the button for Online Stores tab, such as the button text and the tool tip for the button.
-   URLs for images that Windows Media Player displays to identify the online store.
-   URLs of webpages, provided by the online store, that Windows Media Player hosts in its user interface.

When you start developing your online store, you must provide Microsoft with the URL to your ServiceInfo document. During the development phase, your online store will appear in Windows Media Player only when a special registry key is set.

After your online store is published, the ususal scenario is that Windows Media Player retrieves your ServiceInfo document from the Web automatically. In some cases, however, Windows Media Player retrieves the ServiceInfo document from the user's computer. For more information, see [Setting the Initial Online Store](setting-the-initial-online-store.md).

When Windows Media Player retrieves the ServiceInfo document from the Web, it appends a query string to the URL. The query string contains parameters that provide information about the user's locale and the Windows Media Player version.

You can create static or dynamic ServiceInfo documents. A static ServiceInfo document has an .xml file name extension. A dynamic ServiceInfo document is an ASP page and has an .asp or .aspx file name extension.

Not all the elements available for use in the ServiceInfo document can be used by every online store, and some elements are optional for all online stores. For information about the types of online stores you can create and the features available for each type, see [Windows Media Player Online Stores](windows-media-player-online-stores.md).

## Related topics

<dl> <dt>

[**About Type 2 Online Stores**](about-type-2-online-stores.md)
</dt> <dt>

[**Creating the ServiceInfo Document Dynamically**](creating-the-serviceinfo-document-dynamically.md)
</dt> <dt>

[**Example ServiceInfo Document for a Type 2 Online Store**](example-serviceinfo-document-for-a-type-2-online-store.md)
</dt> <dt>

[**ServiceInfo Document**](serviceinfo-document.md)
</dt> </dl>

 

 




