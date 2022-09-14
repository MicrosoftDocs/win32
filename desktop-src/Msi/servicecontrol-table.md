---
description: The ServiceControl table is used to control installed or uninstalled services.Note   Services that rely on the presence of an assembly in the Global Assembly Cache (GAC) cannot be installed or started using the ServiceInstall and ServiceControl tables.
ms.assetid: c51cd9bd-3c55-4eec-ab67-172765adc51c
title: ServiceControl Table
ms.topic: article
ms.date: 05/31/2018
---

# ServiceControl Table

The ServiceControl table is used to control installed or uninstalled services.

> [!Note]  
> Services that rely on the presence of an [assembly](assemblies.md) in the Global Assembly Cache (GAC) cannot be installed or started using the [ServiceInstall](serviceinstall-table.md) and ServiceControl tables. If you need to start a service that depends on an assembly in the GAC, you must use a custom action sequenced after the [InstallFinalize action](installfinalize-action.md) or a [commit custom action](commit-custom-actions.md). For information about installing assemblies to the GAC see [Installation of Assemblies to the Global Assembly Cache](installation-of-assemblies-to-the-global-assembly-cache.md).

 

The ServiceControl table has the following columns.



| Column         | Type                         | Key | Nullable |
|----------------|------------------------------|-----|----------|
| ServiceControl | [Identifier](identifier.md) | Y   | N        |
| Name           | [Formatted](formatted.md)   | N   | N        |
| Event          | [Integer](integer.md)       | N   | N        |
| Arguments      | [Formatted](formatted.md)   | N   | Y        |
| Wait           | [Integer](integer.md)       | N   | Y        |
| Component\_    | [Identifier](identifier.md) | N   | N        |



 

## Columns

<dl> <dt>

<span id="ServiceControl"></span><span id="servicecontrol"></span><span id="SERVICECONTROL"></span>ServiceControl
</dt> <dd>

This is the primary key of this table.

</dd> <dt>

<span id="Name"></span><span id="name"></span><span id="NAME"></span>Name
</dt> <dd>

This column is the string naming the service. This column can be used to control a service that is not installed.

</dd> <dt>

<span id="Event"></span><span id="event"></span><span id="EVENT"></span>Event
</dt> <dd>

This column contains the operations to be performed on the named service. Note that when stopping a service, all services that depend on that service are also stopped. When deleting a service that is running, the installer stops the service.

The values in this field are bit fields that can be combined into a single value that represents several operations.

The following values are only used during an installation.



| Constant                           | Hexadecimal | Decimal | Description                                                                        |
|------------------------------------|-------------|---------|------------------------------------------------------------------------------------|
| **msidbServiceControlEventStart**  | 0x001       | 1       | Starts the service during the [StartServices action](startservices-action.md).    |
| **msidbServiceControlEventStop**   | 0x002       | 2       | Stops the service during the [StopServices action](stopservices-action.md).       |
| (none)                             | 0x004       | 4       | &lt;reserved&gt;                                                                   |
| **msidbServiceControlEventDelete** | 0x008       | 8       | Deletes the service during the [DeleteServices action](deleteservices-action.md). |



 

The following values are only used during an uninstall.



| Constant                                    | Hexadecimal | Decimal | Description                                                                        |
|---------------------------------------------|-------------|---------|------------------------------------------------------------------------------------|
| **msidbServiceControlEventUninstallStart**  | 0x010       | 16      | Starts the service during the [StartServices action](startservices-action.md).    |
| **msidbServiceControlEventUninstallStop**   | 0x020       | 32      | Stops the service during the [StopServices action](stopservices-action.md).       |
| (none)                                      | 0x040       | 64      | &lt;reserved&gt;                                                                   |
| **msidbServiceControlEventUninstallDelete** | 0x080       | 128     | Deletes the service during the [DeleteServices action](deleteservices-action.md). |



 

</dd> <dt>

<span id="Arguments"></span><span id="arguments"></span><span id="ARGUMENTS"></span>Arguments
</dt> <dd>

A list of arguments for starting services. The arguments are separated by null characters \[~\]. For example, the list of arguments One, Two, and Three are listed as: One\[~\]Two\[~\]Three.

</dd> <dt>

<span id="Wait"></span><span id="wait"></span><span id="WAIT"></span>Wait
</dt> <dd>

Leaving this field null or entering a value of 1 causes the installer to wait a maximum of 30 seconds for the service to complete before proceeding. The wait can be used to allow additional time for a critical event to return a failure error. A value of 0 in this field means to wait only until the service control manager (SCM) reports that this service is in a pending state before continuing with the installation.

</dd> <dt>

<span id="Component_"></span><span id="component_"></span><span id="COMPONENT_"></span>Component\_
</dt> <dd>

External key to column one of the [Component Table](component-table.md).

</dd> </dl>

## Remarks

The [StartServices](startservices-action.md), [StopServices](stopservices-action.md), and [DeleteServices](deleteservices-action.md) actions in [*sequence tables*](s-gly.md) process the information in this table. For information about using *sequence tables*, see [Using a Sequence Table](using-a-sequence-table.md).

Use the Name column to start, stop, or delete services that are being replaced by the installation or that are dependent upon a new service that is being installed. For example, entering MyService into the ServiceControl column can tie this service to MyComponent in the Component\_ column. If the bit field in the Event column is set for start while installing, then the installer starts MyService when installing MyComponent.

## Validation

<dl>

[ICE03](ice03.md)  
[ICE06](ice06.md)  
[ICE32](ice32.md)  
[ICE45](ice45.md)  
[ICE46](ice46.md)  
[ICE69](ice69.md)  
</dl>

 

 



