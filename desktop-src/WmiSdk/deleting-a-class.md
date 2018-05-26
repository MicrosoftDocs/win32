---
Description: Unlike deleting a dynamic instance, deleting a class is a simple procedure.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: bc0ee1e8-7515-4f35-ace3-6344c2ef0ab8
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
title: Deleting a Class
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Deleting a Class

Unlike deleting a dynamic instance, deleting a class is a simple procedure. However, as discussed earlier, base or derived classes are rarely deleted. Instead, an instance is more commonly deleted. The [Scripting API for WMI](scripting-api-for-wmi.md) uses the same methods to delete either a class object or an instance. For more information, see [Deleting an Instance](deleting-an-instance.md). For information about removing classes and instances from the WMI repository, see the [**pragma deleteclass**](pragma-deleteclass.md) preprocessor command.

The [COM API for WMI](com-api-for-wmi.md) has different methods for deleting an instance and deleting an object.

The following procedure describes how to delete a base class or derived class.

**To delete a base class or derived class**

-   Call either the [**IWbemServices::DeleteClass**](/windows/win32/WbemCli/nf-wbemcli-iwbemservices-deleteclass?branch=master) or [**IWbemServices::DeleteClassAsync**](/windows/win32/WbemCli/nf-wbemcli-iwbemservices-deleteclassasync?branch=master) method.

    As the name suggests, [**DeleteClassAsync**](/windows/win32/WbemCli/nf-wbemcli-iwbemservices-deleteclassasync?branch=master) deletes an instance asynchronously while [**DeleteClass**](/windows/win32/WbemCli/nf-wbemcli-iwbemservices-deleteclass?branch=master) deletes an instance synchronously. To use **DeleteClassAsync**, you must also implement an [**IWbemObjectSink**](iwbemobjectsink.md) object.

> [!Note]  
> Because the callback to the sink might not be returned at the same authentication level as the client requires, it is recommended that you use semisynchronous instead of asynchronous communication. For more information, see [Calling a Method](calling-a-method.md).

 

 

 



