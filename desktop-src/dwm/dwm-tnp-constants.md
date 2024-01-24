---
title: DWM_TNP Constants (Dwmapi.h)
description: Flags used by the DWM\_THUMBNAIL\_PROPERTIES structure to indicate which of its members contain valid information.
ms.assetid: 8eee1baf-e24e-40af-92ab-a7acae267ecc
topic_type:
- apiref
api_name:
- DWM_TNP_RECTDESTINATION
- DWM_TNP_RECTSOURCE
- DWM_TNP_OPACITY
- DWM_TNP_VISIBLE
- DWM_TNP_SOURCECLIENTAREAONLY
api_location:
- Dwmapi.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# DWM\_TNP Constants

Flags used by the [**DWM\_THUMBNAIL\_PROPERTIES**](/windows/desktop/api/Dwmapi/ns-dwmapi-dwm_thumbnail_properties) structure to indicate which of its members contain valid information.

<dl> <dt>

<span id="DWM_TNP_RECTDESTINATION"></span><span id="dwm_tnp_rectdestination"></span>**DWM\_TNP\_RECTDESTINATION**
</dt> <dd> <dl> <dt>

0x00000001
</dt> <dt>



A value for the **rcDestination** member has been specified.


</dt> </dl> </dd> <dt>

<span id="DWM_TNP_RECTSOURCE"></span><span id="dwm_tnp_rectsource"></span>**DWM\_TNP\_RECTSOURCE**
</dt> <dd> <dl> <dt>

0x00000002
</dt> <dt>



A value for the **rcSource** member has been specified.


</dt> </dl> </dd> <dt>

<span id="DWM_TNP_OPACITY"></span><span id="dwm_tnp_opacity"></span>**DWM\_TNP\_OPACITY**
</dt> <dd> <dl> <dt>

0x00000004
</dt> <dt>



A value for the **opacity** member has been specified.


</dt> </dl> </dd> <dt>

<span id="DWM_TNP_VISIBLE"></span><span id="dwm_tnp_visible"></span>**DWM\_TNP\_VISIBLE**
</dt> <dd> <dl> <dt>

0x00000008
</dt> <dt>



A value for the **fVisible** member has been specified.


</dt> </dl> </dd> <dt>

<span id="DWM_TNP_SOURCECLIENTAREAONLY"></span><span id="dwm_tnp_sourceclientareaonly"></span>**DWM\_TNP\_SOURCECLIENTAREAONLY**
</dt> <dd> <dl> <dt>

0x00000010
</dt> <dt>



A value for the **fSourceClientAreaOnly** member has been specified.


</dt> </dl> </dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                      |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Dwmapi.h</dt> </dl> |



 

 





