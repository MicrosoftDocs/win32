---
title: WTNCA Values (Uxtheme.h)
description: Specifies flags that modify window visual style attributes. Use one, or a bitwise combination of the following values.
ms.assetid: C71D1957-6572-4242-B715-C54BDFBBD6B7
topic_type:
- apiref
api_name:
- WTNCA_NODRAWCAPTION
- WTNCA_NODRAWICON
- WTNCA_NOSYSMENU
- WTNCA_NOMIRRORHELP
- WTNCA_VALIDBITS
api_location:
- Uxtheme.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# WTNCA Values

Specifies flags that modify window visual style attributes. Use one, or a bitwise combination of the following values.



| Constant/value                                                                                                                                                                                                                                  | Description                                                                             |
|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------|
| <span id="WTNCA_NODRAWCAPTION"></span><span id="wtnca_nodrawcaption"></span><dl> <dt>**WTNCA\_NODRAWCAPTION**</dt> <dt>0x00000001</dt> </dl> | Prevents the window caption from being drawn.<br/>                                |
| <span id="WTNCA_NODRAWICON"></span><span id="wtnca_nodrawicon"></span><dl> <dt>**WTNCA\_NODRAWICON**</dt> <dt>0x00000002</dt> </dl>          | Prevents the system icon from being drawn.<br/>                                   |
| <span id="WTNCA_NOSYSMENU"></span><span id="wtnca_nosysmenu"></span><dl> <dt>**WTNCA\_NOSYSMENU**</dt> <dt>0x00000004</dt> </dl>             | Prevents the system icon menu from appearing.<br/>                                |
| <span id="WTNCA_NOMIRRORHELP"></span><span id="wtnca_nomirrorhelp"></span><dl> <dt>**WTNCA\_NOMIRRORHELP**</dt> <dt>0x00000008</dt> </dl>    | Prevents mirroring of the question mark, even in right-to-left (RTL) layout.<br/> |
| <span id="WTNCA_VALIDBITS"></span><span id="wtnca_validbits"></span><dl> <dt>**WTNCA\_VALIDBITS**</dt> </dl>                                                                             | A mask that contains all the valid bits.<br/>                                     |



## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>Uxtheme.h</dt> </dl> |



## See also

<dl> <dt>

**Reference**
</dt> <dt>

[**WTA\_OPTIONS**](/windows/desktop/api/Uxtheme/ns-uxtheme-wta_options)
</dt> <dt>

[**SetWindowThemeNonClientAttributes**](/windows/desktop/api/Uxtheme/nf-uxtheme-setwindowthemenonclientattributes)
</dt> </dl>

 

 





