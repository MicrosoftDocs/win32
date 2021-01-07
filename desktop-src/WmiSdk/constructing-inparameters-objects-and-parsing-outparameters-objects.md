---
description: Normally, direct access is adequate to call a WMI provider method.
ms.assetid: be9332b5-8094-44a2-8632-af9957ecf36b
ms.tgt_platform: multiple
title: Constructing InParameters Objects and Parsing OutParameters Objects
ms.topic: article
ms.date: 05/31/2018
---

# Constructing InParameters Objects and Parsing OutParameters Objects

Normally, direct access is adequate to call a WMI [*provider method*](gloss-p.md). Direct access means executing a method by using *object.method* syntax. However, in some cases, direct access cannot be used. Also, calling a provider method asynchronously from a script requires an [**ExecMethodAsync**](swbemobject-execmethodasync-.md) type of call.

> [!Note]  
> Because the callback to the sink might not be returned at the same authentication level as the client requires, it is recommended that you use semisynchronous instead of asynchronous communication. For more information, see [Calling a Method](calling-a-method.md).

 

The order of method input and output parameters is defined in the Managed Object Format (MOF) schema for the method. WMI does not prevent the parameter order from being changed when the class is recompiled by [mofcomp](mofcomp.md). By using an [**InParameters**](swbemmethod-inparameters.md) object, you can avoid problems that result from changed schema because the input parameters are identified by name. The correct parameter can be seen by examining the **ID** qualifier of each input parameter. The first parameter has an **ID** value of 0 (zero).

[**The SWbemObject.ExecMethod\_**](swbemobject-execmethod-.md), [**SWbemObject.ExecMethodAsync\_**](swbemobject-execmethodasync-.md), [**SWbemServices.ExecMethod**](swbemservices-execmethod.md), and [**SWbemServices.ExecMethodAsync**](swbemservices-execmethodasync.md) methods provide an alternate way to execute a provider method in cases where it is not possible to execute a method directly. For more information, see [Manipulating Class and Instance Information](manipulating-class-and-instance-information.md).

For more information about parameters, see [Constructing InParameters Objects](constructing-inparameters-objects.md) and [Parsing OutParameters Objects](parsing-outparameters-objects.md).

 

 



