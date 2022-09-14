---
title: IVMNetworkAdapter IsEthernetAddressDynamic property (VPCCOMInterfaces.h)
description: Determines whether the Ethernet address is dynamically generated.
ms.assetid: 7bd87868-f1d1-48e5-9e1b-04d2126f9dad
keywords:
- IsEthernetAddressDynamic property Virtual PC
- IsEthernetAddressDynamic property Virtual PC , IVMNetworkAdapter interface
- IVMNetworkAdapter interface Virtual PC , IsEthernetAddressDynamic property
topic_type:
- apiref
api_name:
- IVMNetworkAdapter.IsEthernetAddressDynamic
- IVMNetworkAdapter.get_IsEthernetAddressDynamic
- IVMNetworkAdapter.put_IsEthernetAddressDynamic
api_location:
- VPCCOMInterfaces.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IVMNetworkAdapter::IsEthernetAddressDynamic property

\[Windows Virtual PC is no longer available for use as of Windows 8. Instead, use the [Hyper-V WMI provider (V2)](/windows/desktop/HyperV_v2/windows-virtualization-portal).\]

Determines whether the Ethernet address is dynamically generated.

This property is read/write.

## Syntax


```C++
HRESULT put_IsEthernetAddressDynamic(
  [in]          VARIANT_BOOL isDynamic
);

HRESULT get_IsEthernetAddressDynamic(
  [out, retval] VARIANT_BOOL *isDynamic
);
```



## Property value

Set to VARIANT\_TRUE if the Ethernet address should be dynamically generated and VARIANT\_FALSE if the Ethernet address is static.

## Error codes



| Name/value                                                                                                                                                    | Meaning                                                                                                                                                              |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>S\_OK</dt> <dt>0</dt> </dl>                       | The operation was successful.<br/>                                                                                                                             |
| <dl> <dt>E\_POINTER</dt> <dt>0x80004003</dt> </dl>         | The parameter is **NULL**.<br/>                                                                                                                                |
| <dl> <dt>VM\_E\_VM\_UNKNOWN</dt> <dt>0xA0040207</dt> </dl> | The virtual machine was not found. This may occur if the machine was removed after the [**IVMNetworkAdapter**](ivmnetworkadapter.md) object was created.<br/> |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> <dt>0x80020009</dt> </dl> | An unexpected error has occurred.<br/>                                                                                                                         |



## Remarks

This property should be set to **TRUE** (default) for most virtual network interfaces. If software in the guest requires a static Ethernet address, this property should be set to **FALSE**.

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

 

