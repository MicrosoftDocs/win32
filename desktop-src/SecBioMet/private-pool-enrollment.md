---
title: Private Pool Enrollment
description: Contains the enrollment console project.
ms.assetid: 666CD6FF-A6A2-4992-81EB-F520C8FE5D95
ms.topic: article
ms.date: 05/31/2018
---

# Private Pool Enrollment

The following sections contain the code necessary for private sensor pool enrollment.

-   [Targetver.h](#targetverh)
-   [Stdafx.h](#stdafxh)
-   [PrivatePoolEnroll.cpp](#privatepoolenrollcpp)

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



## PrivatePoolEnroll.cpp


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

// PrivatePoolEnroll.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include "PrivatePoolCommonDefs.h"   // From Private Pool Setup
#include "Strsafe.h"                 // For StringCbGets()


//
// Forward declarations of local functions...
//
static void onEnrollOrPractice(
    __in bool CommitEnrollment
    );

static bool selectSensorMenu(
    __in LPCTSTR Prompt,
    __in WINBIO_UNIT_SCHEMA *UnitArray,
    __in SIZE_T UnitCount,
    __out SIZE_T *SelectedUnit
    );

static bool selectSubFactorMenu(
    __out PWINBIO_BIOMETRIC_SUBTYPE SubFactor
    );

static bool getUlongValue(
    __out PULONG Value
    );

static void displayIdentity(
    __in PWINBIO_IDENTITY Identity,
    __in WINBIO_BIOMETRIC_SUBTYPE SubFactor
    );
//-----------------------------------------------------------------------------

int _tmain(int argc, _TCHAR* argv[])
{
    _tprintf( _T("\nWinBio Private Pool Enrollment\n\n"));

    if (argc < 2)
    {
        _tprintf(_T("Usage: %s -enroll | -practice\n"), argv[0]);
        _tprintf(
            _T("\n")
            _T("  -enroll       create enrollment for a new finger\n")
            _T("  -practice     perform enrollment, but discard results\n")
            _T("\n")
            );
    }
    else
    {
        if (_tcsicmp( argv[1], _T("-enroll")) == 0)
        {
            onEnrollOrPractice(true);
        }
        else if (_tcsicmp( argv[1], _T("-practice")) == 0)
        {
            onEnrollOrPractice(false);
        }
        else
        {
            _tprintf(_T("*** Error - Unknown command option: %s\n"), argv[1]);
        }
    }

    return 0;
}
//-----------------------------------------------------------------------------

static void onEnrollOrPractice(
    __in bool CommitEnrollment
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
            // Build the array of Unit IDs that will make
            // up the private pool
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
            WINBIO_BIOMETRIC_SUBTYPE subFactor = WINBIO_SUBTYPE_NO_INFORMATION;
            if (selectSubFactorMenu( &subFactor ) &&
                subFactor != WINBIO_SUBTYPE_NO_INFORMATION &&
                subFactor != WINBIO_SUBTYPE_ANY)
            {
                //
                // Locate sensor
                //
                _tprintf(_T("\nTap the sensor once when you're ready to begin enrolling...\n\n"));
                WINBIO_UNIT_ID unitId = 0;
                hr = WinBioLocateSensor( sessionHandle, &unitId);
                if (SUCCEEDED(hr))
                {
                    //
                    // Enroll begin
                    //
                    _tprintf(_T("\n(Begining enrollment sequence)\n\n"));
                    hr = WinBioEnrollBegin(
                            sessionHandle,
                            subFactor,
                            unitId
                            );
                    if (SUCCEEDED(hr))
                    {
                        SIZE_T swipeCount = 0;
                        for (swipeCount = 1;; ++swipeCount)
                        {
                            _tprintf(
                                _T("Swipe your finger on the sensor to capture %s sample.\n"),
                                (swipeCount == 1)?_T("the first"):_T("another")
                                );

                            WINBIO_REJECT_DETAIL rejectDetail = 0;
                            hr = WinBioEnrollCapture(
                                    sessionHandle,
                                    &rejectDetail
                                    );
                            _tprintf(_T("   Sample %d captured from unit number %d.\n"), swipeCount, unitId);
                            if (hr == WINBIO_I_MORE_DATA)
                            {
                                _tprintf(_T("   More data required.\n\n"));
                                continue;
                            }
                            if (FAILED(hr))
                            {
                                if (hr == WINBIO_E_BAD_CAPTURE)
                                {
                                    _tprintf(_T("*** Error - Bad capture.\n"));
                                    _tprintf(
                                        _T("- %s\n"), 
                                        BioHelper::ConvertRejectDetailToString( rejectDetail )
                                        );
                                    hr = S_OK;
                                    continue;
                                }
                                else
                                {
                                    break;
                                }
                            }
                            else
                            {
                                _tprintf(_T("   Template completed.\n\n"));
                                break;
                            }
                        }
                        _tprintf(_T("\n"));
                        if (SUCCEEDED(hr))
                        {
                            if (CommitEnrollment)
                            {
                                // ENROLL
                                WINBIO_IDENTITY identity = {};
                                BOOLEAN isNewTemplate = FALSE;

                                _tprintf(_T("Committing enrollment...\n"));
                                hr = WinBioEnrollCommit( sessionHandle, &identity, &isNewTemplate);
                                if (SUCCEEDED(hr))
                                {
                                    _tprintf(_T("Enrollment committed to database\n"));
                                    displayIdentity( &identity, subFactor );
                                }
                            }
                            else
                            {
                                // PRACTICE
                                _tprintf(_T("Discarding enrollment...\n"));
                                hr = WinBioEnrollDiscard( sessionHandle );
                                if (SUCCEEDED(hr))
                                {
                                    _tprintf(_T("Template discarded.\n"));
                                }
                            }
                        }
                    }
                }
            }
            else
            {
                hr = E_INVALIDARG;
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

static bool selectSubFactorMenu(
    __out PWINBIO_BIOMETRIC_SUBTYPE SubFactor
    )
{
    static const WINBIO_BIOMETRIC_SUBTYPE subFactors[] = {
        WINBIO_ANSI_381_POS_RH_THUMB,
        WINBIO_ANSI_381_POS_RH_INDEX_FINGER,
        WINBIO_ANSI_381_POS_RH_MIDDLE_FINGER,
        WINBIO_ANSI_381_POS_RH_RING_FINGER,
        WINBIO_ANSI_381_POS_RH_LITTLE_FINGER,
        WINBIO_ANSI_381_POS_LH_THUMB,
        WINBIO_ANSI_381_POS_LH_INDEX_FINGER,
        WINBIO_ANSI_381_POS_LH_MIDDLE_FINGER,
        WINBIO_ANSI_381_POS_LH_RING_FINGER,
        WINBIO_ANSI_381_POS_LH_LITTLE_FINGER,
    };
    _tprintf(_T("\n- Select a sub-factor:\n\n"));

    for (SIZE_T index = 0; index < ARRAYSIZE(subFactors); ++index)
    {
        _tprintf(
            _T("    %2d - %s\n"),
            (index + 1),
            BioHelper::ConvertSubFactorToString( subFactors[index] )
            );
    }

    ULONG chosen = 0;
    if (getUlongValue( &chosen ) &&
        (chosen - 1) < ARRAYSIZE(subFactors))
    {
        *SubFactor = subFactors[chosen - 1];
        return true;
    }
    return false;
}
//-----------------------------------------------------------------------------

static bool getUlongValue(
    __out PULONG Value
    )
{
    ULONG value = 0;

    _tprintf( _T("\n- Enter a number: "));
    if (_tscanf_s(_T("%u"), &value) != 0)
    {
        *Value = value;
        return true;
    }
    return false;
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
        // invalid type
        break;
    }
    _tprintf(
        _T("    Subfactor:  %s\n"), 
        BioHelper::ConvertSubFactorToString(SubFactor)
        );
}
//-----------------------------------------------------------------------------
```



 

 




