---
Description: 'On 64-bit Windows, portions of the registry entries are stored separately for 32-bit application and 64-bit applications and mapped into separate logical registry views using the registry redirector and registry reflection, because the 64-bit version of an application may use different registry keys and values than the 32-bit version. There are also shared registry keys that are not redirected or reflected.'
ms.assetid: '08dc034c-15ce-41d9-8e74-a49b61ad40a6'
title: '32-bit and 64-bit Application Data in the Registry'
---

# 32-bit and 64-bit Application Data in the Registry

On 64-bit Windows, portions of the registry entries are stored separately for 32-bit application and 64-bit applications and mapped into separate logical registry views using the [registry redirector](https://msdn.microsoft.com/library/windows/desktop/aa384232) and [registry reflection](https://msdn.microsoft.com/library/windows/desktop/aa384235), because the 64-bit version of an application may use different registry keys and values than the 32-bit version. There are also [shared registry keys](https://msdn.microsoft.com/library/windows/desktop/aa384253) that are not redirected or reflected.

The parent of each 64-bit registry node is the Image-Specific Node or ISN. The registry redirector transparently directs an application's registry access to the appropriate ISN subnode. Redirection subnodes in the registry tree are created automatically by the WOW64 component using the name **Wow6432Node**. As a result, it is essential not to name any registry key you create **Wow6432Node**.

The KEY\_WOW64\_64KEY and KEY\_WOW64\_32KEY flags enable explicit access to the 64-bit registry view and the 32-bit view, respectively. For more information, see [Accessing an Alternate Registry View](https://msdn.microsoft.com/library/windows/desktop/aa384129).

To disable and enable registry reflection for a particular key, use the [**RegDisableReflectionKey**](regdisablereflectionkey.md) and [**RegEnableReflectionKey**](regenablereflectionkey.md) functions. Applications should disable reflection only for the registry keys that they create and not attempt to disable reflection for the predefined keys such as **HKEY\_LOCAL\_MACHINE** or **HKEY\_CURRENT\_USER**. To determine which keys are on the reflection list, use the [**RegQueryReflectionKey**](regqueryreflectionkey.md) function.

## Related topics

<dl> <dt>

[Registry Redirector](https://msdn.microsoft.com/library/windows/desktop/aa384232)
</dt> <dt>

[Registry Reflection](https://msdn.microsoft.com/library/windows/desktop/aa384235)
</dt> </dl>

 

 



