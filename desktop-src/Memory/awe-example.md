---
description: The following sample program illustrates the Address Windowing Extensions.
ms.assetid: 1a67bd2f-afc0-48f4-91f2-34fd2b94910d
title: AWE Example
ms.topic: article
ms.date: 05/31/2018
---

# AWE Example

The following sample program illustrates the [**Address Windowing Extensions**](address-windowing-extensions.md).


```C++
#include <windows.h>
#include <stdio.h>
#include <tchar.h>

#define MEMORY_REQUESTED 1024*1024 // request a megabyte

BOOL
LoggedSetLockPagesPrivilege ( HANDLE hProcess,
                              BOOL bEnable);

void _cdecl main()
{
  BOOL bResult;                   // generic Boolean value
  ULONG_PTR NumberOfPages;        // number of pages to request
  ULONG_PTR NumberOfPagesInitial; // initial number of pages requested
  ULONG_PTR *aPFNs;               // page info; holds opaque data
  PVOID lpMemReserved;            // AWE window
  SYSTEM_INFO sSysInfo;           // useful system information
  int PFNArraySize;               // memory to request for PFN array

  GetSystemInfo(&sSysInfo);  // fill the system information structure

  _tprintf(_T("This computer has page size %d.\n"), sSysInfo.dwPageSize);

  // Calculate the number of pages of memory to request.

  NumberOfPages = MEMORY_REQUESTED/sSysInfo.dwPageSize;
  _tprintf (_T("Requesting %d pages of memory.\n"), NumberOfPages);

  // Calculate the size of the user PFN array.

  PFNArraySize = NumberOfPages * sizeof (ULONG_PTR);

  _tprintf (_T("Requesting a PFN array of %d bytes.\n"), PFNArraySize);

  aPFNs = (ULONG_PTR *) HeapAlloc(GetProcessHeap(), 0, PFNArraySize);

  if (aPFNs == NULL) 
  {
    _tprintf (_T("Failed to allocate on heap.\n"));
    return;
  }

  // Enable the privilege.

  if( ! LoggedSetLockPagesPrivilege( GetCurrentProcess(), TRUE ) ) 
  {
    return;
  }

  // Allocate the physical memory.

  NumberOfPagesInitial = NumberOfPages;
  bResult = AllocateUserPhysicalPages( GetCurrentProcess(),
                                       &NumberOfPages,
                                       aPFNs );
    
  if( bResult != TRUE ) 
  {
    _tprintf(_T("Cannot allocate physical pages (%u)\n"), GetLastError() );
    return;
  }

  if( NumberOfPagesInitial != NumberOfPages ) 
  {
    _tprintf(_T("Allocated only %p pages.\n"), NumberOfPages );
    return;
  }

  // Reserve the virtual memory.
    
  lpMemReserved = VirtualAlloc( NULL,
                                MEMORY_REQUESTED,
                                MEM_RESERVE | MEM_PHYSICAL,
                                PAGE_READWRITE );

  if( lpMemReserved == NULL ) 
  {
    _tprintf(_T("Cannot reserve memory.\n"));
    return;
  }

  // Map the physical memory into the window.
    
  bResult = MapUserPhysicalPages( lpMemReserved,
                                  NumberOfPages,
                                  aPFNs );

  if( bResult != TRUE ) 
  {
    _tprintf(_T("MapUserPhysicalPages failed (%u)\n"), GetLastError() );
    return;
  }

  // unmap
    
  bResult = MapUserPhysicalPages( lpMemReserved,
                                  NumberOfPages,
                                  NULL );

  if( bResult != TRUE ) 
  {
    _tprintf(_T("MapUserPhysicalPages failed (%u)\n"), GetLastError() );
    return;
  }

  // Free the physical pages.

  bResult = FreeUserPhysicalPages( GetCurrentProcess(),
                                   &NumberOfPages,
                                   aPFNs );

  if( bResult != TRUE ) 
  {
    _tprintf(_T("Cannot free physical pages, error %u.\n"), GetLastError());
    return;
  }

  // Free virtual memory.

  bResult = VirtualFree( lpMemReserved,
                         0,
                         MEM_RELEASE );

  // Release the aPFNs array.

  bResult = HeapFree(GetProcessHeap(), 0, aPFNs);

  if( bResult != TRUE )
  {
      _tprintf(_T("Call to HeapFree has failed (%u)\n"), GetLastError() );
  }

}

/*****************************************************************
   LoggedSetLockPagesPrivilege: a function to obtain or
   release the privilege of locking physical pages.

   Inputs:

       HANDLE hProcess: Handle for the process for which the
       privilege is needed

       BOOL bEnable: Enable (TRUE) or disable?

   Return value: TRUE indicates success, FALSE failure.

*****************************************************************/
BOOL
LoggedSetLockPagesPrivilege ( HANDLE hProcess,
                              BOOL bEnable)
{
  struct {
    DWORD Count;
    LUID_AND_ATTRIBUTES Privilege [1];
  } Info;

  HANDLE Token;
  BOOL Result;

  // Open the token.

  Result = OpenProcessToken ( hProcess,
                              TOKEN_ADJUST_PRIVILEGES,
                              & Token);

  if( Result != TRUE ) 
  {
    _tprintf( _T("Cannot open process token.\n") );
    return FALSE;
  }

  // Enable or disable?

  Info.Count = 1;
  if( bEnable ) 
  {
    Info.Privilege[0].Attributes = SE_PRIVILEGE_ENABLED;
  } 
  else 
  {
    Info.Privilege[0].Attributes = 0;
  }

  // Get the LUID.

  Result = LookupPrivilegeValue ( NULL,
                                  SE_LOCK_MEMORY_NAME,
                                  &(Info.Privilege[0].Luid));

  if( Result != TRUE ) 
  {
    _tprintf( _T("Cannot get privilege for %s.\n"), SE_LOCK_MEMORY_NAME );
    return FALSE;
  }

  // Adjust the privilege.

  Result = AdjustTokenPrivileges ( Token, FALSE,
                                   (PTOKEN_PRIVILEGES) &Info,
                                   0, NULL, NULL);

  // Check the result.

  if( Result != TRUE ) 
  {
    _tprintf (_T("Cannot adjust token privileges (%u)\n"), GetLastError() );
    return FALSE;
  } 
  else 
  {
    if( GetLastError() != ERROR_SUCCESS ) 
    {
      _tprintf (_T("Cannot enable the SE_LOCK_MEMORY_NAME privilege; "));
      _tprintf (_T("please check the local policy.\n"));
      return FALSE;
    }
  }

  CloseHandle( Token );

  return TRUE;
}
```



 

 



