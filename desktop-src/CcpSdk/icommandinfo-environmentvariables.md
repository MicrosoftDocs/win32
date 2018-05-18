---
Description: 'Retrieves the environment variables used by the command.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '9ad8bd55-a823-4f61-8775-2b81ecca1695'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ICommandInfo::EnvironmentVariables property'
---

# ICommandInfo::EnvironmentVariables property

Retrieves the environment variables used by the command.

This property is read-only.

## Syntax


```C++
HRESULT get_EnvironmentVariables(
  [out] INameValueCollection **pEnvVariables
);
```



## Property value

An [**INameValueCollection**](inamevaluecollection2.md) interface that contains the collection of environment variables used by the command. The variant type of each item is VT\_DISPATCH. Query the **pdispVal** member of the variant for the [**INameValue**](inamevalue2.md) interface.

## Error codes

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code.

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities, HPC Pack 2008 Client Utilities<br/>                           |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



## See also

<dl> <dt>

[**ICommandInfo**](icommandinfo.md)
</dt> </dl>

 

 




