---
title: MDM\_WirelessProfile class
description: Represents wireless profiles on the device.
ms.assetid: 6c0f48d9-4c89-4fd6-8150-dc76cd4b8a7b
keywords:
- MDM_WirelessProfile class MDM Settings
- MDM_WirelessProfile class MDM Settings , described
topic_type:
- apiref
api_name:
- MDM_WirelessProfile
- MDM_WirelessProfile.Name
- MDM_WirelessProfile.SSID
- MDM_WirelessProfile.ConnectWhenNotBroadcasting
- MDM_WirelessProfile.AutoConnect
- MDM_WirelessProfile.ConnectionType
- MDM_WirelessProfile.ConnectToMorePreferedNetwork
- MDM_WirelessProfile.SecurityAuthentication
- MDM_WirelessProfile.SecurityEncryption
- MDM_WirelessProfile.PMKCacheMode
- MDM_WirelessProfile.PMKCacheSize
- MDM_WirelessProfile.PMKCacheTTL
- MDM_WirelessProfile.PreAuthMode
- MDM_WirelessProfile.PreAuthThrottle
- MDM_WirelessProfile.EnableFIPSCompliance
- MDM_WirelessProfile.SharedKeyType
- MDM_WirelessProfile.SharedKeyMaterial
- MDM_WirelessProfile.SharedKeyProtected
- MDM_WirelessProfile.OneXCacheUserData
- MDM_WirelessProfile.OneXAuthenticationMode
- MDM_WirelessProfile.OneXSingleSignOnType
- MDM_WirelessProfile.OneXSingleSignOnMaxDelay
- MDM_WirelessProfile.OneXSingleSignOnAllowAdditionalDialogs
- MDM_WirelessProfile.OneXSingleSignOnUserBasedVirtualLAN
- MDM_WirelessProfile.OneXEAPType
- MDM_WirelessProfile.OneXEAPXml
api_location:
- MDMSettingsProv.dll
api_type:
- DllExport
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MDM\_WirelessProfile class

Represents wireless profiles on the device.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[InPartition("local-user"), dynamic, provider("MDMSettingsProv"), AMENDMENT]
class MDM_WirelessProfile
{
  string  Name;
  string  SSID;
  boolean ConnectWhenNotBroadcasting;
  boolean AutoConnect;
  uint8   ConnectionType;
  boolean ConnectToMorePreferedNetwork;
  uint8   SecurityAuthentication;
  uint8   SecurityEncryption;
  boolean PMKCacheMode;
  uint32  PMKCacheSize;
  uint32  PMKCacheTTL;
  boolean PreAuthMode;
  uint32  PreAuthThrottle;
  boolean EnableFIPSCompliance;
  uint8   SharedKeyType;
  string  SharedKeyMaterial;
  boolean SharedKeyProtected;
  boolean OneXCacheUserData;
  uint8   OneXAuthenticationMode;
  uint8   OneXSingleSignOnType;
  uint32  OneXSingleSignOnMaxDelay;
  boolean OneXSingleSignOnAllowAdditionalDialogs;
  boolean OneXSingleSignOnUserBasedVirtualLAN;
  uint8   OneXEAPType;
  string  OneXEAPXml;
};
```

## Members

The **MDM\_WirelessProfile** class has these types of members:

-   [Properties](#properties)

### Properties

The **MDM\_WirelessProfile** class has these properties.

<dl> <dt>

**AutoConnect**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

True if auto connect is enabled.

</dd> <dt>

**ConnectionType**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The connection type.

Possible values are.

<dt>

<span id="ESS"></span><span id="ess"></span>

**ESS** (1)


</dt> <dd></dd> <dt>

<span id="IBSS"></span><span id="ibss"></span>

**IBSS** (2)


</dt> <dd></dd> </dl>

</dd> <dt>

**ConnectToMorePreferedNetwork**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

True to connect to a hidden network.

</dd> <dt>

**ConnectWhenNotBroadcasting**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

True if **Connect when not broadcasting** is enabled.

</dd> <dt>

**EnableFIPSCompliance**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

True if Federal Information Processing Standards (FIPS) mode is enabled.

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

The name of a wireless LAN profile.

</dd> <dt>

**OneXAuthenticationMode**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The type of credentials used for authentication.

The possible values are.

<dt>

<span id="MachineOrUser"></span><span id="machineoruser"></span><span id="MACHINEORUSER"></span>

**MachineOrUser** (1)


</dt> <dd></dd> <dt>

<span id="Machine"></span><span id="machine"></span><span id="MACHINE"></span>

**Machine** (2)


</dt> <dd></dd> <dt>

<span id="User"></span><span id="user"></span><span id="USER"></span>

**User** (3)


</dt> <dd></dd> <dt>

<span id="Guest"></span><span id="guest"></span><span id="GUEST"></span>

**Guest** (4)


</dt> <dd></dd> </dl>

</dd> <dt>

**OneXCacheUserData**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

True if the user credentials are cached for subsequent connections.

</dd> <dt>

**OneXEAPType**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The type of Extensible Authentication Protocol (EAP) used for this connection.

The possible values are.

<dt>

<span id="TLS"></span><span id="tls"></span>

**TLS** (13)


</dt> <dd></dd> <dt>

<span id="SIM"></span><span id="sim"></span>

**SIM** (18)


</dt> <dd></dd> <dt>

<span id="TTLS"></span><span id="ttls"></span>

**TTLS** (21)


</dt> <dd></dd> <dt>

<span id="AKA"></span><span id="aka"></span>

**AKA** (23)


</dt> <dd></dd> <dt>

<span id="PEAP"></span><span id="peap"></span>

**PEAP** (25)


</dt> <dd></dd> <dt>

<span id="AKAPRIME"></span><span id="akaprime"></span>

**AKAPRIME** (50)


</dt> <dd></dd> </dl>

</dd> <dt>

**OneXEAPXml**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The configuration XML that is used for this EAP connection.

</dd> <dt>

**OneXSingleSignOnAllowAdditionalDialogs**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

True if different dialog boxes are presented to the user at logon for single sign-on, if applicable.

</dd> <dt>

**OneXSingleSignOnMaxDelay**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The maximum delay before the single sign-on connection attempt fails, in seconds.

</dd> <dt>

**OneXSingleSignOnType**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies when single sign-on is performed.

<dt>

<span id="preLogon"></span><span id="prelogon"></span><span id="PRELOGON"></span>

**preLogon** (1)


</dt> <dd></dd> <dt>

<span id="postLogon"></span><span id="postlogon"></span><span id="POSTLOGON"></span>

**postLogon** (2)


</dt> <dd></dd> </dl>

</dd> <dt>

**OneXSingleSignOnUserBasedVirtualLAN**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

True if the virtual LAN (VLAN) used by the device changes based on the user's credentials.

</dd> <dt>

**PMKCacheMode**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

True if *Pairwise Master Key* (PMK) caching is used.

</dd> <dt>

**PMKCacheSize**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of entries in the PMK cache.

</dd> <dt>

**PMKCacheTTL**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The length of time, in minutes, that a PMK cache is retained.

</dd> <dt>

**PreAuthMode**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

True if pre-authentication is used by the client.

</dd> <dt>

**PreAuthThrottle**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of pre-authentication attempts to try on neighboring Access Points.

</dd> <dt>

**SecurityAuthentication**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The authentication method that is used to connect to the wireless LAN.

The possible values are.

<dt>

<span id="Open"></span><span id="open"></span><span id="OPEN"></span>

**Open** (1)


</dt> <dd></dd> <dt>

<span id="WPA-Personal"></span><span id="wpa-personal"></span><span id="WPA-PERSONAL"></span>

**WPA-Personal** (2)


</dt> <dd></dd> <dt>

<span id="WPA-2-Personal"></span><span id="wpa-2-personal"></span><span id="WPA-2-PERSONAL"></span>

**WPA-2-Personal** (3)


</dt> <dd></dd> <dt>

<span id="WPA-Enterprise"></span><span id="wpa-enterprise"></span><span id="WPA-ENTERPRISE"></span>

**WPA-Enterprise** (4)


</dt> <dd></dd> <dt>

<span id="WPA2-Enterprise"></span><span id="wpa2-enterprise"></span><span id="WPA2-ENTERPRISE"></span>

**WPA2-Enterprise** (5)


</dt> <dd></dd> <dt>

<span id="shared"></span><span id="SHARED"></span>

**shared** (6)


</dt> <dd></dd> <dt>

<span id="WEP"></span><span id="wep"></span>

**WEP** (7)


</dt> <dd></dd> </dl>

</dd> <dt>

**SecurityEncryption**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The type of data encryption to use to connect to a wireless LAN.

The possible values are.

<dt>

<span id="None"></span><span id="none"></span><span id="NONE"></span>

**None** (1)


</dt> <dd></dd> <dt>

<span id="WEP"></span><span id="wep"></span>

**WEP** (2)


</dt> <dd></dd> <dt>

<span id="TKIP"></span><span id="tkip"></span>

**TKIP** (3)


</dt> <dd></dd> <dt>

<span id="AES"></span><span id="aes"></span>

**AES** (4)


</dt> <dd></dd> </dl>

</dd> <dt>

**SharedKeyMaterial**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A network key or pass-phrase.

</dd> <dt>

**SharedKeyProtected**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

True if a shared key is encrypted.

</dd> <dt>

**SharedKeyType**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read-only
</dt> </dl>

True if the shared key is a network key or a pass phrase.

The possible values are.

<dt>

<span id="passPhrase"></span><span id="passphrase"></span><span id="PASSPHRASE"></span>

**passPhrase** (1)


</dt> <dd></dd> <dt>

<span id="networkKey"></span><span id="networkkey"></span><span id="NETWORKKEY"></span>

**networkKey** (2)


</dt> <dd></dd> </dl>

</dd> <dt>

**SSID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The service set identifier (SSID) for the wireless LAN.

</dd> </dl>

## Requirements



|                                     |                                                                                                |
|-------------------------------------|------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1<br/>                                                                         |
| Minimum supported server<br/> | None supported<br/>                                                                      |
| Namespace<br/>                | Root\\CIMv2\\MDM<br/>                                                                    |
| MOF<br/>                      | <dl> <dt>MDMSettingsProv.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MDMSettingsProv.dll</dt> </dl> |



## See also

<dl> <dt>

[Mobile Device Management Settings Classes](https://msdn.microsoft.com/library/dn610402)
</dt> </dl>

 

 





