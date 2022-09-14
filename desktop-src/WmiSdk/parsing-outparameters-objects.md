---
description: A SWbemMethod.OutParameters object is created and supplied with data by the provider method that is executing.
ms.assetid: fc06d6a1-770a-4f34-affd-f5035dad9360
ms.tgt_platform: multiple
title: Parsing OutParameters Objects
ms.topic: article
ms.date: 05/31/2018
---

# Parsing OutParameters Objects

A [**SWbemMethod.OutParameters**](swbemmethod-outparameters.md) object is created and supplied with data by the provider method that is executing. Properties of the **OutParameters** object are specific to the method called. For example, in the script below, *SD* (contained in *outParam*) is the output parameter defined for the **\_\_SystemSecurity.GetSD** method. The **ReturnValue** property is a generic property available for all **OutParameters** objects which contain the result of the operation.

The following code example illustrates obtaining output parameters from executing the [**GetSD**](--systemsecurity-getsd.md) method in class [**\_\_SystemSecurity**](--systemsecurity.md) for the local system.


```VB
' Connect to WMI root\cimv2 namespace.
Set svc = GetObject("winmgmts:root/cimv2")
' Execute the GetSD method and obtain the output parameters.
set outParam = svc.Execmethod("__SystemSecurity=@", "GetSD")
wscript.echo outparam.ReturnValue
' Format the security descriptor array
' in the SD parameter into one string to display.
objSD  = Join(outparam.SD,",")
wscript.echo objSD
' Release the out parameters object.
set outParam = nothing
```



For more information, see [**SWbemMethod.InParameters**](swbemmethod-inparameters.md).

 

 



