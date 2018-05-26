---
title: DHCP Client API Examples
description: Navigation page for DHCP Client API examples.
ms.assetid: 85b1ca3a-b004-4cea-b01e-73adda466f13
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# DHCP Client API Examples

The following examples illustrate two uses of the DHCP Client API:

-   Example 1 illustrates how to use the [**DhcpRequestParams**](/windows/previous-versions/Dhcpcsdk/nf-dhcpcsdk-dhcprequestparams?branch=master) function to retrieve a host name.
-   Example 2 shows how the [**DhcpRegisterParamChange**](/windows/previous-versions/Dhcpcsdk/nf-dhcpcsdk-dhcpregisterparamchange?branch=master) function can be used to keep track of host name changes.

## Example 1: Using the DhcpRequestParams function

The following example illustrates how to retrieve the host name using the [**DhcpRequestParams**](/windows/previous-versions/Dhcpcsdk/nf-dhcpcsdk-dhcprequestparams?branch=master) function call. The name of the adapter can be retrieved using the **GetInterfaceInfo** structure, which is part of the Internet Protocol Helper API:


```C++
#include <windows.h>
#include <dhcpcsdk.h>

#pragma comment( lib, "dhcpcsvc.lib" )

BOOL RetrieveHostName(
    IN LPWSTR     pszAdapterName,
    IN OUT CHAR   pszHostNameBuf[], // must be large enough buffer
    IN DWORD      dwHostNameBufSize
)
/*++

Routine returns TRUE on success and FALSE on failure.

--*/
{
    DWORD dwError, dwSize;
    CHAR TmpBuffer[1000]; // host name won't be larger than this
    DHCPCAPI_PARAMS DhcpApiHostNameParams = {
            0,                // Flags
            OPTION_HOST_NAME, // OptionId
            FALSE,            // vendor specific?
            NULL,             // data filled in on return
            0                 // nBytes
        }; 
    DHCPCAPI_PARAMS_ARRAY RequestParams = {
            1,  // only one option to request 
            &amp;DhcpApiHostNameParams
        };

    DHCPCAPI_PARAMS_ARRAY SendParams = {
            0,   
            NULL
        };

    dwSize = sizeof(TmpBuffer);
    dwError = DhcpRequestParams(
            DHCPCAPI_REQUEST_SYNCHRONOUS, // Flags
            NULL,                         // Reserved
            pszAdapterName,               // Adapter Name
            NULL,                         // not using class id
               SendParams,                         // sent parameters
            RequestParams,                // requesting params
            (PBYTE) TmpBuffer,            // buffer
            &amp;dwSize,                      // buffer size
            NULL                          // Request ID
        );

    if( ERROR_MORE_DATA == dwError ) 
    {
            //
            // dwSize is not large enough.
            //
    }

    if( NO_ERROR == dwError ) 
    {

            // Check if the requested option was obtained.

            if( DhcpApiHostNameParams.nBytesData ) 
            {

                // Check size with dwHostNameBufSize.

                CopyMemory(
                     pszHostNameBuf, DhcpApiHostNameParams.Data,
                     DhcpApiHostNameParams.nBytesData
                     );
                pszHostNameBuf[DhcpApiHostNameParams.nBytesData] = '\0';
                return TRUE;
            }
    }

    return FALSE;
}
```



## Example 2: Using the DhcpRegisterParamChange function

The following code illustrates how the [**DhcpRegisterParamChange**](/windows/previous-versions/Dhcpcsdk/nf-dhcpcsdk-dhcpregisterparamchange?branch=master) function can be used to keep track of host name changes:


```C++
ULONG UpdateHostNameLoop(
    IN LPWSTR     pszAdapterName,
    IN CHAR       pszHostNameBuf[],
    IN ULONG      dwHostBufSize
)
{
    DWORD dwError;
    HANDLE hEvent;
    DHCPCAPI_PARAMS DhcpApiHostNameParams = {
            0,                 // Flags
            OPTION_HOST_NAME,  // OptionId
            FALSE,             // vendor specific?
            NULL,              // data filled in on return
            0                  // nBytes
        };
    DHCPCAPI_PARAMS_ARRAY DhcpApiParamsArray = {
        1,         // only one option to request 
        &amp;DhcpApiHostNameParams
        };

    dwError = DhcpRegisterParamChange(
        DHCPCAPI_REGISTER_HANDLE_EVENT, // Flags
        NULL,                           // Reserved
        pszAdapterName,                 // adapter name
        NULL,                           // no class ID
        DhcpApiParamsArray,             // params of interest
        (LPVOID)&amp;hEvent                 // event handle
        );

    if( ERROR_SUCCESS != dwError ) return dwError;

    // Wait on event all the time.

    while( WAIT_OBJECT_0 == WaitForSingleObject(hEvent, INFINITE) ) 
    {

        // Get host name and update it.

        ResetEvent(hEvent);
        dwError = RetrieveHostName(pszAdapterName, pszHostNameBuf, dwHostBufSize );
    
        // Ignore this error.

        break;
    }


    // Wait failed or retrieve failed? De-register the event handle.

    (void)DhcpDeRegisterParamChange(
        DHCPCAPI_REGISTER_HANDLE_EVENT, // Flags
        NULL,                           // Reserved
        (LPVOID) hEvent                 // event
        );

    return dwError;
}
```



> [!Note]  
> The event handle obtained by this routine must not be closed with the **CloseHandle** function. It should be released using the [**DhcpDeRegisterParamChange**](/windows/previous-versions/Dhcpcsdk/nf-dhcpcsdk-dhcpderegisterparamchange?branch=master) function in order to avoid resource leaks; the **DhcpDeRegisterParamChange** function releases internal resources allocated for this notification.

 

 

 




