---
description: Each record of the IsolatedComponent table associates the component specified in the Component\_Application column (commonly an .exe) with the component specified in the Component\_Shared column (commonly a shared DLL).
ms.assetid: dc30e4c7-a938-4060-be4f-744de9c20fd9
title: IsolatedComponent Table
ms.topic: article
ms.date: 05/31/2018
---

# IsolatedComponent Table

Each record of the IsolatedComponent table associates the component specified in the Component\_Application column (commonly an .exe) with the component specified in the Component\_Shared column (commonly a shared DLL). The [IsolateComponents action](isolatecomponents-action.md) installs a copy of Component\_Shared into a private location for use by Component\_Application. This isolates the Component\_Application from other copies of Component\_Shared that may be installed to a shared location on the computer. See [Isolated Components](isolated-components.md).

To link one Component\_Shared to multiple Component\_Application, include a separate record for each pair in the IsolatedComponents table. The installer copies the files of Component\_Shared into the directory of each Component\_Application that is installed.

The IsolatedComponent table has the following columns.



| Column                 | Type                         | Key | Nullable |
|------------------------|------------------------------|-----|----------|
| Component\_Shared      | [Identifier](identifier.md) | Y   | N        |
| Component\_Application | [Identifier](identifier.md) | Y   | N        |



 

## Columns

<dl> <dt>

<span id="Component_Shared"></span><span id="component_shared"></span><span id="COMPONENT_SHARED"></span>Component\_Shared
</dt> <dd>

Foreign key into the [Component table](component-table.md). The component that contains the shared file, usually a DLL. The DLL should be the key file for this component. This must be a different component than listed in the Component\_Application column.

The shared component controls the registration for all the isolated copies of the component and must have the **msidbComponentAttributesSharedDllRefCount** flag set in the Attributes column of the Component table. This ensures that the installer can manage the life of the shared component.

</dd> <dt>

<span id="Component_Application"></span><span id="component_application"></span><span id="COMPONENT_APPLICATION"></span>Component\_Application
</dt> <dd>

Foreign key into the [Component table](component-table.md). The component that contains the .exe which loads the shared file. The .exe should be the key file for this component. This must be a different component than listed in the Component\_Shared column.

</dd> </dl>

## Validation

<dl>

[ICE03](ice03.md)  
[ICE06](ice06.md)  
[ICE32](ice32.md)  
[ICE62](ice62.md)  
[ICE66](ice66.md)  
[ICE97](ice97.md)  
</dl>

 

 



