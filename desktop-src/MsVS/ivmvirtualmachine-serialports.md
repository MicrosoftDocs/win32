---
error-parsing-yaml: 
---

# IVMVirtualMachine::SerialPorts property

The **SerialPorts** property contains an enumerable collection of serial ports.

This property is read-only.

## Syntax


```C++
HRESULT get_SerialPorts(
  [out] IVMSerialPortCollection **serialPortCollection
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
<td><pre><code>VMVirtualMachine.SerialPorts( _
  ByRef serialPortCollection _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

The [**IVMSerialPortCollection**](ivmserialportcollection.md) object associated with this virtual machine.

This property value is read-only.

## Error codes



| Name                                                                                          | Meaning                                                      |
|-----------------------------------------------------------------------------------------------|--------------------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>              | The operation was successful.<br/>                     |
| <dl> <dt>E\_POINTER</dt> </dl>         | The *serialPortCollection* parameter is **NULL**.<br/> |
| <dl> <dt>VM\_E\_VM\_UNKNOWN</dt> </dl> | The configuration is unknown.<br/>                     |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> </dl> | An unexpected error has occurred.<br/>                 |



## Examples

The following example displays the number of serial ports attached to a [**VMVirtualMachine**](ivmvirtualmachine.md) object.


```VB
Set objVS = CreateObject("VirtualServer.Application")
Set objVM = objVS.FindVirtualMachine("Windows Server 2003")
Set colSers = objVM.SerialPorts

Wscript.Echo "VM Name: " & objVM.Name
WScript.Echo "Serial ports: " & colSers.Count
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

 

 





