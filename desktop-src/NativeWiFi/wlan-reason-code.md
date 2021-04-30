---
description: Indicates the reason a WLAN operation has failed.
ms.assetid: 7b267f0b-b3f7-4729-bab4-de3bdd0a35a2
title: WLAN_REASON_CODE (Wlanapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# WLAN\_REASON\_CODE

The **WLAN\_REASON\_CODE** type indicates the reason a WLAN operation has failed.

You can use the [**WlanReasonCodeToString**](/windows/desktop/api/wlanapi/nf-wlanapi-wlanreasoncodetostring) function to map a numeric reason code (for example, 0x00050007) to its text meaning. You can also use the lookup table to help interpret the numeric value of the reason code. To view the lookup table, see Appendix E: Mapping of reason codes to event messages in the document [Troubleshooting Windows Vista 802.11 Wireless Connections](/previous-versions/windows/it-pro/windows-vista/cc766215(v=ws.10)).


```C++
typedef DWORD WLAN_REASON_CODE, *PWLAN_REASON_CODE;
```



The following table lists general error codes.



| Reason code                 | Meaning                            |
|-----------------------------|------------------------------------|
| WLAN\_REASON\_CODE\_SUCCESS | The operation succeeds.            |
| WLAN\_REASON\_CODE\_UNKNOWN | The reason for failure is unknown. |



 

The following table lists automatic configuration error codes.



| Reason Code                                  | Meaning                                         |
|----------------------------------------------|-------------------------------------------------|
| WLAN\_REASON\_CODE\_NETWORK\_NOT\_COMPATIBLE | The wireless network is not compatible.         |
| WLAN\_REASON\_CODE\_PROFILE\_NOT\_COMPATIBLE | The wireless network profile is not compatible. |



 

The following table lists automatic connection error codes.



| Reason Code                                                | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| WLAN\_REASON\_CODE\_NO\_AUTO\_CONNECTION                   | The profile specifies no auto connection.                                                                                                                                                                                                                                                                                                                                                                                                               |
| WLAN\_REASON\_CODE\_NOT\_VISIBLE                           | The wireless network is not visible.                                                                                                                                                                                                                                                                                                                                                                                                                    |
| WLAN\_REASON\_CODE\_GP\_DENIED                             | The wireless network is blocked by group policy.                                                                                                                                                                                                                                                                                                                                                                                                        |
| WLAN\_REASON\_CODE\_USER\_DENIED                           | The wireless network is blocked by the user.                                                                                                                                                                                                                                                                                                                                                                                                            |
| WLAN\_REASON\_CODE\_BSS\_TYPE\_NOT\_ALLOWED                | The basic service set (BSS) type is not allowed on this wireless adapter.                                                                                                                                                                                                                                                                                                                                                                               |
| WLAN\_REASON\_CODE\_IN\_FAILED\_LIST                       | The wireless network is in the failed list.                                                                                                                                                                                                                                                                                                                                                                                                             |
| WLAN\_REASON\_CODE\_IN\_BLOCKED\_LIST                      | The wireless network is in the blocked list.                                                                                                                                                                                                                                                                                                                                                                                                            |
| WLAN\_REASON\_CODE\_SSID\_LIST\_TOO\_LONG                  | The size of the service set identifiers (SSID) list exceeds the maximum size supported by the adapter.                                                                                                                                                                                                                                                                                                                                                  |
| WLAN\_REASON\_CODE\_CONNECT\_CALL\_FAIL                    | The Media Specific Module (MSM) connect call fails.                                                                                                                                                                                                                                                                                                                                                                                                     |
| WLAN\_REASON\_CODE\_SCAN\_CALL\_FAIL                       | The MSM scan call fails.                                                                                                                                                                                                                                                                                                                                                                                                                                |
| WLAN\_REASON\_CODE\_NETWORK\_NOT\_AVAILABLE                | The specified network is not available.This reason code is also used when there is a mismatch between capabilities specified in an XML profile and interface and/or network capabilities. For example, if a profile specifies the use of WPA2 when the NIC only supports WPA, then this error code is returned. Also, if a profile specifies the use of FIPS mode when the NIC does not support FIPS mode, then this error code is returned.<br/> |
| WLAN\_REASON\_CODE\_PROFILE\_CHANGED\_OR\_DELETED          | The profile was changed or deleted before the connection was established.                                                                                                                                                                                                                                                                                                                                                                               |
| WLAN\_REASON\_CODE\_KEY\_MISMATCH                          | The profile key does not match the network key.                                                                                                                                                                                                                                                                                                                                                                                                         |
| WLAN\_REASON\_CODE\_USER\_NOT\_RESPOND                     | The user is not responding.                                                                                                                                                                                                                                                                                                                                                                                                                             |
| WLAN\_REASON\_CODE\_AP\_PROFILE\_NOT\_ALLOWED\_FOR\_CLIENT | An application tried to apply a wireless Hosted Network profile to a physical wireless network adapter using the [**WlanSetProfile**](/windows/desktop/api/wlanapi/nf-wlanapi-wlansetprofile) function, rather than to a virtual device.                                                                                                                                                                                                                                                    |
| WLAN\_REASON\_CODE\_AP\_PROFILE\_NOT\_ALLOWED              | An application tried to apply a wireless Hosted Network profile to a physical wireless network adapter using the [**WlanSetProfile**](/windows/desktop/api/wlanapi/nf-wlanapi-wlansetprofile) function, rather than to a virtual device.                                                                                                                                                                                                                                                    |



 

The following table lists profile validation error codes.



| Reason Code                                                    | Meaning                                                                                                                                                                                                                                       |
|----------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| WLAN\_REASON\_CODE\_INVALID\_PROFILE\_SCHEMA                   | The profile invalid according to the schema.                                                                                                                                                                                                  |
| WLAN\_REASON\_CODE\_PROFILE\_MISSING                           | The WLANProfile element is missing.                                                                                                                                                                                                           |
| WLAN\_REASON\_CODE\_INVALID\_PROFILE\_NAME                     | The name of the profile is invalid.                                                                                                                                                                                                           |
| WLAN\_REASON\_CODE\_INVALID\_PROFILE\_TYPE                     | The type of the profile is invalid.                                                                                                                                                                                                           |
| WLAN\_REASON\_CODE\_INVALID\_PHY\_TYPE                         | The PHY type is invalid.                                                                                                                                                                                                                      |
| WLAN\_REASON\_CODE\_MSM\_SECURITY\_MISSING                     | The MSM security settings are missing.                                                                                                                                                                                                        |
| WLAN\_REASON\_CODE\_IHV\_SECURITY\_NOT\_SUPPORTED              | The independent hardware vendor (IHV) security settings are missing.                                                                                                                                                                          |
| WLAN\_REASON\_CODE\_IHV\_OUI\_MISMATCH                         | The IHV profile OUI did not match with the adapter OUI.                                                                                                                                                                                       |
| WLAN\_REASON\_CODE\_IHV\_OUI\_MISSING                          | The IHV OUI settings are missing.                                                                                                                                                                                                             |
| WLAN\_REASON\_CODE\_IHV\_SETTINGS\_MISSING                     | The IHV security settings are missing.                                                                                                                                                                                                        |
| WLAN\_REASON\_CODE\_IHV\_CONNECTIVITY\_NOT\_SUPPORTED          | An application tried to apply an IHV profile on an adapter that does not support IHV connectivity settings.                                                                                                                                   |
| WLAN\_REASON\_CODE\_CONFLICT\_SECURITY                         | The security settings conflict.                                                                                                                                                                                                               |
| WLAN\_REASON\_CODE\_SECURITY\_MISSING                          | The security settings are missing.                                                                                                                                                                                                            |
| WLAN\_REASON\_CODE\_INVALID\_BSS\_TYPE                         | The BSS type is not valid.                                                                                                                                                                                                                    |
| WLAN\_REASON\_CODE\_INVALID\_ADHOC\_CONNECTION\_MODE           | Automatic connection cannot be set for an ad hoc network.                                                                                                                                                                                     |
| WLAN\_REASON\_CODE\_NON\_BROADCAST\_SET\_FOR\_ADHOC            | Non-broadcast cannot be set for an ad hoc network.                                                                                                                                                                                            |
| WLAN\_REASON\_CODE\_AUTO\_SWITCH\_SET\_FOR\_ADHOC              | Auto-switch cannot be set for an ad hoc network.                                                                                                                                                                                              |
| WLAN\_REASON\_CODE\_AUTO\_SWITCH\_SET\_FOR\_MANUAL\_CONNECTION | Auto-switch cannot be set for a manual connection profile.                                                                                                                                                                                    |
| WLAN\_REASON\_CODE\_IHV\_SECURITY\_ONEX\_MISSING               | The IHV 802.1X security settings are missing.                                                                                                                                                                                                 |
| WLAN\_REASON\_CODE\_PROFILE\_SSID\_INVALID                     | The SSID in the profile is invalid or missing.                                                                                                                                                                                                |
| WLAN\_REASON\_CODE\_TOO\_MANY\_SSID                            | Too many SSIDs were specified in the profile.                                                                                                                                                                                                 |
| WLAN\_REASON\_CODE\_IHV\_CONNECTIVITY\_NOT\_SUPPORTED          |                                                                                                                                                                                                                                               |
| WLAN\_REASON\_CODE\_BAD\_MAX\_NUMBER\_OF\_CLIENTS\_FOR\_AP     | An application tried to apply a wireless Hosted Network profile to a physical network adapter NIC using the [**WlanSetProfile**](/windows/desktop/api/wlanapi/nf-wlanapi-wlansetprofile) function, and specified an unacceptable value for the maximum number of clients allowed. |
| WLAN\_REASON\_CODE\_INVALID\_CHANNEL                           | The channel specified is invalid.                                                                                                                                                                                                             |
| WLAN\_REASON\_CODE\_OPERATION\_MODE\_NOT\_SUPPORTED            |                                                                                                                                                                                                                                               |
| WLAN\_REASON\_CODE\_AUTO\_AP\_PROFILE\_NOT\_ALLOWED            | An internal operating system error occurred with the wireless Hosted Network.                                                                                                                                                                 |
| WLAN\_REASON\_CODE\_AUTO\_CONNECTION\_NOT\_ALLOWED             |                                                                                                                                                                                                                                               |



 

The following table lists MSM network incompatibility error codes.



| Reason Code                                            | Meaning                                                          |
|--------------------------------------------------------|------------------------------------------------------------------|
| WLAN\_REASON\_CODE\_UNSUPPORTED\_SECURITY\_SET\_BY\_OS | The security settings are not supported by the operating system. |
| WLAN\_REASON\_CODE\_UNSUPPORTED\_SECURITY\_SET         | The security settings are not supported.                         |
| WLAN\_REASON\_CODE\_BSS\_TYPE\_UNMATCH                 | The BSS type does not match.                                     |
| WLAN\_REASON\_CODE\_PHY\_TYPE\_UNMATCH                 | The PHY type does not match.                                     |
| WLAN\_REASON\_CODE\_DATARATE\_UNMATCH                  | The data rate does not match.                                    |



 

The following table lists MSM connection failure error codes.



| Reason Code                                       | Meaning                                                                                                      |
|---------------------------------------------------|--------------------------------------------------------------------------------------------------------------|
| WLAN\_REASON\_CODE\_USER\_CANCELLED               | User has canceled the operation.                                                                             |
| WLAN\_REASON\_CODE\_ASSOCIATION\_FAILURE          | Driver disconnected while associating.                                                                       |
| WLAN\_REASON\_CODE\_ASSOCIATION\_TIMEOUT          | Association timed out.                                                                                       |
| WLAN\_REASON\_CODE\_PRE\_SECURITY\_FAILURE        | Pre-association security failure.                                                                            |
| WLAN\_REASON\_CODE\_START\_SECURITY\_FAILURE      | Failed to start security after association.                                                                  |
| WLAN\_REASON\_CODE\_SECURITY\_FAILURE             | Security ends up with failure.                                                                               |
| WLAN\_REASON\_CODE\_SECURITY\_TIMEOUT             | Security operation times out.                                                                                |
| WLAN\_REASON\_CODE\_ROAMING\_FAILURE              | Driver disconnected while roaming.                                                                           |
| WLAN\_REASON\_CODE\_ROAMING\_SECURITY\_FAILURE    | Failed to start security for roaming.                                                                        |
| WLAN\_REASON\_CODE\_ADHOC\_SECURITY\_FAILURE      | Failed to start security for ad hoc peer.                                                                    |
| WLAN\_REASON\_CODE\_DRIVER\_DISCONNECTED          | Driver disconnected.                                                                                         |
| WLAN\_REASON\_CODE\_DRIVER\_OPERATION\_FAILURE    | Driver failed to perform some operations.                                                                    |
| WLAN\_REASON\_CODE\_IHV\_NOT\_AVAILABLE           | The IHV service is not available.                                                                            |
| WLAN\_REASON\_CODE\_IHV\_NOT\_RESPONDING          | The response from the IHV service timed out.                                                                 |
| WLAN\_REASON\_CODE\_DISCONNECT\_TIMEOUT           | Timed out waiting for the driver to disconnect.                                                              |
| WLAN\_REASON\_CODE\_INTERNAL\_FAILURE             | An internal error prevented the operation from being completed.                                              |
| WLAN\_REASON\_CODE\_UI\_REQUEST\_TIMEOUT          | A user interaction request timed out.                                                                        |
| WLAN\_REASON\_CODE\_TOO\_MANY\_SECURITY\_ATTEMPTS | Roaming too often. Post security was not completed after 5 attempts.                                         |
| WLAN\_REASON\_CODE\_AP\_STARTING\_FAILURE         | An internal operating system error occurred that resulted in a failure to start the wireless Hosted Network. |



 

The following table lists MSM security error codes.



| Reason Code                                                             | Meaning                                                                                                                                                                                   |
|-------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| WLAN\_REASON\_CODE\_MSMSEC\_PROFILE\_INVALID\_KEY\_INDEX                | Key index specified is not valid.                                                                                                                                                         |
| WLAN\_REASON\_CODE\_MSMSEC\_PROFILE\_PSK\_PRESENT                       | Key required, PSK present.                                                                                                                                                                |
| WLAN\_REASON\_CODE\_MSMSEC\_PROFILE\_KEY\_LENGTH                        | Invalid key length.                                                                                                                                                                       |
| WLAN\_REASON\_CODE\_MSMSEC\_PROFILE\_PSK\_LENGTH                        | Invalid PSK length.                                                                                                                                                                       |
| WLAN\_REASON\_CODE\_MSMSEC\_PROFILE\_NO\_AUTH\_CIPHER\_SPECIFIED        | No auth/cipher pairs specified.                                                                                                                                                           |
| WLAN\_REASON\_CODE\_MSMSEC\_PROFILE\_TOO\_MANY\_AUTH\_CIPHER\_SPECIFIED | Too many auth/cipher pairs specified.                                                                                                                                                     |
| WLAN\_REASON\_CODE\_MSMSEC\_PROFILE\_DUPLICATE\_AUTH\_CIPHER            | Profile contains duplicate auth/cipher pair.                                                                                                                                              |
| WLAN\_REASON\_CODE\_MSMSEC\_PROFILE\_RAWDATA\_INVALID                   | Profile raw data is invalid.                                                                                                                                                              |
| WLAN\_REASON\_CODE\_MSMSEC\_PROFILE\_INVALID\_AUTH\_CIPHER              | Invalid auth/cipher combination.                                                                                                                                                          |
| WLAN\_REASON\_CODE\_MSMSEC\_PROFILE\_ONEX\_DISABLED                     | 802.1X disabled when it is required to be enabled.                                                                                                                                        |
| WLAN\_REASON\_CODE\_MSMSEC\_PROFILE\_ONEX\_ENABLED                      | 802.1X enabled when it is required to be disabled.                                                                                                                                        |
| WLAN\_REASON\_CODE\_MSMSEC\_PROFILE\_INVALID\_PMKCACHE\_MODE            | Invalid PMK cache mode.                                                                                                                                                                   |
| WLAN\_REASON\_CODE\_MSMSEC\_PROFILE\_INVALID\_PMKCACHE\_SIZE            | Invalid PMK cache size.                                                                                                                                                                   |
| WLAN\_REASON\_CODE\_MSMSEC\_PROFILE\_INVALID\_PMKCACHE\_TTL             | Invalid PMK cache TTL.                                                                                                                                                                    |
| WLAN\_REASON\_CODE\_MSMSEC\_PROFILE\_INVALID\_PREAUTH\_MODE             | Invalid preauth mode.                                                                                                                                                                     |
| WLAN\_REASON\_CODE\_MSMSEC\_PROFILE\_INVALID\_PREAUTH\_THROTTLE         | Invalid preauth throttle.                                                                                                                                                                 |
| WLAN\_REASON\_CODE\_MSMSEC\_PROFILE\_PREAUTH\_ONLY\_ENABLED             | Preauth enabled when PMK cache is disabled.                                                                                                                                               |
| WLAN\_REASON\_CODE\_MSMSEC\_CAPABILITY\_NETWORK                         | Capability matching failed at network.                                                                                                                                                    |
| WLAN\_REASON\_CODE\_MSMSEC\_CAPABILITY\_NIC                             | Capability matching failed at NIC.                                                                                                                                                        |
| WLAN\_REASON\_CODE\_MSMSEC\_CAPABILITY\_PROFILE                         | Capability matching failed at profile.                                                                                                                                                    |
| WLAN\_REASON\_CODE\_MSMSEC\_CAPABILITY\_DISCOVERY                       | Network does not support specified capability type.                                                                                                                                       |
| WLAN\_REASON\_CODE\_MSMSEC\_PROFILE\_PASSPHRASE\_CHAR                   | Passphrase contains invalid character.                                                                                                                                                    |
| WLAN\_REASON\_CODE\_MSMSEC\_PROFILE\_KEYMATERIAL\_CHAR                  | Key material contains invalid character.                                                                                                                                                  |
| WLAN\_REASON\_CODE\_MSMSEC\_PROFILE\_WRONG\_KEYTYPE                     | The key type specified does not match the key material.                                                                                                                                   |
| WLAN\_REASON\_CODE\_MSMSEC\_MIXED\_CELL                                 | A mixed cell is suspected. The AP is not signaling that it is compatible with a privacy-enabled profile.                                                                                  |
| WLAN\_REASON\_CODE\_MSMSEC\_PROFILE\_AUTH\_TIMERS\_INVALID              | The number of authentication timers or the number of timeouts specified in the profile is invalid.                                                                                        |
| WLAN\_REASON\_CODE\_MSMSEC\_PROFILE\_INVALID\_GKEY\_INTV                | The group key update interval specified in the profile is invalid.                                                                                                                        |
| WLAN\_REASON\_CODE\_MSMSEC\_TRANSITION\_NETWORK                         | A "transition network" is suspected. Legacy 802.11 security is used for the next authentication attempt.                                                                                  |
| WLAN\_REASON\_CODE\_MSMSEC\_PROFILE\_KEY\_UNMAPPED\_CHAR                | The key contains characters that are not in the ASCII character set.                                                                                                                      |
| WLAN\_REASON\_CODE\_MSMSEC\_CAPABILITY\_PROFILE\_AUTH                   | Capability matching failed because the network does not support the authentication method in the profile.                                                                                 |
| WLAN\_REASON\_CODE\_MSMSEC\_CAPABILITY\_PROFILE\_CIPHER                 | Capability matching failed because the network does not support the cipher algorithm in the profile.                                                                                      |
| WLAN\_REASON\_CODE\_MSMSEC\_PROFILE\_SAFE\_MODE                         | FIPS 140-2 mode value in the profile is invalid.                                                                                                                                          |
| WLAN\_REASON\_CODE\_MSMSEC\_CAPABILITY\_PROFILE\_SAFE\_MODE\_NIC        | Profile requires FIPS 140-2 mode, which is not supported by network interface card (NIC).                                                                                                 |
| WLAN\_REASON\_CODE\_MSMSEC\_CAPABILITY\_PROFILE\_SAFE\_MODE\_NW         | Profile requires FIPS 140-2 mode, which is not supported by network.                                                                                                                      |
| WLAN\_REASON\_CODE\_MSMSEC\_PROFILE\_UNSUPPORTED\_AUTH                  | Profile specifies an unsupported authentication ,mechanism.                                                                                                                               |
| WLAN\_REASON\_CODE\_MSMSEC\_PROFILE\_UNSUPPORTED\_CIPHER                | Profile specifies an unsupported cipher.                                                                                                                                                  |
| WLAN\_REASON\_CODE\_MSMSEC\_UI\_REQUEST\_FAILURE                        | Failed to queue the user interface request.                                                                                                                                               |
| WLAN\_REASON\_CODE\_MSMSEC\_CAPABILITY\_MFP\_NW\_NIC                    | The wireless LAN requires Management Frame Protection (MFP) and the network interface does not support MFP. For more information, see the IEEE 802.11w amendment to the 802.11 standard. |



 

The following table lists MSM connection error codes.



| Reason Code                                             | Meaning                                                                                                          |
|---------------------------------------------------------|------------------------------------------------------------------------------------------------------------------|
| WLAN\_REASON\_CODE\_MSMSEC\_AUTH\_START\_TIMEOUT        | 802.1X authentication did not start within configured time.                                                      |
| WLAN\_REASON\_CODE\_MSMSEC\_AUTH\_SUCCESS\_TIMEOUT      | 802.1X authentication did not complete within configured time.                                                   |
| WLAN\_REASON\_CODE\_MSMSEC\_KEY\_START\_TIMEOUT         | Dynamic key exchange did not start within configured time.                                                       |
| WLAN\_REASON\_CODE\_MSMSEC\_KEY\_SUCCESS\_TIMEOUT       | Dynamic key exchange did not complete within configured time.                                                    |
| WLAN\_REASON\_CODE\_MSMSEC\_M3\_MISSING\_KEY\_DATA      | Message 3 of 4-way handshake has no key data.                                                                    |
| WLAN\_REASON\_CODE\_MSMSEC\_M3\_MISSING\_IE             | Message 3 of 4-way handshake has no IE.                                                                          |
| WLAN\_REASON\_CODE\_MSMSEC\_M3\_MISSING\_GRP\_KEY       | Message 3 of 4-way handshake has no GRP key.                                                                     |
| WLAN\_REASON\_CODE\_MSMSEC\_PR\_IE\_MATCHING            | Matching security capabilities of IE in M3 failed.                                                               |
| WLAN\_REASON\_CODE\_MSMSEC\_SEC\_IE\_MATCHING           | Matching security capabilities of secondary IE in M3 failed.                                                     |
| WLAN\_REASON\_CODE\_MSMSEC\_NO\_PAIRWISE\_KEY           | Required a pairwise key but access point (AP) configured only group keys.                                        |
| WLAN\_REASON\_CODE\_MSMSEC\_G1\_MISSING\_KEY\_DATA      | Message 1 of group key handshake has no key data.                                                                |
| WLAN\_REASON\_CODE\_MSMSEC\_G1\_MISSING\_GRP\_KEY       | Message 1 of group key handshake has no group key.                                                               |
| WLAN\_REASON\_CODE\_MSMSEC\_PEER\_INDICATED\_INSECURE   | AP reset secure bit after connection was secured.                                                                |
| WLAN\_REASON\_CODE\_MSMSEC\_NO\_AUTHENTICATOR           | 802.1X indicated that there is no authenticator, but the profile requires one.                                   |
| WLAN\_REASON\_CODE\_MSMSEC\_NIC\_FAILURE                | Plumbing settings to NIC failed.                                                                                 |
| WLAN\_REASON\_CODE\_MSMSEC\_CANCELLED                   | Operation was canceled by a caller.                                                                              |
| WLAN\_REASON\_CODE\_MSMSEC\_KEY\_FORMAT                 | Entered key format is not in a valid format.                                                                     |
| WLAN\_REASON\_CODE\_MSMSEC\_DOWNGRADE\_DETECTED         | A security downgrade was detected.                                                                               |
| WLAN\_REASON\_CODE\_MSMSEC\_PSK\_MISMATCH\_SUSPECTED    | A PSK mismatch is suspected.                                                                                     |
| WLAN\_REASON\_CODE\_MSMSEC\_FORCED\_FAILURE             | There was a forced failure because the connection method was not secure.                                         |
| WLAN\_REASON\_CODE\_MSMSEC\_M3\_TOO\_MANY\_RSNIE        | Message 3 of 4 way handshake contains too many RSN IE (RSN).                                                     |
| WLAN\_REASON\_CODE\_MSMSEC\_M2\_MISSING\_KEY\_DATA      | Message 2 of 4 way handshake has no key data (RSN Adhoc).                                                        |
| WLAN\_REASON\_CODE\_MSMSEC\_M2\_MISSING\_IE             | Message 2 of 4 way handshake has no IE (RSN Adhoc).                                                              |
| WLAN\_REASON\_CODE\_MSMSEC\_AUTH\_WCN\_COMPLETED        |                                                                                                                  |
| WLAN\_REASON\_CODE\_MSMSEC\_SECURITY\_UI\_FAILURE       | The security UI request failed because the request could not be queued or because the user canceled the request. |
| WLAN\_REASON\_CODE\_MSMSEC\_M3\_MISSING\_MGMT\_GRP\_KEY | Message 3 of 4 way handshake has no Mgmt Group Key (RSN).                                                        |
| WLAN\_REASON\_CODE\_MSMSEC\_G1\_MISSING\_MGMT\_GRP\_KEY | Message 1 of group key handshake has no group management key.                                                    |



 

The following table lists 802.1X reason codes. Schema elements named below are defined in the OneX schema and specified in the WLAN profile.



| Reason Code                                         | Meaning                                                                                                                                                                            |
|-----------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ONEX\_UNABLE\_TO\_IDENTIFY\_USER                    | No user is available for 802.1X authentication. This error can occur when machine authentication is disabled and no user is logged on to the machine.                              |
| ONEX\_IDENTITY\_NOT\_FOUND                          | The 802.1X identity could not be found.                                                                                                                                            |
| ONEX\_UI\_DISABLED                                  | Authentication could only be completed through the user interface and this interface could not be displayed.                                                                       |
| ONEX\_EAP\_FAILURE\_RECEIVED                        | The EAP authentication failed.                                                                                                                                                     |
| ONEX\_AUTHENTICATOR\_NO\_LONGER\_PRESENT            | The 802.1X authenticator went away from the network.                                                                                                                               |
| ONEX\_PROFILE\_VERSION\_NOT\_SUPPORTED              | The version of the OneX profile supplied is not supported.                                                                                                                         |
| ONEX\_PROFILE\_INVALID\_LENGTH                      | The OneX profile has an invalid length.                                                                                                                                            |
| ONEX\_PROFILE\_DISALLOWED\_EAP\_TYPE                | The EAP type specified in the OneX profile(possibly supplied by the EAPType element) is not allowed.                                                                               |
| ONEX\_PROFILE\_INVALID\_EAP\_TYPE\_OR\_FLAG         | The EAP Type specified in the OneX profile (possibly supplied by the EAPType element) is invalid, or one of the EAP flags (possibly supplied in the EAPConfig element) is invalid. |
| ONEX\_PROFILE\_INVALID\_ONEX\_FLAGS                 | The supplicant flags (possibly supplied in the EAPConfig element) in the OneX profile are invalid.                                                                                 |
| ONEX\_PROFILE\_INVALID\_TIMER\_VALUE                | A timer specified in the OneX profile (possibly supplied by the heldPeriod, authPeriod, or startPeriod element) is invalid.                                                        |
| ONEX\_PROFILE\_INVALID\_SUPPLICANT\_MODE            | The supplicant mode specified in the OneX profile (possibly supplied by the supplicantMode element) is invalid.                                                                    |
| ONEX\_PROFILE\_INVALID\_AUTH\_MODE                  | The authentication mode specified in the OneX profile (possibly supplied by the authMode element) is invalid.                                                                      |
| ONEX\_PROFILE\_INVALID\_EAP\_CONNECTION\_PROPERTIES | The connection properties specified in the OneX profile (possibly supplied by the EAPConfig element) are invalid.                                                                  |



 

## Remarks

A limited set of reason codes are supported on Windows XP with Service Pack 3 (SP3) and on the Wireless LAN API for Windows XP with Service Pack 2 (SP2). The profile validation error codes supported on Windows XP with SP3 and on the Wireless LAN API for Windows XP with SP2 are as follows:

-   WLAN\_REASON\_CODE\_INVALID\_PROFILE\_SCHEMA
-   WLAN\_REASON\_CODE\_PROFILE\_MISSING
-   WLAN\_REASON\_CODE\_PROFILE\_SSID\_INVALID

The MSM security error codes supported on Windows XP with SP3 and on the Wireless LAN API for Windows XP with SP2 are as follows:

-   WLAN\_REASON\_CODE\_MSMSEC\_PROFILE\_INVALID\_KEY\_INDEX
-   WLAN\_REASON\_CODE\_MSMSEC\_PROFILE\_KEY\_LENGTH
-   WLAN\_REASON\_CODE\_MSMSEC\_PROFILE\_PSK\_LENGTH
-   WLAN\_REASON\_CODE\_MSMSEC\_PROFILE\_INVALID\_AUTH\_CIPHER
-   WLAN\_REASON\_CODE\_MSMSEC\_PROFILE\_ONEX\_DISABLED
-   WLAN\_REASON\_CODE\_MSMSEC\_PROFILE\_ONEX\_ENABLED
-   WLAN\_REASON\_CODE\_MSMSEC\_CAPABILITY\_NETWORK
-   WLAN\_REASON\_CODE\_MSMSEC\_CAPABILITY\_NIC
-   WLAN\_REASON\_CODE\_MSMSEC\_PROFILE\_KEYMATERIAL\_CHAR
-   WLAN\_REASON\_CODE\_MSMSEC\_PROFILE\_WRONG\_KEYTYPE

The 802.1x error codes supported on Windows XP with SP3 and on the Wireless LAN API for Windows XP with SP2 are as follows:

-   ONEX\_PROFILE\_INVALID\_LENGTH
-   ONEX\_PROFILE\_INVALID\_EAP\_TYPE\_OR\_FLAG
-   ONEX\_PROFILE\_INVALID\_AUTH\_MODE
-   ONEX\_PROFILE\_INVALID\_EAP\_CONNECTION\_PROPERTIES

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista, Windows XP with SP3 \[desktop apps only\]<br/>                  |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                 |
| Redistributable<br/>          | Wireless LAN API for Windows XP with SP2<br/>                                  |
| Header<br/>                   | <dl> <dt>Wlanapi.h</dt> </dl> |



## See also

<dl> <dt>

[**WlanReasonCodeToString**](/windows/desktop/api/wlanapi/nf-wlanapi-wlanreasoncodetostring)
</dt> <dt>

[**WlanSetProfile**](/windows/desktop/api/wlanapi/nf-wlanapi-wlansetprofile)
</dt> </dl>

 

 
