---
description: Network DDE is used to initiate and maintain the network connections needed for DDE conversations between applications running on different computers in a network.
ms.assetid: f9eee391-2b4a-4c17-bea5-72cda5124e1c
title: About Network DDE
ms.topic: article
ms.date: 05/31/2018
---

# About Network DDE

\[Network DDE is no longer supported. Nddeapi.dll is present on Windows Vista, but all function calls return NDDE\_NOT\_IMPLEMENTED.\]

Network DDE is used to initiate and maintain the network connections needed for DDE conversations between applications running on different computers in a network. A DDE *conversation* is the interaction between client and server applications. You use network DDE along with DDE and the DDE management library (DDEML) in your application.

DDE is a form of interprocess communication that uses shared memory to exchange data between applications. Applications can use DDE for one time data transfers or for ongoing exchanges and updating data. For more information on DDE, see [Dynamic Data Exchange](../dataxchg/dynamic-data-exchange.md).

DDEML simplifies the task of adding DDE capability to an application. Instead of sending, posting, and processing DDE messages directly, an application uses the functions provided by the DDEML to manage DDE conversations. For more information on DDEML, see [Dynamic Data Exchange Management Library](../dataxchg/dynamic-data-exchange-management-library.md).

## Network DDE Files

To use the API elements of network DDE, you must include the NDDEApi.h header file in your source files and include NDDEApi.lib file on your link line. You must also make sure that the NDDEApi.dll file is loaded.

For more information, see the following topics:

-   [Network DDE Agent](network-dde-agent.md)
-   [DDE Shares](dde-shares.md)
-   [Trusted Shares and Security](trusted-shares-and-security.md)
-   [Managing DDE Shares](managing-dde-shares.md)

 

 
