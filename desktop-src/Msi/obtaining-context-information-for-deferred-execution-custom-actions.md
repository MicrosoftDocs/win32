---
description: Because installation script can be executed outside of the installation session in which it was written, the session may no longer exist during execution of the installation script.
ms.assetid: 13174c5d-c810-4b5d-9d1e-60ed30b8c44d
title: Obtaining Context Information for Deferred Execution Custom Actions
ms.topic: article
ms.date: 05/31/2018
---

# Obtaining Context Information for Deferred Execution Custom Actions

Because installation script can be executed outside of the installation session in which it was written, the session may no longer exist during execution of the installation script. In this case, the original session handle and properties set during the installation sequence are not available to a deferred execution custom action. Any functions that require a session handle are restricted to a few methods that can retrieve context information, or else properties that are needed during script execution must be written into the installation script. For example, deferred custom actions that call dynamic-link libraries (DLLs) pass a handle which can only be used to obtain a very limited amount of information. Functions that do not require a session handle can be accessed from a deferred custom action.

Deferred execution custom actions are restricted to calling only the following functions requiring a handle.



| Function                                       | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**MsiGetProperty**](/windows/desktop/api/Msiquery/nf-msiquery-msigetpropertya)       | Supports a limited set of properties when used with [deferred execution custom actions](deferred-execution-custom-actions.md): the CustomActionData property, [**ProductCode**](productcode.md) property, and [**UserSID**](usersid.md) property.[Commit custom actions](commit-custom-actions.md) cannot use the [**MsiGetProperty**](/windows/desktop/api/Msiquery/nf-msiquery-msigetpropertya) function to obtain the [**ProductCode**](productcode.md) property. Commit custom actions can use the CustomActionData property to obtain the product code.<br/> |
| [**MsiFormatRecord**](/windows/desktop/api/Msiquery/nf-msiquery-msiformatrecorda)     | Supports a limited set of properties when used with [deferred execution custom actions](deferred-execution-custom-actions.md): the CustomActionData and ProductCode properties.                                                                                                                                                                                                                                                                                                                                                      |
| [**MsiGetMode**](/windows/desktop/api/Msiquery/nf-msiquery-msigetmode)               | When called from [deferred execution custom actions](deferred-execution-custom-actions.md), [commit custom actions](commit-custom-actions.md), or [rollback custom actions](rollback-custom-actions.md), [**MsiGetMode**](/windows/desktop/api/Msiquery/nf-msiquery-msigetmode) returns True or False when requested to check the mode parameters MSIRUNMODE\_SCHEDULED, MSIRUNMODE\_COMMIT, or MSIRUNMODE\_ROLLBACK. Requests to check any other run mode parameters from a deferred, commit, or rollback custom action returns False.<br/>                       |
| [**MsiGetLanguage**](/windows/desktop/api/Msiquery/nf-msiquery-msigetlanguage)       | The numeric language ID for the current product.[Commit custom actions](commit-custom-actions.md) cannot use the [**MsiGetLanguage**](/windows/desktop/api/Msiquery/nf-msiquery-msigetlanguage) function. Commit custom actions can use the CustomActionData property to get the numeric language ID.<br/>                                                                                                                                                                                                                                                           |
| [**MsiProcessMessage**](/windows/desktop/api/Msiquery/nf-msiquery-msiprocessmessage) | Processes error or progress messages from the custom action.                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |



 

A custom action that is written in JScript or VBScript requires the install [**Session**](session-object.md) object. This is of the type **Session Object** and the installer attaches it to the script with the name "Session". Because the **Session** object may not exist during an installation rollback, a deferred custom action written in script must use one of the following methods or properties of the **Session** object to retrieve its context.



| Name                                                           | Description                                                                                                                        |
|----------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------|
| [**Mode Property**](session-mode.md)                          | Returns True for MSIRUNMODE\_SCHEDULED only.                                                                                       |
| [**Property Property (Session Object)**](session-session.md)  | Returns the CustomActionData property, [**ProductCode**](productcode.md) property, or [**UserSID**](usersid.md) property.        |
| [**Language Property (Session Object)**](session-language.md) | Returns numeric language ID of the installation session.                                                                           |
| [**Message Method**](session-message.md)                      | Called to handle errors and progress.                                                                                              |
| [**Installer Property**](session-installer.md)                | Returns the parent object, which is used for non-session functions such as registry access and installer configuration management. |



 

Property values that are set at the time the installation sequence is processed into script may be unavailable at the time of script execution. Only the following limited set of properties is always accessible to custom actions during script execution.



| Property name                      | Description                                                                                                                                                                                                     |
|------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CustomActionData                   | Value at time custom action is processed in sequence table. The CustomActionData property is only available to deferred execution custom actions. Immediate custom actions do not have access to this property. |
| [**ProductCode**](productcode.md) | Unique code for the product, a [GUID](guid.md) string.                                                                                                                                                         |
| [**UserSID**](usersid.md)         | Set by the installer to the user's security identifier (SID).                                                                                                                                                   |



 

If other property data is required by the deferred execution custom action, then their values must be stored in the installation script. This can be done by using a second custom action.

**To write the value of a property into the installation script for use during a deferred execution custom action**

1.  Insert a small custom action into the installation sequence that sets the property of interest to a property having the same name as the deferred execution custom action. For example, if the primary key for the deferred execution custom action is "MyAction" set a property named "MyAction" to the property X which you need to retrieve. You must set the "MyAction" property in the installation sequence before the "MyAction" custom action. Although any type of custom action can set the context data, the simplest method is to use a property assignment custom action (for example [Custom Action Type 51](custom-action-type-51.md)).
2.  At the time when the installation sequence is processed, the installer will write the value of property X into the execution script as the value of the property CustomActionData.

## Related topics

<dl> <dt>

[About Properties](about-properties.md)
</dt> <dt>

[Using Properties](using-properties.md)
</dt> <dt>

[Property Reference](property-reference.md)
</dt> </dl>

 

 




