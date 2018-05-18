---
Description: 'Receives an array of MSFT\_SomFilter objects and evaluates the rules in each for their application to this computer.'
audience: developer
author: 'REDMOND\\markl'
manager: 'REDMOND\\markl'
ms.assetid: 'c3524789-7524-40e4-a719-20a6ebafbd86'
ms.prod: 'windows-server-dev'
ms.technology:
- 'group-policy'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
title: 'BatchEvaluate method of the MSFT\_SomFilter class'
---

# BatchEvaluate method of the MSFT\_SomFilter class

The **BatchEvaluate** class method receives an array of [**MSFT\_SomFilter**](msft-somfilter.md) objects and evaluates the rules in each for their application to this computer. The method returns an array of **uint32** values with each element in the result array corresponding to the parallel [**MSFT\_SomFilter**](msft-somfilter.md) object in the input array.

This topic uses Managed Object Format (MOF) syntax. For more information about using this method, see [Calling a Method](https://msdn.microsoft.com/library/aa384832).

## Syntax


```mof
Uint32 BatchEvaluate(
  [in]  MSFT_SomFilter REF filters[],
  [out] uint32             results[]
);
```



## Parameters

<dl> <dt>

*filters* \[in\]
</dt> <dd>

Reference to an array of [**MSFT\_SomFilter**](msft-somfilter.md) objects.

</dd> <dt>

*results* \[out\]
</dt> <dd>

Array of return values. Each element corresponds to the element in the *filters* array with the same array index.

</dd> </dl>

## Return value

Returns a value of **S\_OK** (0) if all the queries expressed in the rules of the corresponding [**MSFT\_SomFilter**](msft-somfilter.md) object in the *filters* array returned results. A value of **S\_FALSE** (1) indicates that one or more of the queries did not return results. If an error occurs, an applicable WMI error code is returned.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                          |
| Namespace<br/>                | Root\\policy<br/>                                                                 |
| MOF<br/>                      | <dl> <dt>PolicMan.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>PolicMan.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_SomFilter**](msft-somfilter.md)
</dt> <dt>

[**MSFT\_Rule**](msft-rule.md)
</dt> <dt>

[**Evaluate Method in Class MSFT\_SomFilter**](evaluate-method-in-class-msft-somfilter.md)
</dt> </dl>

 

 




