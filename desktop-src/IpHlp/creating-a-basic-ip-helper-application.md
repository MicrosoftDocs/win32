---
description: How to create a basic IP Helper application.
ms.assetid: b53f1cf5-3659-407e-8279-5c94333f3017
title: Creating a Basic IP Helper Application
ms.topic: article
ms.date: 05/31/2018
---

# Creating a Basic IP Helper Application

**To create a basic IP Helper application**

1.  Create a new empty project.
2.  Add an empty C++ source file to the project.
3.  Ensure that the build environment refers to the Include, Lib, and Src directories of the Platform Software Development Kit (SDK).
4.  Ensure that the build environment links to the IP Helper Library file Iphlpapi.lib and the Winsock Library file WS2\_32.lib.
    > [!Note]  
    > Some basic Winsock functions are used to return IP address values and other information.

     

5.  Begin programming the IP Helper application. Use the IP Helper API by including the IP Helper header file.

    ```C++
    #include <winsock2.h>
    #include <iphlpapi.h>
    #include <stdio.h>

    int main() {
      return 0;
    }
    
    ```

    

    > [!Note]
    >
    > The *Iphlpapi.h* header file is required for applications that use the IP Helper functions. The *Iphlpapi.h* header file automatically includes other headers files with structures and enumerations used by the IP Helper functions.
    >
    > The new IP Helper functions introduced in Windows Vista and later are defined in the *Netioapi.h* header file which is automatically included by the *Iphlpapi.h* header file. The *Netioapi.h* header file should never be used directly.
    >
    > Many of the structures and enumerations used by IP Helper functions are defined in the *Iprtrmib.h*, *Ipexport.h*, and *Iptypes.h* header files. These header files are automatically included in the *Iphlpapi.h* header file and should never be used directly.
    >
    > On the Microsoft Windows Software Development Kit (SDK) released for Windows Vista and later, the organization of header files has changed. Some of the structures are now defined in the *Ipmib.h*, *Tcpmib.h*, and *Udpmib.h* header files, not in the *Iprtrmib.h* header file. The *Ipmib.h* header file automatically includes the *Ifmib.h* header file. Note that these header files are automatically included in *Iprtrmib.h*, which is automatically included in the *Iphlpapi.h* header file.
    >
    > The *Winsock2.h* header file for Windows Sockets 2.0 is required by most applications using the IP Helper APIs. When the *Winsock2.h* header file is required, the \#include line for this file should be placed before the \#include line for the *Iphlpapi.h* header file.
    >
    > The *Winsock2.h* header file internally includes core elements from the *Windows.h* header file, so there is not usually an \#include line for *Windows.h* header file in IP Helper applications. If an \#include line is needed for the *Windows.h* header file, this should be preceded with the \#define WIN32\_LEAN\_AND\_MEAN macro. For historical reasons, the *Windows.h* header defaults to including the *Winsock.h* header file for Windows Sockets 1.1. The declarations in the *Winsock.h* header file for Windows Sockets 1.1 will conflict with the declarations in the *Winsock2.h* header file required by Windows Sockets 2.0. The WIN32\_LEAN\_AND\_MEAN macro prevents the *Winsock.h* header file from being included by the *Windows.h* header file. An example illustrating this is shown below.

     

    ```C++
    #ifndef WIN32_LEAN_AND_MEAN
    #define WIN32_LEAN_AND_MEAN
    #endif

    #include <windows.h>

    #include <winsock2.h>
    #include <iphlpapi.h>
    #include <stdio.h>

    int main() {
      return 0;
    }
    
    ```

    

    > [!Note]
    >
    > This basic IP Helper application only uses some IP address data structures and IP address to string conversion functions from Windows Sockets 2.0. These Windows Sockets functions can be used without calling [**WSAStartup**](/windows/desktop/api/winsock/nf-winsock-wsastartup) to initialize Windows Sockets resources and [**WSACleanup**](/windows/desktop/api/winsock/nf-winsock-wsacleanup) when done using these resources.
    >
    > In IP Helper applications that use other Winsock functions other than these IP address to string functions, the [**WSAStartup**](/windows/desktop/api/winsock/nf-winsock-wsastartup) function must be called to initialize Windows Sockets resources before calling any Windows Sockets functions and [**WSACleanup**](/windows/desktop/api/winsock/nf-winsock-wsacleanup) should be called when the application is done using Windows Sockets resources.

     

    > [!Note]
    >
    > The *Stdio.h* header file is required for the use of various standard C functions in this basic IP Helper application.

     

    Next Step: [Retrieving Information Using GetNetworkParams](retrieving-information-using-getnetworkparams.md)

 

 
