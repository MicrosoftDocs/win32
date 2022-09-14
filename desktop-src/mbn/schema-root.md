---
description: Mobile Broadband Profile Schema v4.
MS-HAID: WWAN\_profile\_v4.Schema\_Root
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/desktop
title: Mobile Broadband Profile Schema v4
ms.topic: reference
ms.date: 05/31/2018
ms.assetid: 0945e34c-74f3-4133-8b36-e45562ce2a88
api_name: 
api_type: 
api_location: 
topic_type: 
 - kbArticle

---

# <span id="WWAN_profile_v4.Schema_Root"></span>Mobile Broadband Profile Schema v4

The Windows 10Mobile Broadband Profile Schema v4 is available in the namespace `https://www.microsoft.com/networking/WWAN/profile/v4`.

-   [Mobile Broadband Profile Schema v4 Elements](root-elements.md)
-   [Mobile Broadband Profile Schema v4 Simple Types](simple-types.md)

``` syntax
<xs:schema targetNamespace="https://www.microsoft.com/networking/WWAN/profile/v4"
    xmlns="https://www.microsoft.com/networking/WWAN/profile/v4"
    xmlns:xs="https://www.w3.org/2001/XMLSchema"
    xmlns:WWAN_profile_v1="https://www.microsoft.com/networking/WWAN/profile/v1"
    xmlns:WWAN_profile_v2="https://www.microsoft.com/networking/WWAN/profile/v2"
    xmlns:WWAN_profile_v3="https://www.microsoft.com/networking/WWAN/profile/v3"
    elementFormDefault="qualified">

    <xs:import namespace="https://www.microsoft.com/networking/WWAN/profile/v1" schemaLocation="WWAN_profile_v1.xsd"/>
    <xs:import namespace="https://www.microsoft.com/networking/WWAN/profile/v2" schemaLocation="WWAN_profile_v2.xsd"/>
    <xs:import namespace="https://www.microsoft.com/networking/WWAN/profile/v3" schemaLocation="WWAN_profile_v3.xsd"/>

  <!-- type definition section -->

  <!-- Extended contextType based on the Schema v1 contextType -->
  <xs:complexType name="contextExtType">
    <xs:sequence>
      <xs:element name="AccessString" minOccurs="0">
        <xs:simpleType>
          <xs:restriction base="xs:token">
            <xs:minLength value="1"/>
            <xs:maxLength value="100"/>
          </xs:restriction>
        </xs:simpleType>
      </xs:element>
      <xs:element name="UserLogonCred" minOccurs="0">
        <xs:complexType>
          <xs:sequence>
            <xs:element name="UserName" type="WWAN_profile_v1:nameType"/>
            <xs:element name="IgnorePassword" type="xs:boolean" minOccurs="0" />
            <xs:element name="Password" type="xs:string" minOccurs="0"/>
          </xs:sequence>
        </xs:complexType>
      </xs:element>
      <xs:element name="Compression" minOccurs="0">
        <xs:simpleType>
          <xs:restriction base="xs:token">
            <xs:enumeration value="DISABLE"/>
            <xs:enumeration value="ENABLE"/>
          </xs:restriction>
        </xs:simpleType>
      </xs:element>
      <xs:element name="AuthProtocol" minOccurs="0">
        <xs:simpleType>
          <xs:restriction base="xs:token">
            <xs:enumeration value="NONE"/>
            <xs:enumeration value="PAP"/>
            <xs:enumeration value="CHAP"/>
            <xs:enumeration value="MsCHAPv2"/>
            <!-- NEW enum in contextExType ( not in contextType of v1) -->
            <!-- AutoSelection means that an auth protocol is to be picked by lower layer(s) -->
            <xs:enumeration value="AutoSelection"/>
          </xs:restriction>
        </xs:simpleType>
      </xs:element>
      <!-- NEW element in contextExType ( not in contextType of v1) -->
      <xs:element name="IPType" minOccurs="0">
        <!-- When this element is absent, the IPType is default -->
        <xs:simpleType>
          <xs:restriction base="xs:token">
            <!-- Default means that an IP type is to be picked by lower layer(s) -->
            <xs:enumeration value="Default"/>
            <xs:enumeration value="IPv4"/>
            <xs:enumeration value="IPv6"/>
            <xs:enumeration value="IPv4v6"/>
            <xs:enumeration value="XLAT"/>
          </xs:restriction>
        </xs:simpleType>
      </xs:element>
    </xs:sequence>
  </xs:complexType>

  <!-- applicability to any combination of home carrier, partner MOs and non-partner MOs, except for HomeAndNonPartner -->
  <xs:simpleType name="roamApplicabilityType">
    <xs:restriction base="xs:token">
       <xs:enumeration value="NonPartnerOnly"/>
       <xs:enumeration value="PartnerOnly"/>
       <xs:enumeration value="HomeOnly"/>
       <xs:enumeration value="HomeAndPartner"/>
       <xs:enumeration value="PartnerAndNonpartner"/>
       <xs:enumeration value="AllRoaming"/>
    </xs:restriction>
  </xs:simpleType>

  <xs:simpleType name="roamControlType">
    <xs:restriction base="xs:token">
       <xs:enumeration value="AllRoamAllowed"/>
       <xs:enumeration value="PartnerRoamAllowed"/>
       <xs:enumeration value="NoRoamAllowed"/>
    </xs:restriction>
  </xs:simpleType>

  <!-- A type definition for what wireless network or networks a profile is applicable at -->
  <xs:simpleType name="iwlanApplicabilityType">
    <xs:restriction base="xs:token">
      <xs:enumeration value="CellularOnly"/>
      <xs:enumeration value="CellularAndIwlan"/>
      <xs:enumeration value="IwlanOnly"/>
    </xs:restriction>
  </xs:simpleType>

  <!-- Define the data type for conditions where a profile is applicable -->
  <xs:complexType name="profileConditionType">
    <!-- When an optional element is absent, the profile is not subject to the condition related to the element, -->
    <!-- unless specifically specified otherwise -->
    <xs:sequence>    
      <xs:element name="CellularClass" minOccurs="0">
        <xs:simpleType>
          <xs:restriction base="xs:token">
            <xs:enumeration value="3GPP"/>
            <xs:enumeration value="3GPP2"/>
          </xs:restriction>
        </xs:simpleType>
      </xs:element>
      
      <xs:element name="RATApplicability" minOccurs="0">
        <!-- if this is present, , the element of CellularClass must be present and is 3GPP -->
        <xs:simpleType>
          <xs:restriction base="xs:token">
            <xs:enumeration value="LTE_eHRPD"/>
            <xs:enumeration value="3GPP_LEGACY"/>
          </xs:restriction>
        </xs:simpleType>
      </xs:element>
      
      <xs:element name="RoamApplicability" type="roamApplicabilityType" minOccurs="0" />
      
      <!-- If IMSI is present, the profile is applicable only for the IMSI -->
      <xs:element name="IMSI" type="WWAN_profile_v1:subscriberIdType" minOccurs="0"/>

      <!-- if this element is absent or the containing ProfileConditionType element is absent, CellularOnly is assumed. -->
      <!-- IWLAN network does not have such cellular-centric parameters as roaming state, RAT type or cellular class. -->
      <!-- The profile conditions or policies related to those cellular-centric parameters do not apply -->
      <!-- in the consideration of using a profile on IWLAN. -->
      <xs:element name="IwlanApplicability" type="iwlanApplicabilityType" minOccurs="0"/>

    </xs:sequence>
  </xs:complexType>

  <!-- GUID in string, as in example: {17c5d5ec-c9be-4b8b-aa76-984f07cb1cf0} -->
  <xs:simpleType name="guidType">
    <xs:restriction base="xs:token">
      <xs:pattern value="{[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}}"/>
    </xs:restriction>
  </xs:simpleType>
  
  <xs:complexType name="mmsConfigurationType">
    <xs:sequence>
      <!-- optional element, the URL of the MMSC server for mobile device -->
      <xs:element name="MmscUrl" type="xs:anyURI" minOccurs="0"/>
      
      <!-- optional element, the port number of the MMSC server for mobile device. -->
      <!-- valid range [1,99999]. 0 or absence means no specific port number specified -->
      <xs:element name="MmscPort" minOccurs="0">
        <xs:simpleType>
          <xs:restriction base="xs:nonNegativeInteger">
            <xs:maxInclusive value="99999"/>
          </xs:restriction>
        </xs:simpleType>
      </xs:element>
        
      <!-- optional element, the maximum message size in kilobytes for MMS messages. -->
      <!-- The value 0 indicates no maximum -->
      <xs:element name="MmsMaximumMessageSize" type="xs:nonNegativeInteger" minOccurs="0"/>
    </xs:sequence>
  </xs:complexType>

  <!-- element definition section -->

  <xs:element name="MBNProfileExt">
    <xs:complexType>
      <xs:sequence>
        <!-- Profile name -->
        <xs:element name="Name" type="WWAN_profile_v1:nameType"/>

        <!-- Brief description of the profile -->
        <xs:element name="Description" type="WWAN_profile_v1:nameType" minOccurs="0"/>

        <!-- Path of the icon file for the provider -->
        <xs:element name="ICONFilePath" type="WWAN_profile_v1:iconFileType" minOccurs="0"/>

        <!-- Flag to indicate whether this is the default profile -->
        <!-- Atmost one profile per SIM shall have this flag set to true -->
        <xs:element name="IsDefault" type="xs:boolean"/>

        <!-- Profile creation type -->
        <!-- This is used to decide if the user can delete the profile or not  -->
        <!-- This is used to prioritize profiles when more than one are applicable  -->
        <xs:element name="ProfileCreationType" minOccurs="0">
          <xs:simpleType>
            <xs:restriction base="xs:token">
              <xs:enumeration value="UserProvisioned"/>
              <xs:enumeration value="AdminProvisioned"/>
              <xs:enumeration value="OperatorProvisioned"/>
              <xs:enumeration value="DeviceProvisioned"/>
            </xs:restriction>
          </xs:simpleType>
        </xs:element>

        <!-- Subscriber Identification : IMSI, MIN, etc -->
        <!-- optional in extended MBNProfile -->
        <xs:element name="SubscriberID" type="WWAN_profile_v1:subscriberIdType" minOccurs="0"/>

        <!-- SimIccID number of the SIM -->
        <!-- Mandatory in extended MBNProfile -->
        <xs:element name="SimIccID" type="WWAN_profile_v1:simIccIDType" />

        <!-- Home Provider Name -->
        <xs:element name="HomeProviderName" type="WWAN_profile_v1:providerNameType" minOccurs="0"/>

        <!-- Flag to indicate wether the Auto Connect should be blocked when we have Internet Connectivity -->
        <xs:element name="AutoConnectOnInternet" type="xs:boolean" minOccurs="0"/>

        <!-- Connection Mode, default is "manual" -->
        <xs:element name="ConnectionMode" minOccurs="0">
          <xs:simpleType>
            <xs:restriction base="xs:string">
              <!-- manual connect always -->
              <xs:enumeration value="manual" />
              <!-- auto connect always -->
              <xs:enumeration value="auto" />
              <!-- auto connect when not roaming -->
              <xs:enumeration value="auto-home"/>
            </xs:restriction>
          </xs:simpleType>
        </xs:element>

        <!-- Connection Settings -->
        <xs:element name="Context" type="contextExtType" minOccurs="0"/>

        <!-- Roaming Partner List -->
        <xs:element name="DataRoamingPartners" minOccurs="0">
          <xs:complexType>
            <xs:sequence>
              <xs:element name="Provider" type="WWAN_profile_v1:providerType" maxOccurs="unbounded"/>
            </xs:sequence>
          </xs:complexType>
        </xs:element>

        <!-- Profile Group List -->
        <!-- A profile group is defined by a GUID, for the usage purpose of profiles of the group. -->
        <!-- One profile may belong to more than one group, i.e. a profile can be multi-purposed. -->
        <xs:element name="PurposeGroups" minOccurs="0">
          <xs:complexType>
            <xs:sequence>
              <xs:element name="PurposeGroupGuid" type="guidType" maxOccurs="10"/>
            </xs:sequence>
          </xs:complexType>
        </xs:element>

        <!-- optional element for MBNProfileExt. It defines the condition(s) when the profile is applicable (usable) -->
        <!-- If ProfileConditionedOn is present, the defined condiftion(s) must be satisfied for the profile to be applicable -->
        <xs:element name="ProfileConditionedOn" type="profileConditionType" minOccurs="0"/>

        <!-- Flag to indicate whether this is a provisioning profile, default is "false" -->
        <!-- If IsProvisioningProfile is true, IsDefault must be false, ConnectionMode must be manual -->
        <xs:element name="IsProvisioningProfile" type="xs:boolean" minOccurs="0"/>

        <!-- optional element. the Default is 0 -->
        <xs:element name="ApnID" type="xs:decimal" minOccurs="0"/>
        
        <!-- optional elemtment. the default is TRUE (enabled) -->
        <xs:element name="AdminEnable" type="xs:boolean" minOccurs="0"/>
        
        <!-- optional element, the default is AllRoamAllowed -->
        <xs:element name="AdminRoamControl" type="roamControlType" minOccurs="0"/>

        <!-- Flag to indicate whether this profile excludes other profiles of the same group, default is "false" -->
        <xs:element name="IsExclusiveToOther" type="xs:boolean" minOccurs="0"/>

        <!-- Flag to indicate whether this is a long-standing additional PDP context profile, default is "false" -->
        <!-- If IsLongStandingManualProfile is true, IsAdditionalPdpContextProfile must be true -->
        <xs:element name="IsLongStandingAdditionalPdpContextProfile" type="xs:boolean" minOccurs="0"/>

        <!-- Mms settings -->
        <xs:element name="MmsConfiguration" type="mmsConfigurationType" minOccurs="0"/>
        
        <!-- extension point for other namespaces -->
        <xs:any namespace="##other" processContents="lax" minOccurs="0" maxOccurs="unbounded" />
      </xs:sequence>
    </xs:complexType>
  </xs:element>
  
  <!-- modem DM configuration Profile -->
  <xs:element name="ModemDMConfigProfile">
    <xs:complexType>
      <xs:sequence>
        <!-- Profile name -->
        <xs:element name="Name" type="WWAN_profile_v1:nameType"/>

        <!-- SimIccID -->
        <xs:element name="SimIccID" type="WWAN_profile_v1:simIccIDType" />
        <xs:element name="ApnID" type="xs:decimal"/>
        
        <!-- For modem -->
        <xs:element name="OemConnectionId" type="guidType"/>
        <xs:element name="RoamApplicability" type="roamApplicabilityType" minOccurs="0" />
        
        <xs:element name="Context" type="contextExtType" />
        <xs:element name="AdminEnable" type="xs:boolean"/>
        <xs:element name="AdminRoamControl" type="roamControlType"/>

        <!-- Profile creation type -->
        <!-- This is used to decide if the user can delete the profile or not  -->
        <!-- This is used to prioritize profiles when more than one are applicable  -->
        <xs:element name="ProfileCreationType" minOccurs="0">
          <xs:simpleType>
            <xs:restriction base="xs:token">
              <xs:enumeration value="UserProvisioned"/>
              <xs:enumeration value="AdminProvisioned"/>
              <xs:enumeration value="OperatorProvisioned"/>
              <xs:enumeration value="DeviceProvisioned"/>
            </xs:restriction>
          </xs:simpleType>
        </xs:element>
        
        <!-- extension point for other namespaces -->
        <xs:any namespace="##other" processContents="lax" minOccurs="0" maxOccurs="unbounded" />
      </xs:sequence>
    </xs:complexType>
  </xs:element>

</xs:schema>
```

 

 



