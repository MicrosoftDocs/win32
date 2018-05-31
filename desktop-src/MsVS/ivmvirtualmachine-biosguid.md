---
title: IVMVirtualMachine BIOSGUID property
description: The BIOSGUID property contains the BIOS GUID.
ms.assetid: cdc57fcf-f65c-40c5-9f10-435278cec7fb
keywords:
- BIOSGUID property Virtual Server
- BIOSGUID property Virtual Server , IVMVirtualMachine interface
- IVMVirtualMachine interface Virtual Server , BIOSGUID property
- BIOSGUID property Virtual Server , VMVirtualMachine class
- VMVirtualMachine class Virtual Server , BIOSGUID property
topic_type:
- apiref
api_name:
- IVMVirtualMachine.BIOSGUID
- IVMVirtualMachine.get_BIOSGUID
- IVMVirtualMachine.put_BIOSGUID
- VMVirtualMachine.BIOSGUID
api_location:
- VsComInterfaces.h
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IVMVirtualMachine::BIOSGUID property

The **BIOSGUID** property contains the BIOS **GUID**.

This property is read/write.

## Syntax


```C++
HRESULT put_BIOSGUID(
  [in]  BSTR biosGUID
);

HRESULT get_BIOSGUID(
  [out] BSTR *biosGUID
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
<td><pre><code>VMVirtualMachine.BIOSGUID( _
  ByRef biosGUID, _
  ByVal biosGUID _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

The BIOS **GUID**.

This property value is read/write.

## Error codes



| Name                                                                                          | Meaning                                                                 |
|-----------------------------------------------------------------------------------------------|-------------------------------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>              | The operation was successful.<br/>                                |
| <dl> <dt>E\_POINTER</dt> </dl>         | The *biosGUID* parameter is **NULL**.<br/>                        |
| <dl> <dt>E\_INVALIDARG</dt> </dl>      | The *biosGUID* parameter is not valid or is an empty string.<br/> |
| <dl> <dt>VM\_E\_VM\_UNKNOWN</dt> </dl> | The configuration is unknown.<br/>                                |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> </dl> | An unexpected error has occurred.<br/>                            |



## Remarks

This property will not contain valid information until after the virtual machine has started up for the first time. An empty string will be returned if it is read before the initial startup.

The BIOS **GUID** string is specified and returned using the following format (the actual value shown is only an example): **{a18ad063-1678-43cb-baea-c954b581578c}**. The left and right braces around the hex digits, as well as the hex digit groupings, are required.

## Examples

The following example displays the **BIOSGUID** property value of a [**VMVirtualMachine**](ivmvirtualmachine.md) object.


```VB
Set objVS = CreateObject("VirtualServer.Application")
Set objVM = objVS.FindVirtualMachine("Windows Server 2003")

Wscript.Echo "VM Name: " & objVM.Name
If objVM.BIOSGUID = "" Then
    WScript.Echo "BIOS GUID: [null]"
Else
    WScript.Echo "BIOS GUID: " & objVM.BIOSGUID
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

 

 





