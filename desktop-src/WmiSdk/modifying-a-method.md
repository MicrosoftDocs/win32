---
Description: In addition to classes and instances, WMI allows you to modify a method. The main reason you would want to modify a method is if you changed the implementation of a method in a provider. For more information, see Writing a Method Provider.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 239a994f-ecaf-4558-9626-8f5e60dd350c
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
title: Modifying a Method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Modifying a Method

In addition to classes and instances, WMI allows you to modify a method. The main reason you would want to modify a method is if you changed the implementation of a method in a provider. For more information, see [Writing a Method Provider](writing-a-method-provider.md).

Modifying a method is not an operation that can be done in script.

The following procedure describes how to modify a method programmatically.

**To modify a method programmatically**

1.  Retrieve the class definition with a call to [**IWbemClassObject::GetMethod**](/windows/win32/WbemCli/nf-wbemcli-iwbemclassobject-getmethod?branch=master).

    The two out parameters, *ppInSignature* and *ppOutSignature*, contain the in-parameter class and the out-parameter class, respectively. The return value is bundled into the out-parameter class as a property, and should be named **ReturnValue**.

2.  Retrieve and modify the parameters with calls to [**IWbemClassObject::Get**](/windows/win32/WbemCli/nf-wbemcli-iwbemclassobject-get?branch=master), [**IWbemClassObject::Put**](/windows/win32/WbemCli/nf-wbemcli-iwbemclassobject-put?branch=master), or [**IWbemClassObject::Delete**](/windows/win32/WbemCli/nf-wbemcli-iwbemclassobject-delete?branch=master).
3.  Place your new version of the method back into the parent class with a call to [**IWbemClassObject::PutMethod**](/windows/win32/WbemCli/nf-wbemcli-iwbemclassobject-putmethod?branch=master).

For more information, see [Manipulating Class and Instance Information](manipulating-class-and-instance-information.md).

 

 



