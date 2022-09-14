---
description: PNRP NSP Error Codes
ms.assetid: adf40b1a-c5d6-418d-a012-cf6ba7d4fa24
title: PNRP NSP Error Codes
ms.topic: article
ms.date: 05/31/2018
---

# PNRP NSP Error Codes

If the Namespace Provider (NSP) function returns a **SOCKET\_ERROR**, [WSAGetLastError](winsock-nsp-reference-links.md) must be used to obtain more error information. The PNRP NSP returns the following error codes:



| Term                                                                                                                                                                     | Description                                                                                                        |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|
| <span id="WSA_E_CANCELLED"></span><span id="wsa_e_cancelled"></span>WSA\_E\_CANCELLED<br/>                                                                         | An operation is canceled.<br/>                                                                               |
| <span id="__WSA_E_NO_MORE"></span><span id="__wsa_e_no_more"></span> WSA\_E\_NO\_MORE<br/>                                                                         | The results of a resolved request are not ready. This may not be an error.<br/>                              |
| <span id="_WSA_IO_PENDING_"></span><span id="_wsa_io_pending_"></span> WSA\_IO\_PENDING <br/>                                                                      | An operation is not complete.<br/>                                                                           |
| <span id="WSA_NOT_ENOUGH_MEMORY"></span><span id="wsa_not_enough_memory"></span>WSA\_NOT\_ENOUGH\_MEMORY<br/>                                                      | There is not enough memory to complete a specified action.<br/>                                              |
| <span id="WSA_OPERATION_ABORTED"></span><span id="wsa_operation_aborted"></span>WSA\_OPERATION\_ABORTED<br/>                                                       | An operation is canceled.<br/>                                                                               |
| <span id="WSA_PNRP_CLOUD_DISABLED"></span><span id="wsa_pnrp_cloud_disabled"></span>WSA\_PNRP\_CLOUD\_DISABLED<br/>                                                | A specified cloud name is disabled.<br/>                                                                     |
| <span id="WSA_PNRP_CLOUD_NOT_FOUND"></span><span id="wsa_pnrp_cloud_not_found"></span>WSA\_PNRP\_CLOUD\_NOT\_FOUND<br/>                                            | A specified cloud name is not available.<br/>                                                                |
| <span id="WSA_PNRP_CLOUD_IS_SEARCH_ONLY"></span><span id="wsa_pnrp_cloud_is_search_only"></span>WSA\_PNRP\_CLOUD\_IS\_SEARCH\_ONLY<br/>                            | An attempt has been made to register a name in a cloud that has been configured to be resolve only.<br/>     |
| <span id="WSA_PNRP_CLIENT_INVALID_COMPARTMENT_ID"></span><span id="wsa_pnrp_client_invalid_compartment_id"></span>WSA\_PNRP\_CLIENT\_INVALID\_COMPARTMENT\_ID<br/> | Using PNRP in a compartment outside of the default. PNRP will only work in the default compartment.<br/>     |
| <span id="WSA_PNRP_INVALID_IDENTITY"></span><span id="wsa_pnrp_invalid_identity"></span>WSA\_PNRP\_INVALID\_IDENTITY<br/>                                          | A specified identity cannot be accessed.<br/>                                                                |
| <span id="WSA_PNRP_TOO_MUCH_LOAD"></span><span id="wsa_pnrp_too_much_load"></span>WSA\_PNRP\_TOO\_MUCH\_LOAD<br/>                                                  | A peer name cannot be created because the computer does not have the resources to process the request. <br/> |
| <span id="WSAEFAULT"></span><span id="wsaefault"></span>WSAEFAULT<br/>                                                                                             | A operation is not allowed in the current state.<br/>                                                        |
| <span id="WSAEINVAL"></span><span id="wsaeinval"></span>WSAEINVAL<br/>                                                                                             | An invalid parameter or combination of parameters is specified.<br/>                                         |
| <span id="WSAENETUNREACH"></span><span id="wsaenetunreach"></span>WSAENETUNREACH<br/>                                                                              | A connection to the network is lost.<br/>                                                                    |
| <span id="WSAENOTIMPLEMENTED"></span><span id="wsaenotimplemented"></span>WSAENOTIMPLEMENTED<br/>                                                                  | A specified functionality is not implemented by PNRP.<br/>                                                   |
| <span id="WSAEOPNOTSUPP"></span><span id="wsaeopnotsupp"></span>WSAEOPNOTSUPP<br/>                                                                                 | A specified functionality is not supported by PNRP.<br/>                                                     |
| <span id="WSAEWOULDBLOCK"></span><span id="wsaewouldblock"></span>WSAEWOULDBLOCK<br/>                                                                              | An operation is not complete.<br/>                                                                           |
| <span id="__WSASERVICE_NOT_FOUND"></span><span id="__wsaservice_not_found"></span> WSASERVICE\_NOT\_FOUND<br/>                                                     | A specified provider, namespace, or service ID are not supported.<br/>                                       |
| <span id="WSASYSNOTREADY"></span><span id="wsasysnotready"></span>WSASYSNOTREADY<br/>                                                                              | The service is not started.<br/>                                                                             |



 

 

 




