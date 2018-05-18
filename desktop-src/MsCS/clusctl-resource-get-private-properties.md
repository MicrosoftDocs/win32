---
title: CLUSCTL\_RESOURCE\_GET\_PRIVATE\_PROPERTIES control code
description: Retrieves the read/write private properties for a resource. Applications use this control code as a ClusterResourceControl parameter, and resource DLLs receive the control code as a ResourceControl parameter.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '27d7169a-b336-466e-a978-c55e90e80ea3'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["CLUSCTL_RESOURCE_GET_PRIVATE_PROPERTIES control code Failover Cluster"]
topic_type:
- apiref
api_name:
- CLUSCTL_RESOURCE_GET_PRIVATE_PROPERTIES
api_location:
- ClusAPI.h
api_type:
- HeaderDef
---

# CLUSCTL\_RESOURCE\_GET\_PRIVATE\_PROPERTIES control code

Retrieves the read/write [private properties](private-properties.md) for a [resource](resources.md). Applications use this [control code](about-control-codes.md) as a [**ClusterResourceControl**](clusterresourcecontrol.md) parameter, and [resource DLLs](resource-dlls.md) receive the control code as a [**ResourceControl**](resourcecontrol.md) parameter.


```C++
ClusterResourceControl( 
  hResource,                                         // resource handle
  hHostNode,                                         // optional host node
  CLUSCTL_RESOURCE_GET_PRIVATE_PROPERTIES,           // this control code
  NULL,                                              // input buffer (not used)
  0,                                                 // input buffer size (not used)
  lpOutBuffer,                                       // output buffer: property list
  cbOutBufferSize,                                   // allocated buffer size (bytes)
  lpcbBytesReturned );                               // actual size of resulting data (bytes)
```



## Parameters

The following control code function and DLL support parameters are specific to this control code. For complete parameter descriptions, see [**ClusterResourceControl**](clusterresourcecontrol.md) or [**ResourceControl**](resourcecontrol.md).

<dl> <dt>

*lpOutBuffer* 
</dt> <dd>

On a successful return, points to a [property list](property-lists.md) containing the resource's read/write private properties

</dd> </dl>

## Return value

[**ClusterResourceControl**](clusterresourcecontrol.md) returns one of the following values:

<dl> <dt>

**ERROR\_SUCCESS**
</dt> <dd>

The operation was successful. The *lpcbBytesReturned* parameter points to the actual size of the returned data.

</dd> <dt>

**ERROR\_MORE\_DATA**
</dt> <dd>

The output buffer pointed to by *lpOutBuffer* was not large enough to hold the data resulting from the operation. The *lpcbBytesReturned* parameter points to the size required for the output buffer.

</dd> <dt>

**[System error code](https://msdn.microsoft.com/library/windows/desktop/ms681381)**
</dt> <dd>

The operation failed. The value of *lpcbBytesReturned* is unreliable.

</dd> </dl>

Implementations of [**ResourceControl**](resourcecontrol.md) can return the above values or the following value:

<dl> <dt>

**ERROR\_INVALID\_FUNCTION**
</dt> <dd>

Requests that the [Resource Monitor](resource-monitor.md) perform default processing (if any) for the control code addition to processing supplied by the DLL (if any).

</dd> </dl>

## Remarks

Do not use the CLUSCTL\_RESOURCE\_GET\_PRIVATE\_PROPERTIES control code in any resource DLL entry point function. This control code can safely be called from a worker thread. For more information, see [Function Calls to Avoid in Resource DLLs](function-calls-to-avoid-in-resource-dlls.md).

ClusAPI.h defines the 32 bits of CLUSCTL\_RESOURCE\_GET\_PRIVATE\_PROPERTIES as follows (for more information, see [Control Code Architecture](control-code-architecture.md)).



| Component      | Bit location | Value                                                 |
|----------------|--------------|-------------------------------------------------------|
| Object code    | 24–31        | **CLUS\_OBJECT\_RESOURCE** (0x1)<br/>           |
| Global bit     | 23           | **CLUS\_NOT\_GLOBAL** (0x0)<br/>                |
| Modify bit     | 22           | **CLUS\_NO\_MODIFY** (0x0)<br/>                 |
| User bit       | 21           | **CLCTL\_CLUSTER\_BASE** (0x0)<br/>             |
| Type bit       | 20           | External (0x0)<br/>                             |
| Operation code | 0–23         | **CLCTL\_GET\_PRIVATE\_PROPERTIES** (0x81)<br/> |
| Access code    | 0–1          | **CLUS\_ACCESS\_READ** (0x1)<br/>               |



 

### Resource DLL Support

Required. Always support CLUSCTL\_RESOURCE\_GET\_PRIVATE\_PROPERTIES in your implementation of [**ResourceControl**](resourcecontrol.md). Return a [property list](property-lists.md) that includes the names and data values for all of the resource-specific read/write private properties. Remember to terminate the list with CLUSPROP\_SYNTAX\_ENDMARK. For more information on working with property lists, see [Creating Property Lists](creating-property-lists.md).

As a general guideline, the Resource Monitor should handle all of the control codes for [common properties](common-properties.md), while your DLL should handle all control codes for [private properties](private-properties.md).

For more information on the [**ResourceControl**](resourcecontrol.md) entry point function, see [Implementing ResourceControl](implementing-resourcecontrol.md).

## Examples


```C++
#include <windows.h>

//////////////////////////////////////////////////////////////////////

#include "ClusDocEx.h"

//////////////////////////////////////////////////////////////////////

#ifndef _CLUSDOCEX_RESGETRWPPROPS_CPP
#define _CLUSDOCEX_RESGETRWPPROPS_CPP

LPVOID ClusDocEx_ResGetRWPProperties
(
    IN HRESOURCE hRes,
    IN HNODE     hNode,
    OUT LPDWORD  lpcbDataSize
)
// ====================================================================
// 
// Description:
// 
//     Retrieves the read-write private properties of a resource
//     using CLUSCTL_RESOURCE_GET_PRIVATE_PROPERTIES.
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
//    If successful, returns a property list containing the
//    read-write private properties of the resource identified
//    by hRes.
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
    DWORD  dwControlCode = CLUSCTL_RESOURCE_GET_PRIVATE_PROPERTIES;

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
//  The calling function will need to parse the property list to
//  extract the property names and values.
//
//  See "Parsing Property Lists" for procedures and an example.
//

}

#endif

// end ClusDocEx_ResGetRWPProperties
```



## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                            |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>            |
| Header<br/>                   | <dl> <dt>ClusAPI.h</dt> </dl> |



## See also

<dl> <dt>

[**ClusterResourceControl**](clusterresourcecontrol.md)
</dt> <dt>

[**ResourceControl**](resourcecontrol.md)
</dt> </dl>

 

 





