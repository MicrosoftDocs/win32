---
description: Represent options available when displaying a pop-up menu.
title: MP_POPUPFLAGS constants (Shobjidl.h)
ms.topic: reference
ms.date: 05/31/2018
ms.assetid: cc1d9ff0-a03b-4bd3-b481-9b78d20eb771
api_name: 
 - MPPF_SETFOCUS
 - MPPF_INITIALSELECT
 - MPPF_NOANIMATE
 - MPPF_KEYBOARD
 - MPPF_REPOSITION
 - MPPF_FORCEZORDER
 - MPPF_FINALSELECT
 - MPPF_ALIGN_LEFT
 - MPPF_ALIGN_RIGHT
 - MPPF_TOP
 - MPPF_LEFT
 - MPPF_RIGHT
 - MPPF_BOTTOM
 - MPPF_POS_MASK
api_type: 
 - HeaderDef
api_location: 
 - Shobjidl.h
topic_type: 
 - APIRef
 - kbSyntax

---

# MP\_POPUPFLAGS constants

Represent options available when displaying a pop-up menu.



| Constant/value                                                                                                                                                                                                                               | Description                                                                                                                                                                                                                                                              |
|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="MPPF_SETFOCUS"></span><span id="mppf_setfocus"></span><dl> <dt>**MPPF\_SETFOCUS**</dt> <dt>0x00000001</dt> </dl>                | Give the pop-up menu the focus.<br/>                                                                                                                                                                                                                               |
| <span id="MPPF_INITIALSELECT"></span><span id="mppf_initialselect"></span><dl> <dt>**MPPF\_INITIALSELECT**</dt> <dt>0x00000002</dt> </dl> | Select the first item in the pop-up menu.<br/>                                                                                                                                                                                                                     |
| <span id="MPPF_NOANIMATE"></span><span id="mppf_noanimate"></span><dl> <dt>**MPPF\_NOANIMATE**</dt> <dt>0x00000004</dt> </dl>             | Do not use the default system animations, for example, fade-in, when displaying the menu.<br/>                                                                                                                                                                     |
| <span id="MPPF_KEYBOARD"></span><span id="mppf_keyboard"></span><dl> <dt>**MPPF\_KEYBOARD**</dt> <dt>0x00000010</dt> </dl>                | Activate the menu by a keyboard shortcut.<br/>                                                                                                                                                                                                                     |
| <span id="MPPF_REPOSITION"></span><span id="mppf_reposition"></span><dl> <dt>**MPPF\_REPOSITION**</dt> <dt>0x00000020</dt> </dl>          | Display the bar in a different position, based on changes to the menu.<br/>                                                                                                                                                                                        |
| <span id="MPPF_FORCEZORDER"></span><span id="mppf_forcezorder"></span><dl> <dt>**MPPF\_FORCEZORDER**</dt> <dt>0x00000040</dt> </dl>       | Reserved. Do not use.<br/>                                                                                                                                                                                                                                         |
| <span id="MPPF_FINALSELECT"></span><span id="mppf_finalselect"></span><dl> <dt>**MPPF\_FINALSELECT**</dt> <dt>0x00000080</dt> </dl>       | Select the last item in the menu.<br/>                                                                                                                                                                                                                             |
| <span id="MPPF_ALIGN_LEFT"></span><span id="mppf_align_left"></span><dl> <dt>**MPPF\_ALIGN\_LEFT**</dt> <dt>0x02000000</dt> </dl>         | **Windows Vista or later**: Align the pop-up menu to the left of the area specified in the *prcExclude* parameter of [**ITrackShellMenu::Popup**](/windows/desktop/api/Shdeprecated/nf-shdeprecated-itrackshellmenu-popup) or [**IMenuPopup::Popup**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-imenupopup-popup). This is the default alignment.<br/> |
| <span id="MPPF_ALIGN_RIGHT"></span><span id="mppf_align_right"></span><dl> <dt>**MPPF\_ALIGN\_RIGHT**</dt> <dt>0x04000000</dt> </dl>      | **Windows Vista or later**: Align the pop-up menu to the right of the area specified in the *prcExclude* parameter of [**ITrackShellMenu::Popup**](/windows/desktop/api/Shdeprecated/nf-shdeprecated-itrackshellmenu-popup) or [**IMenuPopup::Popup**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-imenupopup-popup).<br/>                               |
| <span id="MPPF_TOP"></span><span id="mppf_top"></span><dl> <dt>**MPPF\_TOP**</dt> <dt>0x20000000</dt> </dl>                               | Position the pop-up menu above the initial point specified in the *ppt* parameter of [**ITrackShellMenu::Popup**](/windows/desktop/api/Shdeprecated/nf-shdeprecated-itrackshellmenu-popup) or [**IMenuPopup::Popup**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-imenupopup-popup).<br/>                                                                |
| <span id="MPPF_LEFT"></span><span id="mppf_left"></span><dl> <dt>**MPPF\_LEFT**</dt> <dt>0x40000000</dt> </dl>                            | Position the pop-up menu to the left of the initial point.<br/>                                                                                                                                                                                                    |
| <span id="MPPF_RIGHT"></span><span id="mppf_right"></span><dl> <dt>**MPPF\_RIGHT**</dt> <dt>0x60000000</dt> </dl>                         | Position the pop-up menu to the right of the initial point.<br/>                                                                                                                                                                                                   |
| <span id="MPPF_BOTTOM"></span><span id="mppf_bottom"></span><dl> <dt>**MPPF\_BOTTOM**</dt> <dt>(int)0x80000000</dt> </dl>                 | Position the pop-up menu below the initial point.<br/>                                                                                                                                                                                                             |
| <span id="MPPF_POS_MASK"></span><span id="mppf_pos_mask"></span><dl> <dt>**MPPF\_POS\_MASK**</dt> <dt>(int)0xE0000000</dt> </dl>          | The menu position mask.<br/>                                                                                                                                                                                                                                       |



## Remarks

These constants are defined in the Shobjidl.h file beginning in Windows XP Service Pack 1 (SP1) and Windows Server 2003

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP with SP1 \[desktop apps only\]<br/>                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>Shobjidl.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Shobjidl.idl</dt> </dl> |



## See also

<dl> <dt>

[**IMenuPopup::Popup**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-imenupopup-popup)
</dt> <dt>

[**ITrackShellMenu::Popup**](/windows/desktop/api/Shdeprecated/nf-shdeprecated-itrackshellmenu-popup)
</dt> </dl>

 

 




