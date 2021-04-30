---
description: Qualified components are a method of indirection and can be used to group components with parallel functionality into categories.
ms.assetid: 45a05ab2-d951-415d-bdb8-cb0a73eb9967
title: Using Qualified Components
ms.topic: article
ms.date: 05/31/2018
---

# Using Qualified Components

Qualified components are a method of indirection and can be used to group components with parallel functionality into categories.

To return the full path and install a [qualified component](qualified-components.md), call [**MsiProvideQualifiedComponent**](/windows/desktop/api/Msi/nf-msi-msiprovidequalifiedcomponenta) or [**MsiProvideQualifiedComponentEx**](/windows/desktop/api/Msi/nf-msi-msiprovidequalifiedcomponentexa).

To enumerate all of the qualified component qualifiers and descriptive strings, call [**MsiEnumComponentQualifiers**](/windows/desktop/api/Msi/nf-msi-msienumcomponentqualifiersa).

**To group components together into a qualified-component category**

1.  There must be a record in the [Component table](component-table.md) for each component that is included in the new category of qualified components. Author the fields in the Component table the same as for ordinary components. Note that each qualified component must have a unique component ID GUID entered in the ComponentId column of the Component table.
2.  Generate a qualifier text string for each qualified component. The qualifier must be unique text string that can be easily generated when searching for a qualified component. For example, if the components in the category are being qualified by language, the numeric locale identifier (LCID) is a reasonable qualifier string.
3.  Add a record in the [PublishComponent table](publishcomponent-table.md) for each qualified component. Enter the qualified-component identifiers from the Component column of the Component table into the Component\_ column of the PublishComponent table. Enter the qualifier strings for each qualified component into the Qualifier column. Enter a localized string to be displayed to the user and describing the qualified component into the optional AppData column. An explanatory string should be put in the AppData field, such as "French Dictionary," rather than just the numeric LCID. Enter the name of the feature that uses this component into the Feature\_ column. The feature identifier in this field must also be listed in the Feature column of the [Feature table](feature-table.md).
4.  Generate a category GUID for this category of qualified components. This must be a valid [GUID](guid.md). If you use a utility such as GUIDGEN to generate the GUID be sure that it contains only uppercase letters. For every qualified component in this category, enter the category GUID into the ComponentId field of the [PublishComponent table](publishcomponent-table.md).

The following example illustrates how the "FAX Templates" category of qualified components are authored into the Component, Feature, and PublishComponent tables.

[PublishComponent table](publishcomponent-table.md)



| ComponentId                  | Qualifier | AppData             | Feature\_   | Component\_    |
|------------------------------|-----------|---------------------|-------------|----------------|
| {FAX Template Category GUID} | 1033      | US English template | FAXTemplate | FAXTemplateENU |
|                              | 1041      | Japanese template   | FAXTemplate | FAXTemplateJPN |
|                              | 1054      | Thai template       | FAXTemplate | FAXTemplateTHA |
|                              | 1031      | German template     | FAXTemplate | FAXTemplateDEU |



 

[Component table](component-table.md) (partial table)



| Component      | ComponentId                                  |
|----------------|----------------------------------------------|
| FAXTemplateENU | {*FAX Template (US English) component GUID*} |
| FAXTemplateJPN | {*FAX Template (Japanese) component GUID*}   |
| FAXTemplateTHA | {*FAX Template (Thai) component GUID*}       |
| FAXTemplateDEU | {*FAX Template (German) component GUID*}     |



 

[Feature table](feature-table.md) (partial table)



| Feature     |
|-------------|
| FAXTemplate |
| FAXTemplate |
| FAXTemplate |
| FAXTemplate |



 

 

 



