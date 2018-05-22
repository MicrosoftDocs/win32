---
title: BCM\_GETIMAGELIST message
description: Gets the BUTTON\_IMAGELIST structure that describes the image list assigned to a button control. You can send this message explicitly or use the Button\_GetImageList macro.
ms.assetid: '79383758-53d4-4955-b472-befd338cbec6'
keywords: ["BCM_GETIMAGELIST message Windows Controls"]
topic_type:
- apiref
api_name:
- BCM_GETIMAGELIST
api_location:
- Commctrl.h
api_type:
- HeaderDef
---

# BCM\_GETIMAGELIST message

Gets the [**BUTTON\_IMAGELIST**](button-imagelist.md) structure that describes the image list assigned to a button control. You can send this message explicitly or use the [**Button\_GetImageList**](button-getimagelist.md) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Not used; must be zero.

</dd> <dt>

*lParam* 
</dt> <dd>

A pointer to a [**BUTTON\_IMAGELIST**](button-imagelist.md) structure that contains image list information.

</dd> </dl>

## Return value

If the message succeeds, it returns **TRUE**. Otherwise it returns **FALSE**.

## Remarks

> [!Note]  
> To use this message, you must provide a manifest specifying Comclt32.dll version 6.0. For more information on manifests, see [Enabling Visual Styles](cookbook-overview.md).

 

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





