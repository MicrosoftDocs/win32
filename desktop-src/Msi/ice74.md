---
description: ICE74 verifies that the FASTOEM property has not been authored into the Property table.
ms.assetid: 2af132f0-0ffa-405f-9d05-7cb5d5f826b8
title: ICE74
ms.topic: article
ms.date: 05/31/2018
---

# ICE74

ICE74 verifies that the [**FASTOEM**](fastoem.md) property has not been authored into the [Property table](property-table.md).

The [**FASTOEM**](fastoem.md) property enables OEMs to reduce the time required to install Windows Installer applications for the first time. It cannot be used after the first install. The **FASTOEM** property must not be authored in the Property table because this interferes with subsequent installations for the maintenance, removal, or repair of the application.

ICE74 also verifies that the [**UpgradeCode**](upgradecode.md) property is authored into the [Property table](property-table.md), and that its value is not a null GUID, {00000000-0000-0000-0000-000000000000}.

## Result

ICE74 can post the following errors.



| ICE74 error                                                                       | Description                                                                                             |
|-----------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------|
| The [**FASTOEM**](fastoem.md) property cannot be authored in the Property table. | The [**FASTOEM**](fastoem.md) property has been set in the Property table.                             |
| '\[2\]' is not a valid [**UpgradeCode**](upgradecode.md).                        | A null GUID has been entered for the [**UpgradeCode**](upgradecode.md) property in the Property table. |



 

ICE74 can post the following warning.



| ICE74 warning                                                                                                                                                                                             | Description                                                                            |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|
| The [**UpgradeCode**](upgradecode.md) property is not authored in the Property table. It is strongly recommended that authors of installation packages specify an **UpgradeCode** for their application. | The [**UpgradeCode**](upgradecode.md) property is not authored in the Property table. |



 

## Example

ICE74 reports the following error if the [**FASTOEM**](fastoem.md) property is set: The FASTOEM

``` syntax
 property cannot be authored in the Property table.
```

[Property Table](property-table.md) (partial)



| Property                   | Value |
|----------------------------|-------|
| [**FASTOEM**](fastoem.md) | 1     |



 

To fix this error remove the [**FASTOEM**](fastoem.md) property from the Property Table.

## Related topics

<dl> <dt>

[**FASTOEM property**](fastoem.md)
</dt> <dt>

[Property table](property-table.md)
</dt> <dt>

[ICE Reference](ice-reference.md)
</dt> </dl>

 

 



