---
Description: 'Retrieves the processor speed.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '3b36a378-fce1-4ba2-a3c4-4c4ded9ea958'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'INode::get\_ProcessorSpeed method'
---

# INode::get\_ProcessorSpeed method

Retrieves the processor speed.

## Syntax


```C++
HRESULT get_ProcessorSpeed(
  [out] long *pRetVal
);
```



## Parameters

<dl> <dt>

*pRetVal* \[out\]
</dt> <dd>

The processor speed, in megahertz (MHz).

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

[**INode**](inode.md)
</dt> </dl>

 

 




