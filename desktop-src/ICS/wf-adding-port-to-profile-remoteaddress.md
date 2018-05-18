---
title: Adding a Port to Current Profile Using Remote Addresses
description: Adding a Port to Current Profile Using Remote Addresses
ms.assetid: '5b76c285-e15e-4a2d-b384-4d72edc37e0f'
keywords: ["Windows Firewall", "using"]
---

# Adding a Port to Current Profile Using Remote Addresses

This example shows adding a port to the current profile using RemoteAddresses to specify scope.


```VB
Option Explicit
On Error GoTo 0

'Set Constants
Const NET_FW_IP_PROTOCOL_UDP = 17
Const NET_FW_IP_PROTOCOL_TCP = 6

'Declare variables
Dim errornum

' Create the firewall manager object.
Dim fwMgr
Set fwMgr = CreateObject("HNetCfg.FwMgr")

' Get the current profile for the local firewall policy.
Dim profile
Set profile = fwMgr.LocalPolicy.CurrentProfile

Dim port
Set port = CreateObject("HNetCfg.FWOpenPort")

port.Name = "HTTP"
port.Protocol = NET_FW_IP_PROTOCOL_TCP
port.Port = 80

'If using RemoteAddresses, don't use Scope
' "*" means Scope of Any. Other entries are ignored if this is specified.
' "LocalSubnet" means Scope of Local Subnet. Can be used with other addresses as well. 
port.RemoteAddresses = "*"
'Use this line to scope the port to Local Subnet only
'port.RemoteAddresses = "LocalSubnet"
'Use this line to scope the port to the specific IP 10.1.1.1, the specific subnet 12.5.0.0, and Local Subnet. Don't put spaces.
'port.RemoteAddresses = "LocalSubnet,10.1.1.1/255.255.255.255,12.5.0.0/255.255.0.0"

port.Enabled = TRUE
'Use this line instead if you want to add the port, but disabled
'port.Enabled = FALSE

On Error Resume Next
profile.GloballyOpenPorts.Add port
errornum = Err.Number

If errornum <> 0 Then
    WScript.Echo("Adding the port failed. Error Number: " & errornum)
End If

```



 

 




