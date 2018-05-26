---
title: Extendable Node Types
description: To extend the Active Directory Manager, register the node type that you want to extend.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 26e4a44b-b71b-47c2-b796-379cd5676cec
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- extendable node types MMC
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Extendable Node Types

To extend the Active Directory Manager, register the node type that you want to extend. Be aware that Active Directory Manager does not register all possible node types that it can display because the schema for the Active Directory Manager is extensible. For Active Directory Manager, the GUID for the node type is the GUID stored in the schemaIDGUID property of the classSchema object that represents the type of object you want to extend. For example, if you want to add a context menu item to the **Tasks** menu of user objects in Active Directory Manager, use the COM string representation of the GUID. This representation is stored in the schemaIDGUID property of the user classSchema object as the node-type GUID.

For more information, see [Registering Node Type](registering-node-type.md).

 

 




