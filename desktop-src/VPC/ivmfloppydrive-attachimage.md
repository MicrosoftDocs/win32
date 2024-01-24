---
title: IVMFloppyDrive AttachImage method (VPCCOMInterfaces.h)
description: Attaches a floppy media image on the host to the floppy drive of the virtual machine.
ms.assetid: ee7ea6ac-47ef-4e7b-8df3-28c716a728b0
keywords:
- AttachImage method Virtual PC
- AttachImage method Virtual PC , IVMFloppyDrive interface
- IVMFloppyDrive interface Virtual PC , AttachImage method
topic_type:
- apiref
api_name:
- IVMFloppyDrive.AttachImage
api_location:
- VPCCOMInterfaces.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IVMFloppyDrive::AttachImage method

\[Windows Virtual PC is no longer available for use as of Windows 8. Instead, use the [Hyper-V WMI provider (V2)](/windows/desktop/HyperV_v2/windows-virtualization-portal).\]

Attaches a floppy media image on the host to the floppy drive of the virtual machine.

## Syntax


```C++
HRESULT AttachImage(
  [in] BSTR mediaImagePath
);
```



## Parameters

<dl> <dt>

*mediaImagePath* \[in\]
</dt> <dd>

The full path to the floppy media image that is to be attached.

</dd> </dl>

## Return value

This method can return one of these values.



| Return code/value                                                                                                                                                                            | Description                                                                                                                             |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> <dt>0</dt> </dl>                                                  | The operation was successful.<br/>                                                                                                |
| <dl> <dt>**E\_INVALIDARG**</dt> <dt>0x80000003</dt> </dl>                                 | The *mediaImagePath* parameter is not valid.<br/>                                                                                 |
| <dl> <dt>**E\_POINTER**</dt> <dt>0x80004003</dt> </dl>                                    | The parameter is **NULL**.<br/>                                                                                                   |
| <dl> <dt>**HRESULT\_FROM\_WIN32(ERROR\_OUTOFMEMORY)**</dt> <dt>0x8007000e</dt> </dl>      | There is not enough memory available to complete this request.<br/>                                                               |
| <dl> <dt>**HRESULT\_FROM\_WIN32(ERROR\_BUFFER\_OVERFLOW)**</dt> <dt>0x8007006f</dt> </dl> | The path specified by the *mediaImagePath* parameter is too long. The path must be less than **MAX\_PATH** (260) characters.<br/> |
| <dl> <dt>**HRESULT\_FROM\_WIN32(ERROR\_INVALID\_NAME)**</dt> <dt>0x8007007b</dt> </dl>    | The *mediaImagePath* parameter contains an invalid character (one of "\*?<>/\|":").<br/>                                    |
| <dl> <dt>**HRESULT\_FROM\_WIN32(ERROR\_BAD\_PATHNAME)**</dt> <dt>0x800700a1</dt> </dl>    | The *mediaImagePath* parameter specifies an empty or relative path. An absolute path is required.<br/>                            |
| <dl> <dt>**VM\_E\_VM\_UNKNOWN**</dt> <dt>0xA0040207</dt> </dl>                            | The configuration for this virtual machine is not valid or cannot be found.<br/>                                                  |
| <dl> <dt>**VM\_E\_IMAGE\_CAPTURE\_FAIL**</dt> <dt>0xA00400650</dt> </dl>                  | The image file specified could not be captured.<br/>                                                                              |
| <dl> <dt>**DISP\_E\_EXCEPTION**</dt> <dt>0x80020009</dt> </dl>                            | An unexpected error has occurred.<br/>                                                                                            |



 

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                                    |
| Minimum supported server<br/> | None supported<br/>                                                                     |
| End of client support<br/>    | Windows 7<br/>                                                                          |
| Product<br/>                  | Windows Virtual PC<br/>                                                                 |
| Header<br/>                   | <dl> <dt>VPCCOMInterfaces.h</dt> </dl> |
| IID<br/>                      | IID\_IVMFloppyDrive is defined as 661abee6-112a-4ed9-babf-3c874969f10e<br/>             |



## See also

<dl> <dt>

[**IVMFloppyDrive**](ivmfloppydrive.md)
</dt> </dl>

 

