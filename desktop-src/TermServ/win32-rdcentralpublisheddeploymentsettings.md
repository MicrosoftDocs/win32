---
title: Win32_RDCentralPublishedDeploymentSettings class
description: Contains the deployment settings used to generate RDP files for resources published from a farm.
ms.assetid: 6d1be0b2-e070-4c60-8068-b59ba121bf9f
ms.tgt_platform: multiple
keywords:
- Win32_RDCentralPublishedDeploymentSettings class Remote Desktop Services
- Win32_RDCentralPublishedDeploymentSettings class Remote Desktop Services , described
topic_type:
- apiref
api_name:
- Win32_RDCentralPublishedDeploymentSettings
- Win32_RDCentralPublishedDeploymentSettings.Caption
- Win32_RDCentralPublishedDeploymentSettings.Description
- Win32_RDCentralPublishedDeploymentSettings.InstallDate
- Win32_RDCentralPublishedDeploymentSettings.Name
- Win32_RDCentralPublishedDeploymentSettings.Status
- Win32_RDCentralPublishedDeploymentSettings.PublishingFarm
- Win32_RDCentralPublishedDeploymentSettings.Port
- Win32_RDCentralPublishedDeploymentSettings.FarmName
- Win32_RDCentralPublishedDeploymentSettings.GatewayUsage
- Win32_RDCentralPublishedDeploymentSettings.GatewayName
- Win32_RDCentralPublishedDeploymentSettings.GatewayAuthMode
- Win32_RDCentralPublishedDeploymentSettings.GatewayUseCachedCreds
- Win32_RDCentralPublishedDeploymentSettings.ColorBitDepth
- Win32_RDCentralPublishedDeploymentSettings.AllowFontSmoothing
- Win32_RDCentralPublishedDeploymentSettings.UseMultimon
- Win32_RDCentralPublishedDeploymentSettings.RedirectionOptions
- Win32_RDCentralPublishedDeploymentSettings.HasCertificate
- Win32_RDCentralPublishedDeploymentSettings.CertificateHash
- Win32_RDCentralPublishedDeploymentSettings.CustomRDPSettings
- Win32_RDCentralPublishedDeploymentSettings.DeploymentRDPSettings
api_location:
- TscPubWmi.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# Win32\_RDCentralPublishedDeploymentSettings class

Contains the deployment settings used to generate RDP files for resources published from a farm.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[provider("Win32_TSCentralPublisher_Prov"), dynamic]
class Win32_RDCentralPublishedDeploymentSettings : CIM_LogicalElement
{
  string   Caption;
  string   Description;
  datetime InstallDate;
  string   Name;
  string   Status;
  string   PublishingFarm;
  sint32   Port;
  string   FarmName;
  sint32   GatewayUsage;
  string   GatewayName;
  sint32   GatewayAuthMode;
  boolean  GatewayUseCachedCreds;
  sint32   ColorBitDepth;
  boolean  AllowFontSmoothing;
  boolean  UseMultimon;
  sint32   RedirectionOptions;
  boolean  HasCertificate;
  uint8    CertificateHash[];
  string   CustomRDPSettings;
  string   DeploymentRDPSettings;
};
```

## Members

The **Win32\_RDCentralPublishedDeploymentSettings** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_RDCentralPublishedDeploymentSettings** class has these properties.

<dl> <dt>

**AllowFontSmoothing**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

**true** to allow font smoothing; otherwise, **false**.

</dd> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](/windows/desktop/WmiSdk/standard-qualifiers) (64)
</dt> </dl>

Short description (one-line string) of the object.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

</dd> <dt>

**CertificateHash**
</dt> <dd> <dl> <dt>

Data type: **uint8** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

The certificate used to sign the RDP files; necessarily only if *HasCertificate* is true.

</dd> <dt>

**ColorBitDepth**
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Contains the color bit depth:

<dt>

<span id="4"></span>

**4** ()


</dt> <dd></dd> <dt>

<span id="8"></span>

**8** ()


</dt> <dd></dd> <dt>

<span id="15"></span>

**15** ()


</dt> <dd></dd> <dt>

<span id="16"></span>

**16** ()


</dt> <dd></dd> <dt>

<span id="24"></span>

**24** ()


</dt> <dd></dd> <dt>

<span id="32"></span>

**32** ()


</dt> <dd></dd> </dl>

</dd> <dt>

**CustomRDPSettings**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Contains the contents of the RDP file corresponding to the custom RDP settings.

</dd> <dt>

**DeploymentRDPSettings**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Contains the contents of the RDP file corresponding to the deployment settings. If this parameter is set, the system will use this RDP file, and ignore the other RDP settings in this call.

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Description of the object.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

</dd> <dt>

**FarmName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The name of the farm.

</dd> <dt>

**GatewayAuthMode**
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Contains the gateway authentication mode:

<dt>

<span id="Password_0_"></span><span id="password_0_"></span><span id="PASSWORD_0_"></span>

<span id="Password_0_"></span><span id="password_0_"></span><span id="PASSWORD_0_"></span>**Password(0)** (0)


</dt> <dd></dd> <dt>

<span id="Smartcard_1_"></span><span id="smartcard_1_"></span><span id="SMARTCARD_1_"></span>

<span id="Smartcard_1_"></span><span id="smartcard_1_"></span><span id="SMARTCARD_1_"></span>**Smartcard(1)** (1)


</dt> <dd></dd> <dt>

<span id="Allow_User_to_Choose_4_"></span><span id="allow_user_to_choose_4_"></span><span id="ALLOW_USER_TO_CHOOSE_4_"></span>

<span id="Allow_User_to_Choose_4_"></span><span id="allow_user_to_choose_4_"></span><span id="ALLOW_USER_TO_CHOOSE_4_"></span>**Allow User to Choose(4)** (4)


</dt> <dd></dd> </dl>

</dd> <dt>

**GatewayName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The name of the gateway.

</dd> <dt>

**GatewayUsage**
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Describes how the gateway is used:

<dt>

<span id="NoGateway"></span><span id="nogateway"></span><span id="NOGATEWAY"></span>

<span id="NoGateway"></span><span id="nogateway"></span><span id="NOGATEWAY"></span>**NoGateway** (0)


</dt> <dd>

No gateway.

</dd> <dt>

<span id="UseGatewayBypassLocal"></span><span id="usegatewaybypasslocal"></span><span id="USEGATEWAYBYPASSLOCAL"></span>

<span id="UseGatewayBypassLocal"></span><span id="usegatewaybypasslocal"></span><span id="USEGATEWAYBYPASSLOCAL"></span>**UseGatewayBypassLocal** (1)


</dt> <dd>

Use gateway pass by local.

</dd> <dt>

<span id="UseGateway"></span><span id="usegateway"></span><span id="USEGATEWAY"></span>

<span id="UseGateway"></span><span id="usegateway"></span><span id="USEGATEWAY"></span>**UseGateway** (2)


</dt> <dd>

Use gateway.

</dd> <dt>

<span id="DetectGateway"></span><span id="detectgateway"></span><span id="DETECTGATEWAY"></span>

<span id="DetectGateway"></span><span id="detectgateway"></span><span id="DETECTGATEWAY"></span>**DetectGateway** (3)


</dt> <dd>

Detect gateway.

</dd> </dl>

</dd> <dt>

**GatewayUseCachedCreds**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

**true** to use the same user credentials for TS gateway and TS server when possible; otherwise, **false**.

</dd> <dt>

**HasCertificate**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

**true** to use a certificate to sign the RDP files; otherwise, **false**.

</dd> <dt>

**InstallDate**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Mappingstrings**](/windows/desktop/WmiSdk/standard-qualifiers) ("MIF.DMTF\|ComponentID\|001.5")
</dt> </dl>

The date the object was installed. A lack of a value does not indicate that the object is not installed.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The name of the object.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

</dd> <dt>

**Port**
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The RDP port.

</dd> <dt>

**PublishingFarm**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**key**](/windows/desktop/WmiSdk/key-qualifier)
</dt> </dl>

The alias of the farm that published the application.

</dd> <dt>

**RedirectionOptions**
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Redirection Options:

<dt>

0
</dt> <dd>

None

</dd> <dt>

1
</dt> <dd>

Drives

</dd> <dt>

2
</dt> <dd>

Printers

</dd> <dt>

4
</dt> <dd>

Clipboard

</dd> <dt>

8
</dt> <dd>

Plug and Play

</dd> <dt>

16
</dt> <dd>

Smart Card

</dd> </dl>

</dd> <dt>

**Status**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](/windows/desktop/WmiSdk/standard-qualifiers) (10)
</dt> </dl>

Current status of the object. Various operational and nonoperational statuses can be defined. Operational statuses include: "OK", "Degraded", and "Pred Fail" (an element, such as a SMART-enabled hard disk drive, may be functioning properly but predicting a failure in the near future). Nonoperational statuses include: "Error", "Starting", "Stopping", and "Service". The latter, "Service", could apply during mirror-resilvering of a disk, reload of a user permissions list, or other administrative work. Not all such work is on-line, yet the managed element is neither "OK" nor in one of the other states.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

<dt>



 ("OK")


</dt> <dd></dd> <dt>



 ("Error")


</dt> <dd></dd> <dt>



 ("Degraded")


</dt> <dd></dd> <dt>



 ("Unknown")


</dt> <dd></dd> <dt>



 ("Pred Fail")


</dt> <dd></dd> <dt>



 ("Starting")


</dt> <dd></dd> <dt>



 ("Stopping")


</dt> <dd></dd> <dt>



 ("Service")


</dt> <dd></dd> </dl>

</dd> <dt>

**UseMultimon**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

**true** to enable multi-monitor for desktop (not RAIL); otherwise, **false**.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                           |
| Namespace<br/>                | Root\\cimv2\\TerminalServices<br/>                                                 |
| MOF<br/>                      | <dl> <dt>Tscpub.mof</dt> </dl>    |
| DLL<br/>                      | <dl> <dt>TscPubWmi.dll</dt> </dl> |



 

