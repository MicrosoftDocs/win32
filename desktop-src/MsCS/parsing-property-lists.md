---
title: Parsing Property Lists
description: The recommended way to parse a property list is to use one of the property list parsing functions to locate a specific type of value. Both cluster-aware applications and resource DLLs can use these functions.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: fde017dc-fcc8-4b34-a56a-85f052306569
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- property lists Failover Cluster ,parsing
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Parsing Property Lists

The recommended way to parse a [property list](property-lists.md) is to use one of the [property list parsing functions](property-list-parsing-functions.md) to locate a specific type of value. Both [*cluster-aware applications*](c-gly.md#-wolf-cluster-aware-application-gly) and [resource DLLs](resource-dlls.md) can use these functions.

If no parsing function exists for the type of data you are seeking, you can parse the property list with [**CLUSPROP\_BUFFER\_HELPER**](/windows/previous-versions/ClusAPI/ns-clusapi-clusprop_buffer_helper?branch=master) (see [Using CLUSPROP\_BUFFER\_HELPER](using-clusprop-buffer-helper.md)).


```C++
#include <windows.h>

//////////////////////////////////////////////////////////////////////

#include "ClusDocEx.h"

//////////////////////////////////////////////////////////////////////

#ifndef _CLUSDOCEX_GRPGETRWCDWPROPVALUE_CPP
#define _CLUSDOCEX_GRPGETRWCDWPROPVALUE_CPP
//--------------------------------------------------------------------
//
//  ClusDocEx_GrpGetRWCDwPropValue
//
//  Retrieves a read-write common (RWC) group property value
//  of type DWORD.
//
//  Arguments:
//      IN HGROUP hGroup            Handle to the group.
//      IN LPWSTR lpszPropName      Name of property to find.
//      OUT LPDWORD lpdwPropValue   Returns the value of property.
//
// Return Value:
//      System error code
//
//--------------------------------------------------------------------
DWORD GrpGetRWCDwPropValue( 
    IN HGROUP hGroup,
    IN LPCWSTR lpszPropName,
    OUT LPDWORD lpdwPropValue
)
{
    DWORD dwResult = ERROR_SUCCESS;
    DWORD cbPropListSize = 0;

//  Retrieve a property list

    LPVOID lpPropList = ClusDocEx_GrpGetControlCodeOutput(
                            hGroup,
                            NULL,
                            CLUSCTL_GROUP_GET_COMMON_PROPERTIES,
                            &amp;cbPropListSize );

    if( lpPropList != NULL )
    {

    //  Parse the property list for the property specified
    //  by lpszPropName.

        dwResult = ResUtilFindDwordProperty( 
                       lpPropList, 
                       cbPropListSize, 
                       lpszPropName, 
                       lpdwPropValue );

        if ( dwResult != ERROR_SUCCESS )
        {
        //  Add error handling if necessary.
        }

        LocalFree( lpPropList );

    }
    else
    {
        dwResult = GetLastError();
    }

    return dwResult;

}
//
//  end GrpGetRWCDwProp()
//--------------------------------------------------------------------
#endif
```



 

 




