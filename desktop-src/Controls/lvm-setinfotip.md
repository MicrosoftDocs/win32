---
title: LVM\_SETINFOTIP message
description: Sets tooltip text in delayed response to the LVN\_GETINFOTIP notification.
ms.assetid: '3dbf6a9a-52ec-4619-9c70-041e75942e20'
keywords: ["LVM_SETINFOTIP message Windows Controls"]
topic_type:
- apiref
api_name:
- LVM_SETINFOTIP
api_location:
- Commctrl.h
api_type:
- HeaderDef
---

# LVM\_SETINFOTIP message

Sets tooltip text in delayed response to the [LVN\_GETINFOTIP](lvn-getinfotip.md) notification.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>Must be zero.</dd> <dt>

*lParam* 
</dt> <dd>Pointer to a [**LVSETINFOTIP**](lvsetinfotip.md) structure that contains the information to set.</dd> </dl>

## Return value

Returns **TRUE** if the tooltip text is set successful, or **FALSE** otherwise.

## Remarks

The **LVM\_SETINFOTIP** message lets an application calculate infotips in the background by performing the following steps:

1.  In response to the [LVN\_GETINFOTIP](lvn-getinfotip.md) notification, set the **pszText** member of the [**NMLVGETINFOTIP**](nmlvgetinfotip.md) structure to an empty string and return 0.
2.  In the background, compute the infotip.
3.  After computing the infotip, send the **LVM\_SETINFOTIP** message, setting the **pszText** member of the [**LVSETINFOTIP**](lvsetinfotip.md) structure to the infotip and the **iItem** and **iSubItem** members to the item and sub-item to which the infotip applies.

The text passed to the **LVM\_SETINFOTIP** message appears only if the item and sub-item described by the [**LVSETINFOTIP**](lvsetinfotip.md) structure are still in a state that requires an infotip

> [!Note]  
> To use this message, you must provide a manifest specifying Comclt32.dll version 6.0. For more information on manifests, see [Enabling Visual Styles](cookbook-overview.md).

 

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





