---
title: IVMVirtualMachine Name property (VPCCOMInterfaces.h)
description: Name of the virtual machine configuration.
ms.assetid: 90acedbf-4159-48a3-a9e9-6f1ee00dab8b
keywords:
- Name property Virtual PC
- Name property Virtual PC , IVMVirtualMachine interface
- IVMVirtualMachine interface Virtual PC , Name property
topic_type:
- apiref
api_name:
- IVMVirtualMachine.Name
- IVMVirtualMachine.get_Name
- IVMVirtualMachine.put_Name
api_location:
- VPCCOMInterfaces.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IVMVirtualMachine::Name property

\[Windows Virtual PC is no longer available for use as of Windows 8. Instead, use the [Hyper-V WMI provider (V2)](/windows/desktop/HyperV_v2/windows-virtualization-portal).\]

Retrieves and sets the name of the virtual machine configuration.

This property is read/write.

## Syntax


```C++
HRESULT put_Name(
  [in]          BSTR virtualMachineName
);

HRESULT get_Name(
  [out, retval] BSTR *virtualMachineName
);
```



## Property value

Specifies the name of the virtual machine configuration. The length of the name cannot be more than 80 characters and the total length of the fully qualified path that includes the virtual machine name configuration file cannot be more than **MAX\_PATH** (260) characters.

## Error codes



| Name/value                                                                                                                                                                    | Meaning                                                                                         |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|
| <dl> <dt>S\_OK</dt> <dt>0</dt> </dl>                                       | The operation was successful.<br/>                                                        |
| <dl> <dt>E\_POINTER</dt> <dt>0x80004003</dt> </dl>                         | The parameter is **NULL**.<br/>                                                           |
| <dl> <dt>E\_INVALIDARG</dt> <dt>0x80000003</dt> </dl>                      | The parameter is not valid or is an empty string.<br/>                                    |
| <dl> <dt>VM\_E\_VM\_UNKNOWN</dt> <dt>0xA0040207</dt> </dl>                 | The configuration is unknown.<br/>                                                        |
| <dl> <dt>VM\_E\_PREF\_VM\_ACTIVE</dt> <dt>0xA0040302</dt> </dl>            | The virtual machine is running or saved.<br/>                                             |
| <dl> <dt>VM\_E\_CONFIG\_NO\_NAME</dt> <dt>0xA0040400</dt> </dl>            | The *virtualMachineName* parameter is empty.<br/>                                         |
| <dl> <dt>VM\_E\_CONFIG\_NAME\_TOO\_LONG</dt> <dt>0xA00400401</dt> </dl>    | The parameter contains too many characters.<br/>                                          |
| <dl> <dt>VM\_E\_CONFIG\_NAME\_INVALID\_CHAR</dt> <dt>0xA0040402</dt> </dl> | The parameter contains one of the following invalid characters "\*?:<>/\|\\"".<br/> |
| <dl> <dt>VM\_E\_CONFIG\_DUPLICATE\_NAME</dt> <dt>0xA0040403</dt> </dl>     | The specified name already exists as the name of another virtual machine.<br/>            |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> <dt>0x80020009</dt> </dl>                 | An unexpected error has occurred.<br/>                                                    |



## Remarks

Virtual machine names are case-insensitive, e.g. "MyVM" and "myvm" refer to the same virtual machine. This is the default property for [**IVMVirtualMachine**](ivmvirtualmachine.md).

If VPC.exe is running and the VM is saved then setting the **Name** property will not succeed. If VPC.exe is not running and the VM is saved then setting the **Name** property will succeed when VPC.exe is next started.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                                    |
| Minimum supported server<br/> | None supported<br/>                                                                     |
| End of client support<br/>    | Windows 7<br/>                                                                          |
| Product<br/>                  | Windows Virtual PC<br/>                                                                 |
| Header<br/>                   | <dl> <dt>VPCCOMInterfaces.h</dt> </dl> |
| IID<br/>                      | IID\_IVMVirtualMachine is defined as f7092aa1-33ed-4f78-a59f-c00adfc2edd7<br/>          |



## See also

<dl> <dt>

[**IVMVirtualMachine**](ivmvirtualmachine.md)
</dt> </dl>

 

