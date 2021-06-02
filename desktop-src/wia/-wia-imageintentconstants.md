---
description: Image intent constants specify what type of data the image is meant to represent.
ms.assetid: 171228d9-a619-49aa-964e-f72a7f294a9d
title: Image Intent Constants (Wiadef.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- WIA_INTENT_IMAGE_TYPE_COLOR
- WIA_INTENT_IMAGE_TYPE_GRAYSCALE
- WIA_INTENT_IMAGE_TYPE_TEXT
- WIA_INTENT_MINIMIZE_SIZE
- WIA_INTENT_MAXIMIZE_QUALITY
- WIA_INTENT_BEST_PREVIEW
api_type: 
- HeaderDef
api_location: 
- wiadef.h
---

# Image Intent Constants

Image intent constants specify what type of data the image is meant to represent. The [**WIA\_IPS\_CUR\_INTENT**](-wia-wiaitempropscanneritem.md) scanner property uses these flags. To provide an intent, combine an intended image type flag with an intended size/quality flag by using the OR operator. WIA\_INTENT\_NONE should not be combined with any other flags. Note that an image cannot be both grayscale and color.

The following are valid image intent constants:



| Intended image type flags           | Description                                  |
|-------------------------------------|----------------------------------------------|
| WIA\_INTENT\_NONE                   | Default value. Do not preset any properties. |
| WIA\_INTENT\_IMAGE\_TYPE\_COLOR     | Preset properties for color content.         |
| WIA\_INTENT\_IMAGE\_TYPE\_GRAYSCALE | Preset properties for grayscale content.     |
| WIA\_INTENT\_IMAGE\_TYPE\_TEXT      | Preset properties for text content.          |
| WIA\_INTENT\_IMAGE\_TYPE\_MASK      | Mask for all of the image type flags.        |



 



| Intended image size/quality flags | Description                                  |
|-----------------------------------|----------------------------------------------|
| WIA\_INTENT\_MINIMIZE\_SIZE       | Preset properties to minimize image size.    |
| WIA\_INTENT\_MAXIMIZE\_QUALITY    | Preset properties to maximize image quality. |
| WIA\_INTENT\_SIZE\_MASK           | Mask for all of the size/quality flags.      |
| WIA\_INTENT\_BEST\_PREVIEW        | Specifies the best quality preview.          |



 

The following list shows the C/C++ constant name followed by the corresponding name in parentheses that is used in scripting. The script names are from the WiaIntent enumerated type. Note that not all constants are available through script.



| Constant/value                                                                                                                                                                                                                                                                         | Description                                             |
|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------------------------------------------|
| <span id="WIA_INTENT_IMAGE_TYPE_COLOR"></span><span id="wia_intent_image_type_color"></span><dl> <dt>**WIA\_INTENT\_IMAGE\_TYPE\_COLOR**</dt> <dt>0x00000001</dt> </dl>             | Preset properties for color content.<br/>         |
| <span id="WIA_INTENT_IMAGE_TYPE_GRAYSCALE"></span><span id="wia_intent_image_type_grayscale"></span><dl> <dt>**WIA\_INTENT\_IMAGE\_TYPE\_GRAYSCALE**</dt> <dt>0x00000002</dt> </dl> | Preset properties for grayscale content.<br/>     |
| <span id="WIA_INTENT_IMAGE_TYPE_TEXT"></span><span id="wia_intent_image_type_text"></span><dl> <dt>**WIA\_INTENT\_IMAGE\_TYPE\_TEXT**</dt> <dt>0x00000004</dt> </dl>                | Preset properties for text content.<br/>          |
| <span id="WIA_INTENT_MINIMIZE_SIZE"></span><span id="wia_intent_minimize_size"></span><dl> <dt>**WIA\_INTENT\_MINIMIZE\_SIZE**</dt> <dt>0x00010000</dt> </dl>                       | Preset properties to minimize image size.<br/>    |
| <span id="WIA_INTENT_MAXIMIZE_QUALITY"></span><span id="wia_intent_maximize_quality"></span><dl> <dt>**WIA\_INTENT\_MAXIMIZE\_QUALITY**</dt> <dt>0x00020000</dt> </dl>              | Preset properties to maximize image quality.<br/> |
| <span id="WIA_INTENT_BEST_PREVIEW"></span><span id="wia_intent_best_preview"></span><dl> <dt>**WIA\_INTENT\_BEST\_PREVIEW**</dt> <dt>0x00040000</dt> </dl>                          | Specifies the best quality preview.<br/>          |



## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional, Windows XP \[desktop apps only\]<br/>              |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Wiadef.h</dt> </dl> |



 

 




