---
title: Parsing a Value List
description: The following example parses a value list returned from the CLUSCTL\_RESOURCE\_TYPE\_STORAGE\_GET\_AVAILABLE\_DISKS control code.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '3504b04d-9b96-4b44-a8ae-f5e5eb8231d8'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["value lists Failover Cluster ,parsing"]
---

# Parsing a Value List

The following example parses a value list returned from the [CLUSCTL\_RESOURCE\_TYPE\_STORAGE\_GET\_AVAILABLE\_DISKS](clusctl-resource-type-storage-get-available-disks.md) control code.


```C++
#include <windows.h>

//////////////////////////////////////////////////////////////////////

#include "ClusDocEx.h"

//////////////////////////////////////////////////////////////////////

#ifndef _CLUSDOCEX_NODISSIGNATUREAVAILABLE_CPP
#define _CLUSDOCEX_NODISSIGNATUREAVAILABLE_CPP

//--------------------------------------------------------------------
//  ClusDocEx_NodIsSignatureAvailable
//
//  Tests whether a node can access a disk with a specified signature.
// 
//  Arguments:
//    IN HCLUSTER hCluster       Cluster handle.
//    IN HNODE    hNode          Handle to the node to query.
//    IN DWORD    dwSignature    Signature to query for.
//
//  Return Value:
//    TRUE if the signature is available to the node
//    FALSE if not (or if an error occurs)
//
//--------------------------------------------------------------------
BOOL ClusDocEx_NodIsSignatureAvailable
(
    IN HCLUSTER hCluster,
    IN HNODE    hNode,
    IN DWORD    dwSignature
)
{
    DWORD dwResult = ERROR_SUCCESS;

    DWORD cbPosition = 0;
    DWORD cbListSize = 0;
    BOOL  bDiskFound = FALSE;

    LPVOID lpValueList = NULL;

    CLUSPROP_BUFFER_HELPER cbh;

    if( ( hCluster == NULL ) ||
        ( hNode == NULL ) )
    {
        dwResult = ERROR_BAD_ARGUMENTS;
        goto endf;
    }

//  Get all disks available to the specified node.
    
    lpValueList = ClusDocEx_RtpGetControlCodeOutput( 
                             L"Physical Disk",
                             hCluster,
                             hNode,
                             CLUSCTL_RESOURCE_TYPE_STORAGE_GET_AVAILABLE_DISKS,
                             &amp;cbListSize );

    if( lpValueList == NULL )
    {
        dwResult = GetLastError();
        goto endf;
    }


//  Parse the buffer. The control code returns a value list.
//  The entry for each disk begins with a CLUSPROP_DISK_SIGNATURE structure.

    cbh.pb = (PBYTE) lpValueList;

    while( 1 )
    {
        if( ( cbh.pDiskSignatureValue->Syntax.dw == CLUSPROP_SYNTAX_DISK_SIGNATURE ) &amp;&amp;
            ( cbh.pDiskSignatureValue->dw == dwSignature ) ) 
        {
        //  Syntax indicates a CLUSPROP_DISK_SIGNATURE structure.
        //  The signature found matches the specified signature.
            bDiskFound = TRUE;
            break;
        }
        else if( cbh.pSyntax->dw == CLUSPROP_SYNTAX_ENDMARK )
        //  Reached the end of the list.
            break;

    //  Add the size of the current entry to the position indicator
        cbPosition += ClusDocEx_ListEntrySize( cbh.pValue->cbLength );

    //  Compare position indicator to the size of the list.
    //  Adding sizeof( DWORD ) allows for the read operation at the
    //  top of the loop.
        if( ( cbPosition + sizeof( DWORD ) ) > cbListSize )
            break;

    //  Advance cbh
        cbh.pb += ClusDocEx_ListEntrySize( cbh.pValue->cbLength );

    }
    //  End while.

endf:

    if( lpValueList != NULL )
        LocalFree( lpValueList );

    SetLastError( dwResult );

    return bDiskFound;
}
//  end ClusDocEx_NodIsSignatureAvailable
//--------------------------------------------------------------------
#endif
```



 

 




