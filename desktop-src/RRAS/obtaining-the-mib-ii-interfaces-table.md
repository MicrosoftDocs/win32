---
title: Obtaining the MIB II Interfaces Table
description: The following code uses MprAdminMIBEntryGet to obtain the MIB II interfaces table from the local machine.
ms.assetid: 76152cd8-f285-42b3-8ee5-bbab1d14b99f
keywords:
- MIB, obtaining the interfaces
- Obtaining the MIB interfaces
ms.topic: article
ms.date: 05/31/2018
---

# Obtaining the MIB II Interfaces Table

The following code uses [**MprAdminMIBEntryGet**](/windows/desktop/api/Mprapi/nf-mprapi-mpradminmibentryget) to obtain the MIB II interfaces table from the local machine.


```C++
#include <windows.h>
#include <mprapi.h>
#include <iprtrmib.h>

#pragma comment(lib, "mprapi.lib")

void main()
{
    HANDLE            _hMibSrv = INVALID_HANDLE_VALUE;  
    MIB_OPAQUE_QUERY  MibOpaqueQuery; 
    PMIB_OPAQUE_INFO  pMibOpaqueInfo = NULL; 
    DWORD             dwInSize, dwOutSize, dwResult; 
    PMIB_IFTABLE      pIntfTable; 
    
    MibOpaqueQuery.dwVarId = IF_TABLE; 
    dwInSize = sizeof( MIB_OPAQUE_QUERY ); 
    dwOutSize = 0; 
    
    dwResult = MprAdminMIBEntryGet ( _hMibSrv, 
                                    PID_IP, 
                                    IPRTRMGR_PID, 
                                    (PVOID)&MibOpaqueQuery, 
                                    dwInSize, 
                                    (PVOID *)&pMibOpaqueInfo, 
                                    &dwOutSize );

    if ( dwResult != NO_ERROR )
        return;
    
    if ( pMibOpaqueInfo == NULL ) 
        return; 
    
    pIntfTable = ( PMIB_IFTABLE ) pMibOpaqueInfo -> rgbyData;
}


#include <windows.h>
#include <stdio.h>
#include &quot;Iphlpapi.h&quot;

int __cdecl main(){

    MIB_SERVER_HANDLE hMibSrv = NULL;  
    MIB_OPAQUE_QUERY MibOpaqueQuery; 
    PMIB_OPAQUE_INFO pMibOpaqueInfo = NULL; 
    DWORD dwInSize, dwOutSize, dwRes; 
    PMIB_IFTABLE pIntfTable; 
    
    MibOpaqueQuery.dwVarId = IF_TABLE; 
    dwInSize = sizeof(MIB_OPAQUE_QUERY); 
    dwOutSize = 0; 
    
    // Connect to the MIB server to obtain the hMibSrv handle
    dwRes = MprAdminMIBServerConnect(NULL, &hMibSrv);    
    if (dwRes != NO_ERROR){
        wprintf(L&quot;ERROR: Unable to connect to the MIB server specified.\n&quot;);
        return ERROR_SUCCESS;
    }

    // Retrieve the MIB interfaces table. The local RRAS service MUST be running or this call will fail.
    dwRes = MprAdminMIBEntryGet(hMibSrv, PID_IP, IPRTRMGR_PID, (PVOID)&MibOpaqueQuery, dwInSize, (PVOID*)&pMibOpaqueInfo, &dwOutSize);
    if (dwRes != NO_ERROR){
        wprintf(L&quot;ERROR: Unable to retrieve the MIB interface table.\n&quot;);
        return ERROR_SUCCESS;
    }

    // Disconnect from the MIB server to release the hMibSrv handle
    MprAdminMIBServerDisconnect(hMibSrv);

    if (dwRes != NO_ERROR)
        return ERROR_SUCCESS;
    
    if (pMibOpaqueInfo == NULL) 
        return ERROR_SUCCESS; 
    
    pIntfTable = (PMIB_IFTABLE)pMibOpaqueInfo->rgbyData;

    // Print out the name and description of each MIB interface in the table
    wprintf(L&quot;There were %d MIB table records found:\n&quot;, pIntfTable->dwNumEntries);
    for(UINT i=0; i < pIntfTable->dwNumEntries; i++){
        wprintf(L&quot;%d\t%s\t&quot;, i, pIntfTable->table[i].wszName, pIntfTable->table[i].bDescr);
        printf(&quot;%s\n&quot;, pIntfTable->table[i].bDescr);
    }

    return ERROR_SUCCESS;
}
```





## Related topics

<dl> <dt>

[**MIB\_OPAQUE\_INFO**](/windows/desktop/api/iprtrmib/ns-iprtrmib-mib_opaque_info)
</dt> <dt>

[**MIB\_OPAQUE\_QUERY**](/windows/desktop/api/iprtrmib/ns-iprtrmib-mib_opaque_query)
</dt> <dt>

[**MprAdminMIBEntryGet**](/windows/desktop/api/Mprapi/nf-mprapi-mpradminmibentryget)
</dt> </dl>

 

 