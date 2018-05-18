---
Description: 'Redirects standard input from the specified file.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'f7fa3615-d6a9-4a73-bfbb-afe4035186d1'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ITask::put\_Stdin method'
---

# ITask::put\_Stdin method

Redirects standard input from the specified file.

## Syntax


```C++
HRESULT put_Stdin(
  [in] BSTR Val
);
```



## Parameters

<dl> <dt>

*Val* \[in\]
</dt> <dd>

The path to the file from which standard input is redirected.

</dd> </dl>

## Return value

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code.

## Remarks

If the path contains long file names, enclose the path in quotation marks.

## Requirements



|                         |                                                                                       |
|-------------------------|---------------------------------------------------------------------------------------|
| Product<br/>      | Compute Cluster Pack Client Utilities<br/>                                      |
| Type library<br/> | <dl> <dt>Ccpapi.tlb</dt> </dl> |



## See also

<dl> <dt>

[**ITask**](itask.md)
</dt> <dt>

[**ITask::get\_Stdin**](itask-get-stdin.md)
</dt> <dt>

[**ITask::put\_Stderr**](itask-put-stderr.md)
</dt> <dt>

[**ITask::put\_Stdout**](itask-put-stdout.md)
</dt> </dl>

 

 




