---
description: The SelfReg table contains information about modules that need to be self registered.
ms.assetid: 7fe5c96e-16a4-49c9-9a93-616608aa55b2
title: SelfReg Table
ms.topic: article
ms.date: 05/31/2018
---

# SelfReg Table

The SelfReg table contains information about modules that need to be self registered. The installer calls the [**DllRegisterServer**](/windows/win32/api/olectl/nf-olectl-dllregisterserver) function during installation of the module; it calls [**DllUnregisterServer**](/windows/win32/api/olectl/nf-olectl-dllunregisterserver) during uninstallation of the module. The installer does not self register EXE files.

The SelfReg table has the following columns.



| Column | Type                         | Key | Nullable |
|--------|------------------------------|-----|----------|
| File\_ | [Identifier](identifier.md) | Y   | N        |
| Cost   | [Integer](integer.md)       | N   | Y        |



 

## Columns

<dl> <dt>

<span id="File_"></span><span id="file_"></span><span id="FILE_"></span>File\_
</dt> <dd>

External key into the first column of the [File table](file-table.md) indicating the module that needs to be registered.

</dd> <dt>

<span id="Cost"></span><span id="cost"></span><span id="COST"></span>Cost
</dt> <dd>

The cost of registering the module in bytes. This must be a non-negative number.

</dd> </dl>

## Remarks

Installation package authors are strongly advised against using self registration. Instead they should register modules by authoring one or more tables provided by the installer for this purpose. For more information, see [Registry Tables Group](registry-tables-group.md). Many of the benefits of having a central installer service are lost with self registration because self-registration routines tend to hide critical configuration information. Reasons for avoiding self registration include:

-   Rollback of an installation with self-registered modules cannot be safely done using [**DllUnregisterServer**](/windows/win32/api/olectl/nf-olectl-dllunregisterserver) because there is no way of telling if the self-registered keys are used by another feature or application.
-   The ability to use advertisement is reduced if Class or extension server registration is performed within self-registration routines.
-   The installer automatically handles HKCR keys in the registry tables for both per-user or per-machine installations. [**DllRegisterServer**](/windows/win32/api/olectl/nf-olectl-dllregisterserver) routines currently do not support the notion of a per-user HKCR key.
-   If multiple users are using a self-registered application on the same computer, each user must install the application the first time they run it. Otherwise the installer cannot easily determine that the proper HKCU registry keys exist.
-   The [**DllRegisterServer**](/windows/win32/api/olectl/nf-olectl-dllregisterserver) can be denied access to network resources such as type libraries if a component is both specified as run-from-source and is listed in the SelfReg table. This can cause the installation of the component to fail to during an administrative installation.
-   Self-registering DLLs are more susceptible to coding errors because the new code required for [**DllRegisterServer**](/windows/win32/api/olectl/nf-olectl-dllregisterserver) is commonly different for each DLL. Instead use the registry tables in the database to take advantage of existing code provided by the installer.
-   Self-registering DLLs can sometimes link to auxiliary DLLs that are not present or are the wrong version. In contrast, the installer can register the DLLs using the registry tables with no dependency on the current state of the system.

> [!Note]  
> You cannot specify the order in which the installer registers or unregisters self-registering DLLs by using the [SelfRegModules](selfregmodules-action.md) and [SelfUnRegModules](selfunregmodules-action.md) actions. See [Specifying the Order of Self Registration](specifying-the-order-of-self-registration.md).

 

## Validation

<dl>

[ICE03](ice03.md)  
[ICE06](ice06.md)  
[ICE32](ice32.md)  
</dl>

 

 
