---
description: The Component table lists components and it has the following columns.
ms.assetid: 069d64e9-106a-42b7-8dea-a44fc0c6e0cd
title: Component Table
ms.topic: article
ms.date: 05/31/2018
---

# Component Table

The Component table lists components and it has the following columns.



| Column      | Type                         | Key | Nullable |
|-------------|------------------------------|-----|----------|
| Component   | [Identifier](identifier.md) | Y   | N        |
| ComponentId | [GUID](guid.md)             | N   | Y        |
| Directory\_ | [Identifier](identifier.md) | N   | N        |
| Attributes  | [Integer](integer.md)       | N   | N        |
| Condition   | [Condition](condition.md)   | N   | Y        |
| KeyPath     | [Identifier](identifier.md) | N   | Y        |



 

## Columns

<dl> <dt>

<span id="Component"></span><span id="component"></span><span id="COMPONENT"></span>Component
</dt> <dd>

Identifies the component record.

Primary table key.

</dd> <dt>

<span id="ComponentId"></span><span id="componentid"></span><span id="COMPONENTID"></span>ComponentId
</dt> <dd>

A string GUID unique to this component, version, and language.

Note that the letters of these GUIDs must be uppercase. Utilities such as GUIDGEN can generate GUIDs containing lowercase letters. The lowercase letters must be changed to uppercase to make these valid component code GUIDs.

If this column is null the installer does not register the component and the component cannot be removed or repaired by the installer. This might be intentionally done if the component is only needed during the installation, such as a custom action that cleans up temporary files or removes an old product. It may also be useful when copying data files to a user's computer that do not need to be registered.

</dd> <dt>

<span id="Directory_"></span><span id="directory_"></span><span id="DIRECTORY_"></span>Directory\_
</dt> <dd>

External key of an entry in the [Directory table](directory-table.md). This is a property name whose value contains the actual path, which can be set either by the [AppSearch action](appsearch-action.md) or with the default setting obtained from the Directory table.

Developers must avoid authoring components that place files into one of the User Profile folders. These files would not be available to all users in multi-user situations and could cause the installer to permanently view the component as requiring repair.

External key to column one of the Directory table.

</dd> <dt>

<span id="Attributes"></span><span id="attributes"></span><span id="ATTRIBUTES"></span>Attributes
</dt> <dd>

This column contains a bit flag that specifies options for remote execution. Add the indicated bit to the total value in the column to include an option.

> [!Note]  
> In the case of an .msi file that is being downloaded from a web location, the attribute flags should not be set to allow a component to be run-from-source. This is a limitation of the Windows Installer and can return a feature state of INSTALLSTATE\_BADCONFIG.

 



<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Bit flag</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><dl> <dt><strong>msidbComponentAttributesLocalOnly</strong></dt> <dt>0</dt> <dt>0x0000</dt> </dl> Component cannot be run from source. Set this bit for all components belonging to a feature to prevent the feature from being run-from-network or run-from-source. Note that if a feature has no components, the feature always shows run-from-source and run-from-my-computer as valid options.<br/></td>
</tr>
<tr class="even">
<td><dl> <dt><strong>msidbComponentAttributesSourceOnly</strong></dt> <dt>1</dt> <dt>0x0001</dt> </dl> Component can only be run from source. Set this bit for all components belonging to a feature to prevent the feature from being run-from-my-computer. Note that if a feature has no components, the feature always shows run-from-source and run-from-my-computer as valid options.<br/></td>
</tr>
<tr class="odd">
<td><dl> <dt><strong>msidbComponentAttributesOptional</strong></dt> <dt>2</dt> <dt>0x0002</dt> </dl> Component can run locally or from source.<br/></td>
</tr>
<tr class="even">
<td><dl> <dt><strong>msidbComponentAttributesRegistryKeyPath</strong></dt> <dt>4</dt> <dt>0x0004</dt> </dl> If this bit is set, the value in the KeyPath column is used as a key into the <a href="registry-table.md">Registry table</a>. If the Value field of the corresponding record in the Registry table is null, the Name field in that record must not contain &quot;+&quot;, &quot;-&quot;, or &quot;*&quot;. For more information, see the description of the Name field in <a href="registry-table.md">Registry table</a>.<br/> Setting this bit is recommended for registry entries written to the HKCU hive. This ensures the installer writes the necessary HKCU registry entries when there are multiple users on the same machine.<br/></td>
</tr>
<tr class="odd">
<td><dl> <dt><strong>msidbComponentAttributesSharedDllRefCount</strong></dt> <dt>8</dt> <dt>0x0008</dt> </dl> If this bit is set, the installer increments the reference count in the shared DLL registry of the component's key file. If this bit is not set, the installer increments the reference count only if the reference count already exists.<br/></td>
</tr>
<tr class="even">
<td><dl> <dt><strong>msidbComponentAttributesPermanent</strong></dt> <dt>16</dt> <dt>0x0010</dt> </dl> If this bit is set, the installer does not remove the component during an uninstall. The installer registers an extra system client for the component in the Windows Installer registry settings.<br/></td>
</tr>
<tr class="odd">
<td><dl> <dt><strong>msidbComponentAttributesODBCDataSource</strong></dt> <dt>32</dt> <dt>0x0020</dt> </dl> If this bit is set, the value in the KeyPath column is a key into the <a href="odbcdatasource-table.md">ODBCDataSource table</a>.<br/></td>
</tr>
<tr class="even">
<td><dl> <dt><strong>msidbComponentAttributesTransitive</strong></dt> <dt>64</dt> <dt>0x0040</dt> </dl> If this bit is set, the installer reevaluates the value of the statement in the Condition column upon a reinstall. If the value was previously False and has changed to True, the installer installs the component. If the value was previously True and has changed to False, the installer removes the component even if the component has other products as clients.<br/> This bit should only be set for transitive components. See <a href="using-transitive-components.md">Using Transitive Components</a>.<br/></td>
</tr>
<tr class="odd">
<td><dl> <dt><strong>msidbComponentAttributesNeverOverwrite</strong></dt> <dt>128</dt> <dt>0x0080</dt> </dl> If this bit is set, the installer does not install or reinstall the component if a key path file or a key path registry entry for the component already exists. The application does register itself as a client of the component.<br/> Use this flag only for components that are being registered by the Registry table. Do not use this flag for components registered by the <a href="appid-table.md">AppId</a>, <a href="class-table.md">Class</a>, <a href="extension-table.md">Extension</a>, <a href="progid-table.md">ProgId</a>, <a href="mime-table.md">MIME</a>, and <a href="verb-table.md">Verb tables</a>.<br/></td>
</tr>
<tr class="even">
<td><dl> <dt><strong>msidbComponentAttributes64bit</strong></dt> <dt>256</dt> <dt>0x0100</dt> </dl> Set this bit to mark this as a 64-bit component. This attribute facilitates the installation of packages that include both 32-bit and 64-bit components. If this bit is not set, the component is registered as a 32-bit component.<br/> If this is a 64-bit component replacing a 32-bit component, set this bit and assign a new GUID in the ComponentId column.<br/></td>
</tr>
<tr class="odd">
<td><dl> <dt><strong>msidbComponentAttributesDisableRegistryReflection</strong></dt> <dt>512</dt> <dt>0x0200</dt> </dl> Set this bit to disable <a href="/windows/desktop/WinProg64/registry-reflection">Registry Reflection</a> on all existing and new registry keys affected by this component. If this bit is set, the Windows Installer calls the <a href="/windows/desktop/api/winreg/nf-winreg-regdisablereflectionkey"><strong>RegDisableReflectionKey</strong></a> on each key being accessed by the component. This bit is available with Windows Installer version 4.0. This bit is ignored on 32-bit systems. This bit is ignored on the 64-bit versions of Windows XP.<br/>
<blockquote>
[!Note]<br />
32-bit Windows applications running on the 64-bit Windows emulator (WOW64) refer to a different view of the registry than 64-bit applications. Registry reflection copies some registry values between these two registry views.
</blockquote>
<br/> <br/></td>
</tr>
<tr class="even">
<td><dl> <dt><strong>msidbComponentAttributesUninstallOnSupersedence</strong></dt> <dt>1024</dt> <dt>0x0400</dt> </dl> Set this bit for a component in a patch package to prevent leaving orphan components on the computer. If a subsequent patch is installed, marked with the <strong>msidbPatchSequenceSupersedeEarlier</strong> value in its <a href="msipatchsequence-table.md">MsiPatchSequence</a> table to supersede the first patch, Windows Installer 4.5 and later can unregister and uninstall components marked with the <strong>msidbComponentAttributesUninstallOnSupersedence</strong> value. If the component is not marked with this bit, installation of a superseding patch can leave behind an unused component on the computer.<br/> Setting the <strong>MSIUNINSTALLSUPERSEDEDCOMPONENTS</strong> property has the same effect as setting this bit for all components.<br/> <strong><a href="not-supported-in-windows-installer-4-0.md">Windows Installer 4.0 and earlier</a>:</strong> The <strong>msidbComponentAttributesUninstallOnSupersedence</strong> value is not supported and is ignored.<br/> <br/></td>
</tr>
<tr class="odd">
<td><dl> <dt><strong>msidbComponentAttributesShared</strong></dt> <dt>2048</dt> <dt>0x0800</dt> </dl> If a component is marked with this attribute value in at least one package installed on the system, the installer treats the component as marked in all packages. If a package that shares the marked component is uninstalled, Windows Installer 4.5 can continue to share the highest version of the component on the system, even if that highest version was installed by the package that is being uninstalled. <br/> If the DisableSharedComponent policy is set to 1, no package gets the shared component functionality enabled by this bit.<br/> <strong><a href="not-supported-in-windows-installer-4-0.md">Windows Installer 4.0 and earlier</a>:</strong> The <strong>msidbComponentAttributesShared</strong> value is not supported and is ignored.<br/> <br/></td>
</tr>
</tbody>
</table>



 

</dd> <dt>

<span id="Condition"></span><span id="condition"></span><span id="CONDITION"></span>Condition
</dt> <dd>

This column contains a conditional statement that can control whether a component is installed. If the condition is null or evaluates to true, then the component is enabled. If the condition evaluates to False, then the component is disabled and is not installed.

The Condition field enables or disables a component only during the [CostFinalize action](costfinalize-action.md). To enable or disable a component after CostFinalize, you must use a custom action or the [DoAction ControlEvent](doaction-controlevent.md) to call [**MsiSetComponentState**](/windows/desktop/api/Msiquery/nf-msiquery-msisetcomponentstatea).

Note that unless the Transitive bit in the Attributes column is set for a component, the component remains enabled once installed even if the conditional statement in the Condition column later evaluates to False on a subsequent maintenance installation of the product.

The Condition column in the Component table accepts conditional expressions containing references to the installed states of features and components. For information on the syntax of conditional statements, see [Conditional Statement Syntax](conditional-statement-syntax.md).

</dd> <dt>

<span id="KeyPath"></span><span id="keypath"></span><span id="KEYPATH"></span>KeyPath
</dt> <dd>

This value points to a file or folder belonging to the component that the installer uses to detect the component. Two components cannot share the same key path value. The value in this column is also the path returned by the [**MsiGetComponentPath**](/windows/desktop/api/Msi/nf-msi-msigetcomponentpatha) function.

If the value is not null, then KeyPath is either a primary key into the [Registry](registry-table.md), [ODBCDataSource](odbcdatasource-table.md), or [File tables](file-table.md) depending upon the Attribute value. If KeyPath is null, then the folder of the Directory\_ column is used as the key path.

Because folders created by the installer are deleted when they become empty, you must author an entry into the [CreateFolder table](createfolder-table.md) to install a component that consists of an empty folder.

Note that if a Windows Installer component contains a file or registry key that is protected by [Windows Resource Protection](/windows/desktop/Wfp/windows-resource-protection-portal) (WRP) or a file that is protected by Windows File Protection (WFP), this resource must be used as the KeyPath for the component. In this case, Windows Installer does not install, update, or remove the component. You should not include any protected resources in an installation package. Instead, you should use the [supported resource replacement mechanisms](/windows/desktop/Wfp/supported-file-replacement-mechanisms) for Windows Resource Protection. For more information, see [Using Windows Installer and Windows Resource Protection](windows-resource-protection-on-windows-vista.md).

</dd> </dl>

## Remarks

For a discussion of the relationship between components and features, see [Feature Table](feature-table.md).

The installer keeps track of shared DLLs independently of the shared DLL reference count in the registry. If a reference count for a shared DLL exists in the registry, the installer always increments the count when it is installing the file and decrements it when it is uninstalling. If **msidbComponentAttributesSharedDllRefCount**, is not set, and the reference count does not already exist, the installer will not create one. Note that the SharedDLLs reference count in the registry is incremented for any files installed to the System folder.

If **msidbComponentAttributesSharedDllRefCount** is not set, then another application can remove the component even if it is still needed. To see how this could happen consider the following scenario:

-   An application that uses the installer installs a shared component.
-   The **msidbComponentAttributesSharedDllRefCount** bit is not set and there is no reference count. Thus the installer does not begin a reference count.
-   A legacy application that shares this component and does not use the installer is installed.
-   The legacy application creates and increments a reference count for the shared component.
-   The legacy application is uninstalled.
-   The reference count for the shared component is decremented to zero and the component is removed.
-   The application using the installer no longer has access to the component.

To avoid this behavior, set **msidbComponentAttributesSharedDllRefCount**.

Note that system services components should not be specified as run-from-source without being specifically designed for such use. See the [ServiceInstall table](serviceinstall-table.md) for more details.

Note that attributes enabling run-from-source installation should never be set for components containing dynamic-link libraries that are going into the system folder. The reason is that if the installation state of the component becomes set to run-from-source by following a feature or by being set in the UI, subsequent calls to **LoadLibrary** on the DLL would fail.

See also, [Controlling Feature Selection States](controlling-feature-selection-states.md).

## Validation

<dl>

[ICE02](ice02.md)  
[ICE03](ice03.md)  
[ICE06](ice06.md)  
[ICE07](ice07.md)  
[ICE08](ice08.md)  
[ICE09](ice09.md)  
[ICE18](ice18.md)  
[ICE19](ice19.md)  
[ICE21](ice21.md)  
[ICE30](ice30.md)  
[ICE32](ice32.md)  
[ICE35](ice35.md)  
[ICE38](ice38.md)  
[ICE41](ice41.md)  
[ICE42](ice42.md)  
[ICE43](ice43.md)  
[ICE46](ice46.md)  
[ICE50](ice50.md)  
[ICE54](ice54.md)  
[ICE57](ice57.md)  
[ICE59](ice59.md)  
[ICE62](ice62.md)  
[ICE67](ice67.md)  
[ICE76](ice76.md)  
[ICE79](ice79.md)  
[ICE80](ice80.md)  
[ICE83](ice83.md)  
[ICE86](ice86.md)  
[ICE88](ice88.md)  
[ICE91](ice91.md)  
[ICE92](ice92.md)  
[ICE97](ice97.md)  
</dl>

