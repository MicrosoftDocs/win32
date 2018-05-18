---
Description: 'To use properties in your installation, you can get and set property values from programs using MsiGetProperty and MsiSetProperty and include as part of conditional statements in the installation database.'
ms.assetid: '65fe46d7-16b6-46ef-a440-73f954b03105'
title: Getting and Setting Properties
---

# Getting and Setting Properties

To use [properties](properties.md) in your installation, you can get and set property values from programs using [**MsiGetProperty**](msigetproperty.md) and [**MsiSetProperty**](msisetproperty.md) and include as part of conditional statements in the installation database.

-   To obtain a current property, call the [**MsiGetProperty**](msigetproperty.md) function.
-   To obtain the current installation state, call the [**MsiGetMode**](msigetmode.md) function.
-   To obtain the language for the current installation, call the [**MsiGetLanguage**](msigetlanguage.md) function.
-   To set a property, call the [**MsiSetProperty**](msisetproperty.md) function.
-   To set the installation state, call the [**MsiSetMode**](msisetmode.md) function.
-   To clear a property (setting it to Null), set the property's value to an empty string: "".

## Related topics

<dl> <dt>

[Using Properties](using-properties.md)
</dt> <dt>

[Setting Public Property Values on the Command Line](setting-public-property-values-on-the-command-line.md)
</dt> <dt>

[Clearing an Installer Property](clearing-an-installer-property.md)
</dt> </dl>

 

 



