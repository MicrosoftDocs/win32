---
description: Represents a wireless communication endpoint, which can send and receive data frames when its associated interface device is connected with an IEEE 802.11 wireless LAN.
ms.assetid: 61743402-f333-4501-ba17-e676d85f72f3
title: CIM_WiFiEndpoint class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CIM_WiFiEndpoint
- CIM_WiFiEndpoint.LANID
- CIM_WiFiEndpoint.ProtocolIFType
- CIM_WiFiEndpoint.EncryptionMethod
- CIM_WiFiEndpoint.OtherEncryptionMethod
- CIM_WiFiEndpoint.AuthenticationMethod
- CIM_WiFiEndpoint.OtherAuthenticationMethod
- CIM_WiFiEndpoint.IEEE8021xAuthenticationProtocol
- CIM_WiFiEndpoint.AccessPointAddress
- CIM_WiFiEndpoint.BSSType
- CIM_WiFiEndpoint.Associated
api_type: 
- DllExport
api_location: 
- vmms.exe
---

# CIM\_WiFiEndpoint class

Represents a wireless communication endpoint, which can send and receive data frames when its associated interface device is connected with an IEEE 802.11 wireless LAN.

## Syntax

``` syntax
[Abstract, Version("2.22.0"), UMLPackagePath("CIM::Network::Wireless"), AMENDMENT]
class CIM_WiFiEndpoint : CIM_LANEndpoint
{
  string  LANID;
  uint16  ProtocolIFType = 71;
  uint16  EncryptionMethod;
  string  OtherEncryptionMethod;
  uint16  AuthenticationMethod;
  string  OtherAuthenticationMethod;
  uint16  IEEE8021xAuthenticationProtocol;
  string  AccessPointAddress;
  uint16  BSSType;
  boolean Associated;
};
```

## Members

The **CIM\_WiFiEndpoint** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_WiFiEndpoint** class has these properties.

<dl> <dt>

**AccessPointAddress**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The MAC address of the access point that is associated with the Wi-Fi endpoint; otherwise, **NULL**.

</dd> <dt>

**Associated**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

**true** if the WiFi endpoint is currently associated with an access point or client station; otherwise, **false**.

</dd> <dt>

**AuthenticationMethod**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](/windows/desktop/WmiSdk/standard-qualifiers) ("IEEE 802.11-2007 \| 8"), [**ModelCorrespondence**](/windows/desktop/WmiSdk/standard-qualifiers) ("**CIM\_WiFiEndpoint**.**EncryptionMethod**", "**CIM\_WiFiEndpoint**.**IEEE8021xAuthenticationProtocol**", "**CIM\_WiFiEndpoint**.**OtherAuthenticationMethod**")
</dt> </dl>

The authentication type used between the Wi-Fi endpoint and the network.

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (0)


</dt> <dd></dd> <dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>

**Other** (1)


</dt> <dd></dd> <dt>

<span id="Open_System"></span><span id="open_system"></span><span id="OPEN_SYSTEM"></span>

**Open System** (2)


</dt> <dd></dd> <dt>

<span id="Shared_Key"></span><span id="shared_key"></span><span id="SHARED_KEY"></span>

**Shared Key** (3)


</dt> <dd></dd> <dt>

<span id="WPA_PSK"></span><span id="wpa_psk"></span>

**WPA PSK** (4)


</dt> <dd></dd> <dt>

<span id="WPA_IEEE_802.1x"></span><span id="wpa_ieee_802.1x"></span><span id="WPA_IEEE_802.1X"></span>

**WPA IEEE 802.1x** (5)


</dt> <dd></dd> <dt>

<span id="WPA2_PSK"></span><span id="wpa2_psk"></span>

**WPA2 PSK** (6)


</dt> <dd></dd> <dt>

<span id="WPA2_IEEE_802.1x"></span><span id="wpa2_ieee_802.1x"></span><span id="WPA2_IEEE_802.1X"></span>

**WPA2 IEEE 802.1x** (7)


</dt> <dd></dd> <dt>

<span id="CCKM_IEEE_802.1x"></span><span id="cckm_ieee_802.1x"></span><span id="CCKM_IEEE_802.1X"></span>

**CCKM IEEE 802.1x** (8)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved** (9..)


</dt> <dd></dd> </dl>

</dd> <dt>

**BSSType**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](/windows/desktop/WmiSdk/standard-qualifiers) ("IEEE 802.11-2007 \| 3.16")
</dt> </dl>

The basic service set (BSS) type of the network that corresponds to the instance. A BSS is a set of stations controlled by a single coordination function.

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (0)


</dt> <dd></dd> <dt>

<span id="Independent"></span><span id="independent"></span><span id="INDEPENDENT"></span>

**Independent** (2)


</dt> <dd></dd> <dt>

<span id="Infrastructure"></span><span id="infrastructure"></span><span id="INFRASTRUCTURE"></span>

**Infrastructure** (3)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved** (4..)


</dt> <dd></dd> </dl>

</dd> <dt>

**EncryptionMethod**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](/windows/desktop/WmiSdk/standard-qualifiers) ("IEEE 802.11-2007 \| 8"), [**ModelCorrespondence**](/windows/desktop/WmiSdk/standard-qualifiers) ("**CIM\_WiFiEndpoint**.**AuthenticationMethod**", "**CIM\_WiFiEndpoint**.**OtherEncryptionMethod**")
</dt> </dl>

The encryption type used when sending and receiving data through the Wi-Fi endpoint.

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (0)


</dt> <dd></dd> <dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>

**Other** (1)


</dt> <dd></dd> <dt>

<span id="WEP"></span><span id="wep"></span>

**WEP** (2)


</dt> <dd></dd> <dt>

<span id="TKIP"></span><span id="tkip"></span>

**TKIP** (3)


</dt> <dd></dd> <dt>

<span id="CCMP"></span><span id="ccmp"></span>

**CCMP** (4)


</dt> <dd></dd> <dt>

<span id="None"></span><span id="none"></span><span id="NONE"></span>

**None** (5)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved** (6..)


</dt> <dd></dd> </dl>

</dd> <dt>

**IEEE8021xAuthenticationProtocol**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](/windows/desktop/WmiSdk/standard-qualifiers) ("RFC4017.IETF", "RFC2716.IETF", "draft-ietf-pppext-eap-ttls.IETF", "draft-kamath-pppext-peapv0.IETF", "draft-josefsson-pppext-eap-tls-eap", "RFC4851.IETF", "RFC3748.IETF", "RFC4764.IETF", "RFC4186.IETF", "RFC4187.IETF"), [**ModelCorrespondence**](/windows/desktop/WmiSdk/standard-qualifiers) ("**CIM\_WiFiEndpoint**.**AuthenticationMethod**")
</dt> </dl>

The EAP (Extensible Authentication Protocol) type for the Wi-Fi endpoint when **AuthenticationMethod** contains "7" (WPA IEEE 802.1x) or "8" (CCKM IEEE 802.1x).

<dt>

<span id="EAP-TLS"></span><span id="eap-tls"></span>

**EAP-TLS** (0)


</dt> <dd></dd> <dt>

<span id="EAP-TTLS_MSCHAPv2"></span><span id="eap-ttls_mschapv2"></span><span id="EAP-TTLS_MSCHAPV2"></span>

**EAP-TTLS/MSCHAPv2** (1)


</dt> <dd></dd> <dt>

<span id="PEAPv0_EAP-MSCHAPv2"></span><span id="peapv0_eap-mschapv2"></span><span id="PEAPV0_EAP-MSCHAPV2"></span>

**PEAPv0/EAP-MSCHAPv2** (2)


</dt> <dd></dd> <dt>

<span id="PEAPv1_EAP-GTC"></span><span id="peapv1_eap-gtc"></span><span id="PEAPV1_EAP-GTC"></span>

**PEAPv1/EAP-GTC** (3)


</dt> <dd></dd> <dt>

<span id="EAP-FAST_MSCHAPv2"></span><span id="eap-fast_mschapv2"></span><span id="EAP-FAST_MSCHAPV2"></span>

**EAP-FAST/MSCHAPv2** (4)


</dt> <dd></dd> <dt>

<span id="EAP-FAST_GTC"></span><span id="eap-fast_gtc"></span>

**EAP-FAST/GTC** (5)


</dt> <dd></dd> <dt>

<span id="EAP-MD5"></span><span id="eap-md5"></span>

**EAP-MD5** (6)


</dt> <dd></dd> <dt>

<span id="EAP-PSK"></span><span id="eap-psk"></span>

**EAP-PSK** (7)


</dt> <dd></dd> <dt>

<span id="EAP-SIM"></span><span id="eap-sim"></span>

**EAP-SIM** (8)


</dt> <dd></dd> <dt>

<span id="EAP-AKA"></span><span id="eap-aka"></span>

**EAP-AKA** (9)


</dt> <dd></dd> <dt>

<span id="EAP-FAST_TLS"></span><span id="eap-fast_tls"></span>

**EAP-FAST/TLS** (10)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved** (11..)


</dt> <dd></dd> </dl>

</dd> <dt>

**LANID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](/windows/desktop/WmiSdk/standard-qualifiers) ("LANID"), [**MappingStrings**](/windows/desktop/WmiSdk/standard-qualifiers) ("IEEE 802.11-2007 \| 7.3.2.1")
</dt> </dl>

The service set identifier (SSID) of the wireless LAN that is associated with the Wi-Fi endpoint; otherwise, **NULL**.

</dd> <dt>

**OtherAuthenticationMethod**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](/windows/desktop/WmiSdk/standard-qualifiers) ("**CIM\_WiFiEndpoint**.**AuthenticationMethod**")
</dt> </dl>

The authentication type used between the Wi-Fi endpoint and the network when **AuthenticationMethod** contains "1" (Other).

</dd> <dt>

**OtherEncryptionMethod**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](/windows/desktop/WmiSdk/standard-qualifiers) ("**CIM\_WiFiEndpoint**.**EncryptionMethod**")
</dt> </dl>

Describes the encryption type for the Wi-Fi endpoint when **EncryptionMethod** contains "1" (Other).

</dd> <dt>

**ProtocolIFType**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](/windows/desktop/WmiSdk/standard-qualifiers) ("ProtocolIFType")
</dt> </dl>

The category or classification of this instance. The possible values are limited to the Wi-Fi and reserved values from the DMTF and [IANA ifType MIB](https://www.iana.org/assignments/ianaiftype-mib).

If the **ProtocolIFType** is set to "1" (Other), then the type information should be provided in the **OtherTypeDescription** property.

<dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>

**Other** (1)


</dt> <dd></dd> <dt>

<span id="IEEE_802.11"></span><span id="ieee_802.11"></span>

**IEEE 802.11** (71)


</dt> <dd></dd> <dt>

<span id="IANA_Reserved"></span><span id="iana_reserved"></span><span id="IANA_RESERVED"></span>

**IANA Reserved** (225..4095)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved** (4301..32767)


</dt> <dd></dd> <dt>

<span id="Vendor_Reserved"></span><span id="vendor_reserved"></span><span id="VENDOR_RESERVED"></span>

**Vendor Reserved** (32768..)


</dt> <dd></dd> </dl>

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                                    |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                          |
| Namespace<br/>                | Root\\virtualization\\v2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Vmms.exe</dt> </dl>                     |



## See also

<dl> <dt>

[**CIM\_LANEndpoint**](cim-lanendpoint.md)
</dt> </dl>

 

