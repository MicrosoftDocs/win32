---
Description: 'Retrieves the processor architecture.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'e856a99e-da96-44f6-9b81-ca263dfd23fe'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'INode::get\_ProcessorArchitecture method'
---

# INode::get\_ProcessorArchitecture method

Retrieves the processor architecture.

## Syntax


```C++
HRESULT get_ProcessorArchitecture(
  [out] BSTR *pRetVal
);
```



## Parameters

<dl> <dt>

*pRetVal* \[out\]
</dt> <dd>

The processor architecture.

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

 

 




