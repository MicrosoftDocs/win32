---
title: Displaying all Properties
description: Displaying all Properties
ms.assetid: 49a292e6-f94e-4de1-9071-aa6d01e9ad45
keywords:
- Displaying all Properties
- using
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Displaying all Properties

The following code example displays all properties of the current Windows Firewall profile.


```VB

Option Explicit

' Define Constants from the SDK and their associated string name
' Scope
Const NET_FW_SCOPE_ALL = 0
Const NET_FW_SCOPE_ALL_NAME = "All subnets"
Const NET_FW_SCOPE_LOCAL_SUBNET = 1
Const NET_FW_SCOPE_LOCAL_SUBNET_NAME = "Local subnet only"
Const NET_FW_SCOPE_CUSTOM = 2
Const NET_FW_SCOPE_CUSTOM_NAME = "Custom Scope (see RemoteAddresses)"

' Profile Type
Const NET_FW_PROFILE_DOMAIN = 0
Const NET_FW_PROFILE_DOMAIN_NAME = "Domain"
Const NET_FW_PROFILE_STANDARD = 1
Const NET_FW_PROFILE_STANDARD_NAME = "Standard"

' IP Version
Const NET_FW_IP_VERSION_V4 = 0
Const NET_FW_IP_VERSION_V4_NAME = "IPv4"
Const NET_FW_IP_VERSION_V6 = 1
Const NET_FW_IP_VERSION_V6_NAME = "IPv6"
Const NET_FW_IP_VERSION_ANY = 2
Const NET_FW_IP_VERSION_ANY_NAME = "ANY"

' Protocol
Const NET_FW_IP_PROTOCOL_TCP = 6
Const NET_FW_IP_PROTOCOL_TCP_NAME = "TCP"
Const NET_FW_IP_PROTOCOL_UDP = 17
Const NET_FW_IP_PROTOCOL_UDP_NAME = "UDP"


' Create the firewall manager object.
Dim fwMgr
Set fwMgr = CreateObject("HNetCfg.FwMgr")

' Get the current profile for the local firewall policy.
Dim profile
Set profile = fwMgr.LocalPolicy.CurrentProfile

dim msgOut

msgOut = vbCrLf & "Dumping local firewall profile ..."

' Print the Profile information
Select Case profile.Type
  Case NET_FW_PROFILE_DOMAIN msgOut = msgOut & "Type: " & _
    NET_FW_PROFILE_DOMAIN_NAME & vbcrlf
  Case NET_FW_PROFILE_STANDARD msgOut = msgOut & "Type: " & _
    NET_FW_PROFILE_STANDARD_NAME  & vbcrlf
End Select


WScript.Echo(msgOut)

msgOut = "Firewall Enabled: " & profile.FirewallEnabled & vbCrLf
msgOut = msgOut & "Exceptions Not Allowed: " & _
  profile.ExceptionsNotAllowed & vbCrLf
msgOut = msgOut & "Notifications Disabled: " & _
  profile.NotificationsDisabled & vbCrLf
msgOut = msgOut & "UnicastResponsestoMulticastBroadcastDisabled: " &  _
  profile.UnicastResponsestoMulticastBroadcastDisabled & vbCrLf

WScript.Echo(msgOut)

' Print the Remote Admin settings.
Dim RASettings
Set RASettings = profile.RemoteAdminSettings

msgOut = "Remote Administration Enabled: " & RASettings.Enabled & vbCrLf

Select Case RASettings.IpVersion
    Case NET_FW_IP_VERSION_V4 msgOut = msgOut & _
      "Remote Administration IP Version: " &  _
      NET_FW_IP_VERSION_V4_NAME & vbCrLf
    Case NET_FW_IP_VERSION_V6 msgOut = msgOut & _
      "Remote Administration IP Version: " &  _ 
      NET_FW_IP_VERSION_V6_NAME & vbCrLf
    Case NET_FW_IP_VERSION_ANY msgOut = msgOut & _
      "Remote Administration IP Version: " &  _
      NET_FW_IP_VERSION_ANY_NAME & vbCrLf
End Select

Select Case RASettings.Scope
    Case NET_FW_SCOPE_ALL msgOut = msgOut & _
      "Remote Administration Scope: " &  _
      NET_FW_SCOPE_ALL_NAME & vbCrLf
    Case NET_FW_SCOPE_LOCAL_SUBNET msgOut = msgOut & _
      "Remote Administration Scope: " &  _
      NET_FW_SCOPE_LOCAL_SUBNET_NAME & vbCrLf
    Case NET_FW_SCOPE_CUSTOM msgOut = msgOut & _
      "Remote Administration Scope: " &  _
      NET_FW_SCOPE_CUSTOM_NAME & vbCrLf
End Select

msgOut = msgOut & "Remote Administration RemoteAddresses: " &  _
  RASettings.RemoteAddresses & vbCrLf

WScript.Echo( msgOut & vbCrLf)


' Print the ICMP Settings.
Dim icmpSettings
Set icmpSettings = profile.IcmpSettings
msgOut = "ICMP Settings:" & vbCrLf
msgOut = msgOut & "  AllowOutboundDestinationUnreachable: " & _
  icmpSettings.AllowOutboundDestinationUnreachable & vbCrLf
msgOut = msgOut & "  AllowOutboundSourceQuench:           " & _
  icmpSettings.AllowOutboundSourceQuench & vbCrLf
msgOut = msgOut & "  AllowRedirect:                       " & _
  icmpSettings.AllowRedirect & vbCrLf
msgOut = msgOut & "  AllowInboundEchoRequest:             " & _
  icmpSettings.AllowInboundEchoRequest & vbCrLf
msgOut = msgOut & "  AllowInboundRouterRequest:           " & _
  icmpSettings.AllowInboundRouterRequest & vbCrLf
msgOut = msgOut & "  AllowOutboundTimeExceeded:           " & _
  icmpSettings.AllowOutboundTimeExceeded & vbCrLf
msgOut = msgOut & "  AllowOutboundParameterProblem:       " & _
  icmpSettings.AllowOutboundParameterProblem & vbCrLf
msgOut = msgOut & "  AllowInboundTimestampRequest:        " & _
  icmpSettings.AllowInboundTimestampRequest & vbCrLf
msgOut = msgOut & "  AllowInboundMaskRequest:             " & _
  icmpSettings.AllowInboundMaskRequest & vbCrLf

WScript.Echo( msgOut & vbCrLf)

' Print all the globally open ports.
msgOut = "Globally Open Ports: " & profile.GloballyOpenPorts.Count & vbCrLf
WScript.Echo( msgOut )
msgOut = ""

Dim port

For Each port In profile.GloballyOpenPorts

    msgOut = msgOut & "  Name:               " & port.Name & vbCrLf
    msgOut = msgOut & "  Port Number:        " & port.Port & vbCrLf

    Select Case port.Protocol
        Case NET_FW_IP_PROTOCOL_TCP msgOut = msgOut & _
          "  IP Protocol:        " &  NET_FW_IP_PROTOCOL_TCP_NAME & vbCrLf
        Case NET_FW_IP_PROTOCOL_UDP msgOut = msgOut & _
          "  IP Protocol:        " &  NET_FW_IP_PROTOCOL_UDP_NAME & vbCrLf
    End Select

    msgOut = msgOut & "  BuiltIn:            " & port.BuiltIn & vbCrLf

    Select Case port.IpVersion
        Case NET_FW_IP_VERSION_V4 msgOut = msgOut & _
          "  IP Version:         " &  NET_FW_IP_VERSION_V4_NAME & vbCrLf
        Case NET_FW_IP_VERSION_V6 msgOut = msgOut & _
          "  IP Version:         " &  NET_FW_IP_VERSION_V6_NAME & vbCrLf
        Case NET_FW_IP_VERSION_ANY msgOut = msgOut & _
          "  IP Version:         " &  NET_FW_IP_VERSION_ANY_NAME & vbCrLf
    End Select

    Select Case port.Scope
        Case NET_FW_SCOPE_ALL msgOut = msgOut & _
          "  Scope:              " &  NET_FW_SCOPE_ALL_NAME & vbCrLf
        Case NET_FW_SCOPE_LOCAL_SUBNET msgOut = msgOut & _
          "  Scope:              " &  NET_FW_SCOPE_LOCAL_SUBNET_NAME & vbCrLf
        Case NET_FW_SCOPE_CUSTOM msgOut = msgOut & _
          "  Scope:              " &  NET_FW_SCOPE_CUSTOM_NAME & vbCrLf
    End Select

    msgOut = msgOut & "  RemoteAddresses:    " & _
      port.RemoteAddresses & vbCrLf
    msgOut = msgOut & "  Enabled:            " & _
      port.Enabled & vbCrLf & vbCrLf

  WScript.Echo( msgOut )

  msgOut = ""
Next



' Print all the services
msgOut = "Services: " & profile.Services.Count & vbCrLf
WScript.Echo( msgOut )
msgOut = ""

Dim service

For Each service In profile.Services

  msgOut = msgOut & "  Name:                " & _
         service.Name & vbCrLf
    msgOut = msgOut & "  Type:                " & _
         service.Type & vbCrLf
    msgOut = msgOut & "  Customized:          " & _
         service.Customized & vbCrLf

    Select Case service.IpVersion
        Case NET_FW_IP_VERSION_V4 msgOut = msgOut & _
              "  IP Version:          " &  NET_FW_IP_VERSION_V4_NAME & vbCrLf
        Case NET_FW_IP_VERSION_V6 msgOut = msgOut & _
              "  IP Version:          " &  NET_FW_IP_VERSION_V6_NAME & vbCrLf
        Case NET_FW_IP_VERSION_ANY msgOut = msgOut & _
              "  IP Version:          " &  NET_FW_IP_VERSION_ANY_NAME & vbCrLf
    End Select

    Select Case service.Scope
        Case NET_FW_SCOPE_ALL msgOut = msgOut & _
              "  Scope:              " &  NET_FW_SCOPE_ALL_NAME & vbCrLf
        Case NET_FW_SCOPE_LOCAL_SUBNET msgOut = msgOut & _
              "  Scope:              " &  NET_FW_SCOPE_LOCAL_SUBNET_NAME & vbCrLf
        Case NET_FW_SCOPE_CUSTOM msgOut = msgOut & _
              "  Scope:              " &  NET_FW_SCOPE_CUSTOM_NAME & vbCrLf
    End Select

    msgOut = msgOut & "  RemoteAddresses:     " & _
         service.RemoteAddresses & vbCrLf
    msgOut = msgOut & "  Enabled:             " & _
         service.Enabled & vbCrLf

  WScript.Echo( msgOut )
  msgOut = ""

      'Display header for Service Ports list
  msgOut = msgOut & "Service: " & service.Name & " Globally Open Ports: " & _
    service.GloballyOpenPorts.Count & vbCrLf


    For Each port In service.GloballyOpenPorts

      msgOut = msgOut & "    Name:               " & _
        port.Name & vbCrLf
      msgOut = msgOut & "    Port Number:        " & _
        port.Port & vbCrLf

      Select Case port.Protocol
        Case NET_FW_IP_PROTOCOL_TCP msgOut = msgOut & _
          "    IP Protocol:        " &  NET_FW_IP_PROTOCOL_TCP_NAME & vbCrLf
        Case NET_FW_IP_PROTOCOL_UDP msgOut = msgOut & _
                         "    IP Protocol:        " &  NET_FW_IP_PROTOCOL_UDP_NAME & vbCrLf
      End Select

      msgOut = msgOut & "    BuiltIn:            " & port.BuiltIn & vbCrLf

      Select Case port.IpVersion
        Case NET_FW_IP_VERSION_V4 msgOut = msgOut & _
                         "    IP Version:         " &  NET_FW_IP_VERSION_V4_NAME & vbCrLf
        Case NET_FW_IP_VERSION_V6 msgOut = msgOut & _
                         "    IP Version:         " &  NET_FW_IP_VERSION_V6_NAME & vbCrLf
        Case NET_FW_IP_VERSION_ANY msgOut = msgOut & _
                         "    IP Version:         " &  NET_FW_IP_VERSION_ANY_NAME & vbCrLf
      End Select

      Select Case port.Scope
        Case NET_FW_SCOPE_ALL msgOut = msgOut & _
                         "    Scope:              " &  NET_FW_SCOPE_ALL_NAME & vbCrLf
        Case NET_FW_SCOPE_LOCAL_SUBNET msgOut = msgOut & _
                         "    Scope:              "  & NET_FW_SCOPE_LOCAL_SUBNET_NAME & vbCrLf
        Case NET_FW_SCOPE_CUSTOM msgOut = msgOut & _
                         "    Scope:              " &  NET_FW_SCOPE_CUSTOM_NAME & vbCrLf
      End Select

      msgOut = msgOut & "    RemoteAddresses:    " & _
        port.RemoteAddresses & vbCrLf
      msgOut = msgOut & "    Enabled:            " & _
        port.Enabled & vbCrLf & vbCrLf

    Next
     
    WScript.Echo( msgOut )

    msgOut = ""
Next


' Print all the authorized applications
msgOut = "Authorized Applications: " & _
    profile.AuthorizedApplications.Count & vbCrLf

Dim app
For Each app In profile.AuthorizedApplications
    msgOut = msgOut & "  Name:               " & _
         app.Name & vbCrLf
    msgOut = msgOut & "  Image Filename      " & _
         app.ProcessImageFileName & vbCrLf

    Select Case app.IpVersion
        Case NET_FW_IP_VERSION_V4 msgOut = msgOut & _
              "  IP Version:         " &  NET_FW_IP_VERSION_V4_NAME & vbCrLf
        Case NET_FW_IP_VERSION_V6 msgOut = msgOut & _
              "  IP Version:         " &  NET_FW_IP_VERSION_V6_NAME & vbCrLf
        Case NET_FW_IP_VERSION_ANY msgOut = msgOut & _
              "  IP Version:         " &  NET_FW_IP_VERSION_ANY_NAME & vbCrLf
    End Select

    Select Case app.Scope
        Case NET_FW_SCOPE_ALL msgOut = msgOut & _
              "  Scope:              " &  NET_FW_SCOPE_ALL_NAME & vbCrLf
        Case NET_FW_SCOPE_LOCAL_SUBNET msgOut = msgOut & _
              "  Scope:              " _
            &  NET_FW_SCOPE_LOCAL_SUBNET_NAME & vbCrLf
        Case NET_FW_SCOPE_CUSTOM msgOut = msgOut & _
              "  Scope:              " &  NET_FW_SCOPE_CUSTOM_NAME & vbCrLf
    End Select

    msgOut = msgOut & "  RemoteAddresses:    " & _
         app.RemoteAddresses & vbCrLf
    msgOut = msgOut & "  Enabled:            " & _
         app.Enabled & vbCrLf

    WScript.Echo( msgOut )

    msgOut = ""
Next



WScript.echo ("The End")

```



 

 




