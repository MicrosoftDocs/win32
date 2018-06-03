---
title: Monitoring Application Level Health
description: Demonstrates monitoring services on Network Load Balancing (NLB) nodes, stopping NLB on any nodes where the monitored service has stopped.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 12afb466-d206-4284-9df0-3b62bf1239a4
ms.prod: windows-server-dev
ms.technology:
- network-load-balancing
- windows-management-instrumentation
ms.tgt_platform: multiple
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Monitoring Application Level Health

This example demonstrates monitoring services on Network Load Balancing (NLB) nodes, stopping NLB on any nodes where the monitored service has stopped.


```VB
'''''''''''''''''''''''''''''''''''
' NlbMon.vbs
'
' Sample script to monitor NLB clusters.
'
' User can pass any NT service on the NLB cluster nodes for the
' script to check status. If that service is stopped on any of
' NLB nodes, the script will stop NLB on that node.
' 
' Optionally includes capability of passing alternate credentials
' to use when connecting to the cluster nodes.
'
' Note: Windows Server 2003 nodes should have remote control
' enabled. Otherwise, you can extend the -n command-line
' parameter to accept multiple nodes to connect to individually.
'
'
' Suggested additional enhancements/customizations:
'
' This script can be customized for much more complicated health
' monitoring and dynamic load-balancing capabilities. Examples
' include:
'
'    - Loop infinitely, checking for latest service status. This
'      script currently executes one iteration against the cluster
'      nodes.
'    - Automatically start back NLB on a node if the service
'      comes back to the started state. Currently, this script
'      waits for interaction from the administrator to debug the 
'      service problem before restarting NLB on the affected nodes.
'    - Check stress level on nodes (for example, checking CPU,
'      memory, or other performance metrics on the system).
'    - Check application response times. For example, if the
'      application being load balanced is slow in responding on one
'      of the nodes, the script can change NLB weights and/or
'      stop NLB on the affected nodes.
'    - Work on a localized computer.
' 
'''''''''''''''''''''''''''''''''''

' Variables used throughout the script
Dim strUserName,strPassword
Dim objNlb
Dim strServer,strClusterVip
Dim strService
Dim strURLFile


' Parse the command line.
call ParseCommand()
' Display a warning if only the VIP is provided.
call IsVipOnly()

wscript.echo "Using server IP to query for nodes: " & strServer
wscript.echo "Using primary cluster IP: "           & strClusterVip
wscript.echo

' Perform the NT service check.
if strService <> "" then 
  call CheckServiceAndControlNLB(strService , "Stopped")
end if

' Perform the Web GET request check.
if strURLFile <> "" then 
  call CheckWebURL(strServer,strClusterVip,strURLFile)
end if

wscript.quit



Function IsVipOnly()
'
' Check if a VIP was the only connection IP passed.
' If it is, set strClusterVip to strServr.
'
  if strServer = "" then 
    wscript.echo "WARNING: Only the VIP was passed."
    wscript.echo "Using the VIP to manage cluster may result "_
               & "in errors with connecting to individual nodes.  "
    wscript.echo "If you encounter any error, you should specify a "_
               & "host name or host IP to connect to."
    wscript.echo
    wscript.echo "Attempt the initial connection using the VIP."
    IsVipOnly = (strClusterVip = "")
    strServer = strClusterVip
    exit Function
  end if
end Function


Function CheckServiceAndControlNLB( byVal strService, _
                                    byVal strServiceState)
'
' Connects to specified node to get other nodes in cluster and then 
' queries for state on each NLB node and sets NLB state as appropriate.
'
  Dim objCimv2
  Dim objNodes1,objNLBNode

  if ( ConnectProvEx("root\microsoftnlb", strUserName, strPassword, strServer, objNlb, true) ) then 
    wscript.echo "Unable to connect to NLB node."
    CheckServiceAndControlNLB = -1
    exit Function
  end if
    
  if ( ConnectProvEx("root\cimv2", strUserName, strPassword, strServer, objCimv2, true) ) then 
    wscript.echo "Unable to connect to cimv2 namespace."
    CheckServiceAndControlNLB = -1
    exit Function
  end if

  if (GetClusterMembers(objNlb,strClusterVip ,objNodes1)<>0) then 
    CheckServiceAndControlNLB = -1
    exit Function
  end if

  for each objInst in objNodes1
    szName = objInst.name
    szRelPath = objInst.path_.Relpath
    szComputername =  objInst.Computername
    wscript.echo "#### Attempting to connect to server "    _
               & szComputername & " to check that service " _
               & strService & " is " & strServiceState & " ######"
    call ConnectProvEx( "root\microsoftnlb", strUserName, strPassword, szComputername, objNLBNode, true )
    call ConnectProvEx("root\cimv2", strUserName, strPassword, szComputername, objCimv2, true )
    wscript.echo "Connected to " & szComputername
    szActualState = ""
    if ( GetStateOfServiceOnNode( objCimv2, strService, strServiceState, szActualState ) )  then
      wscript.echo("!!!! Attempt to stop NLB on node: " & szComputername)
      call NodeControl(objNLBNode,szRelPath, "stop")   
      wscript.echo
    end if
  next
end Function


Function CheckWebURL(byVal strServer, strClusterVip, byVal strURLFile) 
'
' Connects to specified node to get other nodes in cluster and then 
' runs a simple HTTP test and sets NLB state as appropriate.
'
  Dim strURL
  Dim objNodes1,objNLBNode

  if (ConnectProvEx( "root\microsoftnlb", strUserName, strPassword, strServer, objNlb, true ) ) then 
    wscript.echo "Unable to connect to NLB node."
    exit Function
  end if

  if (GetClusterMembers(objNlb,strClusterVip ,objNodes1) <> 0) then 
      exit Function
  end if

  for each objInst in objNodes1
    szRelPath = objInst.path_.Relpath
    szComputername =  objInst.Computername
    wscript.echo "#### Attempting to get URL " & strURL & " ######"
    strURL= "http://" & szComputername & "/" & strURLFile
    if CheckWeb(strURL) = False then
      wscript.echo ("Page is unavailable")
      wscript.echo("!!!! Attempt to stop NLB on node: "&amp; szComputername)
      if ConnectProvEx("root\microsoftnlb", strUserName, strPassword, szComputername, objNLBNode, true ) <> 0 then 
        wscript.echo "!!!!" & szRelPath
        call NodeControl(objNLBNode,szRelPath, "stop")   
      end if
    end if
  next
end Function


Function GetClusterMembers( byRef objNLBNode, _
                            byVal szVip,      _
                            byRef objMembers)
'
' Enumerate the cluster members given the VIP.
'
  on error resume next
  szQueryString = "select * from MicrosoftNLB_Node where name like '%" & szVip & "%'"
  set objMembers = objNLBNode.ExecQuery(szQueryString)

  if (Err.Number) then
    Wscript.echo "Failed to get cluster members for " & szVip & ": " & err.description
    GetClusterMembers = err.number
  else                
    if objMembers.count = 0 then 
      wscript.echo "NLB is not bound. Make sure that you are using the primary cluster IP address."
      wscript.echo "Using any other VIP will fail to find the cluster instance."
      GetClusterMembers = 1
    else
      GetClusterMembers = 0
    end if
  end if
end function


Function NodeControl(byRef objNLBNode, byVal szPath, byVal szAction)
'
' Control NLB cluster node state. 
' Action is one of: stop, start, suspend, resume.
'
  on error resume next
  wscript.echo "Attempt to get NLB instance: " & szPath
  Set objNode = objNLBNode.Get(szPath)
  if Err.Number <> 0 then
    Wscript.echo "Failed to get NLB instance " & WMIClass & ": " & err.description
  else                
    Set objOutParam = objNode.ExecMethod_(szAction)
    wscript.echo("Execute method returned:")
    call DisplayReturnValue(objOutParam.ReturnValue)
  end if
end function


sub DisplayReturnValue(ReturnValue)
'
' Translate the return value to a string and display it to output.
'
  select case ReturnValue
    case 1000    
      wscript.echo "    Success."
    case 1001    
      wscript.echo "    Cluster mode is already stopped/started, or traffic handling is already" _
                 & " enabled/disabled on specified port."
    case 1002    
      wscript.echo "    Cluster mode stop or start operation interrupted connection draining process."
    case 1003    
      wscript.echo "    Cluster mode could not be started due to configuration problems on the target host."
    case 1004    
      wscript.echo "    Port number not found among port rules."
    case 1005    
      wscript.echo "    Cluster mode is stopped on the host."
    case 1006    
      wscript.echo "    Cluster is converging."
    case 1007    
      wscript.echo "    Cluster or host converged successfully."
    case 1008    
      wscript.echo "    Host is converged as default host."
    case 1009    
      wscript.echo "    Host is draining after drainstop command."
    case else:
      wscript.echo "    Unknown return (" & ReturnValue & ")."
  end select
End Sub


Function Ping(ByVal szIP)
'
' Ping an remote machine using \root\cimv2:Win32_PingStatus
'
  strComputer = "."
  Set objWMIService = GetObject("winmgmts:\\" & strComputer & "\root\cimv2")
  Set colPings = objWMIService.ExecQuery( "Select * From Win32_PingStatus where Address = '" _
                                         & szIP & "'")

  for Each objStatus in colPings
    if IsNull(objStatus.StatusCode) or objStatus.StatusCode<>0 then
      Ping = false 
      WScript.Echo "Computer did not respond." 
    else
      Ping = true
      Wscript.Echo "Computer responded."
    end If
  next
End Function


Function CheckWeb(byVal strURL)
'
' Validates that a specified Web page is accessible by running an 
' HTTP GET request.
'
  on error resume next
  With CreateObject("MSXML2.XMLHTTP")
    .open "GET", strURL, False
    wscript.echo "Attempt to get: " & strURL
    .send
    if .status <> 200 then
      CheckWeb = false
      wscript.echo "HTTP GET returned " & .status
    else
      CheckWeb = true
      Wscript.echo "GET sucess. Page content as follows:"
      WScript.Echo .responseText
    end if
  End With
end function


Function ConnectProvEX( ByVal strNameSpace, _
                        ByVal strUserName,  _
                        ByVal strPassword,  _
                        ByRef strServer,    _
                        ByRef objService,   _
                        ByVal LOAD_DRIVE)
'
' Connect to WMI provider name space.
'
  on error resume next
  Dim objLocator, objWshNet
  ConnectProvEx = False     'There is no error.  

  'Create Locator object to connect to remote CIM object manager.
  Set objLocator = CreateObject("WbemScripting.SWbemLocator")

  if LOAD_DRIVE <> False then
    objLocator.Security_.Privileges.AddAsString "SeLoadDriverPrivilege", True 
  end if

  if Err.Number then
    wscript.echo("    Error 0x" & CStr(Hex(Err.Number)) & _
                 " occurred in creating a locator object." )
    if Err.Description <> "" then
      wscript.echo("    Error description: " & Err.Description )
    end if
    ConnectProvEx = err.number     'An error occurred
    Err.Clear
    Exit Function
  end if

  Set objService = objLocator.ConnectServer( strServer,    _
                                             strNameSpace, _
                                             strUserName,  _
                                             strPassword)
  if err = -2147023174 then 'HRESULT_FROM_WIN32(RPC_S_SERVER_UNAVAILABLE)
    wscript.echo err.Description 
    wscript.echo "Verify that server name or IP address is correct for " _
               & strServer 
    ConnectProvEx = err.number
    exit function
  end if

    ObjService.Security_.impersonationlevel = 3
    if Err.Number then
      wscript.echo("    Error 0x" & CStr(Hex(Err.Number)) 
                 & " occurred in connecting to server " & strServer & ".")
      if Err.Description <> "" then
        wscript.echo("    Error description: " & Err.Description )
      end if
      Err.Clear
      ConnectProvEx = err.number
  end if
End Function


Function GetStateOfServiceOnNode( byRef objCimvServer, _
                                  byVal strService,    _
                                  byVal chkState,      _
                                  byRef isState)
'
' Query NT service for a given state and return the state.
'
  szQueryString = "Select * from Win32_Service where name = '" & strService & "'"
  Set objService = objCimvServer.ExecQuery(szQueryString)
  if objService.count = 0 then 
    wscript.echo "Service " &  strService & " is not installed"
    GetStateOfServiceOnNode = -1
    exit function
  end if
  for each objInst in objService
    isState = objInst.State
    wscript.echo "Service " &  strService & " is " & isState
    if chkState = isState then 
      GetStateOfServiceOnNode = true
    end if 
  next
end Function


Function ParseCommand()
'
' Parses the command line and fills the script variables 
' with the appropriate values.
'
  Dim ArgCount
  Dim oArgs

  Set oArgs = Wscript.Arguments

  ArgCount = 0
  if oArgs.Count = 0 then
    wscript.echo "No arguments specified."
    wscript.echo
    call Help()
  end if


  While ArgCount < oArgs.Count
    Select Case LCase(oArgs(ArgCount))
      Case "-u"
        ArgCount = ArgCount + 1
        strUserName=LCase(oArgs(ArgCount))
      Case "-p"
        ArgCount = ArgCount + 1
        strPassword=oArgs(ArgCount)
      Case "-s"
        ArgCount = ArgCount + 1
        strService= LCase(oArgs(ArgCount))
      Case "-f"
        ArgCount = ArgCount + 1
        strURLFile = LCase(oArgs(ArgCount))
      Case "-n"
        ArgCount = ArgCount + 1
        strServer= LCase(oArgs(ArgCount))
      Case "-v"
        ArgCount = ArgCount + 1
        strClusterVip= LCase(oArgs(ArgCount))
      Case Else:
        wscript.echo "Invalid command."
        wscript.echo
        call Help()
        wscript.quit
    End Select
    ArgCount = ArgCount + 1
  Wend
End Function


sub Help()
'
' Display command-line syntax for the script.
'
  wscript.echo "Network Load Balancing (NLB) service monitor tool"
  wscript.echo "Checks any Windows service state and stops NLB hosts if that service is stopped."
  wscript.echo "Service Monitor command Line help"
  wscript.echo
  wscript.echo "Syntax:"
  wscript.echo
  wscript.echo "-u User name"
  wscript.echo "-p Password"
  wscript.echo "-n Server name or IP"
  wscript.echo "-s Service name to monitor"
  wscript.echo "-v Primary cluster IP"
  wscript.echo "-f File to HTTP GET"
  wscript.echo
  wscript.echo "Examples:"
  wscript.echo
  wscript.echo "nlbmon.vbs -n 2.77.2.2 -v 2.77.22.200 -s w3svc"
  wscript.echo "nlbmon.vbs -v 2.77.22.200 -s w3svc"
  wscript.echo "nlbmon.vbs -v 2.77.22.200 -s w3svc -f whoami.txt"
  wscript.echo "nlbmon.vbs -n 2.77.2.2 -v 2.77.22.200 -f whoami.txt"
  wscript.quit
End Sub
```



## Related topics

<dl> <dt>

[Using the Network Load Balancing Provider](using-the-network-load-balancing-provider.md)
</dt> <dt>

[**MicrosoftNLB\_Node**](https://msdn.microsoft.com/library/aa371151)
</dt> <dt>

[**Stop Method of the MicrosoftNLB\_Node Class**](https://msdn.microsoft.com/library/aa371406)
</dt> </dl>

 

 




