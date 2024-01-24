---
description: ICE88 validates that the directory referenced in the DirProperty column of the IniFile table exists in the Windows Installer package.
ms.assetid: 9bb253fd-e231-4016-807d-3b1068ecff68
title: ICE88
ms.topic: article
ms.date: 05/31/2018
---

# ICE88

ICE88 validates that the directory referenced in the DirProperty column of the [IniFile table](inifile-table.md) exists in the Windows Installer package. ICE88 issues a warning if the DirProperty value does not represent a property in the Directory, AppSearch, or Property tables, certain [system folder properties](property-reference.md), or a property set by a type 51 custom action.

ICE88 scans the following tables and properties.

-   [Directory Table](directory-table.md)
-   [AppSearch Table](appsearch-table.md)
-   [Property Table](property-table.md)
-   [CustomAction Table](customaction-table.md) , where the custom action is a [Custom Action Type 51](custom-action-type-51.md)
-   [**ProgramFilesFolder Property**](programfilesfolder.md)
-   [**CommonFilesFolder Property**](commonfilesfolder.md)
-   [**SystemFolder Property**](systemfolder.md)
-   [**ProgramFiles64Folder Property**](programfiles64folder.md)
-   [**CommonFiles64Folder Property**](commonfiles64folder.md)
-   [**System64Folder Property**](system64folder.md)

## Result

ICE88 posts the following warning.



| ICE88 Warning                                                                                                                                                                  | Description                                                                                                                                                                                                                                                                                                                                                                     |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| In the IniFile table entry (IniFile=) \[3\] the DirProperty=\[1\] is not found in Directory/Property/AppSearch/CA-Type51 tables and it is not one of the installer properties. | For each record in the IniFile table, ICE88 reads the value in the DirProperty column. ICE88 scans for the value in the [Directory Table](directory-table.md), [AppSearch Table](appsearch-table.md), and [Property Table](property-table.md) and also scans the list of properties set by the installer. ICE88 posts this warning if the value cannot be found in the scan. |



 

## Related topics

<dl> <dt>

[ICE Reference](ice-reference.md)
</dt> </dl>

 

 



