---
title: IMAP Dirty Flags
description: Do not use. Internet Message Access Protocol (IMAP) special folders list dirty flag values that can be set, and their meaning.
ms.assetid: a2df8874-df26-4c5d-98cb-189fa1233490
topic_type:
- apiref
api_name:
- IMAP_FLDRLIST_DIRTY
- IMAP_OE4MIGRATE_DIRTY
- IMAP_SENTITEMS_DIRTY
- IMAP_DRAFTS_DIRTY
- IMAP_DELETEDITEMS_DIRTY
- IMAP_JUNK_DIRTY
api_location:
- Imnact.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IMAP Dirty Flags

Do not use. Internet Message Access Protocol (IMAP) special folders list dirty flag values that can be set, and their meaning.



| Constant/value                                                                                                                                                                                                                                           | Description                                                                                   |
|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------|
| <span id="IMAP_FLDRLIST_DIRTY"></span><span id="imap_fldrlist_dirty"></span><dl> <dt>**IMAP\_FLDRLIST\_DIRTY**</dt> <dt>0x0001</dt> </dl>             | Indicates that the special folders list needs to be refreshed.<br/>                     |
| <span id="IMAP_OE4MIGRATE_DIRTY"></span><span id="imap_oe4migrate_dirty"></span><dl> <dt>**IMAP\_OE4MIGRATE\_DIRTY**</dt> <dt>0x0002</dt> </dl>       | Indicates that all special folders may not be present.<br/>                             |
| <span id="IMAP_SENTITEMS_DIRTY"></span><span id="imap_sentitems_dirty"></span><dl> <dt>**IMAP\_SENTITEMS\_DIRTY**</dt> <dt>0x0004</dt> </dl>          | Indicates that Sent Items special folder should be included in synchronization.<br/>    |
| <span id="IMAP_DRAFTS_DIRTY"></span><span id="imap_drafts_dirty"></span><dl> <dt>**IMAP\_DRAFTS\_DIRTY**</dt> <dt>0x0008</dt> </dl>                   | Indicates that Drafts special folder should be included in synchronization.<br/>        |
| <span id="IMAP_DELETEDITEMS_DIRTY"></span><span id="imap_deleteditems_dirty"></span><dl> <dt>**IMAP\_DELETEDITEMS\_DIRTY**</dt> <dt>0x0010</dt> </dl> | Indicates that Deleted Items special folder should be included in synchronization.<br/> |
| <span id="IMAP_JUNK_DIRTY"></span><span id="imap_junk_dirty"></span><dl> <dt>**IMAP\_JUNK\_DIRTY**</dt> <dt>0x0020</dt> </dl>                         | Indicates that Junk special folder should be included in synchronization.<br/>          |



## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Product<br/>                  | Outlook Express 6.0<br/>                                                        |
| Header<br/>                   | <dl> <dt>Imnact.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Imnact.idl</dt> </dl> |



 

 





