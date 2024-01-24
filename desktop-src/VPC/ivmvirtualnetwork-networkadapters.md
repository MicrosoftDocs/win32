---
title: IVMVirtualNetwork NetworkAdapters property (VPCCOMInterfaces.h)
description: Retrieves an enumerable collection of NICs attached to the virtual network.
ms.assetid: d5b95831-4642-441e-93e8-34e125087a43
keywords:
- NetworkAdapters property Virtual PC
- NetworkAdapters property Virtual PC , IVMVirtualNetwork interface
- IVMVirtualNetwork interface Virtual PC , NetworkAdapters property
topic_type:
- apiref
api_name:
- IVMVirtualNetwork.NetworkAdapters
- IVMVirtualNetwork.get_NetworkAdapters
api_location:
- VPCCOMInterfaces.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IVMVirtualNetwork::NetworkAdapters property

\[Windows Virtual PC is no longer available for use as of Windows 8. Instead, use the [Hyper-V WMI provider (V2)](/windows/desktop/HyperV_v2/windows-virtualization-portal).\]

Retrieves an enumerable collection of NICs attached to the virtual network.

This property is read-only.

## Syntax


```C++
HRESULT get_NetworkAdapters(
  [out, retval] IVMNetworkAdapterCollection **networkInterfaceCollection
);
```



## Property value

A new [**IVMNetworkAdapterCollection**](ivmnetworkadaptercollection.md) which holds the virtual NICs attached to this virtual network.

## Error codes



| Name/value                                                                                                                                                    | Meaning                                      |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------|
| <dl> <dt>S\_OK</dt> <dt>0</dt> </dl>                       | The operation was successful.<br/>     |
| <dl> <dt>E\_POINTER</dt> <dt>0x80004003</dt> </dl>         | The parameter is **NULL**.<br/>        |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> <dt>0x80020009</dt> </dl> | An unexpected error has occurred.<br/> |



## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                                    |
| Minimum supported server<br/> | None supported<br/>                                                                     |
| End of client support<br/>    | Windows 7<br/>                                                                          |
| Product<br/>                  | Windows Virtual PC<br/>                                                                 |
| Header<br/>                   | <dl> <dt>VPCCOMInterfaces.h</dt> </dl> |
| IID<br/>                      | IID\_IVMVirtualNetwork is defined as 431cb7a1-2469-4563-b94e-38b987adca63<br/>          |



## See also

<dl> <dt>

[**IVMVirtualNetwork**](ivmvirtualnetwork.md)
</dt> </dl>

 

