---
description: After selecting the appropriate ICEs for validation, a developer must collect the custom actions together into an ICE database.
ms.assetid: 69151d5a-be6e-4947-862d-cea65306c536
title: Building an ICE Database
ms.topic: article
ms.date: 05/31/2018
---

# Building an ICE Database

After selecting the appropriate [ICEs](internal-consistency-evaluators-ices.md) for validation, a developer must collect the custom actions together into an ICE database. A .cub file is a standard .msi database that contains only ICEs and their required tables. A .cub file cannot be installed and is used only to store and provide access to ICE custom actions.

A .cub file contains the following database tables.



| Table                                  | Description                                                                                                                                                                                                                                                                |
|----------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Binary](binary-table.md)             | The script files, DLLs, and EXEs of the ICE customs actions that are referenced in the CustomAction table.                                                                                                                                                                 |
| [CustomAction](customaction-table.md) | Each record in this table corresponds to an ICE custom action included in the .cub file.                                                                                                                                                                                   |
| \_ICESequence                          | This table lists the ICE customs actions included in the .cub file in their execution sequence. The ICE custom actions listed in this table are executed by calling [**MsiSequence**](/windows/desktop/api/Msiquery/nf-msiquery-msisequencea), or individually executed using [**MsiDoAction**](/windows/desktop/api/Msiquery/nf-msiquery-msidoactiona). |
| [\_Validation](-validation-table.md)  | This table contains the .cub file entries that are to be merged into the \_Validation table.                                                                                                                                                                               |
| \_Special                              | Any special processing tables required by particular ICE custom actions must be included in the .cub file. The name of these tables must have a leading underscore.                                                                                                        |



 

See [Sample .cub File](sample--cub-file.md).

## Related topics

<dl> <dt>

[Building An ICE](building-an-ice.md)
</dt> </dl>

 

 



