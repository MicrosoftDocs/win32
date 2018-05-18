---
title: Parsing with CLUSPROP\_BUFFER\_HELPER
description: To read data from a value or property list with CLUSPROP\_BUFFER\_HELPER, use the following procedure.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '83239274-f3c1-463a-b91d-13db6da86846'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["property lists Failover Cluster ,parsing with CLUSPROP_BUFFER_HELPER", "value lists Failover Cluster ,parsing with CLUSPROP_BUFFER_HELPER"]
---

# Parsing with CLUSPROP\_BUFFER\_HELPER

To read data from a [value](value-lists.md) or [property list](property-lists.md) with [**CLUSPROP\_BUFFER\_HELPER**](clusprop-buffer-helper.md), use the following procedure.

**To read data from a value or property list**

1.  Obtain a buffer containing data.
2.  Set the **pb** member of [**CLUSPROP\_BUFFER\_HELPER**](clusprop-buffer-helper.md) to the start of the buffer.
3.  Use one of [**CLUSPROP\_BUFFER\_HELPER**](clusprop-buffer-helper.md)'s member pointers to read the **Syntax** member of the next data structure.
4.  If the **Syntax** matches what you are looking for, use other member pointers to get the data.
5.  Otherwise, use the [**Length**](cluspropertyvalue-length.md) member to get the byte size of the current entry.
6.  Verify that there is room in the buffer to advance [**CLUSPROP\_BUFFER\_HELPER**](clusprop-buffer-helper.md) to the next read position.
7.  Use the **pb** member to advance to the next read position.
8.  Repeat steps 3-6 until the item is found

When using this procedure, you must be familiar with the architecture of [value lists](value-lists.md) and [property lists](property-lists.md).

## Example

The following example presents a general-purpose parsing function for locating entries in a value or property list.


```C++
#include <windows.h>

//////////////////////////////////////////////////////////////////////

#include "ClusDocEx.h"

//////////////////////////////////////////////////////////////////////

#ifndef _CLUSDOCEX_FINDSYNTAX
#define _CLUSDOCEX_FINDSYNTAX
//--------------------------------------------------------------------
//
//  ClusDocEx_FindSyntax
//
//  Returns the position of the first entry that matches a specified
//  syntax in a property or value list, starting from a specified
//  position within the list.
//
//  Arguments:
//
//  lpList       Pointer to the value or property list buffer.
//  cbListSize   Size of the value or property list.
//  dwSyntax     The syntax to search for (see CLUSPROP_SYNTAX).
//  bPropList    The list is a property list.
//  
//  If successful, returns the byte position of the first match found,
//                 OR zero if no match was found.
//
//  If an error occurred, returns -1 (0xFFFFFFFF).
//
//--------------------------------------------------------------------        
DWORD
ClusDocEx_FindSyntax(
    IN LPVOID lpList,
    IN DWORD cbListSize,
    IN DWORD dwSyntax,
    IN BOOL bPropList
)
{
    DWORD cbPosition = 0;
    DWORD cbNextPos = 0;
    DWORD cbEntrySize = 0;

    CLUSPROP_BUFFER_HELPER cbh;

    if( ( lpList == NULL ) ||
        ( cbListSize == 0 ) )
    {
        cbPosition = -1;
        goto endf;
    }

    cbh.pb = (LPBYTE) lpList;


//  If this is a property list, advance past the count of properties.

    if( bPropList )
        cbh.pb += sizeof( DWORD );

    do 
    {

    //  Check the syntax of the current entry.

        if( cbh.pSyntax->dw == dwSyntax )
        {
        //  Specified syntax found.
            cbPosition = cbh.pb - (LPBYTE) lpList;
            break;
        }
        else if( cbh.pSyntax->dw != CLUSPROP_SYNTAX_ENDMARK )
        {
        //  Specified syntax not found and end of list not found.
        //  Get the size of the current entry.
            cbEntrySize = ClusDocEx_ListEntrySize( cbh.pValue->cbLength );
        }
        else if( bPropList )
        {
        //  Endmark found in a property list.
        //  Advance past the endmark.
            cbEntrySize = sizeof( CLUSPROP_SYNTAX );
        }
        else
        {
        //  Endmark found in a value list.
        //  Specified syntax was not found.
            cbPosition = 0;
            break;
        }


    //  Calculate the next position in the list.

        cbNextPos = cbh.pb - (LPBYTE) lpList + cbEntrySize;


    //  Verify remaining buffer size.
    //  The sizeof(CLUSPROP_SYNTAX) value accounts for the top-of-loop
    //  read operation (cbh.pSyntax->dw).

        if( cbNextPos + sizeof( CLUSPROP_SYNTAX ) > cbListSize )
        {
            cbPosition = 0;
            break;
        }
        else
        {
            cbh.pb += cbEntrySize;
        }

    } while( TRUE );

endf:

    return cbPosition;
}
//
//  End ClusDocEx_FindSyntax.
//--------------------------------------------------------------------
#endif
```



 

 




