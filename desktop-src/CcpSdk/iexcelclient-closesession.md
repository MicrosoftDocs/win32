---
Description: 'Closes the session that you opened by calling the IExcelClient::OpenSession method (subject to the optionally specified time-out period), and closes all instances of Excel that are running on the compute nodes.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'EEAE5510-5CD2-4764-9836-5A8BA6CDE1E5'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'IExcelClient::CloseSession method'
---

# IExcelClient::CloseSession method

Closes the session that you opened by calling the [**IExcelClient::OpenSession**](iexcelclient-opensession.md) method (subject to the optionally specified time-out period), and closes all instances of Excel that are running on the compute nodes.

## Syntax


```C++
HRESULT CloseSession(
  [in, optional] VARIANT timeoutMilliseconds,
  [in, optional] Variant timeoutMilliseconds
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
<td><pre><code>Function CloseSession( _
  [ ByVal timeoutMilliseconds As VARIANT ], _
  [ ByVal timeoutMilliseconds As Variant ] _
) As HRESULT</code></pre></td>
</tr>
</tbody>
</table>



## Parameters

<dl> <dt>*timeoutMilliseconds* \[in, optional\]</dt> <dd> 

|         |                                                                                                                                                                                                                                 |
|---------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **C++** | **VARIANT** that specifies an integer that indicates the length of time in milliseconds that the method should wait for the SOA session to close. The default time-out period is 120,000 milliseconds (two minutes).<br/> |
| **VB**  | **Variant** that specifies an integer that indicates the length of time in milliseconds that the method should wait for the SOA session to close. The default time-out period is 120,000 milliseconds (two minutes).<br/> |

 </dd> </dl>

## Return value

### C++

Returns **S\_OK** unless an exception occurs.

## Requirements



|                         |                                                                                                    |
|-------------------------|----------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities<br/>                                                       |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Excel.tlb</dt> </dl> |



## See also

<dl> <dt>

[**IExcelClient**](iexcelclient.md)
</dt> <dt>

[**IExcelClient::OpenSession**](iexcelclient-opensession.md)
</dt> </dl>

 

 




