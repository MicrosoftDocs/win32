---
description: Media Detector (MediaDet)
ms.assetid: 5cdbb6ca-d2c3-4123-b545-198863fed25f
title: Media Detector (MediaDet)
ms.topic: article
ms.date: 05/31/2018
---

# Media Detector (MediaDet)

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The Media Detector (MediaDet) object retrieves format information and still frames from file sources. The Media Detector does not require the Filter Graph Manager to function. To create this object, call **CoCreateInstance**. The class identifier is CLSID\_MediaDet.

To read Windows Media™ files, the application must provide a software certificate, also called a key. Register the application as a key provider through the Media Detector's **IObjectWithSite** interface. For more information, see [Unlocking the Windows Media Format SDK](unlocking-the-windows-media-format-sdk.md).

The MediaDet object exposes the following interfaces:

-   [**IMediaDet**](imediadet.md)
-   **IObjectWithSite**

## Related topics

<dl> <dt>

[Working with Sources](working-with-sources.md)
</dt> </dl>

 

 



