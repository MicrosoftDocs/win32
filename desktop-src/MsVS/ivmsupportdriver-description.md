---
title: IVMSupportDriver Description property
description: The Description property contains the driver's description.
ms.assetid: fa104c23-8b0e-4e66-8c82-887df069714d
keywords:
- Description property Virtual Server
- Description property Virtual Server , IVMSupportDriver interface
- IVMSupportDriver interface Virtual Server , Description property
- Description property Virtual Server , VMSupportDriver interface
- VMSupportDriver interface Virtual Server , Description property
topic_type:
- apiref
api_name:
- IVMSupportDriver.Description
- IVMSupportDriver.get_Description
- VMSupportDriver.Description
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

# IVMSupportDriver::Description property

The **Description** property contains the driver's description.

This property is read-only.

## Syntax


```C++
HRESULT get_Description(
  [out] BSTR *description
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
<td><pre><code>VMSupportDriver.Description( _
  ByRef description _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

The driver's description.

This property value is read-only.

## Error codes



| Name                                                                                          | Meaning                                                   |
|-----------------------------------------------------------------------------------------------|-----------------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>              | The property value was retrieved successfully.<br/> |
| <dl> <dt> E\_POINTER</dt> </dl>        | The *description* parameter is **NULL**.<br/>       |
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

 

 





