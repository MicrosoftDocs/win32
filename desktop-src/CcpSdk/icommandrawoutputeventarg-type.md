---
Description: 'Retrieves a value that determines the source of the output.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '973e7e3d-d8f7-4f87-a735-a023b9d57a87'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ICommandRawOutputEventArg::Type property'
---

# ICommandRawOutputEventArg::Type property

Retrieves a value that determines the source of the output.

This property is read-only.

## Syntax


```C++
HRESULT get_Type(
  [out] CommandOutputType *pType
);
```



## Property value

A value that determines the source of the output. For possible values, see the [**CommandOutputType**](commandoutputtype.md) enumeration.

## Error codes

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code.

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities, HPC Pack 2008 Client Utilities<br/>                           |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



## See also

<dl> <dt>

[**ICommandRawOutputEventArg**](icommandrawoutputeventarg.md)
</dt> </dl>

 

 




