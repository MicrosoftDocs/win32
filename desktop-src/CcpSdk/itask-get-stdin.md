---
Description: 'Retrieves the file from which standard input has been redirected.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'e616c6a2-423f-4cfb-96ac-eab4fc4cea11'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ITask::get\_Stdin method'
---

# ITask::get\_Stdin method

Retrieves the file from which standard input has been redirected.

## Syntax


```C++
HRESULT get_Stdin(
  [out] BSTR *pRetVal
);
```



## Parameters

<dl> <dt>

*pRetVal* \[out\]
</dt> <dd>

The path to the file from which standard input has been redirected.

</dd> </dl>

## Return value

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code.

## Requirements



|                         |                                                                                       |
|-------------------------|---------------------------------------------------------------------------------------|
| Product<br/>      | Compute Cluster Pack Client Utilities<br/>                                      |
| Type library<br/> | <dl> <dt>Ccpapi.tlb</dt> </dl> |



## See also

<dl> <dt>

[**ITask**](itask.md)
</dt> <dt>

[**ITask::get\_Stderr**](itask-get-stderr.md)
</dt> <dt>

[**ITask::get\_Stdout**](itask-get-stdout.md)
</dt> <dt>

[**ITask::put\_Stdin**](itask-put-stdin.md)
</dt> </dl>

 

 




