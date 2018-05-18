---
title: Turning the Firewall Off
description: This example turns off, or disables, the firewall using the Windows Firewall with Advanced Security APIs.
ms.assetid: 'e3945143-9ff4-449f-88db-72c1ab70bf52'
---

# Turning the Firewall Off

This example turns off, or disables, the firewall using the Windows Firewall with Advanced Security APIs.


```VB
'********************************************************************++
'THIS CODE AND INFORMATION IS PROVIDED "AS IS" WITHOUT WARRANTY OF
'ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING BUT NOT LIMITED
'TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS FOR A
'PARTICULAR PURPOSE.

'Copyright (C) Microsoft. All Rights Reserved.

'Abstract:
'    This VBScript file includes sample code that disables the 
'    firewall using the Microsoft Windows Firewall APIs.

'********************************************************************


option explicit
' Profile Type
Const NET_FW_PROFILE2_DOMAIN = 1
Const NET_FW_PROFILE2_PRIVATE = 2
Const NET_FW_PROFILE2_PUBLIC = 4

Dim fwPolicy2
Set fwPolicy2 = CreateObject("HNetCfg.FwPolicy2")
fwPolicy2.FirewallEnabled(NET_FW_PROFILE2_DOMAIN) = FALSE
fwPolicy2.FirewallEnabled(NET_FW_PROFILE2_PRIVATE) = FALSE
fwPolicy2.FirewallEnabled(NET_FW_PROFILE2_PUBLIC) = FALSE
```



 

 




