---
title: Enumerating Network Resources
description: The following example illustrates an application-defined function (EnumerateFunc) that enumerates all the resources on a network.
ms.assetid: f5872ee7-483d-406a-b7d8-4ce93613fd29
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Enumerating Network Resources

The following example illustrates an application-defined function (EnumerateFunc) that enumerates all the resources on a network. The sample specifies **NULL** for the pointer to the [**NETRESOURCE**](/windows/win32/Winnetwk/ns-winnetwk-_netresourcea?branch=master) structure because when [**WNetOpenEnum**](wnetopenenum.md) receives a **NULL** pointer, it retrieves a handle to the root of the network.

To begin the enumeration of a network container resource, your application should perform the following steps:

1.  Pass the address of a [**NETRESOURCE**](/windows/win32/Winnetwk/ns-winnetwk-_netresourcea?branch=master) structure that represents the resource to the [**WNetOpenEnum**](wnetopenenum.md) function.
2.  Allocate a buffer large enough to hold the array of [**NETRESOURCE**](/windows/win32/Winnetwk/ns-winnetwk-_netresourcea?branch=master) structures that the [**WNetEnumResource**](wnetenumresource.md) function returns, plus the strings to which their members point.
3.  Pass the resource handle returned by [**WNetOpenEnum**](wnetopenenum.md) to the [**WNetEnumResource**](wnetenumresource.md) function.
4.  Close the resource handle when it is no longer needed by calling the [**WNetCloseEnum**](wnetcloseenum.md) function.

You can continue enumerating a container resource described in the array of [**NETRESOURCE**](/windows/win32/Winnetwk/ns-winnetwk-_netresourcea?branch=master) structures retrieved by [**WNetEnumResource**](wnetenumresource.md). If the **dwUsage** member of the **NETRESOURCE** structure is equal to RESOURCEUSAGE\_CONTAINER, pass the address of the structure to the [**WNetOpenEnum**](wnetopenenum.md) function to open the container and continue the enumeration. If **dwUsage** is equal to RESOURCEUSAGE\_CONNECTABLE, the application can pass the structure's address to the [**WNetAddConnection2**](wnetaddconnection2.md) function or the [**WNetAddConnection3**](wnetaddconnection3.md) function to connect to the resource.

First the sample calls the [**WNetOpenEnum**](wnetopenenum.md) function to begin the enumeration. The sample calls the [**GlobalAlloc**](https://msdn.microsoft.com/library/windows/desktop/aa366574) function to allocate the required buffer, and then calls the [**ZeroMemory**](https://msdn.microsoft.com/library/windows/desktop/aa366920) function to set the buffer contents to zero. Then the sample calls the [**WNetEnumResource**](wnetenumresource.md) function to continue the enumeration. Whenever the **dwUsage** member of a [**NETRESOURCE**](/windows/win32/Winnetwk/ns-winnetwk-_netresourcea?branch=master) structure retrieved by **WNetEnumResource** is equal to RESOURCEUSAGE\_CONTAINER, the EnumerateFunc function calls itself recursively and uses a pointer to that structure in its call to **WNetOpenEnum**. Finally, the sample calls the [**GlobalFree**](https://msdn.microsoft.com/library/windows/desktop/aa366579) function to free the allocated memory, and the [**WNetCloseEnum**](wnetcloseenum.md) to end the enumeration.


```C++
#ifndef UNICODE
#define UNICODE
#endif
#pragma comment(lib, "mpr.lib")

#include <windows.h>
#include <stdio.h>
#include <winnetwk.h>

BOOL WINAPI EnumerateFunc(LPNETRESOURCE lpnr);
void DisplayStruct(int i, LPNETRESOURCE lpnrLocal);

int main()
{

    LPNETRESOURCE lpnr = NULL;

    if (EnumerateFunc(lpnr) == FALSE) {
        printf("Call to EnumerateFunc failed\n");
        return 1;
    } else
        return 0;

}

BOOL WINAPI EnumerateFunc(LPNETRESOURCE lpnr)
{
    DWORD dwResult, dwResultEnum;
    HANDLE hEnum;
    DWORD cbBuffer = 16384;     // 16K is a good size
    DWORD cEntries = -1;        // enumerate all possible entries
    LPNETRESOURCE lpnrLocal;    // pointer to enumerated structures
    DWORD i;
    //
    // Call the WNetOpenEnum function to begin the enumeration.
    //
    dwResult = WNetOpenEnum(RESOURCE_GLOBALNET, // all network resources
                            RESOURCETYPE_ANY,   // all resources
                            0,  // enumerate all resources
                            lpnr,       // NULL first time the function is called
                            &amp;hEnum);    // handle to the resource

    if (dwResult != NO_ERROR) {
        printf("WnetOpenEnum failed with error %d\n", dwResult);
        return FALSE;
    }
    //
    // Call the GlobalAlloc function to allocate resources.
    //
    lpnrLocal = (LPNETRESOURCE) GlobalAlloc(GPTR, cbBuffer);
    if (lpnrLocal == NULL) {
        printf("WnetOpenEnum failed with error %d\n", dwResult);
//      NetErrorHandler(hwnd, dwResult, (LPSTR)"WNetOpenEnum");
        return FALSE;
    }

    do {
        //
        // Initialize the buffer.
        //
        ZeroMemory(lpnrLocal, cbBuffer);
        //
        // Call the WNetEnumResource function to continue
        //  the enumeration.
        //
        dwResultEnum = WNetEnumResource(hEnum,  // resource handle
                                        &amp;cEntries,      // defined locally as -1
                                        lpnrLocal,      // LPNETRESOURCE
                                        &amp;cbBuffer);     // buffer size
        //
        // If the call succeeds, loop through the structures.
        //
        if (dwResultEnum == NO_ERROR) {
            for (i = 0; i < cEntries; i++) {
                // Call an application-defined function to
                //  display the contents of the NETRESOURCE structures.
                //
                DisplayStruct(i, &amp;lpnrLocal[i]);

                // If the NETRESOURCE structure represents a container resource, 
                //  call the EnumerateFunc function recursively.

                if (RESOURCEUSAGE_CONTAINER == (lpnrLocal[i].dwUsage
                                                & RESOURCEUSAGE_CONTAINER))
//          if(!EnumerateFunc(hwnd, hdc, &amp;lpnrLocal[i]))
                    if (!EnumerateFunc(&amp;lpnrLocal[i]))
                        printf("EnumerateFunc returned FALSE\n");
//            TextOut(hdc, 10, 10, "EnumerateFunc returned FALSE.", 29);
            }
        }
        // Process errors.
        //
        else if (dwResultEnum != ERROR_NO_MORE_ITEMS) {
            printf("WNetEnumResource failed with error %d\n", dwResultEnum);

//      NetErrorHandler(hwnd, dwResultEnum, (LPSTR)"WNetEnumResource");
            break;
        }
    }
    //
    // End do.
    //
    while (dwResultEnum != ERROR_NO_MORE_ITEMS);
    //
    // Call the GlobalFree function to free the memory.
    //
    GlobalFree((HGLOBAL) lpnrLocal);
    //
    // Call WNetCloseEnum to end the enumeration.
    //
    dwResult = WNetCloseEnum(hEnum);

    if (dwResult != NO_ERROR) {
        //
        // Process errors.
        //
        printf("WNetCloseEnum failed with error %d\n", dwResult);
//    NetErrorHandler(hwnd, dwResult, (LPSTR)"WNetCloseEnum");
        return FALSE;
    }

    return TRUE;
}

void DisplayStruct(int i, LPNETRESOURCE lpnrLocal)
{
    printf("NETRESOURCE[%d] Scope: ", i);
    switch (lpnrLocal->dwScope) {
    case (RESOURCE_CONNECTED):
        printf("connected\n");
        break;
    case (RESOURCE_GLOBALNET):
        printf("all resources\n");
        break;
    case (RESOURCE_REMEMBERED):
        printf("remembered\n");
        break;
    default:
        printf("unknown scope %d\n", lpnrLocal->dwScope);
        break;
    }

    printf("NETRESOURCE[%d] Type: ", i);
    switch (lpnrLocal->dwType) {
    case (RESOURCETYPE_ANY):
        printf("any\n");
        break;
    case (RESOURCETYPE_DISK):
        printf("disk\n");
        break;
    case (RESOURCETYPE_PRINT):
        printf("print\n");
        break;
    default:
        printf("unknown type %d\n", lpnrLocal->dwType);
        break;
    }

    printf("NETRESOURCE[%d] DisplayType: ", i);
    switch (lpnrLocal->dwDisplayType) {
    case (RESOURCEDISPLAYTYPE_GENERIC):
        printf("generic\n");
        break;
    case (RESOURCEDISPLAYTYPE_DOMAIN):
        printf("domain\n");
        break;
    case (RESOURCEDISPLAYTYPE_SERVER):
        printf("server\n");
        break;
    case (RESOURCEDISPLAYTYPE_SHARE):
        printf("share\n");
        break;
    case (RESOURCEDISPLAYTYPE_FILE):
        printf("file\n");
        break;
    case (RESOURCEDISPLAYTYPE_GROUP):
        printf("group\n");
        break;
    case (RESOURCEDISPLAYTYPE_NETWORK):
        printf("network\n");
        break;
    default:
        printf("unknown display type %d\n", lpnrLocal->dwDisplayType);
        break;
    }

    printf("NETRESOURCE[%d] Usage: 0x%x = ", i, lpnrLocal->dwUsage);
    if (lpnrLocal->dwUsage & RESOURCEUSAGE_CONNECTABLE)
        printf("connectable ");
    if (lpnrLocal->dwUsage & RESOURCEUSAGE_CONTAINER)
        printf("container ");
    printf("\n");

    printf("NETRESOURCE[%d] Localname: %S\n", i, lpnrLocal->lpLocalName);
    printf("NETRESOURCE[%d] Remotename: %S\n", i, lpnrLocal->lpRemoteName);
    printf("NETRESOURCE[%d] Comment: %S\n", i, lpnrLocal->lpComment);
    printf("NETRESOURCE[%d] Provider: %S\n", i, lpnrLocal->lpProvider);
    printf("\n");
}

```



For more information about using an application-defined error handler, see [Retrieving Network Errors](retrieving-network-errors.md).

 

 




