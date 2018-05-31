---
error-parsing-yaml: 
---

# IVMVirtualMachine::Mouse property

The **Mouse** property contains the mouse device for the virtual machine.

This property is read-only.

## Syntax


```C++
HRESULT get_Mouse(
  [out] IVMMouse **mouse
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
<td><pre><code>VMVirtualMachine.Mouse( _
  ByRef mouse _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

The [**VMMouse**](ivmmouse.md) object associated with this virtual machine.

This property value is read-only.

## Error codes



| Name                                                                                               | Meaning                                         |
|----------------------------------------------------------------------------------------------------|-------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>                   | The operation was successful.<br/>        |
| <dl> <dt>E\_POINTER</dt> </dl>              | The *mouse* parameter is **NULL**.<br/>   |
| <dl> <dt>VM\_E\_VM\_UNKNOWN</dt> </dl>      | The configuration is unknown.<br/>        |
| <dl> <dt>VM\_E\_VM\_NOT\_RUNNING</dt> </dl> | The virtual machine must be running.<br/> |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> </dl>      | An unexpected error has occurred.<br/>    |



## Examples

The following example accesses the [**VMMouse**](ivmmouse.md) object of a [**VMVirtualMachine**](ivmvirtualmachine.md) object and sends a left click to the VM.


```VB
Set objVS = CreateObject("VirtualServer.Application")
Set objVM = objVS.FindVirtualMachine("Windows Server 2003")
Set objMouse = objVM.Mouse

Wscript.Echo "VM Name: " & objVM.Name
Wscript.Echo "  Clicking left mouse button"
objMouse.Click(1)
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

 

 





