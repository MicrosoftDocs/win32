---
description: The MsiServiceConfig table configures a service that is installed or being installed by the current package.
ms.assetid: 0d9fd005-9326-4a18-8496-35b5d1927f47
title: MsiServiceConfig Table
ms.topic: article
ms.date: 05/31/2018
---

# MsiServiceConfig Table

The MsiServiceConfig table configures a service that is installed or being installed by the current package.

**[Windows Installer 4.5 or earlier](not-supported-in-windows-installer-4-5.md):** Not supported. This table is available beginning with Windows Installer 5.0.

The MsiServiceConfig table has the following columns.



| Column           | Type                         | Key | Nullable |
|------------------|------------------------------|-----|----------|
| MsiServiceConfig | [Identifier](identifier.md) | Y   | N        |
| Name             | [Formatted](formatted.md)   | N   | N        |
| Event            | [Integer](integer.md)       | N   | N        |
| ConfigType       | [Integer](integer.md)       | N   | N        |
| Argument         | [Formatted](formatted.md)   | N   | Y        |
| Component\_      | [Identifier](identifier.md) | N   | N        |



 

## Columns

<dl> <dt>

<span id="MsiServiceConfig"></span><span id="msiserviceconfig"></span><span id="MSISERVICECONFIG"></span>MsiServiceConfig
</dt> <dd>

This is the primary key of this table.

</dd> <dt>

<span id="Name"></span><span id="name"></span><span id="NAME"></span>Name
</dt> <dd>

This column contains the name of a service that is a part of this package or that is already is installed.

</dd> <dt>

<span id="Event"></span><span id="event"></span><span id="EVENT"></span>Event
</dt> <dd>

This column specifies when to change the service configuration. The following values can be combined to represent multiple operations. Any values included other than these are ignored.



| Constant                                         | Description                                              |
|--------------------------------------------------|----------------------------------------------------------|
| **msidbServiceConfigEventInstall**1<br/>   | Takes the action during installation of the component.   |
| **msidbServiceConfigEventUninstall**2<br/> | Takes the action during uninstallation of the component. |
| **msidbServiceConfigEventReinstall**4<br/> | Takes the action during reinstallation of the component. |



 

</dd> <dt>

<span id="ConfigType"></span><span id="configtype"></span><span id="CONFIGTYPE"></span>ConfigType
</dt> <dd>

The value in this field, combined with the value in the Arguments field, specify what change to make to the service configuration. The specified change takes effect the next time the system is started.



| Config                                                      | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|-------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **SERVICE\_CONFIG\_DELAYED\_AUTO\_START**3<br/>       | Configure the time delay of an [auto-start service](../services/automatically-starting-services.md). <br/> Enter 1 in the Argument field to start the service after other auto-start services plus a time delay. <br/> Enter 0 in the Argument field to turn off the auto-start service delay.<br/> Applies only to installed auto-start services or services installed by this package with **SERVICE\_AUTO\_START** in the StartType field of the [ServiceInstall table](serviceinstall-table.md).<br/>                                                                         |
| **SERVICE\_CONFIG\_REQUIRED\_PRIVILEGES\_INFO**6<br/> | Change the list of privileges required by the service.<br/> Enter a list of requested privileges in the Argument field. The [Formatted](formatted.md) string value in the Argument field lists the [**Privilege Constants**](../secauthz/privilege-constants.md) for the requested privileges. You can use the \[~\] syntax of the [Formatted](formatted.md) string to insert a null character. Separate the privilege constants in the list by \[~\].<br/>                                                                                                                              |
| **SERVICE\_CONFIG\_SERVICE\_SID\_INFO**5<br/>         | Add a service SID type to the process token containing this service.<br/> Enter in the Argument field a valid service SID type for the [**SERVICE\_SID\_INFO**](/windows/win32/api/winsvc/ns-winsvc-service_sid_info) structure: **SERVICE\_SID\_TYPE\_NONE** (0x00), **SERVICE\_SID\_TYPE\_RESTRICTED** (0x03), or **SERVICE\_SID\_TYPE\_UNRESTRICTED** (0x01). <br/>                                                                                                                                                                                                                                              |
| **SERVICE\_CONFIG\_PRESHUTDOWN\_INFO**7<br/>          | Configure the length of the time the [Service Control Manager](../services/service-control-manager.md) (SCM) waits before proceeding with other shutdown operations. The SCM waits for this period of time after sending the **SERVICE\_CONTROL\_PRESHUTDOWN** notification to the service. <br/> Enter the time delay length, in milliseconds, in the Argument field. Leave the Argument field empty to reset the time delay to the default of 3 minutes. <br/>                                                                                                                               |
| **SERVICE\_CONFIG\_FAILURE\_ACTIONS\_FLAG**4<br/>     | Configure when to run the failure actions for this service. This setting is ignored if the service has no configured failure actions.<br/> Enter 0 to run the actions only if the service terminates without reporting **SERVICE\_STOPPED**.<br/> Enter 1 to run the actions if the service terminates reporting **SERVICE\_STOPPED** and the **dwWin32ExitCode** member of [**SERVICE\_STATUS**](/windows/win32/api/winsvc/ns-winsvc-service_status) structure is not **ERROR\_SUCCESS**. Configured failure actions are also run if the service terminates without reporting **SERVICE\_STOPPED**.<br/> |



 

</dd> <dt>

<span id="Argument"></span><span id="argument"></span><span id="ARGUMENT"></span>Argument
</dt> <dd>

The value in this field, combined with the value in the ConfigType field, specify what change to make to the service configuration. The specified change takes effect the next time the system is started.

</dd> <dt>

<span id="Component_"></span><span id="component_"></span><span id="COMPONENT_"></span>Component\_
</dt> <dd>

External key to the Component column of the [Component Table](component-table.md).

</dd> </dl>

## Validation

<dl>

[ICE102](ice-102.md)  
[ICE03](ice03.md)  
[ICE06](ice06.md)  
[ICE32](ice32.md)  
[ICE45](ice45.md)  
[ICE46](ice46.md)  
[ICE69](ice69.md)  
</dl>

 

 
