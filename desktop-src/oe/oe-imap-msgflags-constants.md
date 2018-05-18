---
title: IMAP\_MSGFLAGS
description: DWORD that identifies optional flags sent with some Internet Message Access Protocol (IMAP) server commands or returned in server responses.
ms.assetid: '6c3797b7-b576-4b13-a392-822a7e498037'
topic_type:
- apiref
api_name:
- IMAP_MSG_NOFLAGS
- IMAP_MSG_ANSWERED
- IMAP_MSG_FLAGGED
- IMAP_MSG_DELETED
- IMAP_MSG_SEEN
- IMAP_MSG_DRAFT
- IMAP_MSG_ALLFLAGS
api_location:
- Imnxport.h
api_type:
- HeaderDef
---

# IMAP\_MSGFLAGS

\[**IMAP\_MSGFLAGS** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

**DWORD** that identifies optional flags sent with some Internet Message Access Protocol (IMAP) server commands or returned in server responses.



| Constant/value                                                                                                                                                                                                                             | Description                              |
|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------|
| <span id="IMAP_MSG_NOFLAGS"></span><span id="imap_msg_noflags"></span><dl> <dt>**IMAP\_MSG\_NOFLAGS**</dt> <dt>0x00000000</dt> </dl>    | No message flags. <br/>            |
| <span id="IMAP_MSG_ANSWERED"></span><span id="imap_msg_answered"></span><dl> <dt>**IMAP\_MSG\_ANSWERED**</dt> <dt>0x00000001</dt> </dl> | The "Answered" message flag. <br/> |
| <span id="IMAP_MSG_FLAGGED"></span><span id="imap_msg_flagged"></span><dl> <dt>**IMAP\_MSG\_FLAGGED**</dt> <dt>0x00000002</dt> </dl>    | The "Flagged" message flag. <br/>  |
| <span id="IMAP_MSG_DELETED"></span><span id="imap_msg_deleted"></span><dl> <dt>**IMAP\_MSG\_DELETED**</dt> <dt>0x00000004</dt> </dl>    | The "Deleted" message flag. <br/>  |
| <span id="IMAP_MSG_SEEN"></span><span id="imap_msg_seen"></span><dl> <dt>**IMAP\_MSG\_SEEN**</dt> <dt>0x00000008</dt> </dl>             | The "Seen" message flag. <br/>     |
| <span id="IMAP_MSG_DRAFT"></span><span id="imap_msg_draft"></span><dl> <dt>**IMAP\_MSG\_DRAFT**</dt> <dt>0x00000010</dt> </dl>          | The "Draft" message flag. <br/>    |
| <span id="IMAP_MSG_ALLFLAGS"></span><span id="imap_msg_allflags"></span><dl> <dt>**IMAP\_MSG\_ALLFLAGS**</dt> <dt>0x0000001F</dt> </dl> | All the message flags. <br/>       |



## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Product<br/>                  | Outlook Express 6.0<br/>                                                          |
| Header<br/>                   | <dl> <dt>Imnxport.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Imnxport.idl</dt> </dl> |



 

 





