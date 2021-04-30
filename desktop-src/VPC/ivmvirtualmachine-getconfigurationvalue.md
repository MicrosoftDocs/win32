---
title: IVMVirtualMachine GetConfigurationValue method (VPCCOMInterfaces.h)
description: Retrieves the value of the specified configuration setting for this virtual machine.
ms.assetid: fd3c509e-8a40-4828-b866-6bd2cb455ab2
keywords:
- GetConfigurationValue method Virtual PC
- GetConfigurationValue method Virtual PC , IVMVirtualMachine interface
- IVMVirtualMachine interface Virtual PC , GetConfigurationValue method
topic_type:
- apiref
api_name:
- IVMVirtualMachine.GetConfigurationValue
api_location:
- VPCCOMInterfaces.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IVMVirtualMachine::GetConfigurationValue method

\[Windows Virtual PC is no longer available for use as of Windows 8. Instead, use the [Hyper-V WMI provider (V2)](/windows/desktop/HyperV_v2/windows-virtualization-portal).\]

Retrieves the value of the specified configuration setting for this virtual machine.

## Syntax


```C++
HRESULT GetConfigurationValue(
  [in]          BSTR    configurationKey,
  [out, retval] VARIANT *configurationValue
);
```



## Parameters

<dl> <dt>

*configurationKey* \[in\]
</dt> <dd>

The key used to identify the configuration value as stored in the "\*.vmc" file.

</dd> <dt>

*configurationValue* \[out, retval\]
</dt> <dd>

The configuration value. This value can be one of the following **VARIANT** types: **VT\_ARRAY**\|**VT\_UI1** (raw bytes), **VT\_BSTR** (string), **VT\_I4** (integer), or **VT\_BOOL** (Boolean).

</dd> </dl>

## Return value

This method can return one of these values.



| Return code/value                                                                                                                                                      | Description                                                       |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> <dt>0</dt> </dl>                            | The operation was successful.<br/>                          |
| <dl> <dt>**E\_INVALIDARG**</dt> <dt>0x80000003</dt> </dl>           | The *configurationKey* parameter is **NULL** or empty.<br/> |
| <dl> <dt>**E\_POINTER**</dt> <dt>0x80004003</dt> </dl>              | The *configurationValue* parameter is **NULL**.<br/>        |
| <dl> <dt>**VM\_E\_VM\_UNKNOWN**</dt> <dt>0xA0040207</dt> </dl>      | The configuration is unknown.<br/>                          |
| <dl> <dt>**VM\_E\_PREF\_NOT\_FOUND**</dt> <dt>0xA0040300</dt> </dl> | The preference was not found.<br/>                          |
| <dl> <dt>**DISP\_E\_EXCEPTION**</dt> <dt>0x80020009</dt> </dl>      | An unexpected error has occurred.<br/>                      |



 

## Remarks

This method provides low-level access to any configuration value. It can be used to read configuration values for customer-defined keys.

Configuration keys are located in the virtual machine's "\*.vmc" file in XML format. The keys are stored in a hierarchical manner similar to the registry keys in Windows. To specify a specific subkey, a "key path" is constructed which specifies the various keys in a slash mark delimited format.

For example, to read the value of the "ram\_size" key located in the following key tree:

``` syntax
<hardware>
    <memory>
        <ram_size type="integer">128</ram_size>
```

The *configurationKey* path string would be specified as follows:

``` syntax
"hardware/memory/ram_size"
```

If any of the keys in the desired tree have an "id" attribute value, the attribute and its value is embedded in the *configurationKey* path string immediately after its associated configuration key using the following bracketed format: "\[@id="*id\_value*"\]".

For example, to read the value of the "absolute" key located in the following key tree:

``` syntax
<hardware>
    <pci_bus>
        <ide_adapter>
            <ide_controller id="1">
                <location id="0">
                    <pathname>
                        <absolute type="string">D</absolute>
```

The *configurationKey* path string would be specified as follows:

``` syntax
"hardware/pci_bus/ide_adapter/ide_controller[@id=1]/location[@id=0]/pathname/absolute"
```

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                                    |
| Minimum supported server<br/> | None supported<br/>                                                                     |
| End of client support<br/>    | Windows 7<br/>                                                                          |
| Product<br/>                  | Windows Virtual PC<br/>                                                                 |
| Header<br/>                   | <dl> <dt>VPCCOMInterfaces.h</dt> </dl> |
| IID<br/>                      | IID\_IVMVirtualMachine is defined as f7092aa1-33ed-4f78-a59f-c00adfc2edd7<br/>          |



## See also

<dl> <dt>

[**IVMVirtualMachine**](ivmvirtualmachine.md)
</dt> </dl>

 

