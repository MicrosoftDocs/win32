---
title: IVMVirtualNetwork HostAdapter property (VPCCOMInterfaces.h)
description: Name of the adapter to which the virtual network is connected.
ms.assetid: 7ee074d2-13ba-42db-84db-ecfd22576a9a
keywords:
- HostAdapter property Virtual PC
- HostAdapter property Virtual PC , IVMVirtualNetwork interface
- IVMVirtualNetwork interface Virtual PC , HostAdapter property
topic_type:
- apiref
api_name:
- IVMVirtualNetwork.HostAdapter
- IVMVirtualNetwork.get_HostAdapter
api_location:
- VPCCOMInterfaces.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IVMVirtualNetwork::HostAdapter property

\[Windows Virtual PC is no longer available for use as of Windows 8. Instead, use the [Hyper-V WMI provider (V2)](/windows/desktop/HyperV_v2/windows-virtualization-portal).\]

Retrieves the name of the adapter to which the virtual network is connected.

This property is read-only.

## Syntax


```C++
HRESULT get_HostAdapter(
  [out, retval] BSTR *hostAdapter
);
```



## Property value

The name of the host adapter to which the virtual network is connected.

## Error codes



| Name/value                                                                                                                                                            | Meaning                                                                                                                                                               |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>S\_OK</dt> <dt>0</dt> </dl>                               | The operation was successful.<br/>                                                                                                                              |
| <dl> <dt>E\_POINTER</dt> <dt>0x80004003</dt> </dl>                 | The parameter is **NULL**.<br/>                                                                                                                                 |
| <dl> <dt>VM\_E\_ADAPTER\_NOT\_FOUND</dt> <dt>0xA0040700</dt> </dl> | The host Ethernet adapter to which this virtual network was connected is no longer available. The host Ethernet adapter may have been removed or disabled.<br/> |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> <dt>0x80020009</dt> </dl>         | An unexpected error has occurred.<br/>                                                                                                                          |



## Remarks

The virtual network adapter allows a virtual network to talk to external networks. There is normally one adapter per Ethernet adapter installed in the host machine. For example, let's say a host machine had an adapter labeled "10/100 ENET". To connect a virtual NIC to the network attached to "10/100 ENET", set the virtual network's Network **HostAdapter** property to "10/100 ENET" and connect the virtual NIC to this virtual network.

If the **HostAdapter** property is set to an empty string (""), the virtual NIC adapter is connected to the "Internal Network" or "Shared Networking (NAT)" network. Virtual NICs attached to the "Internal Network" network will have no access to external networks on the system host. However, the virtual NICs attached to this virtual network are still able to communicate with each other.

The complete list of adapters can be accessed through the [**IVMHostInfo::NetworkAdapters**](ivmhostinfo-networkadapters.md) property.

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

 

