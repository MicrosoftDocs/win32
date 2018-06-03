---
Description: The following example shows a custom callback function that will be called by DRMAcquireLicense during acquisition of the end-user license chain.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 45527efe-397e-4a25-87fa-06bf7ee5e4e1
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: Revocation\_Callback.cpp
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Revocation\_Callback.cpp

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

The following example shows a custom callback function that will be called by [**DRMAcquireLicense**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmacquirelicense) during acquisition of the end-user license chain. In this example, a blocking event object is created in [Revocation\_GetEULChain.cpp](revocation-geteulchain-cpp.md) prior to calling the **DRMAcquireLicense** function. **DRMAcquireLicense** is an asynchronous function that returns control immediately and continues processing on another thread, periodically calling into your callback with status information that you can filter and report back to the user. After the license has been saved in the certificate store, this example processes the S\_DRM\_COMPLETED value and calls the [SetEvent](http://go.microsoft.com/fwlink/p/?linkid=113906) function to unblock the primary process thread.


```C++
#include "DecryptingContent.h"

/*===================================================================
File:      Decryption_Callback.cpp

THIS CODE AND INFORMATION IS PROVIDED "AS IS" WITHOUT WARRANTY OF
ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING BUT NOT LIMITED TO
THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS FOR A
PARTICULAR PURPOSE.

Copyright (C) Microsoft.  All rights reserved.
===================================================================*/

/////////////////////////////////////////////////////////////////////
// User-defined function to be called by the asynchronous AD RMS
// DRMAcquireLicense function in the Revocation_GetEULChain.cpp 
// file. The callback function must have the following signature, 
// but you can use the function to perform  whatever action your 
// application requires. Typically, you use the callback to relay 
// the status of an AD RMS operation to the end-user.
//
HRESULT __stdcall StatusCallback( 
                       DRM_STATUS_MSG msg, 
                       HRESULT hr, 
                       void *pvParam, 
                       void *pvContext)
{
  // Cast the pvContext (void*) argument to point to a Drm_Context
  // structure and verify that the argument is not NULL.
  PDRM_CONTEXT pContext = (PDRM_CONTEXT)pvContext;
  if (!pContext) return E_FAIL;

  // Initialize the hr member of the Drm_Context structure by using
  // the HRESULT value passed to the callback by the AD RMS
  // function. If the HRESULT passed to the callback is not S_OK,
  // and the Drm_Context structure contains a valid event handle,
  // signal the event and return.
  pContext->hr = hr;
  if (FAILED(pContext->hr) &amp;&amp; pContext->hEvent)
  {
    SetEvent((HANDLE)pContext->hEvent);
    return S_OK;
  }

 // Print the callback status message.
  switch(msg)
  {
  case DRM_MSG_ACTIVATE_MACHINE:
    wprintf(L"\nCallback msg = DRM_MSG_ACTIVATE_MACHINE ");
    break;
  case DRM_MSG_ACTIVATE_GROUPIDENTITY:
    wprintf(L"\nCallback msg = DRM_MSG_ACTIVATE_GROUPIDENTITY ");
    break;
  case DRM_MSG_ACQUIRE_CLIENTLICENSOR:
    wprintf(L"\nCallback msg = DRM_MSG_ACQUIRE_CLIENTLICENSOR ");
    break;
  case DRM_MSG_SIGN_ISSUANCE_LICENSE:
    wprintf(L"\nCallback msg = DRM_MSG_SIGN_ISSUANCE_LICENSE ");
    break;
  case DRM_MSG_ACQUIRE_LICENSE:
    wprintf(L"\nCallback msg = DRM_MSG_ACQUIRE_LICENSE ");
    break;
  default:
    wprintf(L"\nDefault callback status msg = 0x%x ", msg);
    break;
  }

  // Print the callback error result.
  switch(pContext->hr)
  {
  case S_DRM_ALREADY_ACTIVATED:
    wprintf(L"Callback hr = S_DRM_ALREADY_ACTIVATED\n");
    break;
  case S_DRM_CONNECTING:
    wprintf(L"Callback hr = S_DRM_CONNECTING\n");
    break;
  case S_DRM_CONNECTED:
    wprintf(L"Callback hr = S_DRM_CONNECTED\n");
    break;
  case S_DRM_INPROGRESS:
    wprintf(L"Callback hr = S_DRM_INPROGRESS\n");
    break;
  case S_DRM_COMPLETED:
    wprintf(L"Callback hr = S_DRM_COMPLETED\n");
    pContext->hr = S_OK;
    if ( pContext->hEvent )
    {
      SetEvent( ( HANDLE )pContext->hEvent );
    }
    break;
  case E_DRM_ACTIVATIONFAILED:
    wprintf(L"Callback hr = E_DRM_ACTIVATIONFAILED\n");
    break;
  case E_DRM_HID_CORRUPTED:
    wprintf(L"Callback hr = E_DRM_HID_CORRUPTED\n");
    break;
  case E_DRM_INSTALLATION_FAILED:
    wprintf(L"Callback hr = E_DRM_INSTALLATION_FAILED\n");
    break;
  case E_DRM_ALREADY_IN_PROGRESS:
    wprintf(L"Callback hr = E_DRM_ALREADY_IN_PROGRESS\n");
    break;
  case E_DRM_NO_CONNECT:
    wprintf(L"Callback hr = E_DRM_NO_CONNECT\n");
    break;
  case E_DRM_ABORTED:
    wprintf(L"Callback hr = E_DRM_ABORTED\n");
    break;
  case E_DRM_SERVER_ERROR:
    wprintf(L"Callback hr = E_DRM_SERVER_ERROR\n");
    break;
  case E_DRM_INVALID_SERVER_RESPONSE:
    wprintf(L"Callback hr = E_DRM_INVALID_SERVER_RESPONSE\n");
    break;
  case E_DRM_SERVER_NOT_FOUND:
    wprintf(L"Callback hr = E_DRM_SERVER_NOT_FOUND\n");
    break;
  case E_DRM_AUTHENTICATION_FAILED:
    wprintf(L"Callback hr = E_DRM_AUTHENTICATION_FAILED\n");
    break;
  case E_DRM_EMAIL_NOT_VERIFIED:
    wprintf(L"Callback hr = E_DRM_EMAIL_NOT_VERIFIED\n");
    break;
  case E_DRM_AD_ENTRY_NOT_FOUND:
    wprintf(L"Callback hr = E_DRM_AD_ENTRY_NOT_FOUND\n");
    break;
  case E_DRM_NEEDS_MACHINE_ACTIVATION:
    wprintf(L"Callback hr = E_DRM_NEEDS_MACHINE_ACTIVATION\n");
    break;
  case E_DRM_NEEDS_GROUPIDENTITY_ACTIVATION:
    wprintf(L"Callback hr = E_DRM_NEEDS_GROUPIDENTITY_ACTIVATION\n");
    break;
  case E_DRM_REQUEST_DENIED:
    wprintf(L"Callback hr = E_DRM_REQUEST_DENIED\n");
    break;
  case E_DRM_INVALID_EMAIL:
    wprintf(L"Callback hr = E_DRM_INVALID_EMAIL\n");
    break;
  case E_DRM_SERVICE_GONE:
    wprintf(L"Callback hr = E_DRM_SERVICE_GONE\n");
    break;
  case E_DRM_SERVICE_MOVED:
    wprintf(L"Callback hr = E_DRM_SERVICE_MOVED\n");
    break;
  case E_DRM_VALIDITYTIME_VIOLATION:
    wprintf(L"Callback hr = E_DRM_VALIDITYTIME_VIOLATION\n");
    break;
  case S_DRM_REQUEST_PREPARED:
    wprintf(L"Callback hr = S_DRM_REQUEST_PREPARED\n");
    break;
  case E_DRM_NO_LICENSE:
    wprintf(L"Callback hr = E_DRM_NO_LICENSE\n");
    break;
  case E_DRM_SERVICE_NOT_FOUND:
    wprintf(L"Callback hr = E_DRM_SERVICE_NOT_FOUND\n");
    break;
  case E_DRM_LICENSEACQUISITIONFAILED:
    wprintf(L"Callback hr = E_DRM_LICENSEACQUISITIONFAILED\n");
    break;
  default:
    wprintf(L"Default callback hr = 0x%x\n", hr);
    if (pContext->hEvent)
    {
      SetEvent((HANDLE)pContext->hEvent);
    }
    break;
  }
  return S_OK;
}
```



## Related topics

<dl> <dt>

[Revocation Code Example](revocation-code-example.md)
</dt> <dt>

[Revoking a Certificate](revoking-a-certificate.md)
</dt> </dl>

 

 



