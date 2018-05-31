---
title: IVMVirtualMachineEvents OnConfigurationChanged method
description: Called when a value in the configuration for this virtual machine has changed.
ms.assetid: 9f91c164-385c-4d1a-998b-2f049b4acbf0
keywords:
- OnConfigurationChanged method Virtual Server
- OnConfigurationChanged method Virtual Server , IVMVirtualMachineEvents interface
- IVMVirtualMachineEvents interface Virtual Server , OnConfigurationChanged method
topic_type:
- apiref
api_name:
- IVMVirtualMachineEvents.OnConfigurationChanged
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

# IVMVirtualMachineEvents::OnConfigurationChanged method

The **OnConfigurationChanged** method is called when a value in the configuration for this virtual machine has changed.

## Syntax


```C++
HRESULTS OnConfigurationChanged(
  [in] BSTR    configKey,
  [in] VARIANT configData
);
```



## Parameters

<dl> <dt>

*configKey* \[in\]
</dt> <dd>

The value inside the configuration that has changed.

</dd> <dt>

*configData* \[in\]
</dt> <dd>

The new value for the configuration.

</dd> </dl>

## Return value

A [**32-bit value**](hresult-codes-specific-to-the-virtual-server.md) that describes an error or warning.

## Remarks

This method is called when the configuration changes for this virtual machine. The client program must implement this interface method to receive notification of the [**vmVirtualMachineEvent\_ConfigurationChanged**](vmvirtualmachineevents.md) event originating from [**IVMVirtualMachine**](ivmvirtualmachine.md).

## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



## See also

<dl> <dt>

[**IVMVirtualMachineEvents**](ivmvirtualmachineevents.md)
</dt> </dl>

 

 





