---
title: Create client applications
description: How to use the Windows Biometric Framework API to create client applications.
ms.assetid: 7bef37ee-7685-4aaa-8dad-3c5a9c335eca
keywords:
- Windows Biometric Framework API Windows Biometric Framework API , client applications
ms.topic: article
ms.date: 05/31/2018
---

# Create client applications

The following topics discuss how to use the Windows Biometric Framework API to create client applications that use private sensor pools.

## Enroll biometric information

The following code examples show how to enroll a biometric template in the system pool.

### Synchronous enrollment

The following code example:

-   Calls [**WinBioOpenSession**](/windows/desktop/api/Winbio/nf-winbio-winbioopensession) to open a biometric session and connect to the system pool.
-   Calls [**WinBioLocateSensor**](/windows/desktop/api/Winbio/nf-winbio-winbiolocatesensor) to locate a biometric unit.
-   Calls [**WinBioEnrollBegin**](/windows/desktop/api/Winbio/nf-winbio-winbioenrollbegin) to start the enrollment sequence.
-   Calls [**WinBioEnrollCapture**](/windows/desktop/api/Winbio/nf-winbio-winbioenrollcapture) to process multiple finger swipes on the sensor.
-   Calls [**WinBioEnrollCommit**](/windows/desktop/api/Winbio/nf-winbio-winbioenrollcommit) to save the template in the store.

To compile this sample, link to the Winbio.lib static library and include the following header files:

-   Windows.h
-   Stdio.h
-   Conio.h
-   Winbio.h


```C++
HRESULT EnrollSysPool(
                      BOOL discardEnrollment, 
                      WINBIO_BIOMETRIC_SUBTYPE subFactor)
{
    HRESULT hr = S_OK;
    WINBIO_IDENTITY identity = {0};
    WINBIO_SESSION_HANDLE sessionHandle = NULL;
    WINBIO_UNIT_ID unitId = 0;
    WINBIO_REJECT_DETAIL rejectDetail = 0;
    BOOLEAN isNewTemplate = TRUE;

    // Connect to the system pool. 
    hr = WinBioOpenSession( 
            WINBIO_TYPE_FINGERPRINT,    // Service provider
            WINBIO_POOL_SYSTEM,         // Pool type
            WINBIO_FLAG_DEFAULT,        // Configuration and access
            NULL,                       // Array of biometric unit IDs
            0,                          // Count of biometric unit IDs
            NULL,                       // Database ID
            &sessionHandle              // [out] Session handle
            );
    if (FAILED(hr))
    {
        wprintf_s(L"\n WinBioOpenSession failed. ");
        wprintf_s(L"hr = 0x%x\n", hr);
        goto e_Exit;
    }

    // Locate a sensor.
    wprintf_s(L"\n Swipe your finger on the sensor...\n");
    hr = WinBioLocateSensor( sessionHandle, &unitId);
    if (FAILED(hr))
    {
        wprintf_s(L"\n WinBioLocateSensor failed. hr = 0x%x\n", hr);
        goto e_Exit;
    }

    // Begin the enrollment sequence. 
    wprintf_s(L"\n Starting enrollment sequence...\n");
    hr = WinBioEnrollBegin(
            sessionHandle,      // Handle to open biometric session
            subFactor,          // Finger to create template for
            unitId              // Biometric unit ID
            );
    if (FAILED(hr))
    {
        wprintf_s(L"\n WinBioEnrollBegin failed. hr = 0x%x\n", hr);
        goto e_Exit;
    }

    // Capture enrollment information by swiping the sensor with
    // the finger identified by the subFactor argument in the 
    // WinBioEnrollBegin function.
    for (int swipeCount = 1;; ++swipeCount)
    {
        wprintf_s(L"\n Swipe the sensor to capture %s sample.",
                 (swipeCount == 1)?L"the first":L"another");

        hr = WinBioEnrollCapture(
                sessionHandle,  // Handle to open biometric session
                &rejectDetail   // [out] Failure information
                );

        wprintf_s(L"\n Sample %d captured from unit number %d.", 
                  swipeCount, 
                  unitId);

        if (hr == WINBIO_I_MORE_DATA)
        {
            wprintf_s(L"\n    More data required.\n");
            continue;
        }
        if (FAILED(hr))
        {
            if (hr == WINBIO_E_BAD_CAPTURE)
            {
                wprintf_s(L"\n  Error: Bad capture; reason: %d", 
                          rejectDetail);
                continue;
            }
            else
            {
                wprintf_s(L"\n WinBioEnrollCapture failed. hr = 0x%x", hr);
                goto e_Exit;
            }
        }
        else
        {
            wprintf_s(L"\n    Template completed.\n");
            break;
        }
    }

    // Discard the enrollment if the appropriate flag is set.
    // Commit the enrollment if it is not discarded.
    if (discardEnrollment == TRUE)
    {
        wprintf_s(L"\n Discarding enrollment...\n\n");
        hr = WinBioEnrollDiscard( sessionHandle );
        if (FAILED(hr))
        {
            wprintf_s(L"\n WinBioLocateSensor failed. hr = 0x%x\n", hr);
        }
        goto e_Exit;    
    }
    else
    {
        wprintf_s(L"\n Committing enrollment...\n");
        hr = WinBioEnrollCommit( 
                sessionHandle,      // Handle to open biometric session
                &identity,          // WINBIO_IDENTITY object for the user
                &isNewTemplate);    // Is this a new template

        if (FAILED(hr))
        {
            wprintf_s(L"\n WinBioEnrollCommit failed. hr = 0x%x\n", hr);
            goto e_Exit;
        }
    }


e_Exit:
    if (sessionHandle != NULL)
    {
        WinBioCloseSession(sessionHandle);
        sessionHandle = NULL;
    }

    wprintf_s(L" Press any key to continue...");
    _getch();

    return hr;
}

```



### Asynchronous enrollment

The following code example:

-   Calls [**WinBioOpenSession**](/windows/desktop/api/Winbio/nf-winbio-winbioopensession) to open a biometric session and connect to the system pool.
-   Calls [**WinBioLocateSensor**](/windows/desktop/api/Winbio/nf-winbio-winbiolocatesensor) to locate a biometric unit.
-   Calls [**WinBioEnrollBegin**](/windows/desktop/api/Winbio/nf-winbio-winbioenrollbegin) to start the enrollment sequence.
-   Calls [**WinBioEnrollCaptureWithCallback**](/windows/desktop/api/Winbio/nf-winbio-winbioenrollcapturewithcallback) to process multiple finger swipes. This function is asynchronous and uses a custom callback function to continue processing on a separate thread. An example callback function is included below.
-   Calls [**WinBioWait**](/windows/desktop/api/Winbio/nf-winbio-winbiowait) to wait for the asynchronous enrollment process to complete or be canceled.
-   Calls [**WinBioEnrollCommit**](/windows/desktop/api/Winbio/nf-winbio-winbioenrollcommit) to save the template.

Link to the Winbio.lib static library to compile this sample.


```C++
//------------------------------------------------------------------------
// EnrollSystemPoolWithCallback.cpp : Entry point for the application.
//
#include <windows.h>
#include <stdio.h>
#include <conio.h>
#include <winbio.h>


//------------------------------------------------------------------------
// Forward declarations.
//
HRESULT EnrollSysPoolWithCallback(
                      BOOL bCancel,
                      BOOL bDiscard,
                      WINBIO_BIOMETRIC_SUBTYPE subFactor);

VOID CALLBACK EnrollCaptureCallback(
                      __in_opt PVOID EnrollCallbackContext,
                      __in HRESULT OperationStatus,
                      __in WINBIO_REJECT_DETAIL RejectDetail);

typedef struct _ENROLL_CALLBACK_CONTEXT {
    WINBIO_SESSION_HANDLE SessionHandle;
    WINBIO_UNIT_ID UnitId;
    WINBIO_BIOMETRIC_SUBTYPE SubFactor;
} ENROLL_CALLBACK_CONTEXT, *PENROLL_CALLBACK_CONTEXT;

//------------------------------------------------------------------------
int wmain()
{
    HRESULT hr = S_OK;

    hr = EnrollSysPoolWithCallback(
                      FALSE, 
                      FALSE, 
                      WINBIO_ANSI_381_POS_RH_INDEX_FINGER);

    return 0;
}

//------------------------------------------------------------------------
// The following function enrolls a user's fingerprint in the system pool.
// The function calls WinBioEnrollCaptureWithCallback and waits for the
// asynchronous enrollment process to be completed or canceled.
//
HRESULT EnrollSysPoolWithCallback(
                      BOOL bCancel,
                      BOOL bDiscard,
                      WINBIO_BIOMETRIC_SUBTYPE subFactor)
{
    // Declare variables
    HRESULT hr = S_OK;
    WINBIO_IDENTITY identity = {0};
    WINBIO_SESSION_HANDLE sessionHandle = NULL;
    WINBIO_UNIT_ID unitId = 0;
    BOOLEAN isNewTemplate = TRUE;
    ENROLL_CALLBACK_CONTEXT callbackContext = {0};

    // Connect to the system pool. 
    hr = WinBioOpenSession( 
            WINBIO_TYPE_FINGERPRINT,    // Service provider
            WINBIO_POOL_SYSTEM,         // Pool type
            WINBIO_FLAG_DEFAULT,        // Configuration and access
            NULL,                       // Array of biometric unit IDs
            0,                          // Count of biometric unit IDs
            NULL,                       // Database ID
            &sessionHandle              // [out] Session handle
            );
    if (FAILED(hr))
    {
        wprintf_s(L"\n WinBioEnumBiometricUnits failed. ");
        wprintf_s(L"hr = 0x%x\n", hr);
        goto e_Exit;
    }

    // Locate the sensor.
    wprintf_s(L"\n Swipe your finger to locate the sensor...\n");
    hr = WinBioLocateSensor( sessionHandle, &unitId);
    if (FAILED(hr))
    {
        wprintf_s(L"\n WinBioLocateSensor failed. hr = 0x%x\n", hr);
        goto e_Exit;
    }

    // Begin the enrollment sequence. 
    hr = WinBioEnrollBegin(
            sessionHandle,      // Handle to open biometric session
            subFactor,          // Finger to create template for
            unitId              // Biometric unit ID
            );
    if (FAILED(hr))
    {
        wprintf_s(L"\n WinBioEnrollBegin failed. hr = 0x%x\n", hr);
        goto e_Exit;
    }

    // Set up the custom callback context structure.
    callbackContext.SessionHandle = sessionHandle;
    callbackContext.UnitId = unitId;
    callbackContext.SubFactor = subFactor;

    // Call WinBioEnrollCaptureWithCallback. This is an asynchronous
    // method that returns immediately.
    hr = WinBioEnrollCaptureWithCallback(
            sessionHandle,          // Handle to open biometric session
            EnrollCaptureCallback,  // Callback function
            &callbackContext        // Pointer to the custom context
            );
    if (FAILED(hr))
    {
        wprintf_s(L"\n WinBioEnrollCaptureWithCallback failed. ");
        wprintf_s(L"hr = 0x%x\n", hr);
        goto e_Exit;
    }
    wprintf_s(L"\n Swipe the sensor with the appropriate finger...\n");

    // Cancel the enrollment if the bCancel flag is set.
    if (bCancel)
    {
        wprintf_s(L"\n Starting CANCEL timer...\n");
        Sleep( 7000 );

        wprintf_s(L"\n Calling WinBioCancel\n");
        hr = WinBioCancel( sessionHandle );
        if (FAILED(hr))
        {
            wprintf_s(L"\n WinBioCancel failed. hr = 0x%x\n", hr);
            goto e_Exit;
        }
    }

    // Wait for the asynchronous enrollment process to complete
    // or be canceled.
    hr = WinBioWait( sessionHandle );
    if (FAILED(hr))
    {
        wprintf_s(L"\n WinBioWait failed. hr = 0x%x\n", hr);
    }

    // Discard the enrollment if the bDiscard flag is set.
    // Commit the enrollment if the flag is not set.
    if (bDiscard)
    {
        wprintf_s(L"\n Discarding enrollment...\n");
        hr = WinBioEnrollDiscard( sessionHandle );
        if (FAILED(hr))
        {
            wprintf_s(L"\n WinBioLocateSensor failed. ");
            wprintf_s(L"hr = 0x%x\n", hr);
        }
        goto e_Exit;    
    }
    else
    {
        wprintf_s(L"\n Committing enrollment...\n");
        hr = WinBioEnrollCommit( 
                sessionHandle,      // Handle to open biometric session
                &identity,          // WINBIO_IDENTITY object for the user
                &isNewTemplate);    // Is this a new template

        if (FAILED(hr))
        {
            wprintf_s(L"\n WinBioEnrollCommit failed. hr = 0x%x\n", hr);
            goto e_Exit;
        }
    }

e_Exit:
    if (sessionHandle != NULL)
    {
        WinBioCloseSession(sessionHandle);
        sessionHandle = NULL;
    }

    wprintf_s(L"\n Press any key to exit...");
    _getch();

    return hr;
}

//------------------------------------------------------------------------
// The following function is the callback for the Windows Biometric
// Framework WinBioEnrollCaptureWithCallback() function. 
//
VOID CALLBACK EnrollCaptureCallback(
    __in_opt PVOID EnrollCallbackContext,
    __in HRESULT OperationStatus,
    __in WINBIO_REJECT_DETAIL RejectDetail
    )
{
    // Declare variables.
    HRESULT hr = S_OK; 
    static SIZE_T swipeCount = 1;

    PENROLL_CALLBACK_CONTEXT callbackContext = 
        (PENROLL_CALLBACK_CONTEXT)EnrollCallbackContext;

    wprintf_s(L"\n EnrollCaptureCallback executing\n");
    wprintf_s(L"\n Sample %d captured", swipeCount++);

    // The capture was not acceptable or the enrollment operation
    // failed.
    if (FAILED(OperationStatus))
    {
        if (OperationStatus == WINBIO_E_BAD_CAPTURE)
        {
            wprintf_s(L"\n Bad capture; reason: %d\n", RejectDetail);
            wprintf_s(L"\n Swipe your finger to capture another sample.\n");

            // Try again.
            hr = WinBioEnrollCaptureWithCallback(
                    callbackContext->SessionHandle, // Open session handle
                    EnrollCaptureCallback,          // Callback function
                    EnrollCallbackContext           // Callback context
                    );
            if (FAILED(hr))
            {
                wprintf_s(L"WinBioEnrollCaptureWithCallback failed.");
                wprintf_s(L"hr = 0x%x\n", hr);
            }
        }
        else
        {
            wprintf_s(L"EnrollCaptureCallback failed.");
            wprintf_s(L"OperationStatus = 0x%x\n", OperationStatus);
        }
        goto e_Exit;
    }

    // The enrollment operation requires more fingerprint swipes.
    // This is normal and depends on your hardware. Typically, at least
    // three swipes are required.
    if (OperationStatus == WINBIO_I_MORE_DATA)
    {
        wprintf_s(L"\n More data required.");
        wprintf_s(L"\n Swipe your finger on the sensor again.");

        hr = WinBioEnrollCaptureWithCallback(
                callbackContext->SessionHandle,
                EnrollCaptureCallback,
                EnrollCallbackContext
                );
        if (FAILED(hr))
        {
            wprintf_s(L"WinBioEnrollCaptureWithCallback failed. ");
            wprintf_s(L"hr = 0x%x\n", hr);
        }
        goto e_Exit;
    }

    wprintf_s(L"\n Template completed\n");

e_Exit:

    return;
}

```



## Locate biometric units

The following code examples show how to locate an installed biometric unit.

### Locate biometric units synchronously

The following code example:

-   Calls [**WinBioOpenSession**](/windows/desktop/api/Winbio/nf-winbio-winbioopensession) to open a biometric session and connect to the system pool.
-   Calls [**WinBioLocateSensor**](/windows/desktop/api/Winbio/nf-winbio-winbiolocatesensor) to locate a biometric unit.

To compile this sample, link to the Winbio.lib static library and include the following header files:

-   Windows.h
-   Stdio.h
-   Conio.h
-   Winbio.h


```C++
HRESULT LocateSensor( )
{
    HRESULT hr = S_OK;
    WINBIO_SESSION_HANDLE sessionHandle = NULL;
    WINBIO_UNIT_ID unitId = 0;

    // Connect to the system pool. 
    hr = WinBioOpenSession( 
            WINBIO_TYPE_FINGERPRINT,    // Service provider
            WINBIO_POOL_SYSTEM,         // Pool type
            WINBIO_FLAG_DEFAULT,        // Configuration and access
            NULL,                       // Array of biometric unit IDs
            0,                          // Count of biometric unit IDs
            NULL,                       // Database ID
            &sessionHandle              // [out] Session handle
            );
    if (FAILED(hr))
    {
        wprintf_s(L"\n WinBioEnumBiometricUnits failed. hr = 0x%x\n", hr);
        goto e_Exit;
    }

    // Locate the sensor.
    wprintf_s(L"\n Tap the sensor once...\n");
    hr = WinBioLocateSensor( sessionHandle, &unitId);
    if (FAILED(hr))
    {
        wprintf_s(L"\n WinBioLocateSensor failed. hr = 0x%x\n", hr);
        goto e_Exit;
    }
    wprintf_s(L"\n Sensor located successfully. ");
    wprintf_s(L"\n Unit ID = %d \n", unitId);

e_Exit:
    if (sessionHandle != NULL)
    {
        WinBioCloseSession(sessionHandle);
        sessionHandle = NULL;
    }

    wprintf_s(L"\n Hit any key to exit...");
    _getch();

    return hr;
}

```



### Locate biometric units asynchronously

The following code example:

-   Calls [**WinBioOpenSession**](/windows/desktop/api/Winbio/nf-winbio-winbioopensession) to open a biometric session and connect to the system pool.
-   Calls [**WinBioLocateSensorWithCallback**](/windows/desktop/api/Winbio/nf-winbio-winbiolocatesensorwithcallback) to locate a biometric sensor. This is an asynchronous function that configures the biometric subsystem to locate the sensor on another thread. Output from the biometric subsystem is sent to a custom callback function, here called LocateSensorCallback.
-   Calls [**WinBioWait**](/windows/desktop/api/Winbio/nf-winbio-winbiowait) to wait for the asynchronous process to complete or be canceled.

To compile this sample, link to the Winbio.lib static library and include the following header files:

-   Windows.h
-   Stdio.h
-   Conio.h
-   Winbio.h


```C++
HRESULT LocateSensorWithCallback(BOOL bCancel)
{
    HRESULT hr = S_OK;
    WINBIO_SESSION_HANDLE sessionHandle = NULL;
    WINBIO_UNIT_ID unitId = 0;

    // Connect to the system pool. 
    hr = WinBioOpenSession( 
            WINBIO_TYPE_FINGERPRINT,    // Service provider
            WINBIO_POOL_SYSTEM,         // Pool type
            WINBIO_FLAG_DEFAULT,        // Configuration and access
            NULL,                       // Array of biometric unit IDs
            0,                          // Count of biometric unit IDs
            NULL,                       // Database ID
            &sessionHandle              // [out] Session handle
            );
    if (FAILED(hr))
    {
        wprintf_s(L"\n WinBioOpenSession failed. hr = 0x%x\n", hr);
        goto e_Exit;
    }

    wprintf_s(L"\n Calling WinBioLocateSensorWithCallback.");
    hr = WinBioLocateSensorWithCallback(
                sessionHandle,          // Open biometric session
                LocateSensorCallback,   // Callback function
                NULL                    // Optional context
                );
    if (FAILED(hr))
    {
        wprintf_s(L"\n WinBioLocateSensorWithCallback failed.");
        wprintf_s(L"hr = 0x%x\n", hr);
        goto e_Exit;
    }
    wprintf_s(L"\n Swipe the sensor ...\n");

    // Cancel the identification if the bCancel flag is set.
    if (bCancel)
    {
        wprintf_s(L"\n Starting CANCEL timer...\n");
        Sleep( 7000 );

        wprintf_s(L"\n Calling WinBioCancel\n");
        hr = WinBioCancel( sessionHandle );
        if (FAILED(hr))
        {
            wprintf_s(L"\n WinBioCancel failed. hr = 0x%x\n", hr);
            goto e_Exit;
        }
    }

    // Wait for the asynchronous identification process to complete 
    // or be canceled.
    hr = WinBioWait( sessionHandle );
    if (FAILED(hr))
    {
        wprintf_s(L"\n WinBioWait failed. hr = 0x%x\n", hr);
    }

e_Exit:

    if (sessionHandle != NULL)
    {
       wprintf_s(L"\n Closing the session.\n");

        hr = WinBioCloseSession(sessionHandle);
        if (FAILED(hr))
        {
            wprintf_s(L"\n WinBioCloseSession failed. hr = 0x%x\n", hr);
        }
        sessionHandle = NULL;
    }

    wprintf_s(L"\n Hit any key to exit...");
    _getch();

    return hr;
}

//------------------------------------------------------------------------
// The following function is the callback for 
// WinBioLocateSensorWithCallback. The function filters the response 
// from the biometric subsystem and writes a result to the console window.
// 
VOID CALLBACK LocateSensorCallback(
    __in_opt PVOID LocateCallbackContext,
    __in HRESULT OperationStatus,
    __in WINBIO_UNIT_ID UnitId
    )
{
    UNREFERENCED_PARAMETER(LocateCallbackContext);

    wprintf_s(L"\n LocateSensorCallback executing.");

    // A sensor could not be located.
    if (FAILED(OperationStatus))
    {
        wprintf_s(L"\n LocateSensorCallback failed.");
        wprintf_s(L"OperationStatus = 0x%x\n", OperationStatus);
    }
    // A sensor was located.
    else
    {
        wprintf_s(L"\n Selected unit ID: %d\n", UnitId);
    }
}

```



## Verify user identity

### Synchronous verification

The following code example:

-   Calls [**WinBioOpenSession**](/windows/desktop/api/Winbio/nf-winbio-winbioopensession) to open a biometric session and connect to the system pool.
-   Calls [**WinBioVerify**](/windows/desktop/api/Winbio/nf-winbio-winbioverify) to determine whether a biometric sample matches the logged on identity of the current user.

To compile this sample, link to the Winbio.lib static library and include the following header files:

-   Windows.h
-   Stdio.h
-   Conio.h
-   Winbio.h


```C++
HRESULT Verify(WINBIO_BIOMETRIC_SUBTYPE subFactor)
{
    HRESULT hr = S_OK;
    WINBIO_SESSION_HANDLE sessionHandle = NULL;
    WINBIO_UNIT_ID unitId = 0;
    WINBIO_REJECT_DETAIL rejectDetail = 0;
    WINBIO_IDENTITY identity = {0};
    BOOLEAN match = FALSE;

    // Find the identity of the user.
    hr = GetCurrentUserIdentity( &identity );
    if (FAILED(hr))
    {
        wprintf_s(L"\n User identity not found. hr = 0x%x\n", hr);
        goto e_Exit;
    }

    // Connect to the system pool. 
    hr = WinBioOpenSession( 
            WINBIO_TYPE_FINGERPRINT,    // Service provider
            WINBIO_POOL_SYSTEM,         // Pool type
            WINBIO_FLAG_DEFAULT,        // Configuration and access
            NULL,                       // Array of biometric unit IDs
            0,                          // Count of biometric unit IDs
            NULL,                       // Database ID
            &sessionHandle              // [out] Session handle
            );
    if (FAILED(hr))
    {
        wprintf_s(L"\n WinBioOpenSession failed. hr = 0x%x\n", hr);
        goto e_Exit;
    }

    // Verify a biometric sample.
    wprintf_s(L"\n Calling WinBioVerify - Swipe finger on sensor...\n");
    hr = WinBioVerify( 
            sessionHandle, 
            &identity, 
            subFactor, 
            &unitId, 
            &match,
            &rejectDetail
            );
    wprintf_s(L"\n Swipe processed - Unit ID: %d\n", unitId);
    if (FAILED(hr))
    {
        if (hr == WINBIO_E_NO_MATCH)
        {
            wprintf_s(L"\n- NO MATCH - identity verification failed.\n");
        }
        else if (hr == WINBIO_E_BAD_CAPTURE)
        {
            wprintf_s(L"\n- Bad capture; reason: %d\n", rejectDetail);
        }
        else
        {
        wprintf_s(L"\n WinBioVerify failed. hr = 0x%x\n", hr);
        }
        goto e_Exit;
    }
    wprintf_s(L"\n Fingerprint verified:\n", unitId);


e_Exit:
    if (sessionHandle != NULL)
    {
        WinBioCloseSession(sessionHandle);
        sessionHandle = NULL;
    }

    wprintf_s(L"\n Press any key to exit...");
    _getch();

    return hr;
}

//------------------------------------------------------------------------
// The following function retrieves the identity of the current user.
// This is a helper function and is not part of the Windows Biometric
// Framework API.
//
HRESULT GetCurrentUserIdentity(__inout PWINBIO_IDENTITY Identity)
{
    // Declare variables.
    HRESULT hr = S_OK;
    HANDLE tokenHandle = NULL;
    DWORD bytesReturned = 0;
    struct{
        TOKEN_USER tokenUser;
        BYTE buffer[SECURITY_MAX_SID_SIZE];
    } tokenInfoBuffer;

    // Zero the input identity and specify the type.
    ZeroMemory( Identity, sizeof(WINBIO_IDENTITY));
    Identity->Type = WINBIO_ID_TYPE_NULL;

    // Open the access token associated with the
    // current process
    if (!OpenProcessToken(
            GetCurrentProcess(),            // Process handle
            TOKEN_READ,                     // Read access only
            &tokenHandle))                  // Access token handle
    {
        DWORD win32Status = GetLastError();
        wprintf_s(L"Cannot open token handle: %d\n", win32Status);
        hr = HRESULT_FROM_WIN32(win32Status);
        goto e_Exit;
    }

    // Zero the tokenInfoBuffer structure.
    ZeroMemory(&tokenInfoBuffer, sizeof(tokenInfoBuffer));

    // Retrieve information about the access token. In this case,
    // retrieve a SID.
    if (!GetTokenInformation(
            tokenHandle,                    // Access token handle
            TokenUser,                      // User for the token
            &tokenInfoBuffer.tokenUser,     // Buffer to fill
            sizeof(tokenInfoBuffer),        // Size of the buffer
            &bytesReturned))                // Size needed
    {
        DWORD win32Status = GetLastError();
        wprintf_s(L"Cannot query token information: %d\n", win32Status);
        hr = HRESULT_FROM_WIN32(win32Status);
        goto e_Exit;
    }

    // Copy the SID from the tokenInfoBuffer structure to the
    // WINBIO_IDENTITY structure. 
    CopySid(
        SECURITY_MAX_SID_SIZE,
        Identity->Value.AccountSid.Data,
        tokenInfoBuffer.tokenUser.User.Sid
        );

    // Specify the size of the SID and assign WINBIO_ID_TYPE_SID
    // to the type member of the WINBIO_IDENTITY structure.
    Identity->Value.AccountSid.Size = GetLengthSid(tokenInfoBuffer.tokenUser.User.Sid);
    Identity->Type = WINBIO_ID_TYPE_SID;

e_Exit:

    if (tokenHandle != NULL)
    {
        CloseHandle(tokenHandle);
    }

    return hr;
}

```



### Asynchronous verification

The following code example:

-   Calls [**WinBioOpenSession**](/windows/desktop/api/Winbio/nf-winbio-winbioopensession) to open a biometric session and connect to the system pool.
-   Calls [**WinBioVerifyWithCallback**](/windows/desktop/api/Winbio/nf-winbio-winbioverifywithcallback) to determine whether a biometric sample matches the logged on identity of the current user. This is an asynchronous function that configures the biometric subsystem to verify the user on another thread. Output from the biometric subsystem is sent to a custom callback function, here called VerifyCallback.
-   Calls [**WinBioWait**](/windows/desktop/api/Winbio/nf-winbio-winbiowait) to wait for the asynchronous process to complete or be canceled.

To compile this sample, link to the Winbio.lib static library and include the following header files:

-   Windows.h
-   Stdio.h
-   Conio.h
-   Winbio.h


```C++
HRESULT VerifyWithCallback(BOOL bCancel, WINBIO_BIOMETRIC_SUBTYPE subFactor)
{
    // Declare variables.
    HRESULT hr = S_OK;
    WINBIO_SESSION_HANDLE sessionHandle = NULL;
    WINBIO_UNIT_ID unitId = 0;
    WINBIO_REJECT_DETAIL rejectDetail = 0;
    WINBIO_IDENTITY identity = {0};

    // Find the identity of the user.
    hr = GetCurrentUserIdentity( &identity );
    if (FAILED(hr))
    {
        wprintf_s(L"\n User identity not found. hr = 0x%x\n", hr);
        goto e_Exit;
    }

    // Connect to the system pool. 
    hr = WinBioOpenSession( 
            WINBIO_TYPE_FINGERPRINT,    // Service provider
            WINBIO_POOL_SYSTEM,         // Pool type
            WINBIO_FLAG_DEFAULT,        // Configuration and access
            NULL,                       // Array of biometric unit IDs
            0,                          // Count of biometric unit IDs
            NULL,                       // Database ID
            &sessionHandle              // [out] Session handle
            );
    if (FAILED(hr))
    {
        wprintf_s(L"\n WinBioOpenSession failed. hr = 0x%x\n", hr);
        goto e_Exit;
    }

    // Verify a biometric sample asynchronously.
    wprintf_s(L"\n Calling WinBioVerifyWithCallback.\n");
    hr = WinBioVerifyWithCallback(
            sessionHandle,              // Open session handle
            &identity,                  // User SID or GUID
            subFactor,                  // Sample sub-factor
            VerifyCallback,             // Callback function
            NULL                        // Optional context
            );
    if (FAILED(hr))
    {
        wprintf_s(L"\n WinBioVerifyWithCallback failed. hr = 0x%x\n", hr);
        goto e_Exit;
    }
    wprintf_s(L"\n Swipe the sensor ...\n");

    // Cancel the identification if the bCancel flag is set.
    if (bCancel)
    {
        wprintf_s(L"\n Starting CANCEL timer...\n");
        Sleep( 7000 );

        wprintf_s(L"\n Calling WinBioCancel\n");
        hr = WinBioCancel( sessionHandle );
        if (FAILED(hr))
        {
            wprintf_s(L"\n WinBioCancel failed. hr = 0x%x\n", hr);
            goto e_Exit;
        }
    }

    // Wait for the asynchronous identification process to complete 
    // or be canceled.
    hr = WinBioWait( sessionHandle );
    if (FAILED(hr))
    {
        wprintf_s(L"\n WinBioWait failed. hr = 0x%x\n", hr);
    }

e_Exit:
    if (sessionHandle != NULL)
    {
        WinBioCloseSession(sessionHandle);
        sessionHandle = NULL;
    }

    wprintf_s(L"\n Hit any key to continue...");
    _getch();

    return hr;
}

//------------------------------------------------------------------------
// The following function is the callback for WinBioVerifyWithCallback.
// The function filters the response from the biometric subsystem and 
// writes a result to the console window.
// 
VOID CALLBACK VerifyCallback(
  __in_opt PVOID VerifyCallbackContext,
  __in HRESULT OperationStatus,
  __in WINBIO_UNIT_ID UnitId,
  __in BOOLEAN Match,
  __in WINBIO_REJECT_DETAIL RejectDetail
  )
{
    UNREFERENCED_PARAMETER(VerifyCallbackContext);
    UNREFERENCED_PARAMETER(Match);

    wprintf_s(L"\n VerifyCallback executing");
    wprintf_s(L"\n Swipe processed for unit ID %d\n", UnitId);

    // The identity could not be verified.
    if (FAILED(OperationStatus))
    {
        wprintf_s(L"\n Verification failed for the following reason:");
        if (OperationStatus == WINBIO_E_NO_MATCH)
        {
            wprintf_s(L"\n No match.\n");
        }
        else if (OperationStatus == WINBIO_E_BAD_CAPTURE)
        {
            wprintf_s(L"\n Bad capture.\n ");
            wprintf_s(L"\n Bad capture; reason: %d\n", RejectDetail);
        }
        else
        {
            wprintf_s(L"VerifyCallback failed.");
            wprintf_s(L"OperationStatus = 0x%x\n", OperationStatus); 
        }
        goto e_Exit;
    }

    // The user identity was verified.
    wprintf_s(L"\n Fingerprint verified:\n");

e_Exit:
    return;
}

//------------------------------------------------------------------------
// The following function retrieves the identity of the current user.
// This is a helper function and is not part of the Windows Biometric
// Framework API.
//
HRESULT GetCurrentUserIdentity(__inout PWINBIO_IDENTITY Identity)
{
    // Declare variables.
    HRESULT hr = S_OK;
    HANDLE tokenHandle = NULL;
    DWORD bytesReturned = 0;
    struct{
        TOKEN_USER tokenUser;
        BYTE buffer[SECURITY_MAX_SID_SIZE];
    } tokenInfoBuffer;

    // Zero the input identity and specify the type.
    ZeroMemory( Identity, sizeof(WINBIO_IDENTITY));
    Identity->Type = WINBIO_ID_TYPE_NULL;

    // Open the access token associated with the
    // current process
    if (!OpenProcessToken(
            GetCurrentProcess(),            // Process handle
            TOKEN_READ,                     // Read access only
            &tokenHandle))                  // Access token handle
    {
        DWORD win32Status = GetLastError();
        wprintf_s(L"Cannot open token handle: %d\n", win32Status);
        hr = HRESULT_FROM_WIN32(win32Status);
        goto e_Exit;
    }

    // Zero the tokenInfoBuffer structure.
    ZeroMemory(&tokenInfoBuffer, sizeof(tokenInfoBuffer));

    // Retrieve information about the access token. In this case,
    // retrieve a SID.
    if (!GetTokenInformation(
            tokenHandle,                    // Access token handle
            TokenUser,                      // User for the token
            &tokenInfoBuffer.tokenUser,     // Buffer to fill
            sizeof(tokenInfoBuffer),        // Size of the buffer
            &bytesReturned))                // Size needed
    {
        DWORD win32Status = GetLastError();
        wprintf_s(L"Cannot query token information: %d\n", win32Status);
        hr = HRESULT_FROM_WIN32(win32Status);
        goto e_Exit;
    }

    // Copy the SID from the tokenInfoBuffer structure to the
    // WINBIO_IDENTITY structure. 
    CopySid(
        SECURITY_MAX_SID_SIZE,
        Identity->Value.AccountSid.Data,
        tokenInfoBuffer.tokenUser.User.Sid
        );

    // Specify the size of the SID and assign WINBIO_ID_TYPE_SID
    // to the type member of the WINBIO_IDENTITY structure.
    Identity->Value.AccountSid.Size = GetLengthSid(tokenInfoBuffer.tokenUser.User.Sid);
    Identity->Type = WINBIO_ID_TYPE_SID;

e_Exit:

    if (tokenHandle != NULL)
    {
        CloseHandle(tokenHandle);
    }

    return hr;
}

```



## Manage credentials

The credential provider and the credential manager are components in the Windows Biometric Framework. The provider retrieves user credentials from the secure store and responds to logon, unlock, password change, and UAC elevation requests. It also responds during a fast user switch to logon the new user. The manager maps logon credentials to biometric identities and securely stores the credentials. Mappings are typically created by third party enrollment applications during biometric enrollment, but they can also be created by the Windows biometric credential provider during logon if the enrolled user attempts to authenticate biometrically but is either not enrolled or the credentials do not match those in the secure store.

### Credential Manager API Guidelines

-   Credentials cannot be stored, queried, or deleted for the Guest or Built-in Administrator accounts or any non-interactive accounts such as LocalSystem, LocalService, or NetworkService.
-   All functions return an **HRESULT** error code that may be a common error code such as **E\_ACCESSDENIED** or an error specific to the credential manager such as **WINBIO\_E\_UNKNOWN\_ID**.
-   If appropriate, E\_ACCESSDENIED is returned before more specific error codes such as SEC\_E\_LOGON\_DENIED or WINBIO\_E\_UNKNOWN\_ID are returned.
-   Users whose privileges have not been elevated can set, query, or remove credentials for only their own account. Elevated callers can query credential state and remove credentials for other users.
-   All functions will fail and return WINBIO\_E\_CRED\_PROV\_DISABLED:
    -   For all users when the credential provider is not enabled system wide.
    -   For domain users when the provider is not enabled for domain use.
-   An event notice is generated when a credential is added or removed.

### Set a credential

The following code example:

-   Calls GetCurrentUserIdentity to retrieve a [**WINBIO\_IDENTITY**](winbio-identity.md) object for the current user. GetCurrentUserIdentity is a helper function and is not part of the Windows Biometric Framework.
-   Calls the GetCredentials helper function to retrieve a byte array that contains authentication information. GetCredentials displays a dialog box that prompts the user for credentials.
-   Calls [**WinBioSetCredential**](/windows/desktop/api/Winbio/nf-winbio-winbiosetcredential) to save the credentials in the store.

To compile this function link to the Winbio.lib static library and include the following header files:

-   Windows.h
-   Wincred.h
-   Stdio.h
-   Conio.h
-   Winbio.h


```C++
HRESULT SetCredential()
{
    // Declare variables.
    HRESULT hr = S_OK;
    ULONG   ulAuthPackage = 0;
    PVOID   pvAuthBlob = NULL;
    ULONG   cbAuthBlob = 0;
    WINBIO_IDENTITY identity;
    PSID pSid = NULL;

    // Find the identity of the user.
    wprintf_s(L"\n Finding user identity.\n");
    hr = GetCurrentUserIdentity( &identity );
    if (FAILED(hr))
    {
        wprintf_s(L"\n User identity not found. hr = 0x%x\n", hr);
        return hr;
    }

    // Set a pointer to the security descriptor for the user.
    pSid = identity.Value.AccountSid.Data;

    // Retrieve a byte array that contains credential information.
    hr = GetCredentials(pSid, &pvAuthBlob, &cbAuthBlob);
    if (FAILED(hr))
    {
        wprintf_s(L"\n GetCredentials failed. hr = 0x%x\n", hr);
        goto e_Exit;
    }

    // Set the credentials.
    hr = WinBioSetCredential(
            WINBIO_CREDENTIAL_PASSWORD,     // Type of credential.
            (PUCHAR)pvAuthBlob,             // Credentials byte array
            cbAuthBlob,                     // Size of credentials
            WINBIO_PASSWORD_PACKED);        // Credentials format

    if (FAILED(hr))
    {
        wprintf_s(L"\n WinBioSetCredential failed. hr = 0x%x\n", hr);
        goto e_Exit;
    }
    wprintf_s(L"\n Credentials successfully set.\n");

e_Exit:
    // Delete the authentication byte array.
    if (NULL != pvAuthBlob)
    {
        SecureZeroMemory(pvAuthBlob, cbAuthBlob);
        CoTaskMemFree(pvAuthBlob);
        pvAuthBlob = NULL;
    }

    wprintf_s(L"\n Press any key to exit...");
    _getch();

    return hr;


}

//------------------------------------------------------------------------
// The following function displays a dialog box to prompt a user
// for credentials.
//
HRESULT GetCredentials(PSID pSid, PVOID* ppvAuthBlob, ULONG* pcbAuthBlob)
{
    HRESULT hr = S_OK;
    DWORD   dwResult;
    WCHAR   szUsername[MAX_PATH] = {0};
    DWORD   cchUsername = ARRAYSIZE(szUsername);
    WCHAR   szPassword[MAX_PATH] = {0};
    WCHAR   szDomain[MAX_PATH] = {0};
    DWORD   cchDomain = ARRAYSIZE(szDomain);
    WCHAR   szDomainAndUser[MAX_PATH] = {0};
    DWORD   cchDomainAndUser = ARRAYSIZE(szDomainAndUser);
    PVOID   pvInAuthBlob = NULL;
    ULONG   cbInAuthBlob = 0;
    PVOID   pvAuthBlob = NULL;
    ULONG   cbAuthBlob = 0;
    CREDUI_INFOW ui;
    ULONG   ulAuthPackage = 0;
    BOOL    fSave = FALSE;

    static const WCHAR WINBIO_CREDPROV_TEST_PASSWORD_PROMPT_MESSAGE[] =
           L"Enter your current password to enable biometric logon.";

    static const WCHAR WINBIO_CREDPROV_TEST_PASSWORD_PROMPT_CAPTION[] =
           L"Biometric Log On Enrollment";

    if (NULL == pSid || NULL == ppvAuthBlob || NULL == pcbAuthBlob)
    {
        return E_INVALIDARG;
    }

    // Retrieve the user name and domain name.
    SID_NAME_USE    SidUse;
    DWORD           cchTmpUsername = cchUsername;
    DWORD           cchTmpDomain = cchDomain;

    if (!LookupAccountSidW(
              NULL,             // Local computer
              pSid,             // Security identifier for user
              szUsername,       // User name
              &cchTmpUsername,  // Size of user name
              szDomain,         // Domain name
              &cchTmpDomain,    // Size of domain name
              &SidUse))         // Account type
    {
        dwResult = GetLastError();
        hr = HRESULT_FROM_WIN32(dwResult);
        wprintf_s(L"\n LookupAccountSidLocalW failed: hr = 0x%x\n", hr);
        return hr;
    }

    // Combine the domain and user names.
    swprintf_s(
        szDomainAndUser, 
        cchDomainAndUser, 
        L"%s\\%s", 
        szDomain, 
        szUsername);

    // Call CredPackAuthenticationBufferW once to determine the size,
    // in bytes, of the authentication buffer.
    if (!CredPackAuthenticationBufferW(
              0,                // Reserved
              szDomainAndUser,  // Domain\User name
              szPassword,       // User Password
              NULL,             // Packed credentials
              &cbInAuthBlob)    // Size, in bytes, of credentials
        && GetLastError() != ERROR_INSUFFICIENT_BUFFER)
        {
            dwResult = GetLastError();
            hr = HRESULT_FROM_WIN32(dwResult);
            wprintf_s(L"\n CredPackAuthenticationBufferW (1) failed: ");
            wprintf_s(L"hr = 0x%x\n", hr);
        }

    // Allocate memory for the input buffer.
    pvInAuthBlob = CoTaskMemAlloc(cbInAuthBlob);
    if (!pvInAuthBlob)
    {
        cbInAuthBlob = 0;
        wprintf_s(L"\n CoTaskMemAlloc() Out of memory.\n");
        return HRESULT_FROM_WIN32(ERROR_OUTOFMEMORY);
    }

    // Call CredPackAuthenticationBufferW again to retrieve the
    // authentication buffer.
    if (!CredPackAuthenticationBufferW(
              0,
              szDomainAndUser,
              szPassword,
              (PBYTE)pvInAuthBlob,
              &cbInAuthBlob))
    {
        dwResult = GetLastError();
        hr = HRESULT_FROM_WIN32(dwResult);
        wprintf_s(L"\n CredPackAuthenticationBufferW (2) failed: ");
        wprintf_s(L"hr = 0x%x\n", hr);
        goto e_Exit;
    }

    // Display a dialog box to request credentials.
    ui.cbSize = sizeof(ui);
    ui.hwndParent = GetConsoleWindow();
    ui.pszMessageText = WINBIO_CREDPROV_TEST_PASSWORD_PROMPT_MESSAGE;
    ui.pszCaptionText = WINBIO_CREDPROV_TEST_PASSWORD_PROMPT_CAPTION;
    ui.hbmBanner = NULL;

    dwResult = CredUIPromptForWindowsCredentialsW(
                   &ui,             // Customizing information
                   0,               // Error code to display
                   &ulAuthPackage,  // Authorization package
                   pvInAuthBlob,    // Credential byte array
                   cbInAuthBlob,    // Size of credential input buffer
                   &pvAuthBlob,     // Output credential byte array
                   &cbAuthBlob,     // Size of credential byte array
                   &fSave,          // Select the save check box.
                   CREDUIWIN_IN_CRED_ONLY |
                   CREDUIWIN_ENUMERATE_CURRENT_USER
                   );
    if (dwResult != NO_ERROR)
    {
        hr = HRESULT_FROM_WIN32(dwResult);
        wprintf_s(L"\n CredUIPromptForWindowsCredentials failed: ");
        wprintf_s(L"0x%08x\n", dwResult);
        goto e_Exit;
    }

    *ppvAuthBlob = pvAuthBlob;
    *pcbAuthBlob = cbAuthBlob;

e_Exit:
    // Delete the input authentication byte array.
    if (pvInAuthBlob)
    {
        SecureZeroMemory(pvInAuthBlob, cbInAuthBlob);
        CoTaskMemFree(pvInAuthBlob);
        pvInAuthBlob = NULL;
    };

    return hr;
}


//------------------------------------------------------------------------
// The following function retrieves the identity of the current user.
// This is a helper function and is not part of the Windows Biometric
// Framework API.
//
HRESULT GetCurrentUserIdentity(__inout PWINBIO_IDENTITY Identity)
{
    // Declare variables.
    HRESULT hr = S_OK;
    HANDLE tokenHandle = NULL;
    DWORD bytesReturned = 0;
    struct{
        TOKEN_USER tokenUser;
        BYTE buffer[SECURITY_MAX_SID_SIZE];
    } tokenInfoBuffer;

    // Zero the input identity and specify the type.
    ZeroMemory( Identity, sizeof(WINBIO_IDENTITY));
    Identity->Type = WINBIO_ID_TYPE_NULL;

    // Open the access token associated with the
    // current process
    if (!OpenProcessToken(
            GetCurrentProcess(),            // Process handle
            TOKEN_READ,                     // Read access only
            &tokenHandle))                  // Access token handle
    {
        DWORD win32Status = GetLastError();
        wprintf_s(L"Cannot open token handle: %d\n", win32Status);
        hr = HRESULT_FROM_WIN32(win32Status);
        goto e_Exit;
    }

    // Zero the tokenInfoBuffer structure.
    ZeroMemory(&tokenInfoBuffer, sizeof(tokenInfoBuffer));

    // Retrieve information about the access token. In this case,
    // retrieve a SID.
    if (!GetTokenInformation(
            tokenHandle,                    // Access token handle
            TokenUser,                      // User for the token
            &tokenInfoBuffer.tokenUser,     // Buffer to fill
            sizeof(tokenInfoBuffer),        // Size of the buffer
            &bytesReturned))                // Size needed
    {
        DWORD win32Status = GetLastError();
        wprintf_s(L"Cannot query token information: %d\n", win32Status);
        hr = HRESULT_FROM_WIN32(win32Status);
        goto e_Exit;
    }

    // Copy the SID from the tokenInfoBuffer structure to the
    // WINBIO_IDENTITY structure. 
    CopySid(
        SECURITY_MAX_SID_SIZE,
        Identity->Value.AccountSid.Data,
        tokenInfoBuffer.tokenUser.User.Sid
        );

    // Specify the size of the SID and assign WINBIO_ID_TYPE_SID
    // to the type member of the WINBIO_IDENTITY structure.
    Identity->Value.AccountSid.Size = GetLengthSid(tokenInfoBuffer.tokenUser.User.Sid);
    Identity->Type = WINBIO_ID_TYPE_SID;

e_Exit:

    if (tokenHandle != NULL)
    {
        CloseHandle(tokenHandle);
    }

    return hr;
}

```



### Remove a credential

The following code example:

-   Calls GetCurrentUserIdentity to retrieve a [**WINBIO\_IDENTITY**](winbio-identity.md) object for the current user. GetCurrentUserIdentity is a helper function and is not part of the Windows Biometric Framework.
-   Calls [**WinBioRemoveCredential**](/windows/desktop/api/Winbio/nf-winbio-winbioremovecredential) to delete the credentials from the store.

To compile this function link to the Winbio.lib static library and include the following header files:

-   Windows.h
-   Stdio.h
-   Conio.h
-   Winbio.h


```C++
HRESULT RemoveCredential()
{
    HRESULT hr = S_OK;
    WINBIO_IDENTITY identity;

    // Find the identity of the user.
    wprintf_s(L"\n Finding user identity.\n");
    hr = GetCurrentUserIdentity( &identity );
    if (FAILED(hr))
    {
        wprintf(L"\n User identity not found. hr = 0x%x\n", hr);
        goto e_Exit;
    }

    // Remove the user credentials.
    hr = WinBioRemoveCredential(identity, WINBIO_CREDENTIAL_PASSWORD);
    if (FAILED(hr)) 
    {
        wprintf(L"\n WinBioRemoveCredential failed. hr = 0x%x\n", hr);
        goto e_Exit;
    }

    wprintf_s(L"\n User credentials successfully removed.\n");

e_Exit:

    wprintf_s(L"\n Press any key to exit...");
    _getch();

    return hr;
}

//------------------------------------------------------------------------
// The following function retrieves the identity of the current user.
// This is a helper function and is not part of the Windows Biometric
// Framework API.
//
HRESULT GetCurrentUserIdentity(__inout PWINBIO_IDENTITY Identity)
{
    // Declare variables.
    HRESULT hr = S_OK;
    HANDLE tokenHandle = NULL;
    DWORD bytesReturned = 0;
    struct{
        TOKEN_USER tokenUser;
        BYTE buffer[SECURITY_MAX_SID_SIZE];
    } tokenInfoBuffer;

    // Zero the input identity and specify the type.
    ZeroMemory( Identity, sizeof(WINBIO_IDENTITY));
    Identity->Type = WINBIO_ID_TYPE_NULL;

    // Open the access token associated with the
    // current process
    if (!OpenProcessToken(
            GetCurrentProcess(),            // Process handle
            TOKEN_READ,                     // Read access only
            &tokenHandle))                  // Access token handle
    {
        DWORD win32Status = GetLastError();
        wprintf_s(L"Cannot open token handle: %d\n", win32Status);
        hr = HRESULT_FROM_WIN32(win32Status);
        goto e_Exit;
    }

    // Zero the tokenInfoBuffer structure.
    ZeroMemory(&tokenInfoBuffer, sizeof(tokenInfoBuffer));

    // Retrieve information about the access token. In this case,
    // retrieve a SID.
    if (!GetTokenInformation(
            tokenHandle,                    // Access token handle
            TokenUser,                      // User for the token
            &tokenInfoBuffer.tokenUser,     // Buffer to fill
            sizeof(tokenInfoBuffer),        // Size of the buffer
            &bytesReturned))                // Size needed
    {
        DWORD win32Status = GetLastError();
        wprintf_s(L"Cannot query token information: %d\n", win32Status);
        hr = HRESULT_FROM_WIN32(win32Status);
        goto e_Exit;
    }

    // Copy the SID from the tokenInfoBuffer structure to the
    // WINBIO_IDENTITY structure. 
    CopySid(
        SECURITY_MAX_SID_SIZE,
        Identity->Value.AccountSid.Data,
        tokenInfoBuffer.tokenUser.User.Sid
        );

    // Specify the size of the SID and assign WINBIO_ID_TYPE_SID
    // to the type member of the WINBIO_IDENTITY structure.
    Identity->Value.AccountSid.Size = GetLengthSid(tokenInfoBuffer.tokenUser.User.Sid);
    Identity->Type = WINBIO_ID_TYPE_SID;

e_Exit:

    if (tokenHandle != NULL)
    {
        CloseHandle(tokenHandle);
    }

    return hr;
}

```



 

 




