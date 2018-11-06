---
title: SHV Module
description: Note  The Network Access Protection platform is not available starting with Windows 10 Sets up a system health validator (SHV) module including registration and unregistration with the NAP system.
ms.assetid: 0f2edd23-d44a-4a01-ae33-f7eef0e4b27f
ms.topic: article
ms.date: 05/31/2018
---

# SHV Module

> [!Note]  
> The Network Access Protection platform is not available starting with Windows 10

 

Sets up a system health validator (SHV) module including registration and unregistration with the NAP system.

> [!Note]  
> The NAP SDK also contains a full set of sample code that can be found in the ...\\Samples\\NetDS\\NAP... directory of your SDK installation. This sample set includes a system health agent (SHA), SHV, and enforcement client (EC). It has full working NAP scenarios setting up communication between SHA-SHV and SHA-EC.

 


```C++
#include <windows.h>
#include "stdafx.h"
#include "NapUtil.h"

static const wchar_t friendlyName[] = L"SDK SHV Sample";
static const wchar_t version[] = L"1.0.0.1";
static const wchar_t description[] = L"System Health Validator(SHV)";
static const wchar_t vendor[] = L"Microsoft";

/// Registers the SDK SHV with the NAP Server.
HRESULT RegisterSdkShv()
{
    HRESULT hr = S_OK;
    CComPtr<INapServerManagement> pSHVMgmt = NULL;
    
    NapComponentRegistrationInfo shvInfo;
    ZeroMemory (&shvInfo, sizeof(shvInfo));

    hr = pSHVMgmt.CoCreateInstance(CLSID_NapServerManagement, NULL, CLSCTX_INPROC_SERVER);
    hr = FillShvComponentRegistrationInfo(&shvInfo);
    hr = pSHVMgmt->RegisterSystemHealthValidator(&shvInfo, (CLSID *)&__uuidof(CSampleShv));
    
    FreeComponentRegistration(&shvInfo);
    return hr;
}

/// Unregisters the SDK SHV with the NAP Server.
HRESULT UnregisterSdkShv()
{
    HRESULT hr = S_OK;
    CComPtr<INapServerManagement> pSHVMgmt = NULL;

    hr = pSHVMgmt.CoCreateInstance(CLSID_NapServerManagement, NULL, CLSCTX_INPROC_SERVER);
    hr = pSHVMgmt->UnregisterSystemHealthValidator(QuarSampleSystemHealthId);
    return hr;
}

/// Fill the NapComponentRegistrationInfo structure that needs to be passed during registration.
HRESULT FillShvComponentRegistrationInfo (NapComponentRegistrationInfo *shvInfo)
{
    HRESULT hr = S_OK;
    shvInfo->id = QuarSampleSystemHealthId;

    //<Temporarily till implement the Info Class>
    shvInfo->infoClsid = GUID_NULL; 

    hr = ConstructCountedString(friendlyName, sizeof(friendlyName), &(shvInfo->friendlyName));
    hr = ConstructCountedString(description, sizeof(description), &(shvInfo->description));
    hr = ConstructCountedString(version, sizeof(version), &(shvInfo->version));
    hr = ConstructCountedString(vendor, sizeof(vendor), &(shvInfo->vendorName));
    return hr;
}

// Helper Function for FillShvComponentRegistrationInfo.
HRESULT ConstructCountedString(const WCHAR* src, UINT16 len, CountedString* dest)
{
    HRESULT hr = S_OK;
    DWORD retCode = ERROR_SUCCESS;
    hr = AllocateMemory(dest->string, ((len+1)*sizeof(WCHAR)));
    dest->length = len;
    retCode = StringCchCopy(dest->string, len+1, src);
    return hr;
}

// Helper Function for releasing ShaComponentRegistrationInfo members
void FreeComponentRegistration(NapComponentRegistrationInfo *shvInfo)
{
    FreeMemory(shvInfo->friendlyName.string);
    FreeMemory(shvInfo->description.string);
    FreeMemory(shvInfo->version.string);
    FreeMemory(shvInfo->vendorName.string);
}

```



 

 




