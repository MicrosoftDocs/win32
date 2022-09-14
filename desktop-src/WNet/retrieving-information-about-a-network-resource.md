---
title: Retrieving Information About a Network Resource
description: To identify the network provider that owns a resource, an application can call the WNetGetResourceInformation function, as illustrated in the following code sample.
ms.assetid: 4bddb55c-181d-4c6f-bd92-9c27d6b894bb
ms.topic: article
ms.date: 05/31/2018
---

# Retrieving Information About a Network Resource

To identify the network provider that owns a resource, an application can call the [**WNetGetResourceInformation**](/windows/win32/api/winnetwk/nf-winnetwk-wnetgetresourceinformationa) function, as illustrated in the following code sample.

The following sample is a function (CheckServer) that takes a server name as a parameter and returns information about that server. First the function calls the [**ZeroMemory**](/previous-versions/windows/desktop/legacy/aa366920(v=vs.85)) function to initialize the contents of a block of memory to zero. Then the sample calls the [**WNetGetResourceInformation**](/windows/win32/api/winnetwk/nf-winnetwk-wnetgetresourceinformationa) function, specifying a buffer large enough to hold only a [**NETRESOURCE**](/windows/desktop/api/Winnetwk/ns-winnetwk-netresourcea) structure. The routine includes error processing to handle the case when a buffer of this size is insufficient to hold the variable-length strings to which members of the **NETRESOURCE** structure point. If this error occurs, the sample allocates sufficient memory and calls **WNetGetResourceInformation** again. Finally, the sample frees the allocated memory.

Note that the sample assumes that the *pszServer* parameter points to a server name that one of the network providers on the local computer recognizes.


```C++
#include <Windows.h>
#include <Winnetwk.h >

// Need to link with Mpr.lib
#pragma comment(lib, "Mpr.lib")
//
// Verify a server on the network. 
//
DWORD
CheckServer( LPTSTR pszServer )
{  
    DWORD dwBufferSize = sizeof(NETRESOURCE);
    LPBYTE lpBuffer;                  // buffer
    NETRESOURCE nr;
    LPTSTR pszSystem = NULL;          // variable-length strings

    //
    // Set the block of memory to zero; then initialize
    // the NETRESOURCE structure. 
    //
    ZeroMemory(&nr, sizeof(nr));

    nr.dwScope       = RESOURCE_GLOBALNET;
    nr.dwType        = RESOURCETYPE_ANY;
    nr.lpRemoteName  = pszServer;

    //
    // First call the WNetGetResourceInformation function with 
    // memory allocated to hold only a NETRESOURCE structure. This 
    // method can succeed if all the NETRESOURCE pointers are NULL.
    // If the call fails because the buffer is too small, allocate
    // a larger buffer.
    //
    lpBuffer = (LPBYTE) malloc( dwBufferSize );
    if (lpBuffer == NULL) 
        return FALSE;

    while ( WNetGetResourceInformation(&nr, lpBuffer, &dwBufferSize, 
                &pszSystem) == ERROR_MORE_DATA)
    {
        lpBuffer = (LPBYTE) realloc(lpBuffer, dwBufferSize);
    }

    // Process the contents of the NETRESOURCE structure and the
    // variable-length strings in lpBuffer and set dwValue. When
    // finished, free the memory.

    free(lpBuffer);

    return TRUE;
}
```



 

 