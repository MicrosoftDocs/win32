---
title: Creating an Engine Adapter
description: Basic structure of an engine adapter plug-in implemented as a C++ dynamic link library (DLL).
ms.assetid: d443ee2d-6b45-44ac-9d79-f71033d8b7f4
ms.topic: article
ms.date: 05/31/2018
---

# Creating an Engine Adapter

The following code example shows the basic structure of an engine adapter plug-in implemented as a C++ dynamic link library (DLL). To see pseudocode implementations of each public function in the DLL, go to [Engine Adapter Functions](engine-adapter-functions.md). If you choose to not provide functionality for a particular function, you must define a stub for it and return E\_NOTIMPL.


```C++
/*++
 
    THIS CODE AND INFORMATION IS PROVIDED "AS IS" WITHOUT WARRANTY OF
    ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING BUT NOT LIMITED TO
    THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS FOR A
    PARTICULAR PURPOSE.

    Copyright (C) Microsoft. All rights reserved.

Module Name:

    EngineAdapter.cpp

Abstract:

    This module contains a stub implementation of an Engine Adapter
    plug-in for the Windows Biometric service.


    -

Environment:

    Win32, user mode only.

Revision History:

NOTES:

    (None)

--*/

//////////////////////////////////////////////////////////////////////////////////////////
//
// Header files.
//
#include "Winbio_adapter.h"     // Public
#include "EngineAdapter.h"      // Private


//////////////////////////////////////////////////////////////////////////////////////////
//
// Forward declarations for the engine adapter interface routines.
//

static HRESULT
WINAPI
EngineAdapterAttach(
    __inout PWINBIO_PIPELINE Pipeline
    );

static HRESULT
WINAPI
EngineAdapterDetach(
    __inout PWINBIO_PIPELINE Pipeline
    );

static HRESULT
WINAPI
EngineAdapterClearContext(
    __inout PWINBIO_PIPELINE Pipeline
    );

static HRESULT
WINAPI
EngineAdapterEndOperation(
    __inout PWINBIO_PIPELINE Pipeline
    );

static HRESULT
WINAPI
EngineAdapterQueryPreferredFormat(
    __inout PWINBIO_PIPELINE Pipeline,
    __out PWINBIO_REGISTERED_FORMAT StandardFormat,
    __out PWINBIO_UUID VendorFormat
    );

static HRESULT
WINAPI
EngineAdapterQueryIndexVectorSize(
    __inout PWINBIO_PIPELINE Pipeline,
    __out PSIZE_T IndexElementCount
    );

static HRESULT
WINAPI
EngineAdapterQueryHashAlgorithms(
    __inout PWINBIO_PIPELINE Pipeline,
    __out PSIZE_T AlgorithmCount,
    __out PSIZE_T AlgorithmBufferSize,
    __out PUCHAR *AlgorithmBuffer
    );

static HRESULT
WINAPI
EngineAdapterSetHashAlgorithm(
    __inout PWINBIO_PIPELINE Pipeline,
    __in SIZE_T AlgorithmBufferSize,
    __in PUCHAR AlgorithmBuffer
    );

static HRESULT
WINAPI
EngineAdapterQuerySampleHint(
    __inout PWINBIO_PIPELINE Pipeline,
    __out PSIZE_T SampleHint
    );

static HRESULT
WINAPI
EngineAdapterAcceptSampleData(
    __inout PWINBIO_PIPELINE Pipeline,
    __in PWINBIO_BIR SampleBuffer,
    __in SIZE_T SampleSize,
    __in WINBIO_BIR_PURPOSE Purpose,
    __out PWINBIO_REJECT_DETAIL RejectDetail
    );

static HRESULT
WINAPI
EngineAdapterExportEngineData(
    __inout PWINBIO_PIPELINE Pipeline,
    __in WINBIO_BIR_DATA_FLAGS Flags,
    __out PWINBIO_BIR *SampleBuffer,
    __out PSIZE_T SampleSize
    );

static HRESULT
WINAPI
EngineAdapterVerifyFeatureSet(
    __inout PWINBIO_PIPELINE Pipeline,
    __in PWINBIO_IDENTITY Identity,
    __in WINBIO_BIOMETRIC_SUBTYPE SubFactor,
    __out PBOOLEAN Match,
    __out PUCHAR *PayloadBlob,
    __out PSIZE_T PayloadBlobSize,
    __out PUCHAR *HashValue,
    __out PSIZE_T HashSize,
    __out PWINBIO_REJECT_DETAIL RejectDetail
    );

static HRESULT
WINAPI
EngineAdapterIdentifyFeatureSet(
    __inout PWINBIO_PIPELINE Pipeline,
    __out PWINBIO_IDENTITY Identity,
    __out PWINBIO_BIOMETRIC_SUBTYPE SubFactor,
    __out PUCHAR *PayloadBlob,
    __out PSIZE_T PayloadBlobSize,
    __out PUCHAR *HashValue,
    __out PSIZE_T HashSize,
    __out PWINBIO_REJECT_DETAIL RejectDetail
    );

static HRESULT
WINAPI
EngineAdapterCreateEnrollment(
    __inout PWINBIO_PIPELINE Pipeline
    );

static HRESULT
WINAPI
EngineAdapterUpdateEnrollment(
    __inout PWINBIO_PIPELINE Pipeline,
    __out PWINBIO_REJECT_DETAIL RejectDetail
    );

static HRESULT
WINAPI
EngineAdapterGetEnrollmentStatus(
    __inout PWINBIO_PIPELINE Pipeline,
    __out PWINBIO_REJECT_DETAIL RejectDetail
    );

static HRESULT
WINAPI
EngineAdapterGetEnrollmentHash(
    __inout PWINBIO_PIPELINE Pipeline,
    __out PUCHAR *HashValue,
    __out PSIZE_T HashSize
    );

static HRESULT
WINAPI
EngineAdapterCheckForDuplicate(
    __inout PWINBIO_PIPELINE Pipeline,
    __out PWINBIO_IDENTITY Identity,
    __out PWINBIO_BIOMETRIC_SUBTYPE SubFactor,
    __out PBOOLEAN Duplicate
    );

static HRESULT
WINAPI
EngineAdapterCommitEnrollment(
    __inout PWINBIO_PIPELINE Pipeline,
    __in PWINBIO_IDENTITY Identity,
    __in WINBIO_BIOMETRIC_SUBTYPE SubFactor,
    __in PUCHAR PayloadBlob,
    __in SIZE_T PayloadBlobSize
    );

static HRESULT
WINAPI
EngineAdapterDiscardEnrollment(
    __inout PWINBIO_PIPELINE Pipeline
    );

static HRESULT
WINAPI
EngineAdapterControlUnit(
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
EngineAdapterControlUnitPrivileged(
    __inout PWINBIO_PIPELINE Pipeline,
    __in ULONG ControlCode,
    __in PUCHAR SendBuffer,
    __in SIZE_T SendBufferSize,
    __in PUCHAR ReceiveBuffer,
    __in SIZE_T ReceiveBufferSize,
    __out PSIZE_T ReceiveDataSize,
    __out PULONG OperationStatus
    );


//////////////////////////////////////////////////////////////////////////////////////////
//
// Interface dispatch table.
//
static WINBIO_ENGINE_INTERFACE g_EngineInterface = {
    WINBIO_ENGINE_INTERFACE_VERSION_1,
    WINBIO_ADAPTER_TYPE_ENGINE,
    sizeof(WINBIO_ENGINE_INTERFACE),
    {0xb876fdc8, 0x34e7, 0x471a, {0x82, 0xc8, 0x9c, 0xba, 0x6a, 0x35, 0x38, 0xec}},

    EngineAdapterAttach,
    EngineAdapterDetach,
    EngineAdapterClearContext,
    EngineAdapterQueryPreferredFormat,
    EngineAdapterQueryIndexVectorSize,
    EngineAdapterQueryHashAlgorithms,
    EngineAdapterSetHashAlgorithm,
    EngineAdapterQuerySampleHint,
    EngineAdapterAcceptSampleData,
    EngineAdapterExportEngineData,
    EngineAdapterVerifyFeatureSet,
    EngineAdapterIdentifyFeatureSet,
    EngineAdapterCreateEnrollment,
    EngineAdapterUpdateEnrollment,
    EngineAdapterGetEnrollmentStatus,
    EngineAdapterGetEnrollmentHash,
    EngineAdapterCheckForDuplicate,
    EngineAdapterCommitEnrollment,
    EngineAdapterDiscardEnrollment,
    EngineAdapterControlUnit,
    EngineAdapterControlUnitPrivileged
};


//////////////////////////////////////////////////////////////////////////////////////////
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


//////////////////////////////////////////////////////////////////////////////////////////
//
// Well known interface discovery function exported by the engine adapter.
//
WbioQueryEngineInterface(
    __out PWINBIO_ENGINE_INTERFACE *EngineInterface
    )
{
    *EngineInterface = &g_EngineInterface;
    return S_OK;
}
//////////////////////////////////////////////////////////////////////////////////////////
//
// Required routines.
//      This sample adapter assumes that the following three inline functions 
//      are declared in the private engine adapter header file. The first two
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

//////////////////////////////////////////////////////////////////////////////////////////
//
// EngineAdapterAttach
//
// Purpose:
//      Performs any initialization required for later biometric operations.
//
static HRESULT
WINAPI
EngineAdapterAttach(
    __inout PWINBIO_PIPELINE Pipeline
    )
{
    
    // See the EngineAdapterAttach documentation for an implementation example.

    return S_OK;
}

//////////////////////////////////////////////////////////////////////////////////////////
//
// EngineAdapterDetach
//
// Purpose:
//      Releases adapter specific resources attached to the pipeline.
//      
static HRESULT
WINAPI
EngineAdapterDetach(
    __inout PWINBIO_PIPELINE Pipeline
    )
{

    // See the EngineAdapterDetach documentation for an implementation example.

    return S_OK;
}


//////////////////////////////////////////////////////////////////////////////////////////
//
// EngineAdapterClearContext
//
// Purpose:
//      Prepares the processing pipeline of the biometric unit for a 
//      new operation.
//
static HRESULT
WINAPI
EngineAdapterClearContext(
    __inout PWINBIO_PIPELINE Pipeline
    )
{

    // See the EngineAdapterClearContext documentation for an implementation example.

    return S_OK;
}

//////////////////////////////////////////////////////////////////////////////////////////
//
// EngineAdapterQueryPreferredFormat
//
// Purpose:
//      Called by the sensor adapter on the biometric unit to determine the 
//      input data format preferred by the engine adapter.
//
static HRESULT
WINAPI
EngineAdapterQueryPreferredFormat(
    __inout PWINBIO_PIPELINE Pipeline,
    __out PWINBIO_REGISTERED_FORMAT StandardFormat,
    __out PWINBIO_UUID VendorFormat
    )
{

    // See the EngineAdapterQueryPreferredFormat documentation for an implementation example.

    return S_OK;
}


//////////////////////////////////////////////////////////////////////////////////////////
//
// EngineAdapterQueryIndexVectorSize
//
// Purpose:
//      Called by the Windows Biometric Framework to retrieve the size of 
//      the index vector used by the engine adapter.
//
static HRESULT
WINAPI
EngineAdapterQueryIndexVectorSize(
    __inout PWINBIO_PIPELINE Pipeline,
    __out PSIZE_T IndexElementCount
    )
{

    // See the EngineAdapterQueryIndexVectorSize documentation for an implementation example.

    return S_OK;
}


//////////////////////////////////////////////////////////////////////////////////////////
//
// EngineAdapterQueryHashAlgorithms
// 
//      Retrieves an array of object identifiers (OIDs) that represent the 
//      hash algorithms supported by the engine adapter.
//
static HRESULT
WINAPI
EngineAdapterQueryHashAlgorithms(
    __inout PWINBIO_PIPELINE Pipeline,
    __out PSIZE_T AlgorithmCount,
    __out PSIZE_T AlgorithmBufferSize,
    __out PUCHAR *AlgorithmBuffer
    )
{

    // See the EngineAdapterQueryHashAlgorithms documentation for an implementation example.

    return S_OK;
}


//////////////////////////////////////////////////////////////////////////////////////////
//
// EngineAdapterSetHashAlgorithm
//
// Purpose:
//      Selects a hash algorithm for use in subsequent operations.
//
static HRESULT
WINAPI
EngineAdapterSetHashAlgorithm(
    __inout PWINBIO_PIPELINE Pipeline,
    __in SIZE_T AlgorithmBufferSize,
    __in PUCHAR AlgorithmBuffer
    )
{

    // See the EngineAdapterSetHashAlgorithm documentation for an implementation example.

    return S_OK;
}


//////////////////////////////////////////////////////////////////////////////////////////
//
// EngineAdapterQuerySampleHint
//
// Purpose: 
//      Retrieves the number of correct samples required by the engine adapter 
//      to construct an enrollment template.
//
static HRESULT
WINAPI
EngineAdapterQuerySampleHint(
    __inout PWINBIO_PIPELINE Pipeline,
    __out PSIZE_T SampleHint
    )
{

    // See the EngineAdapterQuerySampleHint documentation for an implementation example.

    return S_OK;
}


//////////////////////////////////////////////////////////////////////////////////////////
//
// EngineAdapterAcceptSampleData
//
// Purpose:
//      Notifies the engine adapter to accept a raw biometric sample and 
//      extract a feature set.
//
static HRESULT
WINAPI
EngineAdapterAcceptSampleData(
    __inout PWINBIO_PIPELINE Pipeline,
    __in PWINBIO_BIR SampleBuffer,
    __in SIZE_T SampleSize,
    __in WINBIO_BIR_PURPOSE Purpose,
    __out PWINBIO_REJECT_DETAIL RejectDetail
    )
{

    // See the EngineAdapterAcceptSampleData documentation for an implementation example.

    return S_OK;
}

//////////////////////////////////////////////////////////////////////////////////////////
//
// EngineAdapterExportEngineData
//
// Purpose:
//      Retrieves a copy of the most recently processed feature set or template.
//

static HRESULT
WINAPI
EngineAdapterExportEngineData(
    __inout PWINBIO_PIPELINE Pipeline,
    __in WINBIO_BIR_DATA_FLAGS Flags,
    __out PWINBIO_BIR *SampleBuffer,
    __out PSIZE_T SampleSize
    )
{

    // See the EngineAdapterExportEngineData documentation for an implementation example.

    return S_OK;
}

//////////////////////////////////////////////////////////////////////////////////////////
//
// EngineAdapterVerifyFeatureSet
//
// Purpose:
//      Compares the template in the current feature set with a specific 
//      template in the database.
//      
static HRESULT
WINAPI
EngineAdapterVerifyFeatureSet(
    __inout PWINBIO_PIPELINE Pipeline,
    __in PWINBIO_IDENTITY Identity,
    __in WINBIO_BIOMETRIC_SUBTYPE SubFactor,
    __out PBOOLEAN Match,
    __out PUCHAR *PayloadBlob,
    __out PSIZE_T PayloadBlobSize,
    __out PUCHAR *HashValue,
    __out PSIZE_T HashSize,
    __out PWINBIO_REJECT_DETAIL RejectDetail
    )
{

    // See the EngineAdapterVerifyFeatureSet documentation for an implementation example.

    return S_OK;
}


//////////////////////////////////////////////////////////////////////////////////////////
//
// EngineAdapterIdentifyFeatureSet
//
// Purpose:
//      Build a template from the current feature set and locate a matching 
//      template in the database.
//
WINAPI
EngineAdapterIdentifyFeatureSet(
    __inout PWINBIO_PIPELINE Pipeline,
    __out PWINBIO_IDENTITY Identity,
    __out PWINBIO_BIOMETRIC_SUBTYPE SubFactor,
    __out PUCHAR *PayloadBlob,
    __out PSIZE_T PayloadBlobSize,
    __out PUCHAR *HashValue,
    __out PSIZE_T HashSize,
    __out PWINBIO_REJECT_DETAIL RejectDetail
    )
{

    // See the EngineAdapterIdentifyFeatureSet documentation for an implementation example.

    return S_OK;
}


//////////////////////////////////////////////////////////////////////////////////////////
//
// EngineAdapterCreateEnrollment
//
// Purpose:
//      Initialize the enrollment object in the biometric unit pipeline.
//
static HRESULT
WINAPI
EngineAdapterCreateEnrollment(
    __inout PWINBIO_PIPELINE Pipeline
    )
{

    // See the EngineAdapterCreateEnrollment documentation for an implementation example.

    return S_OK;
}


//////////////////////////////////////////////////////////////////////////////////////////
//
// EngineAdapterUpdateEnrollment
//
// Purpose:
//      Adds the current feature set to the enrollment object.
//
static HRESULT
WINAPI
EngineAdapterUpdateEnrollment(
    __inout PWINBIO_PIPELINE Pipeline,
    __out PWINBIO_REJECT_DETAIL RejectDetail
    )
{

    // See the EngineAdapterUpdateEnrollment documentation for an implementation example.

    return S_OK;
}


//////////////////////////////////////////////////////////////////////////////////////////
//
// EngineAdapterGetEnrollmentStatus
//
// Purpose:
//      Determines whether the enrollment object is ready to be committed to 
//      the pipeline.
//
static HRESULT
WINAPI
EngineAdapterGetEnrollmentStatus(
    __inout PWINBIO_PIPELINE Pipeline,
    __out PWINBIO_REJECT_DETAIL RejectDetail
    )
{

    // See the EngineAdapterGetEnrollmentStatus documentation for an implementation example.

    return S_OK;
}

//////////////////////////////////////////////////////////////////////////////////////////
//
// EngineAdapterGetEnrollmentHash
//
// Purpose:
//      Retrieves the hash of the completed enrollment template in the pipeline.
//
static HRESULT
WINAPI
EngineAdapterGetEnrollmentHash(
    __inout PWINBIO_PIPELINE Pipeline,
    __out PUCHAR *HashValue,
    __out PSIZE_T HashSize
    )
{

    // See the EngineAdapterGetEnrollmentHash documentation for an implementation example.

    return S_OK;
}


//////////////////////////////////////////////////////////////////////////////////////////
//
// EngineAdapterCheckForDuplicate
// 
// Purpose:
//      Determines whether a new template in the pipeline duplicates any 
//      template already saved in the database regardless of the identity 
//      associated with the templates.
//
static HRESULT
WINAPI
EngineAdapterCheckForDuplicate(
    __inout PWINBIO_PIPELINE Pipeline,
    __out PWINBIO_IDENTITY Identity,
    __out PWINBIO_BIOMETRIC_SUBTYPE SubFactor,
    __out PBOOLEAN Duplicate
    )
{

    // See the EngineAdapterCheckForDuplicate documentation for an implementation example.

    return S_OK;
}

//////////////////////////////////////////////////////////////////////////////////////////
//
// EngineAdapterCommitEnrollment
//
// Purpose:
//      Finalizes the enrollment object, converts it to a template, and saves 
//      the template in the database.
//
static HRESULT
WINAPI
EngineAdapterCommitEnrollment(
    __inout PWINBIO_PIPELINE Pipeline,
    __in PWINBIO_IDENTITY Identity,
    __in WINBIO_BIOMETRIC_SUBTYPE SubFactor,
    __in PUCHAR PayloadBlob,
    __in SIZE_T PayloadBlobSize
    )
{

    // See the EngineAdapterCommitEnrollment documentation for an implementation example.

    return S_OK;
}


//////////////////////////////////////////////////////////////////////////////////////////
//
// EngineAdapterDiscardEnrollment
//
// Purpose:
//      Deletes intermediate enrollment state information from the pipeline.
//
static HRESULT
WINAPI
EngineAdapterDiscardEnrollment(
    __inout PWINBIO_PIPELINE Pipeline
    )
{

    // See the EngineAdapterDiscardEnrollment documentation for an implementation example.

    return S_OK;
}


//////////////////////////////////////////////////////////////////////////////////////////
//
// EngineAdapterControlUnit
//
// Purpose:
//      Performs a vendor-defined control operation that does not require 
//      elevated privilege.
//
static HRESULT
WINAPI
EngineAdapterControlUnit(
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


//////////////////////////////////////////////////////////////////////////////////////////
//
// EngineAdapterControlUnitPrivileged
//
// Purpose:
//      Performs a vendor-defined control operation that requires elevated 
//      privilege.
//
static HRESULT
WINAPI
EngineAdapterControlUnitPrivileged(
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

    // See the EngineAdapterControlUnitPrivileged documentation for an implementation example.

    return S_OK;
}

```



## Related topics

<dl> <dt>

[Creating Adapter Plug-ins](creating-adapter-plug-ins.md)
</dt> </dl>

 

 




