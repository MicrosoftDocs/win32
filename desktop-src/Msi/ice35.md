---
description: ICE35 validates that components containing compressed files stored in a cabinet file are not set to run from source. With Windows Installer 2.0 or later, this restriction has been removed.
ms.assetid: b4df27e2-9790-4b18-a173-25fa8b0ecd4d
title: ICE35
ms.topic: article
ms.date: 05/31/2018
---

# ICE35

ICE35 validates that components containing compressed files stored in a [cabinet file](cabinet-files.md) are not set to run from source. With Windows Installer 2.0 or later, this restriction has been removed.

ICE35 queries the Cabinet column of the [Media table](media-table.md) to determine which files are compressed and stored in a cabinet file. It queries the [File table](file-table.md) to determine which components contain these files. Finally, it checks the [Component table](component-table.md) to determine whether the run-from-source bits are set in the Attributes column.

## Result

ICE35 posts an error message if there is a compressed file stored in a cabinet file belonging to a component with the msidbComponentAttributesSourceOnly bit set in the Attributes column of the [Component table](component-table.md). With Windows Installer 2.0 or later, this is changed from an error to a warning message. A package that supports only Windows Installer 2.0 and later has the PID\_PAGECOUNT property of the Summary Information Stream set to a value of at least 200.

ICE35 posts warning message if there is a compressed file stored in a cabinet file belonging to a component with the msidbComponentAttributesOptional bit set in the Attributes column of the [Component table](component-table.md). This warning message has been removed with Windows Installer 2.0 and later.

If multiple files in a component are in a cabinet file, ICE35 reports errors for each file that has the run from source bit set.

## Example

ICE35 reports the following errors and warnings for the example shown using a version earlier than Windows Installer version 2.0.



| ICE35 Error                                                                                                | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ERROR: Component Component3 cannot be Run From Source only, because its member file 'File3' is compressed. | There is a compressed file stored in a cabinet file and this file belongs to a component with the SourceOnly bit set in the Attributes column of the [Component table](component-table.md). To fix this error change the lower 2 bits of Component2's Attributes value to "00", meaning Local only, or remove File4 from the CAB file.<br/>                                                                                                                                                                         |
| ERROR: Component Component3 cannot be Run From Source only, because its member file 'File3' is compressed. | There is a compressed file stored in a cabinet file and this file belongs to a component with the SourceOnly bit set in the Attributes column of the [Component table](component-table.md). Because the files in a component do not all have to originate from the same media, ICE35 reports errors for each file in the component that is in a cabinet.<br/> To fix this error change the lower 2 bits of Component2's Attributes value to "00", meaning Local only, or remove File4 from the CAB file.<br/> |



 

[Media Table](media-table.md) (partial)



| DiskID | LastSequence | Cabinet   |
|--------|--------------|-----------|
| 1      | 2            |           |
| 2      | 4            | One.cab   |
| 3      | 5            | \#Two.cab |



 

[File Table](file-table.md) (partial)



| File  | Component\_ | Sequence |
|-------|-------------|----------|
| File1 | Component1  | 1        |
| File2 | Component2  | 2        |
| File3 | Component2  | 3        |
| File4 | Component3  | 4        |
| File5 | Component3  | 5        |



 

[Component Table](component-table.md) (partial)



| Component  | Attributes |
|------------|------------|
| Component1 | 0          |
| Component2 | 2          |
| Component3 | 1          |



 

[Shortcut Table](shortcut-table.md) (partial)



| Shortcut  | Icon\_ |
|-----------|--------|
| Shortcut1 | Icon2  |



 

Note that files can also be marked as compressed using the [**Word Count Summary**](word-count-summary.md) Property of the [Summary Information stream](summary-information-stream.md).

## Related topics

<dl> <dt>

[ICE Reference](ice-reference.md)
</dt> </dl>

 

 




