---
title: CLUSCTL\_GROUP\_ENUM\_COMMON\_PROPERTIES control code
description: Retrieves a list of the read/write group common property names for a group.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '5d5f2956-8289-48df-903b-47163ae5c1ae'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["CLUSCTL_GROUP_ENUM_COMMON_PROPERTIES control code Failover Cluster"]
topic_type:
- apiref
api_name:
- CLUSCTL_GROUP_ENUM_COMMON_PROPERTIES
api_location:
- ClusAPI.h
api_type:
- HeaderDef
---

# CLUSCTL\_GROUP\_ENUM\_COMMON\_PROPERTIES control code

Retrieves a list of the read/write [group common property](group-common-properties.md) names for a [group](groups.md). Applications use this [control code](about-control-codes.md) as a [**ClusterGroupControl**](clustergroupcontrol.md) parameter.


```C++
ClusterGroupControl( 
  hGroup,                                // group handle
  hHostNode,                             // optional node handle
  CLUSCTL_GROUP_ENUM_COMMON_PROPERTIES,  // this control code
  NULL,                                  // input buffer (not used)
  0,                                     // input buffer size (not used)
  lpOutBuffer,                           // output buffer: array of strings
  cbOutBufferSize,                       // output buffer size (bytes)
  lpcbBytesReturned                      // resulting data size (bytes)
);
```



## Parameters

The following control code function parameter is specific to this control code. For complete parameter descriptions, see [**ClusterGroupControl**](clustergroupcontrol.md).

<dl> <dt>

*lpOutBuffer* 
</dt> <dd>

On a successful return, *lpOutBuffer* contains an array of **NULL**-terminated Unicode strings with an additional **NULL**-terminator appended to the last string. Each string in the array contains the name of a read/write [group common property](group-common-properties.md).

</dd> </dl>

## Return value

[**ClusterGroupControl**](clustergroupcontrol.md) returns one of the following values.

<dl> <dt>

**ERROR\_SUCCESS**
</dt> <dd>

0

The operation completed successfully. The *lpcbBytesReturned* parameter points to the actual size of the returned data.

</dd> <dt>

**ERROR\_MORE\_DATA**
</dt> <dd>

234 (0xEA)

The output buffer pointed to by *lpOutBuffer* was not large enough to hold the data resulting from the operation. The *lpcbBytesReturned* parameter points to the size required for the output buffer.

</dd> <dt>

**[System error code](https://msdn.microsoft.com/library/windows/desktop/ms681381)**
</dt> <dd>

If any other value is returned, then the operation failed. The value of *lpcbBytesReturned* is unreliable.

</dd> </dl>

## Remarks

The CLUSCTL\_GROUP\_ENUM\_COMMON\_PROPERTIES control code returns only property names, not property values. To retrieve values for common group properties, use [CLUSCTL\_GROUP\_GET\_COMMON\_PROPERTIES](clusctl-group-get-common-properties.md) and [CLUSCTL\_GROUP\_GET\_RO\_COMMON\_PROPERTIES](clusctl-group-get-ro-common-properties.md).

Do not use any group control codes in any resource DLL entry point function. Group control codes can safely be called from a worker thread. For more information, see [Function Calls to Avoid in Resource DLLs](function-calls-to-avoid-in-resource-dlls.md).

ClusAPI.h defines the 32 bits of CLUSCTL\_GROUP\_ENUM\_COMMON\_PROPERTIES as follows (for more information, see [Control Code Architecture](control-code-architecture.md)).



| Component      | Bit location | Value                                                 |
|----------------|--------------|-------------------------------------------------------|
| Object code    | 24–31        | **CLUS\_OBJECT\_GROUP** (0x3)<br/>              |
| Global bit     | 23           | **CLUS\_NOT\_GLOBAL** (0x0)<br/>                |
| Modify bit     | 22           | **CLUS\_NO\_MODIFY** (0x0)<br/>                 |
| User bit       | 21           | **CLCTL\_CLUSTER\_BASE** (0x0)<br/>             |
| Type bit       | 20           | External (0x0)<br/>                             |
| Operation code | 0–23         | **CLCTL\_ENUM\_COMMON\_PROPERTIES** (0x51)<br/> |
| Access code    | 0–1          | **CLUS\_ACCESS\_READ** (0x1)<br/>               |



 

## Examples


```C++
#include "ClusDocEx.h"
//////////////////////////////////////////////////////////////////////
// ClusDocEx_IsGroupProperty
//
// Verifies that a string corresponds to a common group property name.
//
// Arguments:
//    IN HGROUP hGroup        Group handle.
//    IN LPWSTR lpszPropName  Possible property name to verify.
//
// Return Values
//    1   The string contains a group common property name.
//    0   The string does not match any common group property name.
//   -1   Results unknown - an error occurred. Call GetLastError for more info.
//////////////////////////////////////////////////////////////////////
int ClusDocEx_IsGroupProperty
(
    IN HGROUP hGroup,
    IN LPWSTR lpszPropName
)
{
    DWORD  dwResult    = 0;
    DWORD  cbAllocated = 256;
    DWORD  cbRequired  = 0;
    DWORD  cbBufferPos = 0;
    LPVOID lpOutBuffer = LocalAlloc( LPTR, cbAllocated );
    LPWSTR lpszParser  = NULL;
    int    intGroupProperty = -1;

    //
    // Basic bounds checking.
    //
    if( lpOutBuffer == NULL )
    {
        dwResult = GetLastError();
        goto EndFunc;
    }
    if( lpszPropName == NULL || hGroup == NULL )
    {
        dwResult = ERROR_BAD_ARGUMENTS;
        goto EndFunc;
    }

    //
    // First call.
    //
    dwResult = ClusterGroupControl( hGroup,
                                    NULL,
                                    CLUSCTL_GROUP_ENUM_COMMON_PROPERTIES,
                                    NULL,
                                    0,
                                    lpOutBuffer,
                                    cbAllocated,
                                    &amp;cbRequired );

    //
    // Reallocation routine.
    //
    if( dwResult == ERROR_MORE_DATA )
    {
        LocalFree( lpOutBuffer );
        cbAllocated = cbRequired;
        lpOutBuffer = LocalAlloc( LPTR, cbAllocated );
        dwResult = ClusterGroupControl( hGroup,
                                        NULL,
                                        CLUSCTL_GROUP_ENUM_COMMON_PROPERTIES,
                                        NULL,
                                        0,
                                        lpOutBuffer,
                                        cbAllocated,
                                        &amp;cbRequired );
    }

    //
    // Parse the output buffer (array of strings) to
    // find the specified property name.
    //
    if( dwResult == ERROR_SUCCESS )
    {
        cbBufferPos = 0;
        lpszParser = (LPWSTR)lpOutBuffer;

        if( lpOutBuffer == NULL )
        {
            dwResult = GetLastError();
            goto EndFunc;
        }

        while(1)
        {
            if( lstrcmpi( lpszPropName, lpszParser ) == 0 )
            {
                intGroupProperty = 1;
                break;
            }

            cbBufferPos += ( lstrlenW(lpszParser) + 1 ) * sizeof( WCHAR );

            if( cbBufferPos < cbRequired )
            {
                lpszParser += lstrlenW(lpszParser) + 1;
            }
            else
            {
                intGroupProperty = 0;
                break;
            }
        }
    }

EndFunc:

    LocalFree( lpOutBuffer );
    SetLastError( dwResult );
    return intGroupProperty;

}
```



## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                            |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>            |
| Header<br/>                   | <dl> <dt>ClusAPI.h</dt> </dl> |



## See also

<dl> <dt>

[Group Control Codes](group-control-codes.md)
</dt> <dt>

[CLUSCTL\_GROUP\_GET\_COMMON\_PROPERTIES](clusctl-group-get-common-properties.md)
</dt> <dt>

[CLUSCTL\_GROUP\_GET\_RO\_COMMON\_PROPERTIES](clusctl-group-get-ro-common-properties.md)
</dt> <dt>

[**ClusterGroupControl**](clustergroupcontrol.md)
</dt> </dl>

 

 





