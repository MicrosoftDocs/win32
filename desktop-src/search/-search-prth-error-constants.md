---
description: 'Error messages returned by protocol handlers:'
ms.assetid: b5e99ad1-1698-483c-8173-796af33085c4
title: Search Protocol Handler Error Messages (Searchapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# Search Protocol Handler Error Messages

Error messages returned by protocol handlers:



| Constant/value                                                                                                                                                                                                                                                    | Description                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="PRTH_E_ACCESS_DENIED"></span><span id="prth_e_access_denied"></span><dl> <dt>**PRTH\_E\_ACCESS\_DENIED**</dt> <dt>0x80041205L</dt> </dl>             | Access was denied. If this occurs during an incremental crawl, the file is deleted from the gatherer's URL queue.<br/>                                                                                                                                                                                                                                                                                                                |
| <span id="PRTH_E_ACL_IS_READ_NONE"></span><span id="prth_e_acl_is_read_none"></span><dl> <dt>**PRTH\_E\_ACL\_IS\_READ\_NONE**</dt> <dt>0x80041211L</dt> </dl>  | Item will not be indexed. Its ACL allows no one to read the item.<br/>                                                                                                                                                                                                                                                                                                                                                                |
| <span id="PRTH_E_ACL_TOO_BIG"></span><span id="prth_e_acl_too_big"></span><dl> <dt>**PRTH\_E\_ACL\_TOO\_BIG**</dt> <dt>0x80041212L</dt> </dl>                  | ACL exceeded 64 KB. Search does not index the item.<br/>                                                                                                                                                                                                                                                                                                                                                                              |
| <span id="PRTH_E_BAD_REQUEST"></span><span id="prth_e_bad_request"></span><dl> <dt>**PRTH\_E\_BAD\_REQUEST**</dt> <dt>0x80041208L</dt> </dl>                   | Request was invalid because of an error in the URL.<br/>                                                                                                                                                                                                                                                                                                                                                                              |
| <span id="PRTH_E_COMM_ERROR"></span><span id="prth_e_comm_error"></span><dl> <dt>**PRTH\_E\_COMM\_ERROR**</dt> <dt>0x80041200L</dt> </dl>                      | Indicates a communication or server error. If there are too many of these errors for a particular server, the gatherer marks the server as unavailable.<br/>                                                                                                                                                                                                                                                                          |
| <span id="PRTH_E_NOT_REDIRECTED"></span><span id="prth_e_not_redirected"></span><dl> <dt>**PRTH\_E\_NOT\_REDIRECTED**</dt> <dt>0x80041207L</dt> </dl>          | Redirected URL does not exist.<br/>                                                                                                                                                                                                                                                                                                                                                                                                   |
| <span id="PRTH_E_OBJ_NOT_FOUND"></span><span id="prth_e_obj_not_found"></span><dl> <dt>**PRTH\_E\_OBJ\_NOT\_FOUND**</dt> <dt>0x80041201L</dt> </dl>            | Object not found. Indicates that the gatherer should delete the document from the queue if it is not found during an incremental crawl.<br/>                                                                                                                                                                                                                                                                                          |
| <span id="PRTH_E_REQUEST_ERROR"></span><span id="prth_e_request_error"></span><dl> <dt>**PRTH\_E\_REQUEST\_ERROR**</dt> <dt>0x80041202L</dt> </dl>             | Options used are not supported.<br/>                                                                                                                                                                                                                                                                                                                                                                                                  |
| <span id="PRTH_E_SERVER_ERROR"></span><span id="prth_e_server_error"></span><dl> <dt>**PRTH\_E\_SERVER\_ERROR**</dt> <dt>0x80041206L</dt> </dl>                | Communication or server error. If there are too many of these errors for a particular server, the gatherer marks the server as unavailable.<br/>                                                                                                                                                                                                                                                                                      |
| <span id="PRTH_S_NOT_ALL_PARTS"></span><span id="prth_s_not_all_parts"></span><dl> <dt>**PRTH\_S\_NOT\_ALL\_PARTS**</dt> <dt>0x8004121BL</dt> </dl>            | Parts of an item cannot be accessed.<br/>                                                                                                                                                                                                                                                                                                                                                                                             |
| <span id="PRTH_S_NOT_MODIFIED"></span><span id="prth_s_not_modified"></span><dl> <dt>**PRTH\_S\_NOT\_MODIFIED**</dt> <dt>0x00041203L</dt> </dl>                | Item content has not changed. If this error occurs during an incremental crawl, the gatherer skips this item because the item has not changed.<br/>                                                                                                                                                                                                                                                                                   |
| <span id="PRTH_S_TRY_IMPERSONATING"></span><span id="prth_s_try_impersonating"></span><dl> <dt>**PRTH\_S\_TRY\_IMPERSONATING**</dt> <dt>0x00041225L</dt> </dl> | Item should be accessed while impersonating a user. The protocol handler is expected to implement [**IUrlAccessor3::GetImpersonationSidBlobs**](/windows/desktop/api/Searchapi/nf-searchapi-iurlaccessor3-getimpersonationsidblobs) so that the search protocol host can retrieve a list of SIDs to use for impersonation and can revert to using [**IUrlAccessor2**](/windows/desktop/api/Searchapi/nn-searchapi-iurlaccessor2), impersonating one of the allowed users when opening the item. <br/> |



## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP with SP2, Windows Vista \[desktop apps only\]<br/>                    |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                   |
| Redistributable<br/>          | Windows Desktop Search (WDS) 3.0<br/>                                            |
| Header<br/>                   | <dl> <dt>Searchapi.h</dt> </dl> |



 

 




