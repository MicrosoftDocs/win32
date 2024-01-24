---
description: A qualified component is a method of single-level indirection, similar to a pointer.
ms.assetid: b483fa7d-d31d-4855-89e5-f733541cd92d
title: Qualified Components
ms.topic: article
ms.date: 05/31/2018
---

# Qualified Components

A qualified component is a method of single-level indirection, similar to a pointer. Qualified components are primarily used to group components with parallel functionality into categories. For example, if you have 30 components listed in the [Component table](component-table.md) that are the same Microsoft Word fax template localized into 30 languages, you can group these together into a category of qualified components by using the [PublishComponent table](publishcomponent-table.md).

Qualified components are entered in the Component table in the same way as ordinary components. Every component must have a unique component ID GUID and component identifier specified in the Component table. In addition, qualified components are associated with a category GUID and a text-string qualifier in the PublishComponent table. Qualified components are referenced by the category GUID and the qualifier, which just points to the ordinary component in the Component table.

For example, a qualified component ID GUID can point to different language versions of a resource DLL. In this case, the group of localized resource DLLs comprises the category and the numeric locale identifiers (LCID) strings are commonly used as the qualifiers. A developer could author an installation package that uses these qualified components to do the following:

-   Find the path to a particular language version of the resource DLL using [**MsiProvideQualifiedComponent**](/windows/desktop/api/Msi/nf-msi-msiprovidequalifiedcomponenta) or [**MsiProvideQualifiedComponentEx**](/windows/desktop/api/Msi/nf-msi-msiprovidequalifiedcomponentexa) and install the resource.
-   Determine all of the language versions of the resource DLL that are present by calling [**MsiEnumComponentQualifiers**](/windows/desktop/api/Msi/nf-msi-msienumcomponentqualifiersa).
-   Prepare the application to support additional languages. A future language pack for the application can use the qualified component to add more language versions of the resource DLL.

For more information, see [Using Qualified Components](using-qualified-components.md).

 

 



