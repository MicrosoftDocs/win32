---
error-parsing-yaml: 
---

# IVMAccountant::CPUUtilizationHistory property

The **CPUUtilizationHistory** property contains an array of percentage values that specify the recent CPU use of this virtual machine.

This property is read-only.

## Syntax


```C++
HRESULT get_CPUUtilizationHistory(
  [out] VARIANT *percentageUtilization
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
<td><pre><code>VMAccountant.CPUUtilizationHistory( _
  ByRef percentageUtilization _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

The recent CPU use of this virtual machine. This use data is returned as a **Byte** array of 60 elements that represent the percentage of CPU use at each second over the past minute.

This property value is read-only.

## Error codes



| Name                                                                                          | Meaning                                                                                                           |
|-----------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>              | The operation was successful.<br/>                                                                          |
| <dl> <dt>E\_POINTER</dt> </dl>         | *percentageUtilization* is **NULL**.<br/>                                                                   |
| <dl> <dt> S\_FALSE</dt> </dl>          | The virtual machine is not running (array is still returned with all 60 values set to 0 in this case).<br/> |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> </dl> | An unexpected error occurred.<br/>                                                                          |



## Examples

The following example prints the CPUUtilizationHistory property information for each virtual machine.


```VB
Set objVS = CreateObject("VirtualServer.Application")
set colVMs = objVS.VirtualMachines

For Each objVM in colVMS
    Set colAccountants = objVM.Accountant
        Wscript.Echo "Virtual machine: " & objVM.Name
        i = 1
        Wscript.Echo "CPU utilization history:"
        For Each intCPUUtilization in colAccountants.CPUUtilizationHistory
            Wscript.Echo vbTab & i & " -- " & intCPUUtilization
            i = i + 1
        Next
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

 

 





