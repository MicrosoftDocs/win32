---
title: IVMHostInfo ProcessorFeaturesString property
description: The ProcessorFeaturesString property contains a list of features supported by the host processor.
ms.assetid: 4e9be1cf-91d9-4119-b4cc-67c286d511ce
keywords:
- ProcessorFeaturesString property Virtual Server
- ProcessorFeaturesString property Virtual Server , IVMHostInfo interface
- IVMHostInfo interface Virtual Server , ProcessorFeaturesString property
- ProcessorFeaturesString property Virtual Server , VMHostInfo interface
- VMHostInfo interface Virtual Server , ProcessorFeaturesString property
topic_type:
- apiref
api_name:
- IVMHostInfo.ProcessorFeaturesString
- IVMHostInfo.get_ProcessorFeaturesString
- VMHostInfo.ProcessorFeaturesString
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

# IVMHostInfo::ProcessorFeaturesString property

The **ProcessorFeaturesString** property contains a list of features supported by the host processor.

This property is read-only.

## Syntax


```C++
HRESULT get_ProcessorFeaturesString(
  [out] BSTR *featuresString
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
<td><pre><code>VMHostInfo.ProcessorFeaturesString( _
  ByRef featuresString _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

Contains a comma-delimited list of features supported by the host processor.

This property value is read-only.

## Error codes



| Name                                                                                           | Meaning                                        |
|------------------------------------------------------------------------------------------------|------------------------------------------------|
| <dl> <dt> S\_OK</dt> </dl>              | The operation was successful.<br/>       |
| <dl> <dt>E\_POINTER</dt> </dl>          | The outgoing parameter is **NULL**.<br/> |
| <dl> <dt> DISP\_E\_EXCEPTION</dt> </dl> | An unexpected error occurred.<br/>       |



## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



## See also

<dl> <dt>

[**IVMHostInfo**](ivmhostinfo.md)
</dt> </dl>

 

 





