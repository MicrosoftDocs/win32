---
description: The pluggable terminals are classified into Terminal Superclasses.
ms.assetid: 0ab2896e-3634-47f7-b1f4-e7d1ffcb3592
title: Registry Entries (Telephony API)
ms.topic: article
ms.date: 05/31/2018
---

# Registry Entries (Telephony API)

The pluggable terminals are classified into Terminal Superclasses. Each Terminal Superclass has an entry in the registry under the following key:

**HKEY\_LOCAL\_MACHINE**\\**SOFTWARE**\\**Microsoft**\\**Windows**\\**CurrentVersion**\\**Telephony**\\**TerminalManager**

Below the Terminal Superclass key are entries for each pluggable terminal within the Terminal Superclass.

The entry for each Terminal Superclass is identified by a Terminal Superclass CLSID. This is a unique identifier for a terminal class. The terminal class has an optional attribute: name, which is a friendly name for the terminal class. Each pluggable terminal is identified by a CLSID Terminal class; that is, a GUID. The attributes for pluggable terminal are stored into pluggable terminal key values. The attributes for a pluggable terminal are the following.



| Terminal class | Key name | Public identifier                                                                 |
|----------------|----------|-----------------------------------------------------------------------------------|
| Name           | REG\_SZ  | Terminal friendly name                                                            |
| Company        | REG\_SZ  | Company name                                                                      |
| Version        | REG\_SZ  | Version information                                                               |
| CLSID          | REG\_SZ  | Terminal CLSID (used in COM [**CoCreateInstance**](/windows/win32/api/combaseapi/nf-combaseapi-cocreateinstance) method) |
| Directions     | DWORD    | Terminal direction                                                                |
| MediaTypes     | DWORD    | Terminal media types supported                                                    |



 

For a terminal class the attributes are the following.



| CLSID | Key name | Public identifier            |
|-------|----------|------------------------------|
| Name  | REG\_SZ  | Terminal class friendly name |



 

 

 
