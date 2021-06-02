---
description: An application that contains at least one queuable component can be marked as queued using the component services administrative tool.
ms.assetid: 7d9fec63-0bb7-45f3-9d40-736a60d69185
title: Creating Component Queues
ms.topic: article
ms.date: 05/31/2018
---

# Creating Component Queues

An application that contains at least one queuable component can be marked as queued using the component services administrative tool.

When an application is marked as queued, COM+ automatically creates a message queuing queue for it. The queue name is the name of the application; if the queue name matches the name of an existing queue, COM+ will use the existing queue.

> [!Note]  
> The Message Queuing *PathName* parameter is a combination of the Remote Server Name (RSN) and the COM+ application name. The RSN refers to the target of a remote activation. You specify an RSN during the installation of a client exportable application on a client computer. The installation procedure uses the RSN to direct activation to a specified client computer. For more information about queue names, refer to the table of parameters in the "Queue Moniker Parameters" section in [Using the Queue Moniker](using-the-queue-moniker.md).

 

## Component Services Administrative Tool

To specify a COM+ application as queued, use the following steps:

1.  In the console tree of the Component Services administrative tool, under **Component Services**, open the **COM+ Applications** folder associated with the computer you wish to manage.

2.  Right-click the application for which you wish to create a queue, and then click **Properties**.

3.  Select the **Queuing** tab in the properties dialog.

4.  Activate the check box labeled **Queued – This application can be reached by MSMQ queues**.

    > [!Note]  
    > If the **Queued** check box is grayed out, the application contains no queuable components.

     

5.  Click **OK**.

## Visual Basic

Does not apply.

## C/C++

Does not apply.

## Remarks

Queues created by the COM+ Administration Library or the Component Services administrative tool are marked with the Message Queuing transactional attribute.

After a queued application is installed at the server, it can be made available to clients by exporting the application and then importing the application at each client.

## Related topics

<dl> <dt>

[Creating Queuable Components](creating-queuable-components.md)
</dt> <dt>

[Queued Components Architecture](queued-components-architecture.md)
</dt> </dl>

 

 



