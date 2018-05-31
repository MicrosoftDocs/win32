---
title: MountVHD function
description: Mounts the specified virtual hard disk file (.vhd file) as a virtual disk device.
ms.assetid: eae54758-b73c-4bf3-a797-26649c807a34
keywords:
- MountVHD function Virtual Server
topic_type:
- apiref
api_name:
- MountVHD
api_location:
- VHDMount.dll
api_type:
- DllExport
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MountVHD function

Mounts the specified virtual hard disk file (.vhd file) as a virtual disk device.

## Syntax


```C++
ULONG WINAPI MountVHD(
  _In_ PWCHAR VHDFileName,
  _In_ ULONG  Flags
);
```



## Parameters

<dl> <dt>

*VHDFileName* \[in\]
</dt> <dd>

A pointer to a null-terminated Unicode string that specifies the full path to the VHD file. Relative paths to the VHD file are not supported.

</dd> <dt>

*Flags* \[in\]
</dt> <dd>

This parameter is reserved. Use **VHD\_NORMAL** (0).

</dd> </dl>

## Return value

On successful call, the return value is **ERROR\_SUCCESS** (0). Any of the [system error codes](https://msdn.microsoft.com/library/windows/desktop/ms681381) can be returned. Common return values include the following.



| Return code/value                                                                                                                                                    | Description                                                                            |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|
| <dl> <dt>**ERROR\_INVALID\_DATA**</dt> <dt>13 (0xD)</dt> </dl>    | A value other than **VHD\_NORMAL** (0) was passed in the *Flags* parameter.<br/> |
| <dl> <dt>**ERROR\_DEV\_NOT\_EXIST**</dt> <dt>55 (0x37)</dt> </dl> | An error occurred while mounting the file.<br/>                                  |



 

## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VHDMount.h</dt> </dl>             |
| Library<br/>  | <dl> <dt>VHDMount.lib</dt> </dl>           |
| DLL<br/>      | <dl> <dt>VHDMount.dll</dt> </dl>           |



## See also

<dl> <dt>

[Virtual Server Functions](virtual-server-functions.md)
</dt> <dt>

[**GetSCSIAddress**](getscsiaddress.md)
</dt> <dt>

[**UnmountVHD**](unmountvhd.md)
</dt> <dt>

[**VHD\_FLAGS**](vhd-flags.md)
</dt> </dl>

 

 





