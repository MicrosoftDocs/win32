---
title: Common Commands for NetShell Helper Administration
description: To provide a common experience for NetShell users, certain commands should be common among NetShell contexts.
ms.assetid: 190ec65a-ef13-489f-a7cb-83332f64f232
keywords:
- helper NetSh , command syntax, helper administration
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Common Commands for NetShell Helper Administration

To provide a common experience for NetShell users, certain commands should be common among NetShell contexts. These commands perform tasks common to networking services or utilities, such as installing, removing, or resetting the component designed to be monitored or administered by the NetShell helper. The following list explains these guidelines.

<dl> <dt>

<span id="add_commands"></span><span id="ADD_COMMANDS"></span>**add** commands
</dt> <dd>

Helpers that enable a user to add rows to a list or table (or other similar convention), should use the specific command **add** *object* where object represents the object to be added to the list or table.

This command should be consistent with the **delete**, **set**, or **show** commands provided by the helper.

</dd> <dt>

<span id="Boolean_values"></span><span id="boolean_values"></span><span id="BOOLEAN_VALUES"></span>Boolean values
</dt> <dd>

Objects that are Boolean should use **enabled** and **disabled** to identify value, rather than other often used indicators of Boolean value (such as yes or no, true or false, 0 or 1).

</dd> <dt>

<span id="delete_commands"></span><span id="DELETE_COMMANDS"></span>**delete** commands
</dt> <dd>

Helpers that enable a user to delete rows from a list or table (or other similar convention), should use the specific command **delete** *object* where object represents the object to be deleted from the list or table.

This command should be consistent with the **add**, **set**, or **show** commands provided by the helper.

</dd> <dt>

<span id="dump_commands"></span><span id="DUMP_COMMANDS"></span>**dump** commands
</dt> <dd>

Helpers that enable NetShell users to set persistent configuration state should support a dump command to display such configuration information.

</dd> <dt>

<span id="help_commands"></span><span id="HELP_COMMANDS"></span>**help** commands
</dt> <dd>

Helpers should provide **help** and **?** commands. Do not use commands called **-?** or **/?** or **list** to provide lists of commands.

</dd> <dt>

<span id="install_commands"></span><span id="INSTALL_COMMANDS"></span>**install** commands
</dt> <dd>

Helpers that enable a component to be installed with a default configuration should use the specific command **install** to perform the task.

</dd> <dt>

<span id="reset_commands"></span><span id="RESET_COMMANDS"></span>**reset** commands
</dt> <dd>

Helpers that enable a component to be reset to a default configuration should use the specific command **reset** to perform the task.

</dd> <dt>

<span id="set_commands"></span><span id="SET_COMMANDS"></span>**set** commands
</dt> <dd>

Helpers that enable a user to modify one or more existing rows in a list or table (or other similar convention), should use the specific command **set** *object* where object represents the object to be modified in the list or table.

This command should be consistent with the **add**, **delete**, or **show** commands provided by the helper.

</dd> <dt>

<span id="show_commands"></span><span id="SHOW_COMMANDS"></span>**show** commands
</dt> <dd>

Helpers that enable a user to display an existing list or table (or other similar convention), should use the specific command **show** *object* where object represents the list or table.

This command should be consistent with the **add**, **delete**, or **set** commands provided by the helper.

</dd> <dt>

<span id="uninstall_commands"></span><span id="UNINSTALL_COMMANDS"></span>**uninstall** commands
</dt> <dd>

Helpers that enable a component to be uninstalled, and its configuration completely removed from the system, should use the specific command **uninstall** to perform the task.

</dd> </dl>

## Remarks

Commands should always appear in code and be listed in alphabetical order.

The **add**, **delete**, **set**, and **show** should always be command groups, never single commands. For example, "add \[name=\]&lt;string&gt;" is not preferable since "add" is not followed by a noun. Examples of preferred usage include "add name \[name=\]&lt;string&gt;" or "add object \[object=\] &lt;string&gt;".

Non-group commands should be one word, like **help** or **dump**. Command groups should result in two word commands, such as **show interface** or **add address**.

Do not abbreviate words in commands. NetShell already allows abbreviating words, for example "addr" for "address" or "ser" for "service". Similarly, avoid naming commands that can be abbreviated the same way, such as **show serviceconfiguration** and **show servicestate**. Both commands would abbreviate to "show ser".

Commands should be unambiguous. If there is a **show** command, there should not be a **display** command. The recommended command verbs are **add**, **delete**, **install**, **reset**, **set**, **show**, and **uninstall**.

 

 




