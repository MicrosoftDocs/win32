---
title: Implementing DllMain
description: To work with an instance of a resource type, a Resource Monitor needs to have the resource DLL that supports the type loaded into its process.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 022bc68f-94f4-4651-8385-e12fc34ae8f2
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- DllMain Failover Cluster
- DllMain Failover Cluster ,implementing
- entry point functions Failover Cluster ,implementing DllMain
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Implementing DllMain

To work with an instance of a [resource type](resource-types.md), a [Resource Monitor](resource-monitor.md) needs to have the [resource DLL](resource-dlls.md) that supports the type loaded into its process. If the DLL is already loaded, the Resource Monitor calls the appropriate entry point function. If not, the Resource Monitor calls [**LoadLibrary**](https://msdn.microsoft.com/library/windows/desktop/ms684175) and triggers the [*DllMain*](https://msdn.microsoft.com/library/windows/desktop/ms682583) entry point.

**To implement DllMain**

1.  Recommended: Call the function [**DisableThreadLibraryCalls**](https://msdn.microsoft.com/library/windows/desktop/ms682579) in response to **DLL\_PROCESS\_ATTACH**. Refer to the description of the function for the performance benefits.
2.  Optional: Initialize semaphores, mutexes, critical sections, classes, COM objects, or any other objects used by the DLL.
3.  Recommended. For optimal performance, take no more than 300 milliseconds to return a value.

Resource DLLs that support multiple resource types typically define a single [*DllMain*](https://msdn.microsoft.com/library/windows/desktop/ms682583) entry point for the entire DLL, and define an entry point for each &lt;Name&gt; resource type supported by the DLL. This is illustrated in the following example.

## Example

The following example demonstrates a [*DllMain*](https://msdn.microsoft.com/library/windows/desktop/ms682583) implementation in a resource DLL that supports two resource types, MyTypeAlpha and MyTypeBeta. For additional examples see [Resource DLL Examples](https://msdn.microsoft.com/library/aa370474).


```C++
//////////////////////////////////////////////////////////////////////

BOOLEAN WINAPI DllMain( IN HINSTANCE hDllHandle, 
         IN DWORD     nReason, 
         IN LPVOID    Reserved )
 {
  BOOLEAN bSuccess = TRUE;


  //  Perform global initialization.

  switch ( nReason )
   {
    case DLL_PROCESS_ATTACH:

      //  For optimization.

      DisableThreadLibraryCalls( hDllHandle );

      break;

    case DLL_PROCESS_DETACH:

      break;
   }


  //  Perform type-specific initialization.

  if(    MyTypeAlphaDllMain( hDllHandle, nReason, Reserved )
      &amp;&amp; MyTypeBetaDllMain(  hDllHandle, nReason, Reserved ) )
   {
    bSuccess = TRUE;
   }
  else
   {
    bSuccess = FALSE;
   }


  return bSuccess;

 }
//  end DllMain

//////////////////////////////////////////////////////////////////////

BOOLEAN WINAPI MyTypeAlphaDllMain( IN HINSTANCE hDllHandle, 
                    IN DWORD nReason, 
                    IN LPVOID Reserved )
 {
  switch ( nReason )
   {
    case DLL_PROCESS_ATTACH:

      g_hSIS = CreateSemaphoreW( NULL, 0, 1, SIS_ALPHA );

      if( g_hSIS == NULL ) return FALSE;

      //  Set initial count to 1.

      if( GetLastError() != ERROR_ALREADY_EXISTS )
         ReleaseSemaphore( g_hSIS, 1, NULL );

      break;

    case DLL_PROCESS_DETACH:

      if ( g_hSIS != NULL )
       {
        CloseHandle( g_hSIS );
        g_hSIS = NULL;
       }

      break;

   }

  return TRUE;

 }
//  end MyTypeAlphaDllMain

//////////////////////////////////////////////////////////////////////

BOOLEAN WINAPI MyTypeBetaDllMain( IN HINSTANCE hDllHandle, 
                   IN DWORD nReason, 
                   IN LPVOID Reserved )
 {

  //  MyTypeBeta needs no processing at this time.

  switch ( nReason )
   {
    case DLL_PROCESS_ATTACH:

      break;

    case DLL_PROCESS_DETACH:

      break;

   }

  return TRUE;

 }
//  end MyTypeBetaDllMain

//////////////////////////////////////////////////////////////////////
```



 

 




