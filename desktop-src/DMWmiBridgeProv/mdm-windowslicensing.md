---
title: MDM_WindowsLicensing class
description: The MDM\_WindowsLicensing class is designed for licensing related management scenarios.
ms.assetid: 9b26d8dc-aab6-4c67-9dbc-4b53525b9354
keywords:
- MDM_WindowsLicensing class
- MDM_WindowsLicensing class, described
topic_type:
- apiref
api_name:
- MDM_WindowsLicensing
- MDM_WindowsLicensing.InstanceID
- MDM_WindowsLicensing.ParentID
api_location:
- DMWmiBridgeProv.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# MDM\_WindowsLicensing class

\[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.\]

The **MDM\_WindowsLicensing** class is designed for licensing related management scenarios. Currently the scope is limited to edition upgrades of Windows 10 desktop and mobile devices, such as Windows 10 Pro to Windows 10 Enterprise. In addition, this CSP provides the capability to activate or change the product key of Windows 10 desktop devices.

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
[InPartition("local-system"), dynamic, provider("DMWmiBridgeProv")]
class MDM_WindowsLicensing
{
  string InstanceID;
  string ParentID;
  sint32 Edition;
  sint32 Status;
  string LicenseKeyType;
};
```

## Members

The **MDM\_WindowsLicensing** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MDM\_WindowsLicensing** class has these methods.




| Method | Description | 
|--------|-------------|
| <a href="mdm-windowslicensing-changeproductkeymethod.md"><strong>ChangeProductKeyMethod</strong></a> | Installs a product key for Windows 10 desktop devices. Does not reboot.<br /> | 
| <a href="mdm-windowslicensing-checkapplicabilitymethod.md"><strong>CheckApplicabilityMethod</strong></a> | Method to check if the entered product key can be used for an edition upgrade, activation or changing a product key of Windows 10 for desktop devices.<br /> | 
| <a href="mdm-windowslicensing-upgradeeditionwithlicensemethod.md"><strong>UpgradeEditionWithLicenseMethod</strong></a> | Provide a license for an edition upgrade of Windows 10 mobile devices.<br /><blockquote>[!Note]<br />This upgrade process does not require a system restart.</blockquote><br /><br /> The date type is XML.<br /> The supported operation is Execute.<br /><blockquote>[!Important]<br />The XML license file contents must be properly escaped (that is, it should not simply be a copied XML), otherwise the edition upgrade on Windows 10 mobile devices will fail. For more information on proper escaping of the XML license file, see Section 2.4 of the <a href="https://www.w3.org/TR/xml/">W3C XML spec</a>. The XML license file is acquired from the Microsoft Volume Licensing Service Center. Your organization must have a Volume Licensing contract with Microsoft to access the portal.</blockquote><br /> The following are valid edition upgrade paths when using this node through an MDM or provisioning package:<ul><li>Windows 10 Mobileto Windows 10 Mobile Enterprise<br /></li></ul><br /> | 
| <a href="mdm-windowslicensing-upgradeeditionwithproductkeymethod.md"><strong>UpgradeEditionWithProductKeyMethod</strong></a> | Triggers the device to take the product key and upgrade the edition of the client.<blockquote>[!Note]<br />This upgrade process requires a system restart.</blockquote><br /><br /> The supported operation is Execute.<br /> When a product key is pushed from an MDM server to a user's device, <strong>changepk.exe</strong> runs using the product key. After it completes, a notification is shown to the user that a new edition of Windows 10 is available. The user can then restart their system manually or, after two hours, the device will restart automatically to complete the upgrade. The user will receive a reminder notification 10 minutes before the automatic restart.<br /> After the device restarts, the edition upgrade process completes. The user will receive a notification of the successful upgrade.<blockquote>[!Important]<br />If another policy requires a system reboot that occurs when <strong>changepk.exe</strong> is running, the edition upgrade will fail.</blockquote><br /><br /> If a product key is entered in a provisioning package and the user begins installation of the package, a notification is shown to the user that their system will restart to complete the package installation. Upon explicit consent from the user to proceed, the package continues installation and <strong>changepk.exe</strong> runs using the product key. The user will receive a reminder notification 30 seconds before the automatic restart. <br /> After the device restarts, the edition upgrade process completes. The user will receive a notification of the successful upgrade. <br /> This node can also be used to activate or change a product key on a particular edition of Windows 10 desktop device by entering a product key. Activation or changing a product key does not require a reboot and is a silent process for the user.<br /><blockquote>[!Important]<br />The product key entered must be 29 characters (that is, it should include dashes), otherwise the activation, edition upgrade, or product key change on Windows 10 desktop devices will fail. The product key is acquired from Microsoft Volume Licensing Service Center. Your organization must have a Volume Licensing contract with Microsoft to access the portal.</blockquote><br /> The following are valid edition upgrade paths when using this node through an MDM:<ul><li>Windows 10 Enterprise to Windows 10 Education</li><li>Windows 10 Home to Windows 10 Education</li><li>Windows 10 Pro to Windows 10 Education</li><li>Windows 10 Pro to Windows 10 Enterprise</li></ul><br /> Activation or changing a product key can be carried out on the following editions:<ul><li>Windows 10 Education</li><li>Windows 10 Enterprise</li><li>Windows 10 Home</li><li>Windows 10 Pro</li></ul><br /> | 




 

### Properties

The **MDM\_WindowsLicensing** class has these properties.

<dl> <dt>

[Edition](/windows/client-management/mdm/windowslicensing-csp#edition)
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

**InstanceID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](/windows/desktop/WmiSdk/key-qualifier)
</dt> </dl>

Identifies the name of the parent node.

</dd> <dt>

[LicenseKeyType](/windows/client-management/mdm/windowslicensing-csp#licensekeytype)
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> <dt>

**ParentID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](/windows/desktop/WmiSdk/key-qualifier)
</dt> </dl>

Describes the full path to the parent node. For this class, the string is "./Vendor/MSFT/"

</dd> <dt>

[Status](/windows/client-management/mdm/windowslicensing-csp#subscriptions-subscriptionid-status)
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10 \[desktop apps only\]<br/>                                                    |
| Minimum supported server<br/> | None supported<br/>                                                                      |
| Namespace<br/>                | Root\\CIMv2\\MDM\\DMMap<br/>                                                             |
| MOF<br/>                      | <dl> <dt>DMWmiBridgeProv.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DMWmiBridgeProv.dll</dt> </dl> |



## See also

<dl> <dt>

[Using PowerShell scripting with the WMI Bridge Provider](/windows/client-management/mdm/using-powershell-scripting-with-the-wmi-bridge-provider)
</dt> </dl>

 

