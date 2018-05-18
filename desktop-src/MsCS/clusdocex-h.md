---
title: ClusDocEx.h
description: This header file loads the necessary libraries and utilities and defines some useful constants, macros, and functions. For any example to compile, the code from ClusDocEx.h must be available.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'fc2032d2-40a5-45bd-8661-1e778789bad6'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["ClusDocEx.h Failover Cluster"]
---

# ClusDocEx.h

This header file loads the necessary libraries and utilities and defines some useful constants, macros, and functions. For any example to compile, the code from ClusDocEx.h must be available.

``` syntax
#ifndef _CLUSDOCEX_H
#define _CLUSDOCEX_H
//////////////////////////////////////////////////////////////////////
//
//  ClusDocEx.h
//  
//  Defines constants, functions, and macros used by code examples 
//  for the Failover Cluster API as presented in the 
//  Windows SDK documentation.
//
//////////////////////////////////////////////////////////////////////

//  Enable Unicode

#ifndef UNICODE

#define UNICODE

#endif

#ifndef _UNICODE

#define _UNICODE

#endif


//  Windows/WCHAR support

#include <windows.h>

#include <tchar.h>

#include <StrSafe.h>

//  Failover Cluster API Compiler Directives

#include <ClusAPI.h>                   // Cluster API.

#include <ResApi.h>                    // Resource API.

#pragma comment( lib, "ClusAPI.lib" )  // Cluster API library.

#pragma comment( lib, "ResUtils.lib" ) // Utility Library.

//////////////////////////////////////////////////////////////////////

//  Constants

//  For specifying string and buffer sizes:

    const DWORD ClusDocEx_DEFAULT_CCH = 256; 

    const DWORD ClusDocEx_DEFAULT_CB  = 256 * sizeof( WCHAR );


//////////////////////////////////////////////////////////////////////

//  Functions

//--------------------------------------------------------------------
//  ClusDocEx_ListEntrySize
//
//  Calculates the size of a value list entry based on the
//  byte size of the data. This is an overloaded function
//  that can be called in two ways:
//
//  Arguments:
//
//      cbDataLength [in]  Byte size of the data to be added
//                         as a value list entry.
//                 - OR -
//      lpszData     [in]  NULL-terminated Unicode string containing
//                         the data to be added as a value list entry.
//
//  Return Value:
//
//      (DWORD) Total byte size required for a value list entry
//              containing the data.
//
//--------------------------------------------------------------------
inline
DWORD
WINAPI
ClusDocEx_ListEntrySize
(
    DWORD cbDataLength
)
{
    return
    (
        sizeof( CLUSPROP_VALUE ) +     // Syntax and length.
        ALIGN_CLUSPROP( cbDataLength ) // Data and padding.
    );
}

//--------------------------------------------------------------------
//  ClusDocEx_DebugPrint
//   
//  Displays debug information.
//        
//  Arguments:
//      LPWSTR lpszMessage  [in]  Optional user-defined message.
//      DWORD  dwErrorCode  [in]  Any system error code.
//
//  Return Value:
//      None.
//--------------------------------------------------------------------
inline
void
ClusDocEx_DebugPrint
( 
    LPWSTR lpszMessage,
    DWORD dwErrorCode
)
{
    LPVOID lpMsgBuf = NULL;

//  FormatMessage is a function
    FormatMessage( ( FORMAT_MESSAGE_ALLOCATE_BUFFER |
                     FORMAT_MESSAGE_FROM_SYSTEM ),
                   NULL,
                   dwErrorCode,
                   MAKELANGID( LANG_NEUTRAL, SUBLANG_DEFAULT ),
                   (LPTSTR) &lpMsgBuf,
                   0,
                   NULL );

    wprintf( L"\n(+)\n" );

    if( lpszMessage != NULL )
        wprintf( L"...%ls\n", lpszMessage );

    wprintf( L"...Line %li of %ls\n", __LINE__, __FILE__ );

    wprintf( L"...Result = %li: %ls \n", 
             dwErrorCode, (LPWSTR)lpMsgBuf );

    wprintf( L"(-)\n\n" );

//  Free the buffer allocated by FormatMessage
    LocalFree( lpMsgBuf );
}


//--------------------------------------------------------------------
//  ClusDocEx_ShowBuffer
//
//  Displays a block of memory as a sequence of bytes.
//
//  Arguments:
//
//      lpData     [in]  Pointer to the start of the data to read.
//      cbLength   [in]  Number of bytes to read.
//
//  Return Value:
//
//      None.
//--------------------------------------------------------------------
inline
void
ClusDocEx_ShowBuffer
(
    LPVOID lpData, 
    DWORD cbLength
)
{
    DWORD dw;
    CLUSPROP_BUFFER_HELPER cbh;

    if( lpData != NULL )
    {       
        cbh.pb = (PBYTE) lpData;

        wprintf( L"\n\nBegin...\n\n" );
        wprintf( L"Address   +0  +1  +2  +3  +4  +5  +6  +7  +8  +9  +A  +B  +C  +D  +E  +F\n" );
        wprintf( L"--------  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --\n%08lX  ", cbh.pb );
        
        for( dw = 0 ; dw < cbLength ; dw++ )
        {           
            wprintf( L"%02lX  ", cbh.pb[dw] );
     
            if( ( ( dw + 1 ) % 16 ) == 0 )
                wprintf( L"\n%08lX  ", cbh.pb + dw + 1 );
        }

        wprintf( L"\n\n...end\n\n" );
    }
    else
    {
        wprintf( L"\nNULL buffer.\n\n" );
    }
}

// end ClusDocEx_ShowBuffer


//--------------------------------------------------------------------
//  ClusDocEx_ConvertArg
//
//  Converts single-byte strings to Unicode strings.
//  Used to make command-line arguments and console input
//  ready for use in cluster functions.
//
//  Returns an error code.
//--------------------------------------------------------------------
inline
DWORD
ConvertArg( 
    char *pszArg,       // Single-byte string to convert.
    LPWSTR lpszOut,     // Wide character buffer to return result.
    DWORD cchOutChars   // Size of the buffer as a count of WCHARs.
)
{
    MultiByteToWideChar( 
        CP_ACP,                   // Specifies the code page to use.
        ( MB_PRECOMPOSED |  
          MB_ERR_INVALID_CHARS ), // Flags governing the conversion.
        pszArg,
        -1,
        lpszOut,
        int( cchOutChars )
    );

    return GetLastError();
}


//////////////////////////////////////////////////////////////////////

//  Forward Declarations

void
ClusDocEx_BasicPropertyValueList();

LPVOID 
ClusDocEx_CreateValueListEntry(
    IN DWORD dwSyntax,
    IN DWORD cbLength,
    IN LPVOID lpData,
    OUT LPDWORD lpcbEntrySize
);

DWORD
ClusDocEx_FindSyntax( 
    IN LPVOID lpList,
    IN DWORD cbListSize,
    IN DWORD dwSyntax,
    IN DWORD cbStartPos = 0 
);

void
ClusDocEx_CreateRequiredDependenciesList();

BOOL   
ClusDocEx_NodIsSignatureAvailable(
    IN HCLUSTER hCluster,
    IN HNODE    hNode,
    IN DWORD    dwSignature 
);

LPVOID
ClusDocEx_CreatePropertyListEntry(
    IN LPWSTR lpszPropName,
    IN DWORD dwSyntax,
    IN DWORD cbLength,
    IN LPVOID lpData,
    OUT LPDWORD lpcbEntrySize
);

LPVOID
ClusDocEx_GrpCreatePropertyList(
    LPDWORD lpcbPropListSize,
    DWORD dwAutoFailbackType,
    LPWSTR lpszDescription,
    DWORD dwFailbackWindowEnd,
    DWORD dwFailbackWindowStart,
    DWORD dwFailoverPeriod,
    DWORD dwFailoverThreshold,
    DWORD dwPersistentState 
);

DWORD 
GrpGetRWCDwPropValue( 
    IN HGROUP hGroup,
    IN LPCWSTR lpszPropName,
    OUT LPDWORD lpdwPropValue
);

HCLUSTER ClusDocEx_OpenLocalClusterWithName();

DWORD
ClusDocEx_ResAddPossibleOwner( 
    LPWSTR lpszResourceName,
    LPWSTR lpszNodeName,
    LPWSTR lpszClusterName 
);

LPVOID
ClusDocEx_GrpGetControlCodeOutput(
    IN HGROUP hGroup,
    IN HNODE hNode,
    IN DWORD dwControlCode,
    OUT LPDWORD lpcbResultSize
);

LPVOID
ClusDocEx_NetGetControlCodeOutput(
    IN HNETWORK hNetwork,
    IN HNODE hNode,
    IN DWORD dwControlCode,
    OUT LPDWORD lpcbResultSize
);

LPVOID
ClusDocEx_NICGetControlCodeOutput(
    IN HNETINTERFACE hNetInterface,
    IN HNODE hNode,
    IN DWORD dwControlCode,
    OUT LPDWORD lpcbResultSize
);

LPVOID
ClusDocEx_NodGetControlCodeOutput(
    IN HNODE hNode,
    IN HNODE hHostNode,
    IN DWORD dwControlCode,
    OUT LPDWORD lpcbResultSize
);

LPVOID
ClusDocEx_ResGetControlCodeOutput(
    IN HRESOURCE hResource,
    IN HNODE hNode,
    IN DWORD dwControlCode,
    OUT LPDWORD lpcbResultSize
);

LPVOID
ClusDocEx_RtpGetControlCodeOutput(
    IN LPWSTR lpszType,
    IN HCLUSTER hCluster,
    IN HNODE hNode,
    IN DWORD dwControlCode,
    OUT LPDWORD lpcbResultSize
);

DWORD
ClusDocEx_SetResourceName(
    HRESOURCE hResource,
    LPWSTR lpszResName
);

void
ClusDocEx_ShowBinary( 
    DWORD dwNum 
);

void 
ClusDocEx_ParseCode( 
    char* pName, 
    DWORD dwCode 
);

DWORD ClusDocEx_ParseDword( 
    DWORD dwNumber, 
    int iHighBit, 
    int iLowBit 
);

DWORD 
WINAPI
ClusDocEx_EventPort( 
     LPVOID hCluster
);

void 
ClusDocEx_EventMessage( 
    HCLUSTER hCluster,
    DWORD    dwNotifyKey,
    DWORD    dwFilterType,
    LPWSTR   lpszObjectName 
);

DWORD
ClusDocEx_GrpEnumResources(
    IN HGROUP hGroup,
    IN OUT LPVOID lpOutBuffer,
    IN DWORD  cbOutBufferSize,
    OUT LPDWORD lpcbResultSize
);

LPWSTR
ClusDocEx_ResDescribeState( 
    HRESOURCE hRdsource 
);

DWORD 
ClusDocEx_ResGetRWCDwordProperty(
    IN LPWSTR lpszResName, 
    IN LPWSTR lpszPropName,
    OUT LPDWORD lpdwPropvalue
);

DWORD
ClusDocEx_GrpResetPropertyDefaults( 
    IN HGROUP hGroup 
);

HGROUP
ClusDocEx_GrpCreateVirtualServer(
    IN HCLUSTER hCluster,
    IN LPWSTR   lpszGroupName,
    IN LPWSTR   lpszIPResName,
    IN LPWSTR   lpszNetResName,
    IN LPWSTR   lpszIPAddress,
    IN LPWSTR   lpszNetworkName,
    IN LPWSTR   lpszSubnetMask
);

HRESOURCE
ClusDocEx_ResCreateDisk(
    IN HCLUSTER hCluster,
    IN HGROUP   hGroup,
    IN LPWSTR   lpszDriveLtr
);

HRESOURCE
ClusDocEx_ResCreateIPAddress(
    IN HGROUP hGroup,
    IN LPWSTR lpszResName,
    IN LPWSTR lpszAddress,
    IN LPWSTR lpszNetwork,
    IN LPWSTR lpszSubnetMask
);

HRESOURCE
ClusDocEx_ResCreateNetworkName(
    IN HGROUP    hGroup,
    IN HRESOURCE hIPDependency,
    IN LPWSTR    lpszResName,
    IN LPWSTR    lpszNetName
);

int
ClusDocEx_IsGroupProperty
(
    IN HGROUP hGroup,
    IN LPWSTR lpszPropName
);

LPVOID
ClusDocEx_ResGetRWCProperties(
    IN HRESOURCE hRes,
    IN HNODE     hNode,
    OUT LPDWORD  lpcbDataSize
);

LPWSTR
ClusDocEx_ResGetName(
    IN HRESOURCE hRes,
    IN HNODE     hNode
);

LPVOID
ClusDocEx_ResGetRWPProperties(
    IN HRESOURCE hRes,
    IN HNODE     hNode,
    OUT LPDWORD  lpcbDataSize
);

LPVOID
ClusDocEx_ResGetRegistryCheckpoints(
    IN HRESOURCE hRes,
    IN HNODE     hNode,
    OUT LPDWORD  lpcbDataSize
);

LPVOID
ClusDocEx_ResGetRequiredDependencies(
    IN HRESOURCE hRes,
    IN HNODE     hNode,
    OUT LPDWORD  lpcbDataSize
);

LPWSTR
ClusDocEx_ResGetResourceType(
    IN HRESOURCE hRes,
    IN HNODE     hNode
);

LPVOID
ClusDocEx_ResGetROCProperties(
    IN HRESOURCE hRes,
    IN HNODE     hNode,
    OUT LPDWORD  lpcbDataSize
);

LPVOID
ClusDocEx_ResGetROPProperties(
    IN HRESOURCE hRes,
    IN HNODE     hNode,
    OUT LPDWORD  lpcbDataSize
);

//////////////////////////////////////////////////////////////////////

#endif

// end ClusDocEx.h
```

 

 




