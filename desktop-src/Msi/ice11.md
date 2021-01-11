---
description: The ICE11 is used with concurrent installations. Concurrent installations are not recommended for the installation of applications intended for release to the public. For information about concurrent installations please see Concurrent Installations.
ms.assetid: fbcc94fa-be94-4ad1-a3f0-ea7d50ee0a15
title: ICE11
ms.topic: article
ms.date: 05/31/2018
---

# ICE11

The ICE11 is used with concurrent installations. Concurrent installations are not recommended for the installation of applications intended for release to the public. For information about concurrent installations please see [Concurrent Installations](concurrent-installations.md).

## Result

ICE11 validates the Source column of the [CustomAction table](customaction-table.md) of concurrent installation custom actions. The Source column must contain a valid [GUID](guid.md) (MSI product code).

ICE11 posts an error if the Source column of the CustomAction table is authored incorrectly for concurrent installation custom actions.

## Example

ICE posts the following error messages for the example shown.

``` syntax
CustomAction: CA4 is a nested install of an advertised MSI.  The 'Source' must contain a valid MSI product code.  Current: ProductCode.
CustomAction: CA1 is a nested install of an advertised MSI.  It duplicates the ProductCode of the base MSI package.  Current: {BFB69273-F0AE-45C4-9853-0AF946714768}.
CustomAction: CA2 is a nested install of an advertised MSI.  The GUID must be all upper-case.  Current: {BFB69273-F0AE-55c5-9853-0AF946714768}.
```

[Property Table](property-table.md) (partial)



| Property        | Value                                  |
|-----------------|----------------------------------------|
| **ProductCode** | {BFB69273-F0AE-45C4-9853-0AF946714768} |



 

[CustomAction Table](customaction-table.md) (partial)



| CustomAction | Type | Source                                 |
|--------------|------|----------------------------------------|
| CA1          | 39   | {BFB69273-F0AE-45C4-9853-0AF946714768} |
| CA2          | 39   | {BFB69273-F0AE-55c5-9853-0AF946714768} |
| CA3          | 39   | {BFB69273-F0AE-66C6-9853-0AF946714768} |
| CA4          | 39   | ProductCode                            |



 

To fix the errors, for CA1, you cannot do a concurrent installation of the "base package". This would result in a recursive installation. This entry should be removed or the Source column should be changed to a GUID for an advertised MSI that differs from the base package's GUID. For CA2, make all characters of the GUID uppercase. Lastly, change CA4's Source column to reference a valid GUID of an advertised MSI.

## Related topics

<dl> <dt>

[Concurrent Installations](concurrent-installations.md)
</dt> <dt>

[ICE Reference](ice-reference.md)
</dt> </dl>

 

 



