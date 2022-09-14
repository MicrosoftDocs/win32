---
title: Private Pool Identity
description: Contains the identification console project.
ms.assetid: 1A96A20D-6991-4D8D-B7EC-7AF84B550920
ms.topic: article
ms.date: 05/31/2018
---

# Private Pool Identity

The following sections contain the code necessary for private sensor pool identification.

-   [Targetver.h](#targetverh)
-   [Stdafx.h](#stdafxh)
-   [PrivatePoolIdentify.cpp](#privatepoolidentifycpp)

## Targetver.h

This sample was created for Windows 7 and later operating systems.


```C++
#pragma once
#ifndef _WIN32_WINNT            
#define _WIN32_WINNT NTDDI_WIN7 
#endif
```



## Stdafx.h


```C++
// stdafx.h : include file for standard system include files,
// or project specific include files that are used frequently but
// are changed infrequently
//

#pragma once

#include "targetver.h"

// Use secure (template) versions of nonsecure 
// CRT text routines
#define _CRT_SECURE_CPP_OVERLOAD_STANDARD_NAMES     1

#include <stdio.h>
#include <tchar.h>

#include <windows.h>
#include <winbio.h>

#include "BioHelper.h"

#ifndef ARGUMENT_PRESENT
#define ARGUMENT_PRESENT(x) (((x) != NULL))
#endif
```



## PrivatePoolIdentify.cpp


```C++
/******************************************************************************
THIS CODE AND INFORMATION IS PROVIDED "AS IS" WITHOUT WARRANTY OF
ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING BUT NOT LIMITED
TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS FOR A
PARTICULAR PURPOSE.

Copyright (C) Microsoft.  All rights reserved.

This source code is only intended as a supplement to Microsoft Development
Tools and/or WinHelp documentation.  See these sources for detailed information
regarding the Microsoft samples programs.
******************************************************************************/

// PrivatePoolIdentify.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include "PrivatePoolCommonDefs.h" // From Private Pool Setup
#include "Strsafe.h"               // For StringCbGets()


// Forward declarations of local functions...
//
static void onIdentifyOrDelete(
    __in bool DeleteEnrollment
    );

static bool selectSensorMenu(
    __in LPCTSTR Prompt,
    __in WINBIO_UNIT_SCHEMA *UnitArray,
    __in SIZE_T UnitCount,
    __out SIZE_T *SelectedUnit
    );

static void displayIdentity(
    __in PWINBIO_IDENTITY Identity,
    __in WINBIO_BIOMETRIC_SUBTYPE SubFactor
    );

//-----------------------------------------------------------------------------

int _tmain(int argc, _TCHAR* argv[])
{
    _tprintf( _T("\nWinBio Private Pool Identification\n\n"));

    if (argc < 2)
    {
        _tprintf(_T("Usage: %s -identify | -delete\n"), argv[0]);
        _tprintf(
            _T("\n")
            _T("  -identify     locate template that matches a finger swipe\n")
            _T("  -delete       locate matching template and delete it\n")
            _T("\n")
            );
    }
    else
    {
        if (_tcsicmp( argv[1], _T("-identify")) == 0)
        {
            onIdentifyOrDelete(false);
        }
        else if (_tcsicmp( argv[1], _T("-delete")) == 0)
        {
            onIdentifyOrDelete(true);
        }
        else
        {
            _tprintf(_T("*** Error - Unknown command option: %s\n"), argv[1]);
        }
    }

    return 0;
}

//-----------------------------------------------------------------------------

static void onIdentifyOrDelete(
    __in bool DeleteEnrollment
    )
{
    WINBIO_UNIT_ID unitIdArray[1] = {};
    SIZE_T unitIdCount = ARRAYSIZE(unitIdArray);

    WINBIO_UNIT_SCHEMA *unitSchemaArray = NULL;
    SIZE_T unitSchemaCount = 0;
    HRESULT hr = WinBioEnumBiometricUnits( 
                    WINBIO_TYPE_FINGERPRINT, 
                    &unitSchemaArray, 
                    &unitSchemaCount 
                    );
    if (SUCCEEDED(hr))
    {
        SIZE_T selectedUnit = 0;
        if (selectSensorMenu( 
                _T("Choose a sensor for the private pool"), 
                unitSchemaArray, 
                unitSchemaCount, 
                &selectedUnit
                ))
        {
            // Build the array of unit IDs that will make up the private pool
            unitIdArray[0] = unitSchemaArray[selectedUnit].UnitId;
            unitIdCount = 1;
        }
        else
        {
            hr = E_INVALIDARG;
        }
        WinBioFree( unitSchemaArray );
        unitSchemaArray = NULL;
        unitSchemaCount = 0;
    }
    if (SUCCEEDED(hr))
    {
        WINBIO_UUID privateDatabaseId = PRIVATE_POOL_DATABASE_ID;
        WINBIO_SESSION_HANDLE sessionHandle = NULL;
        hr = WinBioOpenSession( 
                WINBIO_TYPE_FINGERPRINT, 
                WINBIO_POOL_PRIVATE, 
                WINBIO_FLAG_BASIC, 
                unitIdArray, 
                unitIdCount, 
                &privateDatabaseId, 
                &sessionHandle 
                );
        if (SUCCEEDED(hr))
        {
            _tprintf(_T("\nIdentify yourself by swiping your finger on the sensor...\n"));

            WINBIO_UNIT_ID unitId = 0;
            WINBIO_REJECT_DETAIL rejectDetail = 0;
            WINBIO_BIOMETRIC_SUBTYPE subFactor = WINBIO_SUBTYPE_NO_INFORMATION;
            WINBIO_IDENTITY identity = {};

            hr = WinBioIdentify( 
                    sessionHandle, 
                    &unitId, 
                    &identity, 
                    &subFactor, 
                    &rejectDetail
                    );
            _tprintf(_T("\n- Swipe processed - Unit ID: %d\n"), unitId);
            if (FAILED(hr))
            {
                if (hr == WINBIO_E_UNKNOWN_ID)
                {
                    _tprintf(_T("\n- Unknown identity.\n"));
                    hr = S_OK;
                }
                else if (hr == WINBIO_E_BAD_CAPTURE)
                {
                    _tprintf(_T("\n- Bad capture.\n"));
                    _tprintf(
                        _T("- %s\n"), 
                        BioHelper::ConvertRejectDetailToString( rejectDetail )
                        );
                    hr = S_OK;
                }
            }
            else
            {
                // Display identity
                displayIdentity( &identity, subFactor );

                // Delete identity
                if (DeleteEnrollment)
                {
                    _tprintf(_T("\nDeleting template...\n"));
                    hr = WinBioDeleteTemplate( 
                            sessionHandle, 
                            unitId, 
                            &identity, 
                            subFactor 
                            );
                    if (SUCCEEDED(hr))
                    {
                        _tprintf(_T("\n- Template removed from private database.\n"));
                    }
                }
            }
            WinBioCloseSession( sessionHandle );
            sessionHandle = NULL;
        }
    }

    if (FAILED(hr))
    {
        LPTSTR errorMessage = BioHelper::ConvertErrorCodeToString( hr );
        _tprintf(_T("*** Error - %s\n"), errorMessage );
        LocalFree(errorMessage);
        errorMessage = NULL;
    }
}

//-----------------------------------------------------------------------------

static bool selectSensorMenu(
    __in LPCTSTR Prompt,
    __in WINBIO_UNIT_SCHEMA *UnitArray,
    __in SIZE_T UnitCount,
    __out SIZE_T *SelectedUnit
    )
{
    if (!ARGUMENT_PRESENT(UnitArray) ||
        !ARGUMENT_PRESENT(SelectedUnit) ||
        UnitCount == 0)
    {
        return false;
    }

    _tprintf(_T("\n%s:\n\n"), Prompt);
    for (SIZE_T i = 0; i < UnitCount; ++i)
    {
        _tprintf(
            _T(" %3d - %ls (%ls)\n"), 
            (i + 1), 
            UnitArray[i].Manufacturer, 
            UnitArray[i].Description 
            );
    }

    _tprintf(_T("\nSelect sensor and press <ENTER>: "));
    TCHAR buffer[20] = {};
    HRESULT hr = StringCbGets( buffer, 20*sizeof(TCHAR) );
    _tprintf(_T("\n"));

    int selected = _tstoi( buffer );
    if (selected <= 0 ||
        selected > (int)UnitCount)
    {
        return false;
    }
    *SelectedUnit = (SIZE_T)(selected - 1);
    return true;
}

//-----------------------------------------------------------------------------

static void displayIdentity(
    __in PWINBIO_IDENTITY Identity,
    __in WINBIO_BIOMETRIC_SUBTYPE SubFactor
    )
{
    _tprintf(_T("\n- Identity: "));
    switch (Identity->Type)
    {
    case WINBIO_ID_TYPE_NULL:
        _tprintf(_T("NULL value\n"));
        break;

    case WINBIO_ID_TYPE_WILDCARD:
        _tprintf(_T("WILDCARD value\n"));
        if (Identity->Value.Wildcard != WINBIO_IDENTITY_WILDCARD)
        {
            _tprintf(
                _T("\n*** Error: Invalid wildcard marker (0x%08x)\n"), 
                Identity->Value.Wildcard
                );
        }
        break;

    case WINBIO_ID_TYPE_GUID:
        _tprintf(_T("GUID\n"));
        _tprintf(
            _T("    Value:      {%08X-%04X-%04X-%02X%02X-%02X%02X%02X%02X%02X%02X}\n"),
            Identity->Value.TemplateGuid.Data1,
            Identity->Value.TemplateGuid.Data2,
            Identity->Value.TemplateGuid.Data3,
            Identity->Value.TemplateGuid.Data4[0],
            Identity->Value.TemplateGuid.Data4[1],
            Identity->Value.TemplateGuid.Data4[2],
            Identity->Value.TemplateGuid.Data4[3],
            Identity->Value.TemplateGuid.Data4[4],
            Identity->Value.TemplateGuid.Data4[5],
            Identity->Value.TemplateGuid.Data4[6],
            Identity->Value.TemplateGuid.Data4[7]
            );
        break;

    default:
        _tprintf(_T("(Invalid type)\n"));
        break;
    }
    _tprintf(
        _T("    Subfactor:  %s\n"), 
        BioHelper::ConvertSubFactorToString(SubFactor)
        );
}

//-----------------------------------------------------------------------------
```



 

 




