---
title: Creating a Storage Adapter
description: Basic structure of a storage adapter plug-in implemented as a C++ dynamic link library (DLL).
ms.assetid: c37e4c46-d11c-4458-b87b-78f693188e3c
ms.topic: article
ms.date: 05/31/2018
---

# Creating a Storage Adapter

The following code example shows the basic structure of a storage adapter plug-in implemented as a C++ dynamic link library (DLL). To see pseudocode implementations of each public function in the DLL, go to [Storage Adapter Functions](storage-adapter-functions.md). If you choose to not provide functionality for a particular function, you must define a stub for it and return E\_NOTIMPL.


```C++
*++
 
    THIS CODE AND INFORMATION IS PROVIDED "AS IS" WITHOUT WARRANTY OF
    ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING BUT NOT LIMITED TO
    THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS FOR A
    PARTICULAR PURPOSE.

    Copyright (C) Microsoft. All rights reserved.

Module Name:

    StorageAdapter.cpp

Abstract:

    This module contains a stub implementation of a Storage Adapter
    plug-in for the Windows Biometric service.


    -

Environment:

    Win32, user mode only.

Revision History:

NOTES:

    (None)

--*/

/////////////////////////////////////////////////////////////////////////////////////////
//
// Header files.
//
#include "Stdafx.h"
#include "Winbio_adapter.h"
#include "StorageAdapter.h"


/////////////////////////////////////////////////////////////////////////////////////////
//
// Forward declarations for the storage adapter interface routines.
//
static HRESULT
WINAPI
StorageAdapterAttach(
    __inout PWINBIO_PIPELINE Pipeline
    );

static HRESULT
WINAPI
StorageAdapterDetach(
    __inout PWINBIO_PIPELINE Pipeline
    );

static HRESULT
WINAPI
StorageAdapterClearContext(
    __inout PWINBIO_PIPELINE Pipeline
    );

static HRESULT
WINAPI
StorageAdapterCreateDatabase(
    __inout PWINBIO_PIPELINE Pipeline,
    __in PWINBIO_UUID DatabaseId,
    __in WINBIO_BIOMETRIC_TYPE Factor,
    __in PWINBIO_UUID Format,
    __in LPCWSTR FilePath,
    __in LPCWSTR ConnectString,
    __in SIZE_T IndexElementCount,
    __in SIZE_T InitialSize
    );

static HRESULT
WINAPI
StorageAdapterEraseDatabase(
    __inout PWINBIO_PIPELINE Pipeline,
    __in PWINBIO_UUID DatabaseId,
    __in LPCWSTR FilePath,
    __in LPCWSTR ConnectString
    );

static HRESULT
WINAPI
StorageAdapterOpenDatabase(
    __inout PWINBIO_PIPELINE Pipeline,
    __in PWINBIO_UUID DatabaseId,
    __in LPCWSTR FilePath,
    __in LPCWSTR ConnectString
    );

static HRESULT
WINAPI
StorageAdapterCloseDatabase(
    __inout PWINBIO_PIPELINE Pipeline
    );

static HRESULT
WINAPI
StorageAdapterGetDataFormat(
    __inout PWINBIO_PIPELINE Pipeline,
    __out PWINBIO_UUID Format,
    __out PWINBIO_VERSION Version
    );

static HRESULT
WINAPI
StorageAdapterGetDatabaseSize(
    __inout PWINBIO_PIPELINE Pipeline,
    __out PSIZE_T AvailableRecordCount,
    __out PSIZE_T TotalRecordCount
    );

static HRESULT
WINAPI
StorageAdapterAddRecord(
    __inout PWINBIO_PIPELINE Pipeline,
    __in PWINBIO_STORAGE_RECORD RecordContents
    );

static HRESULT
WINAPI
StorageAdapterDeleteRecord(
    __inout PWINBIO_PIPELINE Pipeline,
    __in PWINBIO_IDENTITY Identity,
    __in WINBIO_BIOMETRIC_SUBTYPE SubFactor
    );

static HRESULT
WINAPI
StorageAdapterQueryBySubject(
    __inout PWINBIO_PIPELINE Pipeline,
    __in PWINBIO_IDENTITY Identity,
    __in WINBIO_BIOMETRIC_SUBTYPE SubFactor
    );

static HRESULT
WINAPI
StorageAdapterQueryByContent(
    __inout PWINBIO_PIPELINE Pipeline,
    __in WINBIO_BIOMETRIC_SUBTYPE SubFactor,
    __in ULONG IndexVector[],
    __in SIZE_T IndexElementCount
    );

static HRESULT
WINAPI
StorageAdapterGetRecordCount(
    __inout PWINBIO_PIPELINE Pipeline,
    __out PSIZE_T RecordCount
    );

static HRESULT
WINAPI
StorageAdapterFirstRecord(
    __inout PWINBIO_PIPELINE Pipeline
    );

static HRESULT
WINAPI
StorageAdapterNextRecord(
    __inout PWINBIO_PIPELINE Pipeline
    );

static HRESULT
WINAPI
StorageAdapterGetCurrentRecord(
    __inout PWINBIO_PIPELINE Pipeline,
    __out PWINBIO_STORAGE_RECORD RecordContents
    );

static HRESULT
WINAPI
StorageAdapterControlUnit(
    __inout PWINBIO_PIPELINE Pipeline,
    __in ULONG ControlCode,
    __in PUCHAR SendBuffer,
    __in SIZE_T SendBufferSize,
    __in PUCHAR ReceiveBuffer,
    __in SIZE_T ReceiveBufferSize,
    __out PSIZE_T ReceiveDataSize,
    __out PULONG OperationStatus
    );

static HRESULT
WINAPI
StorageAdapterControlUnitPrivileged(
    __inout PWINBIO_PIPELINE Pipeline,
    __in ULONG ControlCode,
    __in PUCHAR SendBuffer,
    __in SIZE_T SendBufferSize,
    __in PUCHAR ReceiveBuffer,
    __in SIZE_T ReceiveBufferSize,
    __out PSIZE_T ReceiveDataSize,
    __out PULONG OperationStatus
    );

/////////////////////////////////////////////////////////////////////////////////////////
//
// Interface dispatch table
//
static WINBIO_STORAGE_INTERFACE g_StorageInterface = {
    WINBIO_STORAGE_INTERFACE_VERSION_1,
    WINBIO_ADAPTER_TYPE_STORAGE,
    sizeof(WINBIO_STORAGE_INTERFACE),
    {0xdec3f1f2, 0x44c0, 0x4e84, {0x95, 0x97, 0x88, 0x80, 0xec, 0x89, 0x32, 0x77}},

    StorageAdapterAttach,
    StorageAdapterDetach,
    StorageAdapterClearContext,
    StorageAdapterCreateDatabase,
    StorageAdapterEraseDatabase,
    StorageAdapterOpenDatabase,
    StorageAdapterCloseDatabase,
    StorageAdapterGetDataFormat,
    StorageAdapterGetDatabaseSize,
    StorageAdapterAddRecord,
    StorageAdapterDeleteRecord,
    StorageAdapterQueryBySubject,
    StorageAdapterQueryByContent,
    StorageAdapterGetRecordCount,
    StorageAdapterFirstRecord,
    StorageAdapterNextRecord,
    StorageAdapterGetCurrentRecord,
    StorageAdapterControlUnit,
    StorageAdapterControlUnitPrivileged
};

/////////////////////////////////////////////////////////////////////////////////////////
//
// Mandatory DLL entry point function.
//
BOOL APIENTRY 
DllMain( 
    HANDLE ModuleHandle, 
    DWORD ReasonForCall, 
    LPVOID Reserved
    )
{
    UNREFERENCED_PARAMETER(ModuleHandle);
    UNREFERENCED_PARAMETER(ReasonForCall);
    UNREFERENCED_PARAMETER(Reserved);

    return TRUE;
}

/////////////////////////////////////////////////////////////////////////////////////////
//
// Well-known interface discovery function exported by the Storage Adapter
//
HRESULT
WINAPI
WbioQueryStorageInterface(
    __out PWINBIO_STORAGE_INTERFACE *StorageInterface
    )
{
    *StorageInterface = &g_StorageInterface;
    return S_OK;
}

//////////////////////////////////////////////////////////////////////////////////////////
//
// Required routines.
//      This sample adapter assumes that the following three inline functions 
//      are declared in the private sensor adapter header file. The first two
//      perform memory management. The third normalizes error codes.
//
inline
PVOID
_AdapterAlloc(
    __in SIZE_T ByteCount
    )
{
    return HeapAlloc(GetProcessHeap(), HEAP_ZERO_MEMORY, ByteCount);
}

inline
VOID
_AdapterRelease(
    __in PVOID Address
    )
{
    HeapFree(GetProcessHeap(), 0, Address);
}

inline HRESULT
_AdapterGetHresultFromWin32(
    __in DWORD Error
    )
{
    if ((Error == ERROR_CANCELLED) ||
        (Error == ERROR_OPERATION_ABORTED))
    {
        return WINBIO_E_CANCELED;
    }
    else
    {
        return WINBIO_E_DEVICE_FAILURE;
    }
}

/////////////////////////////////////////////////////////////////////////////////////////
//
// StorageAdapterAttach
//
// Purpose:
//      Performs any initialization required for later biometric operations.
//
static HRESULT
WINAPI
StorageAdapterAttach(
    __inout PWINBIO_PIPELINE Pipeline
    )
{
    
    // See the StorageAdapterAttach documentation for an implementation example.

    return S_OK;
}

/////////////////////////////////////////////////////////////////////////////////////////
//
// StorageAdapterDetach
//
// Purpose:
//      Release adapter specific resources attached to the pipeline.
//
static HRESULT
WINAPI
StorageAdapterDetach(
    __inout PWINBIO_PIPELINE Pipeline
    )
{
    
    // See the StorageAdapterDetach documentation for an implementation example.

    return S_OK;
}

/////////////////////////////////////////////////////////////////////////////////////////
//
// StorageAdapterClearContext
//
// Purpose:
//      Prepare the processing pipeline of the biometric unit for a 
//      new operation.
//
static HRESULT
WINAPI
StorageAdapterClearContext(
    __inout PWINBIO_PIPELINE Pipeline
    )
{
    
    // See the StorageAdapterClearContext documentation for an implementation example.

    return S_OK;
}

/////////////////////////////////////////////////////////////////////////////////////////
//
// StorageAdapterCreateDatabase
//
// Purpose:
//      Creates and configures a new database.
//
static HRESULT
WINAPI
StorageAdapterCreateDatabase(
    __inout PWINBIO_PIPELINE Pipeline,
    __in PWINBIO_UUID DatabaseId,
    __in WINBIO_BIOMETRIC_TYPE Factor,
    __in PWINBIO_UUID Format,
    __in LPCWSTR FilePath,
    __in LPCWSTR ConnectString,
    __in SIZE_T IndexElementCount,
    __in SIZE_T InitialSize
    )
{
    
    // See the StorageAdapterCreateDatabase documentation for an implementation example.

    return S_OK;
}

/////////////////////////////////////////////////////////////////////////////////////////
//
// StorageAdapterEraseDatabase
//
// Purpose:
//      Erases the database and marks it for deletion.
//
static HRESULT
WINAPI
StorageAdapterEraseDatabase(
    __inout PWINBIO_PIPELINE Pipeline,
    __in PWINBIO_UUID DatabaseId,
    __in LPCWSTR FilePath,
    __in LPCWSTR ConnectString
   )
{
    
    // See the StorageAdapterEraseDatabase documentation for an implementation example.

    return S_OK;
}

/////////////////////////////////////////////////////////////////////////////////////////
//
// StorageAdapterOpenDatabase
//
// Purpose:
//      Opens the database.
//
static HRESULT
WINAPI
StorageAdapterOpenDatabase(
    __inout PWINBIO_PIPELINE Pipeline,
    __in PWINBIO_UUID DatabaseId,
    __in LPCWSTR FilePath,
    __in LPCWSTR ConnectString
    )
{
    
    // See the StorageAdapterOpenDatabase documentation for an implementation example.

    return S_OK;
}

/////////////////////////////////////////////////////////////////////////////////////////
//
// StorageAdapterCloseDatabase
//
// Purpose:
//      Close the database associated with the pipeline and free all 
//      related resources.
//
static HRESULT
WINAPI
StorageAdapterCloseDatabase(
    __inout PWINBIO_PIPELINE Pipeline
    )
{
    
    // See the StorageAdapterCloseDatabase documentation for an implementation example.

    return S_OK;
}

/////////////////////////////////////////////////////////////////////////////////////////
//
// StorageAdapterGetDataFormat
//
// Purpose:
//      Retrieves format and version information used by the current database 
//      associated with the pipeline.
//
static HRESULT
WINAPI
StorageAdapterGetDataFormat(
    __inout PWINBIO_PIPELINE Pipeline,
    __out PWINBIO_UUID Format,
    __out PWINBIO_VERSION Version
    )
{
    
    // See the StorageAdapterGetDataFormat documentation for an implementation example.

    return S_OK;
}

/////////////////////////////////////////////////////////////////////////////////////////
//
// StorageAdapterGetDatabaseSize
//
// Purpose:
//      Retrieves the database size and available space.
//
static HRESULT
WINAPI
StorageAdapterGetDatabaseSize(
    __inout PWINBIO_PIPELINE Pipeline,
    __out PSIZE_T AvailableRecordCount,
    __out PSIZE_T TotalRecordCount
    )
{
    
    // See the StorageAdapterGetDatabaseSize documentation for an implementation example.

    return S_OK;
}

/////////////////////////////////////////////////////////////////////////////////////////
//
// StorageAdapterAddRecord
//
// Purpose:
//      Adds a template to the database.
//
static HRESULT
WINAPI
StorageAdapterAddRecord(
    __inout PWINBIO_PIPELINE Pipeline,
    __in PWINBIO_STORAGE_RECORD RecordContents
    )
{
    
    // See the StorageAdapterAddRecord documentation for an implementation example.

    return S_OK;
}

/////////////////////////////////////////////////////////////////////////////////////////
//
// StorageAdapterDeleteRecord
//
// Purpose:
//      Deletes one or more templates from the database.
//
static HRESULT
WINAPI
StorageAdapterDeleteRecord(
    __inout PWINBIO_PIPELINE Pipeline,
    __in PWINBIO_IDENTITY Identity,
    __in WINBIO_BIOMETRIC_SUBTYPE SubFactor
    )
{
    
    // See the StorageAdapterDeleteRecord documentation for an implementation example.

    return S_OK;
}

/////////////////////////////////////////////////////////////////////////////////////////
//
// StorageAdapterQueryBySubject
//
// Purpose:
//      Locates templates that match a specified identity and sub-factor.
//
static HRESULT
WINAPI
StorageAdapterQueryBySubject(
    __inout PWINBIO_PIPELINE Pipeline,
    __in PWINBIO_IDENTITY Identity,
    __in WINBIO_BIOMETRIC_SUBTYPE SubFactor
    )
{
    
    // See the StorageAdapterQueryBySubject documentation for an implementation example.

    return S_OK;
}

/////////////////////////////////////////////////////////////////////////////////////////
//
// StorageAdapterQueryByContent
//
// Purpose:
//      Locates templates that match a specified index vector.
//
static HRESULT
WINAPI
StorageAdapterQueryByContent(
    __inout PWINBIO_PIPELINE Pipeline,
    __in WINBIO_BIOMETRIC_SUBTYPE SubFactor,
    __in ULONG IndexVector[],
    __in SIZE_T IndexElementCount
    )
{
    
    // See the StorageAdapterQueryByContent documentation for an implementation example.

    return S_OK;
}

/////////////////////////////////////////////////////////////////////////////////////////
//
// StorageAdapterGetRecordCount
//
// Purpose:
//      Retrieves the number of template records in the pipeline result set.
//
static HRESULT
WINAPI
StorageAdapterGetRecordCount(
    __inout PWINBIO_PIPELINE Pipeline,
    __out PSIZE_T RecordCount
    )
{
    
    // See the StorageAdapterGetRecordCount documentation for an implementation example.

    return S_OK;
}

/////////////////////////////////////////////////////////////////////////////////////////
//
// StorageAdapterFirstRecord
//
// Purpose:
//      Positions the result set cursor on the first record in the set.
//
static HRESULT
WINAPI
StorageAdapterFirstRecord(
    __inout PWINBIO_PIPELINE Pipeline
    )
{
    
    // See the StorageAdapterFirstRecord documentation for an implementation example.

    return S_OK;
}
/////////////////////////////////////////////////////////////////////////////////////////
//
// StorageAdapterNextRecord
//
// Purpose:
//      Advances the result set cursor by one record.
//
static HRESULT
WINAPI
StorageAdapterNextRecord(
    __inout PWINBIO_PIPELINE Pipeline
    )
{
    
    // See the StorageAdapterNextRecord documentation for an implementation example.

    return S_OK;
}

/////////////////////////////////////////////////////////////////////////////////////////
//
// StorageAdapterGetCurrentRecord
//
// Purpose:
//      Retrieves the contents of the current record in the pipeline result set.
//
static HRESULT
WINAPI
StorageAdapterGetCurrentRecord(
    __inout PWINBIO_PIPELINE Pipeline,
    __out PWINBIO_STORAGE_RECORD RecordContents
    )
{
    
    // See the StorageAdapterGetCurrentRecord documentation for an implementation example.

    return S_OK;
}

/////////////////////////////////////////////////////////////////////////////////////////
//
// StorageAdapterControlUnit
//
// Purpose:
//       Performs a vendor-defined control operation that does not require 
//       elevated privilege.
//
static HRESULT
WINAPI
StorageAdapterControlUnit(
    __inout PWINBIO_PIPELINE Pipeline,
    __in ULONG ControlCode,
    __in PUCHAR SendBuffer,
    __in SIZE_T SendBufferSize,
    __in PUCHAR ReceiveBuffer,
    __in SIZE_T ReceiveBufferSize,
    __out PSIZE_T ReceiveDataSize,
    __out PULONG OperationStatus
    )
{
    
    // See the StorageAdapterControlUnit documentation for an implementation example.

    return S_OK;
}

/////////////////////////////////////////////////////////////////////////////////////////
//
// StorageAdapterControlUnitPrivileged
//
// Purpose:
//      Performs a vendor-defined control operation that requires elevated privilege.
//
static HRESULT
WINAPI
StorageAdapterControlUnitPrivileged(
    __inout PWINBIO_PIPELINE Pipeline,
    __in ULONG ControlCode,
    __in PUCHAR SendBuffer,
    __in SIZE_T SendBufferSize,
    __in PUCHAR ReceiveBuffer,
    __in SIZE_T ReceiveBufferSize,
    __out PSIZE_T ReceiveDataSize,
    __out PULONG OperationStatus
    )
{
    
    // See the StorageAdapterControlUnitPrivileged documentation for an implementation example.

    return S_OK;
}

```



## Related topics

<dl> <dt>

[Creating Adapter Plug-ins](creating-adapter-plug-ins.md)
</dt> </dl>

 

 




