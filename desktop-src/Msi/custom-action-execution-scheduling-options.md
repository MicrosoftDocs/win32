---
description: Because a custom action can be scheduled in both the UI and execute sequence tables, and can be executed either in the service or client process, a custom action can potentially execute multiple times.
ms.assetid: a3ffeecb-cdd6-43af-a3fe-48e3e843ec8b
title: Custom Action Execution Scheduling Options
ms.topic: article
ms.date: 05/31/2018
---

# Custom Action Execution Scheduling Options

Because a custom action can be scheduled in both the UI and execute sequence tables, and can be executed either in the service or client process, a custom action can potentially execute multiple times.

Note that the installer:

-   Executes actions in a sequence table immediately by default.
-   Does not execute an action if the conditional expression field of the sequence table evaluates to False.
-   Processes the UI sequence table in the client process if the internal user's interface level is set to the full UI mode (see [**MsiSetInternalUI**](/windows/desktop/api/Msi/nf-msi-msisetinternalui) for a description of UI levels).
-   Is a service registered by default when using Windows 2000 and, in this case, the execute sequence table is processed in the installer service.

You can use the following option flags to control multiple immediate execution of custom actions. To set an option, add the value in this table to the value in the Type field of the [CustomAction table](customaction-table.md). None of the following flags should be used with [deferred execution custom actions](deferred-execution-custom-actions.md).

<dl> <dt>

<span id="_default_"></span><span id="_DEFAULT_"></span>(default)
</dt> <dd>

Hexadecimal: 0x00000000

Decimal: 0

Always execute. Action may run twice if present in both sequence tables.

</dd> <dt>

<span id="msidbCustomActionTypeFirstSequence_"></span><span id="msidbcustomactiontypefirstsequence_"></span><span id="MSIDBCUSTOMACTIONTYPEFIRSTSEQUENCE_"></span>**msidbCustomActionTypeFirstSequence** 
</dt> <dd>

Hexadecimal: 0x00000100

Decimal: 256

Execute no more than once if present in both sequence tables. Always skips action in execute sequence if UI sequence has run. No effect in UI sequence. The action is not required to be present or run in the UI sequence to be skipped in the execute sequence. Not affected by install service registration.

</dd> <dt>

<span id="msidbCustomActionTypeOncePerProcess"></span><span id="msidbcustomactiontypeonceperprocess"></span><span id="MSIDBCUSTOMACTIONTYPEONCEPERPROCESS"></span>**msidbCustomActionTypeOncePerProcess**
</dt> <dd>

Hexadecimal: 0x00000200

Decimal: 512

Execute once per process if in both sequence tables. Skips action in execute sequence if UI sequence has been run in same process, for example both run in the client process. Used to prevent actions that modify the session state, such as property and database data, from running twice.

</dd> <dt>

<span id="msidbCustomActionTypeClientRepeat"></span><span id="msidbcustomactiontypeclientrepeat"></span><span id="MSIDBCUSTOMACTIONTYPECLIENTREPEAT"></span>**msidbCustomActionTypeClientRepeat**
</dt> <dd>

Hexadecimal: 0x00000300

Decimal: 768

Execute only if running on client after UI sequence has run. The action runs only if the execute sequence is run on the client following UI sequence. May be used to provide either/or logic, or to suppress the UI-related processing if already done for the client session.

</dd> </dl>

Note that to run a custom action during two different run modes, author two entries into the [CustomAction table](customaction-table.md) . For example, to have a custom action that calls a C/C++ dynamic link library (DLL) ( [Custom Action Type 1](custom-action-type-1.md)) both when the mode is MSIRUNMODE\_SCHEDULED and MSIRUNMODE\_ROLLBACK, put two entries in the CustomAction table that call the same DLL but that have different numeric types. Include code that calls [**MsiGetMode**](/windows/desktop/api/Msiquery/nf-msiquery-msigetmode) to determine when to run which custom action.

## Related topics

<dl> <dt>

[Custom Action Reference](custom-action-reference.md)
</dt> <dt>

[About Custom Actions](about-custom-actions.md)
</dt> <dt>

[Using Custom Actions](using-custom-actions.md)
</dt> </dl>

 

 



