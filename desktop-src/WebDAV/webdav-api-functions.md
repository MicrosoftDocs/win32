---
title: WebDAV API Functions
description: The following functions are used in the WebDAV API.
ms.assetid: 489cdc17-aca8-4621-bc61-f0f3b9ac22b0
ms.topic: article
ms.date: 05/31/2018
---

# WebDAV API Functions

The following functions are used in the WebDAV API.



| Function                                                             | Description                                                                                                                                                                                                                           |
|----------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**DavAddConnection**](/windows/desktop/api/davclnt/nf-davclnt-davaddconnection)                         | Creates a secure connection to a WebDAV server or to a remote file or directory on a WebDAV server.                                                                                                                                   |
| [*DavAuthCallback*](/windows/desktop/api/Davclnt/nc-davclnt-pfndavauthcallback)                                | The WebDAV client calls the application-defined [*DavAuthCallback*](/windows/desktop/api/Davclnt/nc-davclnt-pfndavauthcallback) callback function to prompt the user for credentials.                                                                                           |
| [**DavCancelConnectionsToServer**](/windows/desktop/api/davclnt/nf-davclnt-davcancelconnectionstoserver) | Closes all connections to a WebDAV server or to a remote file or directory on a WebDAV server.                                                                                                                                        |
| [**DavDeleteConnection**](/windows/desktop/api/davclnt/nf-davclnt-davdeleteconnection)                   | Closes a connection that was created by using the [**DavAddConnection**](/windows/desktop/api/davclnt/nf-davclnt-davaddconnection) function.                                                                                                                              |
| [**DavFlushFile**](/windows/desktop/api/davclnt/nf-davclnt-davflushfile)                                 | Flushes the data from the local version of a remote file to the WebDAV server.                                                                                                                                                        |
| [*DavFreeCredCallback*](/windows/desktop/api/Davclnt/nc-davclnt-pfndavauthcallback_freecred)                        | The WebDAV client calls the application-defined [*DavFreeCredCallback*](/windows/desktop/api/Davclnt/nc-davclnt-pfndavauthcallback_freecred) callback function to free the credential information that was retrieved by the [*DavAuthCallback*](/windows/desktop/api/Davclnt/nc-davclnt-pfndavauthcallback) callback function. |
| [**DavGetExtendedError**](/windows/desktop/api/davclnt/nf-davclnt-davgetextendederror)                   | Retrieves the extended error code information that the WebDAV server returned for the previous failed I/O operation.                                                                                                                  |
| [**DavGetHTTPFromUNCPath**](/windows/desktop/api/davclnt/nf-davclnt-davgethttpfromuncpath)               | Converts the specified UNC path to an equivalent HTTP path.                                                                                                                                                                           |
| [**DavGetTheLockOwnerOfTheFile**](/windows/desktop/api/davclnt/nf-davclnt-davgetthelockownerofthefile)   | Returns the file lock owner for a file that is locked on a WebDAV server.                                                                                                                                                             |
| [**DavGetUNCFromHTTPPath**](/windows/desktop/api/davclnt/nf-davclnt-davgetuncfromhttppath)               | Converts the specified HTTP path to an equivalent UNC path.                                                                                                                                                                           |
| [**DavInvalidateCache**](/windows/desktop/api/davclnt/nf-davclnt-davinvalidatecache)                     | Invalidates the contents of the local cache for a remote file on a WebDAV server.                                                                                                                                                     |
| [**DavRegisterAuthCallback**](/windows/desktop/api/Davclnt/nf-davclnt-davregisterauthcallback)           | Registers an application-defined callback function that the WebDAV client can use to prompt the user for credentials.                                                                                                                 |
| [**DavUnregisterAuthCallback**](/windows/desktop/api/Davclnt/nf-davclnt-davunregisterauthcallback)       | Unregisters a registered callback function that the WebDAV client uses to prompt the user for credentials.                                                                                                                            |



 

 

 




