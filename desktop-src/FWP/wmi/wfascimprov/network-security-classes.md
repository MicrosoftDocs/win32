---
title: WFasCim provider
Description: The WFasCim provider exposes network security and filtering features.
ms.date: 05/07/2024
ms.assetid: 27B99B67-1872-4042-939B-8D3936391E05


ms.author: windowssdkdev
ms.topic: article
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
| [**MSFT_NetAddressFilter**](msft-netaddressfilter.md)<br/> | Represents a network address filter.<br/> |
| [**MSFT_NetApplicationFilter**](msft-netapplicationfilter.md)<br/> | Filters traffic based on which local application is sending or receiving the traffic.<br/> |
| [**MSFT_NetConSecRule**](msft-netconsecrule.md)<br/> | A Connection Security Rule.<br/> |
| [**MSFT_NetConSecRuleEMAuthSet**](msft-netconsecruleemauthset.md)<br/> | Relates a connection security rule to its Phase 2 Authentication Set.<br/> |
| [**MSFT_NetConSecRuleFilterByAddress**](msft-netconsecrulefilterbyaddress.md)<br/> | Filters a connection security rule by address.<br/> |
| [**MSFT_NetConSecRuleFilterByInterface**](msft-netconsecrulefilterbyinterface.md)<br/> | Filters a connection security rule by interface.<br/> |
| [**MSFT_NetConSecRuleFilterByInterfaceType**](msft-netconsecrulefilterbyinterfacetype.md)<br/> | Filters a connection security rule by interface type.<br/> |
| [**MSFT_NetConSecRuleFilterByProtocolPort**](msft-netconsecrulefilterbyprotocolport.md)<br/> | Filters a connection security rule by protocol or port.<br/> |
| [**MSFT_NetConSecRuleFilters**](msft-netconsecrulefilters.md)<br/> | Associates a connection security rule with its filters. Instances of this class can be traversed and the values in the associated filters can be modified, but instances of this class may not be created or deleted.<br/> |
| [**MSFT_NetConSecRuleInProfile**](msft-netconsecruleinprofile.md)<br/> | Indicates that a rule applies to a particular firewall profile.<br/> |
| [**MSFT_NetConSecRuleMMAuthSet**](msft-netconsecrulemmauthset.md)<br/> | Relates an IPsec rule to its Phase 1 Authentication Set.<br/> |
| [**MSFT_NetConSecRuleQMCryptoSet**](msft-netconsecruleqmcryptoset.md)<br/> | Relates a connection security rule to its Quick Mode Crypto Set.<br/> |
| [**MSFT_NetFirewallProfile**](msft-netfirewallprofile.md)<br/> | Represents a particular firewall profile. Multiple profiles may be in effect on any interface at any given time.<br/> |
| [**MSFT_NetFirewallRule**](msft-netfirewallrule.md)<br/> | Represents a Windows firewall rule.<br/> |
| [**MSFT_NetFirewallRuleFilterByAddress**](msft-netfirewallrulefilterbyaddress.md)<br/> | Associates a FirewallRule to its AddressFilter.<br/> |
| [**MSFT_NetFirewallRuleFilterByApplication**](msft-netfirewallrulefilterbyapplication.md)<br/> | Filters a Windows firewall rule by application.<br/> |
| [**MSFT_NetFirewallRuleFilterByInterface**](msft-netfirewallrulefilterbyinterface.md)<br/> | Filters a Windows firewall rule by interface.<br/> |
| [**MSFT_NetFirewallRuleFilterByInterfaceType**](msft-netfirewallrulefilterbyinterfacetype.md)<br/> | Filters a Windows firewall rule by interface type.<br/> |
| [**MSFT_NetFirewallRuleFilterByProtocolPort**](msft-netfirewallrulefilterbyprotocolport.md)<br/> | Filters a Windows firewall rule by protocol or port.<br/> |
| [**MSFT_NetFirewallRuleFilterBySecurity**](msft-netfirewallrulefilterbysecurity.md)<br/> | Filters a Windows firewall rule by network layer security.<br/> |
| [**MSFT_NetFirewallRuleFilterByService**](msft-netfirewallrulefilterbyservice.md)<br/> | Filters a Windows firewall rule by Windows service.<br/> |
| [**MSFT_NetFirewallRuleFilters**](msft-netfirewallrulefilters.md)<br/> | Associates a firewall rule with its filters. Instances of this class can be traversed and the values in the associated filters can be modified, but instances of this class may not be created or deleted.<br/> |
| [**MSFT_NetFirewallRuleInProfile**](msft-netfirewallruleinprofile.md)<br/> | Associates a firewall rule with a profile that it is in.<br/> |
| [**MSFT_NetGPO**](msft-netgpo.md)<br/> | This class does not have any instances. It is used to manage locally-cached Group Policy Objects.<br/> |
| [**MSFT_NetIKEAuthProposal**](msft-netikeauthproposal.md)<br/> | Represents an auth proposal.<br/> |
| [**MSFT_NetIKEAuthSet**](msft-netikeauthset.md)<br/> | A list of auth suites, in preferential order, to use when negotiating an SA.<br/> |
| [**MSFT_NetIKEBasicAuthProposal**](msft-netikebasicauthproposal.md)<br/> | Represents an auth proposal. Instances of this class only exist as embedded instances within a MSFT_NetIKEP1AuthSet and MSFT_NetIKEP2AuthSet.<br/> |
| [**MSFT_NetIKECertAuthProposal**](msft-netikecertauthproposal.md)<br/> | Represents an auth proposal that uses certificates to authenticate the remote peer. Instances of this class only exist as embedded instances within a MSFT_NetIKEP1AuthSet and MSFT_NetIKEP2AuthSet.<br/> |
| [**MSFT_NetIKECryptoProposal**](msft-netikecryptoproposal.md)<br/> | Represents a suite of crypto algorithms to propose.<br/> |
| [**MSFT_NetIKECryptoSet**](msft-netikecryptoset.md)<br/> | A list of crypto suites, in preferential order, to use when negotiating an SA.<br/> |
| [**MSFT_NetIKEKerbAuthProposal**](msft-netikekerbauthproposal.md)<br/> | Represents an auth proposal for Kerberos.<br/> |
| [**MSFT_NetIKEMMCryptoProposal**](msft-netikemmcryptoproposal.md)<br/> | Represents a crypto suite to propose in main mode.<br/> |
| [**MSFT_NetIKEMMCryptoSet**](msft-netikemmcryptoset.md)<br/> | For a Main Mode or Connection Security rule, sets parameters for the main mode negotiation and describes the crypto proposals that should be negotiated.<br/> |
| [**MSFT_NetIKEP1AuthSet**](msft-netikep1authset.md)<br/> | A set of authentication proposals used in Phase 1 of authentication.<br/> |
| [**MSFT_NetIKEP2AuthSet**](msft-netikep2authset.md)<br/> | A set of authentication proposals that can be used in Phase 2 of authentication.<br/> |
| [**MSFT_NetIKEPSKAuthProposal**](msft-netikepskauthproposal.md)<br/> | A Pre-shared Key authentication proposal.<br/> |
| [**MSFT_NetIKEQMCryptoProposal**](msft-netikeqmcryptoproposal.md)<br/> | Represents a crypto suite to propose in quick mode.<br/> |
| [**MSFT_NetIKEQMCryptoSet**](msft-netikeqmcryptoset.md)<br/> | Specifies parameters for the quick mode negotiation as well as dictating the crypto sets that should be proposed during the exchange.<br/> |
| [**MSFT_NetInterfaceFilter**](msft-netinterfacefilter.md)<br/> | Filters traffic based on what interface it is sent or received on.<br/> |
| [**MSFT_NetInterfaceTypeFilter**](msft-netinterfacetypefilter.md)<br/> | Filters traffic based on the type of interface it is sent or received on.<br/> |
| [**MSFT_NetIPsecDoSPSetting**](msft-netipsecdospsetting.md)<br/> | Denial of Service Prevention Settings for IPsec.<br/> |
| [**MSFT_NetIPsecIdentity**](msft-netipsecidentity.md)<br/> | An identity used by IPsec<br/> |
| [**MSFT_NetMainModeRule**](msft-netmainmoderule.md)<br/> | A rule that alters the behavior of main-mode authentications.<br/> |
| [**MSFT_NetMainModeRuleFilterByAddress**](msft-netmainmoderulefilterbyaddress.md)<br/> | Filters a main mode rule by address.<br/> |
| [**MSFT_NetMainModeRuleFilters**](msft-netmainmoderulefilters.md)<br/> | Associates a main mode rule with its filters. Instances of this class can be traversed and the values in the associated filters can be modified, but instances of this class may not be created or deleted.<br/> |
| [**MSFT_NetMainModeRuleInProfile**](msft-netmainmoderuleinprofile.md)<br/> | Indicates that a rule applies to a particular firewall profile.<br/> |
| [**MSFT_NetMainModeRuleMMAuthSet**](msft-netmainmoderulemmauthset.md)<br/> | Relates a main mode rule to its Phase 1 Authentication Set.<br/> |
| [**MSFT_NetMainModeRuleMMCryptoSet**](msft-netmainmoderulemmcryptoset.md)<br/> | Relates a main mode rule to its Main Mode Crypto Set.<br/> |
| [**MSFT_NetMainModeSA**](msft-netmainmodesa.md)<br/> | A MainMode SA.<br/> |
| [**MSFT_NetNetworkLayerSecurityFilter**](msft-netnetworklayersecurityfilter.md)<br/> | Filters traffic based on certain high-level security constraints, like whether or not the traffic is encrypted. Connection Security rules will have to be created in order for traffic to pass the rule.<br/> |
| [**MSFT_NetPolicyRuleFilters**](msft-netpolicyrulefilters.md)<br/> | Associates a policy rule to its filters.<br/> |
| [**MSFT_NetProtocolPortFilter**](msft-netprotocolportfilter.md)<br/> | Filters traffic based on its protocol and port.<br/> |
| [**MSFT_NetQuickModeSA**](msft-netquickmodesa.md)<br/> | A Quick Mode SA.<br/> |
| [**MSFT_NetRuleInProfile**](msft-netruleinprofile.md)<br/> | Indicates that a rule applies to a particular firewall profile.<br/> |
| [**MSFT_NetSAActionInSARule**](msft-netsaactioninsarule.md)<br/> | Links an IPsec rule to its auth and crypto sets.<br/> |
| [**MSFT_NetSAAssociation**](msft-netsaassociation.md)<br/> | A MainMode SA.<br/> |
| [**MSFT_NetSARule**](msft-netsarule.md)<br/> | Represents an IPsec Rule. Subtypes differentiate between Connection Security Rules (MSFT_NetConSecRule) and Main Mode Rules (MSFT_NetMainModeRule).<br/> |
| [**MSFT_NetSARuleEMAuth**](msft-netsaruleemauth.md)<br/> | Relates an IPsec rule to its Phase 2 Authentication Set.<br/> |
| [**MSFT_NetSARuleMMAuth**](msft-netsarulemmauth.md)<br/> | Relates an IPsec rule to its Phase 1 Authentication Set.<br/> |
| [**MSFT_NetSARuleMMCrypto**](msft-netsarulemmcrypto.md)<br/> | Relates an IPsec rule to its Main Mode crypto set.<br/> |
| [**MSFT_NetSARuleQMCrypto**](msft-netsaruleqmcrypto.md)<br/> | Relates an IPsec rule to its Quick Mode crypto set.<br/> |
| [**MSFT_NetSecDeltaCollection**](msft-netsecdeltacollection.md)<br/> | IPSec policy delta<br/> |
| [**MSFT_NetSecuritySettingData**](msft-netsecuritysettingdata.md)<br/> | Global settings for IPsec.<br/> |
| [**MSFT_NetServiceFilter**](msft-netservicefilter.md)<br/> | Filters traffic based on which Windows service it is sent or received by.<br/> |
| [**MSFT_NetSettingData**](msft-netsettingdata-wfascim.md)<br/> | Serves as a base class for classes that provice access to network settings data, such as [**MSFT_NetIPsecDoSPSetting**](msft-netipsecdospsetting.md) and [**MSFT_NetSecuritySettingData**](msft-netsecuritysettingdata.md).<br/> |
