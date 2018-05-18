---
title: Setting Properties
description: Setting properties is the process of writing new property values to the cluster database. Applications and resource DLLs set properties to change the cluster environment according to their needs.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'b67edcf0-4cdb-4aa1-9681-5cacd4254392'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["properties Failover Cluster ,setting"]
---

# Setting Properties

Setting properties is the process of writing new property values to the [cluster database](cluster-database.md). Applications and [resource DLLs](resource-dlls.md) set properties to change the [*cluster*](c-gly.md#-wolf-cluster-gly) environment according to their needs.

The [Failover Cluster API](the-server-cluster-api.md) provides many ways to set the properties of a [cluster object](cluster-objects.md). The [standard order of preference](standard-order-of-preference.md) for [*cluster-aware applications*](c-gly.md#-wolf-cluster-aware-application-gly) recommends using [control codes](about-control-codes.md) if possible. Therefore, the procedures described below use control codes exclusively. If you are writing a resource DLL, you should use the [cluster database access functions](cluster-database-access-functions.md) and the [cluster utility functions](cluster-utility-functions.md) to work with properties.

The following generalized procedure describes how to set the properties for any object. Substitute the name of the object (that is, [node](nodes.md), [network](networks.md), [network interface](network-interfaces.md), [group](groups.md), [resource](resources.md), or [resource type](resource-types.md) ) for &lt;Object&gt;.

**To set &lt;Object&gt; properties**

1.  Create a [property list](property-lists.md) for the object. (See [Creating Property Lists](creating-property-lists.md).)
2.  Validate the property list to ensure that the formatting is correct and the values are appropriate. Call the [control code function](control-code-functions.md) for the object, **Cluster&lt;Object&gt;Control**, specifying one of the following [control codes](control-codes.md) as the *dwControlCode* parameter.

    

    | Properties to set                            | Control code to use                                    |
    |----------------------------------------------|--------------------------------------------------------|
    | [Common properties](common-properties.md)   | CLUSCTL\_&lt;OBJECT&gt;\_VALIDATE\_COMMON\_PROPERTIES  |
    | [Private properties](private-properties.md) | CLUSCTL\_&lt;OBJECT&gt;\_VALIDATE\_PRIVATE\_PROPERTIES |

    

     

3.  If validation succeeds, set the properties by calling **Cluster&lt;Object&gt;Control** using one of the following control codes as the *dwControlCode* parameter.

    

    | Properties to set  | Control code to use                               |
    |--------------------|---------------------------------------------------|
    | Common properties  | CLUSCTL\_&lt;OBJECT&gt;\_SET\_COMMON\_PROPERTIES  |
    | Private properties | CLUSCTL\_&lt;OBJECT&gt;\_SET\_PRIVATE\_PROPERTIES |

    

     

4.  If **Cluster&lt;Object&gt;Control** returns **ERROR\_SUCCESS**, the properties have been written to the cluster database.
5.  If **Cluster&lt;Object&gt;Control** returns **ERROR\_RESOURCE\_PROPERTIES\_STORED**, the properties have been written to the cluster database, but some or all of the new settings do not take effect until the next time the resource is brought online.

## Example Code

The following example function sets [group](groups.md) properties. It obtains a property list by calling the *ClusDocEx\_GrpCreatePropList* example function from [Creating Property Lists](creating-property-lists.md).


```C++
#include <windows.h>

///////////////////////////////////////////////////////////////////////////////////

#include "ClusDocEx.h"

///////////////////////////////////////////////////////////////////////////////////

#ifndef _CLUSDOCEX_GRPRESETPROPERTYDEFAULTS_CPP
#define _CLUSDOCEX_GRPRESETPROPERTYDEFAULTS_CPP
//---------------------------------------------------------------------------------
//
//  ClusDocEx_GrpResetPropertyDefaults
//
//  Sets all read/write common group properties to their default
//  values.
//
//  Arguments:
//       hGroup     Handle to group whose properties are to be set.
//
//  Return Value:               
//       Error code
//
//---------------------------------------------------------------------------------
DWORD ClusDocEx_GrpResetPropertyDefaults( IN HGROUP hGroup )
{
  DWORD dwResult = ERROR_SUCCESS;
  DWORD cbSize   = 0;

//  Obtain a property list with all values set to defaults.
//  For the ClusDocEx_GrpCreatePropertyList function see
//  "Creating Property Lists".

  LPVOID lpPropList = ClusDocEx_GrpCreatePropertyList( &amp;cbSize,
                                                       ClusterGroupPreventFailback,
                                                       L" ",
                                                       -1, 
                                                       -1,
                                                       6,
                                                       10,
                                                       FALSE );


//  Validate the property list.

   dwResult = ClusterGroupControl( hGroup, 
                                   NULL,
                                   CLUSCTL_GROUP_VALIDATE_COMMON_PROPERTIES,
                                   lpPropList, 
                                   cbSize, 
                                   NULL, 
                                   0, 
                                   NULL );

  if ( dwResult == ERROR_SUCCESS )
   {

    //  Set the properties.

    dwResult = ClusterGroupControl( hGroup, 
                                    NULL,
                                    CLUSCTL_GROUP_SET_COMMON_PROPERTIES,
                                    lpPropList, 
                                    cbSize, 
                                    NULL, 
                                    0, 
                                    NULL );
   }

  if ( dwResult != ERROR_SUCCESS )
   {
    ClusDocEx_DebugPrint( L"ClusDocEx_GrpResetPropertyDefaults", 
                          dwResult );
   }

//  Free the buffer returned by ClusDocEx_GrpCreatePropList

  LocalFree( lpPropList );

  return dwResult;

 }
//  end ClusDocEx_GrpResetPropertyDefaults
//----------------------------------------------------------------------------------
#endif
```



 

 




