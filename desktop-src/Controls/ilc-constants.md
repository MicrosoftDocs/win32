---
title: Image List Creation Flags (Shlobj.h)
description: The set of bit flags that specifies the type of image list to create. This parameter can be a combination of the following values, but it can include only one of the ILC\_COLOR values. Used by ImageList\_Create and IImageList2 Initialize.
ms.assetid: DFEB1934-DB7F-4151-97F9-DDB2BCCC782A
topic_type:
- apiref
api_name:
- ILC_MASK
- ILC_COLOR
- ILC_COLORDDB
- ILC_COLOR4
- ILC_COLOR8
- ILC_COLOR16
- ILC_COLOR24
- ILC_COLOR32
- ILC_PALETTE
- ILC_MIRROR
- ILC_PERITEMMIRROR
- ILC_ORIGINALSIZE
- ILC_HIGHQUALITYSCALE
api_location:
- Shlobj.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# Image List Creation Flags

The set of bit flags that specifies the type of image list to create. This parameter can be a combination of the following values, but it can include only one of the ILC\_COLOR values. Used by [**ImageList\_Create**](/windows/desktop/api/Commctrl/nf-commctrl-imagelist_create) and [**IImageList2::Initialize**](/windows/desktop/api/Commoncontrols/nf-commoncontrols-iimagelist2-initialize).



| Constant/value                                                                                                                                                                                                                                     | Description                                                                                                                                                                                  |
|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="ILC_MASK"></span><span id="ilc_mask"></span><dl> <dt>**ILC\_MASK**</dt> <dt>0x00000001</dt> </dl>                                     | Use a mask. The image list contains two bitmaps, one of which is a monochrome bitmap used as a mask. If this value is not included, the image list contains only one bitmap.<br/>      |
| <span id="ILC_COLOR"></span><span id="ilc_color"></span><dl> <dt>**ILC\_COLOR**</dt> <dt>0x00000000</dt> </dl>                                  | Use the default behavior if none of the other ILC\_COLORx flags is specified. Typically, the default is ILC\_COLOR4, but for older display drivers, the default is ILC\_COLORDDB.<br/> |
| <span id="ILC_COLORDDB"></span><span id="ilc_colorddb"></span><dl> <dt>**ILC\_COLORDDB**</dt> <dt>0x000000FE</dt> </dl>                         | Use a device-dependent bitmap.<br/>                                                                                                                                                    |
| <span id="ILC_COLOR4"></span><span id="ilc_color4"></span><dl> <dt>**ILC\_COLOR4**</dt> <dt>0x00000004</dt> </dl>                               | Use a 4-bit (16-color) device-independent bitmap (DIB) section as the bitmap for the image list.<br/>                                                                                  |
| <span id="ILC_COLOR8"></span><span id="ilc_color8"></span><dl> <dt>**ILC\_COLOR8**</dt> <dt>0x00000008</dt> </dl>                               | Use an 8-bit DIB section. The colors used for the color table are the same colors as the halftone palette.<br/>                                                                        |
| <span id="ILC_COLOR16"></span><span id="ilc_color16"></span><dl> <dt>**ILC\_COLOR16**</dt> <dt>0x00000010</dt> </dl>                            | Use a 16-bit (32/64k-color) DIB section.<br/>                                                                                                                                          |
| <span id="ILC_COLOR24"></span><span id="ilc_color24"></span><dl> <dt>**ILC\_COLOR24**</dt> <dt>0x00000018</dt> </dl>                            | Use a 24-bit DIB section.<br/>                                                                                                                                                         |
| <span id="ILC_COLOR32"></span><span id="ilc_color32"></span><dl> <dt>**ILC\_COLOR32**</dt> <dt>0x00000020</dt> </dl>                            | Use a 32-bit DIB section.<br/>                                                                                                                                                         |
| <span id="ILC_PALETTE"></span><span id="ilc_palette"></span><dl> <dt>**ILC\_PALETTE**</dt> <dt>0x00000800</dt> </dl>                            | Not implemented.<br/>                                                                                                                                                                  |
| <span id="ILC_MIRROR"></span><span id="ilc_mirror"></span><dl> <dt>**ILC\_MIRROR**</dt> <dt>0x00002000</dt> </dl>                               | Mirror the icons contained, if the process is mirrored<br/>                                                                                                                            |
| <span id="ILC_PERITEMMIRROR"></span><span id="ilc_peritemmirror"></span><dl> <dt>**ILC\_PERITEMMIRROR**</dt> <dt>0x00008000</dt> </dl>          | Causes the mirroring code to mirror each item when inserting a set of images, versus the whole strip.<br/>                                                                             |
| <span id="ILC_ORIGINALSIZE"></span><span id="ilc_originalsize"></span><dl> <dt>**ILC\_ORIGINALSIZE**</dt> <dt>0x00010000</dt> </dl>             | **Windows Vista and later.** Imagelist should accept smaller than set images and apply original size based on image added.<br/>                                                        |
| <span id="ILC_HIGHQUALITYSCALE"></span><span id="ilc_highqualityscale"></span><dl> <dt>**ILC\_HIGHQUALITYSCALE**</dt> <dt>0x00020000</dt> </dl> | **Windows Vista and later.** Reserved.<br/>                                                                                                                                            |



## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                      |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Shlobj.h</dt> </dl> |



 

 





