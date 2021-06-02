---
title: IVMVirtualPC RemoveConfigurationValue method (VPCCOMInterfaces.h)
description: Removes the value of the specified configuration setting.
ms.assetid: 07bafa5e-bf62-45bf-af4e-a66050f5afad
keywords:
- RemoveConfigurationValue method Virtual PC
- RemoveConfigurationValue method Virtual PC , IVMVirtualPC interface
- IVMVirtualPC interface Virtual PC , RemoveConfigurationValue method
topic_type:
- apiref
api_name:
- IVMVirtualPC.RemoveConfigurationValue
api_location:
- VPCCOMInterfaces.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IVMVirtualPC::RemoveConfigurationValue method

\[Windows Virtual PC is no longer available for use as of Windows 8. Instead, use the [Hyper-V WMI provider (V2)](/windows/desktop/HyperV_v2/windows-virtualization-portal).\]

Removes the value of the specified configuration setting.

## Syntax


```C++
HRESULT RemoveConfigurationValue(
  [in] BSTR preferenceKey
);
```



## Parameters

<dl> <dt>

*preferenceKey* \[in\]
</dt> <dd>

The key used to identify the preference, as stored in the configuration file.

</dd> </dl>

## Return value

This method can return one of these values.



| Return code/value                                                                                                                                                                        | Description                                                                                     |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> <dt>0</dt> </dl>                                              | The operation was successful.<br/>                                                        |
| <dl> <dt>**E\_POINTER**</dt> <dt>0x80004003</dt> </dl>                                | The *preferenceKey* parameter is **NULL**.<br/>                                           |
| <dl> <dt>**E\_INVALIDARG**</dt> <dt>0x80000003</dt> </dl>                             | The *preferenceKey* parameter is not valid or is an empty string.<br/>                    |
| <dl> <dt>**VM\_E\_PREF\_NOT\_FOUND**</dt> <dt>0xA0040300</dt> </dl>                   | The preference was not found.<br/>                                                        |
| <dl> <dt>**VM\_E\_HARDWARE\_VIRTUALIZATION\_DISABLED**</dt> <dt>0xA0040951</dt> </dl> | The processor does not support Hardware Accelerated Virtualization (HAV) extensions.<br/> |
| <dl> <dt>**DISP\_E\_EXCEPTION**</dt> <dt>0x80020009</dt> </dl>                        | An unexpected error has occurred.<br/>                                                    |



 

## Remarks

This method provides low-level access to any preference value for the current user. It can be used to remove preference values for customer-defined keys.

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

 

