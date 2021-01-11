---
description: A business rule allows an application to use logic at run time to qualify permissions granted to the client.
ms.assetid: 2220d533-87f5-41a6-a688-a3307f0853fa
title: Business Rules
ms.topic: article
ms.date: 05/31/2018
---

# Business Rules

A business rule allows an application to use logic at run time to qualify permissions granted to the client.

A business rule is a script written in the Visual Basic Scripting Edition (VBScript) programming language or written using the Microsoft JScript development software that is associated with an [**IAzTask**](/windows/desktop/api/Azroles/nn-azroles-iaztask) object. When an application checks access for an operation, Authorization Manager first checks if the current client has access to any tasks that contain that operation but that are not associated with business rules. If access is not granted this way, Authorization Manager runs business-rule scripts associated with any task that contains the operation.

An application passes information to a business-rule script as a pair of arrays that represent the names and values of parameters. The script has access to these parameters through an [**AzBizRuleContext**](/windows/desktop/api/Azroles/nn-azroles-iazbizrulecontext) object that is created when the script runs.

A business-rule script cannot be assigned to a task contained by a delegated scope.

## Related topics

<dl> <dt>

[Qualifying Access with Business Logic in C++](qualifying-access-with-business-logic-in-c--.md)
</dt> </dl>

 

 



