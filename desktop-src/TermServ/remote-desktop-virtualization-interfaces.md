---
title: Remote Desktop Virtualization Interfaces
description: The Remote Desktop Virtualization API supports the following interfaces.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 150a3c9a-d504-4854-adaa-92e3a7e8ea70
ms.prod: windows-server-dev
ms.technology: remote-desktop-services
ms.tgt_platform: multiple
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Remote Desktop Virtualization Interfaces

The Remote Desktop Virtualization API supports the following interfaces.

## In this section

<dl> <dt>

[**ITsSbBaseNotifySink**](/windows/win32/sbtsv/nn-sbtsv-itssbbasenotifysink?branch=master)
</dt> <dd>

Exposes methods that report status and error messages to Remote Desktop Connection Broker (RD Connection Broker).

</dd> <dt>

[**ITsSbClientConnection**](/windows/win32/sbtsv/nn-sbtsv-itssbclientconnection?branch=master)
</dt> <dd>

Exposes methods and properties that store state information about an incoming connection request from a Remote Desktop Connection (RDC) client.

</dd> <dt>

[**ITsSbClientConnectionPropertySet**](/windows/win32/sbtsv/?branch=master)
</dt> <dd>

Can be used to define custom properties of a client connection as appropriate.

</dd> <dt>

[**ITsSbEnvironment**](/windows/win32/sbtsv/nn-sbtsv-itssbenvironment?branch=master)
</dt> <dd>

Exposes methods and properties that contain information about the environment that hosts the target computer. This interface can be used to store information about a physical server that hosts virtual machines.

</dd> <dt>

[**ITsSbEnvironmentPropertySet**](/windows/win32/sbtsv/?branch=master)
</dt> <dd>

Can be used to define custom properties of an environment that hosts target computers as appropriate.

</dd> <dt>

[**ITsSbFilterPluginStore**](/windows/win32/sbtsv/nn-sbtsv-itssbfilterpluginstore?branch=master)
</dt> <dd>

Filter Plugin Store

</dd> <dt>

[**ITsSbGenericNotifySink**](/windows/win32/sbtsv/nn-sbtsv-itssbgenericnotifysink?branch=master)
</dt> <dd>

Exposes methods that reports completion to and gets wait time from the RD Connection Broker.

</dd> <dt>

[**ITsSbGlobalStore**](/windows/win32/sbtsv/nn-sbtsv-itssbglobalstore?branch=master)
</dt> <dd>

Exposes methods that query for target computers, sessions, environments, and farms that have been added to the RD Connection Broker store.

</dd> <dt>

[**ITsSbLoadBalanceResult**](/windows/win32/sbtsv/nn-sbtsv-itssbloadbalanceresult?branch=master)
</dt> <dd>

Exposes methods and properties that store the target name returned by a load-balancing algorithm.

</dd> <dt>

[**ITsSbLoadBalancing**](/windows/win32/sbtsv/nn-sbtsv-itssbloadbalancing?branch=master)
</dt> <dd>

Exposes methods you can use to provide a custom load-balancing algorithm.

</dd> <dt>

[**ITsSbLoadBalancingNotifySink**](/windows/win32/sbtsv/nn-sbtsv-itssbloadbalancingnotifysink?branch=master)
</dt> <dd>

Exposes methods that return the result of a load-balancing algorithm to RD Connection Broker.

</dd> <dt>

[**ITsSbOrchestration**](/windows/win32/sbtsv/nn-sbtsv-itssborchestration?branch=master)
</dt> <dd>

Exposes methods that RD Connection Broker uses to ensure that the target is ready before a client is redirected to it.

</dd> <dt>

[**ITsSbOrchestrationNotifySink**](/windows/win32/sbtsv/nn-sbtsv-itssborchestrationnotifysink?branch=master)
</dt> <dd>

Exposes methods that return an [**ITsSbTarget**](/windows/win32/sbtsv/nn-sbtsv-itssbtarget?branch=master) object to RD Connection Broker after the target is successfully prepared for a connection.

</dd> <dt>

[**ITsSbPlacement**](/windows/win32/sbtsv/nn-sbtsv-itssbplacement?branch=master)
</dt> <dd>

Exposes methods that prepare the environment (the computer that hosts the virtual machine).

</dd> <dt>

[**ITsSbPlacementNotifySink**](/windows/win32/sbtsv/nn-sbtsv-itssbplacementnotifysink?branch=master)
</dt> <dd>

Exposes methods that return information about environments to RD Connection Broker.

</dd> <dt>

[**ITsSbPlugin**](/windows/win32/sbtsv/nn-sbtsv-itssbplugin?branch=master)
</dt> <dd>

Exposes methods that initialize and terminate plug-ins.

</dd> <dt>

[**ITsSbPluginNotifySink**](/windows/win32/sbtsv/nn-sbtsv-itssbpluginnotifysink?branch=master)
</dt> <dd>

Exposes methods that notify RD Connection Broker about initialization or termination of a plug-in.

</dd> <dt>

[**ITsSbPluginPropertySet**](/windows/win32/sbtsv/?branch=master)
</dt> <dd>

Can be used to define custom plug-in properties as appropriate.

</dd> <dt>

[**ITsSbPropertySet**](/windows/win32/sbtsv/?branch=master)
</dt> <dd>

Can be used to define custom properties as appropriate.

</dd> <dt>

[**ITsSbProvider**](/windows/win32/sbtsv/nn-sbtsv-itssbprovider?branch=master)
</dt> <dd>

Exposes methods that create default implementations of objects that are used in Remote Desktop Virtualization.

</dd> <dt>

[**ITsSbProvisioning**](/windows/win32/sbtsv/nn-sbtsv-itssbprovisioning?branch=master)
</dt> <dd>

Exposes methods that create and maintain virtual machines.

</dd> <dt>

[**ITsSbProvisioningPluginNotifySink**](/windows/win32/sbtsv/nn-sbtsv-itssbprovisioningpluginnotifysink?branch=master)
</dt> <dd>

Exposes methods that notify RD Connection Broker about the provisioning of virtual machines.

</dd> <dt>

[**ITsSbResourceNotification**](/windows/win32/sbtsv/nn-sbtsv-itssbresourcenotification?branch=master)
</dt> <dd>

Exposes methods that RD Connection Broker uses to notify plug-ins of any state changes that occur in the session, target, and client connection objects.

</dd> <dt>

[**ITsSbResourceNotificationEx**](/windows/win32/sbtsv/nn-sbtsv-itssbresourcenotificationex?branch=master)
</dt> <dd>

Exposes methods that RD Connection Broker uses to notify plug-ins of any state changes that occur in the session, target, and client connection objects.

</dd> <dt>

[**ITsSbResourcePlugin**](/windows/win32/sbtsv/?branch=master)
</dt> <dd>

Exposes methods that extend the capabilities of RD Connection Broker.

</dd> <dt>

[**ITsSbResourcePluginStore**](/windows/win32/sbtsv/nn-sbtsv-itssbresourcepluginstore?branch=master)
</dt> <dd>

Exposes methods that enable resource plug-ins to store objects such as sessions and targets.

</dd> <dt>

[**ITsSbResourcePluginStoreEx**](itssbresourcepluginstoreex.md)
</dt> <dd>

Exposes methods that enable resource plug-ins to store objects such as sessions and targets.

</dd> <dt>

[**ITsSbServiceNotification**](/windows/win32/sbtsv/nn-sbtsv-itssbservicenotification?branch=master)
</dt> <dd>

Exposes methods that RD Connection Broker uses to notify plug-ins of state changes that occur in the RD Connection Broker itself.

</dd> <dt>

[**ITsSbSession**](/windows/win32/sbtsv/nn-sbtsv-itssbsession?branch=master)
</dt> <dd>

Exposes properties that store information about a user session.

</dd> <dt>

[**ITsSbTarget**](/windows/win32/sbtsv/nn-sbtsv-itssbtarget?branch=master)
</dt> <dd>

Exposes properties that store configuration and state information about a target.

</dd> <dt>

[**ITsSbTargetEx**](itssbtargetex.md)
</dt> <dd>

Exposes properties that store configuration and state information about a target.

</dd> <dt>

[**ITsSbTargetPropertySet**](/windows/win32/sbtsv/?branch=master)
</dt> <dd>

Derive from this interface to define a custom target property set.

</dd> <dt>

[**ITsSbTaskInfo**](/windows/win32/sbtsv/nn-sbtsv-itssbtaskinfo?branch=master)
</dt> <dd>

Exposes properties that the Remote Desktop Connection Broker uses to set a plugin’s queue.

</dd> <dt>

[**ITsSbTaskPlugin**](/windows/win32/sbtsv/nn-sbtsv-itssbtaskplugin?branch=master)
</dt> <dd>

Exposes methods that update the queue of tasks for Remote Desktop Connection Broker plugins.

</dd> <dt>

[**ITsSbTaskPluginNotifySink**](/windows/win32/sbtsv/nn-sbtsv-itssbtaskpluginnotifysink?branch=master)
</dt> <dd>

Exposes methods that report status and error messages about tasks to RD Connection Broker.

</dd> <dt>

[**IWTSSBPlugin**](/windows/win32/Tssbx/nn-tssbx-iwtssbplugin?branch=master)
</dt> <dd>

Used to extend the capabilities of Terminal Services Session Broker (TS Session Broker). Implement this interface when you want to provide a plug-in that overrides the redirection logic of TS Session Broker.

</dd> </dl>

 

 




