---
description: PGM uses socket options to set state, provide multicast parameters, and otherwise implement its multicast capabilities.
ms.assetid: 91f5b051-cc42-46ba-88d9-680bd0367aff
title: PGM Socket Options
ms.topic: article
ms.date: 05/31/2018
---

# PGM Socket Options

PGM uses socket options to set state, provide multicast parameters, and otherwise implement its multicast capabilities. This page specifies how PGM socket options should be set, enumerates the socket options available for PGM, and where appropriate, provides usage examples and additional information for various options. For basic definitions of each PCM socket option, see [Socket Options](socket-options.md).

**Windows XP:** Reliable Multicast Programming (PGM) is not supported.

The following socket options are available for PGM senders:

<dl> RM\_LATEJOIN  
RM\_RATE\_WINDOW\_SIZE  
RM\_SEND\_WINDOW\_ADV\_RATE  
RM\_SENDER\_STATISTICS  
RM\_SENDER\_WINDOW\_ADVANCE\_METHOD  
RM\_SET\_MCAST\_TTL  
RM\_SET\_MESSAGE\_BOUNDARY  
RM\_SET\_SEND\_IF  
RM\_USE\_FEC  
</dl>

The RM\_SENDER\_WINDOW\_ADVANCE\_METHOD option specifies the method used when advancing the trailing edge send window. The optval parameter can only be E\_WINDOW\_ADVANCE\_BY\_TIME (the default). Note that E\_WINDOW\_USE\_AS\_DATA\_CACHE is not supported.

The following socket options are available for PGM receivers:

<dl> RM\_ADD\_RECEIVE\_IF  
RM\_DEL\_RECEIVE\_IF  
RM\_HIGH\_SPEED\_INTRANET\_OPT  
RM\_RECEIVER\_STATISTICS  
</dl>

## Setting PGM Socket Options

The following code snippet illustrates a programming guideline for setting PGM socket options:


```C++

ULONG       OptionData;    // This structure is option-dependent
//     :
setsockopt (s,
            IPPROTO_RM,
            Socket_Option,
            (char *) &OptionData,
            sizeof (OptionData));


```



In the snippet above, the type and contents of *OptionData* are dependent on the socket option being set. For all PGM socket options, the socket level is IPPROTO\_RM. PGM socket options must be set immediately following the call to the [**bind**](/windows/desktop/api/winsock/nf-winsock-bind) function, with the following exceptions:

<dl> RM\_SET\_MESSAGE\_BOUNDARY  
RM\_SENDER\_STATISTICS  
RM\_RECEIVER\_STATISTICS  
</dl>

 

 



