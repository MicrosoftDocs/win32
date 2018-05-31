---
error-parsing-yaml: 
---

# IVMVirtualMachine::UndoAction property

The **UndoAction** property contains the default action to be performed on all undo drives when the virtual machine is shut down from within the guest operating system.

This property is read/write.

## Syntax


```C++
HRESULT put_UndoAction(
  [in]  VMUndoAction undoAction
);

HRESULT get_UndoAction(
  [out] VMUndoAction *undoAction
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
<td><pre><code>VMVirtualMachine.UndoAction( _
  ByRef undoAction, _
  ByVal undoAction _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

The default action to be performed on all undo drives when the virtual machine is shut down from within the guest operating system.

This property value is read/write.

## Error codes



| Name                                                                                          | Meaning                                             |
|-----------------------------------------------------------------------------------------------|-----------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>              | The operation was successful.<br/>            |
| <dl> <dt>E\_POINTER</dt> </dl>         | The *undoAction* parameter is **NULL**.<br/>  |
| <dl> <dt>E\_INVALIDARG</dt> </dl>      | The *undoAction* parameter is not valid.<br/> |
| <dl> <dt>VM\_E\_VM\_UNKNOWN</dt> </dl> | The configuration is unknown.<br/>            |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> </dl> | An unexpected error has occurred.<br/>        |



## Remarks

See the [**VMUndoAction**](vmundoaction.md) enumeration for descriptions of the allowable *undoAction* values.

## Examples

The following example displays the **UndoAction** property value of a [**VMVirtualMachine**](ivmvirtualmachine.md) object.


```VB
Set objVS = CreateObject("VirtualServer.Application")
Set objVM = objVS.FindVirtualMachine("Windows Server 2003")

WScript.Echo "VM Name: " & objVM.Name
WScript.Echo "Undo action: " & objVM.UndoAction
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
</dt> <dt>

[**VMUndoAction**](vmundoaction.md)
</dt> </dl>

 

 





