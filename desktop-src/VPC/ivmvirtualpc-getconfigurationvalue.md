---
title: IVMVirtualPC GetConfigurationValue method (VPCCOMInterfaces.h)
description: Retrieves the value of the specified configuration setting.
ms.assetid: 4598b57c-9942-4b40-97b5-41ad9ec74bfa
keywords:
- GetConfigurationValue method Virtual PC
- GetConfigurationValue method Virtual PC , IVMVirtualPC interface
- IVMVirtualPC interface Virtual PC , GetConfigurationValue method
topic_type:
- apiref
api_name:
- IVMVirtualPC.GetConfigurationValue
api_location:
- VPCCOMInterfaces.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IVMVirtualPC::GetConfigurationValue method

\[Windows Virtual PC is no longer available for use as of Windows 8. Instead, use the [Hyper-V WMI provider (V2)](/windows/desktop/HyperV_v2/windows-virtualization-portal).\]

Retrieves the value of the specified configuration setting.

## Syntax


```C++
HRESULT GetConfigurationValue(
  [in]          BSTR    preferenceKey,
  [out, retval] VARIANT *preferenceValue
);
```



## Parameters

<dl> <dt>

*preferenceKey* \[in\]
</dt> <dd>

The key used to identify the preference, as stored in the configuration file.

</dd> <dt>

*preferenceValue* \[out, retval\]
</dt> <dd>

The preference value. This parameter may be one of the following **VARIANT** types: **VT\_ARRAY**\|**VT\_UI1** (raw bytes), **VT\_BSTR** (string), **VT\_I4** (integer), or **VT\_BOOL** (Boolean).

</dd> </dl>

## Return value

This method can return one of these values.



| Return code/value                                                                                                                                                                        | Description                                                                                     |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> <dt>0</dt> </dl>                                              | The operation was successful.<br/>                                                        |
| <dl> <dt>**E\_POINTER**</dt> <dt>0x80004003</dt> </dl>                                | The *preferenceKey* or *preferenceValue* parameter is **NULL**.<br/>                      |
| <dl> <dt>**VM\_E\_PREF\_NOT\_FOUND**</dt> <dt>0xa0040300</dt> </dl>                   | The preference was not found.<br/>                                                        |
| <dl> <dt>**VM\_E\_HARDWARE\_VIRTUALIZATION\_DISABLED**</dt> <dt>0xA0040951</dt> </dl> | The processor does not support Hardware Accelerated Virtualization (HAV) extensions.<br/> |
| <dl> <dt>**DISP\_E\_EXCEPTION**</dt> <dt>0x80020009</dt> </dl>                        | An unexpected error has occurred.<br/>                                                    |



 

## Remarks

This method provides low-level access to any preference value for the current user. It can be used to retrieve preference values for customer-defined keys.

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

 

