---
title: IVMVirtualNetworkCollection Count property (VPCCOMInterfaces.h)
description: Retrieves the number of virtual networks in this collection.
ms.assetid: a9a3ab48-74a0-498e-936e-a99c7b027a85
keywords:
- Count property Virtual PC
- Count property Virtual PC , IVMVirtualNetworkCollection interface
- IVMVirtualNetworkCollection interface Virtual PC , Count property
topic_type:
- apiref
api_name:
- IVMVirtualNetworkCollection.Count
- IVMVirtualNetworkCollection.get_Count
api_location:
- VPCCOMInterfaces.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IVMVirtualNetworkCollection::Count property

\[Windows Virtual PC is no longer available for use as of Windows 8. Instead, use the [Hyper-V WMI provider (V2)](/windows/desktop/HyperV_v2/windows-virtualization-portal).\]

Retrieves the number of virtual networks in this collection.

This property is read-only.

## Syntax


```C++
HRESULT get_Count(
  [out, retval] long *count
);
```



## Property value

The number of virtual networks.

## Error codes



| Name/value                                                                                                                                                    | Meaning                                      |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------|
| <dl> <dt>S\_OK</dt> <dt>0</dt> </dl>                       | The operation was successful.<br/>     |
| <dl> <dt>E\_POINTER</dt> <dt>0x80004003</dt> </dl>         | The parameter is **NULL**.<br/>        |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> <dt>0x80020009</dt> </dl> | An unexpected error has occurred.<br/> |



## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                                     |
| Minimum supported server<br/> | None supported<br/>                                                                      |
| End of client support<br/>    | Windows 7<br/>                                                                           |
| Product<br/>                  | Windows Virtual PC<br/>                                                                  |
| Header<br/>                   | <dl> <dt>VPCCOMInterfaces.h</dt> </dl>  |
| IID<br/>                      | IID\_IVMVirtualNetworkCollection is defined as 8ed680be-4242-4b2a-a21c-1982d8b0f675<br/> |



## See also

<dl> <dt>

[**IVMVirtualNetworkCollection**](ivmvirtualnetworkcollection.md)
</dt> </dl>

 

