---
title: IVMVirtualMachine Display property
description: The Display property contains the video display for the virtual machine.
ms.assetid: 'd8ec1d5f-1880-41d8-bb6a-7c907b2aa8ed'
keywords: ["Display property Virtual Server", "Display property Virtual Server , IVMVirtualMachine interface", "IVMVirtualMachine interface Virtual Server , Display property", "Display property Virtual Server , VMVirtualMachine class", "VMVirtualMachine class Virtual Server , Display property"]
topic_type:
- apiref
api_name:
- IVMVirtualMachine.Display
- IVMVirtualMachine.get_Display
- VMVirtualMachine.Display
api_location:
- VsComInterfaces.h
api_type:
- COM
---

# IVMVirtualMachine::Display property

The **Display** property contains the video display for the virtual machine.

This property is read-only.

## Syntax


```C++
HRESULT get_Display(
  [out] IVMDisplay **display
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
<td><pre><code>VMVirtualMachine.Display( _
  ByRef display _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

The [**VMDisplay**](ivmdisplay.md) object associated with this virtual machine.

This property value is read-only.

## Error codes



| Name                                                                                          | Meaning                                         |
|-----------------------------------------------------------------------------------------------|-------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>              | The operation was successful.<br/>        |
| <dl> <dt>E\_POINTER</dt> </dl>         | The *display* parameter is **NULL**.<br/> |
| <dl> <dt>VM\_E\_VM\_UNKNOWN</dt> </dl> | The configuration is unknown.<br/>        |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> </dl> | An unexpected error has occurred.<br/>    |



## Examples

The following example displays the height and width of the [**VMDisplay**](ivmdisplay.md) object associated with a [**VMVirtualMachine**](ivmvirtualmachine.md) object.


```VB
Set objVS = CreateObject("VirtualServer.Application")
Set objVM = objVS.FindVirtualMachine("Windows Server 2003")
Set objDisplay = objVM.Display

Wscript.Echo "VM Name: " & objVM.Name
WScript.Echo "Display Dimensions: " & objDisplay.Width & "x" & objDisplay.Height
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

 

 





