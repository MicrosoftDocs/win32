---
description: The EvaluateCondition method of the Session object evaluates a logical expression that contains symbols and values. This method uses the MsiEvaluateCondition function.
ms.assetid: 629f7efd-80fe-4a0e-95cc-b62d6258ae0a
title: Session.EvaluateCondition method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Session.EvaluateCondition
api_type: 
- COM
api_location: 
- Msi.dll
---

# Session.EvaluateCondition method

The **EvaluateCondition** method of the [**Session**](session-object.md) object evaluates a logical expression that contains symbols and values. This method uses the [**MsiEvaluateCondition**](/windows/desktop/api/Msiquery/nf-msiquery-msievaluateconditiona) function.

## Syntax


```JScript
Session.EvaluateCondition(
  condition
)
```



## Parameters

<dl> <dt>

*condition* 
</dt> <dd>

Required string that contains the logical expression. For more information, see [Conditional Statement Syntax](conditional-statement-syntax.md).

</dd> </dl>

## Return value

This method returns an integer that indicates the evaluation of the condition.



| Constant                  | Value | Description                               |
|---------------------------|-------|-------------------------------------------|
| msiEvaluateConditionFalse | 0     | The condition evaluates to false.         |
| msiEvaluateConditionTrue  | 1     | The condition evaluates to true.          |
| msiEvaluateConditionNone  | 2     | A conditional expression is not provided. |
| msiEvaluateConditionError | 3     | The condition contains a syntax error.    |



 

## Remarks

Conditional expressions can be used to compare feature and component states. The following table shows the feature and component states that the EvaluateCondition method uses.



| State                 | Value | Description                                              |
|-----------------------|-------|----------------------------------------------------------|
| Null                  | Null  | No action taken on feature or component.                 |
| msiInstallStateAbsent | 2     | Feature or component is not present.                     |
| msiInstallStateLocal  | 3     | Feature or component is installed on the local computer. |
| msiInstallStateSource | 4     | Feature or component is installed to run from source.    |



 

> [!Note]  
> The states are not set until the [**SetInstallLevel**](session-setinstalllevel.md) method is called, either directly or by the [CostFinalize Action](costfinalize-action.md). Therefore, state checking is only useful in conditional expression in an action sequence table.

 

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer on Windows Server 2003 or Windows XP<br/> |
| DLL<br/>     | <dl> <dt>Msi.dll</dt> </dl>                                                                                                                                                                      |
| IID<br/>     | IID\_ISession is defined as 000C109E-0000-0000-C000-000000000046<br/>                                                                                                                                                                             |



## See also

<dl> <dt>

[Conditional Statement Syntax](conditional-statement-syntax.md)
</dt> </dl>

 

 




