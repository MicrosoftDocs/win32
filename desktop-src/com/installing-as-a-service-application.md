---
title: Installing as a Service Application
description: Installing as a Service Application
ms.assetid: 0dd4b348-3d12-49ba-8098-4adb9df01a0e
ms.topic: article
ms.date: 05/31/2018
---

# Installing as a Service Application

In addition to running as a local server executable (EXE), a COM object may also package itself to run as a service application when activated by a local or remote client. Services support numerous useful and user interfaceâ€“integrated administrative features, including local and remote starting, stopping, pausing, and restarting, as well as the ability to establish the server to run under a specific [user account](/windows/desktop/Services/service-user-accounts) and [window station](/windows/desktop/winstation/window-stations).

An object written as a service is installed for use by COM by establishing a [LocalService](localservice.md) value under its [AppID](appid-key.md) key and performing a standard service installation.

Classes may also be configured to run under a specific user account when activated by a remote client without being written as a service application. To do this, the class installs a user name and a password to be used when the SCM launches its local server process.

When a class is configured in this fashion, calls to [**CoRegisterClassObject**](/windows/desktop/api/combaseapi/nf-combaseapi-coregisterclassobject) with this CLSID will fail unless the process was launched by COM on behalf of an actual activation request. In other words, classes configured to run as a particular user may not be registered under any other identity.

The user name is taken from the [RunAs](runas.md) named-value under the class's APPID key. If the user name is "Interactive User", the class code is run in the security context of the currently logged on user and is connected to the interactive window station.

Otherwise, the password is retrieved from a hidden portion of the registry available only to administrators of the machine and to the system. The user name and password are then used to create a logon session in which the class code is run. When launched in this way, the class code runs with its own desktop and window-station and does not share window handles, the clipboard, or other user interface elements with the interactive user or other classes running in other user accounts.

A server registered either with **LocalService** or **RunAs** can register an object in the running object table to allow any client to connect to it. To do so, the server's call to [**IRunningObjectTable::Register**](/windows/desktop/api/ObjIdl/nf-objidl-irunningobjecttable-register) must set the ROTFLAGS\_ALLOWANYCLIENT flag. A server setting this bit must have its executable name in the AppID section of the registry that refers to the AppID for the executable. An "activate as activator" server (not registered as either **LocalService** or **RunAs**) may not register an object with this flag.

## Related topics

<dl> <dt>

[Registering a Class at Installation](registering-a-class-at-installation.md)
</dt> <dt>

[Registering a Running EXE Server](registering-a-running-exe-server.md)
</dt> <dt>

[Registering Objects in the ROT](registering-objects-in-the-rot.md)
</dt> <dt>

[Self-Registration](self-registration.md)
</dt> </dl>

 

 