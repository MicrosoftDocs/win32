---
description: 'This sample illustrates the layout of a .cub file containing two ICEs. The installer executes the custom actions in the sequence: ICE01 and ICE08.'
ms.assetid: 609cd16a-4421-4082-855d-229f5ba7117b
title: Sample .cub File
ms.topic: article
ms.date: 05/31/2018
---

# Sample .cub File

This sample illustrates the layout of a .cub file containing two [ICEs](internal-consistency-evaluators-ices.md). The installer executes the custom actions in the sequence: ICE01 and ICE08.

The custom action ICE01 is a [Custom Action Type 1](custom-action-type-1.md). It is an entry point to a DLL that is stored as a stream in the .cub file. This stream is listed in the Binary Table ice.dll.

The custom action ICE08 is a [Custom Action Type 6](custom-action-type-6.md). It is an entry point to a function in VBScript that is stored as a stream in the .cub file. This stream is listed in the Binary Table as ice.vbs.

[Binary Table](binary-table.md)



| Name    | Data                               |
|---------|------------------------------------|
| ice.vbs | Unformatted binary data of ice.vbs |
| ice.dll | Unformatted binary data of ice.dll |



 

[CustomAction Table](customaction-table.md)



| Action | Type | Source  | Target |
|--------|------|---------|--------|
| ICE01  | 1    | ice.dll | ICE01  |
| ICE08  | 6    | ice.vbs | ICE02  |



 

\_ICESequence Table



| Action | Condition | Sequence |
|--------|-----------|----------|
| ICE01  |           | 10       |
| ICE08  |           | 20       |



 

\_Special Table

ICE01 and ICE08 do not require the inclusion of special processing tables. When the .cub file contains special tables they must also be included in the \_Validation Table.

[\_Validation Table](-validation-table.md)



| Table         | Column    | Nullable | MinValue | MaxValue | KeyTable | KeyColumn | Category                         | Set | Description |
|---------------|-----------|----------|----------|----------|----------|-----------|----------------------------------|-----|-------------|
| Binary        | Name      | N        |          |          |          |           | [Identifier](identifier.md)     |     |             |
| Binary        | Data      | N        |          |          |          |           | [Binary](binary.md)             |     |             |
| CustomAction  | Action    | N        |          |          |          |           | [Identifier](identifier.md)     |     |             |
| CustomAction  | Type      | N        |          |          |          |           | [Integer](integer.md)           |     |             |
| CustomAction  | Source    | Y        |          |          |          |           | [CustomSource](customsource.md) |     |             |
| CustomAction  | Target    | Y        |          |          |          |           | [Formatted](formatted.md)       |     |             |
| \_ICESequence | Action    | N        |          |          |          |           | [Identifier](identifier.md)     |     |             |
| \_ICESequence | Condition | Y        |          |          |          |           | [Condition](condition.md)       |     |             |
| \_ICESequence | Sequence  | Y        |          |          |          |           | [Integer](integer.md)           |     |             |



 

 

 



