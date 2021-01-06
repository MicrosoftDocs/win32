---
description: Activating Component Queues
ms.assetid: cfbf7c73-2521-40cf-8c6e-436f64c07e31
title: Activating Component Queues
ms.topic: article
ms.date: 05/31/2018
---

# Activating Component Queues

Making method calls on a queued component does not directly execute the method. Rather, [Message Queuing](/previous-versions/windows/desktop/legacy/ms711472(v=vs.85)) marshals and stores method calls and parameters in a queue where they are later retrieved and executed by the queued component. Unlike activating a remote DCOM object, the queued component is not instantiated when a method is called. This is the basic idea behind using queued components—queued components need not be instantiated at the same time as the calling application.

> [!Note]  
> The descriptions for activating a queued application assume that the application is marked as queued and that the listener check box is enabled.

 

You can use scripting to start and stop a queued application. You can put the script under the control of the task scheduler to run it as required. For example, the script can be run on system reboot if the applications are to be permanently available. If the application is to process transactions in batch mode, the script can be run at a certain time each day in conjunction with a shutdown script to be sure the batch processing stops at a specific time.

## Component Services Administrative Tool

To start a queued application, use the following steps:

1.  In the console tree of the Component Services administrative tool, under **Component Services**, open the **COM+ Applications** folder associated with the computer you wish to manage.

2.  Right-click the application whose queue you want to activate.

3.  Click **Start**.

## Visual Basic

See the COMAdminCatalog.StartApplication example.

## C/C++

See the [**ICOMAdminCatalog::StartApplication**](/windows/desktop/api/ComAdmin/nf-comadmin-icomadmincatalog-startapplication) example.

## Related topics

<dl> <dt>

[Using the Queue Moniker](using-the-queue-moniker.md)
</dt> </dl>

 

 



