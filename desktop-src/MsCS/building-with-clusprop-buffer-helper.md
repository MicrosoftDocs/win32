---
title: Building with CLUSPROP\_BUFFER\_HELPER
description: To create a value or property list with CLUSPROP\_BUFFER\_HELPER, or to create any other kind of structure in a buffer, use the following procedure.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '9efe1457-72ab-4e9a-9d92-128e206b0fb3'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["property lists Failover Cluster ,building with CLUSPROP_BUFFER_HELPER", "value lists Failover Cluster ,building with CLUSPROP_BUFFER_HELPER"]
---

# Building with CLUSPROP\_BUFFER\_HELPER

To create a [value](value-lists.md) or [property list](property-lists.md) with [**CLUSPROP\_BUFFER\_HELPER**](clusprop-buffer-helper.md), or to create any other kind of structure in a buffer, use the following procedure.

**To create a value or property list**

1.  Allocate a buffer of sufficient size to hold the data.
2.  Set the **pb** member of to the start of the buffer.
3.  Use one of 's member pointers to write one or more values from the present position. You must know the byte size of this value.
4.  Optional. Verify that there is room in the buffer to advance to the next write position.
5.  Use the **pb** member to advance to the next write position.
6.  Repeat steps 3-5 until the buffer is full or all the data is written

When using this procedure, you must be familiar with the architecture of [value lists](value-lists.md) and [property lists](property-lists.md).

## Example

The following examples use [**CLUSPROP\_BUFFER\_HELPER**](clusprop-buffer-helper.md) to generate a value list entry. A value list would consist of "stacks" of these entries terminated by **CLUSPROP\_SYNTAX\_ENDMARK**. A property list would consist of "stacks" of value lists (one value list per property) prefixed by the count of properties in the list.

In the first example (ClusDocEx\_BasicPropertyValueList) the numbers in parentheses correspond to the steps in the procedure presented above. The second example (ClusDocEx\_CreateValueListEntry) is used by several other example functions.


```C++
#include <windows.h>
#include "ClusDocEx.h"

//////////////////////////////////////////////////////////////////////

#ifndef _CLUSDOCEX_BASICPROPERTYVALUELIST_CPP
#define _CLUSDOCEX_BASICPROPERTYVALUELIST_CPP
//--------------------------------------------------------------------
//
//  ClusDocEx_BasicPropertyValueList
//
//  A tutorial example that describes the process of using
//  CLUSPROP_BUFFER_HELPER to create property and value lists.
//
//  This example creates a single-property list that consists
//  of the following:
//
//  Property List:
//  ---------  ------------------------   ---
//  count      DWORD                       N ( = 1 )
//  ---------  -------------------------  ---
//  Syntax  \                              .
//  Length  -> CLUSPROP_PROPERTY_NAME      .     A single property
//  Name    /                              .     typically consists
//  -------                                .     of a value list that
//  Syntax  \                            Value   describes the
//  Length  -> CLUSPROP_PROPERTY_VALUE    List   name and value of
//  Value   /                              .     the property
//  ---------                              .
//  Endmark -> CLUSPROP_ENDMARK            .
//  ------- -  -------------------------  ---
//
//  A longer property list would continue with 1 additional value
//  list per property.
//
//--------------------------------------------------------------------
void ClusDocEx_BasicPropertyValueList()
{

//  Name and intended value of the Role common property for Networks.

    LPCWSTR lpszRoleName = L"Role";
    DWORD   dwRoleValue  = ClusterNetworkRoleInternalUse;

    LPVOID lpList;
    CLUSPROP_BUFFER_HELPER cbh;

    DWORD cbSzSize;
    DWORD cbNameEntrySize;
    DWORD cbDwordEntrySize;
    DWORD cbListSize;



//  Calculate byte size of the Name.  MUST include terminating NULL.

    cbSzSize = ( lstrlenW( lpszRoleName ) + 1 ) * sizeof( WCHAR );


//  Byte size of the value list entry for the name.

    cbNameEntrySize = sizeof( DWORD ) +           // Syntax member
                      sizeof( DWORD ) +           // Length member
                      ALIGN_CLUSPROP( cbSzSize ); // Data + padding for correct alignment


//  Byte size of the value list entry for the DWORD data.

    cbDwordEntrySize = sizeof( DWORD ) + // Syntax member
                       sizeof( DWORD ) + // Length member
                       sizeof( DWORD );  // Data (already aligned)



//  ClusDocEx_ListEntrySize automates the above calculations
//  -----------------------included in ClusDocEx.h)



//  Byte size required for the entire property list.

    cbListSize =  sizeof( DWORD )  + // prop count
                  cbNameEntrySize  + // name
                  cbDwordEntrySize + // value
                  sizeof( DWORD );   // endmark



//  Allocate property list buffer.

    lpList = LocalAlloc( LPTR,          // zeros the memory
                         cbListSize );

    if( lpList == NULL )
    {
    //  Handle the error
    }


//  Position cbh.

    cbh.pb = (PBYTE) lpList;



//  Write the property count using cbh's CLUSPROP_LIST pointer.

    cbh.pList->nPropertyCount = 1;


//  Position cbh.

    cbh.pb += sizeof( DWORD );


//  Write the property name

    cbh.pName->Syntax.dw = CLUSPROP_SYNTAX_NAME;

    cbh.pName->cbLength = cbSzSize;

    StringCbCopy(  cbh.pName->sz, cbSzSize, lpszRoleName );

## /*
----------------------------------------------------------------------
Note that the following alternatives would have the same result:

(1)     *cbh.pdw = 1 ;                                   // property count
        cbh.pb += sizeof( DWORD );                       // Advance pb
        *cbh.pdw = CLUSPROP_PROPERTY_NAME ;              // Set the Syntax
        cbh.pb += sizeof( DWORD );                       // Advance pb
        *cbh.pdw = cbSzSize;                             // Set the Length
        cbh.pb += sizeof( DWORD );                       // Advance pb
        StringCbCopy( cbh.psz, cbSzSize, lpszRoleName ); // Set the Data

(2)     *cbh.pdw = 1 ;
        cbh.pb += sizeof( DWORD );
        cbh.pValue->Syntax.dw = CLUSPROP_PROPERTY_NAME;
        cbh.pValue->cbLength = sizeof( DWORD );
        cbh.pb += sizeof( CLUSPROP_VALUE );
        CLUSPROP_BUFFER_HELPER cbhRead;
        cbhRead.pb = (PBYTE) lpszRoleName;
        for( int i = 0 ; i < cbSzSize ; i++ )
##             cbh.pb[i] = cbhRead.pb[i];
----------------------------------------------------------------------
*/


//  Advance cbh

    cbh.pb += cbNameEntrySize;


//  Add the property value.

    cbh.pDwordValue->Syntax.dw = CLUSPROP_SYNTAX_LIST_VALUE_DWORD;

    cbh.pDwordValue->cbLength = sizeof( DWORD );

    cbh.pDwordValue->dw = dwRoleValue;


//  Advance CBH.pb

    cbh.pb += cbDwordEntrySize;


//  End the value list for this property.

    cbh.pSyntax->dw = CLUSPROP_SYNTAX_ENDMARK;

    cbh.pb = NULL;


//  Use the list. For example, to set the new property
//  in the cluster database:
//
//    (open a network handle)
//
//    dwResult = ClusterNetworkControl( hNetwork,
//                                      NULL,
//                                      CLUSCTL_NODE_SET_COMMON_PROPERTIES
//                                      lpList,
//                                      cbListSize,
//                                      NULL,
//                                      0,
//                                      NULL );

    if( lpList != NULL )
    {

    //  Display lpList as raw bytes

        ClusDocEx_ShowBuffer( lpList, cbListSize );   //  see "ClusDocEx.h"

        LocalFree( lpList );
    }
}
//
//  end ClusDocEx_BasicPropertyValueList
//--------------------------------------------------------------------
#endif


//////////////////////////////////////////////////////////////////////


#ifndef _CLUSDOCEX_CREATEVALUELISTENTRY_CPP
#define _CLUSDOCEX_CREATEVALUELISTENTRY_CPP
//--------------------------------------------------------------------
//
//  ClusDocEx_CreateValueListEntry
//
//  Returns a buffer containing a properly formatted entry for
//  a value list.
//
//  Callers must call LocalFree on the returned pointer.
//
//  Arguments:
//      IN DWORD dwSyntax          Data syntax (see CLUSPROP_SYNTAX).
//      IN DWORD cbLength          Data length (see CLUSPROP_VALUE).
//      IN LPVOID lpData           Pointer to the data.
//      OUT LPDWORD lpcbEntrySize  Byte size of the resulting entry.
//
//  Return Value:
//      Pointer to a buffer containing a value list entry.
//
//--------------------------------------------------------------------
LPVOID ClusDocEx_CreateValueListEntry(
    IN DWORD dwSyntax,
    IN DWORD cbLength,
    IN LPVOID lpData,
    OUT LPDWORD lpcbEntrySize
)
{
    CLUSPROP_BUFFER_HELPER cbh;
    LPVOID lpEntry = NULL;


//  TODO:  Code that checks for bad parameters.


//  Calculate the size of the entry and allocate space.

    *lpcbEntrySize = ClusDocEx_ListEntrySize( cbLength );


//  lpcbEntrySize now describes the size of the entire value list
//  entry, including the alignment padding.

    lpEntry = LocalAlloc( LPTR, *lpcbEntrySize );


    if( lpEntry != NULL )
    {

    //  Position cbh.

        cbh.pb = (LPBYTE) lpEntry;


    //  Write syntax and length.

        cbh.pValue->Syntax.dw = dwSyntax;

        cbh.pValue->cbLength = cbLength;


    //  Position cbh.

        cbh.pb += sizeof( CLUSPROP_VALUE );


    //  Bytewise copy the data (should use memcpy).

        memcpy( cbh.pb, lpEntry, cbLength );


    //  The initial allocation allowed for alignment padding.

    }


    cbh.pb = NULL;

    return lpEntry;

}
//  end ClusDocEx_CreateValueListEntry
//--------------------------------------------------------------------
#endif


//--------------------------------------------------------------------
//  TODO
//
//  ClusDocEx_CreateValueListEntry creates single entries.
//  A class or series of functions could be created to dynamically
//  allocate and "stack" entries.  Remember that the data
//  has to be contiguous, so a linked list solution would have
//  to be able to combine its nodes into a single buffer.
//
//  For an example of a dynamic property list,
//  refer to the CClusPropList class.
//--------------------------------------------------------------------
```



 

 




