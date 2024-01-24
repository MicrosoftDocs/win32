---
description: The WriteEnvironmentStrings action modifies the values of environment variables.
ms.assetid: a91c1ffe-1bdd-49bb-aa6a-71667a1ed812
title: WriteEnvironmentStrings Action
ms.topic: article
ms.date: 05/31/2018
---

# WriteEnvironmentStrings Action

The WriteEnvironmentStrings action modifies the values of environment variables.

Environment variables do not change for the installation in progress when the WriteEnvironmentStrings action or [RemoveEnvironmentStrings action](removeenvironmentstrings-action.md) are run. On Windows 2000, Windows Server 2003, Windows XP, and Windows Vista this information is stored in the registry and a [**WM\_SETTINGCHANGE**](../winmsg/wm-settingchange.md) message is sent to notify the system of the changes when the installation completes. Another process can receive notification of the changes by handling these messages. No message is sent if a restart of the system is pending. A package can use the [**MsiSystemRebootPending**](msisystemrebootpending.md) property to check whether a system restart is pending.

The installer runs the WriteEnvironmentStrings action only during the installation or reinstallation of a component, and runs the [RemoveEnvironmentStrings action](removeenvironmentstrings-action.md) only during the removal of a component.

Values are written or removed based on the selection of primary actions and modifiers. These are described in the following ActionData Messages section. Note that depending on the action specified, WriteEnvironmentStrings may remove variables, and RemoveEnvironmentStrings may add them based on the authoring of the [Environment table](environment-table.md).

## Sequence Restrictions

The [InstallValidate action](installvalidate-action.md) must be executed before the RemoveEnvironmentStrings action. Because the WriteEnvironmentStrings action and RemoveEnvironmentStrings action are never both applied during an install or removal of a component, their relative sequence is not restricted.

## ActionData Messages



| Field | Description of action data                                                                                                                                                                                                  |
|-------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| \[1\] | Name of the environment variable to modify.                                                                                                                                                                                 |
| \[2\] | The environment variable value.                                                                                                                                                                                             |
| \[3\] | This is a field of bit flags that specifies the action to be performed. Include only one bit for a primary action. There may be more than one modifier bit included in this field. See the following bit flag descriptions. |



 



| Bit Value | Description of primary actions                                                                                                                                                                                      |
|-----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0x1       | Set. Sets the value of the environment variable in all cases.<br/> If this bit is combined with an Append or Prefix modifier bit, the action adds the value to any existing value in the variable.<br/> |
| 0x2       | Set. Sets the value if the variable is absent.<br/> If this bit is combined with an Append or Prefix modifier bit, the action adds the value to any existing value in the variable.<br/>                |
| 0x4       | Remove. Removes the value from the variable.<br/> If this bit is combined with an Append or Prefix modifier bit, the value is removed from the existing string, if the value exists.<br/>               |



 



| Bit Value  | Description of modifier                                                                                                                                                              |
|------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0x20000000 | If this bit is set, actions are applied to the machine environment variables.<br/> If this bit is not set, actions are applied to the user's environment variables.<br/> |
| 0x40000000 | Append. This bit is optional. Do not set both the Append and Prefix modifiers.<br/>                                                                                            |
| 0x80000000 | Prefix. This bit is optional. Do not set both the Append and Prefix modifiers.<br/>                                                                                            |



 

 

 
