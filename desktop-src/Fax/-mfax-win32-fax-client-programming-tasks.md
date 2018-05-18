---
Description: 'This tutorial summarizes typical programming tasks required to incorporate the functionality of the Fax Service Client API in a fax client application in the Microsoft Win32 programming environment.'
ms.assetid: 'dd0be776-5fa0-4d68-847a-e00be65d1841'
title: Win32 Fax Client Programming Tasks
---

# Win32 Fax Client Programming Tasks

The following steps summarize typical programming tasks required to incorporate the functionality of the Fax Service Client API in a fax client application in the Microsoft Win32 programming environment.

## To code a fax client application

1.  Connect to the local fax server using a call to the [**FaxConnectFaxServer**](-mfax-faxconnectfaxserver.md) function. For more information, see [Connecting to a Fax Server](-mfax-connecting-to-a-fax-server.md).

2.  Call one or more of the fax service enumeration functions, if necessary. These functions permit viewing fax ports associated with the fax server and the routing information associated with a port. They also permit viewing a list of active fax jobs. The enumeration functions include the [**FaxEnumGlobalRoutingInfo**](-mfax-faxenumglobalroutinginfo.md), [**FaxEnumJobs**](-mfax-faxenumjobs.md), [**FaxEnumPorts**](-mfax-faxenumports.md), and [**FaxEnumRoutingMethods**](-mfax-faxenumroutingmethods.md) functions.

3.  Obtain the handle to a fax port using a call to the [**FaxOpenPort**](-mfax-faxopenport.md) function.

4.  Query and modify the routing information for a fax port, if necessary. Use calls to one or more of the following functions: [**FaxGetRoutingInfo**](-mfax-faxgetroutinginfo.md), [**FaxSetRoutingInfo**](-mfax-faxsetroutinginfo.md), and [**FaxEnableRoutingMethod**](-mfax-faxenableroutingmethod.md). For more information, see [Managing Fax Routing Data](-mfax-managing-fax-routing-data.md).

5.  Transmit a fax document using calls to the [**FaxSendDocument**](-mfax-faxsenddocument.md) function or the [**FaxSendDocumentForBroadcast**](-mfax-faxsenddocumentforbroadcast.md) function. Note that the application must supply transmission information such as the fax number and recipient data. For more information, see [Transmitting Faxes](-mfax-transmitting-faxes.md).

6.  Call the [**FaxFreeBuffer**](-mfax-faxfreebuffer.md) function to free resources allocated previously as the result of a function call by the application. This includes calls to the [**FaxCompleteJobParams**](-mfax-faxcompletejobparams.md) function and functions that begin with **FaxEnum** or **FaxGet**. For more information, see [Freeing Fax Resources](-mfax-freeing-fax-resources.md).

7.  Call the [**FaxClose**](-mfax-faxclose.md) function twice. The first call disconnects the application from the fax port. The second call disconnects the application from the fax server. For more information, see [Disconnecting from a Fax Server](-mfax-disconnecting-from-a-fax-server.md).

In addition, the application may need to call other functions to query device or server configuration data, to manage fax jobs, and to print transmissions. For more information, see [Fax Server Configuration Management](-mfax-fax-server-configuration-management.md), [Fax Device Management](-mfax-fax-device-management.md), and [Managing Fax Jobs](-mfax-managing-fax-jobs.md).

 

 



