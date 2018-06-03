---
title: CLUSCTL\_RESOURCE\_GET\_NAME control code
description: Retrieves the name of a resource.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: d1d4b8cf-ab74-449c-aaf7-9bc7ef09b789
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- CLUSCTL_RESOURCE_GET_NAME control code Failover Cluster
topic_type:
- apiref
api_name:
- CLUSCTL_RESOURCE_GET_NAME
api_location:
- ClusAPI.h
api_type:
- HeaderDef
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CLUSCTL\_RESOURCE\_GET\_NAME control code

Retrieves the name of a [resource](resources.md). Applications use this [control code](about-control-codes.md) as a [**ClusterResourceControl**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clusterresourcecontrol) parameter.


```C++
ClusterResourceControl( 
  hResource,                                         // resource handle
  hHostNode,                                         // optional host node
  CLUSCTL_RESOURCE_GET_NAME,                         // this control code
  NULL,                                              // input buffer (not used)
  0,                                                 // input buffer size (not used)
  lpOutBuffer,                                       // output buffer: string
  cbOutBufferSize,                                   // allocated buffer size (bytes)
  lpcbBytesReturned );                               // actual size of resulting data (bytes)
```



## Parameters

The following control code function parameter is specific to this control code. For complete parameter descriptions, see [**ClusterResourceControl**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clusterresourcecontrol).

<dl> <dt>

*lpOutBuffer* 
</dt> <dd>

On a successful return, points to a null-terminated Unicode string containing the name of the resource.

</dd> </dl>

## Return value

[**ClusterResourceControl**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clusterresourcecontrol) returns one of the following values.

<dl> <dt>

**ERROR\_SUCCESS**
</dt> <dd>

0

The operation completed successfully. The *lpcbBytesReturned* parameter points to the actual size of the returned data.

</dd> <dt>

**ERROR\_MORE\_DATA**
</dt> <dd>

234 (0xEA)

The output buffer pointed to by *lpOutBuffer* was not large enough to hold the data resulting from the operation. The *lpcbBytesReturned* parameter points to the size required for the output buffer.

</dd> <dt>

**[System error code](https://msdn.microsoft.com/library/windows/desktop/ms681381)**
</dt> <dd>

If any other value is returned, then the operation failed. The value of *lpcbBytesReturned* is unreliable.

</dd> </dl>

## Remarks

The name of a resource is stored in the [**Name**](resources-name.md) property. To retrieve the **Name** property along with the other read-only [resource common properties](resource-common-properties.md), use the [CLUSCTL\_RESOURCE\_GET\_RO\_COMMON\_PROPERTIES](clusctl-resource-get-ro-common-properties.md) control code.

Do not use the CLUSCTL\_RESOURCE\_GET\_NAME control code in any resource DLL entry point function. This control code can safely be called from a worker thread. For more information, see [Function Calls to Avoid in Resource DLLs](function-calls-to-avoid-in-resource-dlls.md).

ClusAPI.h defines the 32 bits of CLUSCTL\_RESOURCE\_GET\_NAME as follows (for more information, see [Control Code Architecture](control-code-architecture.md)).



| Component      | Bit location | Value                                       |
|----------------|--------------|---------------------------------------------|
| Object code    | 24 31        | **CLUS\_OBJECT\_RESOURCE** (0x1)<br/> |
| Global bit     | 23           | **CLUS\_NOT\_GLOBAL** (0x0)<br/>      |
| Modify bit     | 22           | **CLUS\_NO\_MODIFY** (0x0)<br/>       |
| User bit       | 21           | **CLCTL\_CLUSTER\_BASE** (0x0)<br/>   |
| Type bit       | 20           | External (0x0)<br/>                   |
| Operation code | 0 23         | **CLCTL\_GET\_NAME** (0x29)<br/>      |
| Access code    | 0 1          | **CLUS\_ACCESS\_READ** (0x1)<br/>     |



 

### Resource DLL Support

The CLUSCTL\_RESOURCE\_GET\_NAME control code is handled by the [Cluster service](cluster-service.md) and is not passed to [resource DLLs](resource-dlls.md).

## Examples


```C++
#include <windows.h>
#include <ClusApi.h>

//////////////////////////////////////////////////////////////////////

#include "ClusDocEx.h"

//////////////////////////////////////////////////////////////////////

#ifndef _CLUSDOCEX_RESGETNAME_CPP
#define _CLUSDOCEX_RESGETNAME_CPP

LPWSTR ClusDocEx_ResGetName
(
    IN HRESOURCE hRes,
    IN HNODE     hNode
)
// ====================================================================
// 
// Description:
// 
//     Retrieves the name of a resource
//     using CLUSCTL_RESOURCE_GET_NAME. 
//     
// 
//     Call LocalFree on the returned pointer to free the memory
// 
// 
// Arguments:
// 
//     IN HRESOURCE hRes       Handle to the resource to affect.
// 
//     IN HNODE     hNode      Optional handle to the node that
//                             owns the resource.
// 
// Return Value:
// 
//     If successful, the name of the resource.
//     If not, a NULL pointer; call GetLastError() for details.
// 
// 
// Local Variables:
// 
//     dwResult      Captures return values.
// 
//     cbBufSize     Byte size of the output buffer.
// 
//     cbResultSize  Actual size of the resulting data.
// 
//     lpszName      Output buffer for the control code operation.
//                   Used as the return value.
// 
// ====================================================================
{
    DWORD  dwResult     = ERROR_SUCCESS;
    DWORD  cbBufSize    = ClusDocEx_DEFAULT_CB;
    DWORD  cbResultSize = 0;
    LPWSTR lpszName     = NULL;

//--------------------------------------------------------------------
//  Allocate the output buffer.
//--------------------------------------------------------------------

    lpszName = (LPWSTR) LocalAlloc( LPTR, cbBufSize );

    if( lpszName == NULL )
    {
        dwResult = GetLastError();
        goto endf;
    }


//--------------------------------------------------------------------
//  Call the control code function.
//--------------------------------------------------------------------
//
//  Use the output configuration:  
//

    dwResult = ClusterResourceControl(
                   hRes,
                   hNode,
                   CLUSCTL_RESOURCE_GET_RESOURCE_TYPE,
                   NULL,
                   0,
                   (LPVOID) lpszName,
                   cbBufSize,
                   &amp;cbResultSize );


//--------------------------------------------------------------------
//  Reallocation routine.
//--------------------------------------------------------------------
//
//  If the buffer was too small, cbResultSize now indicates the
//  necessary byte size.
//
    if ( dwResult == ERROR_MORE_DATA )
    {
        LocalFree( lpszName );

        cbBufSize = cbResultSize;

        lpszName = (LPWSTR) LocalAlloc( LPTR, cbBufSize );

        dwResult = ClusterResourceControl(
                       hRes,
                       hNode,
                       CLUSCTL_RESOURCE_GET_RESOURCE_TYPE,
                       NULL,
                       0,
                       (LPVOID) lpszName,
                       cbBufSize,
                       &amp;cbResultSize );
    }


endf:

    SetLastError( dwResult );

    return lpszName;
}

#endif

// end ClusDocEx_ResGetName
```



## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                            |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>            |
| Header<br/>                   | <dl> <dt>ClusAPI.h</dt> </dl> |



## See also

<dl> <dt>

[External Resource Control Codes](external-resource-control-codes.md)
</dt> <dt>

[CLUSCTL\_RESOURCE\_GET\_RO\_COMMON\_PROPERTIES](clusctl-resource-get-ro-common-properties.md)
</dt> <dt>

[**ClusterResourceControl**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clusterresourcecontrol)
</dt> <dt>

[**Name**](resources-name.md)
</dt> <dt>

[**ResourceControl**](/previous-versions/windows/desktop/api/ResApi/nc-resapi-presource_control_routine)
</dt> </dl>

 

 





