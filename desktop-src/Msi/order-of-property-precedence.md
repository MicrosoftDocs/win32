---
description: The installer sets properties using the following order of precedence. A property value in this list can override a value that comes after it and be overridden by a value coming before it in the list.
ms.assetid: ba9240fe-2e5a-43f5-8cdf-59dd6348092b
title: Order of Property Precedence
ms.topic: article
ms.date: 05/31/2018
---

# Order of Property Precedence

The installer sets properties using the following order of precedence. A property value in this list can override a value that comes after it and be overridden by a value coming before it in the list.

1.  Properties specified by the operating environment.
2.  [Public properties](public-properties.md) set on the command line.
3.  Public properties listed by the [**AdminProperties**](adminproperties.md) propertyset during an [administrative installation](administrative-installation.md) .
4.  Public or private properties set during the application of a [*transform*](t-gly.md).
5.  Public or private property that set by authoring the [Property table](property-table.md) of the .msi file.

## Related topics

<dl> <dt>

[About Properties](about-properties.md)
</dt> </dl>

 

 



