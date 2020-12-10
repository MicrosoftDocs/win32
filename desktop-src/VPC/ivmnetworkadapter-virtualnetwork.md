---
title: IVMNetworkAdapter VirtualNetwork property (VPCCOMInterfaces.h)
description: Retrieves the virtual network to which the network interface is attached.
ms.assetid: 7f52fd86-5f83-41d8-ba48-7db65e9c357c
keywords:
- VirtualNetwork property Virtual PC
- VirtualNetwork property Virtual PC , IVMNetworkAdapter interface
- IVMNetworkAdapter interface Virtual PC , VirtualNetwork property
topic_type:
- apiref
api_name:
- IVMNetworkAdapter.VirtualNetwork
- IVMNetworkAdapter.get_VirtualNetwork
api_location:
- VPCCOMInterfaces.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IVMNetworkAdapter::VirtualNetwork property

\[Windows Virtual PC is no longer available for use as of Windows 8. Instead, use the [Hyper-V WMI provider (V2)](/windows/desktop/HyperV_v2/windows-virtualization-portal).\]

Retrieves the virtual network to which the network interface is attached.

This property is read-only.

## Syntax


```C++
HRESULT get_VirtualNetwork(
  [out, retval] IVMVirtualNetwork **virtualNetwork
);
```



## Property value

An [**IVMVirtualNetwork**](ivmvirtualnetwork.md) interface that represents the virtual network to which this virtual network interface is attached.

## Error codes



| Name/value                                                                                                                                                                       | Meaning                                                                                   |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------|
| <dl> <dt>S\_OK</dt> <dt>0</dt> </dl>                                          | The operation was successful.<br/>                                                  |
| <dl> <dt>E\_POINTER</dt> <dt>0x80004003</dt> </dl>                            | The parameter is **NULL**.<br/>                                                     |
| <dl> <dt>S\_FALSE</dt> <dt>1</dt> </dl>                                       | This network interface is unplugged and is not connected to a virtual network.<br/> |
| <dl> <dt>VM\_E\_INVALID\_VIRTUAL\_NETWORK\_ID</dt> <dt>0xA00400702</dt> </dl> | This interface is connected to a virtual network with an invalid ID.<br/>           |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> <dt>0x80020009</dt> </dl>                    | An unexpected error has occurred.<br/>                                              |



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

 

