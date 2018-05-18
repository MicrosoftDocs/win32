---
title: IMAP\_MBOXFLAGS
description: DWORD that identifies mailbox name attributes returned in the LIST or LSUB response.
ms.assetid: '4b23ab6e-86dc-41a3-8773-f948401e7795'
topic_type:
- apiref
api_name:
- IMAP_MBOX_NOFLAGS
- IMAP_MBOX_MARKED
- IMAP_MBOX_NOINFERIORS
- IMAP_MBOX_NOSELECT
- IMAP_MBOX_UNMARKED
- IMAP_MBOX_ALLFLAGS
api_location:
- Imnxport.h
api_type:
- HeaderDef
---

# IMAP\_MBOXFLAGS

\[**IMAP\_MBOXFLAGS** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

**DWORD** that identifies mailbox name attributes returned in the LIST or LSUB response.



| Constant/value                                                                                                                                                                                                                                         | Description                                                     |
|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------|
| <span id="IMAP_MBOX_NOFLAGS"></span><span id="imap_mbox_noflags"></span><dl> <dt>**IMAP\_MBOX\_NOFLAGS**</dt> <dt>0x00000000</dt> </dl>             | No mailbox name attributes returned. <br/>                |
| <span id="IMAP_MBOX_MARKED"></span><span id="imap_mbox_marked"></span><dl> <dt>**IMAP\_MBOX\_MARKED**</dt> <dt>0x00000001</dt> </dl>                | The "Marked" mailbox name attribute. <br/>                |
| <span id="IMAP_MBOX_NOINFERIORS"></span><span id="imap_mbox_noinferiors"></span><dl> <dt>**IMAP\_MBOX\_NOINFERIORS**</dt> <dt>0x00000002</dt> </dl> | The "Noinferiors" mailbox name attribute. <br/>           |
| <span id="IMAP_MBOX_NOSELECT"></span><span id="imap_mbox_noselect"></span><dl> <dt>**IMAP\_MBOX\_NOSELECT**</dt> <dt>0x00000004</dt> </dl>          | The "Noselect" mailbox name attribute. <br/>              |
| <span id="IMAP_MBOX_UNMARKED"></span><span id="imap_mbox_unmarked"></span><dl> <dt>**IMAP\_MBOX\_UNMARKED**</dt> <dt>0x00000008</dt> </dl>          | The "Unmarked" mailbox name attribute. <br/>              |
| <span id="IMAP_MBOX_ALLFLAGS"></span><span id="imap_mbox_allflags"></span><dl> <dt>**IMAP\_MBOX\_ALLFLAGS**</dt> <dt>0x0000000F</dt> </dl>          | All the mailbox name attributes have been returned. <br/> |



## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Product<br/>                  | Outlook Express 6.0<br/>                                                          |
| Header<br/>                   | <dl> <dt>Imnxport.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Imnxport.idl</dt> </dl> |



 

 





