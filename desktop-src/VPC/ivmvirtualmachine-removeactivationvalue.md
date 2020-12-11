---
title: IVMVirtualMachine RemoveActivationValue method (VPCCOMInterfaces.h)
description: Removes the value of the specified activation setting for this virtual machine.
ms.assetid: 8e9b9d95-aec9-4b73-afc3-cd0d7300f40f
keywords:
- RemoveActivationValue method Virtual PC
- RemoveActivationValue method Virtual PC , IVMVirtualMachine interface
- IVMVirtualMachine interface Virtual PC , RemoveActivationValue method
topic_type:
- apiref
api_name:
- IVMVirtualMachine.RemoveActivationValue
api_location:
- VPCCOMInterfaces.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IVMVirtualMachine::RemoveActivationValue method

\[Windows Virtual PC is no longer available for use as of Windows 8. Instead, use the [Hyper-V WMI provider (V2)](/windows/desktop/HyperV_v2/windows-virtualization-portal).\]

Removes the value of the specified activation setting for this virtual machine.

## Syntax


```C++
HRESULT RemoveActivationValue(
  [in] BSTR activationKey
);
```



## Parameters

<dl> <dt>

*activationKey* \[in\]
</dt> <dd>

The key used to identify the activation value as stored in the "\*.vmc" file.

</dd> </dl>

## Return value

This method can return one of these values.



| Return code/value                                                                                                                                                      | Description                                                                             |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> <dt>0</dt> </dl>                            | The operation was successful.<br/>                                                |
| <dl> <dt>**E\_INVALIDARG**</dt> <dt>0x80000003</dt> </dl>           | The parameter is **NULL** or empty.<br/>                                          |
| <dl> <dt>**VM\_E\_VM\_UNKNOWN**</dt> <dt>0xA0040207</dt> </dl>      | The configuration is unknown.<br/>                                                |
| <dl> <dt>**VM\_E\_PREF\_NOT\_FOUND**</dt> <dt>0xA0040300</dt> </dl> | The preference was not found, or this configuration has no valid activation.<br/> |
| <dl> <dt>**DISP\_E\_EXCEPTION**</dt> <dt>0x80020009</dt> </dl>      | An unexpected error has occurred.<br/>                                            |



 

## Remarks

This method provides low-level access to any activation value. It can be used to remove activation values for customer-defined keys. Be careful if you use this method to remove system activation values, since some values cannot be changed while the virtual machine is running. When a virtual machine is started, a copy is made of its configuration values, which becomes its set of activation values. Activation values are maintained until the virtual machine is shut down or restarted. Note that Windows Virtual PC may only use the configuration to store values for certain keys, that is, the activation value may never be used.

> [!Note]  
> The virtual machine session must be running before any activation values can be changed.

 

Activation keys are stored internally in a hierarchical manner similar to the registry keys in Windows. To specify a specific subkey, a "key path" is constructed which specifies the various keys in a slash mark delimited format.

For example, to remove the value of the "default\_action" key located in the following key tree:

``` syntax
<settings>
    <undo_drives>
        <default_action type="integer">1</default_action>
```

The *activationKey* path string would be specified as follows:

``` syntax
"settings/undo_drives/default_action"
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

 

