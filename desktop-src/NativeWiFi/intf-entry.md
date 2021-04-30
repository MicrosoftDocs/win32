---
description: Contains detailed information about an interface that is required by an RPC client.
ms.assetid: 92e734f3-eacb-44dc-9016-88dc6e9f04b6
title: INTF_ENTRY structure (Wzcsapi.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- INTF_ENTRY
api_type: 
- HeaderDef
api_location: 
- wzcsapi.h
---

# INTF\_ENTRY structure

\[**INTF\_ENTRY** is no longer supported as of Windows Vista and Windows Server 2008. Instead, use the [Native Wifi API](native-wifi-reference.md), which provides similar functionality. For more information, see [About the Native Wifi API](about-the-native-wifi-api.md).\]

Contains detailed information about an interface that is required by an RPC client.

## Syntax


```C++
typedef struct {
  LPWSTR   wszGuid;
  LPWSTR   wszDescr;
  DWORD    dwContext;
  ULONG    ulMediaState;
  ULONG    ulMediaType;
  ULONG    ulPhysicalMediaType;
  INT      nInfraMode;
  INT      nAuthMode;
  INT      nWepStatus;
  DWORD    dwCtlFlags;
  DWORD    dwDynFlags;
  DWORD    dwCapabilities;
  RAW_DATA rdNicCapabilities;
  RAW_DATA rdSSID;
  RAW_DATA rdBSSID;
  RAW_DATA rdBSSIDList;
  RAW_DATA rdStSSIDList;
  RAW_DATA rdCtrlData;
} INTF_ENTRY, *PINTF_ENTRY;
```



## Members

<dl> <dt>

**wszGuid**
</dt> <dd>

A pointer to the interface GUID represented as a Unicode string in the following format: "{xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx}".

</dd> <dt>

**wszDescr**
</dt> <dd>

A pointer to a string that contains the interface description that is retrieved by the Wireless Zero Configuration service (WZCSVC).

</dd> <dt>

**dwContext**
</dt> <dd>

Reserved for internal use.

</dd> <dt>

**ulMediaState**
</dt> <dd>

The current NDIS media connect state for the interface. The following table shows the possible values.



| Value                                                                                                                                                                                                                                                  | Meaning                                |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------|
| <span id="MEDIA_STATE_CONNECTED_"></span><span id="media_state_connected_"></span><dl> <dt>**MEDIA\_STATE\_CONNECTED** </dt> <dt>1</dt> </dl>       | The media is connected.<br/>     |
| <span id="MEDIA_STATE_DISCONNECTED"></span><span id="media_state_disconnected"></span><dl> <dt>**MEDIA\_STATE\_DISCONNECTED**</dt> <dt>0</dt> </dl> | The media is disconnected.<br/>  |
| <span id="MEDIA_STATE_UNKNOWN"></span><span id="media_state_unknown"></span><dl> <dt>**MEDIA\_STATE\_UNKNOWN**</dt> <dt>-1</dt> </dl>               | The media state is unknown.<br/> |



 

</dd> <dt>

**ulMediaType**
</dt> <dd>

The NDIS media types that the NIC currently uses. When queried, the value of this member is **NdisMedium802\_3** as defined in the *Ndispnp.h* header file.

</dd> <dt>

**ulPhysicalMediaType**
</dt> <dd>

The NDIS media type for the interface. When queried, the value of this member is **NdisPhysicalMediumWirelessLan** as defined in the *Ndispnp.h* header file.

</dd> <dt>

**nInfraMode**
</dt> <dd>

The current 802.11 Infrastructure Mode set on the interface.

</dd> <dt>

**nAuthMode**
</dt> <dd>

The current 802.11 Authentication Mode set on the interface.

The following table shows the possible values for the parameter based on the **NDIS\_802\_11\_AUTHENTICATION\_MODE** enumeration defined in the *NtDDNdis.h* header file.



| Value                                                                                                                                                                                                                                                                                                            | Meaning                                                                                                                                                                                                                                                 |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="Ndis802_11AuthModeOpen"></span><span id="ndis802_11authmodeopen"></span><span id="NDIS802_11AUTHMODEOPEN"></span><dl> <dt>**Ndis802\_11AuthModeOpen**</dt> <dt>1</dt> </dl>                         | IEEE 802.11 Open System authentication.<br/>                                                                                                                                                                                                      |
| <span id="Ndis802_11AuthModeShared"></span><span id="ndis802_11authmodeshared"></span><span id="NDIS802_11AUTHMODESHARED"></span><dl> <dt>**Ndis802\_11AuthModeShared**</dt> <dt>2</dt> </dl>                 | IEEE 802.11 shared authentication that uses a pre-shared wired equivalent privacy (WEP) key. <br/>                                                                                                                                                |
| <span id="Ndis802_11AuthModeAutoSwitch"></span><span id="ndis802_11authmodeautoswitch"></span><span id="NDIS802_11AUTHMODEAUTOSWITCH"></span><dl> <dt>**Ndis802\_11AuthModeAutoSwitch**</dt> <dt>3</dt> </dl> | Auto-switch mode. When using auto-switch mode, the wireless network interface card (NIC) tries shared authentication mode first. If shared mode fails, the NIC attempts to use open authentication mode. <br/>                                    |
| <span id="Ndis802_11AuthModeWPA"></span><span id="ndis802_11authmodewpa"></span><span id="NDIS802_11AUTHMODEWPA"></span><dl> <dt>**Ndis802\_11AuthModeWPA**</dt> <dt>4</dt> </dl>                             | Wireless Protected Access(WPA) security. Authentication is performed between the supplicant, authenticator, and authentication server over IEEE 802.1X. Encryption keys are dynamic and are derived through the authentication process. <br/>     |
| <span id="Ndis802_11AuthModeWPAPSK"></span><span id="ndis802_11authmodewpapsk"></span><span id="NDIS802_11AUTHMODEWPAPSK"></span><dl> <dt>**Ndis802\_11AuthModeWPAPSK**</dt> <dt>5</dt> </dl>                 | WPA security using a pre-shared key. Authentication is performed between the supplicant and authenticator over IEEE 802.1X. Encryption keys are dynamic and are derived through the preshared key used by the supplicant and authenticator. <br/> |
| <span id="Ndis802_11AuthModeWPANone"></span><span id="ndis802_11authmodewpanone"></span><span id="NDIS802_11AUTHMODEWPANONE"></span><dl> <dt>**Ndis802\_11AuthModeWPANone**</dt> <dt>6</dt> </dl>             | WPA security. Authentication is performed using a preshared key without IEEE 802.1X authentication. Encryption keys are static and are derived through the preshared key. This mode is applicable only to ad hoc network types. <br/>             |
| <span id="Ndis802_11AuthModeWPA2"></span><span id="ndis802_11authmodewpa2"></span><span id="NDIS802_11AUTHMODEWPA2"></span><dl> <dt>**Ndis802\_11AuthModeWPA2**</dt> <dt>7</dt> </dl>                         | WPA2 security. Authentication is performed between the supplicant, authenticator, and authentication server over IEEE 802.1X. Encryption keys are dynamic and are derived through the authentication process. <br/>                               |
| <span id="Ndis802_11AuthModeWPA2PSK"></span><span id="ndis802_11authmodewpa2psk"></span><span id="NDIS802_11AUTHMODEWPA2PSK"></span><dl> <dt>**Ndis802\_11AuthModeWPA2PSK**</dt> <dt>8</dt> </dl>             | Specifies WPA2 security. Authentication is performed between the supplicant and authenticator over IEEE 802 1X. Encryption keys are dynamic and are derived through the preshared key used by the supplicant and authenticator. <br/>             |
| <span id="Ndis802_11AuthModeMax"></span><span id="ndis802_11authmodemax"></span><span id="NDIS802_11AUTHMODEMAX"></span><dl> <dt>**Ndis802\_11AuthModeMax**</dt> <dt>9</dt> </dl>                             | The maximum possible value for the **NDIS\_802\_11\_AUTHENTICATION\_MODE** enumeration value. This is not a legal value for the authentication mode. <br/>                                                                                        |



 

</dd> <dt>

**nWepStatus**
</dt> <dd>

The current 802.11 Encryption Mode set on the interface.

</dd> <dt>

**dwCtlFlags**
</dt> <dd>

A bitmask value of control flags that indicate how WZCSVC is operating on the interface.

The following table shows the possible bit values.



| Value                                                                                                                                                                                                                                 | Meaning                                                                                                                                                                                                                                                                                     |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="INTFCTL_CM_MASK"></span><span id="intfctl_cm_mask"></span><dl> <dt>**INTFCTL\_CM\_MASK**</dt> <dt>0x0007</dt> </dl>      | A bitmask for the network filter mode. INTFCTL\_CM\_MASK & dwCtlFlags result in a value of the type NDIS\_802\_11\_NETWORK\_INFRASTRUCTURE. The resulting value indicates whether WZCSVC connects only to infrastructure networks, adhoc networks, or to both types of networks.<br/> |
| <span id="INTFCTL_ENABLED"></span><span id="intfctl_enabled"></span><dl> <dt>**INTFCTL\_ENABLED**</dt> <dt>0x8000</dt> </dl>       | Indicates whether WZCSVC should configure the interface.<br/>                                                                                                                                                                                                                         |
| <span id="INTFCTL_FALLBACK"></span><span id="intfctl_fallback"></span><dl> <dt>**INTFCTL\_FALLBACK**</dt> <dt>0x4000</dt> </dl>    | If a preferred network is not available, this value indicates whether WZCSVC should automatically configure the NIC to associate to any available network.<br/>                                                                                                                       |
| <span id="INTFCTL_OIDSSUPP_"></span><span id="intfctl_oidssupp_"></span><dl> <dt>**INTFCTL\_OIDSSUPP** </dt> <dt>0x2000</dt> </dl> | Indicates whether the NIC driver supports all the 802.11 OIDs required by WZCSVC to function.<br/>                                                                                                                                                                                    |
| <span id="INTFCTL_VOLATILE_"></span><span id="intfctl_volatile_"></span><dl> <dt>**INTFCTL\_VOLATILE** </dt> <dt>0x1000</dt> </dl> | Indicates whether the service parameters for this interface should be retained in the registry. <br/> If this value is set, then these parameters are volatile and should not be retained in the registry.<br/>                                                                 |
| <span id="INTFCTL_POLICY_"></span><span id="intfctl_policy_"></span><dl> <dt>**INTFCTL\_POLICY** </dt> <dt>0x0800</dt> </dl>       | Indicates whether the service parameters for this interface are pushed by a group policy.<br/> If this value is set, then the service parameters are pushed to the local computer by group policy.<br/>                                                                         |
| <span id="INTFCTL_8021XSUPP"></span><span id="intfctl_8021xsupp"></span><dl> <dt>**INTFCTL\_8021XSUPP**</dt> <dt>0x1000</dt> </dl> | Indicates whether 802.1X support is enabled.<br/>                                                                                                                                                                                                                                     |



 

</dd> <dt>

**dwDynFlags**
</dt> <dd>

A bitmask of dynamic flags that control the dynamic (non-persistent and non-static) behavior on the interface.

These bits are useful to trigger dynamic, temporary changes in the way the WZCSVC acts on the interface. None of these bits are persisted in the registry, so the settings won't survive a system restart or a device disable and enable sequence.

The following table shows the possible bit values.



| Value                                                                                                                                                                                                                            | Meaning                                                                                                                                            |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="INTFDYN_NOSCAN"></span><span id="intfdyn_noscan"></span><dl> <dt>**INTFDYN\_NOSCAN**</dt> <dt>0x00000001</dt> </dl> | Indicates that the WZCSVC should not request the interface conduct an active scan, but instead use the cached values in the NIC driver.<br/> |



 

</dd> <dt>

**dwCapabilities**
</dt> <dd>

Specifies the driver capabilities.



| Value                                                                                                                                                                                                                                                         | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="INTFCAP_MAX_CIPHER_MASK"></span><span id="intfcap_max_cipher_mask"></span><dl> <dt>**INTFCAP\_MAX\_CIPHER\_MASK**</dt> <dt>0x000000ff</dt> </dl> | The lower order bits of this member are used to indicate the maximum encryption that is supported. The possible values are some of the enumeration values defined in the **NDIS\_802\_11\_WEP\_STATUS** structure in the *NtDDNdis.h* header file included in the Windows SDK.<br/> The Ndis802\_11Encryption1Enabled value (2) indicates that WEP is supported. TKIP and AES are not supported, and a transmit key may or may not be available. <br/> The Ndis802\_11Encryption2Enabled value (9) indicates that TKIP and WEP are supported. AES is not supported, and a transmit key is available. <br/> The Ndis802\_11Encryption3Enabled value (11) indicates that AES, TKIP, and WEP are supported, and a transmit key is available. <br/> The Ndis802\_11EncryptionNotSupported (8) indicates Indicates that the WEP key is not supported. <br/> |
| <span id="INTFCAP_SSN"></span><span id="intfcap_ssn"></span><dl> <dt>**INTFCAP\_SSN**</dt> <dt>0x00000100</dt> </dl>                                       | Indicates support for Simple Secure Network (SSN) which is a subset of 802.11i. <br/> SSN changes the encryption key periodically, as opposed to the WEP (Wired Equivalent Privacy) standard, which uses a static key. In order for SSN to work, the maximum supported cipher should be at least TKIP. SSN was developed by a consortium of vendors in 2002 as an interim approach to improve wireless LAN security while the IEEE 802.11i standard was being completed.<br/>                                                                                                                                                                                                                                                                                                                                                                                            |
| <span id="INTFCAP_80211I"></span><span id="intfcap_80211i"></span><dl> <dt>**INTFCAP\_80211I**</dt> <dt>0x00000200</dt> </dl>                              | Indicates support for the IEEE 802.11i standard.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |



 

</dd> <dt>

**rdNicCapabilities**
</dt> <dd>

A set of capabilities for 802.11i.

The [**WZCQueryInterface**](wzcqueryinterface.md) function returns **rdNicCapabilities** data when called with the **INTF\_CAPABILITIES** flag passed in the *dwInflags* parameter. If the function call is successful, the **pData** member of the **RAW\_DATA** structure contains an **INTF\_80211\_CAPABILITY** structure.

</dd> <dt>

**rdSSID**
</dt> <dd>

Binary data containing the 802.11 SSID currently configured on the interface.

The [**WZCQueryInterface**](wzcqueryinterface.md) function returns **rdSSID** data when called with the **INTF\_SSID** flag passed in the *dwInflags* parameter. If the function call is successful, the **dwDataLen** member of the **RAW\_DATA** structure contains the **SsidLength** member of a **NDIS\_802\_11\_SSID** structure and the **pData** member of the **RAW\_DATA** structure contains the **Ssid** member of a **NDIS\_802\_11\_SSID** structure.

The **NDIS\_802\_11\_SSID** structure is defined in the *Ntddndis.h* header file.

</dd> <dt>

**rdBSSID**
</dt> <dd>

Binary data containing the 802.11 BSSID configured on the interface.

The [**WZCQueryInterface**](wzcqueryinterface.md) function returns **rdBSSID** data when called with the **INTF\_BSSID** flag passed in the *dwInflags* parameter. If the function call is successful, the **dwDataLen** member of the **RAW\_DATA** structure contains the size of an **NDIS\_802\_11\_MAC\_ADDRESS** structure and the **pData** member of the **RAW\_DATA** structure contains the **NDIS\_802\_11\_MAC\_ADDRESS** structure.

The **NDIS\_802\_11\_MAC\_ADDRESS** structure is defined in the *Ntddndis.h* header file.

</dd> <dt>

**rdBSSIDList**
</dt> <dd>

Binary data that contains the list of BSSIDs that was last retrieved by WZCSVC.

The [**WZCQueryInterface**](wzcqueryinterface.md) function returns **rdBSSIDList** data when called with the **INTF\_BSSIDLIST** flag passed in the *dwInflags* parameter. If the function call is successful, the **dwDataLen** member of the **RAW\_DATA** structure contains the length of the buffer with the returned data and the **pData** member of the **RAW\_DATA** structure contains the **WZC\_802\_11\_CONFIG\_LIST** structure.

</dd> <dt>

**rdStSSIDList**
</dt> <dd>

Binary data that contains the list of preferred networks configured for this interface.

The [**WZCQueryInterface**](wzcqueryinterface.md) function returns **rdStSSIDList** data when called with the **INTF\_PREFLIST** flag passed in the *dwInflags* parameter. If the function call is successful, the **dwDataLen** member of the **RAW\_DATA** structure contains the length of the buffer with the returned data and the **pData** member of the **RAW\_DATA** structure contains the **WZC\_802\_11\_CONFIG\_LIST** structure.

If one of the preferred networks is currently connected, the **dwCtlFlags** member of the **WZC\_WLAN\_CONFIG** structure for the network will have the **WZCCTL\_MEDIA\_CONNECTED** (0x0400) bit set.

</dd> <dt>

**rdCtrlData**
</dt> <dd>

Binary data used with other control flags, when setting additional parameters on the interface.

</dd> </dl>

## Remarks

The **INTF\_ENTRY** structure is used by the [**WZCQueryInterface**](wzcqueryinterface.md) and [**WZCRefreshInterface**](wzcrefreshinterface.md) functions.

The **RAW\_DATA** structure is defined as follows:


```C++
typedef struct
{
    DWORD   dwDataLen;
    LPBYTE  pData;
} RAW_DATA, *PRAW_DATA;
```



The *pData* member points to binary data. The *dwDataLen* indicates the number of bytes pointed by *pData*.

> [!Note]  
> The *Wzcsapi.h* header file is not available in the Windows SDK.

 

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP with SP2 \[desktop apps only\]<br/>                                 |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                 |
| End of client support<br/>    | Windows XP with SP3<br/>                                                       |
| End of server support<br/>    | Windows Server 2003<br/>                                                       |
| Header<br/>                   | <dl> <dt>Wzcsapi.h</dt> </dl> |



## See also

<dl> <dt>

[**WZCEnumInterfaces**](wzcenuminterfaces.md)
</dt> <dt>

[**WZCQueryInterface**](wzcqueryinterface.md)
</dt> <dt>

[**WZCRefreshInterface**](wzcrefreshinterface.md)
</dt> </dl>

 

 




