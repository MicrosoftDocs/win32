---
description: The SCM maintains a database of installed services in the registry.
ms.assetid: 70f24e15-2607-4c32-9192-a9413b74558b
title: Database of Installed Services
ms.topic: article
ms.date: 05/31/2018
---

# Database of Installed Services

The SCM maintains a database of installed services in the registry. The database is used by the SCM and programs that add, modify, or configure services. The following is the registry key for this database: **HKEY\_LOCAL\_MACHINE\\SYSTEM\\CurrentControlSet\\Services**.

This key contains a subkey for each installed service and driver service. The name of the subkey is the name of the service, as specified by the [**CreateService**](/windows/desktop/api/Winsvc/nf-winsvc-createservicea) function when the service was installed by a service configuration program.

An initial copy of the database is created when the system is installed. The database contains entries for the device drivers required during system boot. The database includes the following information about each installed service and driver service:

-   The service type. This indicates whether the service executes in its own process or shares a process with other services. For driver services, this indicates whether the service is a kernel driver or a file system driver.
-   The start type. This indicates whether the service or driver service is started automatically at system startup (auto-start service) or whether the SCM starts it when requested by a service control program (demand-start service). The start type can also indicate that the service or driver service is disabled, in which case it cannot be started.
-   The error control level. This specifies the severity of the error if the service or driver service fails to start during system startup and determines the action that the startup program will take.
-   The fully qualified path of the executable file. The filename extension is .EXE for services and .SYS for driver services.
-   Optional dependency information used to determine the proper order for starting services or driver services. For services, this information can include a list of services that the SCM must start before it can start the specified service, the name of a load ordering group that the service is part of, and a tag identifier that indicates the start order of the service in its load ordering group. For driver services, this information includes a list of drivers that must be started before the specified driver.
-   For services, an optional account name and password. The service program runs in the context of this account. If no account is specified, the service executes in the context of the [LocalSystem account](localsystem-account.md).
-   For driver services, an optional driver object name (for example, \\FileSystem\\Rdr or \\Driver\\Xns), used by the I/O system to load the device driver. If no name is specified, the I/O system creates a default name based on the driver service name.

> [!Note]  
> This database is also known as the ServicesActive database or the SCM database. You must use the functions provided by the SCM, instead of modifying the database directly.

 

 

 



