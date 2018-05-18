---
title: \_IVMRCClientControlEvents OnSwitchedDisplay method
description: Called when the VMRC client switches to a different machine.
ms.assetid: 'dbe36d71-79d6-4e2b-90bb-de16ecf050d1'
keywords: ["OnSwitchedDisplay method Virtual Server", "OnSwitchedDisplay method Virtual Server , _IVMRCClientControlEvents interface", "_IVMRCClientControlEvents interface Virtual Server , OnSwitchedDisplay method", "OnSwitchedDisplay method Virtual Server , VMRCClientControl interface", "VMRCClientControl interface Virtual Server , OnSwitchedDisplay method"]
topic_type:
- apiref
api_name:
- _IVMRCClientControlEvents.OnSwitchedDisplay
- VMRCClientControl.OnSwitchedDisplay
api_type:
- COM
---

# \_IVMRCClientControlEvents::OnSwitchedDisplay method

The **OnSwitchedDisplay** method is called when the VMRC client switches to a different machine.

## Syntax


```C++
HRESULT OnSwitchedDisplay(
  [in] BSTR displayName
);
```



## Parameters

<dl> <dt>

*displayName* \[in\]
</dt> <dd>

The name of the virtual machine display.

</dd> </dl>

## Return value

A [**32-bit value**](hresult-codes-specific-to-the-virtual-server.md) that describes an error or warning.

## Remarks

This method is called when the VMRC display is switched from the administrative display to a virtual machine, from one virtual machine to another virtual machine, or from a virtual machine to the administrative display. The client program must implement this interface method to receive notification of the event originating from the [**IVMRCClientControl**](ivmrcclientcontrol.md) object.

## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |



## See also

<dl> <dt>

[**\_IVMRCClientControlEvents**](-ivmrcclientcontrolevents.md)
</dt> </dl>

 

 





