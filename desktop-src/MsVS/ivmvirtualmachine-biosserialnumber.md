---
title: IVMVirtualMachine BIOSSerialNumber property
description: The BIOSSerialNumber property contains the BIOS serial number.
ms.assetid: 'c7ca4b90-ae87-4f83-b881-564f32463fbd'
keywords: ["BIOSSerialNumber property Virtual Server", "BIOSSerialNumber property Virtual Server , IVMVirtualMachine interface", "IVMVirtualMachine interface Virtual Server , BIOSSerialNumber property", "BIOSSerialNumber property Virtual Server , VMVirtualMachine class", "VMVirtualMachine class Virtual Server , BIOSSerialNumber property"]
topic_type:
- apiref
api_name:
- IVMVirtualMachine.BIOSSerialNumber
- IVMVirtualMachine.get_BIOSSerialNumber
- IVMVirtualMachine.put_BIOSSerialNumber
- VMVirtualMachine.BIOSSerialNumber
api_location:
- VsComInterfaces.h
api_type:
- COM
---

# IVMVirtualMachine::BIOSSerialNumber property

The **BIOSSerialNumber** property contains the BIOS serial number.

This property is read/write.

## Syntax


```C++
HRESULT put_BIOSSerialNumber(
  [in]  BSTR biosSerialNumber
);

HRESULT get_BIOSSerialNumber(
  [out] BSTR *biosSerialNumber
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
<td><pre><code>VMVirtualMachine.BIOSSerialNumber( _
  ByRef biosSerialNumber, _
  ByVal biosSerialNumber _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

The BIOS serial number.

This property value is read/write.

## Error codes



| Name                                                                                          | Meaning                                                                                                   |
|-----------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>              | The operation was successful.<br/>                                                                  |
| <dl> <dt>E\_POINTER</dt> </dl>         | The *biosSerialNumber* parameter is **NULL**.<br/>                                                  |
| <dl> <dt>E\_INVALIDARG</dt> </dl>      | The *biosSerialNumber* parameter is greater than 32 characters, an empty string, or not valid.<br/> |
| <dl> <dt>VM\_E\_VM\_RUNNING</dt> </dl> | The serial number cannot be set while the virtual machine is running.<br/>                          |
| <dl> <dt>VM\_E\_VM\_UNKNOWN</dt> </dl> | The configuration is unknown.<br/>                                                                  |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> </dl> | An unexpected error has occurred.<br/>                                                              |



## Remarks

This property will not contain valid information until after the virtual machine has started up for the first time. An empty string will be returned if it is read before the initial startup.

## Examples

The following example displays the **BIOSSerialNumber** property value of a [**VMVirtualMachine**](ivmvirtualmachine.md) object.


```VB
Set objVS = CreateObject("VirtualServer.Application")
Set objVM = objVS.FindVirtualMachine("Windows Server 2003")

Wscript.Echo "VM Name: " & objVM.Name
If objVM.BIOSSerialNumber = "" Then
    WScript.Echo "BIOS serial number: [null]"
Else
    WScript.Echo "BIOS serial number: " & objVM.BIOSSerialNumber
End If
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

 

 





