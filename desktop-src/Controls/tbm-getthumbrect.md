---
title: TBM\_GETTHUMBRECT message
description: Retrieves the size and position of the bounding rectangle for the slider in a trackbar.
ms.assetid: 'f53fd7af-36f8-4490-aa95-f1fa20f34efb'
keywords: ["TBM_GETTHUMBRECT message Windows Controls"]
topic_type:
- apiref
api_name:
- TBM_GETTHUMBRECT
api_location:
- Commctrl.h
api_type:
- HeaderDef
---

# TBM\_GETTHUMBRECT message

Retrieves the size and position of the bounding rectangle for the slider in a trackbar.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>Must be zero.</dd> <dt>

*lParam* 
</dt> <dd>

Pointer to a [**RECT**](https://msdn.microsoft.com/library/windows/desktop/dd162897) structure. The message fills this structure with the bounding rectangle of the trackbar's slider in client coordinates of the trackbar's window.

</dd> </dl>

## Return value

No return value.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





