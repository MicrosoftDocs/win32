---
title: Rich Edit Control Event Mask Flags (RichEdit.h)
description: The event mask specifies which notification codes a rich edit control sends to its parent window. The event mask can be none or a combination of these values.
ms.assetid: ae0d2cbe-5cbc-42bb-aeb1-7e6be846a4ba
topic_type:
- apiref
api_name:
- ENM_CHANGE
- ENM_CLIPFORMAT
- ENM_CORRECTTEXT
- ENM_DRAGDROPDONE
- ENM_DROPFILES
- ENM_IMECHANGE
- ENM_KEYEVENTS
- ENM_LINK
- ENM_LOWFIRTF
- ENM_MOUSEEVENTS
- ENM_OBJECTPOSITIONS
- ENM_PARAGRAPHEXPANDED
- ENM_PROTECTED
- ENM_REQUESTRESIZE
- ENM_SCROLL
- ENM_SCROLLEVENTS
- ENM_SELCHANGE
- ENM_UPDATE
api_location:
- RichEdit.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# Rich Edit Control Event Mask Flags

The event mask specifies which notification codes a rich edit control sends to its parent window. The event mask can be none or a combination of these values.



| Constant                                                                                                                                                                              | Description                                                                                                                                                                                                                                                                                                       |
|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="ENM_CHANGE"></span><span id="enm_change"></span><dl> <dt>**ENM\_CHANGE**</dt> </dl>                                  | Sends [EN\_CHANGE](en-change--rich-edit-control-.md) notifications.<br/>                                                                                                                                                                                                                                   |
| <span id="ENM_CLIPFORMAT"></span><span id="enm_clipformat"></span><dl> <dt>**ENM\_CLIPFORMAT**</dt> </dl>                      | Sends [EN\_CLIPFORMAT](/windows/desktop/Controls/en-clipformat) notifications.<br/>                                                                                                                                                                                                                                          |
| <span id="ENM_CORRECTTEXT"></span><span id="enm_correcttext"></span><dl> <dt>**ENM\_CORRECTTEXT**</dt> </dl>                   | Sends [EN\_CORRECTTEXT](en-correcttext.md) notifications.<br/>                                                                                                                                                                                                                                             |
| <span id="ENM_DRAGDROPDONE"></span><span id="enm_dragdropdone"></span><dl> <dt>**ENM\_DRAGDROPDONE**</dt> </dl>                | Sends [EN\_DRAGDROPDONE](en-dragdropdone.md) notifications.<br/>                                                                                                                                                                                                                                           |
| <span id="ENM_DROPFILES"></span><span id="enm_dropfiles"></span><dl> <dt>**ENM\_DROPFILES**</dt> </dl>                         | Sends [EN\_DROPFILES](en-dropfiles.md) notifications.<br/>                                                                                                                                                                                                                                                 |
| <span id="ENM_IMECHANGE"></span><span id="enm_imechange"></span><dl> <dt>**ENM\_IMECHANGE**</dt> </dl>                         | Microsoft Rich Edit 1.0 only: Sends [EN\_IMECHANGE](en-imechange.md) notifications when the IME conversion status has changed. Only for Asian-language versions of the operating system.<br/>                                                                                                              |
| <span id="ENM_KEYEVENTS"></span><span id="enm_keyevents"></span><dl> <dt>**ENM\_KEYEVENTS**</dt> </dl>                         | Sends [EN\_MSGFILTER](en-msgfilter.md) notifications for keyboard events.<br/>                                                                                                                                                                                                                             |
| <span id="ENM_LINK"></span><span id="enm_link"></span><dl> <dt>**ENM\_LINK**</dt> </dl>                                        | **Rich Edit 2.0 and later:** Sends [EN\_LINK](en-link.md) notifications when the mouse pointer is over text that has the CFE\_LINK and one of several mouse actions is performed.<br/>                                                                                                                     |
| <span id="ENM_LOWFIRTF"></span><span id="enm_lowfirtf"></span><dl> <dt>**ENM\_LOWFIRTF**</dt> </dl>                            | Sends [EN\_LOWFIRTF](en-lowfirtf.md) notifications.<br/>                                                                                                                                                                                                                                                   |
| <span id="ENM_MOUSEEVENTS"></span><span id="enm_mouseevents"></span><dl> <dt>**ENM\_MOUSEEVENTS**</dt> </dl>                   | Sends [EN\_MSGFILTER](en-msgfilter.md) notifications for mouse events.<br/>                                                                                                                                                                                                                                |
| <span id="ENM_OBJECTPOSITIONS"></span><span id="enm_objectpositions"></span><dl> <dt>**ENM\_OBJECTPOSITIONS**</dt> </dl>       | Sends [EN\_OBJECTPOSITIONS](en-objectpositions.md) notifications.<br/>                                                                                                                                                                                                                                     |
| <span id="ENM_PARAGRAPHEXPANDED"></span><span id="enm_paragraphexpanded"></span><dl> <dt>**ENM\_PARAGRAPHEXPANDED**</dt> </dl> | Sends [EN\_PARAGRAPHEXPANDED](/windows/desktop/Controls/en-paragraphexpanded) notifications.<br/>                                                                                                                                                                                                                            |
| <span id="ENM_PROTECTED"></span><span id="enm_protected"></span><dl> <dt>**ENM\_PROTECTED**</dt> </dl>                         | Sends [EN\_PROTECTED](en-protected.md) notifications.<br/>                                                                                                                                                                                                                                                 |
| <span id="ENM_REQUESTRESIZE"></span><span id="enm_requestresize"></span><dl> <dt>**ENM\_REQUESTRESIZE**</dt> </dl>             | Sends [EN\_REQUESTRESIZE](en-requestresize.md) notifications.<br/>                                                                                                                                                                                                                                         |
| <span id="ENM_SCROLL"></span><span id="enm_scroll"></span><dl> <dt>**ENM\_SCROLL**</dt> </dl>                                  | Sends [EN\_HSCROLL](en-hscroll.md) and [EN\_VSCROLL](en-vscroll.md) notifications.<br/>                                                                                                                                                                                                                   |
| <span id="ENM_SCROLLEVENTS"></span><span id="enm_scrollevents"></span><dl> <dt>**ENM\_SCROLLEVENTS**</dt> </dl>                | Sends [EN\_MSGFILTER](en-msgfilter.md) notifications for mouse wheel events.<br/>                                                                                                                                                                                                                          |
| <span id="ENM_SELCHANGE"></span><span id="enm_selchange"></span><dl> <dt>**ENM\_SELCHANGE**</dt> </dl>                         | Sends [EN\_SELCHANGE](en-selchange.md) notifications.<br/>                                                                                                                                                                                                                                                 |
| <span id="ENM_UPDATE"></span><span id="enm_update"></span><dl> <dt>**ENM\_UPDATE**</dt> </dl>                                  | Sends [EN\_UPDATE](en-update.md) notifications. <br/> **Rich Edit 2.0 and later:** this flag is ignored and the [EN\_UPDATE](en-update.md) notifications are always sent. However, if Rich Edit 3.0 emulates Microsoft Rich Edit 1.0, you must use this flag to send EN\_UPDATE notifications.<br/> |



## Remarks

The default event mask is ENM\_NONE in which case no notifications are sent to the parent window. You can retrieve and set the event mask for a rich edit control by using the [**EM\_GETEVENTMASK**](em-geteventmask.md) and [**EM\_SETEVENTMASK**](em-seteventmask.md) messages.

## Requirements



| Requirement | Value |
|-------------------|---------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>RichEdit.h</dt> </dl> |



 

