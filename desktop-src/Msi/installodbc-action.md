---
description: The InstallODBC action installs the drivers, translators, and data sources in the ODBCDriver Table, ODBCTranslator Table, and ODBCDataSource Table.
ms.assetid: fbcf1fdc-5aef-4431-93fe-3ed02748b5ff
title: InstallODBC Action
ms.topic: article
ms.date: 05/31/2018
---

# InstallODBC Action

The InstallODBC action installs the drivers, translators, and data sources in the [ODBCDriver Table](odbcdriver-table.md), [ODBCTranslator Table](odbctranslator-table.md), and [ODBCDataSource Table](odbcdatasource-table.md). If a driver or translator already exists, the InstallODBC action makes SQL calls necessary for the installation.

## Sequence Restrictions

The InstallODBC action does not copy or remove files, and must be after actions that copy or remove files.

## ActionData Messages

The following table identifies the ActionData messages for each installed driver.



| Field       | Description                                                              |
|-------------|--------------------------------------------------------------------------|
| \[1\]       | Driver description. The ODBC driver key.                                 |
| \[2\]       | ComponentId.                                                             |
| \[3\]       | Folder.                                                                  |
| \[4, 5, …\] | Attribute and value pairs from [ODBCAttribute](odbcattribute-table.md). |



 

The following table identifies the ActionData messages for each installed translator.



| Field       | Description                                                              |
|-------------|--------------------------------------------------------------------------|
| \[1\]       | Driver description. The ODBC driver key.                                 |
| \[2\]       | ComponentId.                                                             |
| \[3\]       | Folder.                                                                  |
| \[4, 5, …\] | Attribute and value pairs from [ODBCAttribute](odbcattribute-table.md). |



 

The following table identifies the ActionData messages for each installed data source.



| Field       | Description                                                              |
|-------------|--------------------------------------------------------------------------|
| \[1\]       | Driver description. The ODBC driver key.                                 |
| \[2\]       | ComponentId.                                                             |
| \[3\]       | Registration: ODBC\_ADD\_DSN or ODBC\_ADD\_SYS\_DSN.                     |
| \[4, 5, …\] | Attribute and value pairs from [ODBCAttribute](odbcattribute-table.md). |



 

## Remarks

The ODBC Driver Manager must be authored in the Microsoft Installer package and a component named ODBCDriverManager must be included. The manager is installed if necessary.

To rename the component, set a property named ODBCDriverManager to the new name of the component. If a 64-bit ODBC Driver Manager is to be installed, the component that carries it should be named ODBCDriverManager64.

-   The InstallODBC action queries the [ODBCDataSource Table](odbcdatasource-table.md) and the [ODBCSourceAttribute Table](odbcsourceattribute-table.md) for each data source to be installed, and the attributes of the data source.
-   The InstallODBC action queries the [ODBCDriver Table](odbcdriver-table.md) and the [ODBCTranslator Table](odbctranslator-table.md) for each driver and translator that is selected for installation.
-   The InstallODBC action queries the [ODBCAttribute Table](odbcattribute-table.md) for the attributes of the drivers and translators.

## Related topics

<dl> <dt>

[Windows Installer Examples](windows-installer-examples.md)
</dt> </dl>

 

 



