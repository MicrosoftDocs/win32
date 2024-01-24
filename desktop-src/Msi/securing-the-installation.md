---
description: Add all of the Password properties from the CustomUserAccounts table to the MsiHiddenProperties property in the Property table.
ms.assetid: 682f534c-10a2-4260-b21d-7075d8c1620c
title: Securing the Installation
ms.topic: article
ms.date: 05/31/2018
---

# Securing the Installation

Add all of the Password properties from the CustomUserAccounts table to the [**MsiHiddenProperties**](msihiddenproperties.md) property in the [Property table](property-table.md). Add the names of the deferred custom actions to the **MsiHiddenProperties** property as well. This will prevent the installer from writing the sensitive property values (the passwords) into the log and will ensure these values are not logged when the deferred custom actions use the values as the CustomActionData property.

For the user's password to be available in the Windows Installer service, the password property must be added to the [**SecureCustomProperties**](securecustomproperties.md) property.

[Property Table](property-table.md)



| Property                                                 | Value                                                        |
|----------------------------------------------------------|--------------------------------------------------------------|
| [**MsiHiddenProperties**](msihiddenproperties.md)       | TESTUSERPASSWORD;CreateAccount;RemoveAccount;RollbackAccount |
| [**SecureCustomProperties**](securecustomproperties.md) | TESTUSERPASSWORD                                             |



 

This concludes the sample.

 

 



