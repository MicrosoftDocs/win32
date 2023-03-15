---
title: GetCurrentPackageInfo3
description: Retrieves the package graph's current generation ID.
ms.topic: reference
ms.date: 05/03/2022
req.lib: 
req.dll: Kernel32.dll
topic_type:
- APIRef
- kbSyntax
api_type:
- DllExport
api_location:
- Kernel32.dll
api_name:
- GetCurrentPackageInfo3
targetos: Windows
ms.localizationpriority: low
---

# GetCurrentPackageInfo3 function (appmodel.h)

Retrieves the package graph's current generation ID.

See **Remarks** for info about how to call the function.

## Syntax

```cpp
HRESULT GetCurrentPackageInfo3(
  _In_ UINT32                                 flags,
  _In_ PackageInfo3Type                       packageInfoType,
  _Inout_ UINT32                             *bufferLength,
  _Out_writes_bytes_opt_(*bufferLength) void *buffer,
  _Out_opt_ UINT32                           *count
);
```

## Parameters

`flags`

Type: **const UINT32**

The [package constants](/windows/desktop/appxpkg/package-constants) that specify how package information is retrieved. The **PACKAGE_FILTER_\*** flags are supported.

`packageInfoType`

Type: **PackageInfo3Type**

```cpp
enum PackageInfo3Type
{
	PackageInfo3Type_PackageInfoGeneration = 16,
} PackageInfoType;
```

Declare **PackageInfo3Type** as shown above, and pass **PackageInfo3Type::PackageInfo3Type_PackageInfoGeneration**.

`bufferLength`

Type: **UINT32\***

On input, the size of <i>buffer</i>, in bytes. On output, the size of the array of structures returned, in bytes.

`buffer`

Type: **BYTE\***

The package graph's current generation ID, represented as an array of <a href="/windows/win32/api/appmodel/ns-appmodel-package_info">PACKAGE_INFO</a> structures.

`count`

Type: **UINT32\***

The number of structures in the buffer.

## Return value

Type: **LONG**

If the function succeeds it returns **ERROR_SUCCESS**. Otherwise, the function returns an error code. The possible error codes include the following.

|Return code|Description|
|-|-|
|**APPMODEL_ERROR_NO_PACKAGE**|The process has no package identity.|
|**ERROR_INSUFFICIENT_BUFFER**|The buffer is not large enough to hold the data. The required size is specified  by <i>bufferLength</i>.|

## Remarks

This function does not have an associated header file or library file. Your application can call [**LoadLibrary**](/windows/win32/api/libloaderapi/nf-libloaderapi-loadlibrarya) with the DLL name (`Kernel32.dll`) to obtain a module handle. It can then call [**GetProcAddress**](/windows/win32/api/libloaderapi/nf-libloaderapi-getprocaddress) with the module handle and the name of this function to get the function address.

## Requirements

| &nbsp; | &nbsp; |
| ---- |:---- |
| **Minimum supported client** | Windows 10 [desktop apps only] |
| **Minimum supported server** | Windows Server 2016 [desktop apps only] |
| **Target Platform** | Windows |
| **Header** | None |
| **Library** | None |
| **DLL** | Kernel32.dll |

## See also

* [GetCurrentPackageInfo](/windows/win32/api/appmodel/nf-appmodel-getcurrentpackageinfo)
* [GetCurrentPackageFamilyName](/windows/win32/api/appmodel/nf-appmodel-getcurrentpackagefamilyname)
* [GetCurrentPackageFullName](/windows/win32/api/appmodel/nf-appmodel-getcurrentpackagefullname)
* [GetCurrentPackageId](/windows/win32/api/appmodel/nf-appmodel-getcurrentpackageid)
* [GetCurrentPackagePath](/windows/win32/api/appmodel/nf-appmodel-getcurrentpackagepath)
* [GetPackageInfo](/windows/win32/api/appmodel/nf-appmodel-getpackageinfo)
* [GetPackageInfo2](/windows/win32/api/appmodel/nf-appmodel-getpackageinfo2)
