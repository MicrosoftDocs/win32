---
title: IVMVirtualMachine BaseBoardSerialNumber property
description: The BaseBoardSerialNumber property contains the base board serial number.
ms.assetid: 012f9bb5-292e-4161-a508-bdcbe4045104
keywords:
- BaseBoardSerialNumber property Virtual Server
- BaseBoardSerialNumber property Virtual Server , IVMVirtualMachine interface
- IVMVirtualMachine interface Virtual Server , BaseBoardSerialNumber property
- BaseBoardSerialNumber property Virtual Server , VMVirtualMachine class
- VMVirtualMachine class Virtual Server , BaseBoardSerialNumber property
topic_type:
- apiref
api_name:
- IVMVirtualMachine.BaseBoardSerialNumber
- IVMVirtualMachine.get_BaseBoardSerialNumber
- IVMVirtualMachine.put_BaseBoardSerialNumber
- VMVirtualMachine.BaseBoardSerialNumber
api_location:
- VsComInterfaces.h
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IVMVirtualMachine::BaseBoardSerialNumber property

The **BaseBoardSerialNumber** property contains the base board serial number.

This property is read/write.

## Syntax


```C++
HRESULT put_BaseBoardSerialNumber(
  [in]  BSTR baseBoardSerialNumber
);

HRESULT get_BaseBoardSerialNumber(
  [out] BSTR *baseBoardSerialNumber
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
<td><pre><code>VMVirtualMachine.BaseBoardSerialNumber( _
  ByRef baseBoardSerialNumber, _
  ByVal baseBoardSerialNumber _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

The base board serial number.

This property value is read/write.

## Error codes



| Name                                                                                          | Meaning                                                                                                        |
|-----------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>              | The operation was successful.<br/>                                                                       |
| <dl> <dt>E\_POINTER</dt> </dl>         | The *baseBoardSerialNumber* parameter is **NULL**.<br/>                                                  |
| <dl> <dt>E\_INVALIDARG</dt> </dl>      | The *baseBoardSerialNumber* parameter is greater than 32 characters, an empty string, or not valid.<br/> |
| <dl> <dt>VM\_E\_VM\_RUNNING</dt> </dl> | The serial number cannot be set while the virtual machine is running.<br/>                               |
| <dl> <dt>VM\_E\_VM\_UNKNOWN</dt> </dl> | The configuration is unknown.<br/>                                                                       |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> </dl> | An unexpected error has occurred.<br/>                                                                   |



## Remarks

This property will not contain valid information until after the virtual machine has started up for the first time. An empty string will be returned if it is read before the initial startup.

## Examples

The following example displays the **BaseBoardSerialNumber** property value of a [**IVMVirtualMachine**](ivmvirtualmachine.md) object.


```VB
Set objVS = CreateObject("VirtualServer.Application")
Set objVM = objVS.FindVirtualMachine("Windows Server 2003")

Wscript.Echo "VM Name: " & objVM.Name

If objVM.BaseBoardSerialNumber = "" Then
  Wscript.Echo "Baseboard serial number: [null]"
Else
  WScript.Echo "Baseboard serial number: " & objVM.BaseBoardSerialNumber
End If
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

 

 





