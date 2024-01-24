---
title: Dual-STA query and configuration
description: There are two types of interfaces associated with adapters that support dual station (dual-STA) connections&mdash;primary STA interfaces, and secondary STA interfaces. All adapters expose a primary STA interface, but only adapters supporting the dual-STA functionality expose secondary STA interfaces.
ms.topic: article
ms.date: 10/18/2021
---

# Dual-STA query and configuration

> [!NOTE]
> To develop for the features described in this topic, the Windows 11 SDK (10.0.22000.194), and later, is needed.

There are two types of interfaces associated with adapters that support dual station (dual-STA) connections&mdash;primary STA interfaces, and secondary STA interfaces. All adapters expose a primary STA interface, but only adapters supporting the dual-STA functionality expose secondary STA interfaces.

By default, Windows connects only on the primary STA interface. Windows will connect on the secondary STA interface only if all of the following conditions are met:

1. The driver indicates support for secondary STA interfaces in its capabilities.
2. There's no policy preventing secondary STA connectivity.
3. There's at least one application that has called the [**WlanSetInterface**](/windows/win32/api/wlanapi/nf-wlanapi-wlansetinterface) with the **wlan_intf_opcode_secondary_sta_synchronized_connections** opcode with the parameter set to `TRUE`.

## Querying dual-STA interfaces

To determine whether an adapter is configured for dual-STA, and to get the list of secondary STA interface **GUID**s, your application must call [**WlanQueryInterface**](/windows/win32/api/wlanapi/nf-wlanapi-wlanqueryinterface) (wlanapi.h) with the **wlan_intf_opcode_secondary_sta_interfaces** opcode.

That opcode takes as a parameter the **GUID** of the primary station (STA) interface (which can be obtained by a call to [**WlanEnumInterfaces**](/windows/win32/api/wlanapi/nf-wlanapi-wlanenuminterfaces)), and it returns a list of secondary STA interfaces associated with that primary STA interface.

Here's an example of how to get the list of secondary STA interfaces.

```cpp
#ifndef UNICODE
#define UNICODE
#endif

#include <windows.h>
#include <wlanapi.h>
#include <Windot11.h> // for DOT11_SSID struct
#include <objbase.h>
#include <wtypes.h>

#include <stdio.h>
#include <stdlib.h>

// Need to link with Wlanapi.lib and Ole32.lib
#pragma comment(lib, "wlanapi.lib")
#pragma comment(lib, "ole32.lib")

DWORD QueryDualStaInterfaces()
{
    HANDLE hClient;
    DWORD version;
    DWORD dwResult = WlanOpenHandle(WLAN_API_VERSION_2_0, nullptr, &version, &hClient);
    if (dwResult != ERROR_SUCCESS)
    {
        wprintf(L"WlanOpenHandle failed with error: %u\n", dwResult);
        return dwResult;

    }

    PWLAN_INTERFACE_INFO_LIST pPrimaryIntfList = nullptr;
    dwResult = WlanEnumInterfaces(hClient, nullptr, &pPrimaryIntfList);
    if (dwResult != ERROR_SUCCESS)
    {
        wprintf(L"WlanEnumInterfaces FAILed, error = %u\n", dwResult);
        WlanCloseHandle(hClient, NULL);
        return dwResult;
    }

    wprintf(L"There are %u primary interfaces in the system\n", pPrimaryIntfList->dwNumberOfItems);
    for (UINT i = 0; i < pPrimaryIntfList->dwNumberOfItems; i++)
    {
        WCHAR* strPrimaryUuid = nullptr;
        if (UuidToStringW(&pPrimaryIntfList->InterfaceInfo[i].InterfaceGuid, reinterpret_cast<RPC_WSTR*>(&strPrimaryUuid)) != RPC_S_OK)
        {
            strPrimaryUuid = nullptr;
        }

        DWORD dwDataSize = 0;
        PWLAN_INTERFACE_INFO_LIST pSecondaryIntfList = nullptr;
        dwResult = WlanQueryInterface(
            hClient,
            &pPrimaryIntfList->InterfaceInfo[i].InterfaceGuid,
            wlan_intf_opcode_secondary_sta_interfaces,
            NULL,
            &dwDataSize,
            reinterpret_cast<PVOID*>(&pSecondaryIntfList),
            NULL);
        if (dwResult == ERROR_SUCCESS)
        {
            wprintf(
                L"\t[%d]\tInterface %ws (State = %d) has %u Secondary interfaces\n",
                i,
                strPrimaryUuid ? strPrimaryUuid : L"Unknown",
                pPrimaryIntfList->InterfaceInfo[i].isState,
                pSecondaryIntfList->dwNumberOfItems);
            for (UINT j = 0; j < pSecondaryIntfList->dwNumberOfItems; j++)
            {
                WCHAR* strSecondaryUuid = nullptr;
                if (UuidToStringW(&pSecondaryIntfList->InterfaceInfo[j].InterfaceGuid, reinterpret_cast<RPC_WSTR*>(&strSecondaryUuid)) == RPC_S_OK)
                {
                    wprintf(
                        L"\t\t[%d]\tSecondary Interface GUID: %ws, (State = %d)\n",
                        j,
                        strSecondaryUuid,
                        pSecondaryIntfList->InterfaceInfo[j].isState);
                    RpcStringFreeW(reinterpret_cast<RPC_WSTR*>(&strSecondaryUuid));
                }
            }
            WlanFreeMemory(pSecondaryIntfList);
        }
        else
        {
            wprintf(L"\t[%d]\tInterface %ws has 0 Secondary interfaces, error = %u\n", i, strPrimaryUuid ? strPrimaryUuid : L"Unknown", dwResult);
        }

        if (strPrimaryUuid)
        {
            RpcStringFreeW(reinterpret_cast<RPC_WSTR*>(&strPrimaryUuid));
        }
    }

    WlanFreeMemory(pPrimaryIntfList);
    WlanCloseHandle(hClient, NULL);

    return dwResult;
}
```

## Querying dual-STA synchronized connections state

To determine whether an adapter will automatically connect over the secondary STA interface following a connection over the primary STA interface, your application can query the current state by calling [**WlanQueryInterface**](/windows/win32/api/wlanapi/nf-wlanapi-wlanqueryinterface) with the **wlan_intf_opcode_secondary_sta_synchronized_connections** opcode.

That opcode returns a **BOOL** value indicating whether the primary and secondary STA connections are synchronized.

Here's an example of how to query this state.

```cpp
#ifndef UNICODE
#define UNICODE
#endif

#include <windows.h>
#include <wlanapi.h>
#include <Windot11.h> // for DOT11_SSID struct
#include <objbase.h>
#include <wtypes.h>

#include <stdio.h>
#include <stdlib.h>

// Need to link with Wlanapi.lib and Ole32.lib
#pragma comment(lib, "wlanapi.lib")
#pragma comment(lib, "ole32.lib")

DWORD QueryDualStaConnectivity()
{
    HANDLE hClient;
    DWORD version;
    DWORD dwResult = WlanOpenHandle(WLAN_API_VERSION_2_0, nullptr, &version, &hClient);
    if (dwResult != ERROR_SUCCESS)
    {
        wprintf(L"WlanOpenHandle failed with error: %u\n", dwResult);
        return dwResult;
    }
    PWLAN_INTERFACE_INFO_LIST pPrimaryIntfList = nullptr;
    dwResult = WlanEnumInterfaces(hClient, nullptr, &pPrimaryIntfList);
    if (dwResult != ERROR_SUCCESS)
    {
        wprintf(L"WlanEnumInterfaces FAILed, error = %u\n", dwResult);
        WlanCloseHandle(hClient, NULL);
        return dwResult;
    }

    //
    // Need to call the API only once to query/change the state.
    //
    if (pPrimaryIntfList->dwNumberOfItems)
    {
        WCHAR* strPrimaryUuid = nullptr;
        if (UuidToStringW(&pPrimaryIntfList->InterfaceInfo[0].InterfaceGuid, reinterpret_cast<RPC_WSTR*>(&strPrimaryUuid)) != RPC_S_OK)
        {
            strPrimaryUuid = nullptr;
        }

        DWORD dwDataSize = 0;
        PBOOL bQueriedValue = NULL;
        dwResult = WlanQueryInterface(
            hClient,
            &pPrimaryIntfList->InterfaceInfo[0].InterfaceGuid,
            wlan_intf_opcode_secondary_sta_synchronized_connections,
            NULL,
            &dwDataSize,
            (PVOID*)&bQueriedValue,
            NULL);
        if (dwResult == ERROR_SUCCESS)
        {

            wprintf(L"Secondary Sta Synchronized connections is currently %ws\n", *bQueriedValue ? L"Enabled" : L"Disabled");
            WlanFreeMemory(bQueriedValue);
        }
        else
        {
            wprintf(L"Failed to query Secondary Sta Synchronized connections - error = %u\n", dwResult);
        }

        if (strPrimaryUuid)
        {
            RpcStringFreeW(reinterpret_cast<RPC_WSTR*>(&strPrimaryUuid));
        }
    }

    WlanFreeMemory(pPrimaryIntfList);
    WlanCloseHandle(hClient, NULL);

    return dwResult;
}
```

## Enabling connections on the secondary STA interface

Windows won't connect on the secondary STA interfaces unless an application exists that will use the secondary STA connection. To control whether Windows connects on the secondary STA interface, your application must call [**WlanSetInterface**](/windows/win32/api/wlanapi/nf-wlanapi-wlansetinterface) with the **wlan_intf_opcode_secondary_sta_synchronized_connections** opcode, with a **BOOL** parameter specifying whether to enable or disable connections on the secondary STA interface. A value of `TRUE` indicates that you'd like to enable secondary STA connectivity, while a value of `FALSE` indicates that you no longer need secondary STA connectivity.

Calling the API with the *same* value (`TRUE` or `FALSE`) multiple times is redundant, and only the first instance of a new value causes the functionality to change.
Once your application enables secondary STA connectivity, you must keep the handle to the service open for the duration that you expect to use the secondary STA connection. Once your application disables secondary STA connectivity explicitly (either by calling **WlanSetInterface** with the opcode **wlan_intf_opcode_secondary_sta_synchronized_connections** and parameter value of `FALSE`, or by calling [**WlanCloseHandle**](/windows/win32/api/wlanapi/nf-wlanapi-wlanclosehandle)), or implicitly (by exiting), Windows will disable connectivity over the secondary STA interface at some point in time thereafter.

The secondary STA connectivity will remain enabled as long as at least once application is requesting it.

Here's an example showing how to enable or disable secondary STA connectivity.

```cpp
#ifndef UNICODE
#define UNICODE
#endif

#include <windows.h>
#include <wlanapi.h>
#include <Windot11.h> // for DOT11_SSID struct
#include <objbase.h>
#include <wtypes.h>

#include <stdio.h>
#include <stdlib.h>

// Need to link with Wlanapi.lib and Ole32.lib
#pragma comment(lib, "wlanapi.lib")
#pragma comment(lib, "ole32.lib")

DWORD SetDualStaConnectivity(BOOL bEnable)
{
    HANDLE hClient;
    DWORD version;
    DWORD dwResult = WlanOpenHandle(WLAN_API_VERSION_2_0, nullptr, &version, &hClient);
    if (dwResult != ERROR_SUCCESS)
    {
        wprintf(L"WlanOpenHandle failed with error: %u\n", dwResult);
        return dwResult;
    }
    PWLAN_INTERFACE_INFO_LIST pPrimaryIntfList = nullptr;
    dwResult = WlanEnumInterfaces(hClient, nullptr, &pPrimaryIntfList);
    if (dwResult != ERROR_SUCCESS)
    {
        wprintf(L"WlanEnumInterfaces FAILed, error = %u\n", dwResult);
        WlanCloseHandle(hClient, NULL);
        return dwResult;
    }

    //
    // Only need to call the API once to query/change the state
    //
    if (pPrimaryIntfList->dwNumberOfItems)
    {
        WCHAR* strPrimaryUuid = nullptr;
        if (UuidToStringW(&pPrimaryIntfList->InterfaceInfo[0].InterfaceGuid, reinterpret_cast<RPC_WSTR*>(&strPrimaryUuid)) != RPC_S_OK)
        {
            strPrimaryUuid = nullptr;
        }

        dwResult = WlanSetInterface(
            hClient,
            &pPrimaryIntfList->InterfaceInfo[0].InterfaceGuid,
            wlan_intf_opcode_secondary_sta_synchronized_connections,
            sizeof(bEnable),
            reinterpret_cast<PBYTE>(&bEnable),
            NULL);
        if (dwResult == ERROR_SUCCESS)
        {
            wprintf(L"Successfully set Sec Sta opcode = %x on Primary Interface %ws\n", bEnable, strPrimaryUuid);
        }
        else
        {
            wprintf(L"FAILed set Sec Sta opcode = %x on Primary Interface %ws -- error = %u\n", bEnable, strPrimaryUuid, dwResult);
        }

        if (strPrimaryUuid)
        {
            RpcStringFreeW(reinterpret_cast<RPC_WSTR*>(&strPrimaryUuid));
        }
    }

    WlanFreeMemory(pPrimaryIntfList);

    // Close the handle only when the app no longer needs the dual-sta connection
    //
    WlanCloseHandle(hClient, NULL);
    return dwResult;
}
```
