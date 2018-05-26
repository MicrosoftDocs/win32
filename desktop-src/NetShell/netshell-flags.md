---
title: NetShell Flags
description: Commands can specify their scope or constraints through the use of flags. The following table defines valid flags for NetShell helper commands. These flags are set through the CMD\_ENTRY or CMD\_GROUP\_ENTRY structures, or their associated macros.
ms.assetid: 61dfa4ae-cf70-4858-be10-f77a318eaa28
keywords:
- flags NetSh
- helper NetSh , implementing, flags
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# NetShell Flags

Commands can specify their scope or constraints through the use of flags. The following table defines valid flags for NetShell helper commands. These flags are set through the [**CMD\_ENTRY**](/windows/previous-versions/Netsh/ns-netsh-_cmd_entry?branch=master) or [**CMD\_GROUP\_ENTRY**](/windows/previous-versions/Netsh/ns-netsh-_cmd_group_entry?branch=master) structures, or their associated macros.

The following flags can be specified for a command, in any combination.



| Flag                   | Meaning                                                                                                                                                                                      |
|------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CMD\_FLAG\_PRIVATE     | Indicates the command is valid directly from its context only. If not set, the command is inherited by all subcontexts. This is the only flag set by default for commands added by a helper. |
| CMD\_FLAG\_INTERACTIVE | Indicates the context is available only when NetShell is run in interactive mode, and not available to be passed to NetShell on the command line.                                            |
| CMD\_FLAG\_LOCAL       | Indicates the command is not valid from a remote machine.                                                                                                                                    |
| CMD\_FLAG\_ONLINE      | Indicates the command is not valid in offline mode.                                                                                                                                          |
| CMD\_FLAG\_PRIORITY    | Indicates the **ulPriority** member of the [**NS\_CONTEXT\_ATTRIBUTES**](/windows/previous-versions/Netsh/ns-netsh-_ns_context_attributes?branch=master) structure is used.                                                                       |



 

 

 




