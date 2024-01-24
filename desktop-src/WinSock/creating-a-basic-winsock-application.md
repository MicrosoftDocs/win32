---
description: How to create a basic Windows Sockets (Winsock) application.
ms.assetid: 56af2e95-ea82-49e4-b335-86dcf4c38780
title: Creating a Basic Winsock Application
ms.topic: article
ms.date: 05/31/2018
---

# Creating a Basic Winsock Application

**To create a basic Winsock application**

1.  Create a new empty project.
2.  Add an empty C++ source file to the project.
3.  Ensure that the build environment refers to the Include, Lib, and Src directories of the Microsoft Windows Software Development Kit (SDK) or the earlier Platform Software Development Kit (SDK).
4.  Ensure that the build environment links to the Winsock Library file Ws2\_32.lib. Applications that use Winsock must be linked with the Ws2\_32.lib library file. The \#pragma comment indicates to the linker that the *Ws2\_32.lib* file is needed.
5.  Begin programming the Winsock application. Use the Winsock API by including the Winsock 2 header files. The *Winsock2.h* header file contains most of the Winsock functions, structures, and definitions. The *Ws2tcpip.h* header file contains definitions introduced in the WinSock 2 Protocol-Specific Annex document for TCP/IP that includes newer functions and structures used to retrieve IP addresses.
    > [!Note]  
    > Stdio.h is used for standard input and output, specifically the **printf()** function.

     


```C++
#include <winsock2.h>
#include <ws2tcpip.h>
#include <stdio.h>

#pragma comment(lib, "Ws2_32.lib")

int main() {
  return 0;
}

```



> [!Note]
>
> The *Iphlpapi.h* header file is required if an application is using the IP Helper APIs. When the *Iphlpapi.h* header file is required, the \#include line for the *Winsock2.h* header file should be placed before the \#include line for the *Iphlpapi.h* header file.
>
> The *Winsock2.h* header file internally includes core elements from the *Windows.h* header file, so there is not usually an \#include line for the *Windows.h* header file in Winsock applications. If an \#include line is needed for the *Windows.h* header file, this should be preceded with the \#define WIN32\_LEAN\_AND\_MEAN macro. For historical reasons, the *Windows.h* header defaults to including the *Winsock.h* header file for Windows Sockets 1.1. The declarations in the *Winsock.h* header file will conflict with the declarations in the *Winsock2.h* header file required by Windows Sockets 2.0. The WIN32\_LEAN\_AND\_MEAN macro prevents the *Winsock.h* from being included by the *Windows.h* header. An example illustrating this is shown below.

 


```C++
#ifndef WIN32_LEAN_AND_MEAN
#define WIN32_LEAN_AND_MEAN
#endif

#include <windows.h>
#include <winsock2.h>
#include <ws2tcpip.h>
#include <iphlpapi.h>
#include <stdio.h>

#pragma comment(lib, "Ws2_32.lib")

int main() {
  return 0;
}

```



Next Step: [Initializing Winsock](initializing-winsock.md)

## Related topics

<dl> <dt>

[Getting Started With Winsock](getting-started-with-winsock.md)
</dt> <dt>

[About Servers and Clients](about-clients-and-servers.md)
</dt> </dl>

 

 



