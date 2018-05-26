---
title: CLUSCTL\_RESOURCE\_GET\_RO\_COMMON\_PROPERTIES control code
description: Retrieves the read-only common properties for a resource.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: f9e8c9bb-9ece-4cc8-b271-63e29ab5b30a
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- CLUSCTL_RESOURCE_GET_RO_COMMON_PROPERTIES control code Failover Cluster
topic_type:
- apiref
api_name:
- CLUSCTL_RESOURCE_GET_RO_COMMON_PROPERTIES
api_location:
- ClusAPI.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# CLUSCTL\_RESOURCE\_GET\_RO\_COMMON\_PROPERTIES control code

Retrieves the read-only [common properties](common-properties.md) for a [resource](resources.md). Applications use this [control code](about-control-codes.md) as a [**ClusterResourceControl**](/windows/previous-versions/ClusAPI/nf-clusapi-clusterresourcecontrol?branch=master) parameter, and [resource DLLs](resource-dlls.md) receive the control code as a [**ResourceControl**](/windows/previous-versions/ResApi/nc-resapi-presource_control_routine?branch=master) parameter.


```C++
ClusterResourceControl( 
  hResource,                                         // resource handle
  hHostNode,                                         // optional host node
  CLUSCTL_RESOURCE_GET_RO_COMMON_PROPERTIES,         // this control code
  NULL,                                              // input buffer (not used)
  0,                                                 // input buffer size (not used)
  lpOutBuffer,                                       // output buffer: property list
  cbOutBufferSize,                                   // allocated buffer size (bytes)
  lpcbBytesReturned );                               // actual size of resulting data (bytes)
```



## Parameters

The following control code function and DLL support parameter is specific to this control code. For complete parameter descriptions, see [**ClusterResourceControl**](/windows/previous-versions/ClusAPI/nf-clusapi-clusterresourcecontrol?branch=master) or [**ResourceControl**](/windows/previous-versions/ResApi/nc-resapi-presource_control_routine?branch=master).

<dl> <dt>

*lpOutBuffer* 
</dt> <dd>

On a successful return, points to a [property list](property-lists.md) containing the resource's read-only [common resource properties](resource-common-properties.md).

</dd> </dl>

## Return value

[**ClusterResourceControl**](/windows/previous-versions/ClusAPI/nf-clusapi-clusterresourcecontrol?branch=master) returns one of the following values.

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

Implementations of [**ResourceControl**](/windows/previous-versions/ResApi/nc-resapi-presource_control_routine?branch=master) can return the above values or the following value.

<dl> <dt>

**ERROR\_INVALID\_FUNCTION**
</dt> <dd>

1

Incorrect function. Requests that the Resource Monitor perform default processing (if any) for the control code addition to processing supplied by the DLL (if any).

</dd> </dl>

## Remarks

For information on working with property lists, see [Using Property Lists](using-property-lists.md).

Do not use the CLUSCTL\_RESOURCE\_GET\_RO\_COMMON\_PROPERTIES control code in any resource DLL entry point function. This control code can safely be called from a worker thread. For more information, see [Function Calls to Avoid in Resource DLLs](function-calls-to-avoid-in-resource-dlls.md).

ClusAPI.h defines the 32 bits of CLUSCTL\_RESOURCE\_GET\_RO\_COMMON\_PROPERTIES as follows (for more information, see [Control Code Architecture](control-code-architecture.md)).



| Component      | Bit location | Value                                         |
|----------------|--------------|-----------------------------------------------|
| Object code    | 24 31        | **CLUS\_OBJECT\_RESOURCE** (0x1)              |
| Global bit     | 23           | **CLUS\_NOT\_GLOBAL** (0x0)                   |
| Modify bit     | 22           | **CLUS\_NO\_MODIFY** (0x0)                    |
| User bit       | 21           | **CLCTL\_CLUSTER\_BASE** (0x0)                |
| Type bit       | 20           | External (0x0)                                |
| Operation code | 0 23         | **CLCTL\_GET\_RO\_COMMON\_PROPERTIES** (0x55) |
| Access code    | 0 1          | **CLUS\_ACCESS\_READ** (0x1)                  |



 

### Resource DLL Support

Use default. Whether or not your implementation of [**ResourceControl**](/windows/previous-versions/ResApi/nc-resapi-presource_control_routine?branch=master) performs processing for CLUSCTL\_RESOURCE\_GET\_RO\_COMMON\_PROPERTIES, return ERROR\_INVALID\_FUNCTION to let the [Resource Monitor](resource-monitor.md) create the property list. The Resource Monitor will return a version-appropriate list of resource common properties.

As a general guideline, the Resource Monitor should handle all of the control codes for [common properties](common-properties.md), while your DLL should handle all control codes for [private properties](private-properties.md).

For more information on the [**ResourceControl**](/windows/previous-versions/ResApi/nc-resapi-presource_control_routine?branch=master) entry point, see [Implementing ResourceControl](implementing-resourcecontrol.md).

## Examples


```C++
#include <windows.h>
#include <ClusApi.h>

//////////////////////////////////////////////////////////////////////

#include "ClusDocEx.h"

//////////////////////////////////////////////////////////////////////

#ifndef _CLUSDOCEX_RESGETROCPROPS_CPP
#define _CLUSDOCEX_RESGETROCPROPS_CPP

LPVOID ClusDocEx_ResGetROCProperties
(
    IN HRESOURCE hRes,
    IN HNODE     hNode,
    OUT LPDWORD  lpcbDataSize
)
// ====================================================================
// 
// Description:
// 
//     Retrieves the read-only common properties of a resource
//     using CLUSCTL_RESOURCE_GET_RO_COMMON_PROPERTIES.
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
//    read-only common properties of the resource identified
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
    DWORD  dwControlCode = CLUSCTL_RESOURCE_GET_RO_COMMON_PROPERTIES;

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

// end ClusDocEx_ResGetROCProperties
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

[**ClusterResourceControl**](/windows/previous-versions/ClusAPI/nf-clusapi-clusterresourcecontrol?branch=master)
</dt> <dt>

[**Name**](resources-name.md)
</dt> <dt>

[**ResourceControl**](/windows/previous-versions/ResApi/nc-resapi-presource_control_routine?branch=master)
</dt> </dl>

 

 





