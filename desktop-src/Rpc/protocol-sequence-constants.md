---
title: Protocol Sequence Constants
description: Microsoft RPC supports the following protocol sequences.
ms.assetid: 51284532-b0ac-4bf2-b322-91393b2b9dc6
topic_type:
- apiref
api_name:
- ncacn_nb_tcp
- ncacn_nb_ipx
- ncacn_nb_nb
- ncacn_ip_tcp
- ncacn_np
- ncacn_spx
- ncacn_dnet_nsp
- ncacn_at_dsp
- ncacn_vns_spp
- ncadg_ip_udp
- ncadg_ipx
- ncadg_mq
- ncacn_http
- ncalrpc
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# Protocol Sequence Constants

Microsoft RPC supports the following protocol sequences.



| Constant/value                                                                                                                                                                                                                                                                                 | Description                                                                                                                                                                         |
|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="ncacn_nb_tcp"></span><span id="NCACN_NB_TCP"></span><dl> <dt>**ncacn\_nb\_tcp**</dt> <dt>Connection-oriented NetBIOS over Transmission Control Protocol (TCP)</dt> </dl>          | Client only: MS-DOS, Windows 3.*x* Client and Server: Windows Server 2003, Windows XP, Windows 2000, Windows NT<br/>                                                          |
| <span id="ncacn_nb_ipx"></span><span id="NCACN_NB_IPX"></span><dl> <dt>**ncacn\_nb\_ipx**</dt> <dt>Connection-oriented NetBIOS over Internet Packet Exchange (IPX)</dt> </dl>               | Client only: MS-DOS, Windows 3.*x* Client and Server: Windows Server 2003, Windows XP, Windows 2000, Windows NT<br/>                                                          |
| <span id="ncacn_nb_nb"></span><span id="NCACN_NB_NB"></span><dl> <dt>**ncacn\_nb\_nb**</dt> <dt>Connection-oriented NetBIOS Enhanced User Interface (NetBEUI)</dt> </dl>                    | Client only: MS-DOS, Windows 3.*x* Client and Server: Windows Server 2003, Windows XP, Windows 2000, Windows NT, Windows Me, Windows 98, Windows 95<br/>                      |
| <span id="ncacn_ip_tcp"></span><span id="NCACN_IP_TCP"></span><dl> <dt>**ncacn\_ip\_tcp**</dt> <dt>Connection-oriented Transmission Control Protocol/Internet Protocol (TCP/IP)</dt> </dl>  | Client only: MS-DOS, Windows 3.*x*, and Apple Macintosh Client and Server: Windows Server 2003, Windows XP, Windows 2000, Windows NT, Windows Me, Windows 98, Windows 95<br/> |
| <span id="ncacn_np"></span><span id="NCACN_NP"></span><dl> <dt>**ncacn\_np**</dt> <dt>Connection-oriented named pipes</dt> </dl>                                                            | Client only: MS-DOS, Windows 3.*x*, Windows 95 Client and Server: Windows Server 2003, Windows XP, Windows 2000, Windows NT<br/>                                              |
| <span id="ncacn_spx"></span><span id="NCACN_SPX"></span><dl> <dt>**ncacn\_spx**</dt> <dt>Connection-oriented Sequenced Packet Exchange (SPX)</dt> </dl>                                     | Client only: MS-DOS, Windows 3.*x* Client and Server: Windows Server 2003, Windows XP, Windows 2000, Windows NT, Windows Me, Windows 98, Windows 95<br/>                      |
| <span id="ncacn_dnet_nsp"></span><span id="NCACN_DNET_NSP"></span><dl> <dt>**ncacn\_dnet\_nsp**</dt> <dt>Connection-oriented DECnet transport</dt> </dl>                                    | Client only: MS-DOS, Windows 3.*x*<br/>                                                                                                                                       |
| <span id="ncacn_at_dsp"></span><span id="NCACN_AT_DSP"></span><dl> <dt>**ncacn\_at\_dsp**</dt> <dt>Connection-oriented AppleTalk DSP</dt> </dl>                                             | Client: Apple Macintosh Server: Windows Server 2003, Windows XP, Windows 2000, Windows NT<br/>                                                                                |
| <span id="ncacn_vns_spp"></span><span id="NCACN_VNS_SPP"></span><dl> <dt>**ncacn\_vns\_spp**</dt> <dt>Connection-oriented Vines scalable parallel processing (SPP) transport</dt> </dl>     | Client only: MS-DOS, Windows 3.*x* Client and Server: Windows Server 2003, Windows XP, Windows 2000, Windows NT<br/>                                                          |
| <span id="ncadg_ip_udp"></span><span id="NCADG_IP_UDP"></span><dl> <dt>**ncadg\_ip\_udp**</dt> <dt>Datagram (connectionless) User Datagram Protocol/Internet Protocol (UDP/IP)</dt> </dl>   | Client only: MS-DOS, Windows 3.*x* Client and Server: Windows Server 2003, Windows XP, Windows 2000, Windows NT<br/>                                                          |
| <span id="ncadg_ipx"></span><span id="NCADG_IPX"></span><dl> <dt>**ncadg\_ipx**</dt> <dt>Datagram (connectionless) IPX</dt> </dl>                                                           | Client only: MS-DOS, Windows 3.*x* Client and Server: Windows Server 2003, Windows XP, Windows 2000, Windows NT<br/>                                                          |
| <span id="ncadg_mq"></span><span id="NCADG_MQ"></span><dl> <dt>**ncadg\_mq**</dt> <dt>Datagram (connectionless) over the Microsoft Message Queue Server (MSMQ)</dt> </dl>                   | Client only: Windows Me/98/95 Client and Server: Windows Server 2003, Windows XP, Windows 2000, Windows NT Server 4.0 with SP3 and later<br/>                                 |
| <span id="ncacn_http"></span><span id="NCACN_HTTP"></span><dl> <dt>**ncacn\_http**</dt> <dt>Connection-oriented TCP/IP using Microsoft Internet Information Server as HTTP proxy</dt> </dl> | Client only: Windows Me/98/95 Client and Server: Windows Server 2003, Windows XP, Windows 2000<br/>                                                                           |
| <span id="ncalrpc"></span><span id="NCALRPC"></span><dl> <dt>**ncalrpc**</dt> <dt>Local procedure call</dt> </dl>                                                                           | Client and Server: Windows Server 2003, Windows XP, Windows 2000, Windows NT, Windows Me, Windows 98, Windows 95<br/>                                                         |



## Remarks

The [**ncalrpc**](/windows/desktop/Midl/ncalrpc) transport supports RPC\_C\_AUTHN\_WINNT authentication only. For more information, see [Security](security.md) and [Authentication-Service Constants](authentication-service-constants.md).

Microsoft RPC supports [**RpcBindingCopy**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcbindingcopy) only in client applications, not in server applications.

 

