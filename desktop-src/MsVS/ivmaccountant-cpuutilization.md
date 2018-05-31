---
error-parsing-yaml: 
---

# IVMAccountant::CPUUtilization property

The **CPUUtilization** property contains the current CPU use of this virtual machine.

This property is read-only.

## Syntax


```C++
HRESULT get_CPUUtilization(
  [out] long *percentageUtilization
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
<td><pre><code>VMAccountant.CPUUtilization( _
  ByRef percentageUtilization _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

The current CPU use percentage of this virtual machine.

This property value is read-only.

## Error codes



| Name                                                                                          | Meaning                                         |
|-----------------------------------------------------------------------------------------------|-------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>              | The operation was successful.<br/>        |
| <dl> <dt> E\_POINTER</dt> </dl>        | *percentageUtilization* is **NULL**.<br/> |
| <dl> <dt>S\_FALSE</dt> </dl>           | The virtual machine is not running.<br/>  |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> </dl> | An unexpected error occurred.<br/>        |



## Examples

The following example prints the CPUUtilization property information for each virtual machine.


```VB
Set objVS = CreateObject("VirtualServer.Application")
set colVMs = objVS.VirtualMachines

For Each objVM in colVMS
    Set colAccountants = objVM.Accountant
        Wscript.Echo "Virtual machine: " & objVM.Name
        Wscript.Echo "CPU utilization: " & colAccountants.CPUUtilization
        Wscript.Echo
Next
```



## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



## See also

<dl> <dt>

[**IVMAccountant**](ivmaccountant.md)
</dt> </dl>

 

 





