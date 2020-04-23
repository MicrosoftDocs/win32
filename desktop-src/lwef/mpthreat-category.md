---
title: MPTHREAT_CATEGORY enumeration (MpClient.h)
description: Possible threat categories.
ms.assetid: 478ED59E-5D3C-43B3-A89D-44A649EDD086
keywords:
- MPTHREAT_CATEGORY enumeration Legacy Windows Environment Features
- PMPTHREAT_CATEGORY enumeration pointer Legacy Windows Environment Features
topic_type:
- apiref
api_name:
- MPTHREAT_CATEGORY
api_location:
- MpClient.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# MPTHREAT\_CATEGORY enumeration

Possible threat categories.

## Syntax

```C++
typedef enum tagMPTHREAT_CATEGORY {
  MP_THREAT_CATEGORY_INVALID                    = 0,
  MP_THREAT_CATEGORY_ADWARE                     = 1,
  MP_THREAT_CATEGORY_SPYWARE                    = 2,
  MP_THREAT_CATEGORY_PASSWORDSTEALER            = 3,
  MP_THREAT_CATEGORY_TROJANDOWNLOADER           = 4,
  MP_THREAT_CATEGORY_WORM                       = 5,
  MP_THREAT_CATEGORY_BACKDOOR                   = 6,
  MP_THREAT_CATEGORY_REMOTEACCESSTROJAN         = 7,
  MP_THREAT_CATEGORY_TROJAN                     = 8,
  MP_THREAT_CATEGORY_EMAILFLOODER               = 9,
  MP_THREAT_CATEGORY_KEYLOGGER                  = 10,
  MP_THREAT_CATEGORY_DIALER                     = 11,
  MP_THREAT_CATEGORY_MONITORINGSOFTWARE         = 12,
  MP_THREAT_CATEGORY_BROWSERMODIFIER            = 13,
  MP_THREAT_CATEGORY_COOKIE                     = 14,
  MP_THREAT_CATEGORY_BROWSERPLUGIN              = 15,
  MP_THREAT_CATEGORY_AOLEXPLOIT                 = 16,
  MP_THREAT_CATEGORY_NUKER                      = 17,
  MP_THREAT_CATEGORY_SECURITYDISABLER           = 18,
  MP_THREAT_CATEGORY_JOKEPROGRAM                = 19,
  MP_THREAT_CATEGORY_HOSTILEACTIVEXCONTROL      = 20,
  MP_THREAT_CATEGORY_SOFTWAREBUNDLER            = 21,
  MP_THREAT_CATEGORY_STEALTHNOTIFIER            = 22,
  MP_THREAT_CATEGORY_SETTINGSMODIFIER           = 23,
  MP_THREAT_CATEGORY_TOOLBAR                    = 24,
  MP_THREAT_CATEGORY_REMOTECONTROLSOFTWARE      = 25,
  MP_THREAT_CATEGORY_TROJANFTP                  = 26,
  MP_THREAT_CATEGORY_POTENTIALUNWANTEDSOFTWARE  = 27,
  MP_THREAT_CATEGORY_ICQEXPLOIT                 = 28,
  MP_THREAT_CATEGORY_TROJANTELNET               = 29,
  MP_THREAT_CATEGORY_EXPLOIT                    = 30,
  MP_THREAT_CATEGORY_FILESHARINGPROGRAM         = 31,
  MP_THREAT_CATEGORY_MALWARE_CREATION_TOOL      = 32,
  MP_THREAT_CATEGORY_REMOTE_CONTROL_SOFTWARE    = 33,
  MP_THREAT_CATEGORY_TOOL                       = 34,
  MP_THREAT_CATEGORY_TROJAN_DENIALOFSERVICE     = 36,
  MP_THREAT_CATEGORY_TROJAN_DROPPER             = 37,
  MP_THREAT_CATEGORY_TROJAN_MASSMAILER          = 38,
  MP_THREAT_CATEGORY_TROJAN_MONITORINGSOFTWARE  = 39,
  MP_THREAT_CATEGORY_TROJAN_PROXYSERVER         = 40,
  MP_THREAT_CATEGORY_VIRUS                      = 42,
  MP_THREAT_CATEGORY_KNOWN                      = 43,
  MP_THREAT_CATEGORY_UNKNOWN                    = 44,
  MP_THREAT_CATEGORY_SPP                        = 45,
  MP_THREAT_CATEGORY_BEHAVIOR                   = 46,
  MP_THREAT_CATEGORY_VULNERABILTIY              = 47,
  MP_THREAT_CATEGORY_POLICY                     = 48
} MPTHREAT_CATEGORY, *PMPTHREAT_CATEGORY;
```

## Constants

Threat category | Description
-|-
<span id="MP_THREAT_CATEGORY_INVALID"></span><span id="mp_threat_category_invalid"></span> **MP\_THREAT\_CATEGORY\_INVALID** | The threat category doesn't exist, or has been misspelled.
<span id="MP_THREAT_CATEGORY_ADWARE"></span><span id="mp_threat_category_adware"></span> **MP\_THREAT\_CATEGORY\_ADWARE** |
<span id="MP_THREAT_CATEGORY_SPYWARE"></span><span id="mp_threat_category_spyware"></span> **MP\_THREAT\_CATEGORY\_SPYWARE** |
<span id="MP_THREAT_CATEGORY_PASSWORDSTEALER"></span><span id="mp_threat_category_passwordstealer"></span> **MP\_THREAT\_CATEGORY\_PASSWORDSTEALER** |
<span id="MP_THREAT_CATEGORY_TROJANDOWNLOADER"></span><span id="mp_threat_category_trojandownloader"></span>**MP\_THREAT\_CATEGORY\_TROJANDOWNLOADER** |
<span id="MP_THREAT_CATEGORY_WORM"></span><span id="mp_threat_category_worm"></span> **MP\_THREAT\_CATEGORY\_WORM** |
<span id="MP_THREAT_CATEGORY_BACKDOOR"></span><span id="mp_threat_category_backdoor"></span>**MP\_THREAT\_CATEGORY\_BACKDOOR** |
<span id="MP_THREAT_CATEGORY_REMOTEACCESSTROJAN"></span><span id="mp_threat_category_remoteaccesstrojan"></span> **MP\_THREAT\_CATEGORY\_REMOTEACCESSTROJAN** |
<span id="MP_THREAT_CATEGORY_TROJAN"></span><span id="mp_threat_category_trojan"></span>**MP\_THREAT\_CATEGORY\_TROJAN** |
<span id="MP_THREAT_CATEGORY_EMAILFLOODER"></span><span id="mp_threat_category_emailflooder"></span> **MP\_THREAT\_CATEGORY\_EMAILFLOODER** |
<span id="MP_THREAT_CATEGORY_KEYLOGGER"></span><span id="mp_threat_category_keylogger"></span> **MP\_THREAT\_CATEGORY\_KEYLOGGER** |
<span id="MP_THREAT_CATEGORY_DIALER"></span><span id="mp_threat_category_dialer"></span> **MP\_THREAT\_CATEGORY\_DIALER** |
<span id="MP_THREAT_CATEGORY_MONITORINGSOFTWARE"></span><span id="mp_threat_category_monitoringsoftware"></span> **MP\_THREAT\_CATEGORY\_MONITORINGSOFTWARE** |
<span id="MP_THREAT_CATEGORY_BROWSERMODIFIER"></span><span id="mp_threat_category_browsermodifier"></span> **MP\_THREAT\_CATEGORY\_BROWSERMODIFIER** |
<span id="MP_THREAT_CATEGORY_COOKIE"></span><span id="mp_threat_category_cookie"></span> **MP\_THREAT\_CATEGORY\_COOKIE** |
<span id="MP_THREAT_CATEGORY_BROWSERPLUGIN"></span><span id="mp_threat_category_browserplugin"></span> **MP\_THREAT\_CATEGORY\_BROWSERPLUGIN** |
<span id="MP_THREAT_CATEGORY_AOLEXPLOIT"></span><span id="mp_threat_category_aolexploit"></span> **MP\_THREAT\_CATEGORY\_AOLEXPLOIT** |
<span id="MP_THREAT_CATEGORY_NUKER"></span><span id="mp_threat_category_nuker"></span> **MP\_THREAT\_CATEGORY\_NUKER** |
<span id="MP_THREAT_CATEGORY_SECURITYDISABLER"></span><span id="mp_threat_category_securitydisabler"></span> **MP\_THREAT\_CATEGORY\_SECURITYDISABLER** |
<span id="MP_THREAT_CATEGORY_JOKEPROGRAM"></span><span id="mp_threat_category_jokeprogram"></span> **MP\_THREAT\_CATEGORY\_JOKEPROGRAM** |
<span id="MP_THREAT_CATEGORY_HOSTILEACTIVEXCONTROL"></span><span id="mp_threat_category_hostileactivexcontrol"></span> **MP\_THREAT\_CATEGORY\_HOSTILEACTIVEXCONTROL** |
<span id="MP_THREAT_CATEGORY_SOFTWAREBUNDLER"></span><span id="mp_threat_category_softwarebundler"></span> **MP\_THREAT\_CATEGORY\_SOFTWAREBUNDLER** |
<span id="MP_THREAT_CATEGORY_STEALTHNOTIFIER"></span><span id="mp_threat_category_stealthnotifier"></span> **MP\_THREAT\_CATEGORY\_STEALTHNOTIFIER** |
<span id="MP_THREAT_CATEGORY_SETTINGSMODIFIER"></span><span id="mp_threat_category_settingsmodifier"></span> **MP\_THREAT\_CATEGORY\_SETTINGSMODIFIER** |
<span id="MP_THREAT_CATEGORY_TOOLBAR"></span><span id="mp_threat_category_toolbar"></span> **MP\_THREAT\_CATEGORY\_TOOLBAR** |
<span id="MP_THREAT_CATEGORY_REMOTECONTROLSOFTWARE"></span><span id="mp_threat_category_remotecontrolsoftware"></span> **MP\_THREAT\_CATEGORY\_REMOTECONTROLSOFTWARE** |
<span id="MP_THREAT_CATEGORY_TROJANFTP"></span><span id="mp_threat_category_trojanftp"></span> **MP\_THREAT\_CATEGORY\_TROJANFTP** |
<span id="MP_THREAT_CATEGORY_POTENTIALUNWANTEDSOFTWARE"></span><span id="mp_threat_category_potentialunwantedsoftware"></span> **MP\_THREAT\_CATEGORY\_POTENTIALUNWANTEDSOFTWARE** |
<span id="MP_THREAT_CATEGORY_ICQEXPLOIT"></span><span id="mp_threat_category_icqexploit"></span> **MP\_THREAT\_CATEGORY\_ICQEXPLOIT** |
<span id="MP_THREAT_CATEGORY_TROJANTELNET"></span><span id="mp_threat_category_trojantelnet"></span> **MP\_THREAT\_CATEGORY\_TROJANTELNET** |
<span id="MP_THREAT_CATEGORY_EXPLOIT"></span><span id="mp_threat_category_exploit"></span> **MP\_THREAT\_CATEGORY\_EXPLOIT** |
<span id="MP_THREAT_CATEGORY_FILESHARINGPROGRAM"></span><span id="mp_threat_category_filesharingprogram"></span> **MP\_THREAT\_CATEGORY\_FILESHARINGPROGRAM** |
<span id="MP_THREAT_CATEGORY_MALWARE_CREATION_TOOL"></span><span id="mp_threat_category_malware_creation_tool"></span> **MP\_THREAT\_CATEGORY\_MALWARE\_CREATION\_TOOL** |
<span id="MP_THREAT_CATEGORY_REMOTE_CONTROL_SOFTWARE"></span><span id="mp_threat_category_remote_control_software"></span> **MP\_THREAT\_CATEGORY\_REMOTE\_CONTROL\_SOFTWARE** |
<span id="MP_THREAT_CATEGORY_TOOL"></span><span id="mp_threat_category_tool"></span> **MP\_THREAT\_CATEGORY\_TOOL** |
<span id="MP_THREAT_CATEGORY_TROJAN_DENIALOFSERVICE"></span><span id="mp_threat_category_trojan_denialofservice"></span> **MP\_THREAT\_CATEGORY\_TROJAN\_DENIALOFSERVICE** |
<span id="MP_THREAT_CATEGORY_TROJAN_DROPPER"></span><span id="mp_threat_category_trojan_dropper"></span> **MP\_THREAT\_CATEGORY\_TROJAN\_DROPPER** |
<span id="MP_THREAT_CATEGORY_TROJAN_MASSMAILER"></span><span id="mp_threat_category_trojan_massmailer"></span> **MP\_THREAT\_CATEGORY\_TROJAN\_MASSMAILER** |
<span id="MP_THREAT_CATEGORY_TROJAN_MONITORINGSOFTWARE"></span><span id="mp_threat_category_trojan_monitoringsoftware"></span> **MP\_THREAT\_CATEGORY\_TROJAN\_MONITORINGSOFTWARE** |
<span id="MP_THREAT_CATEGORY_TROJAN_PROXYSERVER"></span><span id="mp_threat_category_trojan_proxyserver"></span> **MP\_THREAT\_CATEGORY\_TROJAN\_PROXYSERVER** |
<span id="MP_THREAT_CATEGORY_VIRUS"></span><span id="mp_threat_category_virus"></span> **MP\_THREAT\_CATEGORY\_VIRUS** |
<span id="MP_THREAT_CATEGORY_KNOWN"></span><span id="mp_threat_category_known"></span> **MP\_THREAT\_CATEGORY\_KNOWN** |
<span id="MP_THREAT_CATEGORY_UNKNOWN"></span><span id="mp_threat_category_unknown"></span> **MP\_THREAT\_CATEGORY\_UNKNOWN** |
<span id="MP_THREAT_CATEGORY_SPP"></span><span id="mp_threat_category_spp"></span> **MP\_THREAT\_CATEGORY\_SPP** |
<span id="MP_THREAT_CATEGORY_BEHAVIOR"></span><span id="mp_threat_category_behavior"></span> **MP\_THREAT\_CATEGORY\_BEHAVIOR** |
<span id="MP_THREAT_CATEGORY_VULNERABILTIY"></span><span id="mp_threat_category_vulnerabiltiy"></span> **MP\_THREAT\_CATEGORY\_VULNERABILTIY** | An NIS category.
<span id="MP_THREAT_CATEGORY_POLICY"></span><span id="mp_threat_category_policy"></span> **MP\_THREAT\_CATEGORY\_POLICY** | An NIS category.

## Requirements

| | |
|-|-|
| Minimum supported client | Windows 8 (desktop apps only) |
| Minimum supported server | Windows Server 2012 (desktop apps only) |
| Header | <dl> <dt>MpClient.h</dt> </dl> |
