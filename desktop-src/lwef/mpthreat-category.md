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
<span id="MP_THREAT_CATEGORY_ADWARE"></span><span id="mp_threat_category_adware"></span> **MP\_THREAT\_CATEGORY\_ADWARE** | A potentially unwanted application that displays advertisements.
<span id="MP_THREAT_CATEGORY_SPYWARE"></span><span id="mp_threat_category_spyware"></span> **MP\_THREAT\_CATEGORY\_SPYWARE** | Malware that transmits information about the device or user, without the user's consent or knowledge.
<span id="MP_THREAT_CATEGORY_PASSWORDSTEALER"></span><span id="mp_threat_category_passwordstealer"></span> **MP\_THREAT\_CATEGORY\_PASSWORDSTEALER** | An application that collects and/or transmits a password to an attacker.
<span id="MP_THREAT_CATEGORY_TROJANDOWNLOADER"></span><span id="mp_threat_category_trojandownloader"></span>**MP\_THREAT\_CATEGORY\_TROJANDOWNLOADER** | A trojan that downloads malware or potentially unwanted applications to an infected device.
<span id="MP_THREAT_CATEGORY_WORM"></span><span id="mp_threat_category_worm"></span> **MP\_THREAT\_CATEGORY\_WORM** | Self-propagating malicious software that can automatically distribute itself through network connections.
<span id="MP_THREAT_CATEGORY_BACKDOOR"></span><span id="mp_threat_category_backdoor"></span>**MP\_THREAT\_CATEGORY\_BACKDOOR** | Malware that provides a means of bypassing normal security and authentication protocols on a device.
<span id="MP_THREAT_CATEGORY_REMOTEACCESSTROJAN"></span><span id="mp_threat_category_remoteaccesstrojan"></span> **MP\_THREAT\_CATEGORY\_REMOTEACCESSTROJAN** | A trojan that provides remote access to a computer.
<span id="MP_THREAT_CATEGORY_TROJAN"></span><span id="mp_threat_category_trojan"></span>**MP\_THREAT\_CATEGORY\_TROJAN** | Malicious software that disguises itself as legitimate software.
<span id="MP_THREAT_CATEGORY_EMAILFLOODER"></span><span id="mp_threat_category_emailflooder"></span> **MP\_THREAT\_CATEGORY\_EMAILFLOODER** | Malware the sends a large volume of email to a target.
<span id="MP_THREAT_CATEGORY_KEYLOGGER"></span><span id="mp_threat_category_keylogger"></span> **MP\_THREAT\_CATEGORY\_KEYLOGGER** | Malware that records the user's keystrokes, potentially stealing passwords and other sensitive data.
<span id="MP_THREAT_CATEGORY_DIALER"></span><span id="mp_threat_category_dialer"></span> **MP\_THREAT\_CATEGORY\_DIALER** | Malware that makes unauthorized phone calls, often at premium rates.
<span id="MP_THREAT_CATEGORY_MONITORINGSOFTWARE"></span><span id="mp_threat_category_monitoringsoftware"></span> **MP\_THREAT\_CATEGORY\_MONITORINGSOFTWARE** | A potentially unwanted application that monitors user activity, such as what the user types on their keyboard or views on their screen.
<span id="MP_THREAT_CATEGORY_BROWSERMODIFIER"></span><span id="mp_threat_category_browsermodifier"></span> **MP\_THREAT\_CATEGORY\_BROWSERMODIFIER** | A potentially unwanted application that changes web browser settings without the user's consent.
<span id="MP_THREAT_CATEGORY_COOKIE"></span><span id="mp_threat_category_cookie"></span> **MP\_THREAT\_CATEGORY\_COOKIE** | Data that a Web server sends to a browser, allowing it to save information about the user, such as web application settings, on repeated visits.
<span id="MP_THREAT_CATEGORY_BROWSERPLUGIN"></span><span id="mp_threat_category_browserplugin"></span> **MP\_THREAT\_CATEGORY\_BROWSERPLUGIN** | Software that lets a standard web browser display and run specific types of content, such as media files, animated images, and interactive forms.
<span id="MP_THREAT_CATEGORY_AOLEXPLOIT"></span><span id="mp_threat_category_aolexploit"></span> **MP\_THREAT\_CATEGORY\_AOLEXPLOIT** | Malware that attacks users of the AOL Internet service, often by retrieving passwords or modifying settings.
<span id="MP_THREAT_CATEGORY_NUKER"></span><span id="mp_threat_category_nuker"></span> **MP\_THREAT\_CATEGORY\_NUKER** | Malware designed to crash a device or make it less stable.
<span id="MP_THREAT_CATEGORY_SECURITYDISABLER"></span><span id="mp_threat_category_securitydisabler"></span> **MP\_THREAT\_CATEGORY\_SECURITYDISABLER** | Malware that disables security settings or products.
<span id="MP_THREAT_CATEGORY_JOKEPROGRAM"></span><span id="mp_threat_category_jokeprogram"></span> **MP\_THREAT\_CATEGORY\_JOKEPROGRAM** | An application designed to amuse or scare a user, without actually harming the device.
<span id="MP_THREAT_CATEGORY_HOSTILEACTIVEXCONTROL"></span><span id="mp_threat_category_hostileactivexcontrol"></span> **MP\_THREAT\_CATEGORY\_HOSTILEACTIVEXCONTROL** | An ActiveX control designed by an attacker to harm a device. An ActiveX control is a kind of browser add-on specific to Internet Explorer.
<span id="MP_THREAT_CATEGORY_SOFTWAREBUNDLER"></span><span id="mp_threat_category_softwarebundler"></span> **MP\_THREAT\_CATEGORY\_SOFTWAREBUNDLER** | Software that installs other potentially unwanted applications, such as adware or spyware. The license agreement of the bundling software may require these other components in order to function.
<span id="MP_THREAT_CATEGORY_STEALTHNOTIFIER"></span><span id="mp_threat_category_stealthnotifier"></span> **MP\_THREAT\_CATEGORY\_STEALTHNOTIFIER** | Malware that connects to a remote server through a stealth connection to notify an attacker that the malware has been installed.
<span id="MP_THREAT_CATEGORY_SETTINGSMODIFIER"></span><span id="mp_threat_category_settingsmodifier"></span> **MP\_THREAT\_CATEGORY\_SETTINGSMODIFIER** | A potentially unwanted application that changes a user's settings without the user's knowledge or consent.
<span id="MP_THREAT_CATEGORY_TOOLBAR"></span><span id="mp_threat_category_toolbar"></span> **MP\_THREAT\_CATEGORY\_TOOLBAR** | A potentially unwanted application (PUA) that installs a toolbar on the user's web browser; often bundled with additional PUA, such as adware.
<span id="MP_THREAT_CATEGORY_REMOTECONTROLSOFTWARE"></span><span id="mp_threat_category_remotecontrolsoftware"></span> **MP\_THREAT\_CATEGORY\_REMOTECONTROLSOFTWARE** | A potentially unwanted application that provides remote access to a device.
<span id="MP_THREAT_CATEGORY_TROJANFTP"></span><span id="mp_threat_category_trojanftp"></span> **MP\_THREAT\_CATEGORY\_TROJANFTP** | A trojan that uses an FTP server to allow an attacker to upload or download files from a device.
<span id="MP_THREAT_CATEGORY_POTENTIALUNWANTEDSOFTWARE"></span><span id="mp_threat_category_potentialunwantedsoftware"></span> **MP\_THREAT\_CATEGORY\_POTENTIALUNWANTEDSOFTWARE** | Also known as *potentially unwanted application* or *PUA*; software that may behave in an overly intrusive way, which the user may not have expected or fully consented to.
<span id="MP_THREAT_CATEGORY_ICQEXPLOIT"></span><span id="mp_threat_category_icqexploit"></span> **MP\_THREAT\_CATEGORY\_ICQEXPLOIT** | A trojan that attacks the ICQ messaging service, often by retrieving passwords or tampering with settings.
<span id="MP_THREAT_CATEGORY_TROJANTELNET"></span><span id="mp_threat_category_trojantelnet"></span> **MP\_THREAT\_CATEGORY\_TROJANTELNET** | A trojan that installs a telnet server on a user's computer without the user's knowledge or consent.
<span id="MP_THREAT_CATEGORY_EXPLOIT"></span><span id="mp_threat_category_exploit"></span> **MP\_THREAT\_CATEGORY\_EXPLOIT** | Malicious code that takes advantage of a vulnerability on a device or system.
<span id="MP_THREAT_CATEGORY_FILESHARINGPROGRAM"></span><span id="mp_threat_category_filesharingprogram"></span> **MP\_THREAT\_CATEGORY\_FILESHARINGPROGRAM** | A potentially unwanted application that opens a device to peer-to-peer sharing of the device's files.
<span id="MP_THREAT_CATEGORY_MALWARE_CREATION_TOOL"></span><span id="mp_threat_category_malware_creation_tool"></span> **MP\_THREAT\_CATEGORY\_MALWARE\_CREATION\_TOOL** | An application that can automatically generate malicious files.
<span id="MP_THREAT_CATEGORY_REMOTE_CONTROL_SOFTWARE"></span><span id="mp_threat_category_remote_control_software"></span> **MP\_THREAT\_CATEGORY\_REMOTE\_CONTROL\_SOFTWARE** | A potentially unwanted application that allows for remote access to a device.
<span id="MP_THREAT_CATEGORY_TOOL"></span><span id="mp_threat_category_tool"></span> **MP\_THREAT\_CATEGORY\_TOOL** | A utility that helps an attacker perform malicious actions on a device.
<span id="MP_THREAT_CATEGORY_TROJAN_DENIALOFSERVICE"></span><span id="mp_threat_category_trojan_denialofservice"></span> **MP\_THREAT\_CATEGORY\_TROJAN\_DENIALOFSERVICE** | A trojan that is designed to send a large volume of network requests to a target as part of a denial of service (DoS) attack.
<span id="MP_THREAT_CATEGORY_TROJAN_DROPPER"></span><span id="mp_threat_category_trojan_dropper"></span> **MP\_THREAT\_CATEGORY\_TROJAN\_DROPPER** | A trojan that downloads and installs malware or potentially unwanted applications on a target.
<span id="MP_THREAT_CATEGORY_TROJAN_MASSMAILER"></span><span id="mp_threat_category_trojan_massmailer"></span> **MP\_THREAT\_CATEGORY\_TROJAN\_MASSMAILER** | A trojan that sends a large volume of email to a target, intended to overwhelm the target's inbox.
<span id="MP_THREAT_CATEGORY_TROJAN_MONITORINGSOFTWARE"></span><span id="mp_threat_category_trojan_monitoringsoftware"></span> **MP\_THREAT\_CATEGORY\_TROJAN\_MONITORINGSOFTWARE** | A trojan that monitors user activity, such as what the user types on their keyboard or views on their screen.
<span id="MP_THREAT_CATEGORY_TROJAN_PROXYSERVER"></span><span id="mp_threat_category_trojan_proxyserver"></span> **MP\_THREAT\_CATEGORY\_TROJAN\_PROXYSERVER** | A proxy server installed by a trojan, providing what appears to be an uninterrupted Internet connection while allowing unauthorized access to the infected device.
<span id="MP_THREAT_CATEGORY_VIRUS"></span><span id="mp_threat_category_virus"></span> **MP\_THREAT\_CATEGORY\_VIRUS** | Malware that replicates, commonly by infecting other files in the system, thus allowing the execution of the malware code and its propagation when those files are activated.
<span id="MP_THREAT_CATEGORY_KNOWN"></span><span id="mp_threat_category_known"></span> **MP\_THREAT\_CATEGORY\_KNOWN** | An unspecified malware threat.
<span id="MP_THREAT_CATEGORY_UNKNOWN"></span><span id="mp_threat_category_unknown"></span> **MP\_THREAT\_CATEGORY\_UNKNOWN** | An unspecified malware threat that has not yet been defined.
<span id="MP_THREAT_CATEGORY_SPP"></span><span id="mp_threat_category_spp"></span> **MP\_THREAT\_CATEGORY\_SPP** | Anti-piracy technology that requires each installation of a Windows product be activated with Microsoft.
<span id="MP_THREAT_CATEGORY_BEHAVIOR"></span><span id="mp_threat_category_behavior"></span> **MP\_THREAT\_CATEGORY\_BEHAVIOR** | A type of detection based on file actions that are often associated with malicious activity.
<span id="MP_THREAT_CATEGORY_VULNERABILTIY"></span><span id="mp_threat_category_vulnerabiltiy"></span> **MP\_THREAT\_CATEGORY\_VULNERABILTIY** | Any weakness, administrative process, or activity that makes a device susceptible to exploit by a threat.
<span id="MP_THREAT_CATEGORY_POLICY"></span><span id="mp_threat_category_policy"></span> **MP\_THREAT\_CATEGORY\_POLICY** | A set of rules defined by an administrator, that control features on desktop and mobile devices such as software updates.

## Requirements

| Requirement | Value |
|-|-|
| Minimum supported client | Windows 8 (desktop apps only) |
| Minimum supported server | Windows Server 2012 (desktop apps only) |
| Header | MpClient.h |
