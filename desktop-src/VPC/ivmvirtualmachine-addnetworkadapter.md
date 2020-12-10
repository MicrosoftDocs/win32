---
title: IVMVirtualMachine AddNetworkAdapter method (VPCCOMInterfaces.h)
description: Adds a network interface to the virtual machine.
ms.assetid: 1fa39d2c-4a5a-42cb-afa4-520bf19b8cc8
keywords:
- AddNetworkAdapter method Virtual PC
- AddNetworkAdapter method Virtual PC , IVMVirtualMachine interface
- IVMVirtualMachine interface Virtual PC , AddNetworkAdapter method
topic_type:
- apiref
api_name:
- IVMVirtualMachine.AddNetworkAdapter
api_location:
- VPCCOMInterfaces.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IVMVirtualMachine::AddNetworkAdapter method

\[Windows Virtual PC is no longer available for use as of Windows 8. Instead, use the [Hyper-V WMI provider (V2)](/windows/desktop/HyperV_v2/windows-virtualization-portal).\]

Adds a network interface to the virtual machine.

## Syntax


```C++
HRESULT AddNetworkAdapter(
  [out, retval] IVMNetworkAdapter **networkAdapter
);
```



## Parameters

<dl> <dt>

*networkAdapter* \[out, retval\]
</dt> <dd>

An [**IVMNetworkAdapter**](ivmnetworkadapter.md) object.

</dd> </dl>

## Return value

This method can return one of these values.



| Return code/value                                                                                                                                                            | Description                                                     |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> <dt>0</dt> </dl>                                  | The operation was successful.<br/>                        |
| <dl> <dt>**E\_POINTER**</dt> <dt>0x80004003</dt> </dl>                    | The *networkAdapter* parameter is **NULL**.<br/>          |
| <dl> <dt>**VM\_E\_VM\_UNKNOWN**</dt> <dt>0xA0040207</dt> </dl>            | The configuration is unknown.<br/>                        |
| <dl> <dt>**VM\_E\_PREF\_ILLEGAL\_VALUE**</dt> <dt>0xA0040301</dt> </dl>   | No more than four (4) network adapters can be added.<br/> |
| <dl> <dt>**VM\_E\_VM\_RUNNING\_OR\_SAVED**</dt> <dt>0xA004020B</dt> </dl> | The virtual machine is in a running or saved state.<br/>  |
| <dl> <dt>**DISP\_E\_EXCEPTION**</dt> <dt>0x80020009</dt> </dl>            | An unexpected error has occurred.<br/>                    |



 

## Remarks

You can only add a new network interface to a stopped virtual machine. The newly created network adapter is not connected to a virtual network.

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

 

