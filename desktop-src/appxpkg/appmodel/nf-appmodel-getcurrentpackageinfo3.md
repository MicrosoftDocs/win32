---
title: GetCurrentPackageInfo3
description: Gets the package information for the calling process, with the option to specify the type of folder path to retrieve for the package.
ms.topic: article
ms.date: 05/02/2022
---

# GetCurrentPackageInfo3 function (appmodel.h)

Gets the package information for the calling process, with the option to specify the type of folder path to retrieve for the package.

See **Remarks** for info about how to call the function.

## Syntax

```cpp
LONG GetCurrentPackageInfo3(
  const UINT32    flags,
  PackagePathType packagePathType,
  UINT32          *bufferLength,
  BYTE            *buffer,
  UINT32          *count
);
```
## Parameters

`flags`

Type: **const UINT32**

The [package constants](/windows/desktop/appxpkg/package-constants) that specify how package information is retrieved. The **PACKAGE_FILTER_\*** flags are supported.

`packagePathType`

Type: [**PackagePathType**](/windows/win32/api/appmodel/ne-appmodel-packagepathtype)

Indicates the type of folder path to retrieve for the package (the original install folder or the mutable folder).

`bufferLength`

Type: **UINT32\***

On input, the size of <i>buffer</i>, in bytes. On output, the size of the array of structures returned, in bytes.

`buffer`

Type: **BYTE\***

The package information, represented as an array of <a href="/windows/win32/api/appmodel/ns-appmodel-package_info">PACKAGE_INFO</a> structures.

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

The *packagePathType* parameter is useful for applications that use the [windows.mutablePackageDirectories extension](/uwp/schemas/appxpackage/uapmanifestschema/element-desktop6-package-extension) in their package manifest. This extension specifies a folder under the `%ProgramFiles%\ModifiableWindowsApps` path where the contents of the application's install folder are projected so that users can modify the installation files. This feature is currently available only for certain types of desktop PC games that are published by Microsoft and our partners, and it enables these types of games to support mods.

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

* [GetCurrentPackageInfo](/windows/win32/api/appmodel/nf-appmodel-getcurrentpackageinfo.md)
* [GetCurrentPackageFamilyName](/windows/win32/api/appmodel/nf-appmodel-getcurrentpackagefamilyname)
* [GetCurrentPackageFullName](/windows/win32/api/appmodel/nf-appmodel-getcurrentpackagefullname)
* [GetCurrentPackageId](/windows/win32/api/appmodel/nf-appmodel-getcurrentpackageid)
* [GetCurrentPackagePath](/windows/win32/api/appmodel/nf-appmodel-getcurrentpackagepath)
* [GetPackageInfo](/windows/win32/api/appmodel/nf-appmodel-getpackageinfo)
* [GetPackageInfo2](/windows/win32/api/appmodel/nf-appmodel-getpackageinfo2.md)
