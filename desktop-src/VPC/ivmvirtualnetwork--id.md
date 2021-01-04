---
title: IVMVirtualNetwork _ID method (VPCCOMInterfaces.h)
description: Retrieves the internal identifier of the virtual network.
ms.assetid: 6f1f75be-4218-40b8-8c73-938f0801f5e5
keywords:
- _ID method Virtual PC
- _ID method Virtual PC , IVMVirtualNetwork interface
- IVMVirtualNetwork interface Virtual PC , _ID method
topic_type:
- apiref
api_name:
- IVMVirtualNetwork._ID
api_location:
- VPCCOMInterfaces.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IVMVirtualNetwork::\_ID method

\[Windows Virtual PC is no longer available for use as of Windows 8. Instead, use the [Hyper-V WMI provider (V2)](/windows/desktop/HyperV_v2/windows-virtualization-portal).\]

Retrieves the internal identifier of the virtual network.

## Syntax


```C++
HRESULT _ID(
  [out] VARIANT *virtualNetworkID
);
```



## Parameters

<dl> <dt>

*virtualNetworkID* \[out\]
</dt> <dd>

The virtual network identifier. The identifier for the Shared Networking (NAT) virtual network is 01010101010101010101010101010101.

</dd> </dl>

## Return value

This method can return one of these values.



| Return code/value                                                                                                                                                 | Description                                  |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------|
| <dl> <dt>**S\_OK**</dt> <dt>0</dt> </dl>                       | The operation was successful.<br/>     |
| <dl> <dt>**E\_POINTER**</dt> <dt>0x80004003</dt> </dl>         | The parameter is **NULL**.<br/>        |
| <dl> <dt>**DISP\_E\_EXCEPTION**</dt> <dt>0x80020009</dt> </dl> | An unexpected error has occurred.<br/> |



 

## Remarks

This property is not usable by scripting languages.

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

 

