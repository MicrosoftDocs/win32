---
Description: The functions used with the Fax Service Client API fall into the following functional groupings. An alphabetic list follows.
ms.assetid: b076b5ba-09af-4312-90c1-27abd0b859df
title: Fax Service Client API Functions
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Fax Service Client API Functions

The functions used with the Fax Service Client API fall into the following functional groupings. An alphabetic list follows.

-   [Configuration Management Functions](#configuration-management-functions)
-   [Device Management Functions](#device-management-functions)
-   [Document Management Functions](#document-management-functions)
-   [Job Management Functions](#job-management-functions)
-   [Fax Utility Functions](#fax-utility-functions)
-   [Fax Service Client Functions Alphabetic List](#fax-service-client-functions-alphabetic-list)

## Configuration Management Functions

The Fax Service Client API configuration management functions enable a fax client application to connect to a fax server and communicate with the server using a fax event queue. These functions also provide the application with access to the server's logging categories, global configuration settings, and fax routing method data.



| Topic                                                              | Contents                                                                                                                                                                                                                                                                                                                                                                                           |
|--------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**FaxClose**](/windows/previous-versions/Winfax/nc-winfax-pfaxclose?branch=master)                                 | The [**FaxClose**](/windows/previous-versions/Winfax/nc-winfax-pfaxclose?branch=master) function closes the following types of fax handles:<br/>                                                                                                                                                                                                                                                                                              |
| [**FaxConnectFaxServer**](/windows/previous-versions/Winfax/nf-winfax-faxconnectfaxservera?branch=master)           | The [**FaxConnectFaxServer**](/windows/previous-versions/Winfax/nf-winfax-faxconnectfaxservera?branch=master) function connects a fax client application to the local fax server. The function returns a fax server handle that is required to call other fax client functions that facilitate job, device, configuration, and document management.<br/>                                                                                      |
| [**FaxEnumGlobalRoutingInfo**](/windows/previous-versions/Winfax/nf-winfax-faxenumglobalroutinginfoa?branch=master) | The [**FaxEnumGlobalRoutingInfo**](/windows/previous-versions/Winfax/nf-winfax-faxenumglobalroutinginfoa?branch=master) function enumerates all fax routing methods associated with a specific fax server. The function returns to the fax client application fax routing method information that applies globally to the server, such as routing priority.<br/>                                                                              |
| [**FaxGetConfiguration**](/windows/previous-versions/Winfax/nf-winfax-faxgetconfigurationa?branch=master)           | The [**FaxGetConfiguration**](/windows/previous-versions/Winfax/nf-winfax-faxgetconfigurationa?branch=master) function returns to a fax client application the global configuration settings for the fax server to which the client has connected. The data includes, among other items, retransmission, branding, archive and cover page settings; discount rate periods; and the status of the fax server queue.<br/>                       |
| [**FaxGetLoggingCategories**](/windows/previous-versions/Winfax/nf-winfax-faxgetloggingcategoriesa?branch=master)   | The [**FaxGetLoggingCategories**](/windows/previous-versions/Winfax/nf-winfax-faxgetloggingcategoriesa?branch=master) function returns to a fax client application the current logging categories for the fax server to which the client has connected. A logging category determines the errors or other events the fax server records in the application event log.<br/>                                                                    |
| [**FaxInitializeEventQueue**](/windows/previous-versions/Winfax/nc-winfax-pfaxinitializeeventqueue?branch=master)   | The [**FaxInitializeEventQueue**](/windows/previous-versions/Winfax/nc-winfax-pfaxinitializeeventqueue?branch=master) function creates a fax event queue for the calling fax client application. The queue enables the application to receive notifications of asynchronous events from the fax server.<br/>                                                                                                                                  |
| [**FaxSetConfiguration**](/windows/previous-versions/Winfax/nf-winfax-faxsetconfigurationa?branch=master)           | A fax client application calls the [**FaxSetConfiguration**](/windows/previous-versions/Winfax/nf-winfax-faxsetconfigurationa?branch=master) function to change the global configuration settings for the fax server to which the client has connected. The configuration data can include, among other items, retransmission, branding, archive and cover page settings; discount rate periods; and the status of the fax server queue.<br/> |
| [**FaxSetGlobalRoutingInfo**](/windows/previous-versions/Winfax/nf-winfax-faxsetglobalroutinginfoa?branch=master)   | A fax management application calls the [**FaxSetGlobalRoutingInfo**](/windows/previous-versions/Winfax/nf-winfax-faxsetglobalroutinginfoa?branch=master) function to modify fax routing method data, such as routing priority, that applies globally to the fax server.<br/>                                                                                                                                                                  |
| [**FaxSetLoggingCategories**](/windows/previous-versions/Winfax/nf-winfax-faxsetloggingcategoriesa?branch=master)   | A fax client application calls the [**FaxSetLoggingCategories**](/windows/previous-versions/Winfax/nf-winfax-faxsetloggingcategoriesa?branch=master) function to modify the current logging categories for the fax server to which the client has connected. A logging category determines the errors or other events the fax server records in the application event log.<br/>                                                               |



 

## Device Management Functions

The Fax Service Client API device management functions enable a fax administration application to query and administer the configuration of a fax port. These functions also provide access to information about the fax routing methods associated with the port.



| Topic                                                          | Contents                                                                                                                                                                                                                                                                                                                           |
|----------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**FaxEnableRoutingMethod**](/windows/previous-versions/Winfax/nf-winfax-faxenableroutingmethoda?branch=master) | The [**FaxEnableRoutingMethod**](/windows/previous-versions/Winfax/nf-winfax-faxenableroutingmethoda?branch=master) function enables or disables a fax routing method for a specific fax device. A fax administration application typically calls this function for device management.<br/>                                                                                   |
| [**FaxEnumPorts**](/windows/previous-versions/Winfax/nf-winfax-faxenumportsa?branch=master)                     | The [**FaxEnumPorts**](/windows/previous-versions/Winfax/nf-winfax-faxenumportsa?branch=master) function enumerates all fax devices currently attached to the fax server to which the client has connected. The function returns detailed information for each fax port to the fax client application.<br/>                                                                   |
| [**FaxEnumRoutingMethods**](/windows/previous-versions/Winfax/nf-winfax-faxenumroutingmethodsa?branch=master)   | The [**FaxEnumRoutingMethods**](/windows/previous-versions/Winfax/nf-winfax-faxenumroutingmethodsa?branch=master) function enumerates all fax routing methods for a specific fax device. The function returns information about each routing method to a fax client application.<br/>                                                                                         |
| [**FaxGetDeviceStatus**](/windows/previous-versions/Winfax/nf-winfax-faxgetdevicestatusa?branch=master)         | The [**FaxGetDeviceStatus**](/windows/previous-versions/Winfax/nf-winfax-faxgetdevicestatusa?branch=master) function returns to a fax client application current status information for the fax device of interest. The returned data includes, among other items, device and station identifiers, sender and recipient names, and routing information.<br/>                  |
| [**FaxGetPort**](/windows/previous-versions/Winfax/nf-winfax-faxgetporta?branch=master)                         | The [**FaxGetPort**](/windows/previous-versions/Winfax/nf-winfax-faxgetporta?branch=master) function returns information for a specified fax port to a fax client application. The data includes, among other items, the permanent line identifier, the current status and capability of the port, and the transmitting and called station identifiers. <br/>                 |
| [**FaxGetRoutingInfo**](/windows/previous-versions/Winfax/nf-winfax-faxgetroutinginfoa?branch=master)           | The [**FaxGetRoutingInfo**](/windows/previous-versions/Winfax/nf-winfax-faxgetroutinginfoa?branch=master) function returns to a fax client application routing information for a fax routing method that is associated with a specific fax device.<br/>                                                                                                                       |
| [**FaxOpenPort**](/windows/previous-versions/Winfax/nc-winfax-pfaxopenport?branch=master)                       | The [**FaxOpenPort**](/windows/previous-versions/Winfax/nc-winfax-pfaxopenport?branch=master) function returns a fax port handle to a fax client application. The port handle is required when the application calls other fax client functions that facilitate device management and fax document routing.<br/>                                                              |
| [**FaxSetPort**](/windows/previous-versions/Winfax/nf-winfax-faxsetporta?branch=master)                         | A fax client application calls the [**FaxSetPort**](/windows/previous-versions/Winfax/nf-winfax-faxsetporta?branch=master) function to change the configuration of the fax port of interest. The configuration data can include, among other items, the capability of the port, its priority, rings before answer, and the transmitting and called station identifiers..<br/> |
| [**FaxSetRoutingInfo**](/windows/previous-versions/Winfax/nf-winfax-faxsetroutinginfoa?branch=master)           | A fax management application calls the [**FaxSetRoutingInfo**](/windows/previous-versions/Winfax/nf-winfax-faxsetroutinginfoa?branch=master) function to modify the routing information for a fax routing method that is associated with a specific fax device.<br/>                                                                                                          |



 

## Document Management Functions

The Fax Service Client API document management functions enable a fax client application to queue outgoing fax jobs and print fax transmissions. These functions also provide the ability to specify a cover page template file and user information to render onto the template at transmission time.



| Topic                                                                    | Contents                                                                                                                                                                                                                                                                                                             |
|--------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**FAX\_RECIPIENT\_CALLBACK**](/windows/previous-versions/Winfax/nc-winfax-pfax_recipient_callbacka?branch=master)         | The [**FAX\_RECIPIENT\_CALLBACK**](/windows/previous-versions/Winfax/nc-winfax-pfax_recipient_callbacka?branch=master) function is an application-defined or library-defined callback function that the [**FaxSendDocumentForBroadcast**](/windows/previous-versions/Winfax/nf-winfax-faxsenddocumentforbroadcasta?branch=master) function calls to retrieve user-specific information for the transmission.<br/> |
| [**FaxPrintCoverPage**](/windows/previous-versions/Winfax/nf-winfax-faxprintcoverpagea?branch=master)                     | The [**FaxPrintCoverPage**](/windows/previous-versions/Winfax/nf-winfax-faxprintcoverpagea?branch=master) function prints a fax transmission cover page to the specified device context for a fax client application.<br/>                                                                                                                                      |
| [**FaxSendDocument**](/windows/previous-versions/Winfax/nf-winfax-faxsenddocumenta?branch=master)                         | A fax client application calls the [**FaxSendDocument**](/windows/previous-versions/Winfax/nf-winfax-faxsenddocumenta?branch=master) function to queue a fax job that will transmit an outgoing fax transmission.<br/>                                                                                                                                          |
| [**FaxSendDocumentForBroadcast**](/windows/previous-versions/Winfax/nf-winfax-faxsenddocumentforbroadcasta?branch=master) | A fax client application calls the [**FaxSendDocumentForBroadcast**](/windows/previous-versions/Winfax/nf-winfax-faxsenddocumentforbroadcasta?branch=master) function to queue several fax jobs that will transmit the same outgoing fax transmission to several recipients.<br/>                                                                               |
| [**FaxStartPrintJob**](/windows/previous-versions/Winfax/nf-winfax-faxstartprintjoba?branch=master)                       | A fax client application calls the [**FaxStartPrintJob**](/windows/previous-versions/Winfax/nf-winfax-faxstartprintjoba?branch=master) function to start printing an outbound fax transmission on the specified fax printer.<br/>                                                                                                                               |



 

## Job Management Functions

The Fax Service Client API job management functions provide a fax client application with the ability to query and manage queued and active fax jobs.



| Topic                                          | Contents                                                                                                                                                                                                                                                                                                       |
|------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**FaxAbort**](/windows/previous-versions/Winfax/nc-winfax-pfaxabort?branch=master)             | A fax client application calls the [**FaxAbort**](/windows/previous-versions/Winfax/nc-winfax-pfaxabort?branch=master) function to terminate a fax job.<br/>                                                                                                                                                                                              |
| [**FaxEnumJobs**](/windows/previous-versions/Winfax/nf-winfax-faxenumjobsa?branch=master)       | The [**FaxEnumJobs**](/windows/previous-versions/Winfax/nf-winfax-faxenumjobsa?branch=master) function enumerates all queued and active fax jobs on the fax server to which the client has connected. The function returns detailed information for each fax job to the fax client application.<br/>                                                      |
| [**FaxGetJob**](/windows/previous-versions/Winfax/nf-winfax-faxgetjoba?branch=master)           | A fax client application calls the [**FaxGetJob**](/windows/previous-versions/Winfax/nf-winfax-faxgetjoba?branch=master) function to retrieve detailed information for the specified queued or active fax job. The function returns the information in a [**FAX\_JOB\_ENTRY**](/windows/previous-versions/Winfax/ns-winfax-_fax_job_entrya?branch=master) structure.<br/>                               |
| [**FaxGetPageData**](/windows/previous-versions/Winfax/nc-winfax-pfaxgetpagedata?branch=master) | The [**FaxGetPageData**](/windows/previous-versions/Winfax/nc-winfax-pfaxgetpagedata?branch=master) function returns to a fax client application the first page of data for a fax job. The fax job must be an outbound job, but it can be queued or active. The function returns data in the Tagged Image File Format Class F (TIFF Class F) format.<br/> |
| [**FaxSetJob**](/windows/previous-versions/Winfax/nf-winfax-faxsetjoba?branch=master)           | A fax client application calls the [**FaxSetJob**](/windows/previous-versions/Winfax/nf-winfax-faxsetjoba?branch=master) function to pause, resume, cancel, or restart a specified fax job.<br/>                                                                                                                                                          |



 

## Fax Utility Functions

The Fax Service Client API utility functions deallocate resources and manipulate data structures. These functions are also useful during the installation of a fax service provider or fax routing extension DLL.



| Topic                                                                          | Contents                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|--------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**FaxAccessCheck**](/windows/previous-versions/Winfax/nc-winfax-pfaxaccesscheck?branch=master)                                 | A fax client application calls the [**FaxAccessCheck**](/windows/previous-versions/Winfax/nc-winfax-pfaxaccesscheck?branch=master) function to query the fax access privileges of a user.<br/>                                                                                                                                                                                                                                                                                                              |
| [**FaxCompleteJobParams**](/windows/previous-versions/Winfax/nf-winfax-faxcompletejobparamsa?branch=master)                     | The FaxCompleteJobParams function creates both a [**FAX\_COVERPAGE\_INFO**](/windows/previous-versions/Winfax/ns-winfax-_fax_coverpage_infoa?branch=master) structure and a [**FAX\_JOB\_PARAM**](/windows/previous-versions/Winfax/ns-winfax-_fax_job_parama?branch=master) structure for a fax client application. This utility function supplies multiple members of these structures with values for the size of the structure, the sender's name, and optional billing code information.<br/>                                                     |
| [**FaxFreeBuffer**](/windows/previous-versions/Winfax/nc-winfax-pfaxfreebuffer?branch=master)                                   | The [**FaxFreeBuffer**](/windows/previous-versions/Winfax/nc-winfax-pfaxfreebuffer?branch=master) function releases resources associated with a buffer allocated previously as the result of a function call by a fax client application. This includes calls to the [**FaxCompleteJobParams**](/windows/previous-versions/Winfax/nf-winfax-faxcompletejobparamsa?branch=master) function and to functions that begin with **FaxEnum** or **FaxGet**.<br/>                                                                                                   |
| [**FaxRegisterRoutingExtension**](/windows/previous-versions/Winfax/?branch=master)       | The [**FaxRegisterRoutingExtension**](/windows/previous-versions/Winfax/?branch=master) function registers a fax routing extension DLL with the fax service. The function configures the fax service registry to use the new routing extension DLL.<br/>                                                                                                                                                                                                              |
| [**FaxRegisterServiceProvider**](/windows/previous-versions/Winfax/?branch=master)         | The [**FaxRegisterServiceProvider**](/windows/previous-versions/Winfax/?branch=master) function registers a fax service provider DLL with the fax service. The function configures the fax service registry to query and use the new fax service provider DLL when the fax service restarts.<br/>                                                                                                                                                                      |
| [**FaxRoutingInstallationCallback**](/windows/previous-versions/Winfax/nc-winfax-pfax_routing_installation_callbackw?branch=master) | The [**FaxRoutingInstallationCallback**](/windows/previous-versions/Winfax/nc-winfax-pfax_routing_installation_callbackw?branch=master) function is a library-defined callback function that the [**FaxRegisterRoutingExtension**](/windows/previous-versions/Winfax/?branch=master) function calls to install a fax routing extension DLL. **FaxRegisterRoutingExtension** calls the **FaxRoutingInstallationCallback** function multiple times, once for each fax routing method the fax routing extension exports.<br/> |



 

## Fax Service Client Functions Alphabetic List

The Fax Service Client API includes the following functions, listed alphabetically.

-   [**FaxAbort**](/windows/previous-versions/Winfax/nc-winfax-pfaxabort?branch=master)
-   [**FaxAccessCheck**](/windows/previous-versions/Winfax/nc-winfax-pfaxaccesscheck?branch=master)
-   [**FaxClose**](/windows/previous-versions/Winfax/nc-winfax-pfaxclose?branch=master)
-   [**FaxCompleteJobParams**](/windows/previous-versions/Winfax/nf-winfax-faxcompletejobparamsa?branch=master)
-   [**FaxConnectFaxServer**](/windows/previous-versions/Winfax/nf-winfax-faxconnectfaxservera?branch=master)
-   [**FaxEnableRoutingMethod**](/windows/previous-versions/Winfax/nf-winfax-faxenableroutingmethoda?branch=master)
-   [**FaxEnumGlobalRoutingInfo**](/windows/previous-versions/Winfax/nf-winfax-faxenumglobalroutinginfoa?branch=master)
-   [**FaxEnumJobs**](/windows/previous-versions/Winfax/nf-winfax-faxenumjobsa?branch=master)
-   [**FaxEnumPorts**](/windows/previous-versions/Winfax/nf-winfax-faxenumportsa?branch=master)
-   [**FaxEnumRoutingMethods**](/windows/previous-versions/Winfax/nf-winfax-faxenumroutingmethodsa?branch=master)
-   [**FaxFreeBuffer**](/windows/previous-versions/Winfax/nc-winfax-pfaxfreebuffer?branch=master)
-   [**FaxGetConfiguration**](/windows/previous-versions/Winfax/nf-winfax-faxgetconfigurationa?branch=master)
-   [**FaxGetDeviceStatus**](/windows/previous-versions/Winfax/nf-winfax-faxgetdevicestatusa?branch=master)
-   [**FaxGetJob**](/windows/previous-versions/Winfax/nf-winfax-faxgetjoba?branch=master)
-   [**FaxGetLoggingCategories**](/windows/previous-versions/Winfax/nf-winfax-faxgetloggingcategoriesa?branch=master)
-   [**FaxGetPageData**](/windows/previous-versions/Winfax/nc-winfax-pfaxgetpagedata?branch=master)
-   [**FaxGetPort**](/windows/previous-versions/Winfax/nf-winfax-faxgetporta?branch=master)
-   [**FaxGetRoutingInfo**](/windows/previous-versions/Winfax/nf-winfax-faxgetroutinginfoa?branch=master)
-   [**FaxInitializeEventQueue**](/windows/previous-versions/Winfax/nc-winfax-pfaxinitializeeventqueue?branch=master)
-   [**FaxOpenPort**](/windows/previous-versions/Winfax/nc-winfax-pfaxopenport?branch=master)
-   [**FaxPrintCoverPage**](/windows/previous-versions/Winfax/nf-winfax-faxprintcoverpagea?branch=master)
-   [**FaxRegisterRoutingExtension**](/windows/previous-versions/Winfax/?branch=master)
-   [**FaxRegisterServiceProvider**](/windows/previous-versions/Winfax/?branch=master)
-   [**FaxSendDocument**](/windows/previous-versions/Winfax/nf-winfax-faxsenddocumenta?branch=master)
-   [**FaxSendDocumentForBroadcast**](/windows/previous-versions/Winfax/nf-winfax-faxsenddocumentforbroadcasta?branch=master)
-   [**FaxSetConfiguration**](/windows/previous-versions/Winfax/nf-winfax-faxsetconfigurationa?branch=master)
-   [**FaxSetGlobalRoutingInfo**](/windows/previous-versions/Winfax/nf-winfax-faxsetglobalroutinginfoa?branch=master)
-   [**FaxSetJob**](/windows/previous-versions/Winfax/nf-winfax-faxsetjoba?branch=master)
-   [**FaxSetLoggingCategories**](/windows/previous-versions/Winfax/nf-winfax-faxsetloggingcategoriesa?branch=master)
-   [**FaxSetPort**](/windows/previous-versions/Winfax/nf-winfax-faxsetporta?branch=master)
-   [**FaxSetRoutingInfo**](/windows/previous-versions/Winfax/nf-winfax-faxsetroutinginfoa?branch=master)
-   [**FaxStartPrintJob**](/windows/previous-versions/Winfax/nf-winfax-faxstartprintjoba?branch=master)

The Fax Service Client API includes the following callback functions.

-   [**FAX\_RECIPIENT\_CALLBACK**](/windows/previous-versions/Winfax/nc-winfax-pfax_recipient_callbacka?branch=master)
-   [**FaxRoutingInstallationCallback**](/windows/previous-versions/Winfax/nc-winfax-pfax_routing_installation_callbackw?branch=master)

 

 




