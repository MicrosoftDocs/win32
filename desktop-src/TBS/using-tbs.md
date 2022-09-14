---
title: Using TBS
description: Each command submitted to the TBS is associated with a specific entity. This is accomplished by creating one or more contexts for an entity, which are then associated with each subsequent command submitted by that entity.
ms.assetid: 609f1e95-9868-4e34-8758-71306ac4e51f
keywords:
- TPM Base Services TBS , examples
- TPM Base Services TBS , using
ms.topic: article
ms.date: 05/31/2018
---

# Using TBS

The TPM Base Services feature is divided into four functional areas:

-   [Resource Virtualization](resource-virtualization.md)
-   [Command Scheduling](command-scheduling.md)
-   [Power Management](power-management.md)
-   [Command Blocking](command-blocking.md)

To ensure that different entities cannot access each other's resources, each command submitted to the TBS is associated with a specific entity. This is accomplished by creating one or more contexts for an entity, which are then associated with each subsequent command submitted by that entity. Each command includes a context object, which allows the TBS to execute TPM commands under the appropriate context. All objects created by commands are flushed from the TPM when the context is closed.

An entity creates the context before it first accesses the TBS and maintains the context until it is finished performing TBS accesses. For example, in the case of a TSS, the TCG core services (TCS) feature of the TSS would create a TBS context when it starts up, and it would keep that context active until it shuts down.

For Windows Server 2008 and Windows Vista, the TBS restricts access to the TBS API to the Administrators, NT AUTHORITY\\LocalService, and NT AUTHORITY\\NetworkService accounts. By default, these accounts are the only ones that can connect to TBS and create contexts. Access restrictions can be modified by creating a registry key **Access** with a string (**REG\_SZ**) registry value name **SecurityDescriptor** <dl> <dt>

Data type
</dt> <dd>REG_SZ</dd> </dl> under it as follows:

```
HKEY_LOCAL_MACHINE
   Software
      Microsoft
         TPM
            Access
               SecurityDescriptor = SecurityDescriptor
```

Example:

**O:BAG:BAD:(A;;0x00000001;;;BA)(A;;0x00000001;;;NS)(A;;0x00000001;;;LS)**

By default, the maximum number of contexts supported by the TBS is 25. This number can be altered by creating or modifying a **DWORD** registry value named **MaxContexts** under **HKEY\_LOCAL\_MACHINE**\\**Software**\\**Microsoft**\\**Tpm**. Real-time TBS context usage can be observed by using the performance monitor tool to track the number of TBS contexts.

For Windows 8, Windows Server 2012 and later, the TBS allows access to standard users and administrators. The **SecurityDescriptor** and **MaxContexts** registry keys became obsolete. For Windows 8, Windows Server 2012 and later, the TBS restricts access to certain commands using Command Blocking.

For Windows 10, version 1607, the TBS allows access from AppContainer applications. For each TPM version, the keys **BlockedAppContainerCommands** and **AllowedW8AppContainerCommands** have been added with the matching lists of blocked and allowed TPM commands, respectively.

For Windows 10, version 1803, the registry keys under **AllowedW8AppContainerCommands** are no longer supported.

 

 




