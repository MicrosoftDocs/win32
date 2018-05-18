---
title: Remote Desktop Virtualization Interfaces
description: The Remote Desktop Virtualization API supports the following interfaces.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '150a3c9a-d504-4854-adaa-92e3a7e8ea70'
ms.prod: 'windows-server-dev'
ms.technology: 'remote-desktop-services'
ms.tgt_platform: multiple
---

# Remote Desktop Virtualization Interfaces

The Remote Desktop Virtualization API supports the following interfaces.

## In this section

<dl> <dt>

[**ITsSbBaseNotifySink**](itssbbasenotifysink.md)
</dt> <dd>

Exposes methods that report status and error messages to Remote Desktop Connection Broker (RD Connection Broker).

</dd> <dt>

[**ITsSbClientConnection**](itssbclientconnection.md)
</dt> <dd>

Exposes methods and properties that store state information about an incoming connection request from a Remote Desktop Connection (RDC) client.

</dd> <dt>

[**ITsSbClientConnectionPropertySet**](itssbclientconnectionpropertyset.md)
</dt> <dd>

Can be used to define custom properties of a client connection as appropriate.

</dd> <dt>

[**ITsSbEnvironment**](itssbenvironment.md)
</dt> <dd>

Exposes methods and properties that contain information about the environment that hosts the target computer. This interface can be used to store information about a physical server that hosts virtual machines.

</dd> <dt>

[**ITsSbEnvironmentPropertySet**](itssbenvironmentpropertyset.md)
</dt> <dd>

Can be used to define custom properties of an environment that hosts target computers as appropriate.

</dd> <dt>

[**ITsSbFilterPluginStore**](itssbfilterpluginstore.md)
</dt> <dd>

Filter Plugin Store

</dd> <dt>

[**ITsSbGenericNotifySink**](itssbgenericnotifysink.md)
</dt> <dd>

Exposes methods that reports completion to and gets wait time from the RD Connection Broker.

</dd> <dt>

[**ITsSbGlobalStore**](itssbglobalstore.md)
</dt> <dd>

Exposes methods that query for target computers, sessions, environments, and farms that have been added to the RD Connection Broker store.

</dd> <dt>

[**ITsSbLoadBalanceResult**](itssbloadbalanceresult.md)
</dt> <dd>

Exposes methods and properties that store the target name returned by a load-balancing algorithm.

</dd> <dt>

[**ITsSbLoadBalancing**](itssbloadbalancing.md)
</dt> <dd>

Exposes methods you can use to provide a custom load-balancing algorithm.

</dd> <dt>

[**ITsSbLoadBalancingNotifySink**](itssbloadbalancingnotifysink.md)
</dt> <dd>

Exposes methods that return the result of a load-balancing algorithm to RD Connection Broker.

</dd> <dt>

[**ITsSbOrchestration**](itssborchestration.md)
</dt> <dd>

Exposes methods that RD Connection Broker uses to ensure that the target is ready before a client is redirected to it.

</dd> <dt>

[**ITsSbOrchestrationNotifySink**](itssborchestrationnotifysink.md)
</dt> <dd>

Exposes methods that return an [**ITsSbTarget**](itssbtarget.md) object to RD Connection Broker after the target is successfully prepared for a connection.

</dd> <dt>

[**ITsSbPlacement**](itssbplacement.md)
</dt> <dd>

Exposes methods that prepare the environment (the computer that hosts the virtual machine).

</dd> <dt>

[**ITsSbPlacementNotifySink**](itssbplacementnotifysink.md)
</dt> <dd>

Exposes methods that return information about environments to RD Connection Broker.

</dd> <dt>

[**ITsSbPlugin**](itssbplugin.md)
</dt> <dd>

Exposes methods that initialize and terminate plug-ins.

</dd> <dt>

[**ITsSbPluginNotifySink**](itssbpluginnotifysink.md)
</dt> <dd>

Exposes methods that notify RD Connection Broker about initialization or termination of a plug-in.

</dd> <dt>

[**ITsSbPluginPropertySet**](itssbpluginpropertyset.md)
</dt> <dd>

Can be used to define custom plug-in properties as appropriate.

</dd> <dt>

[**ITsSbPropertySet**](itssbpropertyset.md)
</dt> <dd>

Can be used to define custom properties as appropriate.

</dd> <dt>

[**ITsSbProvider**](itssbprovider.md)
</dt> <dd>

Exposes methods that create default implementations of objects that are used in Remote Desktop Virtualization.

</dd> <dt>

[**ITsSbProvisioning**](itssbprovisioning.md)
</dt> <dd>

Exposes methods that create and maintain virtual machines.

</dd> <dt>

[**ITsSbProvisioningPluginNotifySink**](itssbprovisioningpluginnotifysink.md)
</dt> <dd>

Exposes methods that notify RD Connection Broker about the provisioning of virtual machines.

</dd> <dt>

[**ITsSbResourceNotification**](itssbresourcenotification.md)
</dt> <dd>

Exposes methods that RD Connection Broker uses to notify plug-ins of any state changes that occur in the session, target, and client connection objects.

</dd> <dt>

[**ITsSbResourceNotificationEx**](itssbresourcenotificationex.md)
</dt> <dd>

Exposes methods that RD Connection Broker uses to notify plug-ins of any state changes that occur in the session, target, and client connection objects.

</dd> <dt>

[**ITsSbResourcePlugin**](itssbresourceplugin.md)
</dt> <dd>

Exposes methods that extend the capabilities of RD Connection Broker.

</dd> <dt>

[**ITsSbResourcePluginStore**](itssbresourcepluginstore.md)
</dt> <dd>

Exposes methods that enable resource plug-ins to store objects such as sessions and targets.

</dd> <dt>

[**ITsSbResourcePluginStoreEx**](itssbresourcepluginstoreex.md)
</dt> <dd>

Exposes methods that enable resource plug-ins to store objects such as sessions and targets.

</dd> <dt>

[**ITsSbServiceNotification**](itssbservicenotification.md)
</dt> <dd>

Exposes methods that RD Connection Broker uses to notify plug-ins of state changes that occur in the RD Connection Broker itself.

</dd> <dt>

[**ITsSbSession**](itssbsession.md)
</dt> <dd>

Exposes properties that store information about a user session.

</dd> <dt>

[**ITsSbTarget**](itssbtarget.md)
</dt> <dd>

Exposes properties that store configuration and state information about a target.

</dd> <dt>

[**ITsSbTargetEx**](itssbtargetex.md)
</dt> <dd>

Exposes properties that store configuration and state information about a target.

</dd> <dt>

[**ITsSbTargetPropertySet**](itssbtargetpropertyset.md)
</dt> <dd>

Derive from this interface to define a custom target property set.

</dd> <dt>

[**ITsSbTaskInfo**](itssbtaskinfo.md)
</dt> <dd>

Exposes properties that the Remote Desktop Connection Broker uses to set a plugin’s queue.

</dd> <dt>

[**ITsSbTaskPlugin**](itssbtaskplugin.md)
</dt> <dd>

Exposes methods that update the queue of tasks for Remote Desktop Connection Broker plugins.

</dd> <dt>

[**ITsSbTaskPluginNotifySink**](itssbtaskpluginnotifysink.md)
</dt> <dd>

Exposes methods that report status and error messages about tasks to RD Connection Broker.

</dd> <dt>

[**IWTSSBPlugin**](iwtssbplugin.md)
</dt> <dd>

Used to extend the capabilities of Terminal Services Session Broker (TS Session Broker). Implement this interface when you want to provide a plug-in that overrides the redirection logic of TS Session Broker.

</dd> </dl>

 

 




