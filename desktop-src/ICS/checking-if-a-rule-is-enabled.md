---
title: Checking if a Rule is Enabled
description: This example checks if the rule group is enabled in the current profile using the Windows Firewall with Advanced Security APIs.
ms.assetid: '7bf055ee-e8f6-4083-9599-c96ddf811923'
---

# Checking if a Rule is Enabled

This example checks if the rule group is enabled in the current profile using the Windows Firewall with Advanced Security APIs.


```VB
'  This VBScript file includes sample code that checks if the 
'  rule group is enabled in the current profile using the 
'  Microsoft Windows Firewall APIs.


Option Explicit

' Profile Type
Const NET_FW_MODIFY_STATE_OK = 0
Const NET_FW_MODIFY_STATE_GP_OVERRIDE = 1
Const NET_FW_MODIFY_STATE_NO_EXCEPTIONS = 2

' Create the FwPolicy2 object
Dim fwPolicy2
Set fwPolicy2 = CreateObject("HNetCfg.FwPolicy2")

Dim bIsEnabled
bIsEnabled = fwPolicy2.IsRuleGroupCurrentlyEnabled("File and Printer Sharing")

if bIsEnabled then
    WScript.Echo("File and Printer Sharing is currently enabled on at least one of the current profiles")
else
    WScript.Echo("File and Printer Sharing is currently not enabled on any of the current profiles")
end if
 
Dim PolicyModifyState
PolicyModifyState = fwPolicy2.LocalPolicyModifyState 

Select Case PolicyModifyState 
   Case NET_FW_MODIFY_STATE_OK            WScript.Echo("Changing or adding a firewall rule (or group) will take effect on at least one of the current profiles.")
   Case NET_FW_MODIFY_STATE_GP_OVERRIDE   WScript.Echo("Changing or adding a firewall rule (or group) to the current profiles will not take effect because group policy overrides it on at least one of the current profiles.")
   Case NET_FW_MODIFY_STATE_INBOUND_BLOCKED WScript.Echo("Changing or adding an inbound firewall rule (or group) to the current profiles will not take effect because inbound rules are not allowed on at least one of the current profiles.")
   Case ELSE                              WScript.Echo("Invalid Modify State returned by LocalPolicyModifyState.")
End Select
```



 

 




