---
Description: 'Cancels any currently running Excel calculations without closing the SOA session.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '161402DC-FB27-4812-B94C-E6E77CA3ABF4'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'IExcelClient::Cancel method'
---

# IExcelClient::Cancel method

Cancels any currently running Excel calculations without closing the SOA session.

## Syntax


```C++
HRESULT Cancel();
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
<td><pre><code>Function Cancel() As HRESULT</code></pre></td>
</tr>
</tbody>
</table>



## Parameters

This method has no parameters.

## Return value

### C++

Returns **S\_OK** unless an exception occurs.

## Remarks

When you call this method, the Excel SOA client stops sending requests, directs the broker to stop processing requests that are already queued, and closes the connection to the HPC cluster. If you run the calculation again after you canceled it, the client uses the original SOA session, as long as that session is valid.

## Requirements



|                         |                                                                                                    |
|-------------------------|----------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities<br/>                                                       |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Excel.tlb</dt> </dl> |



## See also

<dl> <dt>

[**IExcelClient**](iexcelclient.md)
</dt> <dt>

[**IExcelClient::OpenSession**](iexcelclient-opensession.md)
</dt> <dt>

[**IExcelClient::Run**](iexcelclient-run.md)
</dt> </dl>

 

 




