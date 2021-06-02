---
description: This section contains a source code sample that demonstrates how to implement the GetXbyY functions using the new, protocol-independent RNR functions.
ms.assetid: d6246d47-11c2-4e4b-8a2b-17fd9cb041fc
title: Sample Code for a Service Provider
ms.topic: article
ms.date: 05/31/2018
---

# Sample Code for a Service Provider

This section contains a source code sample that demonstrates how to implement the **GetXbyY** functions using the new, protocol-independent RNR functions. A developer should implement these functions as a starting point. To comply with the Windows Sockets specification, many more functions are needed.

> [!IMPORTANT]
> The following code is not guaranteed to compile.

 


```C++
#define WIN32_LEAN_AND_MEAN

#include <windows.h>
#include <winsock2.h>
#include <Ws2tcpip.h>
#include <windns.h>
#include <svcguid.h>
#include <stdio.h>

// Link with ws2_32.lib
#pragma comment(lib, "Ws2_32.lib")

#undef WINSOCK_API_LINKAGE

#define WINSOCK_API_LINKAGE __control_entrypoint(DllExport)

/*++
    xbyrnr.cpp

    
    GetXbyY emulation via new WinSock2 RNR. This source module shows
    code that is built into the WinSock2 DLL (ws2_32.dll). It
    demonstrates how the older GetXByY functions are mapped to the new
    WSALookupServiceBegin, WSALookupServiceNext, WSALookupServiceEnd
    functions.

    This module is not guaranteed to compile. It is provided as source
    code for RNR namespace service providers to understand what will
    be coming down to their code in response to the traditional
    GetXbyY calls.

    At this time, only
        gethostname
        gethostbyname
        gethostbyaddr
        getservbyname
        getservbyport
    are implemented in this manner.

    
    Warning: This is not provided as a template for either RNR
    applications or namespace providers. This code is only intended
    to illustrate what happens in the WinSock2 DLL to map the GetXbyY
    calls to the new RNR APIs.
--*/

// The initial buffer size passed by getxbyy functions
// to WSALookupServiceNext. If it is insuffucient for the query,
// the amount specified by the provider is allocated and call is
// repeated.

// The initial buffer is allocated from stack, so we try to keep it
// relatively small, but still for performance reasons we want to be able
// to satisfy most of the calls with just this amount

#define RNR_BUFFER_SIZE (sizeof(WSAQUERYSET) + 256)

//
//  Forward declares
//

LPBLOB getxyDataEnt(
    PCHAR  *pResults,
    DWORD  dwSize,
    LPSTR  lpszName,
    LPGUID lpType,
    LPSTR *lppName
    );


VOID FixList(PCHAR ** List, PCHAR Base);

VOID UnpackHostEnt(struct hostent * hostent);

VOID UnpackServEnt(struct servent * servent);

GUID HostAddrByNameGuid = SVCID_INET_HOSTADDRBYNAME;
GUID HostNameGuid = SVCID_HOSTNAME;
GUID AddressGuid =  SVCID_INET_HOSTADDRBYINETSTRING;
GUID IANAGuid    =  SVCID_INET_SERVICEBYNAME;

//
// Utility to turn a list of offsets into a list of addresses. Used
// to convert structures returned as BLOBs.
//

VOID FixList(PCHAR ** List, PCHAR Base)
{
    if(*List)
    {
        PCHAR * Addr;

        Addr = *List = (PCHAR *)( ((DWORD)*List + Base) );
        while(*Addr)
        {
            *Addr = (PCHAR)(((DWORD)*Addr + Base));
            Addr++;
        }
    }
}


//
// Routine to convert a hostent returned in a BLOB to one with
// usable pointers. The structure is converted in-place.
//
VOID UnpackHostEnt(struct hostent * hostent)
{
     PCHAR pch;

     pch = (PCHAR)hostent;

     if(hostent->h_name)
     {
         hostent->h_name = (PCHAR)((DWORD)hostent->h_name + pch);
     }
     FixList(&hostent->h_aliases, pch);
     FixList(&hostent->h_addr_list, pch);
}

//
// Routine to unpack a servent returned in a BLOB to one with
// usable pointers. The structure is converted in-place
//

VOID UnpackServEnt(struct servent * servent)
{
    PCHAR pch;

    pch = (PCHAR)servent;

    FixList(&servent->s_aliases, pch);
    servent->s_name = (PCHAR)(DWORD(servent->s_name) + pch);
    servent->s_proto = (PCHAR)(DWORD(servent->s_proto) + pch);
}

WINSOCK_API_LINKAGE
struct hostent FAR *
WSAAPI
gethostbyaddr(
    IN const char *addr,
    IN int len,
    IN int type
    )
/*++
Routine Description:

    Get host information corresponding to an address.

Arguments:

    addr - A pointer to an address in network byte order.

    len - The length of the address, which must be 4 for PF_INET
    addresses.

    type - The type of the address, which must be PF_INET.

Returns:

    If no error occurs, gethostbyaddr() returns a pointer to the
    hostent structure described above. Otherwise it returns a NULL
    pointer and a specific error code is stored with SetErrorCode(). 
--*/
{
    CHAR qbuf[DNS_MAX_NAME_BUFFER_LENGTH];
    struct hostent *ph;
    LPBLOB pBlob;
    PCHAR pResults;
    CHAR localResults[RNR_BUFFER_SIZE];
    INT ErrorCode;
    PTHREAD Thread;

    ErrorCode = PROLOG(&Thread);
    if(ErrorCode != NO_ERROR)
    {
        SetLastError(ErrorCode);
        return(NULL);
    }

    if ( !addr )
    {
        SetLastError(WSAEINVAL);
        return(NULL);
    }
 
    pResults = localResults;

    //
    // NOTICE. Only handles current inet address forms. 
    //
    (void)sprintf_s(qbuf, sizeof(qbuf); "%u.%u.%u.%u",
            ((unsigned)addr[0] & 0xff),
            ((unsigned)addr[1] & 0xff),
            ((unsigned)addr[2] & 0xff),
            ((unsigned)addr[3] & 0xff));


    pBlob = getxyDataEnt(pResults,
                         RNR_BUFFER_SIZE,
                         qbuf,
                         &AddressGuid,
                         0);
    if(pBlob)
    {
        ph = (struct hostent *)Thread->CopyHostEnt(pBlob);
        if(ph)
        {
            UnpackHostEnt(ph);
        }
    }
    else
    {
        ph = 0;
        if(GetLastError() == WSASERVICE_NOT_FOUND)
        {
            SetLastError(WSANO_ADDRESS);
        }
    }
    if (pResults != localResults) 
        delete pResults;

    return(ph);
}  // gethostbyaddr


WINSOCK_API_LINKAGE
struct hostent* FAR WSAAPI 
gethostbyname(
    IN const char FAR * name
    )
/*++
Routine Description:

    Get host information corresponding to a hostname.

Arguments:

    name - A pointer to the null-terminated name of the host.

Returns:

    If no error occurs, gethostbyname() returns a pointer to the
    hostent structure described above. Otherwise it returns a null
    pointer and a specific errorr code is stored with SetErrorCode().
--*/
{
    struct hostent * hent;
    LPBLOB pBlob;
    PCHAR pResults;
    CHAR localResults[RNR_BUFFER_SIZE];
    INT ErrorCode;
    CHAR  szLocalName[200];   // for storing the local name. This
                              // is simply a big number assumed
                              // to be large enough. This is used
                              // only when the caller chooses not to
                              // provide a name.
    PCHAR pszName;

    PDTHREAD Thread;

    ErrorCode = PROLOG(&Thread);
    if(ErrorCode != NO_ERROR)
    {
        SetLastError(ErrorCode);
        return(NULL);
    }

    //
    // A NULL input name means look for the local name. So,
    // get it.
    //
    if(!name || !*name)
    {
        if(gethostname(szLocalName, 200) != NO_ERROR)
        {
            return(NULL);
        }
        pszName = szLocalName;
    }
    else
    {
        pszName = (PCHAR)name;
    }

    pResults = localResults;

    pBlob = getxyDataEnt( &pResults,
                          RNR_BUFFER_SIZE,
                          pszName,
                          &HostAddrByNameGuid,
                          0);
    if(pBlob &&
         ( !name || !*name ) )
    {
        pBlob = getxyDataEnt( &pResults,
                              RNR_BUFFER_SIZE,
                              NULL,
                              &HostAddrByNameGuid,
                              0);
    }
         
    if(pBlob )    {
        hent = (struct hostent *)Thread->CopyHostEnt(pBlob);
        if(hent)
        {
            UnpackHostEnt(hent);
        }
    }
    else
    {
        hent = 0;
        if(GetLastError() == WSASERVICE_NOT_FOUND)
        {
            SetLastError(WSAHOST_NOT_FOUND);
        }
    }

    if (pResults!=localResults)
        delete pResults;

    return(hent);
}  // gethostbyname

WINSOCK_API_LINKAGE
int WSAAPI 
gethostname(
    OUT char FAR * name,
    IN int namelen
    )
/*++
Routine Description:

    Return the standard host name for the local computer.

Arguments:

    name    - A pointer to a buffer that will receive the host name.

    namelen - The length of the buffer.

Returns:

    Zero on success else SOCKET_ERROR. The error code is stored with
    SetErrorCode(). 
--*/
{
    PCHAR lpName;
    PCHAR pResults;
    CHAR localResults[RNR_BUFFER_SIZE];
    INT ErrorCode;
    PDTHREAD Thread;

    ErrorCode = PROLOG(&Thread);
    if(ErrorCode != NO_ERROR)
    {
        gSetLastError(ErrorCode);
        return(NULL);
    }

    pResults = localResults;

    if(getxyDataEnt(pResults, 
                    RNR_BUFFER_SIZE, 
                    NULL, 
                    &HostNameGuid, 
                    &lpName
                    ))
    {
        INT iSize = strlen(lpName) + 1;

        if(iSize <= namelen)
        {
            memcpy(name, lpName, iSize);
        }
        else
        {
            SetLastError(WSAEFAULT);
            ErrorCode = SOCKET_ERROR;
        }
    }
    else
    {
        ErrorCode = SOCKET_ERROR;   // assume LastError has been set
    }

    if (pResults!=localResults)
        delete pResults;

    return(ErrorCode);
}  // gethostname


WINSOCK_API_LINKAGE
struct servent FAR * WSAAPI
getservbyport(
    IN int port,
    IN const char FAR * proto
    )
/*++
Routine Description:

    Get service information corresponding to a port and protocol.

Arguments:

    port  - The port for a service, in network byte order.

    proto - An optional pointer to a protocol name. If this is NULL,
            getservbyport() returns the first service entry for which
            the port matches the s_port. Otherwise getservbyport() 
            matches both the port and the proto. 

Returns:

    If no error occurs, getservbyport() returns a pointer to the
    servent structure described above. Otherwise it returns a NULL
    pointer and a specific error code is stored with SetErrorCode(). 
--*/
{
    PCHAR pszTemp;
    struct servent * sent;
    LPBLOB pBlob;
    PCHAR pResults;
    CHAR localResults[RNR_BUFFER_SIZE];
    INT ErrorCode;
    PDTHREAD Thread;

    ErrorCode = PROLOG(&Thread);
    if(ErrorCode != NO_ERROR)
    {
        SetLastError(ErrorCode);
        return(NULL);
    }

    pResults = localResults;

    if(!proto)
    {
        proto = "";
    }

    //
    // the 5 is the max number of digits in a port
    //
    pszTemp = new CHAR[strlen(proto) + 1 + 1 + 5];
    sprintf_s(pszTemp, strlen(proto)+1+1+5, "%d/%s", (port & 0xffff), proto);
    pBlob =  getxyDataEnt(pResults, 
                          RNR_BUFFER_SIZE, 
                          pszTemp, 
                          &IANAGuid,
                          0
                          );
    delete pszTemp;
    if(!pBlob)
    {
        sent = 0;
        if(GetLastError() == WSATYPE_NOT_FOUND)
        {
            SetLastError(WSANO_DATA);
        }
    }
    else
    {
        sent = (struct servent *)Thread->CopyServEnt(pBlob);
        if(sent)
        {
            UnpackServEnt(sent);
        }
    }

    if (pResults!=localResults)
        delete pResults;

    return(sent);
}  // getservbyport

WINSOCK_API_LINKAGE
struct servent FAR * WSAAPI
getservbyname(
    IN const char FAR * name,
    IN const char FAR * proto
    )
/*++
Routine Description:

    Get service information corresponding to a service name and
    protocol.

Arguments:

     name  - A pointer to a null-terminated service name.

    proto - An optional pointer to a null-terminated protocol name. If
            this pointer is NULL, getservbyname() returns the first
            service entry for which the name matches the s_name or one 
            of the s_aliases. Otherwise getservbyname() matches both 
            the name and the proto.
 
Returns:

    If no error occurs, getservbyname() returns a pointer to the servent
    structure described above. Otherwise it returns a NULL pointer and a
    specific error code is stored with SetErrorCode(). 

--*/
{
    PCHAR pszTemp;
    struct servent * sent;
    LPBLOB pBlob;
    PCHAR pResults;
    CHAR localResults[RNR_BUFFER_SIZE];
    INT ErrorCode;
    PDTHREAD Thread;

    ErrorCode = PROLOG(&Thread);
    if(ErrorCode != NO_ERROR)
    {
        SetLastError(ErrorCode);
        return(NULL);
    }

    pResults = localResults;

    if(!proto)
    {
        proto = "";
    }
    pszTemp = new CHAR[strlen(name) + strlen(proto) + 1 + 1];
    sprintf_s(pszTemp, strlen(name)+strlen(proto)+1+1, "%s/%s", name, proto);
    pBlob = getxyDataEnt(pResults,
                        RNR_BUFFER_SIZE, 
                        pszTemp, 
                        &IANAGuid, 
                        0
                        );
    delete pszTemp;
    if(!pBlob)
    {
        sent = 0;
        if(GetLastError() == WSATYPE_NOT_FOUND)
        {
            SetLastError(WSANO_DATA);
        }
    }
    else
    {
        sent = (struct servent *)Thread->CopyServEnt(pBlob);
        if(sent)
        {
            UnpackServEnt(sent);
        }
    }

    if (pResults!=localResults)
        delete pResults;

    return(sent);
}  // getservbyname

//
// Common routine for obtaining a xxxent buffer. Input is used to
// execute the WSALookup series of APIs.
//
// Args:
//   pResults -- a buffer supplied by the caller to be used in
//               the WASLookup calls. This should be as large as
//               the caller can afford to offer.
//   dwLength -- number of bytes in pResults
//   lpszName -- pointer to the service name. May by NULL
//   lpType   -- pointer to the service type . This should be one of
//               the SVCID_INET_xxxxx types. It may be anything
//               that produces a BLOB.
//   lppName  -- pointer to pointer where the resulting name pointer
//               is stored. May be NULL if the name is not needed.
//
// Returns:
//   0  --   No BLOB data was returned. In general, this means the 
//           operation failed. Evev if the WSALookupNext succeeded 
//           and returned a name, the name will not be returned.
//   else -- a pointer to the BLOB.
//
//
//
// The protocol restrictions list for all emulation operations. This 
// should limit the invoked providers to the set that know about 
// hostents and servents. If not, then the special SVCID_INET GUIDs 
// should take care of the remainder.
//
AFPROTOCOLS afp[2] = {
                      {AF_INET, IPPROTO_UDP},
                      {AF_INET, IPPROTO_TCP}
                     };

LPBLOB
getxyDataEnt(
    PCHAR *pResults,
    DWORD dwLength,
    LPSTR lpszName,
    LPGUID lpType,
    LPSTR *lppName)
{

    PWSAQUERYSETA pwsaq = (PWSAQUERYSETA)pResults;
    int err;
    HANDLE hRnR;
    LPBLOB pvRet = 0;
    INT Err = 0;

    //
    // create the query
    //
    memset(pwsaq, 0, sizeof(*pwsaq));
    pwsaq->dwSize = sizeof(*pwsaq);
    pwsaq->lpszServiceInstanceName = lpszName;
    pwsaq->lpServiceClassId = lpType;
    pwsaq->dwNameSpace = NS_ALL;
    pwsaq->dwNumberOfProtocols = 2;
    pwsaq->lpafpProtocols = &afp[0];

    err = WSALookupServiceBeginA(pwsaq,
                                 LUP_RETURN_BLOB | LUP_RETURN_NAME,
                                 &hRnR);

    if(err == NO_ERROR)
    {
        //
        // The query was accepted, so execute it via the Next call.
        //
        err = WSALookupServiceNextA(
                                hRnR,
                                0,
                                &dwLength,
                                pwsaq);
        //
        // if NO_ERROR was returned and a BLOB is present, this
        // worked, just return the requested information. Otherwise,
        // invent an error or capture the transmitted one.
        //

        if(err == NO_ERROR)
        {
            if(pvRet = pwsaq->lpBlob)
            {
                if(lppName)
                {
                    *lppName = pwsaq->lpszServiceInstanceName;
                }
            }
            else
            {
                err = WSANO_DATA;
            }
        }
        else
        {
            //
            // WSALookupServiceEnd clobbers LastError so save
            // it before closing the handle.
            //

            err = GetLastError();
        }
        WSALookupServiceEnd(hRnR);

        //
        // if an error happened, stash the value in LastError
        //

        if(err != NO_ERROR)
        {
            SetLastError(err);
        }
    }
    return(pvRet);
}
```



 

 



