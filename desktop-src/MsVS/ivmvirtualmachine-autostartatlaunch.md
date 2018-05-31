---
error-parsing-yaml: 
---

# IVMVirtualMachine::AutoStartAtLaunch property

The **AutoStartAtLaunch** property contains whether this virtual machine will start up automatically when Virtual Server is launched.

This property is read/write.

## Syntax


```C++
HRESULT put_AutoStartAtLaunch(
  [in]  VMAutoStartType autoStartAtLaunch
);

HRESULT get_AutoStartAtLaunch(
  [out] VMAutoStartType *autoStartAtLaunch
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
<td><pre><code>VMVirtualMachine.AutoStartAtLaunch( _
  ByRef autoStartAtLaunch, _
  ByVal autoStartAtLaunch _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

Contains a flag indicating whether this virtual machine will start up automatically when Virtual Server is launched.

This property value is read/write.

## Error codes



| Name                                                                                          | Meaning                                                                                                                                            |
|-----------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>              | The operation was successful.<br/>                                                                                                           |
| <dl> <dt>E\_POINTER</dt> </dl>         | The *autoStartAtLaunch* parameter is **NULL**.<br/>                                                                                          |
| <dl> <dt>E\_INVALIDARG</dt> </dl>      | The *autoStartAtLaunch* parameter is not valid.<br/>                                                                                         |
| <dl> <dt>E\_FAIL</dt> </dl>            | The [**RunAsDefinedAccount**](ivmvirtualmachine-runasdefinedaccount.md) property must be set to **TRUE** in order to enable AutoStart.<br/> |
| <dl> <dt>VM\_E\_VM\_UNKNOWN</dt> </dl> | The configuration is unknown.<br/>                                                                                                           |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> </dl> | An unexpected error has occurred.<br/>                                                                                                       |



## Remarks

By default, a virtual machine will start up automatically if it was running when Virtual Server was quit.

## Examples

The following example displays the **AutoStartAtLaunch** property value of a [**IVMVirtualMachine**](ivmvirtualmachine.md) object.


```VB
Set objVS = CreateObject("VirtualServer.Application")
Set objVM = objVS.FindVirtualMachine("Windows Server 2003")

Wscript.Echo "VM Name: " & objVM.Name
WScript.Echo "Autostart at launch: " & objVM.AutoStartAtLaunch
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

[**VMAutoStartType**](vmautostarttype.md)
</dt> </dl>

 

 





