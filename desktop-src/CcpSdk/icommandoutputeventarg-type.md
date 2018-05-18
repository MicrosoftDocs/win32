---
Description: 'Retrieves a value that determines the source of the output.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '49f9cb24-07cf-4e7a-9147-9cefe9dc7d05'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ICommandOutputEventArg::Type property'
---

# ICommandOutputEventArg::Type property

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

[**ICommandOutputEventArg**](icommandoutputeventarg.md)
</dt> </dl>

 

 




