---
title: Getting Replication Backlog Information
description: VBScript example shows how to use the DfsrReplicatedFolderConfig, DfsrReplicatedFolderInfo, and DfsrReplicationGroupConfig classes to get replication backlog information between two servers.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 37b8c2b9-69f5-431c-bfb4-f7a3d91d4301
ms.prod: windows-server-dev
ms.technology:
- distributed-file-system-replication
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Distributed File System Replication examples Files , getting replication backlog information
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Getting Replication Backlog Information

The following VBScript example shows how to use the [**DfsrReplicatedFolderConfig**](dfsrreplicatedfolderconfig.md), [**DfsrReplicatedFolderInfo**](dfsrreplicatedfolderinfo.md), and [**DfsrReplicationGroupConfig**](dfsrreplicationgroupconfig.md) classes to get replication backlog information between two servers.

To run the script, which is in Windows Script Host (WSH) 2.0 XML file format, save the text in a file with a .wsf extension.


```XML
<?XML version="1.0" standalone="yes" ?>

<job id="GetBacklog">
 <runtime>
  <description>
   This script uses the DFSR WMI provider to obtain replication backlog information between two servers.
  </description>
  <named
        name="ReplicationGroupName"
        helpstring="Replication Group Name"
        type="string"
        required="true"
/>
  <named
        name="ReplicatedFolderName"
        helpstring="Replicated Folder Name"
        type="string"
        required="false"
/>
  <named 
        name="SendingServer"
        helpstring="The server sending files"
        type="string"
        required="true"
/>
  <named 
        name="ReceivingServer"
        helpstring="The server receiving files"
        type="string"
        required="true"
/>
  <named
        name="Twoway"
        helpstring="Get backlog both ways between given servers"
        type="simple"
        required="false"
/>
  <named
        name="?"
        helpstring="Display help for this script"
        type="simple"
        required="false"
/>
 </runtime>

 <resource id="DfsrReplicationGroupConfig">DfsrReplicationGroupConfig</resource>
 <resource id="DfsrReplicatedFolderConfig">DfsrReplicatedFolderConfig</resource>
 <resource id="DfsrReplicatedFolderInfo">DfsrReplicatedFolderInfo</resource>
 <resource id="DfsrNamespace">\root\microsoftdfs</resource>

 <resource id="ConfigError0">Success.</resource>
 <resource id="ConfigError1">Registry key is not found.</resource>
 <resource id="ConfigError2">Registry key is not accessible.</resource>
 <resource id="ConfigError3">Registry value is not found.</resource>
 <resource id="ConfigError4">Registry value is not valid.</resource>
 <resource id="ConfigError5">Generic registry error.</resource>
 <resource id="ConfigError6">MSXML.dll Not installed.</resource>
 <resource id="ConfigError7">Missing XML DOM.</resource>
 <resource id="ConfigError8">XML DOM is not valid.</resource>
 <resource id="ConfigError9">XML file not found.</resource>
 <resource id="ConfigError10">XML file not accessible</resource>
 <resource id="ConfigError11">Generic XML error.</resource>
 <resource id="ConfigError12">Cannot connect to AD.</resource>
 <resource id="ConfigError14">Generic AD error.</resource>
 <resource id="ConfigError15">Bad XML\AD parameter.</resource>
 <resource id="ConfigError16">Bad XML\AD parameter.</resource>
 <resource id="ConfigError17">File path is not valid.</resource>
 <resource id="ConfigError18">Volume not found.</resource>
 <resource id="ConfigError19">Out of memory.</resource>
 <resource id="ConfigError20">Configuration source mismatch.</resource>
 <resource id="ConfigError21">Access denied.</resource>
 <resource id="ConfigError22">Generic error.</resource>

 <resource id="MonitorError0">Success.</resource>
 <resource id="MonitorError1">Generic database error.</resource>
 <resource id="MonitorError2">ID record not found.</resource>
 <resource id="MonitorError3">Volume not found.</resource>
 <resource id="MonitorError4">Access denied.</resource>
 <resource id="MonitorError5">Generic error.</resource>

 <reference object="Scripting.FileSystemObject"/>
 <reference object="WbemScripting.SWbemLocator"/>

 <script language="VBScript">
  <![CDATA[
    Option Explicit
    
    Dim objWbemDateTime
    Set objWbemDateTime = CreateObject("WbemScripting.SWbemDateTime")
    
    Call Main()
    
    Function EscapeString(strStringToEscape)
        Dim strReturn
        
        strReturn = Replace(strStringToEscape, "\", "\\")
        strReturn = Replace(strReturn, "'", "\'")
        
        EscapeString = strReturn
    End Function
    
    Function ConstructQueryString(arrStrPropNames, _
                                  strClassName,    _
                                  strCondition)
        Dim strQuery
        Dim intIdx
        
        strQuery = "SELECT "
        If ( IsNull(arrStrPropNames) ) Then
            strQuery = strQuery & "*"
        Else
            strQuery = strQuery & arrStrPropNames(0)
            For intIdx = 1 To UBound(arrStrPropNames) - 1
                strQuery = strQuery & ", " & arrStrPropNames(intIdx)
            Next
        End If
        
        strQuery = strQuery & " FROM " & strClassName
        
        If ( NOT IsNull(strCondition) ) Then
            strQuery = strQuery & " WHERE " & strCondition
        End If

        ConstructQueryString = strQuery
    End Function
    
    Function GetQueryResult(objWmiConnector, _
                            arrStrPropNames, _
                            strClassName,    _
                            strCondition,    _
                            blnForwardOnly   _
                           )
        Dim objObjectSet
        Dim strQuery
        Dim intFlags
        
        strQuery = ConstructQueryString(arrStrPropNames, _
                                        strClassName, _
                                        strCondition)
        
        If ( blnForwardOnly ) Then
            intFlags = _
                wbemFlagReturnImmediately Or _
                wbemFlagForwardOnly
        Else
            intFlags = _
                wbemFlagReturnImmediately
        End If
        
        Set objObjectSet = objWmiConnector.ExecQuery(strQuery, _
                                                     "WQL", _
                                                     intFlags)
        
        If ( IsNull(objObjectSet) ) Then
            Dim strError
            
            strError = vbCrLf & "Query: " & strQuery & " Failed"
            strError = strError & vbCrLf
            strError = "Query returned no matches"
            Err.Raise 6670,,strError
        End If
        
        Set GetQueryResult = objObjectSet
    End Function
    
    Function GetSingleResultFromQuery(objWmiConnector, _
                                      arrStrPropNames, _
                                      strClassName,    _
                                      strCondition)                                      
        Dim objObjectSet, objObject
        
        Set objObjectSet = _
            GetQueryResult(objWmiConnector, _
                           arrStrPropNames, _
                           strClassName,    _
                           strCondition,    _
                           False)
                                      
        If ( objObjectSet.Count <> 1 ) Then
            Dim strError, strQuery
            strQuery = ConstructQueryString(arrStrPropNames, strClassName, strCondition)
            strError = vbCrLf & "Query: " & strQuery & " Failed"
            strError = strError & vbCrLf
            strError = strError & "Query Returned " _
                       & objObjectSet.Count & " matches"
            Err.Raise 6667,,strError
            Exit Function
        End If
        
        For Each objObject in objObjectSet
            Set GetSingleResultFromQuery = objObject
            Exit Function
        Next
    End Function
    
    Function ConstructObjectPath(strClassName, _
                                 strPropName,  _
                                 strPropValue, _
                                 intPropType)
        Dim strReturn
        
        strReturn = strClassName & "." & strPropName & "="
        
        Select Case intPropType
            Case wbemCimtypeChar16
                strReturn = strReturn & "'" & EscapeString(strPropValue) & "'"
            Case wbemCimtypeDateTime
                strReturn = strReturn & "'" & EscapeString(strPropValue) & "'"
            Case wbemCimtypeString
                strReturn = strReturn & "'" & EscapeString(strPropValue) & "'"
            Case Else
                strReturn = strReturn & strPropValue
        End Select
      
        ConstructObjectPath = strReturn
    End Function
    
    Sub GetBacklog(objReceivingWmiConn, _
                   objSendingWmiConn,   _
                   objReceivingDfsrRfInfo)
        
        Dim strVv, strError
        Dim strObjPath
        Dim objSendingDfsrRfInfo
        Dim uintBacklogCount
        Dim uintRecordIdx
        Dim uintErr

        ' Get the version vector for receiving member
        uintErr = objReceivingDfsrRfInfo.GetVersionVector(strVv)

        If uintErr <> 0 Then
            Err.Raise 6668,,getResource("MonitorError" & CStr(uintErr))
            Exit Sub
        End If
        
        ' Get the relative object path to get the
        ' DfsrReplicatedFolderInfo instance from
        ' Serving side
        strObjPath = _
            objReceivingDfsrRfInfo.Path_.RelPath
        
        ' Get the DfsrReplicatedFolderInfo instance from
        ' Serving side
        On Error Resume Next
        Set objSendingDfsrRfInfo = _
            objSendingWmiConn.Get(strObjPath)
            
        If ( Err <> 0 ) Then
            WScript.Echo "Error Getting DfsrReplicatedFolderInfo instance " & _
                         "for Replicated Folder " &  _
                         objReceivingDfsrRfInfo.ReplicatedFolderName & _
                         " from Sending Server"
            WScript.Echo "Error Message: " & Err.Description & ", Code: " & Err.Number
            Exit Sub
        End If
        
        On Error Goto 0
            
        ' Get the backlogged file count from
        ' serving side given receiving side's 
        ' version vector
        uintErr = _
            objSendingDfsrRfInfo.GetOutboundBacklogFileCount( _
                strVv,            _
                uintBacklogCount, _
                uintRecordIdx)
        
        If uintErr <> 0 Then
            Err.Raise 6669,,getResource("MonitorError" & CStr(uintErr))
            Exit Sub
        End If
        
        WScript.Echo objSendingDfsrRfInfo.Path_.Server &            _
                     " -> " &                                       _
                     objReceivingDfsrRfInfo.Path_.Server &          _
                     ", Replicated Folder: " &                      _
                     objReceivingDfsrRfInfo.ReplicatedFolderName &  _
                     " is backlogged by: " &                        _
                     uintBacklogCount &                             _
                     " files"        
    End Sub
                       
    Sub Main
        Dim objNamedArgs
        Dim strSendingComputer, strReceivingComputer
        Dim objSendingWmiService, objReceivingWmiService
        Dim objClass
        Dim strObjPath, strCondition
        Dim objDfsrRgConfig
        Dim objDfsrRfInfo
        Dim objObjectSet
        Dim objTemp
    
        Set objNamedArgs   = WScript.Arguments.Named
    
        ' Display help if there are any unnamed arguments in the command line
        If ( WScript.Arguments.Unnamed.Length <> 0 ) Then
            WScript.Arguments.ShowUsage()
            WScript.Quit(1)
        End If
        
        ' Display help if there are not enough arguments, 
        ' help is requested or
        ' required arguments are not specified
        If ( objNamedArgs.Length < 1 Or _
             objNamedArgs.Exists("help") Or _
             objNamedArgs.Exists("?") Or _
             NOT objNamedArgs.Exists("sendingserver") Or _
             NOT objNamedArgs.Exists("receivingserver") Or _
             NOT objNamedArgs.Exists("replicationgroupname") ) Then
            WScript.Arguments.ShowUsage()
            WScript.Quit(1)
        End If
        
        strReceivingComputer = objNamedArgs("ReceivingServer")
        strSendingComputer   = objNamedArgs("SendingServer")
        
        ' Connect to the receiving server's DFSR WMI namespace
        ' \\server\root\microsoftdfs
        Set objReceivingWmiService = _
            GetObject("winmgmts:\\" & strReceivingComputer & getResource("DfsrNamespace"))
    
        ' Connect to the sending server's DFSR WMI namespace
        ' \\server\root\microsoftdfs
        Set objSendingWmiService = _
            GetObject("winmgmts:\\" & strSendingComputer & getResource("DfsrNamespace"))
    
        ' Get the DfsrReplicationGroupConfig for given RG name
        ' from receiving server
        ' Query: Select ReplicationGroupGuid From DfsrReplicationGroupConfig Where ReplicationGroupName = '<value>'
        strCondition = "ReplicationGroupName = '" & _
                       EscapeString(objNamedArgs("ReplicationGroupName")) & _
                       "'"
        Set objDfsrRgConfig = _
            GetSingleResultFromQuery(objReceivingWmiService, _
                                     Array("ReplicationGroupGuid"), _
                                     getResource("DfsrReplicationGroupConfig"), _
                                     strCondition)
                                     
        ' If a replicated folder name was specified
        ' Get backlog only for that folder
        If ( objNamedArgs.Exists("ReplicatedFolderName") ) Then
            ' Get DfsrReplicatedFolderInfo instance on receiving member
            ' Query: Select * From DfsrReplicatedFolderInfo Where ReplicationGroupGuid = '<value>' AND ReplicatedFolderName = '<value>'
            strCondition = "ReplicationGroupGuid = '" & _
                           objDfsrRgConfig.ReplicationGroupGuid & _
                           "' AND " & _
                           "ReplicatedFolderName = '" & _
                           EscapeString(objNamedArgs("ReplicatedFolderName")) & _
                           "'"
            Set objDfsrRfInfo = _
                GetSingleResultFromQuery(objReceivingWmiService, _
                                         Null, _
                                         getResource("DfsrReplicatedFolderInfo"), _
                                         strCondition)
            Call GetBacklog(objReceivingWmiService, _
                            objSendingWmiService,   _
                            objDfsrRfInfo)
                            
            If ( Not objNamedArgs.Exists("Twoway") ) Then
                WScript.Quit(0)
            End If
            
            ' Swap sending and receiving sides
            Set objTemp = objSendingWmiService
            Set objSendingWmiService   = objReceivingWmiService
            Set objReceivingWmiService = objTemp

            ' Get the DfsrReplicatedFolderInfo instance on receiving member
            ' Query: Select * From DfsrReplicatedFolderInfo Where ReplicationGroupGuid = '<value>' AND ReplicatedFolderName = '<value>'
            Set objDfsrRfInfo = _
                GetSingleResultFromQuery(objReceivingWmiService, _
                                         Null, _
                                         getResource("DfsrReplicatedFolderInfo"), _
                                         strCondition)
            Call GetBacklog(objReceivingWmiService, _
                            objSendingWmiService,   _
                            objDfsrRfInfo)
        ' If no replicated folder name was specified
        ' Get backlog for all replicated folders in 
        ' specified replication group
        Else
            ' Get all DfsrReplicatedFolderInfo instances for
            ' given replication group
            strCondition = "ReplicationGroupGuid = '" & _
                           objDfsrRgConfig.ReplicationGroupGuid & _
                           "'"
            Set objObjectSet = _
                GetQueryResult(objReceivingWmiService, _
                               Null, _
                               getResource("DfsrReplicatedFolderInfo"), _
                               strCondition, _
                               True)
                               
            Dim blnAtleastOneResult 
            blnAtleastOneResult = False
            
            For Each objDfsrRfInfo In objObjectSet
                blnAtleastOneResult = True
                Call GetBacklog(objReceivingWmiService, _
                                objSendingWmiService,   _
                                objDfsrRfInfo)
            Next
            
            If ( Not blnAtLeastOneResult ) Then
                WScript.Echo "Replication Group " & _
                             objNamedArgs("ReplicationGroupName") & _
                             " has no Replicated Folders"
                WScript.Quit(1)
            End If
            
            If ( Not objNamedArgs.Exists("Twoway") ) Then
                WScript.Quit(0)
            End If
            
            ' Swap sending and receiving sides
            Set objTemp = objSendingWmiService
            Set objSendingWmiService   = objReceivingWmiService
            Set objReceivingWmiService = objTemp

            ' Get all DfsrReplicatedFolderInfo instances for
            ' given replication group
            strCondition = "ReplicationGroupGuid = '" & _
                           objDfsrRgConfig.ReplicationGroupGuid & _
                           "'"
            Set objObjectSet = _
                GetQueryResult(objReceivingWmiService, _
                               Null, _
                               getResource("DfsrReplicatedFolderInfo"), _
                               strCondition, _
                               True)
                               
            blnAtleastOneResult = False
            
            For Each objDfsrRfInfo In objObjectSet
                blnAtleastOneResult = True
                Call GetBacklog(objReceivingWmiService, _
                                objSendingWmiService,   _
                                objDfsrRfInfo)
            Next
                        
            If ( Not blnAtLeastOneResult ) Then
                WScript.Echo "Replication Group " & _
                             objNamedArgs("ReplicationGroupName") & _
                             " has no Replicated Folders"
                WScript.Quit(1)
            End If
        End If
        
    End Sub
  ]]>
 </script>

</job>
```



 

 




