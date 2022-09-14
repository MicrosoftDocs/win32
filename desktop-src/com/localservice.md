---
title: LocalService
description: Installs an object as a service application.
ms.assetid: e8086118-f956-4cc2-a0fb-3cebd2e66799
keywords:
- LocalService registry value COM
ms.topic: article
ms.date: 05/31/2018
---

# LocalService

Installs an object as a service application.

## Registry Entry

```
HKEY_LOCAL_MACHINE\SOFTWARE\Classes\AppID
   {AppID_GUID}
      LocalService = name
```

## Remarks

In addition to running as a local server executable (EXE), a COM object may also choose to package itself to run as a service application when activated by a local or remote client. Services support numerous useful and UI-integrated administrative features, including local and remote starting, stopping, pausing, and restarting, as well as the ability to establish the server to run under a specific user account and window station.

An object written as a service is installed for use by COM by establishing a **LocalService** value and performing a standard service installation. The **LocalService** value must be set to the service name, as configured in **HKEY\_LOCAL\_MACHINE\\System\\CurrentControlSet\\Services**, as the default **REG\_SZ** value.

When **LocalService** is set, any string assigned to [**ServiceParameters**](serviceparameters.md) is passed as a command-line argument to the service as it is being launched.

The service configuration is preferred in many situations where the capabilities of the local and remote service management APIs and user interface might be useful for the services that the object provides. For example, leveraging the existing administrative framework of the service architecture should be an obvious choice if the object is long-lived or readily supports concepts such as starting, stopping, resetting, or pausing.

Services can be dynamically configured and can be configured to run automatically when the machine boots, or to be launched when requested by a client application.

If you are implementing classes as services, you should be aware of the following points:

-   This value is used in preference to the [**LocalServer32**](localserver32.md) key for local and remote activation requestsâ€”if **LocalService** exists and refers to a valid service, the **LocalServer32** key is ignored.
-   Currently, only a single instance of a service application may be running at a given time on a computer. COM services must therefore register their class objects on launch using REGCLS\_MULTIPLEUSE to support multiple clients.
-   To launch and initialize properly, COM services configured to run automatically when a machine boots must include RPCSS in their list of dependent services.

## Related topics

<dl> <dt>

[Registering COM Servers](registering-com-servers.md)
</dt> <dt>

[**ServiceParameters**](serviceparameters.md)
</dt> <dt>

[Services](/windows/desktop/Services/services)
</dt> </dl>

 

 