---
title: Changing the Cluster Configuration with Control Codes
description: Failover Cluster API code example for using an input control code.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'bca4e822-ef41-41c5-bbec-295fbf42cbd8'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["control codes Failover Cluster ,changing the cluster configuration"]
---

# Changing the Cluster Configuration with Control Codes

[Control codes](about-control-codes.md) that send data to the [*cluster*](c-gly.md#-wolf-cluster-gly) in the [control code function's](control-code-functions.md) input buffer use the following procedure:

**To use an "input" control code**

1.  Refer to the control code reference to determine what data must be passed in the input buffer and what the format should be. You may need to construct a [value list](value-lists.md) or [property list](property-lists.md) and pass that as the input buffer. See [Creating Property Lists](creating-property-lists.md) and [Creating Value Lists](creating-value-lists.md) for more information.
2.  Allocate and populate the input buffer.
3.  Call the function.
4.  Test the return value and take appropriate action based on success/failure.

## Example

The following example demonstrates the use of the "input" control code [CLUSCTL\_RESOURCE\_SET\_NAME](clusctl-resource-set-name.md).


```C++
#include <windows.h>
//////////////////////////////////////////////////////////////////////

#include "ClusDocEx.h"    

//////////////////////////////////////////////////////////////////////

#ifndef _CLUSDOCEX_RESSETNAME_CPP
#define _CLUSDOCEX_RESSETNAME_CPP

//--------------------------------------------------------------------
//
//  ClusDocEx_SetResourceName
//
//      Changes the name of a resource.
//
//  Arguments:
//
//      HRESOURCE hResource       Handle to the resource.
//
//      LPWSTR    lpszResName     New resource name.
//
//  Return Value:
//
//      If successful, ERROR_SUCCESS, otherwise an error code.
//
//--------------------------------------------------------------------
DWORD ClusDocEx_SetResourceName
(
    HRESOURCE hResource,
    LPWSTR    lpszResName
)
{
    DWORD dwResult = ERROR_SUCCESS;

    if( ( hResource != NULL ) || ( lpszResName != NULL ) )
    {
        DWORD cbNameSize = ( lstrlenW( lpszResName ) + 1 ) * 
                           sizeof( WCHAR );

        dwResult = ClusterResourceControl( hResource,
                                           NULL,
                                           CLUSCTL_RESOURCE_SET_NAME,
                                           lpszResName,
                                           cbNameSize,
                                           NULL,
                                           0,
                                           NULL );

    }
    else
    {
        dwResult = ERROR_BAD_ARGUMENTS;
    }

    return dwResult;
}
#endif
```



 

 




