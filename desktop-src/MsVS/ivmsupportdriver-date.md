---
title: IVMSupportDriver Date property
description: The Date property contains the build date of the driver.
ms.assetid: 09c62e2c-998f-4569-8006-a8c66268c353
keywords:
- Date property Virtual Server
- Date property Virtual Server , IVMSupportDriver interface
- IVMSupportDriver interface Virtual Server , Date property
- Date property Virtual Server , VMSupportDriver interface
- VMSupportDriver interface Virtual Server , Date property
topic_type:
- apiref
api_name:
- IVMSupportDriver.Date
- IVMSupportDriver.get_Date
- VMSupportDriver.Date
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

# IVMSupportDriver::Date property

The **Date** property contains the build date of the driver.

This property is read-only.

## Syntax


```C++
HRESULT get_Date(
  [out] BSTR *date
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
<td><pre><code>VMSupportDriver.Date( _
  ByRef date _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

The driver's build date. The date is given in the default locale's short date form. For example in U.S. English, the date is in the form "mm/dd/yyyy".

This property value is read-only.

## Error codes



| Name                                                                                          | Meaning                                                   |
|-----------------------------------------------------------------------------------------------|-----------------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>              | The property value was retrieved successfully.<br/> |
| <dl> <dt> E\_POINTER</dt> </dl>        | *date* is **NULL**.<br/>                            |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> </dl> | An unknown error has occurred.<br/>                 |



## Remarks

The driver's date information is only valid when the driver has been qualified and digitally signed by Microsoft's Windows Hardware Quality Lab (WHQL). If the driver has not been qualified, this property returns an empty string.

## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



## See also

<dl> <dt>

[**IVMSupportDriver**](ivmsupportdriver.md)
</dt> </dl>

 

 





