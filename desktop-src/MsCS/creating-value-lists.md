---
title: Creating Value Lists
description: This section assumes you are familiar with the architecture described in Value Lists.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 7af7f5a8-fe1f-4b2a-9332-fd2cefc18cc2
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- value lists Failover Cluster ,creating
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Creating Value Lists

This section assumes you are familiar with the architecture described in [Value Lists](value-lists.md). Creating a value list means creating a sequence of bytes that conforms to the architectural conventions for value lists. As long as the result is correct, any technique that properly sequences and aligns the data is fine.

For example, the easiest way to create a value list is to create a structure:

``` syntax
typedef struct DWORD_VALUE_LIST
 {
  CLUSPROP_DWORD First;
  CLUSPROP_DWORD Second;
  CLUSPROP_DWORD Third;
  CLUSPROP_SYNTAX Endmark;
 } DWORD_VALUE_LIST;
```

However, this method gets complicated when variable-length data is introduced.

Another way to create a value list is to use [**CLUSPROP\_BUFFER\_HELPER**](/previous-versions/windows/desktop/api/ClusAPI/ns-clusapi-clusprop_buffer_helper). (See [Building with CLUSPROP\_BUFFER\_HELPER](building-with-clusprop-buffer-helper.md).)

## Example

The following example creates a required [dependencies](resource-dependencies.md) list for a resource using structures to define the value list. A [resource DLL](resource-dlls.md) might build a value list like this in response to the [CLUSCTL\_RESOURCE\_GET\_REQUIRED\_DEPENDENCIES](clusctl-resource-get-required-dependencies.md) control code.


```C++
#include <windows.h>

//////////////////////////////////////////////////////////////////////

#include "ClusDocEx.h"

//////////////////////////////////////////////////////////////////////

#ifndef _CLUSDOCEX_CREATEREQUIREDDEPENDENCIESLIST_CPP
#define _CLUSDOCEX_CREATEREQUIREDDEPENDENCIESLIST_CPP


//  Global buffer that will store the required dependencies value list.

    LPVOID g_CLUSDOCEX_REQDEPS = NULL;

    #define RESOURCE_TYPE_NETWORK_NAME L"Network Name"

//--------------------------------------------------------------------
// 
//  ClusDocEx_CreateRequiredDependenciesList
//
//  Creates a value list specifying the required dependencies
//  of a resource. For this example, the dependencies are a Network
//  Name resource and a storage class resource.
//
//--------------------------------------------------------------------
void ClusDocEx_CreateRequiredDependenciesList()
{

//  Define a structure for the value list.
//  Note the use of the CLUSPROP_SZ_DECLARE macro.

    struct DEP_DATA
    {
        CLUSPROP_RESOURCE_CLASS rcStorage;
        CLUSPROP_SZ_DECLARE(    netnameEntry, 
                                sizeof( RESOURCE_TYPE_NETWORK_NAME ) /
                                  sizeof( WCHAR ) );
        CLUSPROP_SYNTAX         endmark;
    };
    DEP_DATA* pdepdata;

    pdepdata = (DEP_DATA*) LocalAlloc( LPTR, sizeof( DEP_DATA ) );

    if( pdepdata != NULL )
    {

    //  Add the Storage class entry.
        pdepdata->rcStorage.Syntax.dw = CLUSPROP_SYNTAX_RESCLASS;
        pdepdata->rcStorage.cbLength = sizeof( pdepdata->rcStorage.rc );
        pdepdata->rcStorage.rc = CLUS_RESCLASS_STORAGE;

    //  Add the Network Name entry.
        pdepdata->netnameEntry.Syntax.dw = CLUSPROP_SYNTAX_NAME;
        pdepdata->netnameEntry.cbLength = sizeof( RESOURCE_TYPE_NETWORK_NAME );
        StringCchCopyW( pdepdata->netnameEntry.sz, 
                        pdepdata->netnameEntry.cbLength, 
                        RESOURCE_TYPE_NETWORK_NAME );

    //  Add the endmark.
        pdepdata->endmark.dw = CLUSPROP_SYNTAX_ENDMARK;
    }

    g_CLUSDOCEX_REQDEPS = (LPVOID) pdepdata;
}
//  End ClusDocEx_CreateRequiredDependenciesList.
//--------------------------------------------------------------------
#endif
```



 

 




