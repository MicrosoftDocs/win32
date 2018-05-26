---
title: GetSCSIAddress function
description: Retrieves the SCSI address of the virtual hard disk (VHD) mounted using the MountVHD function.
ms.assetid: 880b9ef9-6264-4909-8c24-5772e1963074
keywords:
- GetSCSIAddress function Virtual Server
topic_type:
- apiref
api_name:
- GetSCSIAddress
api_location:
- VHDMount.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# GetSCSIAddress function

Retrieves the SCSI address of the virtual hard disk (VHD) mounted using the [**MountVHD**](mountvhd.md) function.

## Syntax


```C++
ULONG WINAPI GetSCSIAddress(
  _In_  PWCHAR VHDFileName,
  _In_  ULONG  Flags,
  _In_  ULONG  SCSIAddressLength,
  _Out_ PWCHAR SCSIAddress
);
```



## Parameters

<dl> <dt>

*VHDFileName* \[in\]
</dt> <dd>

A pointer to a null-terminated Unicode string that specifies the path to the VHD file used in the call to [**MountVHD**](mountvhd.md).

</dd> <dt>

*Flags* \[in\]
</dt> <dd>

This parameter is reserved. Use **VHD\_NORMAL** (0).

</dd> <dt>

*SCSIAddressLength* \[in\]
</dt> <dd>

The size, in **WCHAR**s, of the buffer pointed to by the *SCSIAddress* parameter.

</dd> <dt>

*SCSIAddress* \[out\]
</dt> <dd>

The address of a buffer to receive the SCSI address of the specified mounted VHD. The buffer must be at least **MAX\_PATH**+1 **WCHAR**s in size.

</dd> </dl>

## Return value

On successful call, the return value is **ERROR\_SUCCESS** (0). Any of the [system error codes](https://msdn.microsoft.com/library/windows/desktop/ms681381) can be returned. Common return values include the following.



| Return code/value                                                                                                                                                    | Description                                                                                                                                                                                  |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**ERROR\_INVALID\_DATA**</dt> <dt>13 (0xD)</dt> </dl>    | A value other than **VHD\_NORMAL** (0) was passed in the *Flags* parameter, the *SCSIAddressLength* parameter was zero, or the *SCSIAddress* parameter was **NULL**.<br/>              |
| <dl> <dt>**ERROR\_DEV\_NOT\_EXIST**</dt> <dt>55 (0x37)</dt> </dl> | An error occurred while retrieving the SCSI address of the mounted disk.<br/>                                                                                                          |
| <dl> <dt>**ERROR\_NOT\_READY**</dt> <dt>21 (0x15)</dt> </dl>      | The device is not yet ready. It takes some time for a newly mounted disk to appear in disk manager. Typically this error is handled by waiting for a short time and trying again.<br/> |



 

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

 

 





