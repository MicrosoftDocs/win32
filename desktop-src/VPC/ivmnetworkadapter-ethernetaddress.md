---
title: IVMNetworkAdapter EthernetAddress property (VPCCOMInterfaces.h)
description: Ethernet (MAC) address of the network interface.
ms.assetid: 2d94c5b3-6b69-4fb1-bee4-081dc026dde3
keywords:
- EthernetAddress property Virtual PC
- EthernetAddress property Virtual PC , IVMNetworkAdapter interface
- IVMNetworkAdapter interface Virtual PC , EthernetAddress property
topic_type:
- apiref
api_name:
- IVMNetworkAdapter.EthernetAddress
- IVMNetworkAdapter.get_EthernetAddress
- IVMNetworkAdapter.put_EthernetAddress
api_location:
- VPCCOMInterfaces.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IVMNetworkAdapter::EthernetAddress property

\[Windows Virtual PC is no longer available for use as of Windows 8. Instead, use the [Hyper-V WMI provider (V2)](/windows/desktop/HyperV_v2/windows-virtualization-portal).\]

Retrieves and sets the Ethernet (MAC) address of the network interface.

This property is read/write.

## Syntax


```C++
HRESULT put_EthernetAddress(
  [in]          BSTR ethernetAddress
);

HRESULT get_EthernetAddress(
  [out, retval] BSTR *ethernetAddress
);
```



## Property value

The MAC address of the virtual NIC. It should have the form "*XX*-*XX*-*XX*-*XX*-*XX*-*XX*" where each *X* is a hexadecimal digit.

## Error codes



| Name/value                                                                                                                                                                         | Meaning                                                                                                                                                                                                                                                                                                                                                                                     |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>                                                                                                   | The operation was successful.<br/>                                                                                                                                                                                                                                                                                                                                                    |
| <dl> <dt>E\_POINTER</dt> <dt>0x80004003</dt> </dl>                              | The parameter is **NULL**.<br/>                                                                                                                                                                                                                                                                                                                                                       |
| <dl> <dt>E\_INVALIDARG</dt> <dt>0x80000003</dt> </dl>                           | The parameter is not in the correct format.<br/>                                                                                                                                                                                                                                                                                                                                      |
| <dl> <dt>VM\_E\_CANT\_SET\_DYNAMIC\_MAC\_ADDRESS</dt> <dt>0xA004070A</dt> </dl> | The Ethernet address for a network interface can either be generated dynamically or can be set to a static address by the user. This method cannot be called when the address is set to be generated dynamically. The [**IsEthernetAddressDynamic**](ivmnetworkadapter-isethernetaddressdynamic.md) property is used to change the generation behavior of the Ethernet address.<br/> |
| <dl> <dt>VM\_E\_VM\_UNKNOWN</dt> <dt>0xA0040207</dt> </dl>                      | The virtual machine was not found. This may occur if the machine was removed after the [**IVMNetworkAdapter**](ivmnetworkadapter.md) object was created.<br/>                                                                                                                                                                                                                        |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> <dt>0x80020009</dt> </dl>                      | An unexpected error has occurred.<br/>                                                                                                                                                                                                                                                                                                                                                |



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

 

