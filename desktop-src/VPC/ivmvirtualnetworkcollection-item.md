---
title: IVMVirtualNetworkCollection Item property (VPCCOMInterfaces.h)
description: IVMVirtualNetwork object that corresponds to the specified index.
ms.assetid: 1c6a3449-f76a-4216-8840-0fb9fb133e67
keywords:
- Item property Virtual PC
- Item property Virtual PC , IVMVirtualNetworkCollection interface
- IVMVirtualNetworkCollection interface Virtual PC , Item property
topic_type:
- apiref
api_name:
- IVMVirtualNetworkCollection.Item
- IVMVirtualNetworkCollection.get_Item
api_location:
- VPCCOMInterfaces.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IVMVirtualNetworkCollection::Item property

\[Windows Virtual PC is no longer available for use as of Windows 8. Instead, use the [Hyper-V WMI provider (V2)](/windows/desktop/HyperV_v2/windows-virtualization-portal).\]

Retrieves the [**IVMVirtualNetwork**](ivmvirtualnetwork.md) object that corresponds to the specified index.

This property is read-only.

## Syntax


```C++
HRESULT get_Item(
  [in]          long              index,
  [out, retval] IVMVirtualNetwork **virtualNetwork
);
```



## Property value

The [**IVMVirtualNetwork**](ivmvirtualnetwork.md) object.

## Error codes



| Name/value                                                                                                                                                    | Meaning                                                                                       |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|
| <dl> <dt>S\_OK</dt> <dt>0</dt> </dl>                       | The operation was successful.<br/>                                                      |
| <dl> <dt>E\_POINTER</dt> <dt>0x80004003</dt> </dl>         | The *virtualNetwork* parameter is **NULL**.<br/>                                        |
| <dl> <dt>DISP\_E\_BADINDEX</dt> <dt>0x8002000B</dt> </dl>  | The index of the requested item does not correspond to an item in this collection.<br/> |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> <dt>0x80020009</dt> </dl> | An unexpected error has occurred.<br/>                                                  |



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

[**IVMVirtualNetwork**](ivmvirtualnetwork.md)
</dt> <dt>

[**IVMVirtualNetworkCollection**](ivmvirtualnetworkcollection.md)
</dt> </dl>

 

