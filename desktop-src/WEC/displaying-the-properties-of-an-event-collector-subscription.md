---
title: Display event collector subscription properties
description: You can view useful information about an Event Collector subscription and its event sources by retrieving and displaying the properties of the subscription.
ms.assetid: 984e21cf-3671-4aca-9e8e-bcad1fa2f02c
ms.tgt_platform: multiple
ms.topic: article
ms.date: 05/31/2018
---

# Display event collector subscription properties

You can view useful information about an Event Collector subscription and its event sources by retrieving and displaying the properties of the subscription.

> [!Note]
>
> You can use this example to display the property values of a subscription or you can type the following command at the command prompt:
>
> **wecutil gs** *SubscriptionName*

 

To display its properties, specify the name of a subscription. For more information and a C++ code example of how to list the names of current subscriptions on a local computer, see [Listing Event Collector Subscriptions](listing-event-collector-subscriptions.md), or you can type the following command at the command prompt:

**wecutil es**

The following code example follows a procedure to display the properties of an Event Collector subscription and its associated event sources.

**To display the properties of an Event Collector subscription and its event sources**

1.  Open the subscription by providing the subscription name and access rights as parameters to the [**EcOpenSubscription**](/windows/desktop/api/Evcoll/nf-evcoll-ecopensubscription) function. For more information about access rights, see [**Windows Event Collector Constants**](windows-event-collector-constants.md).
2.  Get and display the properties of the subscription and event sources by calling the [**EcGetSubscriptionProperty**](/windows/desktop/api/Evcoll/nf-evcoll-ecgetsubscriptionproperty) function and the [**EcGetObjectArrayProperty**](/windows/desktop/api/Evcoll/nf-evcoll-ecgetobjectarrayproperty) function. For more information about subscription and event source properties that can be displayed, see the [**EC\_SUBSCRIPTION\_PROPERTY\_ID**](/windows/desktop/api/Evcoll/ne-evcoll-ec_subscription_property_id) enumeration.
3.  Close the subscription by calling the [**EcClose**](/windows/desktop/api/Evcoll/nf-evcoll-ecclose) function.

The following C++ code example shows how to display the properties of an Event Collector subscription.


```C++
#include <windows.h>
#include <EvColl.h>
#include <vector>
#include <string>
#include <strsafe.h>
#pragma comment(lib, "wecapi.lib")


// Track properties of the Subscription
typedef enum _SUB_TYPE
{
    SubTypeConfigurationMode =0,
    SubTypeCredentialsType,
    SubTypeDeliveryMode,
    SubTypeContentFormat,
    SubTypeSubscriptionType,
    SubTypeNone
} SUB_TYPE;


void  PrintProperty(PEC_VARIANT vProperty, 
    EC_VARIANT_TYPE varType, 
    SUB_TYPE subType);

// Subscription Information
DWORD GetProperty(EC_HANDLE hSubscription,  
    EC_SUBSCRIPTION_PROPERTY_ID propID, 
    DWORD flags, 
    std::vector<BYTE>& buffer, 
    PEC_VARIANT& vProperty);
DWORD GetArrayProperty(EC_OBJECT_ARRAY_PROPERTY_HANDLE hArray, 
    EC_SUBSCRIPTION_PROPERTY_ID propID, 
    DWORD arrayIndex, 
    DWORD flags, 
    std::vector<BYTE>& buffer, 
    PEC_VARIANT& vProperty);

// Helpers - Conversion Functions
std::wstring ConvertEcConfigurationMode(DWORD code);
std::wstring ConvertEcDeliveryMode(DWORD code);
std::wstring ConvertEcContentFormat(DWORD code);
std::wstring ConvertEcCredentialsType(DWORD code);
std::wstring ConvertEcDateTime(ULONGLONG code);
std::wstring ConvertEcSubscriptionType(DWORD code);



void __cdecl wmain()
{
    DWORD dwRetVal = ERROR_SUCCESS;
    DWORD dwEventSourceCount;
    EC_HANDLE hSubscription;
    std::vector<BYTE> buffer; 
    PEC_VARIANT vEventSource;
    PEC_VARIANT vProperty;
    EC_OBJECT_ARRAY_PROPERTY_HANDLE hArray = NULL;
    LPCWSTR lpSubname = L"SourceInit";
    LPVOID lpwszBuffer;
    
    // Step 1: Open the Event Collector subscription.
    hSubscription = EcOpenSubscription(lpSubname,
        EC_READ_ACCESS,
        EC_OPEN_EXISTING);
    if (!hSubscription)
    {
        wprintf(L"Could not open the subscription.\n");
        goto Cleanup;
    }

    // Step 2: Get and print the properties of the subscription and event sources.

    // Print the name of the subscription.
    wprintf(L"\n\nSubscription ID: %s\n", lpSubname);

    // Print the description of the subscription.
    wprintf(L"Description: ");
    dwRetVal = GetProperty(hSubscription, 
        EcSubscriptionDescription,
        0,
        buffer,
        vProperty);
    if (ERROR_SUCCESS == dwRetVal)
        PrintProperty(vProperty, EcVarTypeString, SubTypeNone);

    // Print the URI of the subscription.
    wprintf(L"URI: ");
    dwRetVal = GetProperty(hSubscription, 
        EcSubscriptionURI, 
        0, 
        buffer, 
        vProperty);
    if (ERROR_SUCCESS == dwRetVal)
        PrintProperty(vProperty, EcVarTypeString, SubTypeNone);

    // Print the status of the subscription.
    wprintf(L"Enabled: ");
    dwRetVal = GetProperty(hSubscription,
        EcSubscriptionEnabled,
        0,
        buffer,
        vProperty);
    if (ERROR_SUCCESS == dwRetVal)
        PrintProperty(vProperty, EcVarTypeBoolean, SubTypeNone);

    // Print the configuration mode of the subscription.
    wprintf(L"Configuration Mode: ");
    dwRetVal = GetProperty(hSubscription,
        EcSubscriptionConfigurationMode,
        0,
        buffer,
        vProperty);
    if (ERROR_SUCCESS == dwRetVal)
        PrintProperty(vProperty, EcVarTypeUInt32, SubTypeConfigurationMode);

    // Print the query string of the subscription.
    wprintf(L"Query: ");
    dwRetVal = GetProperty(hSubscription,
        EcSubscriptionQuery,
        0,
        buffer,
        vProperty);
    if (ERROR_SUCCESS == dwRetVal)
        PrintProperty(vProperty, EcVarTypeString, SubTypeNone);

    // Print the delivery mode of the subscription.
    wprintf(L"Delivery Mode: ");
    dwRetVal = GetProperty(hSubscription,
        EcSubscriptionDeliveryMode,
        0,
        buffer,
        vProperty);
    if (ERROR_SUCCESS == dwRetVal)
        PrintProperty(vProperty, EcVarTypeUInt32, SubTypeDeliveryMode);

    // Print the max items of the subscription.
    wprintf(L"Max Items: ");
    dwRetVal = GetProperty(hSubscription,
        EcSubscriptionDeliveryMaxItems,
        0,
        buffer,
        vProperty);
    if (ERROR_SUCCESS == dwRetVal)
        PrintProperty(vProperty, EcVarTypeUInt32, SubTypeNone);
 
    // Print the max latency time of the subscription.
    wprintf(L"Max Latency Time: ");
    dwRetVal = GetProperty(hSubscription,
        EcSubscriptionDeliveryMaxLatencyTime,
        0,
        buffer,
        vProperty);
    if (ERROR_SUCCESS == dwRetVal)
        PrintProperty(vProperty, EcVarTypeUInt32, SubTypeNone);

    // Print the heartbeat interval of the subscription.
    wprintf(L"Heartbeat Interval: ");
    dwRetVal = GetProperty(hSubscription,
        EcSubscriptionHeartbeatInterval,
        0,
        buffer,
        vProperty);
    if (ERROR_SUCCESS == dwRetVal)
        PrintProperty(vProperty, EcVarTypeUInt32, SubTypeNone);

    // Print the locale of the subscription.
    wprintf(L"Locale: ");
    dwRetVal = GetProperty(hSubscription, 
        EcSubscriptionLocale,
        0,
        buffer,
        vProperty);
    if (ERROR_SUCCESS == dwRetVal)
        PrintProperty(vProperty, EcVarTypeString, SubTypeNone);

    // Print the dialect for the subscription.
    wprintf(L"Dialect: ");
    dwRetVal = GetProperty(hSubscription, 
        EcSubscriptionDialect,
        0, 
        buffer, 
        vProperty);
    if (ERROR_SUCCESS == dwRetVal)
        PrintProperty(vProperty, EcVarTypeString, SubTypeNone);

    // Print the content format of the subscription.
    wprintf(L"Content Format: ");
    dwRetVal = GetProperty(hSubscription, 
        EcSubscriptionContentFormat, 
        0,
        buffer,
        vProperty);
    if (ERROR_SUCCESS == dwRetVal)
        PrintProperty(vProperty, EcVarTypeUInt32, SubTypeContentFormat);

    // Print the log file for the subscription.
    wprintf(L"Log File: ");
    dwRetVal = GetProperty(hSubscription,
        EcSubscriptionLogFile,
        0,
        buffer,
        vProperty);
    if (ERROR_SUCCESS == dwRetVal)
        PrintProperty(vProperty, EcVarTypeString, SubTypeNone);

    // Print the read existing events status of the subscription.
    wprintf(L"Read Existing Events: ");
    dwRetVal = GetProperty(hSubscription,
        EcSubscriptionReadExistingEvents, 
        0, 
        buffer, 
        vProperty);
    if (ERROR_SUCCESS == dwRetVal)
        PrintProperty(vProperty, EcVarTypeBoolean, SubTypeNone);

    // Print the expiration date of the subscription.
    wprintf(L"Expires: ");
    dwRetVal = GetProperty(hSubscription, 
        EcSubscriptionExpires,
        0, 
        buffer, 
        vProperty);
    if (ERROR_SUCCESS == dwRetVal)
        PrintProperty(vProperty, EcVarTypeDateTime, SubTypeNone);

    // Print the host name for the subscription.
    wprintf(L"Host Name: ");
    dwRetVal = GetProperty(hSubscription, 
        EcSubscriptionHostName,
        0, 
        buffer, 
        vProperty);
    if (ERROR_SUCCESS == dwRetVal)
        PrintProperty(vProperty, EcVarTypeString, SubTypeNone);

    // Print the publisher name for the subscription.
    wprintf(L"Publisher Name: ");
    dwRetVal = GetProperty(hSubscription, 
        EcSubscriptionPublisherName,
        0, 
        buffer, 
        vProperty);
    if (ERROR_SUCCESS == dwRetVal)
        PrintProperty(vProperty, EcVarTypeString, SubTypeNone);

    // Print the transport used by the subscription.
    wprintf(L"Transport Name: ");
    dwRetVal = GetProperty(hSubscription, 
        EcSubscriptionTransportName,
        0, 
        buffer, 
        vProperty);
    if (ERROR_SUCCESS == dwRetVal)
        PrintProperty(vProperty, EcVarTypeString, SubTypeNone);

    // Print the transport port used by the subscription.
    wprintf(L"Transport Port: ");
    dwRetVal = GetProperty(hSubscription, 
        EcSubscriptionTransportPort,
        0, 
        buffer, 
        vProperty);
    if (ERROR_SUCCESS == dwRetVal)
        PrintProperty(vProperty, EcVarTypeUInt32, SubTypeNone);

    // Print the type of the subscription (source or collector initiated).
    wprintf(L"Subscription Type: ");
    dwRetVal = GetProperty(hSubscription, 
        EcSubscriptionType,
        0, 
        buffer, 
        vProperty);
    if (ERROR_SUCCESS == dwRetVal)
        PrintProperty(vProperty, EcVarTypeUInt32, SubTypeSubscriptionType);

    if( vProperty->UInt32Val == EcSubscriptionTypeSourceInitiated)
    {

        //-------------------------------------------------------------------
        // Properties only used in source initiated subscriptions.

        // Print the allowed issuer CA property for the subscription.
        wprintf(L"AllowedIssuerCAs: ");
        dwRetVal = GetProperty(hSubscription, 
            EcSubscriptionAllowedIssuerCAs,
            0, 
            buffer, 
            vProperty);
        if (ERROR_SUCCESS == dwRetVal)
            PrintProperty(vProperty, EcVarTypeString, SubTypeNone);

        // Print the allowed subjects property for the subscription.
        wprintf(L"Allowed Subjects: ");
        dwRetVal = GetProperty(hSubscription, 
            EcSubscriptionAllowedSubjects,
            0, 
            buffer, 
            vProperty);
        if (ERROR_SUCCESS == dwRetVal)
            PrintProperty(vProperty, EcVarTypeString, SubTypeNone);

        // Print the denied subjects property for the subscription.
        wprintf(L"Denied Subjects: ");
        dwRetVal = GetProperty(hSubscription, 
            EcSubscriptionDeniedSubjects,
            0, 
            buffer, 
            vProperty);
        if (ERROR_SUCCESS == dwRetVal)
            PrintProperty(vProperty, EcVarTypeString, SubTypeNone);

        // Print the allowed subjects property for the subscription.
        wprintf(L"Allowed Source Domain Computers: ");
        dwRetVal = GetProperty(hSubscription, 
            EcSubscriptionAllowedSourceDomainComputers,
            0, 
            buffer, 
            vProperty);
        if (ERROR_SUCCESS == dwRetVal)
            PrintProperty(vProperty, EcVarTypeString, SubTypeNone);
    }
    else if( vProperty->UInt32Val == EcSubscriptionTypeCollectorInitiated)
    {
        //--------------------------------------------------------------------
        // Properties only used in collector initiated subscriptions.

        // Print the credentials type of the subscription.
        wprintf(L"Credentials Type: ");
        dwRetVal = GetProperty(hSubscription,
            EcSubscriptionCredentialsType,
            0,
            buffer,
            vProperty);
        if (ERROR_SUCCESS == dwRetVal)
            PrintProperty(vProperty, EcVarTypeUInt32, SubTypeCredentialsType);

        // Print the common user name of the subscription.
        wprintf(L"Common User Name: ");
        dwRetVal = GetProperty(hSubscription,
            EcSubscriptionCommonUserName,
            0,
            buffer,
            vProperty);
        if (ERROR_SUCCESS == dwRetVal )
            PrintProperty(vProperty, EcVarTypeString, SubTypeNone);

        // Print the event source information.
        dwRetVal = GetProperty(hSubscription, 
            EcSubscriptionEventSources, 
            0,
            buffer,
            vProperty);
        if (ERROR_SUCCESS != dwRetVal)
            goto Cleanup;

        if (vProperty->Type != EcVarTypeNull && vProperty->Type != 
            EcVarObjectArrayPropertyHandle)
        {
            dwRetVal = ERROR_INVALID_DATA;
            goto Cleanup;
        }

        hArray = (vProperty->Type == EcVarTypeNull) ? NULL: 
            vProperty->PropertyHandleVal;
        if (!hArray)
        {
            dwRetVal = ERROR_INVALID_DATA;
            goto Cleanup;
        }

        // Get the size of the event sources array
        if (!EcGetObjectArraySize(hArray, &dwEventSourceCount))
        {
            dwRetVal = GetLastError();
            goto Cleanup;
        }

        // Print information for all the event sources in the array
        for ( DWORD I = 0; I < dwEventSourceCount ; I++)
        {
            wprintf(L"\nEventSource [%u]: \n", I);
            wprintf(L"         Address: ");
            dwRetVal = GetArrayProperty(hArray, 
                EcSubscriptionEventSourceAddress,
                I,
                0,
                buffer,
                vEventSource);

            if (ERROR_SUCCESS == dwRetVal)
                PrintProperty(vEventSource, EcVarTypeString, SubTypeNone);

            wprintf(L"         Enabled: ");
            dwRetVal = GetArrayProperty(hArray,
                EcSubscriptionEventSourceEnabled,
                I,
                0,
                buffer,
                vEventSource);

            if (ERROR_SUCCESS == dwRetVal)
                PrintProperty(vEventSource, EcVarTypeBoolean, SubTypeNone);

            wprintf(L"         UserName: ");
            dwRetVal = GetArrayProperty(hArray,
                EcSubscriptionEventSourceUserName,
                I,
                0,
                buffer,
                vEventSource);

            if (ERROR_SUCCESS == dwRetVal)
                PrintProperty(vEventSource, EcVarTypeString, SubTypeNone);

            wprintf(L"         Password: ");
            dwRetVal = GetArrayProperty(hArray,
                EcSubscriptionEventSourcePassword,
                I,
                0,
                buffer,
                vEventSource);

            // By default, the password cannot be read. 
            // An ACCESS DENIED Error will be returned.
            if (ERROR_SUCCESS != dwRetVal && ERROR_ACCESS_DENIED != dwRetVal)
            {
                wprintf(L"Error Obtaining Data\n");
                continue;
            }
            else
            {
                dwRetVal = ERROR_SUCCESS;
                wprintf(L"*\n");
            }
        }
    }

    Cleanup:
        // Step 3: Close the subscription.
        if (hArray)
            EcClose(hArray);
        if (hSubscription)
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
                L" Error Message: %s\n", dwRetVal, lpwszBuffer);

            LocalFree(lpwszBuffer);
        }
}

void  PrintProperty(PEC_VARIANT vProperty, EC_VARIANT_TYPE varType, SUB_TYPE subType)
{
    if ((!vProperty ) || ((vProperty->Type!= (DWORD) EcVarTypeNull) 
        && (vProperty->Type != (DWORD) varType )))
    {
        wprintf(L"Failed to Obtain Data\n");
        return;
    }

    switch (vProperty->Type)
    {
        case EcVarTypeString:
            wprintf(L"%s\n", vProperty->StringVal);
            break;
        case EcVarTypeUInt32:
            switch (subType)
            {
                case SubTypeConfigurationMode:
                    wprintf(L"%s\n", 
                        ConvertEcConfigurationMode(vProperty->UInt32Val).c_str());
                    break;
                case SubTypeCredentialsType:
                    wprintf(L"%s\n", 
                        ConvertEcCredentialsType( vProperty->UInt32Val).c_str());
                    break;
                case SubTypeContentFormat:
                    wprintf(L"%s\n", 
                        ConvertEcContentFormat( vProperty->UInt32Val).c_str());
                    break;
                case SubTypeDeliveryMode:
                    wprintf(L"%s\n", 
                        ConvertEcDeliveryMode( vProperty->UInt32Val).c_str());
                    break;
                case SubTypeSubscriptionType:
                wprintf(L"%s\n", 
                    ConvertEcSubscriptionType( vProperty->UInt32Val).c_str());
                break;
                default:
                    wprintf(L"%u\n", vProperty->UInt32Val);
            }
            break;
        case EcVarTypeBoolean:
            wprintf(L"%s\n", (vProperty->BooleanVal) ? L"True": L"False");
            break;
        case EcVarTypeDateTime:
            wprintf(L"%s\n", ConvertEcDateTime( vProperty->DateTimeVal).c_str());
            break;
        case EcVarTypeNull:
        default:
            wprintf(L" - \n");
    }

    return;
}

DWORD GetProperty(EC_HANDLE hSubscription, 
    EC_SUBSCRIPTION_PROPERTY_ID propID,
    DWORD flags,
    std::vector<BYTE>& buffer,
    PEC_VARIANT& vProperty)
{
    DWORD  dwBufferSize, dwRetVal = ERROR_SUCCESS;
    buffer.resize(sizeof(EC_VARIANT));
 
    if (!hSubscription)
        return ERROR_INVALID_PARAMETER;

    // Get the value for the specified property. 
    if (!EcGetSubscriptionProperty(hSubscription,
        propID,
        flags, 
        (DWORD) buffer.size(), 
        (PEC_VARIANT)&buffer[0], 
        &dwBufferSize))
    {
        dwRetVal = GetLastError();
        if (ERROR_INSUFFICIENT_BUFFER == dwRetVal)
        {
            dwRetVal = ERROR_SUCCESS;
            buffer.resize(dwBufferSize);

            if (!EcGetSubscriptionProperty(hSubscription,
                propID,
                flags,
                (DWORD) buffer.size(),
                (PEC_VARIANT)&buffer[0],
                &dwBufferSize))
            {
                dwRetVal = GetLastError();
            }
        }
    }

    if (dwRetVal == ERROR_SUCCESS)
    {
        vProperty = (PEC_VARIANT) &buffer[0];
    }
    else
    {
        vProperty = NULL;
    }

    return dwRetVal;
}

DWORD GetArrayProperty(EC_OBJECT_ARRAY_PROPERTY_HANDLE hArray,
    EC_SUBSCRIPTION_PROPERTY_ID propID,
    DWORD arrayIndex,
    DWORD flags,
    std::vector<BYTE>& buffer,
    PEC_VARIANT& vProperty)
{
    DWORD dwRetVal = ERROR_SUCCESS;
    DWORD dwBufferSizeUsed;
    buffer.resize(sizeof(EC_VARIANT));
    
    if (!EcGetObjectArrayProperty(hArray, 
        propID,
        arrayIndex,
        flags,
        (DWORD) buffer.size(),
        (PEC_VARIANT) &buffer[0],
        &dwBufferSizeUsed))
    {
        dwRetVal = GetLastError();
        if (ERROR_INSUFFICIENT_BUFFER == dwRetVal)
        {
            buffer.resize(dwBufferSizeUsed);
            dwRetVal = ERROR_SUCCESS;
            if (!EcGetObjectArrayProperty(hArray,
                propID,
                arrayIndex,
                flags,
                (DWORD) buffer.size(),
                (PEC_VARIANT) &buffer[0],
                &dwBufferSizeUsed))
            {
                dwRetVal = GetLastError();
            }
        }
    }

    if (dwRetVal == ERROR_SUCCESS)
    {
        vProperty = (PEC_VARIANT) &buffer[0];
    }
    else
    {
        vProperty = NULL;
    }

    return dwRetVal;
}

std::wstring ConvertEcConfigurationMode(DWORD code)
{
    if (EcConfigurationModeCustom == 
        (EC_SUBSCRIPTION_CONFIGURATION_MODE) code)
        return L"Custom";
    else if (EcConfigurationModeMinLatency == 
        (EC_SUBSCRIPTION_CONFIGURATION_MODE) code)
        return L"MaxLatency";
    else if (EcConfigurationModeMinBandwidth == 
        (EC_SUBSCRIPTION_CONFIGURATION_MODE) code)
        return L"MinBandwidth";
    else if (EcConfigurationModeNormal == 
        (EC_SUBSCRIPTION_CONFIGURATION_MODE) code)
        return L"Normal";
    else
        return L"Unknown";
}

std::wstring ConvertEcDeliveryMode(DWORD code)
{
    if (EcDeliveryModePull == (EC_SUBSCRIPTION_DELIVERY_MODE) code)
        return L"Pull";
    else if (EcDeliveryModePush == (EC_SUBSCRIPTION_DELIVERY_MODE) code)
        return L"Push";
    else
        return L"Unknown";
}

std::wstring ConvertEcContentFormat(DWORD code)
{
    if (EcContentFormatEvents == code)
        return L"FormatEvents";
    else if (EcContentFormatRenderedText == code)
        return L"RenderedText";
    else
        return L"Unknown";
}

std::wstring ConvertEcCredentialsType(DWORD code)
{
    if (EcSubscriptionCredDefault == code)
        return L"Default";
    else if (EcSubscriptionCredNegotiate == code)
        return L"Negotiate";
    else if (EcSubscriptionCredDigest == code)
        return L"Digest";
    else if (EcSubscriptionCredBasic == code)
        return L"Basic";
    else
        return L"Unknown";
}

std::wstring ConvertEcDateTime(ULONGLONG code)
{
    FILETIME ft;
    SYSTEMTIME utcTime;
    SYSTEMTIME localTime; 
    std::wstring timeString;
    std::vector<WCHAR> buffer(30);

    timeString = L"Error- Failed to Convert Date Time to String";

    ft.dwHighDateTime = (DWORD)((code >> 32) & 0xFFFFFFFF);
    ft.dwLowDateTime = (DWORD)(code & 0xFFFFFFFF);

    if (!FileTimeToSystemTime(&ft, &utcTime))
    {
        return timeString;
    }

    if (!SystemTimeToTzSpecificLocalTime(NULL, &utcTime, &localTime))
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
        localTime.wMilliseconds );

    if (FAILED(hr))
    {
        return timeString;
    }

    timeString = (LPWSTR) &buffer[0];

    return timeString;
}

std::wstring ConvertEcSubscriptionType(DWORD code)
{
    if (EcSubscriptionTypeCollectorInitiated == code)
        return L"Collector Initiated";
    else if (EcSubscriptionTypeSourceInitiated == code)
        return L"Souce Initiated";
    else
        return L"Unknown";
}
```



## Related topics

<dl> <dt>

[Listing Event Collector Subscriptions](listing-event-collector-subscriptions.md)
</dt> <dt>

[Windows Event Collector Reference](windows-event-collector-reference.md)
</dt> </dl>

 

 




