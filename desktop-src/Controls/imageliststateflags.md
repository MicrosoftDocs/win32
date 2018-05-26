---
title: IMAGELISTSTATEFLAGS
description: The following flags are passed to the IImageList Draw method in the fState member of IMAGELISTDRAWPARAMS.
ms.assetid: a22b4acf-c290-44b2-9216-b006d0326236
topic_type:
- apiref
api_name:
- ILS_NORMAL
- ILS_GLOW
- ILS_SHADOW
- ILS_SATURATE
- ILS_ALPHA
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IMAGELISTSTATEFLAGS

The following flags are passed to the [**IImageList::Draw**](/windows/win32/CommonControls/nf-commoncontrols-iimagelist-draw?branch=master) method in the **fState** member of [**IMAGELISTDRAWPARAMS**](/windows/win32/commoncontrols/ns-commctrl-_imagelistdrawparams?branch=master).



| Constant/value                                                                                                                                                                                                             | Description                                                                                                                                                                                                                                                                                                                                                                                   |
|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="ILS_NORMAL"></span><span id="ils_normal"></span><dl> <dt>**ILS\_NORMAL**</dt> <dt>0x00000000</dt> </dl>       | The image state is not modified.<br/>                                                                                                                                                                                                                                                                                                                                                   |
| <span id="ILS_GLOW"></span><span id="ils_glow"></span><dl> <dt>**ILS\_GLOW**</dt> <dt>0x00000001</dt> </dl>             | Not supported. <br/>                                                                                                                                                                                                                                                                                                                                                                    |
| <span id="ILS_SHADOW"></span><span id="ils_shadow"></span><dl> <dt>**ILS\_SHADOW**</dt> <dt>0x00000002</dt> </dl>       | Not supported. <br/>                                                                                                                                                                                                                                                                                                                                                                    |
| <span id="ILS_SATURATE"></span><span id="ils_saturate"></span><dl> <dt>**ILS\_SATURATE**</dt> <dt>0x00000004</dt> </dl> | Reduces the color saturation of the icon to grayscale. This only affects 32bpp images. <br/>                                                                                                                                                                                                                                                                                            |
| <span id="ILS_ALPHA"></span><span id="ils_alpha"></span><dl> <dt>**ILS\_ALPHA**</dt> <dt>0x00000008</dt> </dl>          | Alpha blends the icon. Alpha blending controls the transparency level of an icon, according to the value of its alpha channel. The value of the alpha channel is indicated by the **frame** member in the [**IMAGELISTDRAWPARAMS**](/windows/win32/commoncontrols/ns-commctrl-_imagelistdrawparams?branch=master) method. The alpha channel can be from 0 to 255, with 0 being completely transparent, and 255 being completely opaque.<br/> |



## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





