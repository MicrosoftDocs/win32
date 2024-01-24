---
description: The Component Object Model (COM) is a binary standard for writing component software in a distributed computing environment.
ms.assetid: 5a282158-63b0-4c15-9bfc-0d61f5fe8716
title: Backing Up and Restoring the COM+ Class Registration Database Under VSS
ms.topic: article
ms.date: 05/31/2018
---

# Backing Up and Restoring the COM+ Class Registration Database Under VSS

The Component Object Model (COM) is a binary standard for writing component software in a distributed computing environment.

The original Win32 implementation stored component identifiers (GUIDs) and other COM state in the registry under **HKEY\_CLASSES\_ROOT\\CLSID**.

The current generation of the Component Object Model, COM+, offers a registry-independent database for storing component registration information: the COM+ Class Registration Database.

The COM+ Class Registration Database supports a VSS writer, which allows requesters to back up the registration database using data stored on a shadow-copied volume.

To restore the COM+ Registration Database, a requester must call the [ICOMAdminCatalog::RestoreREGDB](/windows/win32/api/comadmin/nf-comadmin-icomadmincatalog-restoreregdb) method.

For more information about the COM+ Registration Database writer, see [In-Box VSS Writers](in-box-vss-writers.md).

 

 
