---
title: NetShell Helpers
description: NetShell helpers are DLL files that provide the functionality of a context.
ms.assetid: 'b1c68db7-0a24-4db7-97dc-799147739ff1'
keywords: ["helper NetSh", "NetShell NetSh , described, helper", "components NetSh , helper"]
---

# NetShell Helpers

NetShell helpers are DLL files that provide the functionality of a context. Additional helpers extend the functionality of NetShell by providing administrative scripting for networking tasks. Helpers generally provide configuration support, monitoring support, or both, for networking services, utilities, or protocols.

NetShell helpers can also be created to extend the functionality of another helper. For example, the **ras** context has subcontexts for **ip** and **ipx**. Those subcontexts could be created as separate helpers designed specifically to extend the configuration or monitoring support of their respective areas of **ras**.

NetShell discovers which helpers are available on a system by reading the registry for a list of installed helpers. NetShell also provides commands that enable dynamic updates of the list of installed helpers. For more information about using NetShell, see Online Help or the Windows XP Resource Kit.

 

 




