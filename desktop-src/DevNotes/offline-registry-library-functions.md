---
description: The following are the offline registry library functions.
ms.assetid: 378811d2-064c-4d81-979e-392097d55baa
title: Offline Registry Library Functions
ms.topic: article
ms.date: 05/31/2018
---

# Offline Registry Library Functions

The following are the offline registry library functions.



| Function                                       | Description                                                                                                         |
|------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|
| [**ORCloseHive**](orclosehive.md)             | Closes the specified offline registry hive and frees memory allocated for the hive.                                 |
| [**ORCloseKey**](orclosekey.md)               | Closes a handle to the specified registry key in an offline registry hive.                                          |
| [**ORCreateHive**](orcreatehive.md)           | Creates an offline registry hive that contains a single empty root key.                                             |
| [**ORCreateKey**](orcreatekey.md)             | Creates the specified registry key in an offline registry hive. If the key already exists, the function opens it.   |
| [**ORDeleteKey**](ordeletekey.md)             | Deletes a subkey and its values from an offline registry hive.                                                      |
| [**ORDeleteValue**](ordeletevalue.md)         | Removes a value from the specified registry key in an offline registry hive.                                        |
| [**OREnumKey**](orenumkey.md)                 | Enumerates the subkeys of the specified open registry key in an offline registry hive.                              |
| [**OREnumValue**](orenumvalue.md)             | Enumerates the values for the specified open registry key in an offline registry hive.                              |
| [**ORGetKeySecurity**](orgetkeysecurity.md)   | Retrieves a copy of the security descriptor protecting the specified open registry key in an offline registry hive. |
| [**ORGetValue**](orgetvalue.md)               | Retrieves the type and data for the specified registry value in an offline registry hive.                           |
| [**ORGetVersion**](orgetversion.md)           | Retrieves the version of the offline registry library.                                                              |
| [**ORGetVirtualFlags**](orgetvirtualflags.md) | Retrieves the virtual flags on the specified open registry key in an offline registry hive.                         |
| [**OROpenHive**](oropenhive.md)               | Loads the specified hive file into memory and validates the hive.                                                   |
| [**OROpenKey**](oropenkey.md)                 | Opens the specified registry key in an offline registry hive.                                                       |
| [**ORQueryInfoKey**](orqueryinfokey.md)       | Retrieves information about the specified registry key in an offline registry hive.                                 |
| [**ORSaveHive**](orsavehive.md)               | Writes the specified offline registry hive to a file.                                                               |
| [**ORSetKeySecurity**](orsetkeysecurity.md)   | Sets the security of an open registry key in an offline registry hive.                                              |
| [**ORSetValue**](orsetvalue.md)               | Sets the data for the value of a specified registry key in an offline registry hive.                                |
| [**ORSetVirtualFlags**](orsetvirtualflags.md) | Sets virtualization flags on the specified open registry key in an offline registry hive.                           |



 

 

 



