---
Description: The activation context functions and structures are used with side-by-side assemblies.
ms.assetid: b53b30e0-948e-406c-9fb4-9681dc3c5670
title: Activation Context Reference
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Activation Context Reference

The activation context functions and structures are used with side-by-side assemblies.

The following table lists the activation context functions.



| Function                                                   | Description                                                                                                                                             |
|------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**ActivateActCtx**](/windows/win32/Winbase/nf-winbase-activateactctx?branch=master)                   | Activates the specified activation context.                                                                                                             |
| [**AddRefActCtx**](/windows/win32/Winbase/nf-winbase-addrefactctx?branch=master)                       | Increments the reference count of the specified activation context.                                                                                     |
| [**CreateActCtx**](/windows/win32/Winbase/nf-winbase-createactctxa?branch=master)                       | Creates an activation context.                                                                                                                          |
| [**DeactivateActCtx**](/windows/win32/Winbase/nf-winbase-deactivateactctx?branch=master)               | Deactivates the specified activation context.                                                                                                           |
| [**FindActCtxSectionGuid**](/windows/win32/Winbase/nf-winbase-findactctxsectionguid?branch=master)     | Returns data contained in the [**ACTCTX\_SECTION\_KEYED\_DATA**](/windows/win32/Winbase/ns-winbase-tagactctx_section_keyed_data?branch=master) structure that corresponds to the specified GUID.   |
| [**FindActCtxSectionString**](/windows/win32/Winbase/nf-winbase-findactctxsectionstringa?branch=master) | Returns data contained in the [**ACTCTX\_SECTION\_KEYED\_DATA**](/windows/win32/Winbase/ns-winbase-tagactctx_section_keyed_data?branch=master) structure that corresponds to the specified string. |
| [**GetCurrentActCtx**](/windows/win32/Winbase/nf-winbase-getcurrentactctx?branch=master)               | Returns the current activation context.                                                                                                                 |
| [**IsolationAwareCleanup**](/windows/win32/Winbase.inl/?branch=master)     | Ensures that memory is freed when a manifest is loaded, unloaded, and reloaded.                                                                         |
| [**QueryActCtxW**](/windows/win32/Winbase/nf-winbase-queryactctxw?branch=master)                       | Queries the activation context for information about an assembly or file.                                                                               |
| [**QueryActCtxSettingsW**](/windows/win32/Winbase/nf-winbase-queryactctxsettingsw?branch=master)       | Specifies the namespace and attribute name of the attribute that is to be queried.                                                                      |
| [**ReleaseActCtx**](/windows/win32/Winbase/nf-winbase-releaseactctx?branch=master)                     | Decrements the reference count of the specified activation context.                                                                                     |
| [**ZombifyActCtx**](/windows/win32/Winbase/nf-winbase-zombifyactctx?branch=master)                     | Deactivates the specified activation context, but does not deallocate it.                                                                               |



 

The following table lists activation context structures.



| Structure                                                                                                        | Description                                                                                                                                                                                                                                                                                                                                                                                  |
|------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**ACTIVATION\_CONTEXT\_ASSEMBLY\_DETAILED\_INFORMATION**](/windows/win32/Winnt/ns-winnt-_activation_context_assembly_detailed_information?branch=master) | Contains detailed information about the activation context.                                                                                                                                                                                                                                                                                                                                  |
| [**ACTIVATION\_CONTEXT\_DETAILED\_INFORMATION**](/windows/win32/Winnt/ns-winnt-_activation_context_detailed_information?branch=master)                    | Contains information about the assembly in the activation context.                                                                                                                                                                                                                                                                                                                           |
| [**ACTIVATION\_CONTEXT\_QUERY\_INDEX**](/windows/win32/Winnt/ns-winnt-_activation_context_query_index?branch=master)                                      | Contains the assembly within the activation context and the index of the file within the assembly.                                                                                                                                                                                                                                                                                           |
| [**ACTCTX**](/windows/win32/Winbase/ns-winbase-tagactctxa?branch=master)                                                                                     | Contains information that describes a specific activation context.                                                                                                                                                                                                                                                                                                                           |
| [**ACTCTX\_SECTION\_KEYED\_DATA**](/windows/win32/Winbase/ns-winbase-tagactctx_section_keyed_data?branch=master)                                            | Returns the activation context information along with either the GUID or 32-bit integer-tagged activation context section.                                                                                                                                                                                                                                                                   |
| [**ASSEMBLY\_FILE\_DETAILED\_INFORMATION**](/windows/win32/Winnt/ns-winnt-_assembly_file_detailed_information?branch=master)                              | Contains information about a file of the assembly in the activation context.                                                                                                                                                                                                                                                                                                                 |
| [**ACTIVATION\_CONTEXT\_RUN\_LEVEL\_INFORMATION**](/windows/win32/Winnt/ns-winnt-_activation_context_run_level_information?branch=master)                 | Used by the [**QueryActCtxW**](/windows/win32/Winbase/nf-winbase-queryactctxw?branch=master) function.<br/> **Windows Server 2003 and Windows XP:** This structure is not available.<br/>                                                                                                                                                                                                                                    |
| [**COMPATIBILITY\_CONTEXT\_ELEMENT**](/windows/win32/Winnt/ns-winnt-_compatibility_context_element?branch=master)                                         | Used by the [**QueryActCtxW**](/windows/win32/Winbase/nf-winbase-queryactctxw?branch=master) function as part of the [**ACTIVATION\_CONTEXT\_COMPATIBILITY\_INFORMATION**](/windows/win32/Winnt/ns-winnt-_activation_context_compatibility_information?branch=master) structure. <br/> **Windows Server 2008 and earlier, and Windows Vista and earlier:** This structure is not available. It is available beginning with Windows Server 2008 R2 and Windows 7.<br/> |
| [**ACTIVATION\_CONTEXT\_COMPATIBILITY\_INFORMATION**](/windows/win32/Winnt/ns-winnt-_activation_context_compatibility_information?branch=master)          | Used by the [**QueryActCtxW**](/windows/win32/Winbase/nf-winbase-queryactctxw?branch=master) function.<br/> **Windows Server 2008 and earlier, and Windows Vista and earlier:** This structure is not available. It is available beginning with Windows Server 2008 R2 and Windows 7.<br/>                                                                                                                                   |



 

The following table lists activation context enumerations.

| Enumeration                                                                       | Description                                                                                                                                                                                                                                            |
|-----------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**ACTCTX\_REQUESTED\_RUN\_LEVEL**](/windows/win32/Winnt/ne-winnt-actctx_requested_run_level?branch=master)               | Describes the requested run level of the activation context.**Windows Server 2003 and Windows XP:** This enumeration is not available.<br/>                                                                                                      |
| [**ACTCTX\_COMPATIBILITY\_ELEMENT\_TYPE**](/windows/win32/Winnt/ne-winnt-actctx_compatibility_element_type?branch=master) | Describes the compatibility element in the application manifest.**Windows Server 2008 and earlier, and Windows Vista and earlier:** This enumeration is not available. It is available beginning with Windows Server 2008 R2 and Windows 7.<br/> |



 

 

 




