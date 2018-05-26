---
Description: The following example shows the main function of a console application that attempts to activate the computer on which the application is running.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: cefa992c-6734-4cd2-a781-957ac0a6de75
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: ComputerActivation\_Main.cpp
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# ComputerActivation\_Main.cpp

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

The following example shows the main function of a console application that attempts to activate the computer on which the application is running. The function performs the following actions:

-   Creates a client session.
-   Determines whether the computer has already been activated and returns if it has. Attempting to license an already activated computer will overwrite the machine certificate in the certificate store.
-   Creates an event object that the custom callback function can signal when the computer has been activated. For more information, see [ComputerActivation\_Callback.cpp](computeractivation-callback-cpp.md).
-   Calls [**DRMActivate**](/windows/previous-versions/Msdrm/nf-msdrm-drmactivate?branch=master) to activate the computer. This is an asynchronous function that returns immediately and periodically calls into your callback function with status information.

If activation is successful, the machine certificate is automatically saved in the appropriate [Machine Certificate Store](machine-certificate-store.md).


```C++
#include "ComputerActivation.h"

/*===================================================================
File:      ComputerActivation_Main.cpp

THIS CODE AND INFORMATION IS PROVIDED "AS IS" WITHOUT WARRANTY OF
ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING BUT NOT LIMITED TO
THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS FOR A
PARTICULAR PURPOSE.

Copyright (C) Microsoft.  All rights reserved.
===================================================================*/

/////////////////////////////////////////////////////////////////////
// This sample shows how to activate a computer. It activates the
// computer locally and does not, therefore, require service 
// discovery over the Internet or on an intranet.
//
int _tmain(int argc, _TCHAR* argv[])
{
  HRESULT           hr                = S_OK;
  DRMHSESSION       hClient           = NULL;
  DWORD             DW_WAIT_TIME      = 60000;
  DWORD             dwWaitResult      = 0;
  DRM_CONTEXT       context;

  // Create a client session.
  hr = DRMCreateClientSession( 
          &amp;StatusCallback,                    // Callback function
          0,                                  // Reserved
          DRM_DEFAULTGROUPIDTYPE_WINDOWSAUTH, // Authentication type
          NULL,                               // User ID
          &amp;hClient );                         // Client handle
  if (FAILED(hr)) return hr;

  // Determine whether the computer is already activated. If it is,
  // activating it again overwrites the machine certificate.
  hr = DRMIsActivated(
          hClient,                          // Client session handle
          DRM_ACTIVATE_MACHINE,             // Activation type
          NULL);                            // NULL
  if (SUCCEEDED(hr)) goto e_Exit;

  // Create an event for the callback function to signal when
  // the computer has been activated.
  SecureZeroMemory(&amp;context, sizeof(context));
  context.hEvent = CreateEvent(
          NULL,                       // No attributes
          FALSE,                      // Automatic reset
          FALSE,                      // Initial state not signaled
          NULL);                      // Event object not named
  if (NULL == context.hEvent) goto e_Exit;

  // Activate the computer.
  hr = DRMActivate( 
          hClient,                    // Client session handle
          DRM_ACTIVATE_MACHINE |      // Activate the computer
            DRM_ACTIVATE_SILENT,      // Silent activation
          0,                          // Default LCID
          NULL,                       // Server information
          (VOID*)&amp;context,            // Callback context
          NULL);                      // Use the active window
  if (FAILED(hr)) goto e_Exit;

  // Wait for the callback to return.
  dwWaitResult = WaitForSingleObject( 
          context.hEvent, 
          DW_WAIT_TIME);
  if (WAIT_TIMEOUT==dwWaitResult || FAILED(context.hr))
  {
    wprintf(L"Computer activation error.\r\n");
    wprintf(L"Enter any key to continue...");
    _getch();
  }

e_Exit:

  if (NULL != hClient)
  {
    DRMCloseSession(hClient);
    hClient = NULL;
  }
  if (NULL != context.hEvent)
  {
      CloseHandle(context.hEvent);
  }

  return hr;
}
```



## Related topics

<dl> <dt>

[Activating a Computer](activating-a-computer.md)
</dt> <dt>

[ComputerActivation.h](computeractivation-h.md)
</dt> <dt>

[ComputerActivation\_Callback.cpp](computeractivation-callback-cpp.md)
</dt> </dl>

 

 



