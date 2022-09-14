---
title: Tooltip Styles (CommCtrl.h)
description: This section lists the control styles used with tooltip controls.
ms.assetid: a6aeac71-6a69-4903-af78-0bfe1f83e632
topic_type:
- apiref
api_name:
- TTS_ALWAYSTIP
- TTS_BALLOON
- TTS_CLOSE
- TTS_NOANIMATE
- TTS_NOFADE
- TTS_NOPREFIX
- TTS_USEVISUALSTYLE
api_location:
- CommCtrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# Tooltip Styles

This section lists the control styles used with tooltip controls.



| Constant                                                                                                                                                                     | Description                                                                                                                                                                                                                                                                                                                                                       |
|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="TTS_ALWAYSTIP"></span><span id="tts_alwaystip"></span><dl> <dt>**TTS\_ALWAYSTIP**</dt> </dl>                | Indicates that the tooltip control appears when the cursor is on a tool, even if the tooltip control's owner window is inactive. Without this style, the tooltip appears only when the tool's owner window is active.<br/>                                                                                                                                  |
| <span id="TTS_BALLOON"></span><span id="tts_balloon"></span><dl> <dt>**TTS\_BALLOON**</dt> </dl>                      | [Version 5.80](common-control-versions.md). Indicates that the tooltip control has the appearance of a cartoon "balloon," with rounded corners and a stem pointing to the item. <br/>                                                                                                                                                                      |
| <span id="TTS_CLOSE"></span><span id="tts_close"></span><dl> <dt>**TTS\_CLOSE**</dt> </dl>                            | Displays a **Close** button on the tooltip. Valid only when the tooltip has the TTS\_BALLOON style and a title; see [**TTM\_SETTITLE**](ttm-settitle.md).<br/>                                                                                                                                                                                             |
| <span id="TTS_NOANIMATE"></span><span id="tts_noanimate"></span><dl> <dt>**TTS\_NOANIMATE**</dt> </dl>                | [Version 5.80](common-control-versions.md). Disables sliding tooltip animation on Windows 98 and Windows 2000 systems. This style is ignored on earlier systems.<br/>                                                                                                                                                                                      |
| <span id="TTS_NOFADE"></span><span id="tts_nofade"></span><dl> <dt>**TTS\_NOFADE**</dt> </dl>                         | [Version 5.80](common-control-versions.md). Disables fading tooltip animation. <br/>                                                                                                                                                                                                                                                                       |
| <span id="TTS_NOPREFIX"></span><span id="tts_noprefix"></span><dl> <dt>**TTS\_NOPREFIX**</dt> </dl>                   | Prevents the system from stripping ampersand characters from a string or terminating a string at a tab character. Without this style, the system automatically strips ampersand characters and terminates a string at the first tab character. This allows an application to use the same string as both a menu item and as text in a tooltip control.<br/> |
| <span id="TTS_USEVISUALSTYLE"></span><span id="tts_usevisualstyle"></span><dl> <dt>**TTS\_USEVISUALSTYLE**</dt> </dl> | Uses themed hyperlinks. The theme will define the styles for any links in the tooltip. This style always requires TTF\_PARSELINKS to be set. <br/>                                                                                                                                                                                                          |



## Remarks

A tooltip control always has the WS\_POPUP and WS\_EX\_TOOLWINDOW window styles, regardless of whether you specify them when creating the control.

## Requirements



| Requirement | Value |
|-------------------|---------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>CommCtrl.h</dt> </dl> |



 

 





