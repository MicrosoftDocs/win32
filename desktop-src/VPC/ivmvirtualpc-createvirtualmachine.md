---
title: IVMVirtualPC CreateVirtualMachine method (VPCCOMInterfaces.h)
description: Creates a new virtual machine configuration and retrieves the virtual machine object.
ms.assetid: 35f7364f-debd-4b9c-8240-23c0512eb004
keywords:
- CreateVirtualMachine method Virtual PC
- CreateVirtualMachine method Virtual PC , IVMVirtualPC interface
- IVMVirtualPC interface Virtual PC , CreateVirtualMachine method
topic_type:
- apiref
api_name:
- IVMVirtualPC.CreateVirtualMachine
api_location:
- VPCCOMInterfaces.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IVMVirtualPC::CreateVirtualMachine method

\[Windows Virtual PC is no longer available for use as of Windows 8. Instead, use the [Hyper-V WMI provider (V2)](/windows/desktop/HyperV_v2/windows-virtualization-portal).\]

Creates a new virtual machine configuration and retrieves the virtual machine object.

## Syntax


```C++
HRESULT CreateVirtualMachine(
  [in]          BSTR              configurationName,
  [in]          BSTR              configurationPath,
  [out, retval] IVMVirtualMachine **virtualMachine
);
```



## Parameters

<dl> <dt>

*configurationName* \[in\]
</dt> <dd>

The name of the virtual machine to be created. The length of the name cannot exceed 80 characters and the combined length of the name and path to VMC and VMCX files cannot exceed **MAX\_PATH** (260) characters. The file name extensions .vmc and .vmcx will be appended to the end of the virtual machine name when the configuration files are created. If this parameter is **NULL** or an empty string, the *configurationPath* parameter must specify the full path to the VMC file.

</dd> <dt>

*configurationPath* \[in\]
</dt> <dd>

The path to the folder that will contain the VMC file. This folder will be created if it does not exist. If *configurationName* is **NULL** or an empty string, this must specify the full path of the new configuration file.

</dd> <dt>

*virtualMachine* \[out, retval\]
</dt> <dd>

A pointer to a new [**IVMVirtualMachine**](ivmvirtualmachine.md) object that represents this virtual machine.

</dd> </dl>

## Return value

This method can return one of these values.



| Return code/value                                                                                                                                                                            | Description                                                                                                                                                                                                    |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> <dt>0</dt> </dl>                                                  | The operation was successful.<br/>                                                                                                                                                                       |
| <dl> <dt>**E\_POINTER**</dt> <dt>0x80004003</dt> </dl>                                    | The *configurationName* or *configurationPath* parameter is not valid, or the *virtualMachine* parameter is **NULL**.<br/>                                                                               |
| <dl> <dt>**HRESULT\_FROM\_WIN32(ERROR\_PATH\_NOT\_FOUND)**</dt> <dt>0x80070003</dt> </dl> | The system cannot find the path specified by the *configurationPath* parameter.<br/>                                                                                                                     |
| <dl> <dt>**HRESULT\_FROM\_WIN32(ERROR\_INVALID\_NAME)**</dt> <dt>0x8007007b</dt> </dl>    | The *configurationPath* parameter contains an invalid character (one of "\*?:<>/\|"").<br/>                                                                                                        |
| <dl> <dt>**HRESULT\_FROM\_WIN32(ERROR\_BAD\_PATHNAME)**</dt> <dt>0x800700a1</dt> </dl>    | The *configurationPath* parameter specifies an empty or relative path. An absolute path is required.<br/>                                                                                                |
| <dl> <dt>**HRESULT\_FROM\_WIN32(ERROR\_BUFFER\_OVERFLOW)**</dt> <dt>0x8007006f</dt> </dl> | The path specified by the *configurationName* and *configurationPath* parameters results in a path that is too long. The total length of the path must be less than **MAX\_PATH** (260) characters.<br/> |
| <dl> <dt>**HRESULT\_FROM\_WIN32(ERROR\_ALREADY\_EXISTS)**</dt> <dt>0x800700b7</dt> </dl>  | A configuration file with this name already exists at this location.<br/>                                                                                                                                |
| <dl> <dt>**VM\_E\_CONFIG\_NO\_NAME**</dt> <dt>0xA0040400</dt> </dl>                       | The *configurationName* parameter is empty.<br/>                                                                                                                                                         |
| <dl> <dt>**VM\_E\_CONFIG\_NAME\_TOO\_LONG**</dt> <dt>0xA0040401</dt> </dl>                | The *configurationName* parameter exceeds 80 characters in length.<br/>                                                                                                                                  |
| <dl> <dt>**VM\_E\_CONFIG\_NAME\_INVALID\_CHAR**</dt> <dt>0xA0040402</dt> </dl>            | The *configurationName* parameter contains an invalid character (one of "\*?:<>/\|\\"").<br/>                                                                                                      |
| <dl> <dt>**VM\_E\_CONFIG\_DUPLICATE\_NAME**</dt> <dt>0xA0040403</dt> </dl>                | There is already a virtual machine with this name.<br/>                                                                                                                                                  |
| <dl> <dt>**VM\_E\_HARDWARE\_VIRTUALIZATION\_DISABLED**</dt> <dt>0xA0040951</dt> </dl>     | The processor does not support Hardware Accelerated Virtualization (HAV) extensions.<br/>                                                                                                                |
| <dl> <dt>**DISP\_E\_EXCEPTION**</dt> <dt>0x80020009</dt> </dl>                            | An unexpected error has occurred.<br/>                                                                                                                                                                   |



 

## Remarks

Virtual machine names are case-insensitive, for example, "MyVM" and "myvm" refer to the same virtual machine.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                                    |
| Minimum supported server<br/> | None supported<br/>                                                                     |
| End of client support<br/>    | Windows 7<br/>                                                                          |
| Product<br/>                  | Windows Virtual PC<br/>                                                                 |
| Header<br/>                   | <dl> <dt>VPCCOMInterfaces.h</dt> </dl> |
| IID<br/>                      | IID\_IVMVirtualPC is defined as 236ba0d9-a24a-4292-a132-27c1421dfd01<br/>               |



## See also

<dl> <dt>

[**IVMVirtualPC**](ivmvirtualpc.md)
</dt> </dl>

 

