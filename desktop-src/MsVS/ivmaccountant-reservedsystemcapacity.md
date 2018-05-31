---
error-parsing-yaml: 
---

# IVMAccountant::ReservedSystemCapacity property

The **ReservedSystemCapacity** property contains the minimum percentage of system capacity assigned to this virtual machine.

This property is read-only.

## Syntax


```C++
HRESULT get_ReservedSystemCapacity(
  [out] VARIANT *reservedSystemCapacity
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
<td><pre><code>VMAccountant.ReservedSystemCapacity( _
  ByRef reservedSystemCapacity _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

The minimum percentage of system capacity that will always be available to this virtual machine. The minimum value for this parameter is 0, the maximum value depends on the number of host processors. The number is returned as a **Double** value.

This property value is read-only.

## Error codes



| Name                                                                                          | Meaning                                          |
|-----------------------------------------------------------------------------------------------|--------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>              | The operation was successful.<br/>         |
| <dl> <dt>E\_POINTER</dt> </dl>         | *reservedSystemCapacity* is **NULL**.<br/> |
| <dl> <dt>VM\_E\_VM\_UNKNOWN</dt> </dl> | Unknown virtual machine.<br/>              |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> </dl> | An unexpected error occurred.<br/>         |



## Remarks

In order to run a virtual machine, its reserved system capacity cannot exceed the value of [**IVMVirtualServer::AvailableSystemCapacity**](ivmvirtualserver-availablesystemcapacity.md).

## Examples

The following example prints the ReservedSystemCapacity property information for each virtual machine.


```VB
Set objVS = CreateObject("VirtualServer.Application")
set colVMs = objVS.VirtualMachines

For Each objVM in colVMS
    Set colAccountants = objVM.Accountant
        Wscript.Echo "Virtual machine: " & objVM.Name
        Wscript.Echo "Reserved system capacity: " & colAccountants.ReservedSystemCapacity
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

 

 





