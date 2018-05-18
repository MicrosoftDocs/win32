---
title: NNTP User Information Types
description: Do not use. Network News Transport Protocol (NNTP) user information type values that can be set, and their meaning.
ms.assetid: 'adf002f6-842f-44c5-a82e-0f1cabee5a7c'
topic_type:
- apiref
api_name:
- NNTP_USER_AUTOCONFIG
- NNTP_USER_NOTIFIED
- NNTP_USER_DONTSHOW
- NNTP_USER_APPROVED
api_location:
- Imnact.h
api_type:
- HeaderDef
---

# NNTP User Information Types

Do not use. Network News Transport Protocol (NNTP) user information type values that can be set, and their meaning.



| Constant/value                                                                                                                                                                                                                                  | Description                                                       |
|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------|
| <span id="NNTP_USER_AUTOCONFIG"></span><span id="nntp_user_autoconfig"></span><dl> <dt>**NNTP\_USER\_AUTOCONFIG**</dt> <dt>0x0000</dt> </dl> | Suggested display name and email address.<br/>              |
| <span id="NNTP_USER_NOTIFIED"></span><span id="nntp_user_notified"></span><dl> <dt>**NNTP\_USER\_NOTIFIED**</dt> <dt>0x0001</dt> </dl>       | User information has been viewed, but not approved.<br/>    |
| <span id="NNTP_USER_DONTSHOW"></span><span id="nntp_user_dontshow"></span><dl> <dt>**NNTP\_USER\_DONTSHOW**</dt> <dt>0x0002</dt> </dl>       | Approval of user information was deferred.<br/>             |
| <span id="NNTP_USER_APPROVED"></span><span id="nntp_user_approved"></span><dl> <dt>**NNTP\_USER\_APPROVED**</dt> <dt>0x0003</dt> </dl>       | User information is approved, or was entered manually.<br/> |



## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Product<br/>                  | Outlook Express 6.0<br/>                                                        |
| Header<br/>                   | <dl> <dt>Imnact.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Imnact.idl</dt> </dl> |



 

 





