---
title: Test and Production Keys for a Type 1 Online Store
description: Test and Production Keys for a Type 1 Online Store
ms.assetid: 1a975c0b-16b8-4da7-8594-316ae34257d0
keywords:
- Windows Media Player online stores,test keys
- online stores,test keys
- type 1 online stores,test keys
- Windows Media Player online stores,production keys
- online stores,production keys
- type 1 online stores,production keys
- Windows Media Player online stores,ServiceInfo document
- online stores,ServiceInfo document
- type 1 online stores,ServiceInfo document
- test keys
- production keys
- ServiceInfo document
ms.topic: article
ms.date: 05/31/2018
---

# Test and Production Keys for a Type 1 Online Store

When you begin development of your online store, Microsoft provides you with two numeric keys: a test key and a production key. At the same time, you must provide Microsoft with two URLs: one that points to your test ServiceInfo document and one that points to your production ServiceInfo document.

During the development and testing stage, your online store is visible in Windows Media Player only if your test key or your production key is in the registry on the user's computer. If your test key is in the registry, Windows Media Player retrieves your test ServiceInfo document, which points to the plug-in, webpages, and images that belong to your test store. If your production key is in the registry, Windows Media Player retrieves your production ServiceInfo document, which points to the plug-in, webpages, and images that belong to your production store.

You can use your test and production stores in any way that you find useful. Typically, however, the distinction is as follows:

-   Your test store is the place where you make daily changes to your plug-in, webpages, images, and other components of your service.
-   Your production store is the place where you keep a stable release of your service, which includes your plug-in, webpages, images, and other components.

Before your online store can be published in Windows Media Player, Microsoft must validate that your service performs correctly. During the validation phase, Microsoft uses your production key. Microsoft does not use your test key during the validation phase.

When your production online store successfully completes the validation process, Microsoft publishes your store, which means that your production store appears in Windows Media Player for all users, not just the ones who have your production key in the registry. After your store is published, the test and production keys are no longer needed.

> [!Note]  
> Users might be able to guess the test or production key for your online store and view your store while it is being developed. You should be careful about exposing features that you want to keep secret until public release.

 

For detailed information about where to put your production and test keys in the user's registry, see [Registry Keys and Entries for a Type 1 Online Store](registry-keys-and-entries-for-a-type-1-online-store.md).

## Related topics

<dl> <dt>

[**About Type 1 Online Stores**](about-type-1-online-stores.md)
</dt> </dl>

 

 




