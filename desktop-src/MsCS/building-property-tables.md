---
title: Building Property Tables
description: How to build a property table using the Failover Cluster API.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 0b1306d1-b1b4-49c3-8163-73078f5bf9cf
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- property tables Failover Cluster ,building
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Building Property Tables

The following procedure describes how to build a [property table](property-tables.md).

**To build a property table for an object**

1.  Construct a [parameter block](parameter-blocks.md) (see [Using Parameter Blocks](using-parameter-blocks.md)).
2.  Construct an array of [**RESUTIL\_PROPERTY\_ITEM**](/previous-versions/windows/desktop/api/ResApi/ns-resapi-resutil_property_item) structures (one structure for each object property). Each **RESUTIL\_PROPERTY\_ITEM** structure includes:

    -   Property name.
    -   Name of the [cluster database](cluster-database.md) subkey storing the property.
    -   Property format.
    -   Property default, minimum, and maximum values.
    -   Flags to define the property as [read-only](read-only-properties.md) and/or required.
    -   An offset to the appropriate property member of the parameter block.

3.  As the final array element, add a [**RESUTIL\_PROPERTY\_ITEM**](/previous-versions/windows/desktop/api/ResApi/ns-resapi-resutil_property_item) structure with a **NULL** property name.

The entire array of [**RESUTIL\_PROPERTY\_ITEM**](/previous-versions/windows/desktop/api/ResApi/ns-resapi-resutil_property_item) structures is what is referred to as a property table.

## Example

In the following example, a [resource DLL](resource-dlls.md) defines a parameter block and a property table as global data which are used as the basis for property operations. For more information on initializing data in a resource DLL, see [Defining Structures and Constants](defining-structures-and-constants.md).


```C++
#include <windows.h>
#include <clusapi.h>
#include <resapi.h>

//  Private property names
#define PROP_NAME__STRINGPROP  L"StringProp"
#define PROP_NAME__DWORDPROP   L"DwordProp"
#define PROP_NAME__BINARYPROP  L"BinaryProp"
#define PROP_NAME__BOOLPROP    L"BoolProp"
#define PROP_NAME__MULTISZPROP L"MultiSzProp"
#define PROP_NAME__LONGPROP    L"LongProp"

//  Min, max, default values
#define PROP_MIN__DWORDPROP     (1)
#define PROP_MAX__DWORDPROP     (256)
#define PROP_DEFAULT__DWORDPROP (32)
#define PROP_MIN__BOOLPROP      (0)
#define PROP_MAX__BOOLPROP      (1)
#define PROP_DEFAULT__BOOLPROP  (0)
#define PROP_MIN__LONGPROP      (-1)
#define PROP_MAX__LONGPROP      (15)
#define PROP_DEFAULT__LONGPROP  (-1)


//////////////////////////////////////////////////////////////////////

//  Excerpt from the sample SmbSmp.c.

//  Parameter block for the private properties.
typedef struct CLUSDOCEX_PROPS
{
    PWSTR  pszStringProp;
    DWORD  nDwordProp;
    LPBYTE pbBinaryProp;
    DWORD  nBinaryPropSize;
    BOOL   bBoolProp;
    PWSTR  pszMultiSzProp;
    DWORD  nMultiSzPropSize;
    LONG   nLongProp;
}
CLUSDOCEX_PROPS, * PCLUSDOCEX_PROPS;


//  Property table.
RESUTIL_PROPERTY_ITEM
ClusDocExResourcePrivateProperties[] =
{
    {
        PROP_NAME__STRINGPROP, /* property name             */
        NULL,                  /* subkey                    */
        CLUSPROP_FORMAT_SZ,    /* format                    */
        0, 0, 0,               /* default, min, max value   */
        0,                     /* flags                     */
        FIELD_OFFSET(          /* offset to parameter block */
            CLUSDOCEX_PROPS, 
            pszStringProp )

    },
    { 
        PROP_NAME__DWORDPROP, 
        NULL, 
        CLUSPROP_FORMAT_DWORD, 
        PROP_DEFAULT__DWORDPROP, 
        PROP_MIN__DWORDPROP, 
        PROP_MAX__DWORDPROP, 
        0, 
        FIELD_OFFSET( 
            CLUSDOCEX_PROPS, 
            nDwordProp ) 
    },
    { 
        PROP_NAME__BINARYPROP, 
        NULL, 
        CLUSPROP_FORMAT_BINARY, 
        0, 0, 0, 
        0, 
        FIELD_OFFSET( 
            CLUSDOCEX_PROPS, 
           pbBinaryProp ) 
    },
    { 
        PROP_NAME__BOOLPROP, 
        NULL, 
        CLUSPROP_FORMAT_DWORD, 
        PROP_DEFAULT__BOOLPROP, 
        PROP_MIN__BOOLPROP, 
        PROP_MAX__BOOLPROP, 
        RESUTIL_PROPITEM_SIGNED, 
        FIELD_OFFSET( 
            CLUSDOCEX_PROPS, 
            bBoolProp ) 
    },
    { 
        PROP_NAME__MULTISZPROP, 
        NULL, 
        CLUSPROP_FORMAT_MULTI_SZ, 
        0, 0, 0, 
        0, 
        FIELD_OFFSET( 
            CLUSDOCEX_PROPS, 
            pszMultiSzProp ) 
    },
    { 
        PROP_NAME__LONGPROP, 
        NULL, 
        CLUSPROP_FORMAT_LONG, 
        (DWORD) PROP_DEFAULT__LONGPROP, 
        (DWORD) PROP_MIN__LONGPROP, 
        (DWORD) PROP_MAX__LONGPROP, 
        0, 
        FIELD_OFFSET( 
            CLUSDOCEX_PROPS, 
            nLongProp ) 
    },
    { 0 }
};
```



 

 




