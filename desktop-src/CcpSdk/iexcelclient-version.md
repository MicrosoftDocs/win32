---
Description: 'Gets the version of the Excel client.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'D36AE57C-A145-4ECA-B879-3A6D21C03012'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'IExcelClient::Version property'
---

# IExcelClient::Version property

Gets the version of the Excel client.

This property is read-only.

## Syntax


```C++
HRESULT get_Version(
  [out, retval] BSTR *pRetVal
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
<td><pre><code>&#39; Data type: String

Property Version( _
) As String</code></pre></td>
</tr>
</tbody>
</table>



## Property value

The version of the Excel client. For Windows HPC Server 2008 R2, this value is always 1.0.

## Error codes

Returns **S\_OK** unless an exception occurs.

## Requirements



|                         |                                                                                                    |
|-------------------------|----------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities<br/>                                                       |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Excel.tlb</dt> </dl> |



## See also

<dl> <dt>

[**IExcelClient**](iexcelclient.md)
</dt> </dl>

 

 




