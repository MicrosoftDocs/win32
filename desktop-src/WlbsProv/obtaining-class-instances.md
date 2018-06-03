---
title: Obtaining Class Instances
description: Procedure to obtain class instances of the Network Load Balancing provider.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 68b681f5-c6ee-4457-847c-bf3df6ec4963
ms.prod: windows-server-dev
ms.technology:
- network-load-balancing
- windows-management-instrumentation
ms.tgt_platform: multiple
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Obtaining Class Instances

If you establish a direct connection with a cluster [*node*](https://msdn.microsoft.com/library/aa371764#mscs-n---z-5-gly) (see [Making Direct Connections](making-direct-connections.md)), you can obtain instances of Network Load Balancing (NLB) provider classes as follows:

-   Use the [**SWbemServices.InstancesOf**](https://msdn.microsoft.com/library/aa393870) method to get a collection of [**MicrosoftNLB\_Node**](microsoftnlb-node.md) objects. The collection will always return the node you are connected to first, or you can use the object's **Name** property to identify a particular node. Note that the nodes you will be able to enumerate depend on several factors. For more information see [Enumerating Objects](https://msdn.microsoft.com/library/aa369563).
-   Use the [**SWbemServices.InstancesOf**](https://msdn.microsoft.com/library/aa393870) method to get a collection of [**MicrosoftNLB\_NodeSetting**](microsoftnlb-nodesetting.md) objects. The collection will always return the **MicrosoftNLB\_NodeSetting** corresponding to the node you are connected to first, or you can use the **MicrosoftNLB\_NodeSetting** object's **Name** property to identify a particular node setting. Note that the node settings you will be able to enumerate depend on several factors. For more information see [Enumerating Objects](https://msdn.microsoft.com/library/aa369563).
-   Use the [**MicrosoftNLB\_NodeSetting.GetPortRule**](microsoftnlb-nodesetting-getportrule.md) method to get instances of [**MicrosoftNLB\_PortRule**](microsoftnlb-portrule.md) objects.

The following code snippet demonstrates how to obtain instances of NLB provider classes. For a more detailed code example, see [NLBScriptLib.vbs](nlbscriptlib-vbs.md).


```VB
'Set configuration data.
strClusterIP = "172.50.66.14"
strHostID = "1"
strDIP = "172.50.35.12"
strKey = strClusterIP & ":" & strHostID
strNamespace = "root\MicrosoftNLB"
strUser = "Administrator"
strPassword = ""
strPortNumber = "65535"

'Make a direct connection.
Set oLoc = CreateObject("WbemScripting.SWbemLocator")
Set oSvc = oLoc.ConnectServer(strDIP, _
                              strNamespace, _
                              strUser, _
                              strPassword)
oLoc.Security_.ImpersonationLevel = 3

'Get a node instance.
Set oNodes = oSvc.InstancesOf ("MicrosoftNLB_Node")
For Each oNode in oNodes
    ' The first one is the one we want
    Exit For
Next

'Get a node setting instance.
Set oNodeSettings = oSvc.InstancesOf ("MicrosoftNLB_NodeSetting")
For Each oNodeSetting in oNodeSettings
    ' The first one is the one we want
    Exit For
Next

'Get a port rule instance.
oNodeSetting.GetPortRule CLng(strPortNumber), oPortRule

WScript.Echo oPortRule.Name

Set oPortRule = Nothing
Set oNodeSetting = Nothing
Set oNodeSettings = Nothing
Set oNode = Nothing
Set oNodes = Nothing
Set oSvc = Nothing
Set oLoc = Nothing
```



 

 




