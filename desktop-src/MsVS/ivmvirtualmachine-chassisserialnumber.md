---
title: IVMVirtualMachine ChassisSerialNumber property
description: The ChassisSerialNumber property contains the chassis serial number.
ms.assetid: '9d4d2ce9-f4f1-48f4-9976-f3017b2be045'
keywords: ["ChassisSerialNumber property Virtual Server", "ChassisSerialNumber property Virtual Server , IVMVirtualMachine interface", "IVMVirtualMachine interface Virtual Server , ChassisSerialNumber property"]
topic_type:
- apiref
api_name:
- IVMVirtualMachine.ChassisSerialNumber
- IVMVirtualMachine.get_ChassisSerialNumber
- IVMVirtualMachine.put_ChassisSerialNumber
api_location:
- VsComInterfaces.h
api_type:
- COM
---

# IVMVirtualMachine::ChassisSerialNumber property

The **ChassisSerialNumber** property contains the chassis serial number.

This property is read/write.

## Syntax


```C++
HRESULT put_ChassisSerialNumber(
  [in]  BSTR chassisSerialNumber
);

HRESULT get_ChassisSerialNumber(
  [out] BSTR *chassisSerialNumber
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
<td><pre><code>.ChassisSerialNumber( _
  ByRef chassisSerialNumber, _
  ByVal chassisSerialNumber _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

The chassis serial number.

This property value is read/write.

## Error codes



| Name                                                                                          | Meaning                                                                                                      |
|-----------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>              | The operation was successful.<br/>                                                                     |
| <dl> <dt>E\_POINTER</dt> </dl>         | The *chassisSerialNumber* parameter is **NULL**.<br/>                                                  |
| <dl> <dt>E\_INVALIDARG</dt> </dl>      | The *chassisSerialNumber* parameter is greater than 32 characters, an empty string, or not valid.<br/> |
| <dl> <dt>VM\_E\_VM\_RUNNING</dt> </dl> | The serial number cannot be set while the virtual machine is running.<br/>                             |
| <dl> <dt>VM\_E\_VM\_UNKNOWN</dt> </dl> | The configuration is unknown.<br/>                                                                     |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> </dl> | An unexpected error has occurred.<br/>                                                                 |



## Remarks

This property will not contain valid information until after the virtual machine has started up for the first time. An empty string will be returned if it is read before the initial startup.

## Examples

The following example displays the **ChassisSerialNumber** property value of a [**VMVirtualMachine**](ivmvirtualmachine.md) object.


```VB
Set objVS = CreateObject("VirtualServer.Application")
Set objVM = objVS.FindVirtualMachine("Windows Server 2003")

Wscript.Echo "VM Name: " & objVM.Name
If objVM.ChassisSerialNumber = "" Then
  WScript.Echo "Chassis serial number: [null]"
Else
  WScript.Echo "Chassis serial number: " & objVM.ChassisSerialNumber
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

 

 





