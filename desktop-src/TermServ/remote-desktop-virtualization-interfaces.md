---
title: Remote Desktop Virtualization Interfaces
description: The Remote Desktop Virtualization API supports the following interfaces.
ms.assetid: 150a3c9a-d504-4854-adaa-92e3a7e8ea70
ms.tgt_platform: multiple
ms.topic: article
ms.date: 05/31/2018
---

# Remote Desktop Virtualization Interfaces

The Remote Desktop Virtualization API supports the following interfaces.

## In this section

<dl> <dt>

[**ITsSbBaseNotifySink**](/windows/desktop/api/sbtsv/nn-sbtsv-itssbbasenotifysink)
</dt> <dd>

Exposes methods that report status and error messages to Remote Desktop Connection Broker (RD Connection Broker).

</dd> <dt>

[**ITsSbClientConnection**](/windows/desktop/api/sbtsv/nn-sbtsv-itssbclientconnection)
</dt> <dd>

Exposes methods and properties that store state information about an incoming connection request from a Remote Desktop Connection (RDC) client.

</dd> <dt>

[**ITsSbClientConnectionPropertySet**](/windows/win32/api/sbtsv/nn-sbtsv-itssbclientconnectionpropertyset)
</dt> <dd>

Can be used to define custom properties of a client connection as appropriate.

</dd> <dt>

[**ITsSbEnvironment**](/windows/desktop/api/sbtsv/nn-sbtsv-itssbenvironment)
</dt> <dd>

Exposes methods and properties that contain information about the environment that hosts the target computer. This interface can be used to store information about a physical server that hosts virtual machines.

</dd> <dt>

[**ITsSbEnvironmentPropertySet**](/windows/win32/api/sbtsv/nn-sbtsv-itssbenvironmentpropertyset)
</dt> <dd>

Can be used to define custom properties of an environment that hosts target computers as appropriate.

</dd> <dt>

[**ITsSbFilterPluginStore**](/windows/desktop/api/sbtsv/nn-sbtsv-itssbfilterpluginstore)
</dt> <dd>

Filter Plugin Store

</dd> <dt>

[**ITsSbGenericNotifySink**](/windows/desktop/api/sbtsv/nn-sbtsv-itssbgenericnotifysink)
</dt> <dd>

Exposes methods that reports completion to and gets wait time from the RD Connection Broker.

</dd> <dt>

[**ITsSbGlobalStore**](/windows/desktop/api/sbtsv/nn-sbtsv-itssbglobalstore)
</dt> <dd>

Exposes methods that query for target computers, sessions, environments, and farms that have been added to the RD Connection Broker store.

</dd> <dt>

[**ITsSbLoadBalanceResult**](/windows/desktop/api/sbtsv/nn-sbtsv-itssbloadbalanceresult)
</dt> <dd>

Exposes methods and properties that store the target name returned by a load-balancing algorithm.

</dd> <dt>

[**ITsSbLoadBalancing**](/windows/desktop/api/sbtsv/nn-sbtsv-itssbloadbalancing)
</dt> <dd>

Exposes methods you can use to provide a custom load-balancing algorithm.

</dd> <dt>

[**ITsSbLoadBalancingNotifySink**](/windows/desktop/api/sbtsv/nn-sbtsv-itssbloadbalancingnotifysink)
</dt> <dd>

Exposes methods that return the result of a load-balancing algorithm to RD Connection Broker.

</dd> <dt>

[**ITsSbOrchestration**](/windows/desktop/api/sbtsv/nn-sbtsv-itssborchestration)
</dt> <dd>

Exposes methods that RD Connection Broker uses to ensure that the target is ready before a client is redirected to it.

</dd> <dt>

[**ITsSbOrchestrationNotifySink**](/windows/desktop/api/sbtsv/nn-sbtsv-itssborchestrationnotifysink)
</dt> <dd>

Exposes methods that return an [**ITsSbTarget**](/windows/desktop/api/sbtsv/nn-sbtsv-itssbtarget) object to RD Connection Broker after the target is successfully prepared for a connection.

</dd> <dt>

[**ITsSbPlacement**](/windows/desktop/api/sbtsv/nn-sbtsv-itssbplacement)
</dt> <dd>

Exposes methods that prepare the environment (the computer that hosts the virtual machine).

</dd> <dt>

[**ITsSbPlacementNotifySink**](/windows/desktop/api/sbtsv/nn-sbtsv-itssbplacementnotifysink)
</dt> <dd>

Exposes methods that return information about environments to RD Connection Broker.

</dd> <dt>

[**ITsSbPlugin**](/windows/desktop/api/sbtsv/nn-sbtsv-itssbplugin)
</dt> <dd>

Exposes methods that initialize and terminate plug-ins.

</dd> <dt>

[**ITsSbPluginNotifySink**](/windows/desktop/api/sbtsv/nn-sbtsv-itssbpluginnotifysink)
</dt> <dd>

Exposes methods that notify RD Connection Broker about initialization or termination of a plug-in.

</dd> <dt>

[**ITsSbPluginPropertySet**](/windows/win32/api/sbtsv/nn-sbtsv-itssbpluginpropertyset)
</dt> <dd>

Can be used to define custom plug-in properties as appropriate.

</dd> <dt>

[**ITsSbPropertySet**](/windows/win32/api/sbtsv/nn-sbtsv-itssbpropertyset)
</dt> <dd>

Can be used to define custom properties as appropriate.

</dd> <dt>

[**ITsSbProvider**](/windows/desktop/api/sbtsv/nn-sbtsv-itssbprovider)
</dt> <dd>

Exposes methods that create default implementations of objects that are used in Remote Desktop Virtualization.

</dd> <dt>

[**ITsSbProvisioning**](/windows/desktop/api/sbtsv/nn-sbtsv-itssbprovisioning)
</dt> <dd>

Exposes methods that create and maintain virtual machines.

</dd> <dt>

[**ITsSbProvisioningPluginNotifySink**](/windows/desktop/api/sbtsv/nn-sbtsv-itssbprovisioningpluginnotifysink)
</dt> <dd>

Exposes methods that notify RD Connection Broker about the provisioning of virtual machines.

</dd> <dt>

[**ITsSbResourceNotification**](/windows/desktop/api/sbtsv/nn-sbtsv-itssbresourcenotification)
</dt> <dd>

Exposes methods that RD Connection Broker uses to notify plug-ins of any state changes that occur in the session, target, and client connection objects.

</dd> <dt>

[**ITsSbResourceNotificationEx**](/windows/desktop/api/sbtsv/nn-sbtsv-itssbresourcenotificationex)
</dt> <dd>

Exposes methods that RD Connection Broker uses to notify plug-ins of any state changes that occur in the session, target, and client connection objects.

</dd> <dt>

[**ITsSbResourcePlugin**](/windows/win32/api/sbtsv/nn-sbtsv-itssbresourceplugin)
</dt> <dd>

Exposes methods that extend the capabilities of RD Connection Broker.

</dd> <dt>

[**ITsSbResourcePluginStore**](/windows/desktop/api/sbtsv/nn-sbtsv-itssbresourcepluginstore)
</dt> <dd>

Exposes methods that enable resource plug-ins to store objects such as sessions and targets.

</dd> <dt>

[**ITsSbResourcePluginStoreEx**](itssbresourcepluginstoreex.md)
</dt> <dd>

Exposes methods that enable resource plug-ins to store objects such as sessions and targets.

</dd> <dt>

[**ITsSbServiceNotification**](/windows/desktop/api/sbtsv/nn-sbtsv-itssbservicenotification)
</dt> <dd>

Exposes methods that RD Connection Broker uses to notify plug-ins of state changes that occur in the RD Connection Broker itself.

</dd> <dt>

[**ITsSbSession**](/windows/desktop/api/sbtsv/nn-sbtsv-itssbsession)
</dt> <dd>

Exposes properties that store information about a user session.

</dd> <dt>

[**ITsSbTarget**](/windows/desktop/api/sbtsv/nn-sbtsv-itssbtarget)
</dt> <dd>

Exposes properties that store configuration and state information about a target.

</dd> <dt>

[**ITsSbTargetEx**](itssbtargetex.md)
</dt> <dd>

Exposes properties that store configuration and state information about a target.

</dd> <dt>

[**ITsSbTargetPropertySet**](/windows/win32/api/sbtsv/nn-sbtsv-itssbtargetpropertyset)
</dt> <dd>

Derive from this interface to define a custom target property set.

</dd> <dt>

[**ITsSbTaskInfo**](/windows/desktop/api/sbtsv/nn-sbtsv-itssbtaskinfo)
</dt> <dd>

Exposes properties that the Remote Desktop Connection Broker uses to set a plugin’s queue.

</dd> <dt>

[**ITsSbTaskPlugin**](/windows/desktop/api/sbtsv/nn-sbtsv-itssbtaskplugin)
</dt> <dd>

Exposes methods that update the queue of tasks for Remote Desktop Connection Broker plugins.

</dd> <dt>

[**ITsSbTaskPluginNotifySink**](/windows/desktop/api/sbtsv/nn-sbtsv-itssbtaskpluginnotifysink)
</dt> <dd>

Exposes methods that report status and error messages about tasks to RD Connection Broker.

</dd> <dt>

[**IWTSSBPlugin**](/windows/desktop/api/Tssbx/nn-tssbx-iwtssbplugin)
</dt> <dd>

Used to extend the capabilities of Terminal Services Session Broker (TS Session Broker). Implement this interface when you want to provide a plug-in that overrides the redirection logic of TS Session Broker.

</dd> </dl>

 

 