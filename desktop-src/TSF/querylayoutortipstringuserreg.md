---
title: QueryLayoutOrTipStringUserReg function
description: Queries the specified string which represents the format of a keyboard layout list or text services profile list of the specified registry path.
ms.assetid: b7b42fda-5a65-483a-b3f3-85157bb1a667
keywords:
- QueryLayoutOrTipStringUserReg function Text Services Framework
topic_type:
- apiref
api_name:
- QueryLayoutOrTipStringUserReg
api_location:
- input.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# QueryLayoutOrTipStringUserReg function

Queries the specified string which represents the format of a keyboard layout list or text services profile list of the specified registry path.

## Syntax


```C++
HRESULT CALLBACK QueryLayoutOrTipStringUserReg(
  _In_ LPCWSTR pszUserReg,
  _In_ LPCWSTR pszSystemReg,
  _In_ LPCWSTR pszSoftwareReg,
  _In_ LPCWSTR psz,
  _In_ DWORD   dwFlags
);
```



## Parameters

<dl> <dt>

*pszUserReg* \[in\]
</dt> <dd>

The registry path of the user. If this parameter is **NULL**, HKEY\_CURRENT\_USER is used.

</dd> <dt>

*pszSystemReg* \[in\]
</dt> <dd>

The registry path of the system. If this parameter is **NULL**, HKEY\_LOCAL\_MACHINE\\System is used.

</dd> <dt>

*pszSoftwareReg* \[in\]
</dt> <dd>

The registry path of the software. If this parameter is **NULL**, HKEY\_LOCAL\_MACHINE\\Software is used.

</dd> <dt>

*psz* \[in\]
</dt> <dd>

A string that represents a keyboard layout list or a text services profile list.

</dd> <dt>

*dwFlags* \[in\]
</dt> <dd>

This must be 0.

</dd> </dl>

## Return value

This function can return one of these values.



| Return code                                                                                  | Description                                                                       |
|----------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>         | All layouts or profiles defined in **psz** are valid.<br/>                  |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl> | One or more of the layouts or profiles defined in **psz** are invalid.<br/> |



 

## Remarks

There is no import library available that defines this function, so it is necessary to obtain a pointer to this function using [**LoadLibrary**](/windows/desktop/api/libloaderapi/nf-libloaderapi-loadlibrarya) and [**GetProcAddress**](/windows/desktop/api/libloaderapi/nf-libloaderapi-getprocaddress).

> [!Note]  
> Using [**LoadLibrary**](/windows/desktop/api/libloaderapi/nf-libloaderapi-loadlibrarya) incorrectly can compromise the security of your application by loading the wrong DLL. Refer to [Dynamic-Link Library Search Order](/windows/desktop/Dlls/dynamic-link-library-search-order) for information on how to correctly load DLLs with different versions of Microsoft Windows.

 

The string format of the layout list is:

<LangID 1>:<KLID 1>;\[...<LangID N>:<KLID N>

The string format of the text service profile list is:

<LangID 1>:{xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx}{xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx};

The following is an example of a value for the *psz* parameter:

``` syntax
"0x0407:0x00000407"
"0x0407:0x00000407;0x040C:0x0000040C"
"0x0407:0x00000407;0x0412:{A028AE76-01B1-46C2-99C4-ACD9858AE02F}{B5FE1F02-D5F2-4445-9C03-C568F23C99A1};0x040C:0x0000040C"
```

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                 |
| DLL<br/>                      | <dl> <dt>Input.dll</dt> </dl> |



 

