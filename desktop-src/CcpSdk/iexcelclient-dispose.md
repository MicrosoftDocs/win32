---
Description: 'Releases all of the resources that the object allocated.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '8CC7F56C-DC61-4236-9620-9D4FB4916C67'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'IExcelClient::Dispose method'
---

# IExcelClient::Dispose method

Releases all of the resources that the object allocated.

## Syntax


```C++
HRESULT Dispose();
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
<td><pre><code>Function Dispose() As HRESULT</code></pre></td>
</tr>
</tbody>
</table>



## Parameters

This method has no parameters.

## Return value

### C++

Returns **S\_OK** unless an exception occurs.

## Remarks

This method does not close or release resources for open instances of Excel.

If you do not call the **IExcelClient::Dispose** method for an instance of the [**IExcelClient**](iexcelclient.md) interface that you create, the Excel process can continue to exist after you exit Excel.

## Requirements



|                         |                                                                                                    |
|-------------------------|----------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities<br/>                                                       |
| Header<br/>       | <dl> <dt>Httpserv.h</dt> </dl>              |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Excel.tlb</dt> </dl> |



## See also

<dl> <dt>

[**IExcelClient**](iexcelclient.md)
</dt> </dl>

 

 




