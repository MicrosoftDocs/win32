---
title: IVMVirtualMachine RemoveActivationValue method
description: The RemoveActivationValue method removes the value of the specified activation setting for this virtual machine.
ms.assetid: 8b23eb9a-445f-4ff6-9a69-b8a8e898c938
keywords:
- RemoveActivationValue method Virtual Server
- RemoveActivationValue method Virtual Server , IVMVirtualMachine interface
- IVMVirtualMachine interface Virtual Server , RemoveActivationValue method
topic_type:
- apiref
api_name:
- IVMVirtualMachine.RemoveActivationValue
api_location:
- VsComInterfaces.h
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IVMVirtualMachine::RemoveActivationValue method

The **RemoveActivationValue** method removes the value of the specified activation setting for this virtual machine.

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

Key used to identify the activation value as stored in the "\*.vmc" file.

</dd> </dl>

## Return value

This method can return one of these values.

This method supports standard return values, as well as the following. For information on Virtual Server specific return values not listed below, see [**HRESULT Codes Specific to the Virtual Server**](hresult-codes-specific-to-the-virtual-server.md).



| Return code                                                                                            | Description                                                                             |
|--------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                   | The operation was successful.<br/>                                                |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>           | The *activationKey* parameter is **NULL** or empty.<br/>                          |
| <dl> <dt>**VM\_E\_VM\_UNKNOWN**</dt> </dl>      | The configuration is unknown.<br/>                                                |
| <dl> <dt>**VM\_E\_PREF\_NOT\_FOUND**</dt> </dl> | The preference was not found, or this configuration has no valid activation.<br/> |
| <dl> <dt>**DISP\_E\_EXCEPTION**</dt> </dl>      | An unexpected error has occurred.<br/>                                            |



 

## Remarks

This method provides low-level access to any activation value. It can be used to remove activation values for customer-defined keys. Be careful if you use this method to remove system activation values, since some values cannot be changed while the virtual machine is running. When a virtual machine is started, a copy is made of its configuration values, which becomes its set of activation values. Activation values are maintained until the virtual machine is shut down or restarted. Note that Virtual Server may only use the configuration to store values for certain keys, that is, the activation value may never be used.

> [!Note]  
> The virtual machine session must be running before any activation values can be changed.

 

Activation keys are stored internally in a hierarchical manner similar to the registry keys in Windows. To specify a specific subkey, a "key path" is constructed which specifies the various keys in a slash mark delimited format.

For example, to remove the value of the "default\_action" key located in the following key tree:

``` syntax
<settings>
    <undo_drives>
        <default_action type="integer">1</ram_size>
```

The *activationKey* path string would be specified as follows:

``` syntax
"settings/undo_drives/default_action"
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

 

 





