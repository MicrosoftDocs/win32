---
title: Image Element (WMP SDK)
description: Note This section describes functionality designed for use by online stores. | Image Element (WMP SDK)
ms.assetid: 06804c26-e847-43a7-bb75-60da600c7d4f
keywords:
- Image Element Windows Media Player
topic_type:
- apiref
api_name:
- Image Element
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# Image Element (WMP SDK)

> [!Note]  
> This section describes functionality designed for use by online stores. Use of this functionality outside the context of an online store is not supported.

 

The **Image** element specifies the images that Windows Media Player displays to the user to represent the online store.

``` syntax
<Image
    EulaURL = "URL"
    MenuURL = "URL"
    ServiceLargeURL = "URL"
    ServiceSmallURL = "URL"
/>
```

## Attributes

<dl> <dt>

<span id="EulaURL__required_for_type_1_stores__ignored_for_type_2_"></span><span id="eulaurl__required_for_type_1_stores__ignored_for_type_2_"></span><span id="EULAURL__REQUIRED_FOR_TYPE_1_STORES__IGNORED_FOR_TYPE_2_"></span>**EulaURL** (required for type 1 stores, ignored for type 2)
</dt> <dd>

URL for the logo that Windows Media Player displays in the end user license agreement (EULA) dialog box. This must be a PNG image that is 80 x 80 pixels.

</dd> <dt>

<span id="MenuURL__optional_"></span><span id="menuurl__optional_"></span><span id="MENUURL__OPTIONAL_"></span>**MenuURL** (optional)
</dt> <dd>

URL for the image that Windows Media Player displays on the services menu. This image must be 15 x 15 pixels.

</dd> <dt>

<span id="ServiceLargeURL__optional_"></span><span id="servicelargeurl__optional_"></span><span id="SERVICELARGEURL__OPTIONAL_"></span>**ServiceLargeURL** (optional)
</dt> <dd>

For a type 1 online store, this is the URL for the image that Windows Media Player displays on the **Online Stores** tab. For Windows Media Player 11, this image must be 45 pixels wide by 13 pixels high. For Windows Media Player 12, this image must be 45 pixels wide by 30 pixels high. To support both versions 11 and 12 of Windows Media Player, you must provide two separate ServiceInfo.xml documents, each of which points to the appropriately sized image for ServiceLargeURL.

For a type 2 online store, this is the URL for the image that Windows Media Player displays beside the **Online Stores** tab or beside the task pane buttons. This image must be 30 x 30 pixels.

</dd> <dt>

<span id="ServiceSmallURL__optional_"></span><span id="servicesmallurl__optional_"></span><span id="SERVICESMALLURL__OPTIONAL_"></span>**ServiceSmallURL** (optional)
</dt> <dd>

URL for the logo that is displayed along with the marketing description specified in the **Description** element. If it is not supplied, it will be blank. (All types, optional) This must be a PNG image that is 45 pixels wide and 13 pixels high.

</dd> </dl>

## Parent/Child Elements



| Hierarchy       | Element         |
|-----------------|-----------------|
| Parent elements | **ServiceInfo** |
| Child elements  | None            |



 

## Remarks

The supported image formats are .gif, .jpg, .bmp, and .png (which is the recommended format). Using Web transparency is both supported and recommended. Animated GIF files are not supported.

If you do not supply a value for **MenuURL**, Windows Media Player displays no graphic on the menu for your online store.

You can provide an animated image for ServiceLargeURL. In Windows Media Player 10 or 11, the image is animated. In Windows Media Player 12, only the first frame of the image is displayed. To provide an animated image, create a single image file that contains successive frames of your animation. For example, for an image that is 30 pixels wide and 30 pixels high, you could supply 20 successive images side by side in an image that is 600 pixels wide and 30 pixels high. Windows Media Player would automatically animate such an image by showing the 20 individual images one after another. This animation occurs only once when the online store opens; it does not repeat.

## Requirements



|                    |                                             |
|--------------------|---------------------------------------------|
| Version<br/> | Windows Media Player 10 or later<br/> |



## See also

<dl> <dt>

[**Example ServiceInfo Document for a Type 1 Online Store**](example-serviceinfo-document-for-a-type-1-online-store.md)
</dt> <dt>

[**Example ServiceInfo Document for a Type 2 Online Store**](example-serviceinfo-document-for-a-type-2-online-store.md)
</dt> <dt>

[**ServiceInfo Document**](serviceinfo-document.md)
</dt> </dl>

 

 





