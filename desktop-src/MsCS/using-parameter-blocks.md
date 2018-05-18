---
title: Using Parameter Blocks
description: A parameter block provides data storage for a property table.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '61bbda33-da5f-4826-b52a-e45252ac0374'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["parameter blocks Failover Cluster ,using"]
---

# Using Parameter Blocks

A [parameter block](parameter-blocks.md) provides data storage for a [property table](property-tables.md). A parameter block is a user-defined structure that includes:

-   One member for each property. The structure may store properties as actual data values or as pointers to the data.
-   Additional members, as needed, for storing miscellaneous non-property information.

## Example

The following example shows two parameter blocks for a [Generic Application](generic-application.md) resource:


```C++
//
// Parameter block for a Generic Application resource.
// This example contains only property data (see below)
//
typedef struct CLUSDOCEX_GENAPP_PARAMS {

    LPWSTR CommandLine;         // CommandLine property

    LPWSTR CurrentDirectory;    // CurrentDirectory property

    DWORD  UseNetworkName;      // UseNetworkName property

    DWORD  InteractWithDesktop; // InteractWithDesktop property

} 
CLUSDOCEX_GENAPP_PARAMS, *PCLUSDOCEX_GENAPP_PARAMS;


//
// Another parameter block for a Generic Application resource.
// This example contains both property and non-property data.
//
typedef struct CLUSDOCEX_GENAPP_PARAMS2 
{
    LPWSTR ApplicationName;          // non-property data.

    LPWSTR CommandLineName;          // non-property data (stores the name of the property).
    LPWSTR CommandLineValue;         // property data.

    LPWSTR CurrentDirectoryName;     // non-property data.
    LPWSTR CurrentDirectoryValue;    // property data.
    
    LPWSTR UseNetworkNameName;       // non-property data.
    DWORD  UseNetworkNameValue;      // property data.
    
    LPWSTR InteractWithDesktopName;  // non-property data.
    DWORD  InteractWithDesktopValue; // property data.

}
CLUSDOCEX_GENAPP_PARAMS2, *PCLUSDOCEX_GENAPP_PARAMS2;
```



 

 




