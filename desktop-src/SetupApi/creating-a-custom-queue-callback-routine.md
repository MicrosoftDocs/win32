---
Description: In addition to using the default queue callback, you can write a custom callback routine.
ms.assetid: 68781565-71a2-43bf-ad01-7c1cdc514f7b
title: Creating a Custom Queue Callback Routine
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Creating a Custom Queue Callback Routine

In addition to using the default queue callback, you can write a custom callback routine. This function must have the same form as [*FileCallback*](/windows/win32/setupapi/?branch=master). This is useful if you need a callback routine to handle a notification in a manner other than that provided by the default queue callback routine.

If only a small portion of the default queue callback routine's behavior needs to be changed, you can create a custom callback routine to filter the notifications, handling only those that require special behavior and calling [**SetupDefaultQueueCallback**](/windows/win32/Setupapi/nf-setupapi-setupdefaultqueuecallbacka?branch=master) for the others.

For example, if you wanted to custom-handle file delete errors, you could create a custom callback function, *MyCallback*. This function would intercept and process [**SPFILENOTIFY\_DELETEERROR**](spfilenotify-deleteerror.md) notifications, and call the default queue callback function for all other notifications. *MyCallback* returns a value for the delete error notifications. For all other notifications, *MyCallback* passes whatever value the default queue callback routine returned to the queue.

This flow of control is illustrated in the following diagram.

![arrows and boxes showing data flow for custom callback function](images/callback.png)

> \[!Important\]  
> If the custom callback function calls the default queue callback routine, it must pass the void pointer returned by [**SetupInitDefaultQueueCallback**](/windows/win32/Setupapi/nf-setupapi-setupinitdefaultqueuecallback?branch=master) or [**SetupInitDefaultQueueCallbackEx**](/windows/win32/Setupapi/nf-setupapi-setupinitdefaultqueuecallbackex?branch=master) to the default callback routine.

 

 

 



