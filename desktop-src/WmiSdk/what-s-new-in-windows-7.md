---
description: Whats New in Windows 7
ms.assetid: C3FE15EF-CBF0-4A5D-ADCC-108795F8CE7A
ms.tgt_platform: multiple
title: Whats New in Windows 7
ms.topic: article
ms.date: 05/31/2018
---

# Whats New in Windows 7

## New Security Feature in Windows 7

The following lists the new Windows Management Instrumentation (WMI) security feature that is available in Windows 7.

<dl> <dt>

<span id="Controlling_provider_security"></span><span id="controlling_provider_security"></span><span id="CONTROLLING_PROVIDER_SECURITY"></span>Controlling provider security
</dt> <dd>

Changes to enhance the security of the WMI shared provider host process (wmiprvse.exe). These changes introduce three new group policies and two running modes for the WMI shared host, which are called secure and compatible modes. For more information, see [Registry Keys for Controlling Provider Security](registry-keys-for-controlling-provider-security-.md).

</dd> </dl>

## Other New or Updated Features in Windows 7

The following list lists new WMI features that are available in Windows 7.

<dl> <dt>

<span id="CIM_schema_compatibility"></span><span id="cim_schema_compatibility"></span><span id="CIM_SCHEMA_COMPATIBILITY"></span>CIM schema compatibility
</dt> <dd>

Starting in Windows 7, WMI is compatible with the Common Information Model (CIM) Schema version 2.17.1. For more information, see [CIM Schema Compatibility](cim-schema-compatibility.md).

</dd> <dt>

<span id="Cross-namespace_association_traversal"></span><span id="cross-namespace_association_traversal"></span><span id="CROSS-NAMESPACE_ASSOCIATION_TRAVERSAL"></span>Cross-namespace association traversal
</dt> <dd>

WMI implemented a standard mechanism for discovering profiles by using the CIM schema. For more information, see [Cross Namespace Association Traversal](cross-namespace-association-traversal.md).

</dd> <dt>

<span id="Association_providers"></span><span id="association_providers"></span><span id="ASSOCIATION_PROVIDERS"></span>Association providers
</dt> <dd>

Information about writing and registering an association provider. Association providers are used to expose standard profiles, like a power profile. For more information, see [Writing an Association Provider for Interop](writing-an-association-provider-for-interop.md).

</dd> <dt>

<span id="Optional_feature_status"></span><span id="optional_feature_status"></span><span id="OPTIONAL_FEATURE_STATUS"></span>Optional feature status
</dt> <dd>

WMI implemented the [**Win32\_OptionalFeature**](/windows/desktop/CIMWin32Prov/win32-optionalfeature) class. This class queries and returns the status of the optional features that are present on a computer. For example queries using Windows PowerShell, see [Querying the Status of Optional Features](querying-the-status-of-optional-features.md).

</dd> <dt>

<span id="Changing_the_default_behavior_for_the_AutoRestore_repository_feature"></span><span id="changing_the_default_behavior_for_the_autorestore_repository_feature"></span><span id="CHANGING_THE_DEFAULT_BEHAVIOR_FOR_THE_AUTORESTORE_REPOSITORY_FEATURE"></span>Changing the default behavior for the AutoRestore repository feature
</dt> <dd>

WMI has a new registry key to enable or disable the AutoRestore repository feature. For more information, see [Registry Key for Repository Configuration](registry-key-for-repository-configuration.md).

</dd> <dt>

<span id="New__PowerShell_command_classes"></span><span id="new__powershell_command_classes"></span><span id="NEW__POWERSHELL_COMMAND_CLASSES"></span>New Windows PowerShell command classes
</dt> <dd>

Windows PowerShell cmdlets enable users to complete the end-to-end tasks necessary to manage local and remote computers. For more information, see [Managed Reference for WMI PowerShell Command Classes](managed-reference-for-wmi-powershell-command-classes.md).

</dd> <dt>

<span id="New_mechanism_to_connect_to_remote_computers"></span><span id="new_mechanism_to_connect_to_remote_computers"></span><span id="NEW_MECHANISM_TO_CONNECT_TO_REMOTE_COMPUTERS"></span>New mechanism to connect to remote computers
</dt> <dd>

Windows PowerShell provides a simple mechanism to connect to WMI on a remote computer. For more information, see [Connecting to WMI on a Remote Computer by using PowerShell](connecting-to-wmi-on-a-remote-computer-by-using-powershell.md).

</dd> <dt>

<span id="Changes_to_the_software_licensing_classes"></span><span id="changes_to_the_software_licensing_classes"></span><span id="CHANGES_TO_THE_SOFTWARE_LICENSING_CLASSES"></span>Changes to the software licensing classes
</dt> <dd>

The [software licensing classes](/previous-versions/windows/desktop/sppwmi/software-license-provider-) have new methods and properties to provide more software licensing data. In addition, the [**SoftwareLicensingTokenActivationLicense**](/previous-versions/windows/desktop/sppwmi/softwarelicensingtokenactivationlicense) class was added.

</dd> <dt>

<span id="New_power_metering_and_budgeting_classes"></span><span id="new_power_metering_and_budgeting_classes"></span><span id="NEW_POWER_METERING_AND_BUDGETING_CLASSES"></span>New power metering and budgeting classes
</dt> <dd>

[Power metering and budgeting classes](/previous-versions/windows/desktop/powermeterprov/power-meter-provider-) are the primary interface for the query of Power Meter Interface (PMI) information from underlying power meters on the system.

</dd> <dt>

<span id="New_power_policy_classes"></span><span id="new_power_policy_classes"></span><span id="NEW_POWER_POLICY_CLASSES"></span>New power policy classes
</dt> <dd>

[Power policy classes](/previous-versions/windows/desktop/powerwmiprov/power-policy-provider-) enable the remote management of all power policy infrastructures.

</dd> <dt>

<span id="Changes_to_the_Win32_ServerFeature_class"></span><span id="changes_to_the_win32_serverfeature_class"></span><span id="CHANGES_TO_THE_WIN32_SERVERFEATURE_CLASS"></span>Changes to the [**Win32\_ServerFeature**](win32-serverfeature.md) class
</dt> <dd>

The **ID** property of the [**Win32\_ServerFeature**](win32-serverfeature.md) was updated.

</dd> </dl>

For more information about new features in previous operating system versions, see [What's New in Windows Vista](what-s-new-in-windows-vista.md).

## Related topics

<dl> <dt>

[About WMI](about-wmi.md)
</dt> </dl>

 

 
