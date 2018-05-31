---
error-parsing-yaml: 
---

# IVMVirtualMachine::AttachedDriveTypes property

The **AttachedDriveTypes** property contains an array indicating the type of drive attached to each location in the virtual machine.

This property is read-only.

## Syntax


```C++
HRESULT get_AttachedDriveTypes(
  [out] VARIANT *driveTypes
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
<td><pre><code>VMVirtualMachine.AttachedDriveTypes( _
  ByRef driveTypes _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

Contains an array of **Byte** objects representing the [**VMDriveType**](vmdrivetype.md) of each device connected to every bus location. The array is ordered by \[busType\]\[busNumber\]\[deviceID\].

This property value is read-only.

## Error codes



| Name                                                                                          | Meaning                                            |
|-----------------------------------------------------------------------------------------------|----------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>              | The operation was successful.<br/>           |
| <dl> <dt>E\_POINTER</dt> </dl>         | The *driveTypes* parameter is **NULL**.<br/> |
| <dl> <dt>VM\_E\_VM\_UNKNOWN</dt> </dl> | The configuration is unknown.<br/>           |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> </dl> | An unexpected error has occurred.<br/>       |



## Examples

The following example displays the **AttachedDriveTypes** property value array of a [**VMVirtualMachine**](ivmvirtualmachine.md) object.


```VB
Set objVS = CreateObject("VirtualServer.Application")
Set objVM = objVS.FindVirtualMachine("Windows Server 2003")

Wscript.Echo "VM Name: " & objVM.Name

Set colDrives = objVM.AttachedDriveTypes

WScript.Echo "Attached Drives: "
For Each objDrive in colDrives
  If objDrive = 2 Then
    Wscript.Echo "  DVD/CDROM disc drive attached"
  Elseif objDrive = 1 Then
    Wscript.Echo "  Hard disk drive attached"
  Else
    Wscript.Echo "  (no drive attachment)"
  End If
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

[**IVMVirtualMachine**](ivmvirtualmachine.md)
</dt> </dl>

 

 





