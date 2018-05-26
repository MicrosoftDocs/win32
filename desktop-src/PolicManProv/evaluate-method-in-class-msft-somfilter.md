---
Description: The Evaluate instance method evaluates the MSFT\_SomFilter object Rules as to whether they apply to this machine.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 31f489c5-aca6-49e8-96c4-b037c205edb5
ms.prod: windows-server-dev
ms.technology:
- group-policy
- windows-management-instrumentation
ms.tgt_platform: multiple
title: Evaluate method of the MSFT\_SomFilter class
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Evaluate method of the MSFT\_SomFilter class

The **Evaluate** instance method evaluates the [**MSFT\_SomFilter**](msft-somfilter.md) object Rules as to whether they apply to this machine.

This topic uses Managed Object Format (MOF) syntax. For more information about using this method, see [Calling a Method](https://msdn.microsoft.com/library/aa384832).

## Syntax


```mof
Uint32 Evaluate();
```



## Parameters

This method has no parameters.

## Return value

Returns a value of S\_OK (0) if all the queries expressed in the rules of the [**MSFT\_SomFilter**](msft-somfilter.md) object return results. If one or more of the queries in the rules does not return results, S\_FALSE (1) is returned. If an error occurs, an applicable WMI error code is returned.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                          |
| Namespace<br/>                | Root\\policy<br/>                                                                 |
| MOF<br/>                      | <dl> <dt>PolicMan.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>PolicMan.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_SomFilter**](msft-somfilter.md)
</dt> <dt>

[**MSFT\_Rule**](msft-rule.md)
</dt> <dt>

[**BatchEvaluate Method in Class MSFT\_SomFilter**](batchevaluate-method-in-class-msft-somfilter.md)
</dt> </dl>

 

 




