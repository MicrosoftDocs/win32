---
title: Getting Object Properties
description: An cluster object's properties determine its identity and behavior in the cluster. Applications typically retrieve an object's properties to discover how the object is currently configured.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: abeade46-e84a-445e-b91c-1e17b6c48179
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- cluster objects Failover Cluster ,retrieving properties
- properties Failover Cluster ,retrieving object properties
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Getting Object Properties

An [cluster object's](cluster-objects.md) properties determine its identity and behavior in the [*cluster*](https://www.bing.com/search?q=*cluster*). Applications typically retrieve an object's properties to discover how the object is currently configured.

The [Failover Cluster API](the-server-cluster-api.md) provides many ways to get the properties of an object. The [standard order of preference](standard-order-of-preference.md) for [cluster-aware applications](cluster-aware-applications.md) recommends using [control codes](about-control-codes.md) if possible. Therefore, the procedures described below use control codes exclusively. If you are writing a [resource DLL](resource-dlls.md), you should use the [cluster database access functions](cluster-database-access-functions.md) and the [cluster utility functions](cluster-utility-functions.md) to work with properties.

The following generalized procedure describes how to use control codes to retrieve the properties for any object. Substitute the name of the object (node, network, netinterface, group, resource, or restype ) for &lt;Object&gt;.

**To retrieve &lt;Object&gt; properties:**

1.  Allocate an output buffer to receive the property list.
2.  Call the [control code function](control-code-functions.md) for the object, **Cluster&lt;Object&gt;Control**, specifying one of the following [control codes](control-codes.md) as the *dwControlCode* parameter.

    

    | Properties to Retrieve                                                            | Control Code to Use                                   |
    |-----------------------------------------------------------------------------------|-------------------------------------------------------|
    | [Common](common-properties.md)[read/write](read-write-properties.md) properties | CLUSCTL\_&lt;OBJECT&gt;\_GET\_COMMON\_PROPERTIES      |
    | Common [read-only](read-only-properties.md) properties                           | CLUSCTL\_&lt;OBJECT&gt;\_GET\_RO\_COMMON\_PROPERTIES  |
    | [Private](private-properties.md) read/write properties                           | CLUSCTL\_&lt;OBJECT&gt;\_GET\_PRIVATE\_PROPERTIES     |
    | Private read-only properties                                                      | CLUSCTL\_&lt;OBJECT&gt;\_GET\_RO\_PRIVATE\_PROPERTIES |

    

     

    For more information on using control codes see [Getting Information with Control Codes](getting-information-with-control-codes.md).

3.  If **Cluster&lt;Object&gt;Control** returns **ERROR\_MORE\_DATA**, reallocate the output buffer according to the size returned by the *lpcbBytesReturned* parameter.
4.  If **Cluster&lt;Object&gt;Control** returns **ERROR\_SUCCESS**, the output buffer contains a property list for the object. Parse the property list to retrieve individual property names and values - see [Parsing Property Lists](parsing-property-lists.md).

To obtain a list of the [read/write](read-write-properties.md) [common](common-properties.md) or [private properties](private-properties.md) of an object, use the CLUSCTL\_&lt;OBJECT&gt;\_ENUM\_COMMON\_PROPERTIES and CLUSCTL\_&lt;OBJECT&gt;\_ENUM\_PRIVATE\_PROPERTIES control codes.

## Example Code

The following example retrieves the [read/write](read-write-properties.md) [common properties](common-properties.md) of a [resource](resources.md) and returns the value of a specified property. This example calls other example functions presented elsewhere in this documentation. To locate these example functions, see the [Index of Examples](index-of-examples.md).


```C++
#include <windows.h>

//////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////

#include "ClusDocEx.h"

//////////////////////////////////////////////////////////////////////

#ifndef _CLUSDOCEX_RESGETRWCDWORDPROPERTY_CPP
#define _CLUSDOCEX_RESGETRWCDWORDPROPERTY_CPP
//--------------------------------------------------------------------
//
//  ClusDocEx_ResGetRWCDwordProperty
//
//  Retrieves the value of a specified read-write common resource
//  property of type DWORD.
//
//  Arguments:
//
//      IN  LPWSTR  lpszResName    Name of the resource.
//
//      IN  LPWSTR  lpszPropName   Name of the read-write common 
//                                 DWORD property to get.
//
//      OUT LPDWORD lpdwPropValue  Returns the property value.
//
//  Return Value:
//      System error code
//  
//--------------------------------------------------------------------
DWORD ClusDocEx_ResGetRWCDwordProperty(
    IN LPWSTR lpszResName, 
    IN LPWSTR lpszPropName,
    OUT LPDWORD lpdwPropValue
)
{
    HCLUSTER hCluster = NULL;
    HRESOURCE hResource = NULL;
    LPVOID lpPropList = NULL;
    DWORD dwResult = ERROR_SUCCESS; 
    DWORD cbPropListSize = 0;
        

//  For the ClusDocEx_OpenLocalClusterWithName function, 
//  see "Using Object Handles".

    hCluster = ClusDocEx_OpenLocalClusterWithName();

    if( hCluster == NULL )
    {
        goto endf;
    }

    hResource = OpenClusterResource( hCluster, lpszResName );

    if( hResource == NULL )
    {
        goto endf;
    }


//  For the ClusDocEx_ResGetControlCodeOutput function, 
//  see "Getting Information with "Control Codes".

    lpPropList = ClusDocEx_ResGetControlCodeOutput(
                     hResource,
                     NULL,
                     CLUSCTL_RESOURCE_GET_COMMON_PROPERTIES,
                     &amp;cbPropListSize );

    if( dwResult != ERROR_SUCCESS )
    {
        goto endf;
    }


//  ResUtilFindDwordProperty is one of the cluster utility functions.

    dwResult = ResUtilFindDwordProperty(
                   lpPropList,
                   cbPropListSize,
                   lpszPropName,
                   lpdwPropValue );

endf:

    if( dwResult != ERROR_SUCCESS )
    {
        ClusDocEx_DebugPrint( L"ClusDocEx_ResGetRWCDwordProperty", dwResult );
    }


//  Free the buffer allocated by ClusDocEx_ResGetControlCodeOutput.

    LocalFree( lpPropList );

    if( hResource ) CloseClusterResource( hResource );

    if( hCluster ) CloseCluster( hCluster );

    return dwResult;
}
//  end ClusDocEx_ResGetRWCDwordProperty
//--------------------------------------------------------------------
#endif
```



 

 




