---
description: The following is a list of .lib files required to compile various TAPI 3 applications, as of 1/22/01.
ms.assetid: f1765829-9a5d-4e85-b898-6679279aa6d9
title: Libraries Required
ms.topic: article
ms.date: 05/31/2018
---

# Libraries Required

A list of .lib files required to compile various TAPI 3 applications, as of 1/22/01:

-   Advapi32.lib
-   Amstrmid.lib (ActiveMovie GUIDs)
-   Kernel32.lib
-   Mdhcpid.lib (multicast GUIDs)
-   Ole32.lib (COM)
-   Oleaut32.lib (COM Automation)
-   Rendid.lib (Rendezvous GUIDs)
-   Rpcndr.lib
-   Rpcns4.lib
-   Rpcrt4.lib
-   Sdpblbid.lib (Session Descriptor Protocol (SDP) GUIDs)
-   Strmiids.lib
-   User32.lib
-   Uuid.lib
-   Wldap32.lib
-   Ws2\_32.lib

If you are using Microsoft Visual Studio, you may need to update your version. In particular, Link.exe must carry a date of 3/19/98 or later.

Compiler defines must include \_WIN32\_WINNT set to at least 0x500 and \_WIN32\_DCOM.

 

 



