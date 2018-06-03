---
title: CLUSCTL\_RESOURCE\_GET\_RESOURCE\_TYPE control code
description: Retrieves the resource type name for a resource.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: ed679b50-306e-4623-aba3-bab64cd0e671
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- CLUSCTL_RESOURCE_GET_RESOURCE_TYPE control code Failover Cluster
topic_type:
- apiref
api_name:
- CLUSCTL_RESOURCE_GET_RESOURCE_TYPE
api_location:
- ClusAPI.h
api_type:
- HeaderDef
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CLUSCTL\_RESOURCE\_GET\_RESOURCE\_TYPE control code

Retrieves the [resource type](resource-types.md) name for a [resource](resources.md). Applications use this [control code](about-control-codes.md) as a [**ClusterResourceControl**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clusterresourcecontrol) parameter.


```C++
ClusterResourceControl( 
  hResource,                                         // resource handle
  hHostNode,                                         // optional host node
  CLUSCTL_RESOURCE_GET_RESOURCE_TYPE,                // this control code
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

On a successful return, points to a null-terminated Unicode string containing the resource type of the resource.

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

More data is available. The output buffer pointed to by *lpOutBuffer* was not large enough to hold the data resulting from the operation. The *lpcbBytesReturned* parameter points to the size required for the output buffer.

</dd> <dt>

**[System error code](https://msdn.microsoft.com/library/windows/desktop/ms681381)**
</dt> <dd>

If any other value is returned, then the operation failed. The value of *lpcbBytesReturned* is unreliable.

</dd> </dl>

## Remarks

The resource type name is stored in the [**Type**](resources-type.md) property. This is the registered name of the resource type, such as "File Share" or "Physical Disk", and not the display name. For information on the difference between registered and display names, see [Display Names](display-names.md).

Do not use the CLUSCTL\_RESOURCE\_GET\_RESOURCE\_TYPE control code in any resource DLL entry point function. This control code can safely be called from a worker thread. For more information, see [Function Calls to Avoid in Resource DLLs](function-calls-to-avoid-in-resource-dlls.md).

ClusAPI.h defines the 32 bits of CLUSCTL\_RESOURCE\_GET\_RESOURCE\_TYPE as follows (for more information, see [Control Code Architecture](control-code-architecture.md)).



| Component      | Bit location | Value                                            |
|----------------|--------------|--------------------------------------------------|
| Object code    | 24 31        | **CLUS\_OBJECT\_RESOURCE** (0x1)<br/>      |
| Global bit     | 23           | **CLUS\_NOT\_GLOBAL** (0x0)<br/>           |
| Modify bit     | 22           | **CLUS\_NO\_MODIFY** (0x0)<br/>            |
| User bit       | 21           | **CLCTL\_CLUSTER\_BASE** (0x0)<br/>        |
| Type bit       | 20           | External (0x0)<br/>                        |
| Operation code | 0 23         | **CLCTL\_GET\_RESOURCE\_TYPE** (0x2d)<br/> |
| Access code    | 0 1          | **CLUS\_ACCESS\_READ** (0x1)<br/>          |



 

### Resource DLL Support

The CLUSCTL\_RESOURCE\_GET\_RESOURCE\_TYPE control code is handled by the [Cluster service](cluster-service.md) and is not passed to [resource DLLs](resource-dlls.md).

## Examples


```C++
#include <windows.h>
#include <ClusApi.h>

//////////////////////////////////////////////////////////////////////

#include "ClusDocEx.h"

//////////////////////////////////////////////////////////////////////

#ifndef _CLUSDOCEX_RESGETTYPE_CPP
#define _CLUSDOCEX_RESGETTYPE_CPP

LPWSTR ClusDocEx_ResGetResourceType
(
    IN HRESOURCE hRes,
    IN HNODE     hNode
)
// ====================================================================
// 
// Description:
// 
//     Retrieves the resource type of a resource
//     using CLUSCTL_RESOURCE_GET_RESOURCE_TYPE.
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
// 
// Return Value:
// 
//    If successful, returns a string specifying the resource type
//    of the resource identified by hRes.
// 
//    If unsuccessful, returns a NULL pointer; 
//    call GetLastError() for details.
// 
// 
// Local Variables:
// 
//    dwResult        Captures return values.
//    cbBufSize       Allocated byte size of the output buffer.
//    cbDataSize      Actual byte size of the resulting data.
//    lpszType        Output buffer for the control code operation.
//    dwControlCode   Specifies the operation to perform.
// 
// ====================================================================
{
    DWORD  dwResult      = ERROR_SUCCESS;
    DWORD  cbBufSize     = ClusDocEx_DEFAULT_CB;
    DWORD  cbDataSize    = 0;
    LPWSTR lpszType      = NULL;
    DWORD  dwControlCode = CLUSCTL_RESOURCE_GET_RESOURCE_TYPE;

    lpszType = (LPWSTR) LocalAlloc( LPTR, cbBufSize );

    if( lpszType == NULL )
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
                   (LPVOID)lpszType,// Output buffer.
                   cbBufSize,       // Byte size of the buffer.
                   &amp;cbDataSize      // Byte size of the resulting data.
               );

//
//  2.  Reallocate if necessary. If the buffer was too small, 
//      cbDataSize now indicates the necessary byte size.
//
    if ( dwResult == ERROR_MORE_DATA )
    {
        LocalFree( lpszType );

        cbBufSize = cbDataSize;

        lpszType = (LPWSTR) LocalAlloc( LPTR, cbBufSize );

        if( lpszType == NULL )
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
                   (LPVOID)lpszType,// Output buffer.
                   cbBufSize,       // Byte size of the buffer.
                   &amp;cbDataSize      // Byte size of the resulting data.
            );

    }

//
//  3.  Handle errors.
//
    if( dwResult != ERROR_SUCCESS )
    {
        LocalFree( lpszType );
        lpszType = NULL;
    }


endf:

    SetLastError( dwResult );

    return lpszType;  // Call LocalFree to release the memory.

}

#endif

// end ClusDocEx_ResGetType
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

[**ClusterResourceControl**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clusterresourcecontrol)
</dt> <dt>

[**ResourceControl**](/previous-versions/windows/desktop/api/ResApi/nc-resapi-presource_control_routine)
</dt> <dt>

[**Type**](resources-type.md)
</dt> </dl>

 

 





