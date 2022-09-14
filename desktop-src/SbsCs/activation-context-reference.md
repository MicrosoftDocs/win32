---
description: The activation context functions and structures are used with side-by-side assemblies.
ms.assetid: b53b30e0-948e-406c-9fb4-9681dc3c5670
title: Activation Context Reference
ms.topic: article
ms.date: 05/31/2018
---

# Activation Context Reference

The activation context functions and structures are used with side-by-side assemblies.

The following table lists the activation context functions.



| Function                                                   | Description                                                                                                                                             |
|------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**ActivateActCtx**](/windows/desktop/api/Winbase/nf-winbase-activateactctx)                   | Activates the specified activation context.                                                                                                             |
| [**AddRefActCtx**](/windows/desktop/api/Winbase/nf-winbase-addrefactctx)                       | Increments the reference count of the specified activation context.                                                                                     |
| [**CreateActCtx**](/windows/desktop/api/Winbase/nf-winbase-createactctxa)                       | Creates an activation context.                                                                                                                          |
| [**DeactivateActCtx**](/windows/desktop/api/Winbase/nf-winbase-deactivateactctx)               | Deactivates the specified activation context.                                                                                                           |
| [**FindActCtxSectionGuid**](/windows/desktop/api/Winbase/nf-winbase-findactctxsectionguid)     | Returns data contained in the [**ACTCTX\_SECTION\_KEYED\_DATA**](/windows/win32/api/winbase/ns-winbase-actctx_section_keyed_data) structure that corresponds to the specified GUID.   |
| [**FindActCtxSectionString**](/windows/desktop/api/Winbase/nf-winbase-findactctxsectionstringa) | Returns data contained in the [**ACTCTX\_SECTION\_KEYED\_DATA**](/windows/win32/api/winbase/ns-winbase-actctx_section_keyed_data) structure that corresponds to the specified string. |
| [**GetCurrentActCtx**](/windows/desktop/api/Winbase/nf-winbase-getcurrentactctx)               | Returns the current activation context.                                                                                                                 |
| [**IsolationAwareCleanup**](/previous-versions/windows/desktop/legacy/aa375204(v=vs.85))     | Ensures that memory is freed when a manifest is loaded, unloaded, and reloaded.                                                                         |
| [**QueryActCtxW**](/windows/desktop/api/Winbase/nf-winbase-queryactctxw)                       | Queries the activation context for information about an assembly or file.                                                                               |
| [**QueryActCtxSettingsW**](/windows/desktop/api/Winbase/nf-winbase-queryactctxsettingsw)       | Specifies the namespace and attribute name of the attribute that is to be queried.                                                                      |
| [**ReleaseActCtx**](/windows/desktop/api/Winbase/nf-winbase-releaseactctx)                     | Decrements the reference count of the specified activation context.                                                                                     |
| [**ZombifyActCtx**](/windows/desktop/api/Winbase/nf-winbase-zombifyactctx)                     | Deactivates the specified activation context, but does not deallocate it.                                                                               |



 

The following table lists activation context structures.



| Structure                                                                                                        | Description                                                                                                                                                                                                                                                                                                                                                                                  |
|------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**ACTIVATION\_CONTEXT\_ASSEMBLY\_DETAILED\_INFORMATION**](/windows/desktop/api/Winnt/ns-winnt-activation_context_assembly_detailed_information) | Contains detailed information about the activation context.                                                                                                                                                                                                                                                                                                                                  |
| [**ACTIVATION\_CONTEXT\_DETAILED\_INFORMATION**](/windows/desktop/api/Winnt/ns-winnt-activation_context_detailed_information)                    | Contains information about the assembly in the activation context.                                                                                                                                                                                                                                                                                                                           |
| [**ACTIVATION\_CONTEXT\_QUERY\_INDEX**](/windows/desktop/api/Winnt/ns-winnt-activation_context_query_index)                                      | Contains the assembly within the activation context and the index of the file within the assembly.                                                                                                                                                                                                                                                                                           |
| [**ACTCTX**](/windows/win32/api/winbase/ns-winbase-actctxa)                                                                                     | Contains information that describes a specific activation context.                                                                                                                                                                                                                                                                                                                           |
| [**ACTCTX\_SECTION\_KEYED\_DATA**](/windows/win32/api/winbase/ns-winbase-actctx_section_keyed_data)                                            | Returns the activation context information along with either the GUID or 32-bit integer-tagged activation context section.                                                                                                                                                                                                                                                                   |
| [**ASSEMBLY\_FILE\_DETAILED\_INFORMATION**](/windows/desktop/api/Winnt/ns-winnt-assembly_file_detailed_information)                              | Contains information about a file of the assembly in the activation context.                                                                                                                                                                                                                                                                                                                 |
| [**ACTIVATION\_CONTEXT\_RUN\_LEVEL\_INFORMATION**](/windows/desktop/api/Winnt/ns-winnt-activation_context_run_level_information)                 | Used by the [**QueryActCtxW**](/windows/desktop/api/Winbase/nf-winbase-queryactctxw) function.<br/> **Windows Server 2003 and Windows XP:** This structure is not available.<br/>                                                                                                                                                                                                                                    |
| [**COMPATIBILITY\_CONTEXT\_ELEMENT**](/windows/desktop/api/Winnt/ns-winnt-compatibility_context_element)                                         | Used by the [**QueryActCtxW**](/windows/desktop/api/Winbase/nf-winbase-queryactctxw) function as part of the [**ACTIVATION\_CONTEXT\_COMPATIBILITY\_INFORMATION**](/windows/desktop/api/Winnt/ns-winnt-activation_context_compatibility_information) structure. <br/> **Windows Server 2008 and earlier, and Windows Vista and earlier:** This structure is not available. It is available beginning with Windows Server 2008 R2 and Windows 7.<br/> |
| [**ACTIVATION\_CONTEXT\_COMPATIBILITY\_INFORMATION**](/windows/desktop/api/Winnt/ns-winnt-activation_context_compatibility_information)          | Used by the [**QueryActCtxW**](/windows/desktop/api/Winbase/nf-winbase-queryactctxw) function.<br/> **Windows Server 2008 and earlier, and Windows Vista and earlier:** This structure is not available. It is available beginning with Windows Server 2008 R2 and Windows 7.<br/>                                                                                                                                   |



 

The following table lists activation context enumerations.

| Enumeration                                                                       | Description                                                                                                                                                                                                                                            |
|-----------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**ACTCTX\_REQUESTED\_RUN\_LEVEL**](/windows/desktop/api/Winnt/ne-winnt-actctx_requested_run_level)               | Describes the requested run level of the activation context.**Windows Server 2003 and Windows XP:** This enumeration is not available.<br/>                                                                                                      |
| [**ACTCTX\_COMPATIBILITY\_ELEMENT\_TYPE**](/windows/desktop/api/Winnt/ne-winnt-actctx_compatibility_element_type) | Describes the compatibility element in the application manifest.**Windows Server 2008 and earlier, and Windows Vista and earlier:** This enumeration is not available. It is available beginning with Windows Server 2008 R2 and Windows 7.<br/> |



 

 

