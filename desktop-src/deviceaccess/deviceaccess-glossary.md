---
title: Device Access Glossary
description: The following are terms used throughout the documentation for the Device Access API.
Robots: noindex, nofollow
ms.assetid: A6311538-D7CC-4A23-A145-14AF3BBFC4C4
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Device Access Glossary

The following are terms used throughout the documentation for the Device Access API.

<dl> <dt>

<span id="deviceaccess.appcontainer"></span><span id="DEVICEACCESS.APPCONTAINER"></span>**AppContainer**
</dt> <dd>

A highly restricted execution environment in which a process runs with a reduced subset of the user's privileges. A process that's running within an AppContainer is called an AppContainer process. An AppContainer process is isolated from other AppContainer processes and from the user's profile. It has limited access to a very small subset of system resources like files, devices, registry keys, interprocess communication (IPC)/remote procedure call (RPC) endpoints, and network resources.

</dd> <dt>

<span id="deviceaccess.binding"></span><span id="DEVICEACCESS.BINDING"></span>**Binding**
</dt> <dd>

Associating a device access object with a particular device interface. If binding is successful, Windows Store apps can use the device access object as a broker to communicate with the device driver.

</dd> <dt>

<span id="deviceaccess.broker"></span><span id="DEVICEACCESS.BROKER"></span>**Broker**
</dt> <dd>

A component that provides access to a resource that isn't granted by default.

</dd> <dt>

<span id="deviceaccess.privilegedapp"></span><span id="DEVICEACCESS.PRIVILEGEDAPP"></span>**Privileged App**
</dt> <dd>

An app that's identified in a particular device's metadata as associated with that device, so that it can communicate with the device driver's restricted interface. An example of such an app might be a proprietary music playback app that has exclusive permission to sync with a portable music player, when apps from competitors can't. For more information about how to set a device's metadata or how to restrict a driver to privileged apps, see [Device Experience for Specialized Devices](http://go.microsoft.com/fwlink/p/?linkid=242009).

</dd> </dl>

 

 




