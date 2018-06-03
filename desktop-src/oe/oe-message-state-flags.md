---
title: Message State Flags
description: Do not use. Message state flag values that can be set and their meaning.
ms.assetid: 131eefb7-68c6-4d84-b5e2-408224744e80
topic_type:
- apiref
api_name:
- MSG_DELETED
- MSG_UNREAD
- MSG_SUBMITTED
- MSG_UNSENT
- MSG_RECEIVED
- MSG_NEWSMSG
- MSG_NOSECUI
- MSG_VOICEMAIL
- MSG_REPLIED
- MSG_FORWARDED
- MSG_RCPTSENT
- MSG_FLAGGED
api_location:
- Msoeapi.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Message State Flags

Do not use. Message state flag values that can be set and their meaning.



| Constant/value                                                                                                                                                                                                            | Description                                                                                       |
|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------|
| <span id="MSG_DELETED"></span><span id="msg_deleted"></span><dl> <dt>**MSG\_DELETED**</dt> <dt>0x0001</dt> </dl>       | The message has been deleted. Compacting folders will remove this message permanently.<br/> |
| <span id="MSG_UNREAD"></span><span id="msg_unread"></span><dl> <dt>**MSG\_UNREAD**</dt> <dt>0x0002</dt> </dl>          | The message has not been read.<br/>                                                         |
| <span id="MSG_SUBMITTED"></span><span id="msg_submitted"></span><dl> <dt>**MSG\_SUBMITTED**</dt> <dt>0x0004</dt> </dl> | The outgoing message is in the outbox and is waiting to be sent.<br/>                       |
| <span id="MSG_UNSENT"></span><span id="msg_unsent"></span><dl> <dt>**MSG\_UNSENT**</dt> <dt>0x0008</dt> </dl>          | The outgoing message has been saved locally but has not been sent.<br/>                     |
| <span id="MSG_RECEIVED"></span><span id="msg_received"></span><dl> <dt>**MSG\_RECEIVED**</dt> <dt>0x0010</dt> </dl>    | The message has been received from a server.<br/>                                           |
| <span id="MSG_NEWSMSG"></span><span id="msg_newsmsg"></span><dl> <dt>**MSG\_NEWSMSG**</dt> <dt>0x0020</dt> </dl>       | The message is associated with a newsgroup.<br/>                                            |
| <span id="MSG_NOSECUI"></span><span id="msg_nosecui"></span><dl> <dt>**MSG\_NOSECUI**</dt> <dt>0x0040</dt> </dl>       | Do not use.<br/>                                                                            |
| <span id="MSG_VOICEMAIL"></span><span id="msg_voicemail"></span><dl> <dt>**MSG\_VOICEMAIL**</dt> <dt>0x0080</dt> </dl> | The message's header has been set with the x-voicemail specification.<br/>                  |
| <span id="MSG_REPLIED"></span><span id="msg_replied"></span><dl> <dt>**MSG\_REPLIED**</dt> <dt>0x0100</dt> </dl>       | The message has been replied to.<br/>                                                       |
| <span id="MSG_FORWARDED"></span><span id="msg_forwarded"></span><dl> <dt>**MSG\_FORWARDED**</dt> <dt>0x0200</dt> </dl> | The message has been forwarded to another recipient.<br/>                                   |
| <span id="MSG_RCPTSENT"></span><span id="msg_rcptsent"></span><dl> <dt>**MSG\_RCPTSENT**</dt> <dt>0x0400</dt> </dl>    | The message's S/MIME receipt has been sent.<br/>                                            |
| <span id="MSG_FLAGGED"></span><span id="msg_flagged"></span><dl> <dt>**MSG\_FLAGGED**</dt> <dt>0x0800</dt> </dl>       | The message is "flagged" for urgent attention.<br/>                                         |



## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                            |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                   |
| Product<br/>                  | Outlook Express 6.0<br/>                                                         |
| Header<br/>                   | <dl> <dt>Msoeapi.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Msoeapi.idl</dt> </dl> |



 

 





