---
title: IVMDVDDrive AttachImage method (VPCCOMInterfaces.h)
description: Attaches an ISO image to the DVD drive within the VM.
ms.assetid: 08947898-ca3f-41b6-97a3-52dc6977fc6d
keywords:
- AttachImage method Virtual PC
- AttachImage method Virtual PC , IVMDVDDrive interface
- IVMDVDDrive interface Virtual PC , AttachImage method
topic_type:
- apiref
api_name:
- IVMDVDDrive.AttachImage
api_location:
- VPCCOMInterfaces.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IVMDVDDrive::AttachImage method

\[Windows Virtual PC is no longer available for use as of Windows 8. Instead, use the [Hyper-V WMI provider (V2)](/windows/desktop/HyperV_v2/windows-virtualization-portal).\]

Attaches an ISO image to the DVD drive within the virtual machine (VM).

## Syntax


```C++
HRESULT AttachImage(
  [in] BSTR imagePath
);
```



## Parameters

<dl> <dt>

*imagePath* \[in\]
</dt> <dd>

The full path to the ISO image that is to be attached.

</dd> </dl>

## Return value

This method can return one of these values.



| Return code/value                                                                                                                                                    | Description                                                                                                  |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> <dt>0</dt> </dl>                          | The operation was successful.<br/>                                                                     |
| <dl> <dt>**E\_INVALIDARG**</dt> <dt>0x80000003</dt> </dl>         | The *imagePath* parameter is a directory.<br/>                                                         |
| <dl> <dt>**E\_POINTER**</dt> <dt>0x80004003</dt> </dl>            | The *imagePath* parameter is **NULL**.<br/>                                                            |
| <dl> <dt>**VM\_E\_VM\_UNKNOWN**</dt> <dt>0xA0040207</dt> </dl>    | The VM could not be found.<br/>                                                                        |
| <dl> <dt>**VM\_E\_DRIVE\_IN\_USE**</dt> <dt>0xA0040727</dt> </dl> | A host DVD drive or ISO image is already attached to this drive.<br/>                                  |
| <dl> <dt>**VM\_E\_DRIVE\_INVALID**</dt> <dt>0xA0040502</dt> </dl> | The bus location for this drive is invalid, or the drive does not appear to be a valid DVD drive.<br/> |
| <dl> <dt>**DISP\_E\_EXCEPTION**</dt> <dt>0x80020009</dt> </dl>    | An unexpected error has occurred.<br/>                                                                 |



 

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                                    |
| Minimum supported server<br/> | None supported<br/>                                                                     |
| End of client support<br/>    | Windows 7<br/>                                                                          |
| Product<br/>                  | Windows Virtual PC<br/>                                                                 |
| Header<br/>                   | <dl> <dt>VPCCOMInterfaces.h</dt> </dl> |
| IID<br/>                      | IID\_IVMDVDDrive is defined as b96328f6-6732-437d-a00d-ffa47e43971c<br/>                |



## See also

<dl> <dt>

[**IVMDVDDrive**](ivmdvddrive.md)
</dt> </dl>

 

