---
title: IVMSupportDriver Version property
description: The Version property contains the version number of the driver.
ms.assetid: 'c83a85b5-5040-4813-9c93-8c1c8615614e'
keywords: ["Version property Virtual Server", "Version property Virtual Server , IVMSupportDriver interface", "IVMSupportDriver interface Virtual Server , Version property", "Version property Virtual Server , VMSupportDriver interface", "VMSupportDriver interface Virtual Server , Version property"]
topic_type:
- apiref
api_name:
- IVMSupportDriver.Version
- IVMSupportDriver.get_Version
- VMSupportDriver.Version
api_location:
- VsComInterfaces.h
api_type:
- COM
---

# IVMSupportDriver::Version property

The **Version** property contains the version number of the driver.

This property is read-only.

## Syntax


```C++
HRESULT get_Version(
  [out] BSTR *version
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
<td><pre><code>VMSupportDriver.Version( _
  ByRef version _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

The driver's version. The version is in the form "w.x.y.z".

This property value is read-only.

## Error codes



| Name                                                                                           | Meaning                                                   |
|------------------------------------------------------------------------------------------------|-----------------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>               | The property value was retrieved successfully.<br/> |
| <dl> <dt>E\_POINTER</dt> </dl>          | The *version* parameter is **NULL**.<br/>           |
| <dl> <dt> DISP\_E\_EXCEPTION</dt> </dl> | An unknown error has occurred.<br/>                 |



## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



## See also

<dl> <dt>

[**IVMSupportDriver**](ivmsupportdriver.md)
</dt> </dl>

 

 





