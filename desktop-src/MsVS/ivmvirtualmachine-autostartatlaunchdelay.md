---
title: IVMVirtualMachine AutoStartAtLaunchDelay property
description: The AutoStartAtLaunchDelay property contains the delay in seconds to use when this virtual machine is started up automatically when Virtual Server is launched.
ms.assetid: '37a9e66f-dbf1-43c4-9010-7f7699b159dc'
keywords: ["AutoStartAtLaunchDelay property Virtual Server", "AutoStartAtLaunchDelay property Virtual Server , IVMVirtualMachine interface", "IVMVirtualMachine interface Virtual Server , AutoStartAtLaunchDelay property", "AutoStartAtLaunchDelay property Virtual Server , VMVirtualMachine class", "VMVirtualMachine class Virtual Server , AutoStartAtLaunchDelay property"]
topic_type:
- apiref
api_name:
- IVMVirtualMachine.AutoStartAtLaunchDelay
- IVMVirtualMachine.get_AutoStartAtLaunchDelay
- IVMVirtualMachine.put_AutoStartAtLaunchDelay
- VMVirtualMachine.AutoStartAtLaunchDelay
api_location:
- VsComInterfaces.h
api_type:
- COM
---

# IVMVirtualMachine::AutoStartAtLaunchDelay property

The **AutoStartAtLaunchDelay** property contains the delay in seconds to use when this virtual machine is started up automatically when Virtual Server is launched.

This property is read/write.

## Syntax


```C++
HRESULT put_AutoStartAtLaunchDelay(
  [in]  long autoStartAtLaunchDelay
);

HRESULT get_AutoStartAtLaunchDelay(
  [out] long *autoStartAtLaunchDelay
);
```

<span codelanguage="VisualBasic"></span>

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>VB</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><pre><code>VMVirtualMachine.AutoStartAtLaunchDelay( _
  ByRef autoStartAtLaunchDelay, _
  ByVal autoStartAtLaunchDelay _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

The delay in seconds.

This property value is read/write.

## Error codes



| Name                                                                                          | Meaning                                                                                |
|-----------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>              | The operation was successful.<br/>                                               |
| <dl> <dt>E\_POINTER</dt> </dl>         | The *autoStartAtLaunchDelay* parameter is **NULL** or is not a valid value.<br/> |
| <dl> <dt>VM\_E\_VM\_UNKNOWN</dt> </dl> | The configuration is unknown.<br/>                                               |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> </dl> | An unexpected error has occurred.<br/>                                           |



## Remarks

By default, the value of this property is 0 and there is no delay.

## Examples

The following example displays the **AutoStartAtLaunchDelay** property value of a [**IVMVirtualMachine**](ivmvirtualmachine.md) object.


```VB
Set objVS = CreateObject("VirtualServer.Application")
Set objVM = objVS.FindVirtualMachine("Windows Server 2003")

Wscript.Echo "VM Name: " & objVM.Name
WScript.Echo "Autostart at launch delay: " & objVM.AutoStartAtLaunchDelay
```



## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



## See also

<dl> <dt>

[**IVMVirtualMachine**](ivmvirtualmachine.md)
</dt> </dl>

 

 





