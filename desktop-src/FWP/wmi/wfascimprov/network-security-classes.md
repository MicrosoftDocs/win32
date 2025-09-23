---
title: WFasCim provider
description: The WFasCim provider exposes network security and filtering features.
ms.date: 05/17/2024
ms.assetid: 27B99B67-1872-4042-939B-8D3936391E05
ms.topic: reference
topic_type: 
- kbSyntax
api_name: 
api_type: 
api_location: 
---

# WFasCim provider

This section provides reference information for Windows Firewall and advanced security common information module (WFasCim) provider classes (for [Windows Management Instrumentation](/windows/win32/wmisdk/wmi-start-page)) defined in `WFasCim.mof`, and implemented in `WFasCim.dll`.

## In this section

| Topic | Description |
|-|-|
| [**MSFT_NetAddressFilter**](msft-netaddressfilter.md) | Represents a network address filter. |
| [**MSFT_NetApplicationFilter**](msft-netapplicationfilter.md) | Filters traffic based on which local application is sending or receiving the traffic. |
| [**MSFT_NetConSecRule**](msft-netconsecrule.md) | A Connection Security Rule. |
| [**MSFT_NetConSecRuleEMAuthSet**](msft-netconsecruleemauthset.md) | Relates a connection security rule to its Phase 2 Authentication Set. |
| [**MSFT_NetConSecRuleFilterByAddress**](msft-netconsecrulefilterbyaddress.md) | Filters a connection security rule by address. |
| [**MSFT_NetConSecRuleFilterByInterface**](msft-netconsecrulefilterbyinterface.md) | Filters a connection security rule by interface. |
| [**MSFT_NetConSecRuleFilterByInterfaceType**](msft-netconsecrulefilterbyinterfacetype.md) | Filters a connection security rule by interface type. |
| [**MSFT_NetConSecRuleFilterByProtocolPort**](msft-netconsecrulefilterbyprotocolport.md) | Filters a connection security rule by protocol or port. |
| [**MSFT_NetConSecRuleFilters**](msft-netconsecrulefilters.md) | Associates a connection security rule with its filters. Instances of this class can be traversed and the values in the associated filters can be modified, but instances of this class may not be created or deleted. |
| [**MSFT_NetConSecRuleInProfile**](msft-netconsecruleinprofile.md) | Indicates that a rule applies to a particular firewall profile. |
| [**MSFT_NetConSecRuleMMAuthSet**](msft-netconsecrulemmauthset.md) | Relates an IPsec rule to its Phase 1 Authentication Set. |
| [**MSFT_NetConSecRuleQMCryptoSet**](msft-netconsecruleqmcryptoset.md) | Relates a connection security rule to its Quick Mode Crypto Set. |
| [**MSFT_NetFirewallDynamicKeywordAddress**](msft-netfirewalldynamickeywordaddress.md) | Represents a Windows Defender Firewall dynamic keyword address. |
| [**MSFT_NetFirewallHyperVPort**](msft-netfirewallhypervport.md) | Represents a particular Windows Defender Firewall Hyper-V port. |
| [**MSFT_NetFirewallHyperVProfile**](msft-netfirewallhypervprofile.md) | Represents Windows Defender Firewall Hyper-V settings that are applicable to a VM Creator and profile type. |
| [**MSFT_NetFirewallHyperVRule**](msft-netfirewallhypervrule.md) | Represents a Windows Defender firewall Hyper-V rule. |
| [**MSFT_NetFirewallHyperVRulePortStatus**](msft-netfirewallhypervruleportstatus.md) | Represents the status of a firewall rule on a particular port. |
| [**MSFT_NetFirewallHyperVVMCreator**](msft-netfirewallhypervvmcreator.md) | Represents a particular Windows Defender Firewall Hyper-V VM Creator. |
| [**MSFT_NetFirewallHyperVVMSetting**](msft-netfirewallhypervvmsetting.md) | Represents Windows Defender Firewall Hyper-V settings for a VM type. |
| [**MSFT_NetFirewallProfile**](msft-netfirewallprofile.md) | Represents a particular firewall profile. Multiple profiles may be in effect on any interface at any given time. |
| [**MSFT_NetFirewallRule**](msft-netfirewallrule.md) | Represents a Windows firewall rule. |
| [**MSFT_NetFirewallRuleFilterByAddress**](msft-netfirewallrulefilterbyaddress.md) | Associates a FirewallRule to its AddressFilter. |
| [**MSFT_NetFirewallRuleFilterByApplication**](msft-netfirewallrulefilterbyapplication.md) | Filters a Windows firewall rule by application. |
| [**MSFT_NetFirewallRuleFilterByInterface**](msft-netfirewallrulefilterbyinterface.md) | Filters a Windows firewall rule by interface. |
| [**MSFT_NetFirewallRuleFilterByInterfaceType**](msft-netfirewallrulefilterbyinterfacetype.md) | Filters a Windows firewall rule by interface type. |
| [**MSFT_NetFirewallRuleFilterByProtocolPort**](msft-netfirewallrulefilterbyprotocolport.md) | Filters a Windows firewall rule by protocol or port. |
| [**MSFT_NetFirewallRuleFilterBySecurity**](msft-netfirewallrulefilterbysecurity.md) | Filters a Windows firewall rule by network layer security. |
| [**MSFT_NetFirewallRuleFilterByService**](msft-netfirewallrulefilterbyservice.md) | Filters a Windows firewall rule by Windows service. |
| [**MSFT_NetFirewallRuleFilters**](msft-netfirewallrulefilters.md) | Associates a firewall rule with its filters. Instances of this class can be traversed and the values in the associated filters can be modified, but instances of this class may not be created or deleted. |
| [**MSFT_NetFirewallRuleInProfile**](msft-netfirewallruleinprofile.md) | Associates a firewall rule with a profile that it is in. |
| [**MSFT_NetGPO**](msft-netgpo.md) | This class does not have any instances. It is used to manage locally-cached Group Policy Objects. |
| [**MSFT_NetIKEAuthProposal**](msft-netikeauthproposal.md) | Represents an auth proposal. |
| [**MSFT_NetIKEAuthSet**](msft-netikeauthset.md) | A list of auth suites, in preferential order, to use when negotiating an SA. |
| [**MSFT_NetIKEBasicAuthProposal**](msft-netikebasicauthproposal.md) | Represents an auth proposal. Instances of this class only exist as embedded instances within a MSFT_NetIKEP1AuthSet and MSFT_NetIKEP2AuthSet. |
| [**MSFT_NetIKECertAuthProposal**](msft-netikecertauthproposal.md) | Represents an auth proposal that uses certificates to authenticate the remote peer. Instances of this class only exist as embedded instances within a MSFT_NetIKEP1AuthSet and MSFT_NetIKEP2AuthSet. |
| [**MSFT_NetIKECryptoProposal**](msft-netikecryptoproposal.md) | Represents a suite of crypto algorithms to propose. |
| [**MSFT_NetIKECryptoSet**](msft-netikecryptoset.md) | A list of crypto suites, in preferential order, to use when negotiating an SA. |
| [**MSFT_NetIKEKerbAuthProposal**](msft-netikekerbauthproposal.md) | Represents an auth proposal for Kerberos. |
| [**MSFT_NetIKEMMCryptoProposal**](msft-netikemmcryptoproposal.md) | Represents a crypto suite to propose in main mode. |
| [**MSFT_NetIKEMMCryptoSet**](msft-netikemmcryptoset.md) | For a Main Mode or Connection Security rule, sets parameters for the main mode negotiation and describes the crypto proposals that should be negotiated. |
| [**MSFT_NetIKEP1AuthSet**](msft-netikep1authset.md) | A set of authentication proposals used in Phase 1 of authentication. |
| [**MSFT_NetIKEP2AuthSet**](msft-netikep2authset.md) | A set of authentication proposals that can be used in Phase 2 of authentication. |
| [**MSFT_NetIKEPSKAuthProposal**](msft-netikepskauthproposal.md) | A Pre-shared Key authentication proposal. |
| [**MSFT_NetIKEQMCryptoProposal**](msft-netikeqmcryptoproposal.md) | Represents a crypto suite to propose in quick mode. |
| [**MSFT_NetIKEQMCryptoSet**](msft-netikeqmcryptoset.md) | Specifies parameters for the quick mode negotiation as well as dictating the crypto sets that should be proposed during the exchange. |
| [**MSFT_NetInterfaceFilter**](msft-netinterfacefilter.md) | Filters traffic based on what interface it is sent or received on. |
| [**MSFT_NetInterfaceTypeFilter**](msft-netinterfacetypefilter.md) | Filters traffic based on the type of interface it is sent or received on. |
| [**MSFT_NetIPsecDoSPSetting**](msft-netipsecdospsetting.md) | Denial of Service Prevention Settings for IPsec. |
| [**MSFT_NetIPsecIdentity**](msft-netipsecidentity.md) | An identity used by IPsec |
| [**MSFT_NetMainModeRule**](msft-netmainmoderule.md) | A rule that alters the behavior of main-mode authentications. |
| [**MSFT_NetMainModeRuleFilterByAddress**](msft-netmainmoderulefilterbyaddress.md) | Filters a main mode rule by address. |
| [**MSFT_NetMainModeRuleFilters**](msft-netmainmoderulefilters.md) | Associates a main mode rule with its filters. Instances of this class can be traversed and the values in the associated filters can be modified, but instances of this class may not be created or deleted. |
| [**MSFT_NetMainModeRuleInProfile**](msft-netmainmoderuleinprofile.md) | Indicates that a rule applies to a particular firewall profile. |
| [**MSFT_NetMainModeRuleMMAuthSet**](msft-netmainmoderulemmauthset.md) | Relates a main mode rule to its Phase 1 Authentication Set. |
| [**MSFT_NetMainModeRuleMMCryptoSet**](msft-netmainmoderulemmcryptoset.md) | Relates a main mode rule to its Main Mode Crypto Set. |
| [**MSFT_NetMainModeSA**](msft-netmainmodesa.md) | A MainMode SA. |
| [**MSFT_NetNetworkLayerSecurityFilter**](msft-netnetworklayersecurityfilter.md) | Filters traffic based on certain high-level security constraints, like whether or not the traffic is encrypted. Connection Security rules will have to be created in order for traffic to pass the rule. |
| [**MSFT_NetPolicyRuleFilters**](msft-netpolicyrulefilters.md) | Associates a policy rule to its filters. |
| [**MSFT_NetProtocolPortFilter**](msft-netprotocolportfilter.md) | Filters traffic based on its protocol and port. |
| [**MSFT_NetQuickModeSA**](msft-netquickmodesa.md) | A Quick Mode SA. |
| [**MSFT_NetRuleInProfile**](msft-netruleinprofile.md) | Indicates that a rule applies to a particular firewall profile. |
| [**MSFT_NetSAActionInSARule**](msft-netsaactioninsarule.md) | Links an IPsec rule to its auth and crypto sets. |
| [**MSFT_NetSAAssociation**](msft-netsaassociation.md) | A MainMode SA. |
| [**MSFT_NetSARule**](msft-netsarule.md) | Represents an IPsec Rule. Subtypes differentiate between Connection Security Rules (MSFT_NetConSecRule) and Main Mode Rules (MSFT_NetMainModeRule). |
| [**MSFT_NetSARuleEMAuth**](msft-netsaruleemauth.md) | Relates an IPsec rule to its Phase 2 Authentication Set. |
| [**MSFT_NetSARuleMMAuth**](msft-netsarulemmauth.md) | Relates an IPsec rule to its Phase 1 Authentication Set. |
| [**MSFT_NetSARuleMMCrypto**](msft-netsarulemmcrypto.md) | Relates an IPsec rule to its Main Mode crypto set. |
| [**MSFT_NetSARuleQMCrypto**](msft-netsaruleqmcrypto.md) | Relates an IPsec rule to its Quick Mode crypto set. |
| [**MSFT_NetSecDeltaCollection**](msft-netsecdeltacollection.md) | IPSec policy delta |
| [**MSFT_NetSecuritySettingData**](msft-netsecuritysettingdata.md) | Global settings for IPsec. |
| [**MSFT_NetServiceFilter**](msft-netservicefilter.md) | Filters traffic based on which Windows service it is sent or received by. |
| [**MSFT_NetSettingData**](msft-netsettingdata-wfascim.md) | Serves as a base class for classes that provide access to network settings data, such as [**MSFT_NetIPsecDoSPSetting**](msft-netipsecdospsetting.md) and [**MSFT_NetSecuritySettingData**](msft-netsecuritysettingdata.md). |
