---
description: The ProductLanguage property must be updated to the numeric language identifier (LANGID) for the new language.
ms.assetid: e00ef69b-c54b-41de-9230-a7582b260891
title: Updating ProductLanguage and ProductCode Properties
ms.topic: article
ms.date: 05/31/2018
---

# Updating ProductLanguage and ProductCode Properties

The [**ProductLanguage**](productlanguage.md) property must be updated to the numeric language identifier (LANGID) for the new language. In the case of the localization example, the value of the **ProductLanguage** property must be changed from the LANGID for English (1033) to the LANGID for French (1036) in the [Property table](property-table.md).

The value of the [**ProductCode**](productcode.md) property in the [Property table](property-table.md) must be changed to a new, unique value when localizing a database because a localized product is considered a different product. For example, the German and English versions of an application are considered two different products and must have different product codes. See [Product Codes](product-codes.md).

Use your database table editor to update the values of the ProductCode and ProductLanguage properties in the Property table. Do not reuse the GUID shown if you copy this example.

[Property Table](property-table.md)



| Property                                   | Value                                  |
|--------------------------------------------|----------------------------------------|
| [**ProductCode**](productcode.md)         | {EE389960-E426-4EEA-B669-AD8129249881} |
| [**ProductLanguage**](productlanguage.md) | 1036                                   |



 

[Continue](updating-a-summary-information-stream.md)

 

 



