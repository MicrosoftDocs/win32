---
title: Enumerating Remote Nodes
description: This example demonstrates enumerating remote nodes on a Network Load Balancing (NLB) cluster.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 092c14fd-d584-4d54-8ebc-8127fc56eba7
ms.prod: windows-server-dev
ms.technology:
- network-load-balancing
- windows-management-instrumentation
ms.tgt_platform: multiple
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Enumerating Remote Nodes

This example demonstrates enumerating remote nodes on a Network Load Balancing (NLB) cluster.


```VB
strComputer = "."
Set objWMIService = GetObject("winmgmts:\\" & strComputer & "\root\MicrosoftNLB")
Wscript.Echo ""
Wscript.Echo ""
Wscript.Echo "MicrosoftNLB_Node"
Wscript.Echo "================="
Wscript.Echo ""
Set objWMIService = GetObject("winmgmts:\\" & strComputer & "\root\MicrosoftNLB")
Set colItems = objWMIService.ExecQuery("Select * from MicrosoftNLB_Node",,48)
For Each objItem in colItems
  Wscript.Echo "ComputerName:       " & objItem.ComputerName
  Wscript.Echo "CreationClassName:  " & objItem.CreationClassName
  Wscript.Echo "DedicatedIPAddress: " & objItem.DedicatedIPAddress
  Wscript.Echo "HostPriority:       " & objItem.HostPriority
  Wscript.Echo "Name:               " & objItem.Name
  Wscript.Echo "StatusCode:         " & objItem.StatusCode  & _
               " (only correct for connected host - " & strComputer & ")"
  Wscript.Echo ""

  Wscript.Echo "Connecting to this node directly (to get the correct host state)..."
  Set objWMIService2 = GetObject("winmgmts:\\" & objItem.ComputerName & _
                                 "\root\MicrosoftNLB")
  Wscript.Echo "Connected to this node (via " & "winmgmts:\\" & _
                objItem.ComputerName & "\root\MicrosoftNLB" & ") ..."
  Set colItems2 = objWMIService2.ExecQuery("Select * from MicrosoftNLB_Node",,48)
  For Each objItem2 in colItems2
    If objItem.ComputerName = objItem2.ComputerName Then
      Wscript.Echo "Correct StatusCode: "      & objItem2.StatusCode
    End If
  Next

  Wscript.Echo ""
  Wscript.Echo "================="
  Wscript.Echo ""
Next
```



## Related topics

<dl> <dt>

[Using the Network Load Balancing Provider](using-the-network-load-balancing-provider.md)
</dt> <dt>

[Enumerating Nodes](enumerating-nodes.md)
</dt> <dt>

[**MicrosoftNLB\_Node**](https://msdn.microsoft.com/library/aa371151)
</dt> </dl>

 

 




