---
description: The GetInterfaceInfo function fills a pointer to an IP\_INTERFACE\_INFO structure with information about the interfaces associated with the system.
ms.assetid: 0cc18e14-7329-49b0-bb07-912fa403db46
title: Managing Interfaces Using GetInterfaceInfo
ms.topic: article
ms.date: 05/31/2018
---

# Managing Interfaces Using GetInterfaceInfo

The [**GetInterfaceInfo**](/windows/desktop/api/Iphlpapi/nf-iphlpapi-getinterfaceinfo) function fills a pointer to an [**IP\_INTERFACE\_INFO**](/windows/desktop/api/Ipexport/ns-ipexport-ip_interface_info) structure with information about the interfaces associated with the system.

**To use GetInterfaceInfo**

1.  Declare a pointer to an [**IP\_INTERFACE\_INFO**](/windows/desktop/api/Ipexport/ns-ipexport-ip_interface_info) object called `pInfo`, and a **ULONG** object called `ulOutBufLen`. Also declare a **DWORD** object called `dwRetVal` (used for error checking).
    ```C++
        ULONG               ulOutBufLen;
        DWORD               dwRetVal;
        unsigned int       i;

        IP_INTERFACE_INFO*  pInterfaceInfo;
    ```

    

2.  Allocate memory for the structures.
    > [!Note]  
    > The size of `ulOutBufLen` is not sufficient to hold the information. See the next step.

     

    ```C++
        pInterfaceInfo = (IP_INTERFACE_INFO *) malloc(sizeof (IP_INTERFACE_INFO));
        ulOutBufLen = sizeof(IP_INTERFACE_INFO);
    
    ```

    

3.  Make an initial call to [**GetInterfaceInfo**](/windows/desktop/api/Iphlpapi/nf-iphlpapi-getinterfaceinfo) to get the size needed into the `ulOutBufLen` variable.
    > [!Note]  
    > This call to the function is meant to fail, and is used to ensure that the `ulOutBufLen` variable specifies a size sufficient for holding all the information returned to `pInfo`. This is a common programming model in IP Helper for data structures and functions of this type.

     

    ```C++
        if (GetInterfaceInfo(pInterfaceInfo, &ulOutBufLen) ==
            ERROR_INSUFFICIENT_BUFFER) {
            free(pInterfaceInfo);
            pInterfaceInfo = (IP_INTERFACE_INFO *) malloc(ulOutBufLen);
        }
    ```

    

4.  Make a second call to [**GetInterfaceInfo**](/windows/desktop/api/Iphlpapi/nf-iphlpapi-getinterfaceinfo) with general error checking and return its value to the **DWORD** variable `dwRetVal` (for more advanced error checking).
    ```C++
        if ((dwRetVal = GetInterfaceInfo(pInterfaceInfo, &ulOutBufLen)) != NO_ERROR) {
            printf("  GetInterfaceInfo failed with error: %d\n", dwRetVal);
        }
    ```

    

5.  If the call was successful, access the data from the `pInfo` data structure.

    ```C++
            printf("  GetInterfaceInfo succeeded.\n");

            printf("  Num Adapters: %ld\n\n", pInterfaceInfo->NumAdapters);
            for (i = 0; i < (unsigned int) pInterfaceInfo->NumAdapters; i++) {
                printf("  Adapter Index[%d]: %ld\n", i,
                       pInterfaceInfo->Adapter[i].Index);
                printf("  Adapter Name[%d]:  %ws\n\n", i,
                       pInterfaceInfo->Adapter[i].Name);
            }
        }
    ```

    

    > [!Note]  
    > The %ws in the first line denotes a wide string. This is used because the **Name** attribute of the [**IP\_ADAPTER\_INDEX\_MAP**](/windows/desktop/api/Ipexport/ns-ipexport-ip_adapter_index_map) structure `Adapter` is a **WCHAR**, which is a Unicode string.

     

6.  Free any memory allocated for the *pInfo* structure.
    ```C++
        if (pInterfaceInfo) {
            free(pInterfaceInfo);
            pInterfaceInfo = NULL;
        }
    ```

    

Next Step: [Managing IP Addresses Using GetIpAddrTable](managing-ip-addresses-using-getipaddrtable.md)

Previous Step: [Managing Network Adapters Using GetAdaptersInfo](managing-network-adapters-using-getadaptersinfo.md)

 

 



