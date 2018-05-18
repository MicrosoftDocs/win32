---
title: WebDAV API Functions
description: The following functions are used in the WebDAV API.
ms.assetid: '489cdc17-aca8-4621-bc61-f0f3b9ac22b0'
---

# WebDAV API Functions

The following functions are used in the WebDAV API.



| Function                                                             | Description                                                                                                                                                                                                                           |
|----------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**DavAddConnection**](davaddconnection.md)                         | Creates a secure connection to a WebDAV server or to a remote file or directory on a WebDAV server.                                                                                                                                   |
| [*DavAuthCallback*](authcallback.md)                                | The WebDAV client calls the application-defined [*DavAuthCallback*](authcallback.md) callback function to prompt the user for credentials.                                                                                           |
| [**DavCancelConnectionsToServer**](davcancelconnectionstoserver.md) | Closes all connections to a WebDAV server or to a remote file or directory on a WebDAV server.                                                                                                                                        |
| [**DavDeleteConnection**](davdeleteconnection.md)                   | Closes a connection that was created by using the [**DavAddConnection**](davaddconnection.md) function.                                                                                                                              |
| [**DavFlushFile**](davflushfile.md)                                 | Flushes the data from the local version of a remote file to the WebDAV server.                                                                                                                                                        |
| [*DavFreeCredCallback*](freecredcallback.md)                        | The WebDAV client calls the application-defined [*DavFreeCredCallback*](freecredcallback.md) callback function to free the credential information that was retrieved by the [*DavAuthCallback*](authcallback.md) callback function. |
| [**DavGetExtendedError**](davgetextendederror.md)                   | Retrieves the extended error code information that the WebDAV server returned for the previous failed I/O operation.                                                                                                                  |
| [**DavGetHTTPFromUNCPath**](davgethttpfromuncpath.md)               | Converts the specified UNC path to an equivalent HTTP path.                                                                                                                                                                           |
| [**DavGetTheLockOwnerOfTheFile**](davgetthelockownerofthefile.md)   | Returns the file lock owner for a file that is locked on a WebDAV server.                                                                                                                                                             |
| [**DavGetUNCFromHTTPPath**](davgetuncfromhttppath.md)               | Converts the specified HTTP path to an equivalent UNC path.                                                                                                                                                                           |
| [**DavInvalidateCache**](davinvalidatecache.md)                     | Invalidates the contents of the local cache for a remote file on a WebDAV server.                                                                                                                                                     |
| [**DavRegisterAuthCallback**](davregisterauthcallback.md)           | Registers an application-defined callback function that the WebDAV client can use to prompt the user for credentials.                                                                                                                 |
| [**DavUnregisterAuthCallback**](davunregisterauthcallback.md)       | Unregisters a registered callback function that the WebDAV client uses to prompt the user for credentials.                                                                                                                            |



 

 

 




