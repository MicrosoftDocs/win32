---
title: BCM\_GETSPLITINFO message
description: Gets information for a split button control. Send this message explicitly or by using the Button\_GetSplitInfo macro.
ms.assetid: 'd608440d-b8d8-4e32-9128-08b7566b185c'
keywords: ["BCM_GETSPLITINFO message Windows Controls"]
topic_type:
- apiref
api_name:
- BCM_GETSPLITINFO
api_location:
- Commctrl.h
api_type:
- HeaderDef
---

# BCM\_GETSPLITINFO message

Gets information for a split button control. Send this message explicitly or by using the [**Button\_GetSplitInfo**](button-getsplitinfo.md) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Must be zero.

</dd> <dt>

*lParam* \[in, out\]
</dt> <dd>

A pointer to a [**BUTTON\_SPLITINFO**](button-splitinfo.md) structure to receive information on the button. The caller is responsible for allocating the memory for the structure. Set the **mask** member of this structure to determine what information to receive.

</dd> </dl>

## Return value

Returns **TRUE** if successful, or **FALSE** otherwise.

## Remarks

Use this message only with the [**BS\_SPLITBUTTON**](button-styles.md#bs-splitbutton) and [**BS\_DEFSPLITBUTTON**](button-styles.md#bs-defsplitbutton) button styles.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



## See also

<dl> <dt>

**Reference**
</dt> <dt>

[Button Styles](button-styles.md)
</dt> <dt>

**Conceptual**
</dt> <dt>

[Button Types](button-types-and-styles.md)
</dt> </dl>

 

 





