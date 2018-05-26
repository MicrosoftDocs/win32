---
title: MSFT\_MpThreatCatalog class
description: This class represents the catalog of recognized threats.
ms.assetid: 3d207993-4b8a-4444-8c23-f86ecd103b6b
keywords:
- MSFT_MpThreatCatalog class
- MSFT_MpThreatCatalog class, described
topic_type:
- apiref
api_name:
- MSFT_MpThreatCatalog
- MSFT_MpThreatCatalog.ThreatID
- MSFT_MpThreatCatalog.ThreatName
- MSFT_MpThreatCatalog.SeverityID
- MSFT_MpThreatCatalog.CategoryID
- MSFT_MpThreatCatalog.TypeID
api_location:
- ProtectionManagement.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MSFT\_MpThreatCatalog class

This class represents the catalog of recognized threats

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
class MSFT_MpThreatCatalog : BaseStatus
{
  sint64 ThreatID;
  string ThreatName;
  uint8  SeverityID;
  uint8  CategoryID;
  uint8  TypeID;
};
```

## Members

The **MSFT\_MpThreatCatalog** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_MpThreatCatalog** class has these properties.

<dl> <dt>

**CategoryID**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Category ID - Enumeration

<dl> <dt>

<span id="INVALID"></span><span id="invalid"></span>**INVALID** (0)
</dt> <dt>

<span id="ADWARE"></span><span id="adware"></span>**ADWARE** (1)
</dt> <dt>

<span id="SPYWARE"></span><span id="spyware"></span>**SPYWARE** (2)
</dt> <dt>

<span id="PASSWORDSTEALER"></span><span id="passwordstealer"></span>**PASSWORDSTEALER** (3)
</dt> <dt>

<span id="TROJANDOWNLOADER"></span><span id="trojandownloader"></span>**TROJANDOWNLOADER** (4)
</dt> <dt>

<span id="WORM"></span><span id="worm"></span>**WORM** (5)
</dt> <dt>

<span id="BACKDOOR"></span><span id="backdoor"></span>**BACKDOOR** (6)
</dt> <dt>

<span id="REMOTEACCESSTROJAN"></span><span id="remoteaccesstrojan"></span>**REMOTEACCESSTROJAN** (7)
</dt> <dt>

<span id="TROJAN"></span><span id="trojan"></span>**TROJAN** (8)
</dt> <dt>

<span id="EMAILFLOODER"></span><span id="emailflooder"></span>**EMAILFLOODER** (9)
</dt> <dt>

<span id="KEYLOGGER"></span><span id="keylogger"></span>**KEYLOGGER** (10)
</dt> <dt>

<span id="DIALER"></span><span id="dialer"></span>**DIALER** (11)
</dt> <dt>

<span id="MONITORINGSOFTWARE"></span><span id="monitoringsoftware"></span>**MONITORINGSOFTWARE** (12)
</dt> <dt>

<span id="BROWSERMODIFIER"></span><span id="browsermodifier"></span>**BROWSERMODIFIER** (13)
</dt> <dt>

<span id="COOKIE"></span><span id="cookie"></span>**COOKIE** (14)
</dt> <dt>

<span id="BROWSERPLUGIN"></span><span id="browserplugin"></span>**BROWSERPLUGIN** (15)
</dt> <dt>

<span id="AOLEXPLOIT"></span><span id="aolexploit"></span>**AOLEXPLOIT** (16)
</dt> <dt>

<span id="NUKER"></span><span id="nuker"></span>**NUKER** (17)
</dt> <dt>

<span id="SECURITYDISABLER"></span><span id="securitydisabler"></span>**SECURITYDISABLER** (18)
</dt> <dt>

<span id="JOKEPROGRAM"></span><span id="jokeprogram"></span>**JOKEPROGRAM** (19)
</dt> <dt>

<span id="HOSTILEACTIVEXCONTROL"></span><span id="hostileactivexcontrol"></span>**HOSTILEACTIVEXCONTROL** (20)
</dt> <dt>

<span id="SOFTWAREBUNDLER"></span><span id="softwarebundler"></span>**SOFTWAREBUNDLER** (21)
</dt> <dt>

<span id="STEALTHNOTIFIER"></span><span id="stealthnotifier"></span>**STEALTHNOTIFIER** (22)
</dt> <dt>

<span id="SETTINGSMODIFIER"></span><span id="settingsmodifier"></span>**SETTINGSMODIFIER** (23)
</dt> <dt>

<span id="TOOLBAR"></span><span id="toolbar"></span>**TOOLBAR** (24)
</dt> <dt>

<span id="REMOTECONTROLSOFTWARE"></span><span id="remotecontrolsoftware"></span>**REMOTECONTROLSOFTWARE** (25)
</dt> <dt>

<span id="TROJANFTP"></span><span id="trojanftp"></span>**TROJANFTP** (26)
</dt> <dt>

<span id="POTENTIALUNWANTEDSOFTWARE"></span><span id="potentialunwantedsoftware"></span>**POTENTIALUNWANTEDSOFTWARE** (27)
</dt> <dt>

<span id="ICQEXPLOIT"></span><span id="icqexploit"></span>**ICQEXPLOIT** (28)
</dt> <dt>

<span id="TROJANTELNET"></span><span id="trojantelnet"></span>**TROJANTELNET** (29)
</dt> <dt>

<span id="FILESHARINGPROGRAM"></span><span id="filesharingprogram"></span>**FILESHARINGPROGRAM** (30)
</dt> <dt>

<span id="MALWARE_CREATION_TOOL"></span><span id="malware_creation_tool"></span>**MALWARE\_CREATION\_TOOL** (31)
</dt> <dt>

<span id="REMOTE_CONTROL_SOFTWARE"></span><span id="remote_control_software"></span>**REMOTE\_CONTROL\_SOFTWARE** (32)
</dt> <dt>

<span id="TOOL"></span><span id="tool"></span>**TOOL** (33)
</dt> <dt>

<span id="TROJAN_DENIALOFSERVICE"></span><span id="trojan_denialofservice"></span>**TROJAN\_DENIALOFSERVICE** (34)
</dt> <dt>

<span id="TROJAN_DROPPER"></span><span id="trojan_dropper"></span>**TROJAN\_DROPPER** (36)
</dt> <dt>

<span id="TROJAN_MASSMAILER"></span><span id="trojan_massmailer"></span>**TROJAN\_MASSMAILER** (37)
</dt> <dt>

<span id="TROJAN_MONITORINGSOFTWARE"></span><span id="trojan_monitoringsoftware"></span>**TROJAN\_MONITORINGSOFTWARE** (38)
</dt> <dt>

<span id="TROJAN_PROXYSERVER"></span><span id="trojan_proxyserver"></span>**TROJAN\_PROXYSERVER** (39)
</dt> <dt>

<span id="VIRUS"></span><span id="virus"></span>**VIRUS** (40)
</dt> <dt>

<span id="KNOWN"></span><span id="known"></span>**KNOWN** (42)
</dt> <dt>

<span id="UNKNOWN"></span><span id="unknown"></span>**UNKNOWN** (43)
</dt> <dt>

<span id="SPP"></span><span id="spp"></span>**SPP** (44)
</dt> <dt>

<span id="BEHAVIOR"></span><span id="behavior"></span>**BEHAVIOR** (45)
</dt> <dt>

<span id="VULNERABILTIY"></span><span id="vulnerabiltiy"></span>**VULNERABILTIY** (46)
</dt> <dt>

<span id="POLICY_"></span><span id="policy_"></span>**POLICY** (47)
</dt> </dl>

</dd> <dt>

**SeverityID**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Severity ID - Enumeration

<dl> <dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>**Unknown** (0)
</dt> <dt>

<span id="Low"></span><span id="low"></span><span id="LOW"></span>**Low** (1)
</dt> <dt>

<span id="Moderate"></span><span id="moderate"></span><span id="MODERATE"></span>**Moderate** (2)
</dt> <dt>

<span id="High"></span><span id="high"></span><span id="HIGH"></span>**High** (3)
</dt> <dt>

<span id="Severe"></span><span id="severe"></span><span id="SEVERE"></span>**Severe** (4)
</dt> </dl>

</dd> <dt>

**ThreatID**
</dt> <dd> <dl> <dt>

Data type: **sint64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**
</dt> </dl>

Unique Detection ID

</dd> <dt>

**ThreatName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The name of the threat

</dd> <dt>

**TypeID**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Type ID - Enumeration

<dl> <dt>

<span id="Known_Bad"></span><span id="known_bad"></span><span id="KNOWN_BAD"></span>**Known Bad** (0)
</dt> <dt>

<span id="Behavior"></span><span id="behavior"></span><span id="BEHAVIOR"></span>**Behavior** (1)
</dt> <dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>**Unknown** (2)
</dt> <dt>

<span id="Known_Good"></span><span id="known_good"></span><span id="KNOWN_GOOD"></span>**Known Good** (3)
</dt> <dt>

<span id="NRI"></span><span id="nri"></span>**NRI** (4)
</dt> </dl>

</dd> </dl>

## Requirements



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1 \[desktop apps only\]<br/>                                                        |
| Minimum supported server<br/> | Windows Server 2012 R2 \[desktop apps only\]<br/>                                             |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Defender<br/>                                                       |
| MOF<br/>                      | <dl> <dt>ProtectionManagement.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>ProtectionManagement.dll</dt> </dl> |



 

 





