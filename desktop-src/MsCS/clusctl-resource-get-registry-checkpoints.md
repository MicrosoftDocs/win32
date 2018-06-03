---
title: CLUSCTL\_RESOURCE\_GET\_REGISTRY\_CHECKPOINTS control code
description: Retrieves a list of all the registry checkpoints set for a resource. Applications use this control code as a ClusterResourceControl parameter.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 06c990c9-bf73-44ff-aef8-c2da9a691519
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- CLUSCTL_RESOURCE_GET_REGISTRY_CHECKPOINTS control code Failover Cluster
topic_type:
- apiref
api_name:
- CLUSCTL_RESOURCE_GET_REGISTRY_CHECKPOINTS
api_location:
- ClusAPI.h
api_type:
- HeaderDef
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CLUSCTL\_RESOURCE\_GET\_REGISTRY\_CHECKPOINTS control code

Retrieves a list of all the registry [checkpoints](checkpointing.md) set for a [resource](resources.md). Applications use this [control code](about-control-codes.md) as a [**ClusterResourceControl**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clusterresourcecontrol) parameter.


```C++
ClusterResourceControl( hResource,            // resource handle
                        hHostNode,            // optional host node
                        CLUSCTL_RESOURCE_GET_REGISTRY_CHECKPOINTS,
                        NULL,                 // not used
                        0,                    // not used
                        lpOutBuffer,          // output buffer: array of strings
                        cbOutBufferSize,      // allocated buffer size (bytes)
                        lpcbBytesReturned );  // size of returned data (bytes)
```



## Parameters

The following control code function parameters are specific to this control code. For complete parameter descriptions, see [**ClusterResourceControl**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clusterresourcecontrol).

<dl> <dt>

*lpOutBuffer* 
</dt> <dd>

On a successful return, points to an array of null-terminated Unicode strings with an additional **NULL** terminator appended to the last string. Each string in the array contains a registry key that has previously been added to the resource's list of checkpoints with the [CLUSCTL\_RESOURCE\_ADD\_REGISTRY\_CHECKPOINT](clusctl-resource-add-registry-checkpoint.md) control code.

</dd> </dl>

## Return value

[**ClusterResourceControl**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clusterresourcecontrol) returns one of the following values:

<dl> <dt>

**ERROR\_SUCCESS**
</dt> <dd>

0

The operation was successful. The *lpcbBytesReturned* parameter points to the actual size of the returned data.

</dd> <dt>

**ERROR\_MORE\_DATA**
</dt> <dd>

234 (0xEA)

The output buffer pointed to by the *lpOutBuffer* parameter was not large enough to hold the data resulting from the operation. The *lpcbBytesReturned* parameter points to the size required for the output buffer.

</dd> <dt>

**[System error code](https://msdn.microsoft.com/library/windows/desktop/ms681381)**
</dt> <dd>

The operation failed. The value of *lpcbBytesReturned* is unreliable.

</dd> </dl>

## Remarks

If the *lpOutBuffer* parameter is **NULL** and the *cbOutBufferSize* parameter is zero, then **ERROR\_SUCCESS** may be returned, not **ERROR\_MORE\_DATA**.

ClusAPI.h defines the 32 bits of CLUSCTL\_RESOURCE\_GET\_REGISTRY\_CHECKPOINTS as follows (for more information, see [Control Code Architecture](control-code-architecture.md)).



| Component                 | Bit location     | Value                                                   |
|---------------------------|------------------|---------------------------------------------------------|
| Object code<br/>    | 24 31<br/> | **CLUS\_OBJECT\_RESOURCE** (0x1)<br/>             |
| Global bit<br/>     | 23<br/>    | **CLUS\_NOT\_GLOBAL** (0x0)<br/>                  |
| Modify bit<br/>     | 22<br/>    | **CLUS\_NO\_MODIFY** (0x0)<br/>                   |
| User bit<br/>       | 21<br/>    | **CLCTL\_CLUSTER\_BASE** (0x0)<br/>               |
| Type bit<br/>       | 20<br/>    | External (0x0)<br/>                               |
| Operation code<br/> | 0 23<br/>  | **CLCTL\_GET\_REGISTRY\_CHECKPOINTS** (0xa9)<br/> |
| Access code<br/>    | 0 1<br/>   | **CLUS\_ACCESS\_READ** (0x1)<br/>                 |



 

### Resource DLL Support

The CLUSCTL\_RESOURCE\_GET\_REGISTRY\_CHECKPOINTS control code is handled by the [Cluster service](cluster-service.md) and is not passed to [resource DLLs](resource-dlls.md).

## Examples


```C++
#include <windows.h>

//////////////////////////////////////////////////////////////////////

#include "ClusDocEx.h"

//////////////////////////////////////////////////////////////////////

#ifndef _CLUSDOCEX_RESGETREGISTRYCHECKPOINTS_CPP
#define _CLUSDOCEX_RESGETREGISTRYCHECKPOINTS_CPP

LPVOID ClusDocEx_ResGetRegistryCheckpoints
(
    IN HRESOURCE hRes,
    IN HNODE     hNode,
    OUT LPDWORD  lpcbDataSize
)
// ====================================================================
// 
// Description:
// 
//     Retrieves the current registry checkpoints of a resource
//     using CLUSCTL_RESOURCE_GET_REGISTRY_CHECKPOINTS.
//     
// >!! Call LocalFree on the returned pointer to free the memory. !!<
// 
// 
// Arguments:
// 
//    IN HRESOURCE hRes           Handle to the resource to query.
//                                
//    IN HNODE     hNode          Handle to the node to perform the
//                                operation or NULL to default to
//                                the owner node.
// 
//    OUT LPDWORD  lpcbDataSize   Returns the byte size of the
//                                resulting data.
// 
// Return Value:
// 
//    If successful, returns a string array containing the
//    checkpointed registry keys currently established for
//    the resource identified by hRes.
// 
//    If unsuccessful, returns a NULL pointer; 
//    call GetLastError() for details.
// 
// 
// Local Variables:
// 
//    dwResult        Captures return values.
//    cbBufSize       Allocated byte size of the output buffer.
//    lpOutBuffer     Output buffer for the control code operation.
//    dwControlCode   Specifies the operation to perform.
// 
// ====================================================================
{
    DWORD  dwResult      = ERROR_SUCCESS;
    DWORD  cbBufSize     = ClusDocEx_DEFAULT_CB;
    LPVOID lpOutBuffer   = NULL;
    DWORD  dwControlCode = CLUSCTL_RESOURCE_GET_REGISTRY_CHECKPOINTS;

    lpOutBuffer = LocalAlloc( LPTR, cbBufSize );

    if( lpOutBuffer == NULL )
    {
        dwResult = GetLastError();
        goto endf;
    }

//
//  1.  Call the control code function:  
//
    dwResult = ClusterResourceControl(
                   hRes,            // Resource to query.
                   hNode,           // Node to perform operation.
                   dwControlCode,   // Control code.
                   NULL,            // Input buffer (not used).
                   0,               // Input buffer size (not used).
                   lpOutBuffer,     // Output buffer.
                   cbBufSize,       // Byte size of the buffer.
                   lpcbDataSize     // Byte size of the resulting data.
               );

//
//  2.  Reallocate if necessary. If the buffer was too small, 
//      lpcbDataSize now indicates the necessary byte size.
//
    if ( dwResult == ERROR_MORE_DATA )
    {
        LocalFree( lpOutBuffer );

        cbBufSize = *lpcbDataSize;

        lpOutBuffer = LocalAlloc( LPTR, cbBufSize );

        if( lpOutBuffer == NULL )
        {
            dwResult = GetLastError();
            goto endf;
        }

        dwResult =
            ClusterResourceControl(
                   hRes,            // Resource to query.
                   hNode,           // Node to perform operation.
                   dwControlCode,   // Control code.
                   NULL,            // Input buffer (not used).
                   0,               // Input buffer size (not used).
                   lpOutBuffer,     // Output buffer.
                   cbBufSize,       // Byte size of the buffer.
                   lpcbDataSize     // Byte size of the resulting data.
            );

    }

//
//  3.  Handle errors.
//
    if( dwResult != ERROR_SUCCESS )
    {
        LocalFree( lpOutBuffer );
        lpOutBuffer = NULL;
        *lpcbDataSize = 0;
    }


endf:

    SetLastError( dwResult );

    return lpOutBuffer;  // Call LocalFree to release the memory.

//
//  The calling function will need to parse the returned buffer
//  to read individual key names from the array. 
//

}

#endif

// end ClusDocEx_ResGetRegistryCheckpoints
```



## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                            |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>            |
| Header<br/>                   | <dl> <dt>ClusAPI.h</dt> </dl> |



## See also

<dl> <dt>

[**ClusterResourceControl**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clusterresourcecontrol)
</dt> <dt>

[**ResourceControl**](/previous-versions/windows/desktop/api/ResApi/nc-resapi-presource_control_routine)
</dt> </dl>

 

 





