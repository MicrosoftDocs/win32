---
description: To use properties in your installation, you can get and set property values from programs using MsiGetProperty and MsiSetProperty and include as part of conditional statements in the installation database.
ms.assetid: 65fe46d7-16b6-46ef-a440-73f954b03105
title: Getting and Setting Properties (Windows Installer)
ms.topic: article
ms.date: 05/31/2018
---

# Getting and Setting Properties (Windows Installer)

To use [properties](properties.md) in your installation, you can get and set property values from programs using [**MsiGetProperty**](/windows/desktop/api/Msiquery/nf-msiquery-msigetpropertya) and [**MsiSetProperty**](/windows/desktop/api/Msiquery/nf-msiquery-msisetpropertya) and include as part of conditional statements in the installation database.

-   To obtain a current property, call the [**MsiGetProperty**](/windows/desktop/api/Msiquery/nf-msiquery-msigetpropertya) function.
-   To obtain the current installation state, call the [**MsiGetMode**](/windows/desktop/api/Msiquery/nf-msiquery-msigetmode) function.
-   To obtain the language for the current installation, call the [**MsiGetLanguage**](/windows/desktop/api/Msiquery/nf-msiquery-msigetlanguage) function.
-   To set a property, call the [**MsiSetProperty**](/windows/desktop/api/Msiquery/nf-msiquery-msisetpropertya) function.
-   To set the installation state, call the [**MsiSetMode**](/windows/desktop/api/Msiquery/nf-msiquery-msisetmode) function.
-   To clear a property (setting it to Null), set the property's value to an empty string: "".

## Related topics

<dl> <dt>

[Using Properties](using-properties.md)
</dt> <dt>

[Setting Public Property Values on the Command Line](setting-public-property-values-on-the-command-line.md)
</dt> <dt>

[Clearing an Installer Property](clearing-an-installer-property.md)
</dt> </dl>

 

 



