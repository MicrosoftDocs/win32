---
title: Making Direct Connections
description: Procedure for using the WMI scripting API to establish a direct connection to the Network Load Balancing provider.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '046fbf80-57b5-4c45-bc96-a13f1266e0bf'
ms.prod: 'windows-server-dev'
ms.technology:
- 'network-load-balancing'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
---

# Making Direct Connections

The following procedure describes how to use the Scripting API for [*WMI*](https://msdn.microsoft.com/library/aa371764#mscs-n---z-21-gly) to establish a [direct connection](direct-connections.md):

**How to use the Scripting API for WMI to establish a direct connection**

1.  Obtain an [**SWbemLocator**](https://msdn.microsoft.com/library/aa393719) object.
2.  Obtain an [**SWbemServices**](https://msdn.microsoft.com/library/aa393854) object using [**SWbemLocator.ConnectServer**](https://msdn.microsoft.com/library/aa393720), specifying the target host's dedicated IP address as the *Computername* parameter.
3.  Use the methods of [**SWbemServices**](https://msdn.microsoft.com/library/aa393854) to obtain instances of Network Load Balancing provider classes. For more information see [Obtaining Class Instances](obtaining-class-instances.md).

The following code snippet demonstrates this procedure. For a more detailed code example, see [NLBScriptLib.vbs](nlbscriptlib-vbs.md).


```VB
Set oLoc     = CreateObject("WbemScripting.SWbemLocator")
strDIP       = "172.16.102.43"
strNamespace = "root\MicrosoftNLB"
strUser      = "Administrator"
strPassword  = ""

Set oSvc     = oLoc.ConnectServer(strDIP,       _
                                  strNamespace, _
                                  strUser,      _
                                  strPassword)
oLoc.Security_.ImpersonationLevel = 3
```



 

 




