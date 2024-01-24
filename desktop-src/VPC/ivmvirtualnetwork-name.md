---
title: IVMVirtualNetwork Name property (VPCCOMInterfaces.h)
description: Unique name of the virtual network instance.
ms.assetid: dd4807dc-abae-4bdb-ba27-597cf1337834
keywords:
- Name property Virtual PC
- Name property Virtual PC , IVMVirtualNetwork interface
- IVMVirtualNetwork interface Virtual PC , Name property
topic_type:
- apiref
api_name:
- IVMVirtualNetwork.Name
- IVMVirtualNetwork.get_Name
api_location:
- VPCCOMInterfaces.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IVMVirtualNetwork::Name property

\[Windows Virtual PC is no longer available for use as of Windows 8. Instead, use the [Hyper-V WMI provider (V2)](/windows/desktop/HyperV_v2/windows-virtualization-portal).\]

Retrieves the unique name of the virtual network instance.

This property is read-only.

## Syntax


```C++
HRESULT get_Name(
  [out, retval] BSTR *virtualNetworkName
);
```



## Property value

The name of the virtual network.

## Error codes



| Name/value                                                                                                                                                    | Meaning                                                                                 |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------|
| <dl> <dt>S\_OK</dt> <dt>0</dt> </dl>                       | The operation was successful.<br/>                                                |
| <dl> <dt>E\_POINTER</dt> <dt>0x80004003</dt> </dl>         | The parameter is **NULL**.<br/>                                                   |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> <dt>0x80020009</dt> </dl> | An unexpected error has occurred or the virtual network instance is unknown.<br/> |



## Remarks

Virtual network names are case-insensitive, for example, "MyNetwork" and "mynetwork" refer to the same virtual network.

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

 

