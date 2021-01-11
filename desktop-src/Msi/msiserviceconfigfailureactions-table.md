---
description: The MsiServiceConfigFailureActions table lists operations to be run after a service fails. The operations specified in this table run the next time the system is started.
ms.assetid: 7c450b74-1f91-4a1c-beee-646a407eb8a8
title: MsiServiceConfigFailureActions Table
ms.topic: article
ms.date: 05/31/2018
---

# MsiServiceConfigFailureActions Table

The MsiServiceConfigFailureActions table lists operations to be run after a service fails. The operations specified in this table run the next time the system is started.

**[Windows Installer 4.5 or earlier](not-supported-in-windows-installer-4-5.md):** Not supported. This table is available beginning with Windows Installer 5.0.

The MsiServiceConfigFailureActions table has the following columns.



| Column                         | Type                         | Key | Nullable |
|--------------------------------|------------------------------|-----|----------|
| MsiServiceConfigFailureActions | [Identifier](identifier.md) | Y   | N        |
| Name                           | [Formatted](formatted.md)   | N   | N        |
| Event                          | [Integer](integer.md)       | N   | N        |
| ResetPeriod                    | [Integer](integer.md)       | N   | Y        |
| RebootMessage                  | [Formatted](formatted.md)   | N   | Y        |
| Command                        | [Formatted](formatted.md)   | N   | Y        |
| Actions                        | [Text](text.md)             | N   | Y        |
| DelayActions                   | [Text](text.md)             | N   | Y        |
| Component\_                    | [Identifier](identifier.md) | N   | N        |



 

## Columns

<dl> <dt>

<span id="MsiServiceConfigFailureActions"></span><span id="msiserviceconfigfailureactions"></span><span id="MSISERVICECONFIGFAILUREACTIONS"></span>MsiServiceConfigFailureActions
</dt> <dd>

This is the primary key of this table that identifies a failure action.

</dd> <dt>

<span id="Name"></span><span id="name"></span><span id="NAME"></span>Name
</dt> <dd>

This column contains the name of a service that is a part of this package or that is already is installed.

</dd> <dt>

<span id="Event"></span><span id="event"></span><span id="EVENT"></span>Event
</dt> <dd>

This column specifies when to change the service's configuration. The following values are bit fields that can be combined to represent multiple operations. Any other bit field values are ignored.



| Constant                                         | Description                                     |
|--------------------------------------------------|-------------------------------------------------|
| **msidbServiceConfigEventInstall**1<br/>   | Change during installation of the component.    |
| **msidbServiceConfigEventUninstall**2<br/> | Change during uninstallation of the component.  |
| **msidbServiceConfigEventReinstall**4<br/> | Change during re-installation of the component. |



 

</dd> <dt>

<span id="ResetPeriod"></span><span id="resetperiod"></span><span id="RESETPERIOD"></span>ResetPeriod
</dt> <dd>

The reset period in seconds of service's failure count. The [Service Control Manager](../services/service-control-manager.md) (SCM) counts the number of times each service has failed since the system was last restarted. The count is reset to zero if the service does not fail for the reset period. When the service fails for the Nth time, the system performs the action specified in the element \[N-1\] of the array specified in the Actions field.

Leave ResetPeriod field empty to indicate that failure count should never be reset.

</dd> <dt>

<span id="RebootMessage"></span><span id="rebootmessage"></span><span id="REBOOTMESSAGE"></span>RebootMessage
</dt> <dd>

The message sent to users before restarting the computer in response to a **SC\_ACTION\_REBOOT** action specified in the Actions column. You can use an empty string, "", to send the current message unchanged. You can use \[~\] syntax of the [Formatted](formatted.md) data type to delete the current message and send no message.

</dd> <dt>

<span id="Command"></span><span id="command"></span><span id="COMMAND"></span>Command
</dt> <dd>

The command line run by the process created by the [**CreateProcess**](/windows/win32/api/processthreadsapi/nf-processthreadsapi-createprocessa) function in response to a **SC\_ACTION\_RUN\_COMMAND** action specified in the Actions column. The new process runs under the same account as the service and only if the Action field is **SC\_ACTION\_RUN\_COMMAND**. You can use an empty string, "", to use the current command line unchanged. You can use \[~\] syntax of the [Formatted](formatted.md) data type to delete the current command line and run no operation when the service fails.

</dd> <dt>

<span id="Actions"></span><span id="actions"></span><span id="ACTIONS"></span>Actions
</dt> <dd>

This field contains an array of integer values that specify the actions taken by the SCM if the service fails. Separate the values in the array by \[~\]. The integer value in the Nth element of the array specifies the action performed when the service fails for the Nth time. Each member of the array is one of following integer values.



| Constant                                 | Description           |
|------------------------------------------|-----------------------|
| **SC\_ACTION\_NONE**0<br/>         | No action.            |
| **SC\_ACTION\_REBOOT**2<br/>       | Restart the computer. |
| **SC\_ACTION\_RESTART**1<br/>      | Restart the service.  |
| **SC\_ACTION\_RUN\_COMMAND**3<br/> | Run a command.        |



 

</dd> <dt>

<span id="DelayActions"></span><span id="delayactions"></span><span id="DELAYACTIONS"></span>DelayActions
</dt> <dd>

This field contains an array of integer values that specify the time in milliseconds to wait before performing the action specified in the Action column. Separate the values in the array by \[~\]. The number of elements in the DelayActions array must be equal to the number of elements in the Actions array. The Nth element of the DelayActions array specifies the time delay for the nth element of the Actions array.

</dd> <dt>

<span id="Component_"></span><span id="component_"></span><span id="COMPONENT_"></span>Component\_
</dt> <dd>

External key to column one of the [Component Table](component-table.md).

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

 

 
