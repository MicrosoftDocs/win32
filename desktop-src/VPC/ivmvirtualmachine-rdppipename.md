---
title: IVMVirtualMachine RdpPipeName property (VPCCOMInterfaces.h)
description: Retrieves the name of the RDP connection named pipe used for video and input.
ms.assetid: 0c2d0f23-40cd-4a86-96dd-546fb3570871
keywords:
- RdpPipeName property Virtual PC
- RdpPipeName property Virtual PC , IVMVirtualMachine interface
- IVMVirtualMachine interface Virtual PC , RdpPipeName property
topic_type:
- apiref
api_name:
- IVMVirtualMachine.RdpPipeName
- IVMVirtualMachine.get_RdpPipeName
api_location:
- VPCCOMInterfaces.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IVMVirtualMachine::RdpPipeName property

\[Windows Virtual PC is no longer available for use as of Windows 8. Instead, use the [Hyper-V WMI provider (V2)](/windows/desktop/HyperV_v2/windows-virtualization-portal).\]

Retrieves the name of the RDP connection named pipe used for video and input.

This property is read-only.

## Syntax


```C++
HRESULT get_RdpPipeName(
  [out, retval] BSTR *RdpPipeName
);
```



## Property value

Name of the RDP connection named pipe used for video and input.

## Error codes

If the method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.



| Name/value                                                                                                                                                         | Meaning                                           |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------|
| <dl> <dt>S\_OK</dt> <dt>0</dt> </dl>                            | The operation was successful.<br/>          |
| <dl> <dt>E\_POINTER</dt> <dt>0x80004003</dt> </dl>              | The RdpPipeName parameter is **NULL**.<br/> |
| <dl> <dt>VM\_E\_VM\_NOT\_RUNNING</dt> <dt>0xA0040206</dt> </dl> | The virtual machine is not running.<br/>    |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> <dt>0x80020009</dt> </dl>      | An unknown error occurred.<br/>             |



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

 

