---
title: SysLink Control Styles (CommCtrl.h)
description: The following style constants are used when creating SysLink controls.
ms.assetid: e9a8c99b-86c4-4385-ae20-b2b78a07b491
topic_type:
- apiref
api_name:
- LWS_TRANSPARENT
- LWS_IGNORERETURN
- LWS_NOPREFIX
- LWS_USEVISUALSTYLE
- LWS_USECUSTOMTEXT
- LWS_RIGHT
api_location:
- CommCtrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# SysLink Control Styles

The following style constants are used when creating SysLink controls.



| Constant                                                                                                                                                                        | Description                                                                                                                                                               |
|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="LWS_TRANSPARENT"></span><span id="lws_transparent"></span><dl> <dt>**LWS\_TRANSPARENT**</dt> </dl>             | The background mix mode is transparent. <br/>                                                                                                                       |
| <span id="LWS_IGNORERETURN_"></span><span id="lws_ignorereturn_"></span><dl> <dt>**LWS\_IGNORERETURN** </dt> </dl>       | When the link has keyboard focus and the user presses Enter, the keystroke is ignored by the control and passed to the host dialog box.<br/>                        |
| <span id="LWS_NOPREFIX"></span><span id="lws_noprefix"></span><dl> <dt>**LWS\_NOPREFIX**</dt> </dl>                      | **Windows Vista**. If the text contains an ampersand, it is treated as a literal character rather than the prefix to a shortcut key.<br/>                           |
| <span id="LWS_USEVISUALSTYLE_"></span><span id="lws_usevisualstyle_"></span><dl> <dt>**LWS\_USEVISUALSTYLE** </dt> </dl> | **Windows Vista**. The link is displayed in the current visual style.<br/>                                                                                          |
| <span id="LWS_USECUSTOMTEXT"></span><span id="lws_usecustomtext"></span><dl> <dt>**LWS\_USECUSTOMTEXT**</dt> </dl>       | **Windows Vista**. An [NM\_CUSTOMTEXT](nm-customtext.md) notification is sent when the control is drawn, so that the application can supply text dynamically.<br/> |
| <span id="LWS_RIGHT"></span><span id="lws_right"></span><dl> <dt>**LWS\_RIGHT**</dt> </dl>                               | **Windows Vista**. The text is right-justified.<br/>                                                                                                                |



## Requirements



| Requirement | Value |
|-------------------|---------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>CommCtrl.h</dt> </dl> |



 

 





