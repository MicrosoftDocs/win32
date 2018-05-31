---
title: IVMSupportDriver Provider property
description: The Provider property contains the name of the driver's provider.
ms.assetid: 488e6568-3ab3-46dd-b34f-cfdd12abefe5
keywords:
- Provider property Virtual Server
- Provider property Virtual Server , IVMSupportDriver interface
- IVMSupportDriver interface Virtual Server , Provider property
- Provider property Virtual Server , VMSupportDriver interface
- VMSupportDriver interface Virtual Server , Provider property
topic_type:
- apiref
api_name:
- IVMSupportDriver.Provider
- IVMSupportDriver.get_Provider
- VMSupportDriver.Provider
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

# IVMSupportDriver::Provider property

The **Provider** property contains the name of the driver's provider.

This property is read-only.

## Syntax


```C++
HRESULT get_Provider(
  [out] BSTR *provider
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
<td><pre><code>VMSupportDriver.Provider( _
  ByRef provider _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

The driver's provider.

This property value is read-only.

## Error codes



| Name                                                                                          | Meaning                                                   |
|-----------------------------------------------------------------------------------------------|-----------------------------------------------------------|
| <dl> <dt> S\_OK</dt> </dl>             | The property value was retrieved successfully.<br/> |
| <dl> <dt>E\_POINTER</dt> </dl>         | The *provider* parameter is **NULL**.<br/>          |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> </dl> | An unknown error has occurred.<br/>                 |



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

 

 





