---
Description: 'Specifies whether the calling application is a console or Windows application.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'd7f0a0e3-046f-4d74-a1ba-c4f5113e0093'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'IScheduler::SetInterfaceMode method'
---

# IScheduler::SetInterfaceMode method

Specifies whether the calling application is a console or Windows application.

## Syntax


```C++
HRESULT SetInterfaceMode(
  [in] VARIANT_BOOL isConsole,
  [in] long         hwnd
);
```



## Parameters

<dl> <dt>

*isConsole* \[in\]
</dt> <dd>

Set to VARIANT\_TRUE if the calling application is a console application: otherwise, VARIANT\_FALSE.

</dd> <dt>

*hwnd* \[in\]
</dt> <dd>

The window handle to the parent window if the application is a Windows application. Is ignored if *isConsole* is VARIANT\_TRUE.

</dd> </dl>

## Return value

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code.

## Remarks

The information is used to determine how to prompt the user for credentials if they are not specified in the job. If you do not call this method, the console is used.

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities, HPC Pack 2008 Client Utilities<br/>                           |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



## See also

<dl> <dt>

[**IScheduler**](ischeduler.md)
</dt> </dl>

 

 




