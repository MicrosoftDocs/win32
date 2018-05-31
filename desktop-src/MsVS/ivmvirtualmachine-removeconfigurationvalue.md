---
title: IVMVirtualMachine RemoveConfigurationValue method
description: The RemoveConfigurationValue method removes the value of the specified configuration setting for this virtual machine.
ms.assetid: a36af3cd-04e1-42a9-98e7-ee807afe046b
keywords:
- RemoveConfigurationValue method Virtual Server
- RemoveConfigurationValue method Virtual Server , IVMVirtualMachine interface
- IVMVirtualMachine interface Virtual Server , RemoveConfigurationValue method
topic_type:
- apiref
api_name:
- IVMVirtualMachine.RemoveConfigurationValue
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
api_location:
- VsComInterfaces.h
api_type:
- COM
---

# IVMVirtualMachine::RemoveConfigurationValue method

The **RemoveConfigurationValue** method removes the value of the specified configuration setting for this virtual machine.

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

Key used to identify the configuration value as stored in the "\*.vmc" file.

</dd> </dl>

## Return value

This method can return one of these values.

This method supports standard return values, as well as the following. For information on Virtual Server specific return values not listed below, see [**HRESULT Codes Specific to the Virtual Server**](hresult-codes-specific-to-the-virtual-server.md).



| Return code                                                                                            | Description                                                       |
|--------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                   | The operation was successful.<br/>                          |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>           | The *configurationKey* parameter is **NULL** or empty.<br/> |
| <dl> <dt>**VM\_E\_VM\_UNKNOWN**</dt> </dl>      | The configuration is unknown.<br/>                          |
| <dl> <dt>**VM\_E\_PREF\_NOT\_FOUND**</dt> </dl> | The preference was not found.<br/>                          |
| <dl> <dt>**DISP\_E\_EXCEPTION**</dt> </dl>      | An unexpected error has occurred.<br/>                      |



 

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



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



## See also

<dl> <dt>

[**IVMVirtualMachine**](ivmvirtualmachine.md)
</dt> </dl>

 

 





