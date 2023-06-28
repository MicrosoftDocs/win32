---
title: globalFlags (LANPolicy) element
description: Contains the global settings for the automatic configuration of wired networks.
ms.topic: reference
ms.date: 06/24/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- globalFlags
api_type: 
- Schema
api_location: 
ms.assetid: 172cf15c-cd51-43d4-ae5d-f9460c2a40e2
---

# globalFlags (LANPolicy) element

The globalFlags (LANPolicy) element contains the global settings for the automatic configuration of wired networks.

```XSD
<xs:element name="globalFlags">
    <xs:complexType>
        <xs:sequence>
            <xs:element name="enableAutoConfig"
                type="boolean"
             />
            <xs:element name="enableExplicitCreds"
                minOccurs="0"
                type="boolean"
             />
            <xs:element name="blockPeriod"
                minOccurs="0"
             >
                <xs:simpleType>
                    <xs:restriction base="xs:integer">
                        <xs:minInclusive value="0">
                        <xs:maxInclusive value="60">
                    </xs:restriction>
                </xs:simpleType>
            </xs:element>
            <xs:any
                processContents="lax"
                minOccurs="0"
                maxOccurs="unbounded"
                namespace="##other"
             />
        </xs:sequence>
    </xs:complexType>
</xs:element>
```

## Parent elements

* [LANPolicy](./lan-policyschema-lanpolicy-element.md)

## Child elements

| Element | Type | Description |
| - | - | - |
| [**enableAutoConfig**](#enableautoconfig) | boolean | Specifies whether machines use the built-in automatic configuration service to manage connections to wired networks that require layer 2 authentication (such as 802.1X). |
| [**enableExplicitCreds**](#enableexplicitcreds) | boolean | A flag to indicate whether to disable explicit credentials. |
| [**blockPeriod**](#blockperiod) | | The value of the block timeout period. |

### enableAutoConfig

The **enableAutoConfig** (globalFlags) element specifies whether machines use the built-in automatic configuration service to manage connections to wired networks that require layer 2 authentication (such as 802.1X).

When **enableAutoConfig** has a value of FALSE, machines must not use built-in automatic configuration service to manage connections that require layer 2 authentication. Instead, the network specified in the [**profileList**](./lan-policyschema-lanpolicy-element.md#profilelist) element is the only network available for connection. The automatic configuration service will only respond to requests to enable the service.

When **enableAutoConfig** has a value of TRUE, machines may use the built-in automatic configuration service to connect to wired networks that require layer 2 authentication.

### enableExplicitCreds

A flag to indicate whether to disable explicit credentials.

The target namespace for the **enableExplicitCreds** element is `https://www.microsoft.com/networking/LAN/policy/v2`.

### blockPeriod

The value of the block timeout period. The default value is 20 minutes when the element isn't present.

The target namespace for the **blockPeriod** element is `https://www.microsoft.com/networking/LAN/policy/v2`.

## Requirements

| Requirement | Value |
| - | - |
| Minimum supported client | Windows Vista \[desktop apps only\] |
| Minimum supported server | Windows Server 2008 \[desktop apps only\] |
