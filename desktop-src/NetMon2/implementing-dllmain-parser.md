---
description: Network Monitor uses the DllMain export function to identify the existence of the parser, and release resources that Network Monitor uses to store information about the parser.
ms.assetid: 1741a12c-3645-4e83-b97f-37e67218c5eb
title: Implementing DllMain Parser
ms.topic: article
ms.date: 05/31/2018
---

# Implementing DllMain Parser

Network Monitor uses the **DllMain** export function to identify the existence of the parser, and release resources that Network Monitor uses to store information about the parser.

When Network Monitor calls **DllMain** for the first time, the parser DLL calls [**CreateProtocol**](createprotocol.md) to do the following:

-   Specify the protocol that the parser detects.
-   Provide entry points for remaining parser export functions that Network Monitor calls.

When Network Monitor calls **DllMain** for the last time, **DllMain** calls [**DestroyProtocol**](destroyprotocol.md) to release all resources that Network Monitor uses to store information about the parser.

The following procedure identifies the steps necessary to implement **DllMain**.

**To implement DllMain**

1.  Specify the [**ENTRYPOINTS**](entrypoints.md) structure for the [**CreateProtocol**](createprotocol.md) function and global Attach variable. The Attach variable is used to track the number of protocol instances that are running.
2.  Look at the value of the *Command* parameter that the operating system sets.

    If the *Command* parameter is set to DLL\_PROCESS\_ATTACH and Attach is 0, then call [**CreateProtocol**](createprotocol.md) to provide the protocol name and entry points for the following export functions.

    -   **Register**
    -   **Deregister**
    -   **RecognizeFrame**
    -   **AttachProperties**
    -   **FormatProperties** (only required if Network Monitor will be displaying the protocol properties).

    If the *Command* parameter is set to DLL\_PROCESS\_DETACH and Attach is 0, then call [**DestroyProtocol**](destroyprotocol.md) using the instance handle that [**CreateProtocol**](createprotocol.md) returns.

3.  Return **TRUE** because the **DllMain** parser function must always return **TRUE**.

The following is a basic implementation of **DllMain**. The code example uses a case statement to trap values of the *Command* parameter to determine if [**CreateProtocol**](createprotocol.md) or [**DestroyProtocol**](destroyprotocol.md) should be called.

``` syntax
#include <windows.h>

// Entry point structure for parser export functions and global
// Attach variable.
ENTRYPOINTS EntryPoints =
{
  Register,
  Deregister,
  RecognizeFrame,
  AttachProperties,
  FormatProperties
};

DWORD Attached = 0; 

BOOL WINAPI DllMain(HANDLE hInstance, ULONG Command, LPVOID Reserved)
{
  switch(Command)
  {
  // Call CreateProtocol.
  case DLL_PROCESS_ATTACH:
       // Loading parser DLL.
       if(Attached == 0)
       {
         hProtocol = CreateProtocol( "ProtocolName",
                                     &EntryPoints,
                                     ENTRYPOINTS_SIZE);
       }
       Attached++;
       break;
  // Call DestroyProtocol.
  case DLL_PROCESS_DETACH:
       // Unloading parser DLL.
       Attached--;
       if(Attached == 0)
       {
         DestroyProtocol( hProtocol);
       }
       break;
  }
  return TRUE;
}
```

 

 



