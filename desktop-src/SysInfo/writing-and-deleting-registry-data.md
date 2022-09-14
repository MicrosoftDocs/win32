---
description: An application can use the RegSetValueEx function to associate a value and its data with a key. For a list of the value types supported by RegSetValueEx, see Registry Value Types.
ms.assetid: 75ac826a-f169-400c-b6d6-3e3ec9ebf996
title: Writing and Deleting Registry Data
ms.topic: article
ms.date: 05/31/2018
---

# Writing and Deleting Registry Data

An application can use the [**RegSetValueEx**](/windows/desktop/api/Winreg/nf-winreg-regsetvalueexa) function to associate a value and its data with a key. For a list of the value types supported by **RegSetValueEx**, see [Registry Value Types](registry-value-types.md).

To delete a value from a key, an application can use the [**RegDeleteValue**](/windows/desktop/api/Winreg/nf-winreg-regdeletevaluea) function. To delete a key, it can use the [**RegDeleteKey**](/windows/desktop/api/Winreg/nf-winreg-regdeletekeya) function. A deleted key is not removed until the last handle to it has been closed. Subkeys and values cannot be created under a deleted key.

It is not possible to lock a registry key during a write operation to synchronize access to the data. However, you can control access to a registry key using security attributes. For more information, see [Registry Key Security and Access Rights](registry-key-security-and-access-rights.md).

More than one registry operation can be performed within a single transaction. To associate a registry key with a transaction, an application can use the [**RegCreateKeyTransacted**](/windows/desktop/api/Winreg/nf-winreg-regcreatekeytransacteda) or [**RegOpenKeyTransacted**](/windows/desktop/api/Winreg/nf-winreg-regopenkeytransacteda) function. For more information about transactions, see [Kernel Transaction Manager](/windows/desktop/Ktm/kernel-transaction-manager-portal).

 

 
