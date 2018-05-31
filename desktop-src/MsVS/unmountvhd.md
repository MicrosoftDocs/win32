---
title: UnmountVHD function
description: Unmounts a virtual hard disk file (.vhd file) that had been mounted with the MountVHD function.
ms.assetid: 862ab967-607a-439e-8926-70f1a6ae49da
keywords:
- UnmountVHD function Virtual Server
topic_type:
- apiref
api_name:
- UnmountVHD
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

# UnmountVHD function

Unmounts a virtual hard disk file (.vhd file) that had been mounted with the [**MountVHD**](mountvhd.md) function.

## Syntax


```C++
ULONG WINAPI UnmountVHD(
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



| Value                                                                                                                                                                                                                             | Meaning                                                                                                                                                                                                              |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="VHD_NORMAL"></span><span id="vhd_normal"></span><dl> <dt>**VHD\_NORMAL**</dt> <dt>0</dt> </dl>                       | Unmount the VHD file normally.<br/>                                                                                                                                                                            |
| <span id="VHD_FORCE_UNMOUNT"></span><span id="vhd_force_unmount"></span><dl> <dt>**VHD\_FORCE\_UNMOUNT**</dt> <dt>3</dt> </dl> | Force the system to unmount the VHD file without sending any device eject notification. This could result in a message being logged in the event viewer and data loss and corruption on the mounted file.<br/> |



 

</dd> </dl>

## Return value

On successful call, the return value is **ERROR\_SUCCESS** (0). Any of the [system error codes](https://msdn.microsoft.com/library/windows/desktop/ms681381) can be returned. Common return values include the following.



| Return code/value                                                                                                                                                       | Description                                                                                                                                      |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**ERROR\_INVALID\_DATA**</dt> <dt>13 (0xD)</dt> </dl>       | A value other than **VHD\_NORMAL** (0) or **VHD\_FORCE\_UNMOUNT** (3) was passed in the *Flags* parameter.<br/>                            |
| <dl> <dt>**ERROR\_DEV\_NOT\_EXIST**</dt> <dt>55 (0x37)</dt> </dl>    | An error occurred while unmounting the file.<br/>                                                                                          |
| <dl> <dt>**ERROR\_DEVICE\_IN\_USE**</dt> <dt>2404 (0x964)</dt> </dl> | The device is in use and cannot be unmounted. Passing **VHD\_FORCE\_UNMOUNT** in the *Flags* parameter can force the file to unmount.<br/> |



 

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

[**MountVHD**](mountvhd.md)
</dt> <dt>

[**VHD\_FLAGS**](vhd-flags.md)
</dt> </dl>

 

 





