---
title: Defining Structures and Constants
description: Some entry point functions require your resource DLL to describe and manage data in very specific ways. The following list describes the structures and constants that your DLL can or should define.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 20b150b4-293f-408b-888e-bac2b2fa4fb8
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- structures Failover Cluster ,defining
- constants Failover Cluster
- constants Failover Cluster ,defining
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Defining Structures and Constants

Some entry point functions require your [resource DLL](resource-dlls.md) to describe and manage data in very specific ways. The following list describes the structures and constants that your DLL can or should define.

1.  Required. Define a function table for each resource type supported by your resource DLL. See [**CLRES\_V1\_FUNCTIONS**](/windows/previous-versions/ResApi/ns-resapi-clres_v1_functions?branch=master).
2.  Required. Define global storage for the address of the [**LogEvent**](/windows/previous-versions/ResApi/nc-resapi-plog_event_routine?branch=master) callback function. You need only one **LogEvent** callback per resource DLL.
3.  Required. Define global storage for the address of the [**SetResourceStatus**](/windows/previous-versions/ResApi/nc-resapi-pset_resource_status_routine?branch=master) callback function. You only need one **SetResourceStatus** callback per resource DLL.
4.  Required. Define a structure, class, or other object to manage instance data. The recommended way to do this is to define a [resource structure](resource-structures.md). For more information see [Implementing Instance Management](implementing-instance-management.md).
5.  Required: Define the following objects if your resource type defines any private properties.

    -   Constants storing each property name.
    -   Constants describing minimum, maximum, and default values.
    -   A [parameter block](parameter-blocks.md).
    -   A [property table](property-tables.md).

Any additional objects are optional. For example:

-   Semaphores, mutexes, and critical sections necessary to synchronize instance counts and other shared data.
-   Structures or classes that simplify the process of working with [value lists](value-lists.md) and [property lists](property-lists.md).
-   Required [dependency](resource-dependencies.md) lists.
-   Constants, structures, classes, or other objects that specify the ideal configuration for the resource type. This would include property settings for the dependencies and dependents of the resource type and of the [group](groups.md) in which they reside.

## Example

The following example defines data in a resource DLL that supports two resource types, *MyTypeAlpha* and *MyTypeBeta*. For additional examples see [Resource DLL Examples](https://msdn.microsoft.com/library/aa370474).


```C++
//////////////////////////////////////////////////////////////////////

//  Callback function pointers for the DLL.

    PSET_RESOURCE_STATUS_ROUTINE g_pfnSetResourceStatus = NULL;

    PLOG_EVENT_ROUTINE           g_pfnLogEvent          = NULL;

//////////////////////////////////////////////////////////////////////

//  Resource type name constants

    #define TYPE_NAME_ALPHA L"MyTypeAlpha"

    #define TYPE_NAME_BETA  L"MyTypeBeta"

//////////////////////////////////////////////////////////////////////

//  Function tables.

    
    CLRES_V1_FUNCTION_TABLE(
        g_FTable_Alpha,    
        CLRES_VERSION_V1_00,     
        MyTypeAlpha,                 
        NULL,                      
        NULL,                       
        MyTypeAlphaResourceControl,  
        MyTypeAlphaResourceTypeControl
    );
    
    CLRES_V1_FUNCTION_TABLE(
        g_FTable_Beta,
        CLRES_VERSION_V1_00,
        MyTypeBeta,
        NULL,              
        NULL,                     
        MyTypeBetaResourceControl,
        MyTypeBetaResourceTypeControl
    );
    
//////////////////////////////////////////////////////////////////////

//  Resource structures.

    typedef struct _INSTANCE_ALPHA
    {
        RESID             resid;
        PARAM_BLOCK_ALPHA propsActive;
        PARAM_BLOCK_ALPHA props;
        HCLUSTER          hCluster;
        HRESOURCE         hResource;
        SC_HANDLE         hService;
        DWORD             dwServicePid;
        HKEY              hkeyParameters;
        RESOURCE_HANDLE   hResourceHandle;
        LPWSTR            pszResourceName;
        CLUS_WORKER       cwWorkerThread;
        CLUSTER_RESOURCE_STATE state;
    } 
    INSTANCE_ALPHA, * PINSTANCE_ALPHA;
    
    typedef struct _INSTANCE_BETA
    {
        RESID                   resid;
        HCLUSTER                hCluster;
        HRESOURCE               hResource;
        HKEY                    hkeyParameters;
        RESOURCE_HANDLE         hResourceHandle;
        LPWSTR                  pszResourceName;
        CLUS_WORKER             cwWorkerThread;
        CLUSTER_RESOURCE_STATE  state;
    } 
    INSTANCE_BETA, * PINSTANCE_BETA;

//////////////////////////////////////////////////////////////////////

//  Private property data.
//  Only MyTypeAlpha defines private properties.
    
    #define PROP_NAME__MAXUSERS L"MaxUsers"
    #define PROP_MIN__MAXUSERS        (-1)
    #define PROP_MAX__MAXUSERS        (256)
    #define PROP_DEFAULT__MAXUSERS    (8)
    
    typedef struct _PARAM_BLOCK_ALPHA
    {
        LONG nMaxUsers;
    } 
    PARAM_BLOCK_ALPHA, * PPARAM_BLOCK_ALPHA;
    

    RESUTIL_PROPERTY_ITEM PROP_TABLE_ALPHA[] =
    {
        {    
            PROP_NAME__MAXUSERS, 
            NULL, 
            CLUSPROP_FORMAT_LONG, 
            (DWORD) PROP_DEFAULT__MAXUSERS, 
            (DWORD) PROP_MIN__MAXUSERS, 
            (DWORD) PROP_MAX__MAXUSERS, 
            RESUTIL_PROPITEM_REQUIRED, 
            FIELD_OFFSET( PARAM_BLOCK_ALPHA, 
                          nMaxUsers ) 
        },

        { 0 }
    };
    
//////////////////////////////////////////////////////////////////////

//  Define a semaphore to limit MyTypeAlpha instances to
//  one per cluster.  SIS = "single instance semaphore"

    #define SIS_ALPHA L"SISAlpha"
    static HANDLE g_hSIS = NULL;
    static PINSTANCE_ALPHA g_pInstance_Alpha = NULL;
    
//////////////////////////////////////////////////////////////////////
```



 

 




