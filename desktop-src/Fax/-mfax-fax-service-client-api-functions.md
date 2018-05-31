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
| [**FaxClose**](-mfax-faxclose.md)                                 | The [**FaxClose**](-mfax-faxclose.md) function closes the following types of fax handles:<br/>                                                                                                                                                                                                                                                                                              |
| [**FaxConnectFaxServer**](-mfax-faxconnectfaxserver.md)           | The [**FaxConnectFaxServer**](-mfax-faxconnectfaxserver.md) function connects a fax client application to the local fax server. The function returns a fax server handle that is required to call other fax client functions that facilitate job, device, configuration, and document management.<br/>                                                                                      |
| [**FaxEnumGlobalRoutingInfo**](-mfax-faxenumglobalroutinginfo.md) | The [**FaxEnumGlobalRoutingInfo**](-mfax-faxenumglobalroutinginfo.md) function enumerates all fax routing methods associated with a specific fax server. The function returns to the fax client application fax routing method information that applies globally to the server, such as routing priority.<br/>                                                                              |
| [**FaxGetConfiguration**](-mfax-faxgetconfiguration.md)           | The [**FaxGetConfiguration**](-mfax-faxgetconfiguration.md) function returns to a fax client application the global configuration settings for the fax server to which the client has connected. The data includes, among other items, retransmission, branding, archive and cover page settings; discount rate periods; and the status of the fax server queue.<br/>                       |
| [**FaxGetLoggingCategories**](-mfax-faxgetloggingcategories.md)   | The [**FaxGetLoggingCategories**](-mfax-faxgetloggingcategories.md) function returns to a fax client application the current logging categories for the fax server to which the client has connected. A logging category determines the errors or other events the fax server records in the application event log.<br/>                                                                    |
| [**FaxInitializeEventQueue**](-mfax-faxinitializeeventqueue.md)   | The [**FaxInitializeEventQueue**](-mfax-faxinitializeeventqueue.md) function creates a fax event queue for the calling fax client application. The queue enables the application to receive notifications of asynchronous events from the fax server.<br/>                                                                                                                                  |
| [**FaxSetConfiguration**](-mfax-faxsetconfiguration.md)           | A fax client application calls the [**FaxSetConfiguration**](-mfax-faxsetconfiguration.md) function to change the global configuration settings for the fax server to which the client has connected. The configuration data can include, among other items, retransmission, branding, archive and cover page settings; discount rate periods; and the status of the fax server queue.<br/> |
| [**FaxSetGlobalRoutingInfo**](-mfax-faxsetglobalroutinginfo.md)   | A fax management application calls the [**FaxSetGlobalRoutingInfo**](-mfax-faxsetglobalroutinginfo.md) function to modify fax routing method data, such as routing priority, that applies globally to the fax server.<br/>                                                                                                                                                                  |
| [**FaxSetLoggingCategories**](-mfax-faxsetloggingcategories.md)   | A fax client application calls the [**FaxSetLoggingCategories**](-mfax-faxsetloggingcategories.md) function to modify the current logging categories for the fax server to which the client has connected. A logging category determines the errors or other events the fax server records in the application event log.<br/>                                                               |



 

## Device Management Functions

The Fax Service Client API device management functions enable a fax administration application to query and administer the configuration of a fax port. These functions also provide access to information about the fax routing methods associated with the port.



| Topic                                                          | Contents                                                                                                                                                                                                                                                                                                                           |
|----------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**FaxEnableRoutingMethod**](-mfax-faxenableroutingmethod.md) | The [**FaxEnableRoutingMethod**](-mfax-faxenableroutingmethod.md) function enables or disables a fax routing method for a specific fax device. A fax administration application typically calls this function for device management.<br/>                                                                                   |
| [**FaxEnumPorts**](-mfax-faxenumports.md)                     | The [**FaxEnumPorts**](-mfax-faxenumports.md) function enumerates all fax devices currently attached to the fax server to which the client has connected. The function returns detailed information for each fax port to the fax client application.<br/>                                                                   |
| [**FaxEnumRoutingMethods**](-mfax-faxenumroutingmethods.md)   | The [**FaxEnumRoutingMethods**](-mfax-faxenumroutingmethods.md) function enumerates all fax routing methods for a specific fax device. The function returns information about each routing method to a fax client application.<br/>                                                                                         |
| [**FaxGetDeviceStatus**](-mfax-faxgetdevicestatus.md)         | The [**FaxGetDeviceStatus**](-mfax-faxgetdevicestatus.md) function returns to a fax client application current status information for the fax device of interest. The returned data includes, among other items, device and station identifiers, sender and recipient names, and routing information.<br/>                  |
| [**FaxGetPort**](-mfax-faxgetport.md)                         | The [**FaxGetPort**](-mfax-faxgetport.md) function returns information for a specified fax port to a fax client application. The data includes, among other items, the permanent line identifier, the current status and capability of the port, and the transmitting and called station identifiers. <br/>                 |
| [**FaxGetRoutingInfo**](-mfax-faxgetroutinginfo.md)           | The [**FaxGetRoutingInfo**](-mfax-faxgetroutinginfo.md) function returns to a fax client application routing information for a fax routing method that is associated with a specific fax device.<br/>                                                                                                                       |
| [**FaxOpenPort**](-mfax-faxopenport.md)                       | The [**FaxOpenPort**](-mfax-faxopenport.md) function returns a fax port handle to a fax client application. The port handle is required when the application calls other fax client functions that facilitate device management and fax document routing.<br/>                                                              |
| [**FaxSetPort**](-mfax-faxsetport.md)                         | A fax client application calls the [**FaxSetPort**](-mfax-faxsetport.md) function to change the configuration of the fax port of interest. The configuration data can include, among other items, the capability of the port, its priority, rings before answer, and the transmitting and called station identifiers..<br/> |
| [**FaxSetRoutingInfo**](-mfax-faxsetroutinginfo.md)           | A fax management application calls the [**FaxSetRoutingInfo**](-mfax-faxsetroutinginfo.md) function to modify the routing information for a fax routing method that is associated with a specific fax device.<br/>                                                                                                          |



 

## Document Management Functions

The Fax Service Client API document management functions enable a fax client application to queue outgoing fax jobs and print fax transmissions. These functions also provide the ability to specify a cover page template file and user information to render onto the template at transmission time.



| Topic                                                                    | Contents                                                                                                                                                                                                                                                                                                             |
|--------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**FAX\_RECIPIENT\_CALLBACK**](-mfax-fax-recipient-callback.md)         | The [**FAX\_RECIPIENT\_CALLBACK**](-mfax-fax-recipient-callback.md) function is an application-defined or library-defined callback function that the [**FaxSendDocumentForBroadcast**](-mfax-faxsenddocumentforbroadcast.md) function calls to retrieve user-specific information for the transmission.<br/> |
| [**FaxPrintCoverPage**](-mfax-faxprintcoverpage.md)                     | The [**FaxPrintCoverPage**](-mfax-faxprintcoverpage.md) function prints a fax transmission cover page to the specified device context for a fax client application.<br/>                                                                                                                                      |
| [**FaxSendDocument**](-mfax-faxsenddocument.md)                         | A fax client application calls the [**FaxSendDocument**](-mfax-faxsenddocument.md) function to queue a fax job that will transmit an outgoing fax transmission.<br/>                                                                                                                                          |
| [**FaxSendDocumentForBroadcast**](-mfax-faxsenddocumentforbroadcast.md) | A fax client application calls the [**FaxSendDocumentForBroadcast**](-mfax-faxsenddocumentforbroadcast.md) function to queue several fax jobs that will transmit the same outgoing fax transmission to several recipients.<br/>                                                                               |
| [**FaxStartPrintJob**](-mfax-faxstartprintjob.md)                       | A fax client application calls the [**FaxStartPrintJob**](-mfax-faxstartprintjob.md) function to start printing an outbound fax transmission on the specified fax printer.<br/>                                                                                                                               |



 

## Job Management Functions

The Fax Service Client API job management functions provide a fax client application with the ability to query and manage queued and active fax jobs.



| Topic                                          | Contents                                                                                                                                                                                                                                                                                                       |
|------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**FaxAbort**](-mfax-faxabort.md)             | A fax client application calls the [**FaxAbort**](-mfax-faxabort.md) function to terminate a fax job.<br/>                                                                                                                                                                                              |
| [**FaxEnumJobs**](-mfax-faxenumjobs.md)       | The [**FaxEnumJobs**](-mfax-faxenumjobs.md) function enumerates all queued and active fax jobs on the fax server to which the client has connected. The function returns detailed information for each fax job to the fax client application.<br/>                                                      |
| [**FaxGetJob**](-mfax-faxgetjob.md)           | A fax client application calls the [**FaxGetJob**](-mfax-faxgetjob.md) function to retrieve detailed information for the specified queued or active fax job. The function returns the information in a [**FAX\_JOB\_ENTRY**](-mfax-fax-job-entry-str.md) structure.<br/>                               |
| [**FaxGetPageData**](-mfax-faxgetpagedata.md) | The [**FaxGetPageData**](-mfax-faxgetpagedata.md) function returns to a fax client application the first page of data for a fax job. The fax job must be an outbound job, but it can be queued or active. The function returns data in the Tagged Image File Format Class F (TIFF Class F) format.<br/> |
| [**FaxSetJob**](-mfax-faxsetjob.md)           | A fax client application calls the [**FaxSetJob**](-mfax-faxsetjob.md) function to pause, resume, cancel, or restart a specified fax job.<br/>                                                                                                                                                          |



 

## Fax Utility Functions

The Fax Service Client API utility functions deallocate resources and manipulate data structures. These functions are also useful during the installation of a fax service provider or fax routing extension DLL.



| Topic                                                                          | Contents                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|--------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**FaxAccessCheck**](-mfax-faxaccesscheck.md)                                 | A fax client application calls the [**FaxAccessCheck**](-mfax-faxaccesscheck.md) function to query the fax access privileges of a user.<br/>                                                                                                                                                                                                                                                                                                              |
| [**FaxCompleteJobParams**](-mfax-faxcompletejobparams.md)                     | The FaxCompleteJobParams function creates both a [**FAX\_COVERPAGE\_INFO**](-mfax-fax-coverpage-info-str.md) structure and a [**FAX\_JOB\_PARAM**](-mfax-fax-job-param-str.md) structure for a fax client application. This utility function supplies multiple members of these structures with values for the size of the structure, the sender's name, and optional billing code information.<br/>                                                     |
| [**FaxFreeBuffer**](-mfax-faxfreebuffer.md)                                   | The [**FaxFreeBuffer**](-mfax-faxfreebuffer.md) function releases resources associated with a buffer allocated previously as the result of a function call by a fax client application. This includes calls to the [**FaxCompleteJobParams**](-mfax-faxcompletejobparams.md) function and to functions that begin with **FaxEnum** or **FaxGet**.<br/>                                                                                                   |
| [**FaxRegisterRoutingExtension**](-mfax-faxregisterroutingextension.md)       | The [**FaxRegisterRoutingExtension**](-mfax-faxregisterroutingextension.md) function registers a fax routing extension DLL with the fax service. The function configures the fax service registry to use the new routing extension DLL.<br/>                                                                                                                                                                                                              |
| [**FaxRegisterServiceProvider**](-mfax-faxregisterserviceprovider.md)         | The [**FaxRegisterServiceProvider**](-mfax-faxregisterserviceprovider.md) function registers a fax service provider DLL with the fax service. The function configures the fax service registry to query and use the new fax service provider DLL when the fax service restarts.<br/>                                                                                                                                                                      |
| [**FaxRoutingInstallationCallback**](-mfax-faxroutinginstallationcallback.md) | The [**FaxRoutingInstallationCallback**](-mfax-faxroutinginstallationcallback.md) function is a library-defined callback function that the [**FaxRegisterRoutingExtension**](-mfax-faxregisterroutingextension.md) function calls to install a fax routing extension DLL. **FaxRegisterRoutingExtension** calls the **FaxRoutingInstallationCallback** function multiple times, once for each fax routing method the fax routing extension exports.<br/> |



 

## Fax Service Client Functions Alphabetic List

The Fax Service Client API includes the following functions, listed alphabetically.

-   [**FaxAbort**](-mfax-faxabort.md)
-   [**FaxAccessCheck**](-mfax-faxaccesscheck.md)
-   [**FaxClose**](-mfax-faxclose.md)
-   [**FaxCompleteJobParams**](-mfax-faxcompletejobparams.md)
-   [**FaxConnectFaxServer**](-mfax-faxconnectfaxserver.md)
-   [**FaxEnableRoutingMethod**](-mfax-faxenableroutingmethod.md)
-   [**FaxEnumGlobalRoutingInfo**](-mfax-faxenumglobalroutinginfo.md)
-   [**FaxEnumJobs**](-mfax-faxenumjobs.md)
-   [**FaxEnumPorts**](-mfax-faxenumports.md)
-   [**FaxEnumRoutingMethods**](-mfax-faxenumroutingmethods.md)
-   [**FaxFreeBuffer**](-mfax-faxfreebuffer.md)
-   [**FaxGetConfiguration**](-mfax-faxgetconfiguration.md)
-   [**FaxGetDeviceStatus**](-mfax-faxgetdevicestatus.md)
-   [**FaxGetJob**](-mfax-faxgetjob.md)
-   [**FaxGetLoggingCategories**](-mfax-faxgetloggingcategories.md)
-   [**FaxGetPageData**](-mfax-faxgetpagedata.md)
-   [**FaxGetPort**](-mfax-faxgetport.md)
-   [**FaxGetRoutingInfo**](-mfax-faxgetroutinginfo.md)
-   [**FaxInitializeEventQueue**](-mfax-faxinitializeeventqueue.md)
-   [**FaxOpenPort**](-mfax-faxopenport.md)
-   [**FaxPrintCoverPage**](-mfax-faxprintcoverpage.md)
-   [**FaxRegisterRoutingExtension**](-mfax-faxregisterroutingextension.md)
-   [**FaxRegisterServiceProvider**](-mfax-faxregisterserviceprovider.md)
-   [**FaxSendDocument**](-mfax-faxsenddocument.md)
-   [**FaxSendDocumentForBroadcast**](-mfax-faxsenddocumentforbroadcast.md)
-   [**FaxSetConfiguration**](-mfax-faxsetconfiguration.md)
-   [**FaxSetGlobalRoutingInfo**](-mfax-faxsetglobalroutinginfo.md)
-   [**FaxSetJob**](-mfax-faxsetjob.md)
-   [**FaxSetLoggingCategories**](-mfax-faxsetloggingcategories.md)
-   [**FaxSetPort**](-mfax-faxsetport.md)
-   [**FaxSetRoutingInfo**](-mfax-faxsetroutinginfo.md)
-   [**FaxStartPrintJob**](-mfax-faxstartprintjob.md)

The Fax Service Client API includes the following callback functions.

-   [**FAX\_RECIPIENT\_CALLBACK**](-mfax-fax-recipient-callback.md)
-   [**FaxRoutingInstallationCallback**](-mfax-faxroutinginstallationcallback.md)

 

 




