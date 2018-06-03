---
title: Allowing Incoming Echo Requests
description: Allowing Incoming Echo Requests
ms.assetid: 353fd3da-2885-40e5-8241-2971b6a26554
keywords:
- Windows Firewall
- using
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Allowing Incoming Echo Requests

This example shows how to allow incoming echo requests.


```VB
' Open up ICMP type 8 in the firewall (Allow Incoming Echo Requests)

Option Explicit

'Declare variables
' Create the firewall manager object.
Dim fwMgr
Set fwMgr = CreateObject("HNetCfg.FwMgr")

' Get the current profile for the local firewall policy.
Dim profile
Set profile = fwMgr.LocalPolicy.CurrentProfile

profile.IcmpSettings.AllowInboundEchoRequest = TRUE

'Use this line if you want to disable the setting.
'profile.IcmpSettings.AllowInboundEchoRequest = FALSE


```



 

 




