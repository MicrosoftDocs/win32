---
title: Displaying the Status of an Event Collector Subscription
description: You can display the status of an Event Collector subscription. The status includes the availability of the subscription, the last error that occurred for the subscription, the time of the last error, and the next time the subscription will be retried.
ms.assetid: e1c3c3ed-2f7c-433d-a51d-66c2abd2e961
ms.tgt_platform: multiple
ms.topic: article
ms.date: 05/31/2018
---

# Displaying the Status of an Event Collector Subscription

You can display the status of an Event Collector subscription. The status includes the availability of the subscription, the last error that occurred for the subscription, the time of the last error, and the next time the subscription will be retried.

> [!Note]
>
> You can use this example to display the status of a subscription or you can type the following command at the command prompt:
>
> **wecutil gr** *SubscriptionName*

 

You will need the name of a subscription to display its status. To list the names of current subscriptions on a local computer, you can use the C++ example in shown in [Listing Event Collector Subscriptions](listing-event-collector-subscriptions.md), or you can type the following command at the command prompt:

**wecutil es**

The following example follows a procedure to display the status of an Event Collector subscription:

**To display the status of an Event Collector subscription**

1.  Open the subscription by providing the subscription name and access rights as parameters to the [**EcOpenSubscription**](/windows/desktop/api/Evcoll/nf-evcoll-ecopensubscription) function. For more information about access rights, see [**Windows Event Collector Constants**](windows-event-collector-constants.md).
2.  Get the status of the subscription by calling the [**EcGetSubscriptionRunTimeStatus**](/windows/desktop/api/Evcoll/nf-evcoll-ecgetsubscriptionruntimestatus) function (do not specify an event source when calling the function).
3.  Get the event sources array of the subscription by calling the [**EcGetSubscriptionRunTimeStatus**](/windows/desktop/api/Evcoll/nf-evcoll-ecgetsubscriptionruntimestatus) function and passing in the EcSubscriptionRunTimeStatusEventSources flag.
4.  Get the status information for each event source by calling the [**EcGetSubscriptionRunTimeStatus**](/windows/desktop/api/Evcoll/nf-evcoll-ecgetsubscriptionruntimestatus) function and passing in the event source name. For more information about the status information that can be retrieved, see the [**EC\_SUBSCRIPTION\_RUNTIME\_STATUS\_INFO\_ID**](/windows/desktop/api/Evcoll/ne-evcoll-ec_subscription_runtime_status_info_id) enumeration.
5.  Print the status information for the subscription.
6.  Close the subscription by calling the [**EcClose**](/windows/desktop/api/Evcoll/nf-evcoll-ecclose) function.

The following C++ code example shows how to display the status of an Event Collector subscription.


```C++
#include <iostream>
using namespace std;
#include <windows.h>
#include <EvColl.h>
#include <vector>
#include <string>
#include <strsafe.h>
#pragma comment(lib, "wecapi.lib")


// Track Runtime Status
typedef struct _RUNTIME_STATUS
{
    std::wstring ActiveStatus;
    DWORD LastError;
    std::wstring LastErrorMessage;
    std::wstring NextRetryTime;

} RUNTIME_STATUS;

// Subscription Information

DWORD GetStatus(LPCWSTR subscriptionName, 
    LPCWSTR eventSource, 
    EC_SUBSCRIPTION_RUNTIME_STATUS_INFO_ID statusInfoID, 
    DWORD flags, 
    std::vector<BYTE>& buffer, 
    PEC_VARIANT& vStatus);

std::wstring ConvertEcDateTime( ULONGLONG code );



void __cdecl wmain()
{
    LPVOID lpwszBuffer;
    DWORD dwEventSourceCount, dwRetVal = ERROR_SUCCESS;
    std::vector<BYTE> buffer;
    std::vector<BYTE> eventSourceBuffer;
    std::vector<BYTE>::iterator sourceNameIterator;
    PEC_VARIANT vStatus, vEventSources;
    EC_HANDLE hSubscription;
    LPCWSTR lpSubname = L"TestSubscription";
    RUNTIME_STATUS runtimeStatus;
    std::wstring eventSource;

    // Step 1: Open the Event Collector subscription.
    hSubscription = EcOpenSubscription(lpSubname, 
        EC_READ_ACCESS, 
        EC_OPEN_EXISTING);
    if (!hSubscription)
    {
        dwRetVal = GetLastError();
        goto Cleanup;
    }

    // Get the status values for the entire subscription.
    dwRetVal = GetStatus(lpSubname, NULL, 
        EcSubscriptionRunTimeStatusActive,
        0,
        buffer,
        vStatus);
    if (ERROR_SUCCESS != dwRetVal) {
        goto Cleanup;
    }
    wprintf(L"\nEvent Subscription: %s\n",  lpSubname);
    
    // Convert the status value to text.
    switch (vStatus->UInt32Val)
    {
        case EcRuntimeStatusActiveStatusActive:
            runtimeStatus.ActiveStatus = L"Active";
            break;
        case EcRuntimeStatusActiveStatusDisabled:
            runtimeStatus.ActiveStatus = L"Disabled";
            break;
        case EcRuntimeStatusActiveStatusInactive:
            runtimeStatus.ActiveStatus = L"Inactive";
            break;
        case EcRuntimeStatusActiveStatusTrying:
            runtimeStatus.ActiveStatus = L"Trying";
            break;
        default:
            runtimeStatus.ActiveStatus = L"Unknown Status";
        break;
    }
    wprintf(L"Runtime Status: %s\n", runtimeStatus.ActiveStatus.c_str());
    
    dwRetVal = GetStatus(lpSubname, NULL, 
        EcSubscriptionRunTimeStatusLastError,
        0,
        buffer,
        vStatus);
    if (ERROR_SUCCESS != dwRetVal) {
        goto Cleanup;
    }
    wprintf(L"Last Error: %u\n", vStatus->UInt32Val);
        
    

    // Step 2: Get the event sources array to query for event source status.
    dwRetVal = GetStatus(lpSubname, NULL, 
        EcSubscriptionRunTimeStatusEventSources, 
        0,
        eventSourceBuffer, 
        vEventSources);
    if (ERROR_SUCCESS != dwRetVal){
        goto Cleanup;
    }

    // Ensure that a handle to the event sources array has been obtained.
    if (vEventSources->Type != EcVarTypeNull && 
        vEventSources->Type != (EcVarTypeString | EC_VARIANT_TYPE_ARRAY) )
    {
        dwRetVal = ERROR_INVALID_DATA;
        goto Cleanup;
    }

    dwEventSourceCount = vEventSources->Count;
    
    // Step 3: Get the status of each event source.
    for (DWORD I = 0; I < dwEventSourceCount ; I++)
    {
        eventSource = vEventSources->StringArr[I];

        // Get the status of the subscription event source.
        dwRetVal = GetStatus(lpSubname, 
            eventSource.c_str(),
            EcSubscriptionRunTimeStatusActive, 
            0, 
            buffer, 
            vStatus);
        if (ERROR_SUCCESS != dwRetVal)
        {
            goto Cleanup;
        }
        if (vStatus->Type != EcVarTypeUInt32)
        {
            dwRetVal = ERROR_INVALID_DATA;
            goto Cleanup;
        }

        // Convert the status value to text.
        switch (vStatus->UInt32Val)
        {
            case EcRuntimeStatusActiveStatusActive:
                runtimeStatus.ActiveStatus = L"Active";
                break;
            case EcRuntimeStatusActiveStatusDisabled:
                runtimeStatus.ActiveStatus = L"Disabled";
                break;
            case EcRuntimeStatusActiveStatusInactive:
                runtimeStatus.ActiveStatus = L"Inactive";
                break;
            case EcRuntimeStatusActiveStatusTrying:
                runtimeStatus.ActiveStatus = L"Trying";
                break;
            default:
                runtimeStatus.ActiveStatus = L"Unknown Status";
            break;
        }

        // Get the last error that occurred for the subscription.
        dwRetVal = GetStatus(lpSubname, 
            eventSource.c_str(), 
            EcSubscriptionRunTimeStatusLastError, 
            0, 
            buffer, 
            vStatus);
        if(ERROR_SUCCESS != dwRetVal)
        {
            goto Cleanup;
        }
        if (vStatus->Type != EcVarTypeUInt32)
        {
            dwRetVal = ERROR_INVALID_DATA;
            goto Cleanup;
        }
        
        runtimeStatus.LastError = vStatus->UInt32Val;

        // Get the error message for the last error.
        dwRetVal = GetStatus(lpSubname, 
            eventSource.c_str(), 
            EcSubscriptionRunTimeStatusLastErrorMessage, 
            0, 
            buffer, 
            vStatus);

        if (ERROR_SUCCESS != dwRetVal)
        {
            goto Cleanup;
        }
        if (vStatus->Type != EcVarTypeNull && vStatus->Type != EcVarTypeString)
        {
            dwRetVal = ERROR_INVALID_DATA;
            goto Cleanup;
        }
          
        if (vStatus->Type != EcVarTypeNull)
        {
            runtimeStatus.LastErrorMessage = vStatus->StringVal;
        }
        else
        {
            runtimeStatus.LastErrorMessage = L"";
        }

        // Get the time when the subscription will be retried.
        dwRetVal = GetStatus( lpSubname, 
            eventSource.c_str(), 
            EcSubscriptionRunTimeStatusNextRetryTime, 
            0, 
            buffer, 
            vStatus);

        if( ERROR_SUCCESS != dwRetVal)
        {
            goto Cleanup;
        }
         
        if (vStatus->Type != EcVarTypeNull && vStatus->Type != EcVarTypeDateTime)
        {
            dwRetVal = ERROR_INVALID_DATA;
            goto Cleanup;
        }
          
        if( vStatus->Type != EcVarTypeNull)
        {
            runtimeStatus.NextRetryTime = ConvertEcDateTime(vStatus->DateTimeVal);
        }
        else
        {
            runtimeStatus.NextRetryTime = L"";
        }

        // Step 4: Print the status information.
        wprintf(L"\nEventSource[%u]\n",  I);
        wprintf(L"    Address: %s\n", eventSource.c_str());
        wprintf(L"    Runtime Status: %s\n", runtimeStatus.ActiveStatus.c_str());
        wprintf(L"    Last Error: %u\n", runtimeStatus.LastError);
         
        if( 0 != runtimeStatus.LastError )
        {
            wprintf(L"    Last Error Message: %s\n", runtimeStatus.LastErrorMessage.c_str());
        }
        else
        {
            wprintf(L"    Last Error Message: No Error\n");
        }
         
        wprintf(L"    Next Retry Time: %s\n", runtimeStatus.NextRetryTime.c_str());
    }

    Cleanup:

       // Step 5: Close the subscription.
       if(hSubscription)
           EcClose(hSubscription);
   
       if (dwRetVal != ERROR_SUCCESS)
       {
            FormatMessageW( FORMAT_MESSAGE_ALLOCATE_BUFFER | FORMAT_MESSAGE_FROM_SYSTEM,
                NULL,
                dwRetVal,
                0,
                (LPWSTR) &lpwszBuffer,
                0,
                NULL);
            
            if (!lpwszBuffer)
            {
                wprintf(L"Failed to FormatMessage.  Operation Error Code: %u." \
                    L"Error Code from FormatMessage: %u\n", dwRetVal, GetLastError());
                return;
            }

            wprintf(L"\nFailed to Perform Operation.\nError Code: %u\n" \
                L"Error Message: %s\n", dwRetVal, lpwszBuffer);

            LocalFree(lpwszBuffer);
        }
}

// Get the information for the specified EC_SUBSCRIPTION_RUNTIME_STATUS_INFO_ID
DWORD GetStatus(LPCWSTR subscriptionName, 
    LPCWSTR eventSource, 
    EC_SUBSCRIPTION_RUNTIME_STATUS_INFO_ID statusInfoID, 
    DWORD flags, 
    std::vector<BYTE>& buffer, 
    PEC_VARIANT& vStatus)
{
    DWORD dwBufferSize, dwRetVal = ERROR_SUCCESS;
    buffer.clear();
    buffer.resize(sizeof(EC_VARIANT));
    
    if ( !EcGetSubscriptionRunTimeStatus( subscriptionName,
        statusInfoID,
        eventSource,
        flags,
        (DWORD) buffer.size(),
        (PEC_VARIANT) &buffer[0],
        &dwBufferSize))
    {
        dwRetVal = GetLastError();

        if( ERROR_INSUFFICIENT_BUFFER ==  dwRetVal)
        {
            dwRetVal = ERROR_SUCCESS;
            buffer.resize(dwBufferSize);
            if(!EcGetSubscriptionRunTimeStatus( subscriptionName,
                statusInfoID,
                eventSource,
                flags,
                (DWORD) buffer.size(),
                (PEC_VARIANT) &buffer[0],
                &dwBufferSize))
            {
                dwRetVal = GetLastError();
            }
        }
    }

    if ( ERROR_SUCCESS == dwRetVal)
    {
        vStatus = (PEC_VARIANT) &buffer[0];
    }
    else
    {
        vStatus = NULL;
    }

    return dwRetVal;
}

std::wstring ConvertEcDateTime( ULONGLONG code )
{
    FILETIME ft;
    SYSTEMTIME utcTime;
    SYSTEMTIME localTime; 
    std::wstring timeString;
    std::vector<WCHAR> buffer(30);

    timeString = L"Error- Failed to Convert Date Time to String";

    ft.dwHighDateTime = (DWORD)((code >> 32) & 0xFFFFFFFF);
    ft.dwLowDateTime = (DWORD)(code & 0xFFFFFFFF);

    if( !FileTimeToSystemTime( &ft, &utcTime) )
    {
        return timeString;
    }

    if(!SystemTimeToTzSpecificLocalTime(NULL, &utcTime, &localTime))
    {
        return timeString;
    }

    HRESULT hr = StringCchPrintfW((LPWSTR) &buffer[0], 
        buffer.size(), 
        L"%4.4hd-%2.2hd-%2.2hdT%2.2hd:%2.2hd:%2.2hd.%3.3hdZ",
        localTime.wYear,
        localTime.wMonth,
        localTime.wDay,
        localTime.wHour,
        localTime.wMinute,
        localTime.wSecond,
        localTime.wMilliseconds);

    if (FAILED(hr)) 
    {
        return timeString;
    }

    timeString = (LPWSTR) &buffer[0];

    return timeString;
}
```



## Related topics

<dl> <dt>

[Listing Event Collector Subscriptions](listing-event-collector-subscriptions.md)
</dt> <dt>

[Windows Event Collector Reference](windows-event-collector-reference.md)
</dt> </dl>

 

 




