---
title: Getting Information with Control Codes
description: Control codes that get information from the cluster use the control code function's output buffer in which to return data. Although the nature of the returned data can vary, the same set of procedures apply.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '1611745e-b8db-4b4b-9a12-1812591e01ac'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["control codes Failover Cluster ,retrieving information"]
---

# Getting Information with Control Codes

[Control codes](about-control-codes.md) that get information from the cluster use the [control code function's](control-code-functions.md) output buffer in which to return data. Although the nature of the returned data can vary, the same set of procedures apply.

**To get information with a control code**

1.  Allocate an output buffer.
2.  Call the control code function.
3.  Test the return value. If the function returns **ERROR\_MORE\_DATA**, use the *lpcbBytesReturned* parameter to reallocate the buffer and call the function again.
4.  If successful, you now have data in the output buffer. The *lpcbBytesReturned* parameter indicates the size of the data in bytes.

The returned buffer may contain a **DWORD**, a string, or a value or property list, as specified by the control code.

## Example

The following example is a collection of functions that encapsulate the above procedure for various object types.


```C++
#include <windows.h>

////////////////////////////////////////////////////////////////////////////////
//
//  ClusDocEx_GetControlCodeOutput.cpp
//
//  Functions that encapsulate the algorithm for using control
//  codes that return data in an output buffer.
//
//  Contains the following functions
//      ClusDocEx_CluGetControlCodeOutput
//      ClusDocEx_GrpGetControlCodeOutput
//      ClusDocEx_NetGetControlCodeOutput
//      ClusDocEx_NICGetControlCodeOutput
//      ClusDocEx_NodGetControlCodeOutput
//      ClusDocEx_ResGetControlCodeOutput
//      ClusDocEx_RtpGetControlCodeOutput
//
////////////////////////////////////////////////////////////////////////////////


#include "ClusDocEx.h"


////////////////////////////////////////////////////////////////////////////////


#ifndef _CLUSDOCEX_GRPGETCONTROLCODEOUTPUT
#define _CLUSDOCEX_GRPGETCONTROLCODEOUTPUT
//------------------------------------------------------------------------------
//
//  ClusDocEx_GrpGetControlCodeOutput
//
//  Encapsulates group control code operations that retrieve 
//  data into an output buffer.
//
//  Call LocalFree to free the memory allocated by this function.
//
//  Arguments:
//      hGroup         [in]  Handle to the group to affect.
//      hNode          [in]  Optional node handle.
//      dwControlCode  [in]  Specifies the control code operation.
//      lpcbResultSize [out] Byte size of the resulting data.
//
//
//  Return Value:
//      If successful, returns a pointer to a buffer containing the
//      results of the control code operation. The nature of the data
//      returned depends on the control code.
//      If unsuccessful, returns NULL. Call GetLastError for more information.
//
//------------------------------------------------------------------------------
LPVOID
ClusDocEx_GrpGetControlCodeOutput
 (
  IN  HGROUP  hGroup,
  IN  HNODE   hNode,
  IN  DWORD   dwControlCode,
  OUT LPDWORD lpcbResultSize
 )
 {
  DWORD  dwResult    = ERROR_SUCCESS;
  DWORD  cbBufSize   = sizeof( DWORD );
  LPVOID lpOutBuffer = LocalAlloc( LPTR, cbBufSize );

  if( lpOutBuffer == NULL )
   {
    dwResult = GetLastError();
    goto endf;
   }


// Call the control code function:  

   dwResult = ClusterGroupControl( hGroup,           // Handle to the group
                                   hNode,            // Optional node handle
                                   dwControlCode,    // Control code
                                   NULL,             // Input buffer. Not used
                                   0,                // Byte size of input buffer
                                   lpOutBuffer,      // Output buffer
                                   cbBufSize,        // Byte size of output buffer
                                   lpcbResultSize ); // Byte size of resulting data


// Reallocate if necessary.

   if ( dwResult == ERROR_MORE_DATA )
    {
     LocalFree( lpOutBuffer );

     cbBufSize = *lpcbResultSize;

     lpOutBuffer = LocalAlloc( LPTR, cbBufSize );

     if( lpOutBuffer == NULL )
      {
       dwResult = GetLastError();
       goto endf;
      }

     dwResult = ClusterGroupControl( hGroup,           // Handle to the affected group.
                                     hNode,            // Optional node handle.
                                     dwControlCode,    // Control code.
                                     NULL,             // Input buffer. Not used.
                                     0,                // Byte size of input buffer.
                                     lpOutBuffer,      // Output buffer.
                                     cbBufSize,        // Byte size of output buffer.
                                     lpcbResultSize ); // Byte size of resulting data.
    }


//  Handle errors.

   if( dwResult != ERROR_SUCCESS )
    {
     LocalFree( lpOutBuffer );
     lpOutBuffer = NULL;
     *lpcbResultSize = 0;
    }


endf:

   SetLastError( dwResult );

   return lpOutBuffer;
 }
//  end ClusDocEx_GrpGetControlCodeOutput
//------------------------------------------------------------------------------
#endif


#ifndef _CLUSDOCEX_NETGETCONTROLCODEOUTPUT
#define _CLUSDOCEX_NETGETCONTROLCODEOUTPUT
//------------------------------------------------------------------------------
//  
//  ClusDocEx_NetGetControlCodeOutput
//  
//  Encapsulates network control code operations that retrieve 
//  data into an output buffer.
//         
//  Call LocalFree to free the memory allocated by this function.
//  
//  Arguments:
//      hNetwork       [in]  Handle to the network to affect.
//      hNode          [in]  Optional node handle.
//      dwControlCode  [in]  Specifies the control code operation.
//      lpcbResultSize [out] Byte size of the resulting data.
//  
//  
//  Return Value:
//      If successful, returns a pointer to a buffer containing the
//      results of the control code operation. The nature of the data
//      returned depends on the control code.
//      If unsuccessful, returns NULL. Call GetLastError for more information.
//  
//------------------------------------------------------------------------------
LPVOID
ClusDocEx_NetGetControlCodeOutput
 (
  IN  HNETWORK hNetwork,
  IN  HNODE    hNode,
  IN  DWORD    dwControlCode,
  OUT LPDWORD  lpcbResultSize
 )
 {
  DWORD  dwResult    = ERROR_SUCCESS;
  DWORD  cbBufSize   = sizeof( DWORD );
  LPVOID lpOutBuffer = LocalAlloc( LPTR, cbBufSize );

  if( lpOutBuffer == NULL )
   {
    dwResult = GetLastError();
    goto endf;
   }


// Call the control code function:  

  dwResult = ClusterNetworkControl( hNetwork,         // Handle to the network
                                    hNode,            // Optional node handle
                                    dwControlCode,    // Control code
                                    NULL,             // Input buffer. Not used
                                    0,                // Byte size of input buffer
                                    lpOutBuffer,      // Output buffer
                                    cbBufSize,        // Byte size of output buffer
                                    lpcbResultSize ); // Byte size of resulting data


// Reallocate if necessary.

  if ( dwResult == ERROR_MORE_DATA )
   {
    LocalFree( lpOutBuffer );

    cbBufSize = *lpcbResultSize;

    lpOutBuffer = LocalAlloc( LPTR, cbBufSize );

    if( lpOutBuffer == NULL )
     {
      dwResult = GetLastError();
      goto endf;
     }

    dwResult = ClusterNetworkControl( hNetwork,         // Handle to the network
                                      hNode,            // Optional node handle
                                      dwControlCode,    // Control code
                                      NULL,             // Input buffer. Not used
                                      0,                // Byte size of input buffer
                                      lpOutBuffer,      // Output buffer
                                      cbBufSize,        // Byte size of output buffer
                                      lpcbResultSize ); // Byte size of resulting data
   }


// Handle errors.

  if( dwResult != ERROR_SUCCESS )
   {
    LocalFree( lpOutBuffer );
    lpOutBuffer = NULL;
    *lpcbResultSize = 0;
   }


endf:

  SetLastError( dwResult );

  return lpOutBuffer;
 }
//  end ClusDocEx_NetGetControlCodeOutput
//------------------------------------------------------------------------------
#endif


#ifndef _CLUSDOCEX_NICGETCONTROLCODEOUTPUT
#define _CLUSDOCEX_NICGETCONTROLCODEOUTPUT
//------------------------------------------------------------------------------
//  
//  ClusDocEx_NICGetControlCodeOutput
//  
//  Encapsulates network interface control code operations that 
//  retrieve data into an output buffer.
//         
//  Call LocalFree to free the memory allocated by this function.
//  
//  Arguments:
//      hNetInterface  [in]  Handle to the network interface.
//      hNode          [in]  Optional node handle.
//      dwControlCode  [in]  Specifies the control code operation.
//      lpcbResultSize [out] Byte size of the resulting data.
//  
//  
//  Return Value:
//      If successful, returns a pointer to a buffer containing the
//      results of the control code operation. The nature of the data
//      returned depends on the control code.
//      If unsuccessful, returns NULL. Call GetLastError for more info.
//  
//------------------------------------------------------------------------------
LPVOID
ClusDocEx_NICGetControlCodeOutput
 (
  IN  HNETINTERFACE hNetInterface,
  IN  HNODE         hNode,
  IN  DWORD         dwControlCode,
  OUT LPDWORD       lpcbResultSize
 )
 {
  DWORD  dwResult    = ERROR_SUCCESS;
  DWORD  cbBufSize   = sizeof( DWORD );
  LPVOID lpOutBuffer = LocalAlloc( LPTR, cbBufSize );

  if( lpOutBuffer == NULL )
   {
    dwResult = GetLastError();
    goto endf;
   }


//  Call the control code function:  

  dwResult = ClusterNetInterfaceControl( hNetInterface,    // Handle to the affected NIC.
                                         hNode,            // Optional node handle.
                                         dwControlCode,    // Control code.
                                         NULL,             // Input buffer. Not used.
                                         0,                // Byte size of input buffer.
                                         lpOutBuffer,      // Output buffer.
                                         cbBufSize,        // Byte size of output buffer.
                                         lpcbResultSize ); // Byte size of resulting data.


//  Reallocate if necessary.

  if ( dwResult == ERROR_MORE_DATA )
   {
    LocalFree( lpOutBuffer );

    cbBufSize = *lpcbResultSize;

    lpOutBuffer = LocalAlloc( LPTR, cbBufSize );

    if( lpOutBuffer == NULL )
     {
      dwResult = GetLastError();
      goto endf;
     }

    dwResult = ClusterNetInterfaceControl( hNetInterface,    // Handle to the affected NIC.
                                           hNode,            // Optional node handle.
                                           dwControlCode,    // Control code.
                                           NULL,             // Input buffer. Not used.
                                           0,                // Byte size of input buffer.
                                           lpOutBuffer,      // Output buffer.
                                           cbBufSize,        // Byte size of output buffer.
                                           lpcbResultSize ); // Byte size of resulting data.
   }


//  Handle errors.

  if( dwResult != ERROR_SUCCESS )
   {
    LocalFree( lpOutBuffer );
    lpOutBuffer = NULL;
    *lpcbResultSize = 0;
   }


endf:

  SetLastError( dwResult );

  return lpOutBuffer;
 }
//  end ClusDocEx_NICGetControlCodeOutput
//------------------------------------------------------------------------------
#endif


#ifndef _CLUSDOCEX_NODGETCONTROLCODEOUTPUT
#define _CLUSDOCEX_NODGETCONTROLCODEOUTPUT
//------------------------------------------------------------------------------
//  
//  ClusDocEx_NodGetControlCodeOutput
//  
//  Encapsulates node control code operations that retrieve 
//  data into an output buffer.
//         
//  Call LocalFree to free the memory allocated by this function.
//  
//  Arguments:
//      hNode          [in]  Handle to the node to affect.
//      hHostNode      [in]  Optional node handle.
//      dwControlCode  [in]  Specifies the control code operation.
//      lpcbResultSize [out] Byte size of the resulting data.
//  
//  
//  Return Value:
//      If successful, returns a pointer to a buffer containing the
//      results of the control code operation. The nature of the data
//      returned depends on the control code.
//      If unsuccessful, returns NULL. Call GetLastError for more info.
//  
//------------------------------------------------------------------------------
LPVOID
ClusDocEx_NodGetControlCodeOutput
 (
  IN  HNODE   hNode,
  IN  HNODE   hHostNode,
  IN  DWORD   dwControlCode,
  OUT LPDWORD lpcbResultSize
 )
 {
  DWORD  dwResult    = ERROR_SUCCESS;
  DWORD  cbBufSize   = sizeof( DWORD );
  LPVOID lpOutBuffer = LocalAlloc( LPTR, cbBufSize );

  if( lpOutBuffer == NULL )
   {
    dwResult = GetLastError();
    goto endf;
   }


//  Call the control code function:  
 
  dwResult = ClusterNodeControl( hNode,            // Handle to the affected node.
                                 hHostNode,        // Optional node handle.
                                 dwControlCode,    // Control code
                                 NULL,             // Input buffer. Not used.
                                 0,                // Byte size of input buffer.
                                 lpOutBuffer,      // Output buffer.
                                 cbBufSize,        // Byte size of output buffer.
                                 lpcbResultSize ); // Byte size of resulting data.


//  Reallocate if necessary.

  if ( dwResult == ERROR_MORE_DATA )
   {
    LocalFree( lpOutBuffer );

    cbBufSize = *lpcbResultSize;

    lpOutBuffer = LocalAlloc( LPTR, cbBufSize );

    if( lpOutBuffer == NULL )
     {
      dwResult = GetLastError();
      goto endf;
     }

    dwResult = ClusterNodeControl( hNode,            // Handle to the affected node.
                                   hHostNode,        // Optional node handle.
                                   dwControlCode,    // Control code.
                                   NULL,             // Input buffer. Not used.
                                   0,                // Byte size of input buffer.
                                   lpOutBuffer,      // Output buffer.
                                   cbBufSize,        // Byte size of output buffer.
                                   lpcbResultSize ); // Byte size of resulting data.
   }


//  Handle errors.

  if( dwResult != ERROR_SUCCESS )
   {
    LocalFree( lpOutBuffer );
    lpOutBuffer = NULL;
    *lpcbResultSize = 0;
   }


endf:

  SetLastError( dwResult );

  return lpOutBuffer;
 }
//  end ClusDocEx_NodGetControlCodeOutput
//------------------------------------------------------------------------------
#endif

#ifndef _CLUSDOCEX_RESGETCONTROLCODEOUTPUT
#define _CLUSDOCEX_RESGETCONTROLCODEOUTPUT
//------------------------------------------------------------------------------
//  
//  ClusDocEx_ResGetControlCodeOutput
//  
//  Encapsulates resource control code operations that retrieve 
//  data into an output buffer.
//         
//  Call LocalFree to free the memory allocated by this function.
//  
//  Arguments:
//      hResource      [in]  Handle to the resource to affect.
//      hNode          [in]  Optional node handle.
//      dwControlCode  [in]  Specifies the control code operation.
//      lpcbResultSize [out] Byte size of the resulting data.
//  
//  
//  Return Value:
//      If successful, returns a pointer to a buffer containing the
//      results of the control code operation. The nature of the data
//      returned depends on the control code.
//      If unsuccessful, returns NULL. Call GetLastError for more info.
//  
//------------------------------------------------------------------------------
LPVOID
ClusDocEx_ResGetControlCodeOutput
 (
    IN  HRESOURCE hResource,
    IN  HNODE     hNode,
    IN  DWORD     dwControlCode,
    OUT LPDWORD   lpcbResultSize
 )
 {
  DWORD  dwResult    = ERROR_SUCCESS;
  DWORD  cbBufSize   = sizeof( DWORD );
  LPVOID lpOutBuffer = LocalAlloc( LPTR, cbBufSize );

  if( lpOutBuffer == NULL )
   {
    dwResult = GetLastError();
    goto endf;
   }


//  Call the control code function:  

  dwResult = ClusterResourceControl( hResource,        // Handle to the affected resource.
                                     hNode,            // Optional node handle.
                                     dwControlCode,    // Control code.
                                     NULL,             // Input buffer. Not used.
                                     0,                // Byte size of input buffer.
                                     lpOutBuffer,      // Output buffer.
                                     cbBufSize,        // Byte size of output buffer.
                                     lpcbResultSize ); // Byte size of resulting data.


//  Reallocate if necessary.

  if ( dwResult == ERROR_MORE_DATA )
   {
    LocalFree( lpOutBuffer );

    cbBufSize = *lpcbResultSize;

    lpOutBuffer = LocalAlloc( LPTR, cbBufSize );

    if( lpOutBuffer == NULL )
     {
      dwResult = GetLastError();
      goto endf;
     }

    dwResult = ClusterResourceControl( hResource,        // Handle to the affected resource.
                                       hNode,            // Optional node handle
                                       dwControlCode,    // Control code.
                                       NULL,             // Input buffer. Not used.
                                       0,                // Byte size of input buffer.
                                       lpOutBuffer,      // Output buffer.
                                       cbBufSize,        // Byte size of output buffer.
                                       lpcbResultSize ); // Byte size of resulting data.
   }


//  Handle errors.

  if( dwResult != ERROR_SUCCESS )
   {
    LocalFree( lpOutBuffer );
    lpOutBuffer = NULL;
    *lpcbResultSize = 0;
   }


endf:

  SetLastError( dwResult );

  return lpOutBuffer;
 }
//  end ClusDocEx_ResGetControlCodeOutput
//------------------------------------------------------------------------------
#endif


#ifndef _CLUSDOCEX_RTPGETCONTROLCODEOUTPUT
#define _CLUSDOCEX_RTPGETCONTROLCODEOUTPUT
//------------------------------------------------------------------------------
//  
//  ClusDocEx_RtpGetControlCodeOutput
//  
//  Encapsulates resource type control code operations that retrieve 
//  data into an output buffer.
//         
//  Call LocalFree to free the memory allocated by this function.
//  
//  Arguments:
//      lpszType       [in]  Name of the resource type.
//      hCluster       [in]  Cluster handle.
//      hNode          [in]  Optional node handle.
//      dwControlCode  [in]  Specifies the control code operation.
//      lpcbResultSize [out] Byte size of the resulting data.
//                           
//  
//  Return Value:
//      If successful, returns a pointer to a buffer containing the
//      results of the control code operation. The nature of the data
//      returned depends on the control code.
//      If unsuccessful, returns NULL. Call GetLastError for more info.
//  
//------------------------------------------------------------------------------
LPVOID
ClusDocEx_RtpGetControlCodeOutput
 (
  IN  LPWSTR   lpszType,
  IN  HCLUSTER hCluster,
  IN  HNODE    hNode,
  IN  DWORD    dwControlCode,
  OUT LPDWORD  lpcbResultSize
 )
 {
  DWORD  dwResult     = ERROR_SUCCESS;
  DWORD  cbBufSize    = sizeof( DWORD );

  LPVOID lpOutBuffer  = LocalAlloc( LPTR, cbBufSize );

  if( lpOutBuffer == NULL )
   {
    dwResult = GetLastError();
    goto endf;
   }


//  Call the control code function:  

  dwResult = ClusterResourceTypeControl( hCluster,         // Cluster handle.
                                         lpszType,         // name of the resource type.
                                         hNode,            // Optional node handle.
                                         dwControlCode,    // Control code.
                                         NULL,             // Input buffer. Not used.
                                         0,                // Byte size of input buffer.
                                         lpOutBuffer,      // Output buffer.
                                         cbBufSize,        // Byte size of output buffer.
                                         lpcbResultSize ); // Byte size of resulting data.


//  Reallocate if necessary.

  if ( dwResult == ERROR_MORE_DATA )
   {
    LocalFree( lpOutBuffer );

    cbBufSize = *lpcbResultSize;

    lpOutBuffer = LocalAlloc( LPTR, cbBufSize );

    if( lpOutBuffer == NULL )
     {
      dwResult = GetLastError();
      goto endf;
     }

    dwResult = ClusterResourceTypeControl( hCluster,         // Cluster handle.
                                           lpszType,         // name of the resource type.
                                           hNode,            // Optional node handle.
                                           dwControlCode,    // Control code.
                                           NULL,             // Input buffer. Not used.
                                           0,                // Byte size of input buffer.
                                           lpOutBuffer,      // Output buffer.
                                           cbBufSize,        // Byte size of output buffer.
                                           lpcbResultSize ); // Byte size of resulting data.
   }


//  Handle errors.

  if( dwResult != ERROR_SUCCESS )
   {
    LocalFree( lpOutBuffer );
    lpOutBuffer = NULL;
    *lpcbResultSize = 0;
   }


endf:
    
  SetLastError( dwResult );

  return lpOutBuffer;
 }
//  end ClusDocEx_RtpGetControlCodeOutput
//------------------------------------------------------------------------------
#endif

////////////////////////////////////////////////////////////////////////////////

//  end ClusDocEx_GetControlCodeOutput.cpp
```



 

 




