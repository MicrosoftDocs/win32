---
description: To obtain notification of invalidated logical networks, use the WSANSPIoctl function to register for network location change events.
ms.assetid: 531b6269-5f35-44c1-ad0f-c5f103029893
title: Querying NLA
ms.topic: article
ms.date: 05/31/2018
---

# Querying NLA

To obtain notification of invalidated logical networks, use the [**WSANSPIoctl**](/windows/desktop/api/Winsock2/nf-winsock2-wsanspioctl) function to register for network location change events. Two methods can be used to determine whether a previously valid network location has become invalid: polling methods, or notification using overlapped I/O or Windows messaging.

Queries are formed using the [**WSALookupServiceBegin**](/windows/desktop/api/Winsock2/nf-winsock2-wsalookupservicebegina), [**WSALookupServiceNext,**](/windows/desktop/api/Winsock2/nf-winsock2-wsalookupservicenexta) and [**WSALookupServiceEnd**](/windows/desktop/api/Winsock2/nf-winsock2-wsalookupserviceend) functions to enumerate all available logical networks. The use of each of these functions is explained individually throughout the remainder of this section, beginning with the **WSALookupServiceBegin** function.

> [!Note]  
> NLA requires the Mswsock.h header file, which by default is not included in the Winsock2.h file.

 

## Step 1: Initiate the Query

For quick reference, the [**WSALookupServiceBegin**](/windows/desktop/api/Winsock2/nf-winsock2-wsalookupservicebegina) function has the following syntax:

``` syntax
INT WSALookupServiceBegin(
  LPWSAQUERYSET lpqsRestrictions,
  DWORD dwControlFlags,
  LPHANDLE lphLookup
);
```

NLA supports the following *dwControlFlags* lookup flags:

<dl> LUP\_RETURN\_NAME  
LUP\_RETURN\_COMMENT  
LUP\_RETURN\_BLOB  
LUP\_RETURN\_ALL  
LUP\_DEEP  
</dl>

These flags restrict the result sets returned in subsequent calls to the [**WSALookupServiceNext**](/windows/desktop/api/Winsock2/nf-winsock2-wsalookupservicenexta), function to networks that contain fields of the specified type. For example, specifying LUP\_RETURN\_BLOB in the *dwControlFlags* parameter of the [**WSALookupServiceBegin**](/windows/desktop/api/Winsock2/nf-winsock2-wsalookupservicebegina) function call restricts result sets from subsequent calls to **WSALookupServiceNext**, to networks that contain BLOB information. Using the LUP\_RETURN\_ALL flag is equivalent to specifying LUP\_RETURN\_NAME, LUP\_RETURN\_COMMENT, and LUP\_RETURN\_BLOB, but not LUP\_DEEP.

For an explanation of these lookup flags, consult the [**WSALookupServiceBegin**](/windows/desktop/api/Winsock2/nf-winsock2-wsalookupservicebegina) function reference page.

The lookup handle returned by NLA in the *lphLookup* parameter is private to NLA, and should not be modified. Since the returned handle is private to NLA, functions such as [**WSAGetOverlappedResult**](/windows/desktop/api/Winsock2/nf-winsock2-wsagetoverlappedresult) are not available.

NLA returns zero upon successful completion, as defined in the [**WSALookupServiceBegin**](/windows/desktop/api/Winsock2/nf-winsock2-wsalookupservicebegina) function reference page. Otherwise, NLA supports the following error codes.

| Error                    | Meaning                                                                                                                                                     |
|--------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| WSANOTINITIALISED        | A successful call to the [**WSAStartup**](/windows/desktop/api/winsock/nf-winsock-wsastartup) function to initialize NLA was not performed.                                                   |
| WSAEINVAL                | One or more parameters were invalid, or parameters specified in the function call apply to protocols other than IP.                                         |
| WSASERVICE\_NOT\_FOUND   | The *lpServiceClassId* parameter of the [**WSAQUERYSET**](/windows/desktop/api/Winsock2/ns-winsock2-wsaquerysetw) structure passed in the *lpqsRestrictions* parameter contains an invalid GUID. |
| WSANO\_DATA              | The LUP\_CONTAINERS flag was specified in *dwControlFlags* parameter.                                                                                       |
| WSAEFAULT                | An access violation occurred when attempting to access user-supplied parameters.                                                                            |
| WSASYSNOTREADY           | The NLA service is unavailable to process the request.                                                                                                      |
| WSA\_NOT\_ENOUGH\_MEMORY | NLA or the NLA service was unable to allocate enough memory to process this request.                                                                        |



 

## Step 2: Perform the Query

The next step in querying NLA requires use of the [**WSALookupServiceNext**](/windows/desktop/api/Winsock2/nf-winsock2-wsalookupservicenexta) function. For quick reference, the **WSALookupServiceNext**, function has the following syntax:

``` syntax
INT WSALookupServiceNext(
  HANDLE hLookup,
  DWORD dwControlFlags,
  LPDWORD lpdwBufferLength,
  LPWSAQUERYSET lpqsResults
);
```

The *lLookup* parameter is the lookup handle returned from the previous call to the [**WSALookupServiceBegin**](/windows/desktop/api/Winsock2/nf-winsock2-wsalookupservicebegina) function.

The *dwControlFlags* parameter supports the following flags:

<dl> LUP\_RETURN\_NAME  
LUP\_RETURN\_COMMENT  
LUP\_RETURN\_BLOB  
LUP\_RETURN\_ALL  
LUP\_FLUSHPREVIOUS  
</dl>

These flags are independent of the flags supported in the [**WSALookupServiceBegin**](/windows/desktop/api/Winsock2/nf-winsock2-wsalookupservicebegina) function call. Note that any constraints specified in the previous call to the **WSALookupServiceBegin** function constrain the lookup; adding flags with the [**WSALookupServiceNext**](/windows/desktop/api/Winsock2/nf-winsock2-wsalookupservicenexta) function in an attempt to broaden the query beyond the constraints specified in the **WSALookupServiceBegin** call are silently ignored. Specifying a more restrictive set of flags than that specified in the **WSALookupServiceBegin** call, however, is allowed.

If the network detailed in *lpqsResults* is an active network, a series of **NLA\_BLOB** structures is appended as specified in the **lpBlob** member of the [**WSAQUERYSET**](/windows/desktop/api/Winsock2/ns-winsock2-wsaquerysetw) structure returned in *lpqsResults*. These **NLA\_BLOB** structures may be chained, and can be enumerated by traversing the list while NLA\_BLOB.header.nextOffset is nonzero. To obtain results for all network location information, continue calling the [**WSALookupServiceNext**](/windows/desktop/api/Winsock2/nf-winsock2-wsalookupservicenexta), function until the WSA\_E\_NO\_MORE error is returned, as explained in the **WSALookupServiceNext**, reference page.

The [**WSALookupServiceNext**](/windows/desktop/api/Winsock2/nf-winsock2-wsalookupservicenexta) function is also used in conjunction with the [**WSANSPIoctl**](/windows/desktop/api/Winsock2/nf-winsock2-wsanspioctl) function to receive notification of network changes. See [Notification from NLA](notification-from-nla-2.md) for more information.

NLA returns zero upon successful completion. Clients of NLA should continue calling the [**WSALookupServiceNext**](/windows/desktop/api/Winsock2/nf-winsock2-wsalookupservicenexta), function until WSA\_E\_NO\_MORE is returned, indicating that all of the information about available networks has been returned.

Otherwise, calling the [**WSALookupServiceNext**](/windows/desktop/api/Winsock2/nf-winsock2-wsalookupservicenexta), function for NLA supports the following error codes.

| Error                    | Meaning                                                                                                                                                                                                                                                                                                                                                                                                     |
|--------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| WSANOTINITIALISED        | A successful call to the [**WSAStartup**](/windows/desktop/api/winsock/nf-winsock-wsastartup) function that initialized NLA was not performed.                                                                                                                                                                                                                                                                                                |
| WSA\_INVALID\_HANDLE     | The lookup handle provided in the *hLookup* parameter was not a valid NLA SP handle. Clients must first call the [**WSALookupServiceBegin**](/windows/desktop/api/Winsock2/nf-winsock2-wsalookupservicebegina) function and receive a valid NLA SP handle to obtain query results.                                                                                                                                                               |
| WSAESYSNOTREADY          | The NLA service is unavailable to process this request.                                                                                                                                                                                                                                                                                                                                                     |
| WSAEFAULT                | The buffer size specified in the *lpdwBufferLength* parameter was insufficient to hold the results pointed to by *lpqsResults*. The required buffer is specified in *lpdwBufferLength*; if the client cannot supply a sufficiently large buffer, the client can call the [**WSALookupServiceNext**](/windows/desktop/api/Winsock2/nf-winsock2-wsalookupservicenexta) function with *dwControlFlags* set to LUP\_FLUSHPREVIOUS to skip the entry. |
| WSA\_NOT\_ENOUGH\_MEMORY | NLA is unable to obtain network information from the NLA system service due to insufficient memory in the calling process.                                                                                                                                                                                                                                                                                  |
| WSA\_E\_NO\_MORE         | There are no additional networks to enumerate for the query.                                                                                                                                                                                                                                                                                                                                                |



 

## Step 3: Terminate the Query

When all queries to NLA are complete and an application no longer requires use of NLA, a call to the [**WSALookupServiceEnd**](/windows/desktop/api/Winsock2/nf-winsock2-wsalookupserviceend) function should be made. Do not call **WSALookupServiceEnd** if the application will receive change notification based on the submitted query. See [Notification from NLA](notification-from-nla-2.md) for more information on receiving notification. Like most Windows Sockets service providers, NLA maintains a reference count for its clients. Calling the **WSALookupServiceEnd** function when queries to NLA are completed enables system resources no longer required by NLA to be freed.

NLA supports the following error codes for [**WSALookupServiceEnd**](/windows/desktop/api/Winsock2/nf-winsock2-wsalookupserviceend) function calls.

| Error                | Meaning                                                                                                   |
|----------------------|-----------------------------------------------------------------------------------------------------------|
| WSANOTINITIALISED    | A successful call to the [**WSAStartup**](/windows/desktop/api/winsock/nf-winsock-wsastartup) function to initialize NLA was not performed. |
| WSA\_INVALID\_HANDLE | The handle provided in the *hLookup* parameter was not a valid NLA SP handle.                             |



 

 

 



