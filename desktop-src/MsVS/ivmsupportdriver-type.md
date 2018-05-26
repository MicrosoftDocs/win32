---
title: IVMSupportDriver Type property
description: The Type property contains the type of support driver.
ms.assetid: f49b1c7d-c491-4f17-b48b-3b3f620b52d2
keywords:
- Type property Virtual Server
- Type property Virtual Server , IVMSupportDriver interface
- IVMSupportDriver interface Virtual Server , Type property
- Type property Virtual Server , VMSupportDriver interface
- VMSupportDriver interface Virtual Server , Type property
topic_type:
- apiref
api_name:
- IVMSupportDriver.Type
- IVMSupportDriver.get_Type
- VMSupportDriver.Type
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

# IVMSupportDriver::Type property

The **Type** property contains the type of support driver.

This property is read-only.

## Syntax


```C++
HRESULT get_Type(
  [out] VMSupportDriverType *driverType
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
<td><pre><code>VMSupportDriver.Type( _
  ByRef driverType _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

The type of driver this object represents.

This property value is read-only.

## Error codes



| Name                                                                                  | Meaning                                                   |
|---------------------------------------------------------------------------------------|-----------------------------------------------------------|
| <dl> <dt> S\_OK</dt> </dl>     | The property value was retrieved successfully.<br/> |
| <dl> <dt>E\_POINTER</dt> </dl> | The *driverType* parameter is **NULL**.<br/>        |



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

 

 





