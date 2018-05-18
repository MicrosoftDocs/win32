---
title: Adding a Protocol Rule
description: This example adds a Generic Routing Encapsulation (GRE) protocol rule using the Windows Firewall with Advanced Security APIs.VB' This VBScript file includes sample code that adds a ' Generic Routing Encapsulation (GRE) protocol rule ' using the Microsoft Windows Firewall APIs. option explicit Dim CurrentProfiles 'Action Const NET\_FW\_ACTION\_ALLOW 1 ' Create the FwPolicy2 object. Dim fwPolicy2 Set fwPolicy2 CreateObject( \ 0034;HNetCfg.FwPolicy2 \ 0034;) ' Get the Rules object Dim RulesObject Set RulesObject fwPolicy2.Rules CurrentProfiles fwPolicy2.CurrentProfileTypes 'Create a Rule Object. Dim NewRule Set NewRule CreateObject( \ 0034;HNetCfg.FWRule \ 0034;) NewRule.Name \ 0034;GRE\_RULE \ 0034; NewRule.Description \ 0034;Allow GRE Traffic \ 0034; NewRule.Protocol 47 NewRule.Enabled TRUE NewRule.Grouping \ 0034; firewallapi.dll,-23255 \ 0034; NewRule.Profiles CurrentProfiles NewRule.Action NET\_FW\_ACTION\_ALLOW 'Add a new rule RulesObject.Add NewRule
ms.assetid: '76c40fe0-67cb-4e60-b053-77ec5b80c35b'
---

# Adding a Protocol Rule

This example adds a Generic Routing Encapsulation (GRE) protocol rule using the Windows Firewall with Advanced Security APIs.


```VB
'  This VBScript file includes sample code that adds a
'  Generic Routing Encapsulation (GRE) protocol rule 
'  using the Microsoft Windows Firewall APIs.


option explicit

Dim CurrentProfiles

'Action
Const NET_FW_ACTION_ALLOW = 1

' Create the FwPolicy2 object.
Dim fwPolicy2
Set fwPolicy2 = CreateObject("HNetCfg.FwPolicy2")

' Get the Rules object
Dim RulesObject
Set RulesObject = fwPolicy2.Rules

CurrentProfiles = fwPolicy2.CurrentProfileTypes

'Create a Rule Object.
Dim NewRule
Set NewRule = CreateObject("HNetCfg.FWRule")
    
NewRule.Name = "GRE_RULE"
NewRule.Description = "Allow GRE Traffic"
NewRule.Protocol = 47
NewRule.Enabled = TRUE
NewRule.Grouping = "@firewallapi.dll,-23255"
NewRule.Profiles = CurrentProfiles
NewRule.Action = NET_FW_ACTION_ALLOW
    
'Add a new rule
RulesObject.Add NewRule
```



 

 




