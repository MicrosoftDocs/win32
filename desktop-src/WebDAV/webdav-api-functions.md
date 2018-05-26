---
title: WebDAV API Functions
description: The following functions are used in the WebDAV API.
ms.assetid: 489cdc17-aca8-4621-bc61-f0f3b9ac22b0
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# WebDAV API Functions

The following functions are used in the WebDAV API.



| Function                                                             | Description                                                                                                                                                                                                                           |
|----------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**DavAddConnection**](/windows/win32/davclnt/nf-davclnt-davaddconnection?branch=master)                         | Creates a secure connection to a WebDAV server or to a remote file or directory on a WebDAV server.                                                                                                                                   |
| [*DavAuthCallback*](/windows/win32/Davclnt/nc-davclnt-pfndavauthcallback?branch=master)                                | The WebDAV client calls the application-defined [*DavAuthCallback*](/windows/win32/Davclnt/nc-davclnt-pfndavauthcallback?branch=master) callback function to prompt the user for credentials.                                                                                           |
| [**DavCancelConnectionsToServer**](/windows/win32/davclnt/nf-davclnt-davcancelconnectionstoserver?branch=master) | Closes all connections to a WebDAV server or to a remote file or directory on a WebDAV server.                                                                                                                                        |
| [**DavDeleteConnection**](/windows/win32/davclnt/nf-davclnt-davdeleteconnection?branch=master)                   | Closes a connection that was created by using the [**DavAddConnection**](/windows/win32/davclnt/nf-davclnt-davaddconnection?branch=master) function.                                                                                                                              |
| [**DavFlushFile**](/windows/win32/davclnt/nf-davclnt-davflushfile?branch=master)                                 | Flushes the data from the local version of a remote file to the WebDAV server.                                                                                                                                                        |
| [*DavFreeCredCallback*](/windows/win32/Davclnt/nc-davclnt-pfndavauthcallback_freecred?branch=master)                        | The WebDAV client calls the application-defined [*DavFreeCredCallback*](/windows/win32/Davclnt/nc-davclnt-pfndavauthcallback_freecred?branch=master) callback function to free the credential information that was retrieved by the [*DavAuthCallback*](/windows/win32/Davclnt/nc-davclnt-pfndavauthcallback?branch=master) callback function. |
| [**DavGetExtendedError**](/windows/win32/davclnt/nf-davclnt-davgetextendederror?branch=master)                   | Retrieves the extended error code information that the WebDAV server returned for the previous failed I/O operation.                                                                                                                  |
| [**DavGetHTTPFromUNCPath**](/windows/win32/davclnt/nf-davclnt-davgethttpfromuncpath?branch=master)               | Converts the specified UNC path to an equivalent HTTP path.                                                                                                                                                                           |
| [**DavGetTheLockOwnerOfTheFile**](/windows/win32/davclnt/nf-davclnt-davgetthelockownerofthefile?branch=master)   | Returns the file lock owner for a file that is locked on a WebDAV server.                                                                                                                                                             |
| [**DavGetUNCFromHTTPPath**](/windows/win32/davclnt/nf-davclnt-davgetuncfromhttppath?branch=master)               | Converts the specified HTTP path to an equivalent UNC path.                                                                                                                                                                           |
| [**DavInvalidateCache**](/windows/win32/davclnt/nf-davclnt-davinvalidatecache?branch=master)                     | Invalidates the contents of the local cache for a remote file on a WebDAV server.                                                                                                                                                     |
| [**DavRegisterAuthCallback**](/windows/win32/Davclnt/nf-davclnt-davregisterauthcallback?branch=master)           | Registers an application-defined callback function that the WebDAV client can use to prompt the user for credentials.                                                                                                                 |
| [**DavUnregisterAuthCallback**](/windows/win32/Davclnt/nf-davclnt-davunregisterauthcallback?branch=master)       | Unregisters a registered callback function that the WebDAV client uses to prompt the user for credentials.                                                                                                                            |



 

 

 




