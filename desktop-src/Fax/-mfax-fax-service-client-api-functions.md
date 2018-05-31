---
Description: The functions used with the Fax Service Client API fall into the following functional groupings. An alphabetic list follows.
ms.assetid: b076b5ba-09af-4312-90c1-27abd0b859df
title: Fax Service Client API Functions
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
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
| [**FaxClose**](/previous-versions/windows/desktop/api/Winfax/nc-winfax-pfaxclose)                                 | The [**FaxClose**](/previous-versions/windows/desktop/api/Winfax/nc-winfax-pfaxclose) function closes the following types of fax handles:<br/>                                                                                                                                                                                                                                                                                              |
| [**FaxConnectFaxServer**](/previous-versions/windows/desktop/api/Winfax/nf-winfax-faxconnectfaxservera)           | The [**FaxConnectFaxServer**](/previous-versions/windows/desktop/api/Winfax/nf-winfax-faxconnectfaxservera) function connects a fax client application to the local fax server. The function returns a fax server handle that is required to call other fax client functions that facilitate job, device, configuration, and document management.<br/>                                                                                      |
| [**FaxEnumGlobalRoutingInfo**](/previous-versions/windows/desktop/api/Winfax/nf-winfax-faxenumglobalroutinginfoa) | The [**FaxEnumGlobalRoutingInfo**](/previous-versions/windows/desktop/api/Winfax/nf-winfax-faxenumglobalroutinginfoa) function enumerates all fax routing methods associated with a specific fax server. The function returns to the fax client application fax routing method information that applies globally to the server, such as routing priority.<br/>                                                                              |
| [**FaxGetConfiguration**](/previous-versions/windows/desktop/api/Winfax/nf-winfax-faxgetconfigurationa)           | The [**FaxGetConfiguration**](/previous-versions/windows/desktop/api/Winfax/nf-winfax-faxgetconfigurationa) function returns to a fax client application the global configuration settings for the fax server to which the client has connected. The data includes, among other items, retransmission, branding, archive and cover page settings; discount rate periods; and the status of the fax server queue.<br/>                       |
| [**FaxGetLoggingCategories**](/previous-versions/windows/desktop/api/Winfax/nf-winfax-faxgetloggingcategoriesa)   | The [**FaxGetLoggingCategories**](/previous-versions/windows/desktop/api/Winfax/nf-winfax-faxgetloggingcategoriesa) function returns to a fax client application the current logging categories for the fax server to which the client has connected. A logging category determines the errors or other events the fax server records in the application event log.<br/>                                                                    |
| [**FaxInitializeEventQueue**](/previous-versions/windows/desktop/api/Winfax/nc-winfax-pfaxinitializeeventqueue)   | The [**FaxInitializeEventQueue**](/previous-versions/windows/desktop/api/Winfax/nc-winfax-pfaxinitializeeventqueue) function creates a fax event queue for the calling fax client application. The queue enables the application to receive notifications of asynchronous events from the fax server.<br/>                                                                                                                                  |
| [**FaxSetConfiguration**](/previous-versions/windows/desktop/api/Winfax/nf-winfax-faxsetconfigurationa)           | A fax client application calls the [**FaxSetConfiguration**](/previous-versions/windows/desktop/api/Winfax/nf-winfax-faxsetconfigurationa) function to change the global configuration settings for the fax server to which the client has connected. The configuration data can include, among other items, retransmission, branding, archive and cover page settings; discount rate periods; and the status of the fax server queue.<br/> |
| [**FaxSetGlobalRoutingInfo**](/previous-versions/windows/desktop/api/Winfax/nf-winfax-faxsetglobalroutinginfoa)   | A fax management application calls the [**FaxSetGlobalRoutingInfo**](/previous-versions/windows/desktop/api/Winfax/nf-winfax-faxsetglobalroutinginfoa) function to modify fax routing method data, such as routing priority, that applies globally to the fax server.<br/>                                                                                                                                                                  |
| [**FaxSetLoggingCategories**](/previous-versions/windows/desktop/api/Winfax/nf-winfax-faxsetloggingcategoriesa)   | A fax client application calls the [**FaxSetLoggingCategories**](/previous-versions/windows/desktop/api/Winfax/nf-winfax-faxsetloggingcategoriesa) function to modify the current logging categories for the fax server to which the client has connected. A logging category determines the errors or other events the fax server records in the application event log.<br/>                                                               |



 

## Device Management Functions

The Fax Service Client API device management functions enable a fax administration application to query and administer the configuration of a fax port. These functions also provide access to information about the fax routing methods associated with the port.



| Topic                                                          | Contents                                                                                                                                                                                                                                                                                                                           |
|----------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**FaxEnableRoutingMethod**](/previous-versions/windows/desktop/api/Winfax/nf-winfax-faxenableroutingmethoda) | The [**FaxEnableRoutingMethod**](/previous-versions/windows/desktop/api/Winfax/nf-winfax-faxenableroutingmethoda) function enables or disables a fax routing method for a specific fax device. A fax administration application typically calls this function for device management.<br/>                                                                                   |
| [**FaxEnumPorts**](/previous-versions/windows/desktop/api/Winfax/nf-winfax-faxenumportsa)                     | The [**FaxEnumPorts**](/previous-versions/windows/desktop/api/Winfax/nf-winfax-faxenumportsa) function enumerates all fax devices currently attached to the fax server to which the client has connected. The function returns detailed information for each fax port to the fax client application.<br/>                                                                   |
| [**FaxEnumRoutingMethods**](/previous-versions/windows/desktop/api/Winfax/nf-winfax-faxenumroutingmethodsa)   | The [**FaxEnumRoutingMethods**](/previous-versions/windows/desktop/api/Winfax/nf-winfax-faxenumroutingmethodsa) function enumerates all fax routing methods for a specific fax device. The function returns information about each routing method to a fax client application.<br/>                                                                                         |
| [**FaxGetDeviceStatus**](/previous-versions/windows/desktop/api/Winfax/nf-winfax-faxgetdevicestatusa)         | The [**FaxGetDeviceStatus**](/previous-versions/windows/desktop/api/Winfax/nf-winfax-faxgetdevicestatusa) function returns to a fax client application current status information for the fax device of interest. The returned data includes, among other items, device and station identifiers, sender and recipient names, and routing information.<br/>                  |
| [**FaxGetPort**](/previous-versions/windows/desktop/api/Winfax/nf-winfax-faxgetporta)                         | The [**FaxGetPort**](/previous-versions/windows/desktop/api/Winfax/nf-winfax-faxgetporta) function returns information for a specified fax port to a fax client application. The data includes, among other items, the permanent line identifier, the current status and capability of the port, and the transmitting and called station identifiers. <br/>                 |
| [**FaxGetRoutingInfo**](/previous-versions/windows/desktop/api/Winfax/nf-winfax-faxgetroutinginfoa)           | The [**FaxGetRoutingInfo**](/previous-versions/windows/desktop/api/Winfax/nf-winfax-faxgetroutinginfoa) function returns to a fax client application routing information for a fax routing method that is associated with a specific fax device.<br/>                                                                                                                       |
| [**FaxOpenPort**](/previous-versions/windows/desktop/api/Winfax/nc-winfax-pfaxopenport)                       | The [**FaxOpenPort**](/previous-versions/windows/desktop/api/Winfax/nc-winfax-pfaxopenport) function returns a fax port handle to a fax client application. The port handle is required when the application calls other fax client functions that facilitate device management and fax document routing.<br/>                                                              |
| [**FaxSetPort**](/previous-versions/windows/desktop/api/Winfax/nf-winfax-faxsetporta)                         | A fax client application calls the [**FaxSetPort**](/previous-versions/windows/desktop/api/Winfax/nf-winfax-faxsetporta) function to change the configuration of the fax port of interest. The configuration data can include, among other items, the capability of the port, its priority, rings before answer, and the transmitting and called station identifiers..<br/> |
| [**FaxSetRoutingInfo**](/previous-versions/windows/desktop/api/Winfax/nf-winfax-faxsetroutinginfoa)           | A fax management application calls the [**FaxSetRoutingInfo**](/previous-versions/windows/desktop/api/Winfax/nf-winfax-faxsetroutinginfoa) function to modify the routing information for a fax routing method that is associated with a specific fax device.<br/>                                                                                                          |



 

## Document Management Functions

The Fax Service Client API document management functions enable a fax client application to queue outgoing fax jobs and print fax transmissions. These functions also provide the ability to specify a cover page template file and user information to render onto the template at transmission time.



| Topic                                                                    | Contents                                                                                                                                                                                                                                                                                                             |
|--------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**FAX\_RECIPIENT\_CALLBACK**](/previous-versions/windows/desktop/api/Winfax/nc-winfax-pfax_recipient_callbacka)         | The [**FAX\_RECIPIENT\_CALLBACK**](/previous-versions/windows/desktop/api/Winfax/nc-winfax-pfax_recipient_callbacka) function is an application-defined or library-defined callback function that the [**FaxSendDocumentForBroadcast**](/previous-versions/windows/desktop/api/Winfax/nf-winfax-faxsenddocumentforbroadcasta) function calls to retrieve user-specific information for the transmission.<br/> |
| [**FaxPrintCoverPage**](/previous-versions/windows/desktop/api/Winfax/nf-winfax-faxprintcoverpagea)                     | The [**FaxPrintCoverPage**](/previous-versions/windows/desktop/api/Winfax/nf-winfax-faxprintcoverpagea) function prints a fax transmission cover page to the specified device context for a fax client application.<br/>                                                                                                                                      |
| [**FaxSendDocument**](/previous-versions/windows/desktop/api/Winfax/nf-winfax-faxsenddocumenta)                         | A fax client application calls the [**FaxSendDocument**](/previous-versions/windows/desktop/api/Winfax/nf-winfax-faxsenddocumenta) function to queue a fax job that will transmit an outgoing fax transmission.<br/>                                                                                                                                          |
| [**FaxSendDocumentForBroadcast**](/previous-versions/windows/desktop/api/Winfax/nf-winfax-faxsenddocumentforbroadcasta) | A fax client application calls the [**FaxSendDocumentForBroadcast**](/previous-versions/windows/desktop/api/Winfax/nf-winfax-faxsenddocumentforbroadcasta) function to queue several fax jobs that will transmit the same outgoing fax transmission to several recipients.<br/>                                                                               |
| [**FaxStartPrintJob**](/previous-versions/windows/desktop/api/Winfax/nf-winfax-faxstartprintjoba)                       | A fax client application calls the [**FaxStartPrintJob**](/previous-versions/windows/desktop/api/Winfax/nf-winfax-faxstartprintjoba) function to start printing an outbound fax transmission on the specified fax printer.<br/>                                                                                                                               |



 

## Job Management Functions

The Fax Service Client API job management functions provide a fax client application with the ability to query and manage queued and active fax jobs.



| Topic                                          | Contents                                                                                                                                                                                                                                                                                                       |
|------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**FaxAbort**](/previous-versions/windows/desktop/api/Winfax/nc-winfax-pfaxabort)             | A fax client application calls the [**FaxAbort**](/previous-versions/windows/desktop/api/Winfax/nc-winfax-pfaxabort) function to terminate a fax job.<br/>                                                                                                                                                                                              |
| [**FaxEnumJobs**](/previous-versions/windows/desktop/api/Winfax/nf-winfax-faxenumjobsa)       | The [**FaxEnumJobs**](/previous-versions/windows/desktop/api/Winfax/nf-winfax-faxenumjobsa) function enumerates all queued and active fax jobs on the fax server to which the client has connected. The function returns detailed information for each fax job to the fax client application.<br/>                                                      |
| [**FaxGetJob**](/previous-versions/windows/desktop/api/Winfax/nf-winfax-faxgetjoba)           | A fax client application calls the [**FaxGetJob**](/previous-versions/windows/desktop/api/Winfax/nf-winfax-faxgetjoba) function to retrieve detailed information for the specified queued or active fax job. The function returns the information in a [**FAX\_JOB\_ENTRY**](/previous-versions/windows/desktop/api/Winfax/ns-winfax-_fax_job_entrya) structure.<br/>                               |
| [**FaxGetPageData**](/previous-versions/windows/desktop/api/Winfax/nc-winfax-pfaxgetpagedata) | The [**FaxGetPageData**](/previous-versions/windows/desktop/api/Winfax/nc-winfax-pfaxgetpagedata) function returns to a fax client application the first page of data for a fax job. The fax job must be an outbound job, but it can be queued or active. The function returns data in the Tagged Image File Format Class F (TIFF Class F) format.<br/> |
| [**FaxSetJob**](/previous-versions/windows/desktop/api/Winfax/nf-winfax-faxsetjoba)           | A fax client application calls the [**FaxSetJob**](/previous-versions/windows/desktop/api/Winfax/nf-winfax-faxsetjoba) function to pause, resume, cancel, or restart a specified fax job.<br/>                                                                                                                                                          |



 

## Fax Utility Functions

The Fax Service Client API utility functions deallocate resources and manipulate data structures. These functions are also useful during the installation of a fax service provider or fax routing extension DLL.



| Topic                                                                          | Contents                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|--------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**FaxAccessCheck**](/previous-versions/windows/desktop/api/Winfax/nc-winfax-pfaxaccesscheck)                                 | A fax client application calls the [**FaxAccessCheck**](/previous-versions/windows/desktop/api/Winfax/nc-winfax-pfaxaccesscheck) function to query the fax access privileges of a user.<br/>                                                                                                                                                                                                                                                                                                              |
| [**FaxCompleteJobParams**](/previous-versions/windows/desktop/api/Winfax/nf-winfax-faxcompletejobparamsa)                     | The FaxCompleteJobParams function creates both a [**FAX\_COVERPAGE\_INFO**](/previous-versions/windows/desktop/api/Winfax/ns-winfax-_fax_coverpage_infoa) structure and a [**FAX\_JOB\_PARAM**](/previous-versions/windows/desktop/api/Winfax/ns-winfax-_fax_job_parama) structure for a fax client application. This utility function supplies multiple members of these structures with values for the size of the structure, the sender's name, and optional billing code information.<br/>                                                     |
| [**FaxFreeBuffer**](/previous-versions/windows/desktop/api/Winfax/nc-winfax-pfaxfreebuffer)                                   | The [**FaxFreeBuffer**](/previous-versions/windows/desktop/api/Winfax/nc-winfax-pfaxfreebuffer) function releases resources associated with a buffer allocated previously as the result of a function call by a fax client application. This includes calls to the [**FaxCompleteJobParams**](/previous-versions/windows/desktop/api/Winfax/nf-winfax-faxcompletejobparamsa) function and to functions that begin with **FaxEnum** or **FaxGet**.<br/>                                                                                                   |
| [**FaxRegisterRoutingExtension**](/previous-versions/windows/desktop/api/Winfax/)       | The [**FaxRegisterRoutingExtension**](/previous-versions/windows/desktop/api/Winfax/) function registers a fax routing extension DLL with the fax service. The function configures the fax service registry to use the new routing extension DLL.<br/>                                                                                                                                                                                                              |
| [**FaxRegisterServiceProvider**](/previous-versions/windows/desktop/api/Winfax/)         | The [**FaxRegisterServiceProvider**](/previous-versions/windows/desktop/api/Winfax/) function registers a fax service provider DLL with the fax service. The function configures the fax service registry to query and use the new fax service provider DLL when the fax service restarts.<br/>                                                                                                                                                                      |
| [**FaxRoutingInstallationCallback**](/previous-versions/windows/desktop/api/Winfax/nc-winfax-pfax_routing_installation_callbackw) | The [**FaxRoutingInstallationCallback**](/previous-versions/windows/desktop/api/Winfax/nc-winfax-pfax_routing_installation_callbackw) function is a library-defined callback function that the [**FaxRegisterRoutingExtension**](/previous-versions/windows/desktop/api/Winfax/) function calls to install a fax routing extension DLL. **FaxRegisterRoutingExtension** calls the **FaxRoutingInstallationCallback** function multiple times, once for each fax routing method the fax routing extension exports.<br/> |



 

## Fax Service Client Functions Alphabetic List

The Fax Service Client API includes the following functions, listed alphabetically.

-   [**FaxAbort**](/previous-versions/windows/desktop/api/Winfax/nc-winfax-pfaxabort)
-   [**FaxAccessCheck**](/previous-versions/windows/desktop/api/Winfax/nc-winfax-pfaxaccesscheck)
-   [**FaxClose**](/previous-versions/windows/desktop/api/Winfax/nc-winfax-pfaxclose)
-   [**FaxCompleteJobParams**](/previous-versions/windows/desktop/api/Winfax/nf-winfax-faxcompletejobparamsa)
-   [**FaxConnectFaxServer**](/previous-versions/windows/desktop/api/Winfax/nf-winfax-faxconnectfaxservera)
-   [**FaxEnableRoutingMethod**](/previous-versions/windows/desktop/api/Winfax/nf-winfax-faxenableroutingmethoda)
-   [**FaxEnumGlobalRoutingInfo**](/previous-versions/windows/desktop/api/Winfax/nf-winfax-faxenumglobalroutinginfoa)
-   [**FaxEnumJobs**](/previous-versions/windows/desktop/api/Winfax/nf-winfax-faxenumjobsa)
-   [**FaxEnumPorts**](/previous-versions/windows/desktop/api/Winfax/nf-winfax-faxenumportsa)
-   [**FaxEnumRoutingMethods**](/previous-versions/windows/desktop/api/Winfax/nf-winfax-faxenumroutingmethodsa)
-   [**FaxFreeBuffer**](/previous-versions/windows/desktop/api/Winfax/nc-winfax-pfaxfreebuffer)
-   [**FaxGetConfiguration**](/previous-versions/windows/desktop/api/Winfax/nf-winfax-faxgetconfigurationa)
-   [**FaxGetDeviceStatus**](/previous-versions/windows/desktop/api/Winfax/nf-winfax-faxgetdevicestatusa)
-   [**FaxGetJob**](/previous-versions/windows/desktop/api/Winfax/nf-winfax-faxgetjoba)
-   [**FaxGetLoggingCategories**](/previous-versions/windows/desktop/api/Winfax/nf-winfax-faxgetloggingcategoriesa)
-   [**FaxGetPageData**](/previous-versions/windows/desktop/api/Winfax/nc-winfax-pfaxgetpagedata)
-   [**FaxGetPort**](/previous-versions/windows/desktop/api/Winfax/nf-winfax-faxgetporta)
-   [**FaxGetRoutingInfo**](/previous-versions/windows/desktop/api/Winfax/nf-winfax-faxgetroutinginfoa)
-   [**FaxInitializeEventQueue**](/previous-versions/windows/desktop/api/Winfax/nc-winfax-pfaxinitializeeventqueue)
-   [**FaxOpenPort**](/previous-versions/windows/desktop/api/Winfax/nc-winfax-pfaxopenport)
-   [**FaxPrintCoverPage**](/previous-versions/windows/desktop/api/Winfax/nf-winfax-faxprintcoverpagea)
-   [**FaxRegisterRoutingExtension**](/previous-versions/windows/desktop/api/Winfax/)
-   [**FaxRegisterServiceProvider**](/previous-versions/windows/desktop/api/Winfax/)
-   [**FaxSendDocument**](/previous-versions/windows/desktop/api/Winfax/nf-winfax-faxsenddocumenta)
-   [**FaxSendDocumentForBroadcast**](/previous-versions/windows/desktop/api/Winfax/nf-winfax-faxsenddocumentforbroadcasta)
-   [**FaxSetConfiguration**](/previous-versions/windows/desktop/api/Winfax/nf-winfax-faxsetconfigurationa)
-   [**FaxSetGlobalRoutingInfo**](/previous-versions/windows/desktop/api/Winfax/nf-winfax-faxsetglobalroutinginfoa)
-   [**FaxSetJob**](/previous-versions/windows/desktop/api/Winfax/nf-winfax-faxsetjoba)
-   [**FaxSetLoggingCategories**](/previous-versions/windows/desktop/api/Winfax/nf-winfax-faxsetloggingcategoriesa)
-   [**FaxSetPort**](/previous-versions/windows/desktop/api/Winfax/nf-winfax-faxsetporta)
-   [**FaxSetRoutingInfo**](/previous-versions/windows/desktop/api/Winfax/nf-winfax-faxsetroutinginfoa)
-   [**FaxStartPrintJob**](/previous-versions/windows/desktop/api/Winfax/nf-winfax-faxstartprintjoba)

The Fax Service Client API includes the following callback functions.

-   [**FAX\_RECIPIENT\_CALLBACK**](/previous-versions/windows/desktop/api/Winfax/nc-winfax-pfax_recipient_callbacka)
-   [**FaxRoutingInstallationCallback**](/previous-versions/windows/desktop/api/Winfax/nc-winfax-pfax_routing_installation_callbackw)

 

 




