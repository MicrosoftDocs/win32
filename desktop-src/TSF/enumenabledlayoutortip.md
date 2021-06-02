---
title: EnumEnabledLayoutOrTip function
description: Enumerates all enabled keyboard layouts or text services of the specified user setting.
ms.assetid: b3c57e88-e04b-411b-9eba-83258da16773
keywords:
- EnumEnabledLayoutOrTip function Text Services Framework
topic_type:
- apiref
api_name:
- EnumEnabledLayoutOrTip
api_location:
- input.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# EnumEnabledLayoutOrTip function

Enumerates all enabled keyboard layouts or text services of the specified user setting.

## Syntax


```C++
UINT EnumEnabledLayoutOrTip(
  _In_opt_ LPCWSTR            pszUserReg,
  _In_opt_ LPCWSTR            pszSystemReg,
  _In_opt_ LPCWSTR            pszSoftwareReg,
  _Out_    LAYOUTORTIPPROFILE *pLayoutOrTipProfile,
  _In_     UINT               uBufLength
);
```



## Parameters

<dl> <dt>

*pszUserReg* \[in, optional\]
</dt> <dd>

The registry path of the user. If this parameter is **NULL**, HKEY\_CURRENT\_USER is used.

</dd> <dt>

*pszSystemReg* \[in, optional\]
</dt> <dd>

The registry path of the system. If this parameter is **NULL**, HKEY\_LOCAL\_MACHINE\\System is used.

</dd> <dt>

*pszSoftwareReg* \[in, optional\]
</dt> <dd>

The registry path of the software. If this parameter is **NULL**, HKEY\_LOCAL\_MACHINE\\Software is used.

</dd> <dt>

*pLayoutOrTipProfile* \[out\]
</dt> <dd>

Pointer to the buffer that receives the LAYOUTORTIPPROFILE array.

</dd> <dt>

*uBufLength* \[in\]
</dt> <dd>

The length of the buffer pointed to by *pLayoutOrTipProfile*.

</dd> </dl>

## Return value

If *pLayoutOrTipProfile* is **NULL**, the number of keyboard items that are enabled in the user setting; otherwise, the number of keyboard items that are copied into *pLayoutOrTipProfile*.

For Input Method Editor (IME) languages, all IMEs are returned, even when only one IME is enabled. For example, if a user has the CHT New Quick IME enabled, the **EnumEnabledLayoutOrTip** function returns all 5 CHT IMEs.

## Remarks

There is no import library available that defines this function, so it is necessary to obtain a pointer to this function using [**LoadLibrary**](/windows/desktop/api/libloaderapi/nf-libloaderapi-loadlibrarya) and [**GetProcAddress**](/windows/desktop/api/libloaderapi/nf-libloaderapi-getprocaddress).

> [!Note]  
> Using [**LoadLibrary**](/windows/desktop/api/libloaderapi/nf-libloaderapi-loadlibrarya) incorrectly can compromise the security of your application by loading the wrong DLL. Refer to [Dynamic-Link Library Search Order](/windows/desktop/Dlls/dynamic-link-library-search-order) for information on how to correctly load DLLs with different versions of Microsoft Windows.

 

The definition of LAYOUTORTIPPROFILE is:

``` syntax
typedef struct tagLAYOUTORTIPPROFILE {
    DWORD  dwProfileType;       // InputProcessor or HKL 
#define LOTP_INPUTPROCESSOR 1
#define LOTP_KEYBOARDLAYOUT 2
    LANGID langid;              // language id 
    CLSID  clsid;               // CLSID of tip 
    GUID   guidProfile;         // profile description 
    GUID   catid;               // category of tip 
    DWORD  dwSubstituteLayout;  // substitute hkl 
    DWORD  dwFlags;             // Flags 
    WCHAR  szId[MAX_PATH];      // KLID or TIP profile for string 
} LAYOUTORTIPPROFILE;
```

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                 |
| DLL<br/>                      | <dl> <dt>Input.dll</dt> </dl> |



 

