---
description: The ServiceInstall table is used to install a service and has the following columns.
ms.assetid: 81688d31-e560-4dd0-8d84-efb50206c76e
title: ServiceInstall Table
ms.topic: article
ms.date: 05/31/2018
---

# ServiceInstall Table

The ServiceInstall table is used to install a service and has the following columns.



| Column         | Type                               | Key | Nullable |
|----------------|------------------------------------|-----|----------|
| ServiceInstall | [Identifier](identifier.md)       | Y   | N        |
| Name           | [Formatted](formatted.md)         | N   | N        |
| DisplayName    | [Formatted](formatted.md)         | N   | Y        |
| ServiceType    | [DoubleInteger](doubleinteger.md) | N   | N        |
| StartType      | [DoubleInteger](doubleinteger.md) | N   | N        |
| ErrorControl   | [DoubleInteger](doubleinteger.md) | N   | N        |
| LoadOrderGroup | [Formatted](formatted.md)         | N   | Y        |
| Dependencies   | [Formatted](formatted.md)         | N   | Y        |
| StartName      | [Formatted](formatted.md)         | N   | Y        |
| Password       | [Formatted](formatted.md)         | N   | Y        |
| Arguments      | [Formatted](formatted.md)         | N   | Y        |
| Component\_    | [Identifier](identifier.md)       | N   | N        |
| Description    | [Formatted](formatted.md)         | N   | Y        |



 

## Columns

<dl> <dt>

<span id="ServiceInstall"></span><span id="serviceinstall"></span><span id="SERVICEINSTALL"></span>ServiceInstall
</dt> <dd>

This is the primary key for the table.

</dd> <dt>

<span id="Name"></span><span id="name"></span><span id="NAME"></span>Name
</dt> <dd>

This column is the string that gives the service name to install. The string has a maximum length of 256 characters. The service control manager database preserves the case of the characters in the service name, but comparisons of service names are case insensitive. Forward-slash (/) and back-slash (\\) are invalid service name characters.

</dd> <dt>

<span id="DisplayName"></span><span id="displayname"></span><span id="DISPLAYNAME"></span>DisplayName
</dt> <dd>

This column is the localizable string that user interface programs use to identify the service. The string has a maximum length of 256 characters. The service control manager preserves the case of the display name, but display name comparisons are case insensitive.

</dd> <dt>

<span id="ServiceType"></span><span id="servicetype"></span><span id="SERVICETYPE"></span>ServiceType
</dt> <dd>

This column is a set of bit flags that specify the type of service. One of the following service types must be specified in this column.



| Type of service                | Value      | Description                                                                                                                                                                                                                  |
|--------------------------------|------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SERVICE\_WIN32\_OWN\_PROCESS   | 0x00000010 | A Microsoft Win32 service that runs its own process.                                                                                                                                                                         |
| SERVICE\_WIN32\_SHARE\_PROCESS | 0x00000020 | A Win32 service that shares a process.                                                                                                                                                                                       |
| SERVICE\_INTERACTIVE\_PROCESS  | 0x00000100 | A Win32 service that interacts with the desktop. This value cannot be used alone and must be added to one of the two previous types.The StartName column must be set to LocalSystem or null when using this flag.<br/> |



 

The following types of service are unsupported.



| Type of service               | Value      | Description                   |
|-------------------------------|------------|-------------------------------|
| SERVICE\_KERNEL\_DRIVER       | 0x00000001 | A driver service.             |
| SERVICE\_FILE\_SYSTEM\_DRIVER | 0x00000002 | A file system driver service. |



 

</dd> <dt>

<span id="StartType"></span><span id="starttype"></span><span id="STARTTYPE"></span>StartType
</dt> <dd>

This column is a set of bit flags that specify when to start the service. One of the following types of service start must be specified in this column.



| Type of service start  | Value      | Description                                                                                                |
|------------------------|------------|------------------------------------------------------------------------------------------------------------|
| SERVICE\_AUTO\_START   | 0x00000002 | A service start during startup of the system.                                                              |
| SERVICE\_DEMAND\_START | 0x00000003 | A service start when the service control manager calls the [**StartService**](/windows/win32/api/winsvc/nf-winsvc-startservicea) function. |
| SERVICE\_DISABLED      | 0x00000004 | Specifies a service that can no longer be started.                                                         |



 

The Windows Installer cannot use the SERVICE\_BOOT\_START and SERVICE\_SYSTEM\_START options.

</dd> <dt>

<span id="ErrorControl"></span><span id="errorcontrol"></span><span id="ERRORCONTROL"></span>ErrorControl
</dt> <dd>

This column specifies the action taken by the startup program if the service fails to start during startup. These values affect the ServiceControl StartService events for installed services. One of the following error control flags must be specified in this column.

Adding the constant **msidbServiceInstallErrorControlVital** (value = 0x08000) to the flags in the following table specifies that the overall install should fail if the service cannot be installed into the system.



| Error control flag       | Value      | Startup program's action                                                                                                                                                                       |
|--------------------------|------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SERVICE\_ERROR\_IGNORE   | 0x00000000 | Logs the error and continues with the startup operation.                                                                                                                                       |
| SERVICE\_ERROR\_NORMAL   | 0x00000001 | Logs the error, displays a message box and continues the startup operation.                                                                                                                    |
| SERVICE\_ERROR\_CRITICAL | 0x00000003 | Logs the error if it is possible and the system is restarted with the last configuration known to be good. If the last-known-good configuration is being started, the startup operation fails. |



 

</dd> <dt>

<span id="LoadOrderGroup"></span><span id="loadordergroup"></span><span id="LOADORDERGROUP"></span>LoadOrderGroup
</dt> <dd>

This column contains the string that names the load ordering group of which this service is a member. Specify null or an empty string if the service does not belong to a group.

</dd> <dt>

<span id="Dependencies"></span><span id="dependencies"></span><span id="DEPENDENCIES"></span>Dependencies
</dt> <dd>

This column is a list of names of services or load ordering groups that the system must start before this service. Separate names in the list by Nulls. If the service has no dependencies, then specify Null or an empty string. Use the syntax \[~\] to insert a Null. Dependency on a group means that this service can run if at least one member of the group is running after an attempt to start all members of the group.

For example, to require that the system start service1 and service2, before starting the service listed in the ServiceInstall column, enter service1\[~\]service2\[~\]\[~\] into the Dependencies column. The identifiers service1 and service2 must either occur in the primary key of the table or be the name of the service that is already installed.

You must prefix group names with + so that they can be distinguished from a service name. To require that the system start service1 and at least one member of the ordering group MyGroup before starting the service listed in the ServiceInstall column, enter service1\[~\]+MyGroup\[~\]\[~\].

</dd> <dt>

<span id="StartName"></span><span id="startname"></span><span id="STARTNAME"></span>StartName
</dt> <dd>

The service is logged on as the name given by the string in this column. If the service type is SERVICE\_WIN32\_OWN\_PROCESS use an account name in the form: DomainName\\UserName. If the account belongs to the built-in domain it is permitted to specify .\\UserName. The LocalSystem account must be used if the type of service is SERVICE\_WIN32\_SHARE\_PROCESS or SERVICE\_INTERACTIVE\_PROCESS. The [**CreateService**](/windows/win32/api/winsvc/nf-winsvc-createservicea) function uses the LocalSystem account if StartName is specified as null and most services therefore leave this column blank.

</dd> <dt>

<span id="Password"></span><span id="password"></span><span id="PASSWORD"></span>Password
</dt> <dd>

This string is the password to the account name specified in the StartName column. Note that the user must have permissions to log on as a service. The service has no password if StartName is null or an empty string. The Startname of LocalSystem is null, and therefore the password in this instance is null, so most services leave this column blank.

Note that after deleting a service that was installed with a user name and password, the installer cannot rollback the service without first using a custom action to get the password. The installer can acquire all the necessary information about the service except the password, which is stored in a protected part of the system. The custom action acquires the password by prompting the user, reading a property from the database, or reading a file. The custom action must then call [**ChangeServiceConfig**](/windows/win32/api/winsvc/nf-winsvc-changeserviceconfiga), to supply the password, before reinstalling the service.

Windows Installer does not write the value entered into the Password field into the log file.

</dd> <dt>

<span id="Arguments"></span><span id="arguments"></span><span id="ARGUMENTS"></span>Arguments
</dt> <dd>

This column contains any command line arguments or properties required to run the service.

</dd> <dt>

<span id="Component_"></span><span id="component_"></span><span id="COMPONENT_"></span>Component\_
</dt> <dd>

External key to column one of the [Component Table](component-table.md). Note that to install this service using the InstallService table, the KeyPath for this component must be the executable file for the service.

</dd> <dt>

<span id="Description"></span><span id="description"></span><span id="DESCRIPTION"></span>Description
</dt> <dd>

This column contains a localizable description for the service being configured. If this column is left blank the installer uses the existing description of the service if one exists. For more information, see SERVICE\_DESCRIPTION in the Microsoft Windows Software Development Kit (SDK). To erase an existing description enter "\[~\]" in this column. This results in a blank description for either a new or existing service.

</dd> </dl>

## Remarks

The [InstallServices](installservices-action.md) action in [*sequence tables*](s-gly.md) processes the information in this table. For information about using *sequence tables*, see [Using a Sequence Table](using-a-sequence-table.md).

This table has most of the parameters to the Win32 [**CreateService**](/windows/win32/api/winsvc/nf-winsvc-createservicea) function.

Although it is possible to use the user interface to specify that a service be installed as run-from-source, the installer does not actually support this type of installation. Services that run with the privilege level of the local system must be installed to run from the local hard drive. Avoid installing services that impersonate the privileges of a particular user because this may write security data into a log or the system registry. This can potentially create a security problem, password conflict, or the loss of configuration data when the system is restarted.

To delete a service during an uninstallation, there must be a corresponding record for the service in the [ServiceControl table](servicecontrol-table.md) and the **msidbServiceControlEventUninstallDelete** flag must appear in the Event column. The installer does not delete a service in the ServiceInstall table during uninstallation without this entry in the ServiceControl table.

For information on how to secure a service see the [MsiLockPermissionsEx Table](msilockpermissionsex-table.md).

## Validation

<dl>

[ICE03](ice03.md)  
[ICE06](ice06.md)  
[ICE32](ice32.md)  
[ICE45](ice45.md)  
[ICE46](ice46.md)  
[ICE66](ice66.md)  
[ICE69](ice69.md)  
</dl>

 

 
