---
title: IVMVirtualMachine RemoveConfigurationValue method (VPCCOMInterfaces.h)
description: Removes the value of the specified configuration setting for this virtual machine.
ms.assetid: 2d75a667-9656-4d4c-bafe-f3f8be3763f5
keywords:
- RemoveConfigurationValue method Virtual PC
- RemoveConfigurationValue method Virtual PC , IVMVirtualMachine interface
- IVMVirtualMachine interface Virtual PC , RemoveConfigurationValue method
topic_type:
- apiref
api_name:
- IVMVirtualMachine.RemoveConfigurationValue
api_location:
- VPCCOMInterfaces.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IVMVirtualMachine::RemoveConfigurationValue method

\[Windows Virtual PC is no longer available for use as of Windows 8. Instead, use the [Hyper-V WMI provider (V2)](/windows/desktop/HyperV_v2/windows-virtualization-portal).\]

Removes the value of the specified configuration setting for this virtual machine.

## Syntax


```C++
HRESULT RemoveConfigurationValue(
  [in] BSTR configurationKey
);
```



## Parameters

<dl> <dt>

*configurationKey* \[in\]
</dt> <dd>

The key used to identify the configuration value as stored in the "\*.vmc" file.

</dd> </dl>

## Return value

This method can return one of these values.



| Return code/value                                                                                                                                                      | Description                                    |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> <dt>0</dt> </dl>                            | The operation was successful.<br/>       |
| <dl> <dt>**E\_INVALIDARG**</dt> <dt>0x80000003</dt> </dl>           | The parameter is **NULL** or empty.<br/> |
| <dl> <dt>**VM\_E\_VM\_UNKNOWN**</dt> <dt>0xA0040207</dt> </dl>      | The configuration is unknown.<br/>       |
| <dl> <dt>**VM\_E\_PREF\_NOT\_FOUND**</dt> <dt>0xA0040300</dt> </dl> | The preference was not found.<br/>       |
| <dl> <dt>**DISP\_E\_EXCEPTION**</dt> <dt>0x80020009</dt> </dl>      | An unexpected error has occurred.<br/>   |



 

## Remarks

This method provides low-level access to any configuration value. It can be used to remove configuration values for customer-defined keys. Be careful if you use this method to remove system configuration values, since some values cannot be changed while the virtual machine is running.

Configuration keys are located in the virtual machine's "\*.vmc" file in XML format. The keys are stored in a hierarchical manner similar to the registry keys in Windows. To specify a specific subkey, a "key path" is constructed which specifies the various keys in a slash mark delimited format.

For example, to remove the value of the "ram\_size" key located in the following key tree:

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

For example, to remove the value of the "absolute" key located in the following key tree:

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

 

