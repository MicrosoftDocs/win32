---
title: Creating Property Lists
description: How to create a property list using the Failover Cluster API.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '15d08ce0-070a-47cd-bf0c-71fdc98d6d7f'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["property lists Failover Cluster ,creating"]
---

# Creating Property Lists

There are two recommended ways of creating a [property list](property-lists.md):

-   [*Cluster-aware applications*](c-gly.md#-wolf-cluster-aware-application-gly) should use [**CLUSPROP\_BUFFER\_HELPER**](clusprop-buffer-helper.md) to build the property list as a series of value lists. For procedures and examples, see [Building with CLUSPROP\_BUFFER\_HELPER](building-with-clusprop-buffer-helper.md).
-   [Resource DLLs](resource-dlls.md) should store local copies of property data in [parameter blocks](parameter-blocks.md) and [property tables](property-tables.md), and use the property structure construction functions to generate [property lists](property-lists.md). For procedures and examples, see [Using Parameter Blocks](using-parameter-blocks.md) and [Using Lists and Tables](using-lists-and-tables.md).

This distinction is based on the fact that many property table operations require direct access to the [cluster database](cluster-database.md). Resource DLLs are expected to have such access. However, cluster-aware applications should avoid direct cluster database manipulation. See the [standard order of preference](standard-order-of-preference.md).

As a third option, the FileShareSample sample resource type (located in the Samples\\WinBase\\Cluster directory of the Windows SDK) includes the complete implementation of **CClusPropList**, a sample property list management class.

## Example

The following example contains the functions **ClusDocEx\_CreatePropertyListEntry** and **ClusDocEx\_GrpCreatePropertyList**. The first function returns a buffer containing a single property list entry. The second function uses the first function to create multiple entries and "stacks" them into a property list.


```C++
#include <windows.h>

//////////////////////////////////////////////////////////////////////

#include "ClusDocEx.h"

//////////////////////////////////////////////////////////////////////

#ifndef _CLUSDOCEX_CREATEPROPERTYLISTENTRY_CPP
#define _CLUSDOCEX_CREATEPROPERTYLISTENTRY_CPP
//--------------------------------------------------------------------
//
//  ClusDocEx_CreatePropertyListEntry.
//      
//  Returns a buffer containing an entry for a property list,
//  formatted as a value list containing the following entries:
//      Property Name  (syntax, length, data, padding)
//      Property Value (syntax, length, data, padding)
//      CLUSPROP_SYNTAX_ENDMARK
//  
//  Callers must call LocalFree on the returned pointer.
//  
//  Arguments:
//      IN LPWSTR lpszPropName     Name of the property.
//      IN DWORD dwSyntax          Data syntax (see CLUSPROP_SYNTAX).
//      IN DWORD cbLength          Data length (see CLUSPROP_VALUE).
//      IN LPVOID lpData           Pointer to the data.
//      OUT LPDWORD lpcbEntrySize  Byte size of the resulting entry.  
//  
//  Return Value: 
//      Pointer to a buffer containing a property list entry.
// 
//-------------------------------------------------------------------- 
LPVOID ClusDocEx_CreatePropertyListEntry( IN LPWSTR lpszPropName,
                                   IN DWORD dwSyntax,
                                   IN DWORD cbLength,
                                   IN LPVOID lpData,
                                   OUT LPDWORD lpcbEntrySize)
{
  DWORD cbPropNameSize = ( lstrlenW( lpszPropName ) + 1 ) * 
                           sizeof( WCHAR );
  DWORD cbNameEntrySize;
  DWORD cbValueEntrySize;

  CLUSPROP_BUFFER_HELPER cbh;
  LPVOID lpEntry = NULL;


  //  TODO:  Code that checks for bad parameters.

  //  Calculate sizes.
  //  ClusDocEx_ListEntrySize is defined in ClusDocEx.h.

  cbNameEntrySize = ClusDocEx_ListEntrySize( cbPropNameSize );

  cbValueEntrySize = ClusDocEx_ListEntrySize( cbLength );

  *lpcbEntrySize = cbNameEntrySize +
                   cbValueEntrySize +
                   sizeof( DWORD );

  lpEntry = LocalAlloc( LPTR, *lpcbEntrySize );

  if( lpEntry != NULL )
   {

    //  Position cbh.

    cbh.pb = (LPBYTE) lpEntry;

    //  Write the property name.

    cbh.pName->Syntax.dw = CLUSPROP_SYNTAX_NAME;

    cbh.pName->cbLength = cbPropNameSize;

    StringCchCopyW( cbh.pName->sz, cbPropNameSize, lpszPropName );

    //  Advance cbh. 

    cbh.pb += cbNameEntrySize;

    //  Write syntax and length

    cbh.pValue->Syntax.dw = dwSyntax;

    cbh.pValue->cbLength = cbLength;

    //  Position cbh.

    cbh.pb += sizeof( CLUSPROP_VALUE );

    //  Copy the data.

    memcpy( cbh.pb, lpData, cbLength );

    //  Position cbh. 

    cbh.pb = (PBYTE) lpEntry + cbNameEntrySize + cbValueEntrySize;

    //  Set the endmark.

    *cbh.pdw = CLUSPROP_SYNTAX_ENDMARK;
   }

  cbh.pb = NULL;

  return lpEntry;
 }
//  end ClusDocEx_CreatePropertyListEntry
//--------------------------------------------------------------------
#endif


//////////////////////////////////////////////////////////////////////


#ifndef _CLUSDOCEX_GRPCREATEPROPERTYLIST_CPP
#define _CLUSDOCEX_GRPCREATEPROPERTYLIST_CPP
//--------------------------------------------------------------------
//
//  ClusDocEx_GrpCreatePropertyList(
//      
//  Returns a property list containing all of the read/write common
//  properties for a group.
//  
//  Callers must call LocalFree on the returned pointer.
//  
//  Arguments:
//      LPDWORD lpcbPropListSize    Byte size of the resulting 
//                                  property list.  
//      Use the remaining arguments to assign new values to the 
//      read/write group common properties.
//  
//  Return Value: 
//      Pointer to a buffer containing a property list.
//-------------------------------------------------------------------- 
LPVOID
ClusDocEx_GrpCreatePropertyList( LPDWORD lpcbPropListSize,
                                 DWORD   dwAutoFailbackType,
                                 LPWSTR  lpszDescription,
                                 DWORD   dwFailbackWindowEnd,
                                 DWORD   dwFailbackWindowStart,
                                 DWORD   dwFailoverPeriod,
                                 DWORD   dwFailoverThreshold,
                                 DWORD   dwPersistentState )
 {
  LPVOID lpPropList;
  LPVOID lpAutoFailbackType;    
  LPVOID lpDescription;         
  LPVOID lpFailbackWindowEnd;   
  LPVOID lpFailbackWindowStart; 
  LPVOID lpFailoverPeriod;      
  LPVOID lpFailoverThreshold;   
  LPVOID lpPersistentState;     

  DWORD dwPropCount = 7;
  DWORD cbPropEntrySize[7];
  DWORD cbPosition = 0;
  DWORD cb, dw;

  CLUSPROP_BUFFER_HELPER cbh_write, cbh_read;

  //  Create the property list entries for each property.

  lpAutoFailbackType    = ClusDocEx_CreatePropertyListEntry(
                                    L"AutoFailbackType",
                                    CLUSPROP_SYNTAX_LIST_VALUE_DWORD,
                                    sizeof( DWORD ),
                                    (LPVOID) &amp;dwAutoFailbackType,
                                    &amp;cbPropEntrySize[0] );

  lpDescription         = ClusDocEx_CreatePropertyListEntry(
                                    L"Description",
                                    CLUSPROP_SYNTAX_LIST_VALUE_SZ,
                                    (lstrlenW(lpszDescription) + 1)*sizeof(WCHAR),
                                    (LPVOID) lpszDescription,
                                    &amp;cbPropEntrySize[1] );

  lpFailbackWindowEnd   = ClusDocEx_CreatePropertyListEntry(
                                    L"FailbackWindowEnd",
                                    CLUSPROP_SYNTAX_LIST_VALUE_DWORD,
                                    sizeof( DWORD ),
                                    (LPVOID) &amp;dwFailbackWindowEnd,
                                    &amp;cbPropEntrySize[2] );

  lpFailbackWindowStart = ClusDocEx_CreatePropertyListEntry(
                                    L"FailbackWindowStart",
                                    CLUSPROP_SYNTAX_LIST_VALUE_DWORD,
                                    sizeof( DWORD ),
                                    (LPVOID) &amp;dwFailbackWindowStart,
                                    &amp;cbPropEntrySize[3] );

  lpFailoverPeriod      = ClusDocEx_CreatePropertyListEntry(
                                    L"FailoverPeriod",
                                    CLUSPROP_SYNTAX_LIST_VALUE_DWORD,
                                    sizeof( DWORD ),
                                    (LPVOID) &amp;dwFailoverPeriod,
                                    &amp;cbPropEntrySize[4] );

  lpFailoverThreshold   = ClusDocEx_CreatePropertyListEntry(
                                    L"FailoverThreshold",
                                    CLUSPROP_SYNTAX_LIST_VALUE_DWORD,
                                    sizeof( DWORD ),
                                    (LPVOID) &amp;dwFailoverThreshold,
                                    &amp;cbPropEntrySize[5] );

  lpPersistentState     = ClusDocEx_CreatePropertyListEntry(
                                    L"PersistentState",
                                    CLUSPROP_SYNTAX_LIST_VALUE_DWORD,
                                    sizeof( DWORD ),
                                    (LPVOID) &amp;dwPersistentState,
                                    &amp;cbPropEntrySize[6] );

  // Calculate the required size, which should be the sum of each entry
  // plus the size of the property count.

  *lpcbPropListSize = sizeof( DWORD );  // property count.

  for( cb = 0 ; cb < dwPropCount ; cb++ )
    *lpcbPropListSize += cbPropEntrySize[cb];

  lpPropList = LocalAlloc( LPTR, *lpcbPropListSize );

  //  Position cbh and write the property count.

  cbh_write.pb = (PBYTE) lpPropList;

  *cbh_write.pdw = dwPropCount;

  cbPosition = sizeof( DWORD );

  // Iterate through the property list entries and copy each entry
  // to the property list buffer.

  for( dw = 0 ; dw < dwPropCount ; dw++ )
   {
    switch( dw )
     {
      case 0:  cbh_read.pb = (PBYTE) lpAutoFailbackType;    break;
      case 1:  cbh_read.pb = (PBYTE) lpDescription;         break;
      case 2:  cbh_read.pb = (PBYTE) lpFailbackWindowEnd;   break;
      case 3:  cbh_read.pb = (PBYTE) lpFailbackWindowStart; break;
      case 4:  cbh_read.pb = (PBYTE) lpFailoverPeriod;      break;
      case 5:  cbh_read.pb = (PBYTE) lpFailoverThreshold;   break;
      case 6:  cbh_read.pb = (PBYTE) lpPersistentState;     break;
      default: break;
     }

    // cbPosition is the index into the property list buffer.
    // cb is the index into the current entry buffer.
    // dw iterates the entries.

    for( cb = 0 ; cb < cbPropEntrySize[dw] ; cb++, cbPosition++ )
      cbh_write.pb[cbPosition] = cbh_read.pb[cb];
   }

  // Free the memory allocated by ClusDocEx_CreatePropertyListEntry

  LocalFree( lpAutoFailbackType );    
  LocalFree( lpDescription );         
  LocalFree( lpFailbackWindowEnd );   
  LocalFree( lpFailbackWindowStart ); 
  LocalFree( lpFailoverPeriod );      
  LocalFree( lpFailoverThreshold );   
  LocalFree( lpPersistentState );     

  return lpPropList;

 }
//  end ClusDocEx_GrpCreatePropertyList
//--------------------------------------------------------------------
#endif
```



 

 




