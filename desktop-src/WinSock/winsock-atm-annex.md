---
description: ATM is applicable to both LAN and WAN environments.
ms.assetid: 532a876c-9b31-410e-9331-5e8aa98ccaee
title: Winsock ATM Annex
ms.topic: article
ms.date: 05/31/2018
---

# Winsock ATM Annex

ATM is applicable to both LAN and WAN environments. An ATM network simultaneously transports a wide variety of network traffic — voice, data, image, and video. It provides users with a guaranteed quality of service on a per-virtual channel (VC) basis.



| Element          | Description                                                                                                                                                 |
|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Protocol name(s) | ATMPROTO\_AAL5, ATMPROTO\_AALUSER                                                                                                                           |
| Description      | ATM AAL5 provides a transport service that is connection oriented, message-boundary preserved, and QOS guaranteed. ATMPROTO\_AALUSER is a user-defined AAL. |
| Address family   | AF\_ATM                                                                                                                                                     |
| Header file      | Ws2atm.h                                                                                                                                                    |



 

This section describes the Asynchronous Transfer Mode (ATM)-specific extensions needed to support the native ATM services as exposed and specified in the ATM Forum User Network Interface (UNI) specification version 3.x (3.0 and 3.1). This document supports AAL type 5 (message mode) and user-defined AAL. Future versions of this document will support other types of AAL as well as UNI 4.0.

 

 



