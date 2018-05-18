---
title: CLUSCTL\_RESOURCE\_GET\_REQUIRED\_DEPENDENCIES control code
description: Retrieves a list of all required dependencies for a resource.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '4bf78e9c-a6da-453c-a199-9ec73fc5dafe'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["CLUSCTL_RESOURCE_GET_REQUIRED_DEPENDENCIES control code Failover Cluster"]
topic_type:
- apiref
api_name:
- CLUSCTL_RESOURCE_GET_REQUIRED_DEPENDENCIES
api_location:
- ClusAPI.h
api_type:
- HeaderDef
---

# CLUSCTL\_RESOURCE\_GET\_REQUIRED\_DEPENDENCIES control code

Retrieves a list of all required [dependencies](resource-dependencies.md) for a [resource](resources.md). Applications use this [control code](about-control-codes.md) as a [**ClusterResourceControl**](clusterresourcecontrol.md) parameter, and [resource DLLs](resource-dlls.md) receive the control code as a parameter to the [**ResourceControl**](resourcecontrol.md) function.


```C++
ClusterResourceControl( 
  hResource,                                  // resource handle
  hHostNode,                                  // optional host node
  CLUSCTL_RESOURCE_GET_REQUIRED_DEPENDENCIES, // this control code
  NULL,                                       // not used
  0,                                          // not used
  lpOutBuffer,                                // output buffer: value list
  cbOutBufferSize,                            // buffer size (bytes)
  lpcbBytesReturned );                        // returned data size (bytes)
```



## Parameters

The following control code function and DLL support parameter is specific to this control code. For complete parameter descriptions, see [**ClusterResourceControl**](clusterresourcecontrol.md) or [**ResourceControl**](resourcecontrol.md).

<dl> <dt>

*lpOutBuffer* 
</dt> <dd>

On a successful return, points to a [value list](value-lists.md) containing a [**CLUSPROP\_REQUIRED\_DEPENDENCY**](clusprop-required-dependency.md) union for each dependency.

</dd> </dl>

## Return value

[**ClusterResourceControl**](clusterresourcecontrol.md) returns one of the following values.

<dl> <dt>

**ERROR\_SUCCESS**
</dt> <dd>

0

The operation completed successfully. The *lpcbBytesReturned* parameter points to the actual size of the returned data.

</dd> <dt>

**ERROR\_MORE\_DATA**
</dt> <dd>

234 (0xEA)

More data is available. The output buffer pointed to by *lpOutBuffer* was not large enough to hold the data resulting from the operation. The *lpcbBytesReturned* parameter points to the size required for the output buffer.

</dd> <dt>

**[System error code](https://msdn.microsoft.com/library/windows/desktop/ms681381)**
</dt> <dd>

If any other value is returned, then the operation failed. The value of *lpcbBytesReturned* is unreliable.

</dd> </dl>

Implementations of [**ResourceControl**](resourcecontrol.md) can return the above values or the following value.

<dl> <dt>

**ERROR\_INVALID\_FUNCTION**
</dt> <dd>

1

Invalid function. Requests that the Resource Monitor perform default processing (if any) for the control code addition to processing supplied by the DLL (if any).

</dd> </dl>

## Remarks

For examples of using CLUSCTL\_RESOURCE\_GET\_REQUIRED\_DEPENDENCIES, see [Creating a Value List](creating-value-lists.md) and [Parsing a Value List](parsing-a-value-list.md).

ClusAPI.h defines the 32 bits of CLUSCTL\_RESOURCE\_GET\_REQUIRED\_DEPENDENCIES as follows (for more information, see [Control Code Architecture](control-code-architecture.md)).



| Component      | Bit location | Value                                                    |
|----------------|--------------|----------------------------------------------------------|
| Object code    | 24–31        | **CLUS\_OBJECT\_RESOURCE** (0x1)<br/>              |
| Global bit     | 23           | **CLUS\_NOT\_GLOBAL** (0x0)<br/>                   |
| Modify bit     | 22           | **CLUS\_NO\_MODIFY** (0x0)<br/>                    |
| User bit       | 21           | **CLCTL\_CLUSTER\_BASE** (0x0)<br/>                |
| Type bit       | 20           | External (0x0)<br/>                                |
| Operation code | 0–23         | **CLCTL\_GET\_REQUIRED\_DEPENDENCIES** (0x11)<br/> |
| Access code    | 0–1          | **CLUS\_ACCESS\_READ** (0x1)<br/>                  |



 

### Resource DLL Support

Conditional. If your resource has required dependencies, you must support the CLUSCTL\_RESOURCE\_GET\_REQUIRED\_DEPENDENCIES control code in your implementation of [**ResourceControl**](resourcecontrol.md). Return a value list containing one [**CLUSPROP\_REQUIRED\_DEPENDENCY**](clusprop-required-dependency.md) union for each resource on which your resource is required to depend. Remember to terminate the list with **CLUSPROP\_SYNTAX\_ENDMARK**.

For example, if your resource has required dependencies on a [*storage class resource*](s-gly.md#-wolf-storage-class-resource-gly) and a [Network Name](network-name.md) resource, [**ResourceControl**](resourcecontrol.md) should return a value list with three entries:

-   A [**CLUSPROP\_REQUIRED\_DEPENDENCY**](clusprop-required-dependency.md) union with the **ResClass** member set to **CLUS\_RESCLASS\_STORAGE**.
-   A [**CLUSPROP\_REQUIRED\_DEPENDENCY**](clusprop-required-dependency.md) union with the **ResTypeName** member set to "Network Name".
-   A [**CLUSPROP\_VALUE**](clusprop-value.md) structure with the Syntax member set to **CLUSPROP\_SYNTAX\_ENDMARK**.

The [Resource Monitor](resource-monitor.md) provides no default processing.

For more information on the [**ResourceControl**](resourcecontrol.md) entry point function, see [Implementing ResourceControl](implementing-resourcecontrol.md).

## Examples


```C++
#include <windows.h>
#include <ClusApi.h>

//////////////////////////////////////////////////////////////////////

#include "ClusDocEx.h"

//////////////////////////////////////////////////////////////////////

#ifndef _CLUSDOCEX_RESGETREQDEPS_CPP
#define _CLUSDOCEX_RESGETREQDEPS_CPP


LPVOID ClusDocEx_ResGetRequiredDependencies
(
    IN HRESOURCE hRes,
    IN HNODE     hNode,
    OUT LPDWORD  lpcbDataSize
)
// ====================================================================
// 
// Description:
// 
//     Retrieves the required dependencies of a resource
//     using CLUSCTL_RESOURCE_GET_REQUIRED_DEPENDENCIES.
//     Note that the resource DLL that manages the resource
//     is responsible for returning the resource's required 
//     dependencies. 
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
//                                resulting value list.
// 
// Return Value:
// 
//    If successful, returns a value list containing a
//    CLUSPROP_REQUIRED_DEPENDENCY union for each resource that
//    hRes depends on.
// 
//    If unsuccessful, returns a NULL pointer; 
//    call GetLastError() for details.
// 
// 
// Local Variables:
// 
//    dwResult        Captures return values.
//    cbBufSize       Allocated byte size of the output buffer.
//    lpReqDeps       Output buffer for the control code operation.
//    dwControlCode   Specifies the operation to perform.
// 
// ====================================================================
{
    DWORD  dwResult      = ERROR_SUCCESS;
    DWORD  cbBufSize     = ClusDocEx_DEFAULT_CB;
    LPVOID lpReqDeps     = NULL;
    DWORD  dwControlCode = CLUSCTL_RESOURCE_GET_REQUIRED_DEPENDENCIES;

    lpReqDeps = LocalAlloc( LPTR, cbBufSize );

    if( lpReqDeps == NULL )
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
                   lpReqDeps,       // Output buffer.
                   cbBufSize,       // Byte size of the buffer.
                   lpcbDataSize     // Byte size of the resulting data.
               );

//
//  2.  Reallocate if necessary. If the buffer was too small, 
//      lpcbDataSize now indicates the necessary byte size.
//
    if ( dwResult == ERROR_MORE_DATA )
    {
        LocalFree( lpReqDeps );

        cbBufSize = *lpcbDataSize;

        lpReqDeps = LocalAlloc( LPTR, cbBufSize );

        if( lpReqDeps == NULL )
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
                   lpReqDeps,       // Output buffer.
                   cbBufSize,       // Byte size of the buffer.
                   lpcbDataSize     // Byte size of the resulting data.
            );

    }

//
//  3.  Handle errors.
//
    if( dwResult != ERROR_SUCCESS )
    {
        LocalFree( lpReqDeps );
        lpReqDeps = NULL;
        *lpcbDataSize = 0;
    }


endf:

    SetLastError( dwResult );

    return lpReqDeps;  // Call LocalFree to release the memory.

//
//  The calling function will need to parse the value list to
//  extract the resource type names and resource classes
//  that hRes depends on.
//
//  See "Parsing Value Lists" for procedures and an example.
//

}

#endif

// End ClusDocEx_ResGetRequiredDependencies.
```



## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                            |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>            |
| Header<br/>                   | <dl> <dt>ClusAPI.h</dt> </dl> |



## See also

<dl> <dt>

[External Resource Control Codes](external-resource-control-codes.md)
</dt> <dt>

[**ClusterResourceControl**](clusterresourcecontrol.md)
</dt> <dt>

[**ResourceControl**](resourcecontrol.md)
</dt> </dl>

 

 





