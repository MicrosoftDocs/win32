---
title: IVMVirtualPC FindVirtualNetwork method (VPCCOMInterfaces.h)
description: Retrieves a virtual network object that matches the requested name.
ms.assetid: 84526fa4-fe88-4466-866d-c432ed3125aa
keywords:
- FindVirtualNetwork method Virtual PC
- FindVirtualNetwork method Virtual PC , IVMVirtualPC interface
- IVMVirtualPC interface Virtual PC , FindVirtualNetwork method
topic_type:
- apiref
api_name:
- IVMVirtualPC.FindVirtualNetwork
api_location:
- VPCCOMInterfaces.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IVMVirtualPC::FindVirtualNetwork method

\[Windows Virtual PC is no longer available for use as of Windows 8. Instead, use the [Hyper-V WMI provider (V2)](/windows/desktop/HyperV_v2/windows-virtualization-portal).\]

Retrieves a virtual network object that matches the requested name.

## Syntax


```C++
HRESULT FindVirtualNetwork(
  [in]          BSTR              virtualNetworkName,
  [out, retval] IVMVirtualNetwork **virtualNetwork
);
```



## Parameters

<dl> <dt>

*virtualNetworkName* \[in\]
</dt> <dd>

The name of the virtual network to find.

</dd> <dt>

*virtualNetwork* \[out, retval\]
</dt> <dd>

A pointer to a new [**IVMVirtualNetwork**](ivmvirtualnetwork.md) object that represents this virtual network.

</dd> </dl>

## Return value

This method can return one of these values.



| Return code/value                                                                                                                                                                            | Description                                                                                     |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> <dt>0</dt> </dl>                                                  | The operation was successful.<br/>                                                        |
| <dl> <dt>**S\_FALSE**</dt> <dt>1</dt> </dl>                                               | The specified virtual network could not be found.<br/>                                    |
| <dl> <dt>**E\_POINTER**</dt> <dt>0x80004003</dt> </dl>                                    | The *virtualNetwork* parameter is **NULL** or the virtual network cannot be found.<br/>   |
| <dl> <dt>**E\_INVALIDARG**</dt> <dt>0x80000003</dt> </dl>                                 | The *virtualNetworkName* parameter is not valid or is an empty string.<br/>               |
| <dl> <dt>**HRESULT\_FROM\_WIN32(ERROR\_FILE\_NOT\_FOUND)**</dt> <dt>0x80070002</dt> </dl> | The virtual network file could not be found.<br/>                                         |
| <dl> <dt>**DISP\_E\_EXCEPTION**</dt> <dt>0x80020009</dt> </dl>                            | An unexpected error has occurred.<br/>                                                    |
| <dl> <dt>**VM\_E\_HARDWARE\_VIRTUALIZATION\_DISABLED**</dt> <dt>0xA0040951</dt> </dl>     | The processor does not support Hardware Accelerated Virtualization (HAV) extensions.<br/> |



 

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
| IID<br/>                      | IID\_IVMVirtualPC is defined as 236ba0d9-a24a-4292-a132-27c1421dfd01<br/>               |



## See also

<dl> <dt>

[**IVMVirtualPC**](ivmvirtualpc.md)
</dt> </dl>

 

