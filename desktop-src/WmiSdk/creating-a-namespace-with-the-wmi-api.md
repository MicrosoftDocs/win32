---
Description: Another way of creating a namespace is to use the WMI API to create the namespace programmatically.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 27a65eb0-4312-4df6-8c74-f30fe61dfec9
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
title: Creating a Namespace with the WMI API
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Creating a Namespace with the WMI API

Another way of creating a namespace is to use the WMI API to create the namespace programmatically. The advantage to creating a namespace programmatically is that you can create the namespace from within an application. However, using the WMI API is more complex than using Managed Object Format (MOF) code, and you cannot as easily share your namespaces with other developers.

The following procedure describes how to create a namespace using the WMI API.

**To create a namespace using the WMI API**

1.  Use [**IWbemServices::GetObject**](/windows/win32/WbemCli/nf-wbemcli-iwbemservices-getobject?branch=master) to retrieve a pointer to an [**IWbemClassObject**](/windows/win32/WbemCli/nn-wbemcli-iwbemclassobject?branch=master) object that points to the [**\_\_Namespace**](--namespace.md) system class.
2.  Define an instance of the [**\_\_Namespace**](--namespace.md) system class with a call to [**IWbemClassObject::SpawnInstance**](/windows/win32/WbemCli/nf-wbemcli-iwbemclassobject-spawninstance?branch=master).
3.  Set the **Name** property of the [**\_\_Namespace**](--namespace.md) instance with a call to [**IWbemClassObject::Put**](/windows/win32/WbemCli/nf-wbemcli-iwbemclassobject-put?branch=master).
4.  Create the namespace with a call to [**IWbemServices::PutInstance**](/windows/win32/WbemCli/nf-wbemcli-iwbemservices-putinstance?branch=master).

    The *pInst* parameter of [**PutInstance**](/windows/win32/WbemCli/nf-wbemcli-iwbemservices-putinstance?branch=master) should point to the new instance.

 

 



