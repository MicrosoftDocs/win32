---
Description: 'The activation context functions and structures are used with side-by-side assemblies.'
ms.assetid: 'b53b30e0-948e-406c-9fb4-9681dc3c5670'
title: Activation Context Reference
---

# Activation Context Reference

The activation context functions and structures are used with side-by-side assemblies.

The following table lists the activation context functions.



| Function                                                   | Description                                                                                                                                             |
|------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**ActivateActCtx**](activateactctx.md)                   | Activates the specified activation context.                                                                                                             |
| [**AddRefActCtx**](addrefactctx.md)                       | Increments the reference count of the specified activation context.                                                                                     |
| [**CreateActCtx**](createactctx.md)                       | Creates an activation context.                                                                                                                          |
| [**DeactivateActCtx**](deactivateactctx.md)               | Deactivates the specified activation context.                                                                                                           |
| [**FindActCtxSectionGuid**](findactctxsectionguid.md)     | Returns data contained in the [**ACTCTX\_SECTION\_KEYED\_DATA**](actctx-section-keyed-data-str.md) structure that corresponds to the specified GUID.   |
| [**FindActCtxSectionString**](findactctxsectionstring.md) | Returns data contained in the [**ACTCTX\_SECTION\_KEYED\_DATA**](actctx-section-keyed-data-str.md) structure that corresponds to the specified string. |
| [**GetCurrentActCtx**](getcurrentactctx.md)               | Returns the current activation context.                                                                                                                 |
| [**IsolationAwareCleanup**](isolationawarecleanup.md)     | Ensures that memory is freed when a manifest is loaded, unloaded, and reloaded.                                                                         |
| [**QueryActCtxW**](queryactctxw.md)                       | Queries the activation context for information about an assembly or file.                                                                               |
| [**QueryActCtxSettingsW**](queryactctxsettingsw.md)       | Specifies the namespace and attribute name of the attribute that is to be queried.                                                                      |
| [**ReleaseActCtx**](releaseactctx.md)                     | Decrements the reference count of the specified activation context.                                                                                     |
| [**ZombifyActCtx**](zombifyactctx.md)                     | Deactivates the specified activation context, but does not deallocate it.                                                                               |



 

The following table lists activation context structures.



| Structure                                                                                                        | Description                                                                                                                                                                                                                                                                                                                                                                                  |
|------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**ACTIVATION\_CONTEXT\_ASSEMBLY\_DETAILED\_INFORMATION**](activation-context-assembly-detailed-information.md) | Contains detailed information about the activation context.                                                                                                                                                                                                                                                                                                                                  |
| [**ACTIVATION\_CONTEXT\_DETAILED\_INFORMATION**](activation-context-detailed-information.md)                    | Contains information about the assembly in the activation context.                                                                                                                                                                                                                                                                                                                           |
| [**ACTIVATION\_CONTEXT\_QUERY\_INDEX**](activation-context-query-index.md)                                      | Contains the assembly within the activation context and the index of the file within the assembly.                                                                                                                                                                                                                                                                                           |
| [**ACTCTX**](actctx-str.md)                                                                                     | Contains information that describes a specific activation context.                                                                                                                                                                                                                                                                                                                           |
| [**ACTCTX\_SECTION\_KEYED\_DATA**](actctx-section-keyed-data-str.md)                                            | Returns the activation context information along with either the GUID or 32-bit integer-tagged activation context section.                                                                                                                                                                                                                                                                   |
| [**ASSEMBLY\_FILE\_DETAILED\_INFORMATION**](assembly-file-detailed-information.md)                              | Contains information about a file of the assembly in the activation context.                                                                                                                                                                                                                                                                                                                 |
| [**ACTIVATION\_CONTEXT\_RUN\_LEVEL\_INFORMATION**](activation-context-run-level-information.md)                 | Used by the [**QueryActCtxW**](queryactctxw.md) function.<br/> **Windows Server 2003 and Windows XP:** This structure is not available.<br/>                                                                                                                                                                                                                                    |
| [**COMPATIBILITY\_CONTEXT\_ELEMENT**](compatibility-context-element.md)                                         | Used by the [**QueryActCtxW**](queryactctxw.md) function as part of the [**ACTIVATION\_CONTEXT\_COMPATIBILITY\_INFORMATION**](activation-context-compatibility-information.md) structure. <br/> **Windows Server 2008 and earlier, and Windows Vista and earlier:** This structure is not available. It is available beginning with Windows Server 2008 R2 and Windows 7.<br/> |
| [**ACTIVATION\_CONTEXT\_COMPATIBILITY\_INFORMATION**](activation-context-compatibility-information.md)          | Used by the [**QueryActCtxW**](queryactctxw.md) function.<br/> **Windows Server 2008 and earlier, and Windows Vista and earlier:** This structure is not available. It is available beginning with Windows Server 2008 R2 and Windows 7.<br/>                                                                                                                                   |



 

The following table lists activation context enumerations.

| Enumeration                                                                       | Description                                                                                                                                                                                                                                            |
|-----------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**ACTCTX\_REQUESTED\_RUN\_LEVEL**](actctx-requested-run-level.md)               | Describes the requested run level of the activation context.**Windows Server 2003 and Windows XP:** This enumeration is not available.<br/>                                                                                                      |
| [**ACTCTX\_COMPATIBILITY\_ELEMENT\_TYPE**](actctx-compatibility-element-type.md) | Describes the compatibility element in the application manifest.**Windows Server 2008 and earlier, and Windows Vista and earlier:** This enumeration is not available. It is available beginning with Windows Server 2008 R2 and Windows 7.<br/> |



 

 

 




