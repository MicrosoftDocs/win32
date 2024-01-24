---
description: The RemoveEnvironmentStrings action modifies the values of environment variables.
ms.assetid: 024a734a-2e40-45b6-9dec-73def89a417f
title: RemoveEnvironmentStrings Action
ms.topic: article
ms.date: 05/31/2018
---

# RemoveEnvironmentStrings Action

The RemoveEnvironmentStrings action modifies the values of environment variables.

Note that environment variables do not change for the installation in progress when either the [WriteEnvironmentStrings action](writeenvironmentstrings-action.md) or RemoveEnvironmentStrings action are run. On Windows 2000, this information is stored in the registry and a message is sent to notify the system of changes when the installation completes. A new process, or another process that checks for these messages, will use the new environment variables.

The installer runs the [WriteEnvironmentStrings action](writeenvironmentstrings-action.md) only during the installation or reinstallation of a component, and runs the RemoveEnvironmentStrings action only during the removal of a component.

Values are written or removed based on the selection of primary actions and modifiers. These are described in the following ActionData Messages section. Note that depending upon the action specified, WriteEnvironmentStrings may remove variables, and RemoveEnvironmentStrings may add them based on the authoring of the [Environment table](environment-table.md).

## Sequence Restrictions

The [InstallValidate action](installvalidate-action.md) must be executed before the RemoveEnvironmentStrings action. Because the WriteEnvironmentStrings action and RemoveEnvironmentStrings action are never both applied during the installation or removal of a component, their relative sequence is not restricted.

## ActionData Messages



| Field | Description of action data                                                                                                                                                                                                |
|-------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| \[1\] | Name of the environment variable to modify.                                                                                                                                                                               |
| \[2\] | The environment variable value.                                                                                                                                                                                           |
| \[3\] | This is a field of bit flags that specify the action to be performed. Include only one bit for a primary action. There may be more than one modifier bit included in this field. See the following bit flag descriptions. |



 



| Bit value | Description of primary actions                                                                                                                                                                                      |
|-----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0x1       | Set. Sets the value of the environment variable in all cases.<br/> If this bit is combined with an Append or Prefix modifier bit, the action adds the value to any existing value in the variable.<br/> |
| 0x2       | Set. Sets the value if the variable is absent.<br/> If this bit is combined with an Append or Prefix modifier bit, the action adds the value to any existing value in the variable.<br/>                |
| 0x4       | Remove. Removes the value from the variable.<br/> If this bit is combined with an Append or Prefix modifier bit, the value is removed from the existing string, if the value exists.<br/>               |



 



| Bit value  | Description of modifier                                                                                                                                                              |
|------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0x20000000 | If this bit is set, actions are applied to the machine environment variables.<br/> If this bit is not set, actions are applied to the user's environment variables.<br/> |
| 0x40000000 | Append. This bit is optional. Do not set both the Append and Prefix modifiers.<br/>                                                                                            |
| 0x80000000 | Prefix. This bit is optional. Do not set both the Append and Prefix modifiers.<br/>                                                                                            |



 

 

 




