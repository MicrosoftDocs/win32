---
description: To retrieve data from the registry, an application typically enumerates the subkeys of a key until it finds a particular one and then retrieves data from the value or values associated with it.
ms.assetid: ce4be388-5506-4d01-a73c-33372ef4ccd7
title: Retrieving Data from the Registry
ms.topic: article
ms.date: 05/31/2018
---

# Retrieving Data from the Registry

To retrieve data from the registry, an application typically enumerates the subkeys of a key until it finds a particular one and then retrieves data from the value or values associated with it. An application can call the [**RegEnumKeyEx**](/windows/desktop/api/Winreg/nf-winreg-regenumkeyexa) function to enumerate the subkeys of a given key.

To retrieve detailed data about a particular subkey, an application can call the [**RegQueryInfoKey**](/windows/desktop/api/Winreg/nf-winreg-regqueryinfokeya) function. The [**RegGetKeySecurity**](/windows/desktop/api/winreg/nf-winreg-reggetkeysecurity) function retrieves a copy of the security descriptor protecting a key.

An application can use the [**RegEnumValue**](/windows/desktop/api/Winreg/nf-winreg-regenumvaluea) function to enumerate the values for a given key, and [**RegQueryValueEx**](/windows/desktop/api/Winreg/nf-winreg-regqueryvalueexa) function to retrieve a particular value for a key. An application typically calls **RegEnumValue** to determine the value names and then **RegQueryValueEx** to retrieve the data for the names.

The [**RegQueryMultipleValues**](/windows/desktop/api/Winreg/nf-winreg-regquerymultiplevaluesa) function retrieves the type and data for a list of value names associated with an open registry key. This function is useful for dynamic key providers because it assures consistency of data by retrieving multiple values in an atomic operation.

Because other applications can change the data in a registry value between the time your application can read a value and use it, you may need to ensure your application has the latest data. You can use the [**RegNotifyChangeKeyValue**](/windows/desktop/api/Winreg/nf-winreg-regnotifychangekeyvalue) function to notify the calling thread when there are changes to the attributes or contents of a registry key, or if the key is deleted. The function signals an event object to notify the caller. If the thread that calls **RegNotifyChangeKeyValue** exits, the event is signaled and the monitoring of the registry key is stopped.

You can control or specify what changes should be reported through the use of a notify filter or flag. Usually, changes are reported by signaling an event that you specify to the function. Note that the [**RegNotifyChangeKeyValue**](/windows/desktop/api/Winreg/nf-winreg-regnotifychangekeyvalue) function does not work with remote handles.

To monitor registry operations in more detail, see [**Registry**](/windows/desktop/ETW/registry).

 

 
