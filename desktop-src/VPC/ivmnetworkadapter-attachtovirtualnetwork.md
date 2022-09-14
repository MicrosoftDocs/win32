---
title: IVMNetworkAdapter AttachToVirtualNetwork method (VPCCOMInterfaces.h)
description: Attaches the network interface to the specified virtual network.
ms.assetid: c743e930-c22e-4f32-b691-f7adc2485fed
keywords:
- AttachToVirtualNetwork method Virtual PC
- AttachToVirtualNetwork method Virtual PC , IVMNetworkAdapter interface
- IVMNetworkAdapter interface Virtual PC , AttachToVirtualNetwork method
topic_type:
- apiref
api_name:
- IVMNetworkAdapter.AttachToVirtualNetwork
api_location:
- VPCCOMInterfaces.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IVMNetworkAdapter::AttachToVirtualNetwork method

\[Windows Virtual PC is no longer available for use as of Windows 8. Instead, use the [Hyper-V WMI provider (V2)](/windows/desktop/HyperV_v2/windows-virtualization-portal).\]

Attaches the network interface to the specified virtual network.

## Syntax


```C++
HRESULT AttachToVirtualNetwork(
  [in] IVMVirtualNetwork *virtualNetwork
);
```



## Parameters

<dl> <dt>

*virtualNetwork* \[in\]
</dt> <dd>

The virtual network to which this virtual NIC will be connected. See [**IVMVirtualNetwork**](ivmvirtualnetwork.md).

</dd> </dl>

## Return value

This method can return one of these values.



| Return code/value                                                                                                                                                                          | Description                                                        |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                                                                                                       | The operation was successful.<br/>                           |
| <dl> <dt>**E\_POINTER**</dt> <dt>0x80004003</dt> </dl>                                  | The parameter is **NULL**.<br/>                              |
| <dl> <dt>**E\_INVALIDARG**</dt> <dt>0x80000003</dt> </dl>                               | The parameter does not contain a valid virtual network.<br/> |
| <dl> <dt>**HRESULT\_FROM\_WIN32(ERROR\_ACCESS\_DENIED)**</dt> <dt>0x80070005</dt> </dl> | Access was denied to the requested virtual network.<br/>     |
| <dl> <dt>**VM\_E\_VM\_UNKNOWN**</dt> <dt>0xA0040207</dt> </dl>                          | The virtual machine is invalid or no longer exists.<br/>     |
| <dl> <dt>**VM\_E\_INVALID\_VIRTUAL\_NETWORK\_ID**</dt> </dl>                                                                        | The parameter is not an existing virtual network.<br/>       |
| <dl> <dt>**DISP\_E\_EXCEPTION**</dt> </dl>                                                                                          | An unexpected error has occurred.<br/>                       |



 

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                                    |
| Minimum supported server<br/> | None supported<br/>                                                                     |
| End of client support<br/>    | Windows 7<br/>                                                                          |
| Product<br/>                  | Windows Virtual PC<br/>                                                                 |
| Header<br/>                   | <dl> <dt>VPCCOMInterfaces.h</dt> </dl> |
| IID<br/>                      | IID\_IVMNetworkAdapter is defined as e32e4165-22b8-4dc0-8d57-850171ae207a<br/>          |



## See also

<dl> <dt>

[**IVMNetworkAdapter**](ivmnetworkadapter.md)
</dt> </dl>

 

