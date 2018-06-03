---
title: Finding the Server that Originated a File or Folder Update
description: VBScript example shows how to use the DfsrConnectionConfig, DfsrIdRecordInfo, DfsrReplicatedFolderConfig, DfsrReplicatedFolderInfo, DfsrReplicationGroupConfig, and DfsrVolumeInfo classes to find the server that originated a file or folder update.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 00180b7f-613f-4ff3-9f6f-15c5b578a542
ms.prod: windows-server-dev
ms.technology:
- distributed-file-system-replication
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Distributed File System Replication examples Files , finding the server that originated a file or folder update
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Finding the Server that Originated a File or Folder Update

The following VBScript example shows how to use the [**DfsrConnectionConfig**](dfsrconnectionconfig.md), [**DfsrIdRecordInfo**](dfsridrecordinfo.md), [**DfsrReplicatedFolderConfig**](dfsrreplicatedfolderconfig.md), [**DfsrReplicatedFolderInfo**](dfsrreplicatedfolderinfo.md), [**DfsrReplicationGroupConfig**](dfsrreplicationgroupconfig.md), and [**DfsrVolumeInfo**](dfsrvolumeinfo.md) classes to find the server that originated a file or folder update.

To run the script, which is in Windows Script Host (WSH) 2.0 XML file format, save the text in a file with a .wsf extension.


```XML
<?XML version="1.0" standalone="yes" ?>

<job id="FindUpdateOrigin">
 <runtime>
  <description>
   This script uses the DFSR WMI provider to attempt to find the server that 
   originated a file/folder update. Tracing can start with either the full file 
   path for the update to be traced or the UID of the update to be traced.
  </description>
  <named 
        name="Server"
        helpstring="Server where the trace should start"
        type="string"
        required="true"
/>
  <named
        name="FilePath"
        helpstring="File Path for which the trace needs to be done"
        type="string"
        required="false"
/>
  <named
        name="FileUid"
        helpstring="File UID for which the trace needs to be done"
        type="string"
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
 <resource id="DfsrConnectionConfig">DfsrConnectionConfig</resource>
 <resource id="DfsrReplicatedFolderInfo">DfsrReplicatedFolderInfo</resource>
 <resource id="DfsrIdRecordInfo">DfsrIdRecordInfo</resource>
 <resource id="DfsrVolumeInfo">DfsrVolumeInfo</resource>
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

 <reference object="Scripting.Dictionary"/>
 <reference object="Scripting.FileSystemObject"/>
 <reference object="WbemScripting.SWbemLocator"/>

 <script language="VBScript">
  <![CDATA[
    Option Explicit
    
    Dim objWbemDateTime
    Set objWbemDateTime = CreateObject("WbemScripting.SWbemDateTime")
    
    Dim objCreatorVolumeInfo, objUpdaterVolumeInfo
    Dim strCreatorName, strUpdaterName
    
    Call Main()
    
    Function WmiDateStringToDate(dtmDate)
        objWbemDateTime.Value = dtmDate
        WmiDateStringToDate = objWbemDateTime.GetVarDate
    End Function

    Sub DisplayWmiObject(objObjectToDisplay)
        Dim objPropValue, objProperty
        Dim strObjectClassName

        strObjectClassName = objObjectToDisplay.Path_.[Class]
        WScript.Echo objObjectToDisplay.Path_.Server & " " & strObjectClassName
        WScript.Echo _
            String(Len(objObjectToDisplay.Path_.Server) + _
                   Len(strObjectClassName) + 1, _
                   "-")
        For Each objProperty In objObjectToDisplay.Properties_
            objPropValue = objProperty.Value
            If ( objProperty.CIMType = wbemCimtypeDatetime ) Then
                objPropValue = WmiDateStringToDate(objPropValue)
            End If
            WScript.Echo objProperty.Name & _
                         Space(40-Len(objProperty.Name)) & _
                         " : " & _
                         objPropValue
        Next
        WScript.StdOut.WriteLine
    End Sub
    
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
    
    Function GetFileNameFromFullPath(strFullPath)
        Dim strTemp, strReturn
        Dim uintPos
        
        strTemp = Replace(strFullPath, "\\", "\")
        uintPos = InStrRev(strTemp, "\")
        If ( uintPos = Len(strTemp) ) Then
            uintPos = InStrRev(strTemp, "\", uintPos-1)
        End If
        
        strReturn = Right(strTemp, Len(strTemp)-uintPos)
        GetFileNameFromFullPath = strReturn        
    End Function
    
    Function GetGuidFromUidOrGvsn(strUidOrGvsn)
        Dim uintPos
        
        ' Search for '}' from the end
        uintPos = InStrRev(strUidOrGvsn, "}")
        
        If ( uintPos <> 0 ) Then
            ' Get the position of the '}'
            ' The GUID is what's between the '{' and the '}'
            Dim strReturn            
            strReturn = Left(strUidOrGvsn, uintPos-1)
            strReturn = Right(strReturn, Len(strReturn)-1)
            GetGuidFromUidOrGvsn = strReturn
        Else
            Err.Raise 6674,,"UID Or GVSN is not in the right format: " & strUidOrGvsn
        End If
    End Function
    
    Function IsTombstone(objIdRecordInfo)
        If ( (objIdRecordInfo.Flags And 1) = 1 ) Then
            IsTombstone = False
        Else
            IsTombstone = True
        End If
    End Function
    
    Function GetFullFilePathFromIdRecord(objIdRecordInfo)
        Dim uintRc
        Dim strFullFilePath
        
        uintRc = objIdRecordInfo.GetFullFilePath(strFullFilePath)
        
        If ( uintRc <> 0 ) Then
            Err.Raise 6673,,"GetFullFilePath failed.  Error: " & getResource("MonitorError" & uintRc)
            Exit Function
        End If
        
        GetFullFilePathFromIdRecord = strFullFilePath
    End Function
    
    Function GetIdRecordFromFullPath(objWmiConnector, _
                                     strFullFilePath)
        Dim objObjectSet
        Dim objDfsrRfConfig
        Dim objDfsrIdRecordInfo
        Dim objTombstoneIdRecordInfo
        Dim strRfFolderPath
        Dim strLcFullFilePath
        Dim strFilePathPrefix
        Dim strFileName
        Dim strCondition
        Dim blnRfFound
        Dim blnFoundTombstoneMatch
        
        strLcFullFilePath = LCase(strFullFilePath)
        
        ' First find the replicated folder corresponding
        ' to this full file path.
        
        ' For this, get all configured replicated folders and
        ' search for a prefix match of the root folder against the
        ' given full file path. Because a proper configuration does not
        ' support root path overlap, you do not have to worry about
        ' longest prefix match.
        
        ' Get all configured replicated folder root paths
        Set objObjectSet = _
            GetQueryResult(objWmiConnector, _
                           Array("RootPath", "ReplicatedFolderGuid"), _
                           getResource("DfsrReplicatedFolderConfig"),   _
                           Null, _
                           True)

        ' Find the replicated folder whose root path
        ' is a prefix of provided full file path
        blnRfFound = False
        For Each objDfsrRfConfig In objObjectSet
            strRfFolderPath = objDfsrRfConfig.RootPath
            If ( Len(strRfFolderPath) <= Len(strFullFilePath) ) Then
                strFilePathPrefix = Left(strLcFullFilePath, Len(strRfFolderPath))
                If ( strRfFolderPath = strFilePathPrefix ) Then
                    blnRfFound = True
                    Exit For
                End If
            End If
        Next

        If ( Not blnRfFound ) Then
            Err.Raise 6671,,"No Replicated Folder found for file path " & strFullFilePath
            Exit Function
        End If
        
        ' Extract the file name portion from supplied path
        strFileName = GetFileNameFromFullPath(strFullFilePath)
        
        ' Query: Select * From DfsrIdRecordInfo Where ReplicatedFolderGuid = '<value>' AND FileName = '<value>'
        strCondition = "ReplicatedFolderGuid = '" & _
                       EscapeString(objDfsrRfConfig.ReplicatedFolderGuid) & _
                       "' AND FileName = '" & _
                       EscapeString(strFileName) & _
                       "'"
        
        Set objObjectSet = _
            GetQueryResult(objWmiConnector, _
                           Null, _
                           getResource("DfsrIdRecordInfo"), _
                           strCondition, _
                           True)

        ' Because only fully qualified file names are unique, you can have
        ' multiple matches for the above query.  Even with a fully qualified
        ' file name, multiple ID records are possible due to name conflicts
        blnFoundTombstoneMatch = False
        For Each objDfsrIdRecordInfo In objObjectSet
            On Error Resume Next
            Dim strIdRecordFullFilePath
            ' For each ID record get the full file path
            strIdRecordFullFilePath = _
                GetFullFilePathFromIdRecord(objDfsrIdRecordInfo)
            On Error Goto 0
            ' Root path quirk - append '\' to the root path
            If ( Right(strIdRecordFullFilePath, 1) = "\" ) Then
                strIdRecordFullFilePath = Left(strIdRecordFullFilePath, Len(strIdRecordFullFilePath)-1)
            End If
            If ( Err.Number = 0 ) Then
                ' If the fully qualified file name of the ID record matches the one given
                If ( LCase(strIdRecordFullFilePath) = strLcFullFilePath ) Then
                    ' If it is a tombstoned record, see if there is a live one that matches
                    ' Save the tombstone match in case there isn't one
                    If ( IsTombstone(objDfsrIdRecordInfo) ) Then
                        Set objTombstoneIdRecordInfo = objDfsrIdRecordInfo
                        blnFoundTombstoneMatch = True
                    ' If there is a live match, that's what we're interested in
                    Else
                        Set GetIdRecordFromFullPath = objDfsrIdRecordInfo
                        Exit Function
                    End If
                End If
            Else
                Err.Clear
            End If
        Next
        
        ' If there was no live match, but a tombstone match was found
        ' return that instead
        If ( blnFoundTombstoneMatch ) Then
            Set GetIdRecordFromFullPath = objTombstoneIdRecordInfo
            Exit Function
        End If
        
        Err.Raise 6672,,"No ID Record found for file path " & strFullFilePath        
    End Function
    
    Sub FindUpdaterAndOrigin(objWmiConnector, _
                             strCreatorGuidQuery, _
                             strUpdaterGuidQuery, _
                             strConnectionQuery, _
                             objServersToProcessTable, _
                             objServersProcessedTable, _
                             blnCreatorFound, _
                             blnUpdaterFound, _
                             strServer _
                            )
        Dim objObjectSet
        Dim objVolumeInfo
        
        If ( Not blnCreatorFound ) Then
            On Error Resume Next
            Set objObjectSet = objWmiConnector.ExecQuery(strCreatorGuidQuery, _
                                                         "WQL", _
                                                         (wbemFlagReturnImmediately Or _
                                                          wbemFlagForwardOnly))
            If ( Err.Number = 0 And _
                 Not IsNull(objObjectSet) ) Then
                For Each objVolumeInfo in objObjectSet
                    Set objCreatorVolumeInfo = objVolumeInfo
                    strCreatorName = objCreatorVolumeInfo.Path_.Server
                    blnCreatorFound = True
                    Exit For
                Next
            Else
                WScript.Echo "Error Searching: " & strServer
                If ( Err.Number <> 0 ) Then
                    WScript.Echo "Error Code: " & Err.Number & ", Message: " & Err.Description
                Else
                    WScript.Echo "Query: " & strCreatorGuidQuery & vbCrLf
                    WScript.Echo "Did not find any matches"
                End If
            End If            
            On Error Goto 0
        End If
        
        If ( Not blnUpdaterFound ) Then
            On Error Resume Next
            Set objObjectSet = objWmiConnector.ExecQuery(strUpdaterGuidQuery, _
                                                         "WQL", _
                                                         (wbemFlagReturnImmediately Or _
                                                          wbemFlagForwardOnly))
            If ( Err.Number = 0 And _
                 Not IsNull(objObjectSet) ) Then
                For Each objVolumeInfo in objObjectSet
                    Set objUpdaterVolumeInfo = objVolumeInfo
                    strUpdaterName = objUpdaterVolumeInfo.Path_.Server
                    blnUpdaterFound = True
                    Exit For
                Next
            Else
                WScript.Echo "Error Searching: " & strServer
                If ( Err.Number <> 0 ) Then
                    WScript.Echo "Error Code: " & Err.Number & ", Message: " & Err.Description
                Else
                    WScript.Echo "Query: " & strUpdaterGuidQuery & vbCrLf
                    WScript.Echo "Did not find any matches"
                End If
            End If            
            On Error Goto 0
        End If
        
        If ( Not blnCreatorFound Or _
             Not blnUpdaterFound ) Then
            On Error Resume Next
            Set objObjectSet = objWmiConnector.ExecQuery(strConnectionQuery, _
                                                         "WQL", _
                                                         (wbemFlagReturnImmediately Or _
                                                          wbemFlagForwardOnly))
            If ( Err.Number = 0 And _
                 Not IsNull(objObjectSet) ) Then
                Dim objConnectionConfig
                For Each objConnectionConfig in objObjectSet
                    Dim strTemp
                    strTemp = objConnectionConfig.PartnerName
                    If ( Not objServersProcessedTable.Exists(strTemp) And _
                         Not objServersToProcessTable.Exists(strTemp) ) Then
                        WScript.Echo "Adding " & strTemp & " to search list"                        
                        Call objServersToProcessTable.Add(strTemp, strTemp)
                    End If
                Next
            Else
                WScript.Echo "Error Searching: " & strServer
                If ( Err.Number <> 0 ) Then
                    WScript.Echo "Error Code: " & Err.Number & ", Message: " & Err.Description
                Else
                    WScript.Echo "Query: " & strConnectionQuery & vbCrLf
                    WScript.Echo "Did not find any matches"
                End If
            End If
            On Error Goto 0
        End If        
    End Sub
    
    Sub Main
        Dim objNamedArgs
        Dim strComputer
        Dim objWmiService
        Dim objIdRecord
        Dim strObjPath, strCondition
        Dim strFullPath
        
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
             NOT objNamedArgs.Exists("Server") Or _
             (NOT objNamedArgs.Exists("FileUid") And _
              NOT objNamedArgs.Exists("FilePath")) ) Then
            WScript.Arguments.ShowUsage()
            WScript.Quit(1)
        End If
        
        strComputer = objNamedArgs("Server")
        
        ' Connect to the server's DFSR WMI namespace
        ' \\server\root\microsoftdfs
        Set objWmiService = _
            GetObject("winmgmts:\\" & strComputer & getResource("DfsrNamespace"))
        
        ' Get the ID record for the given file either using
        ' full file path or UID
        If ( objNamedArgs.Exists("FileUid") ) Then
            ' If UID was given, just get the record directly via WMI
            Dim strIdRecordPath
            strIdRecordPath = ConstructObjectPath(getResource("DfsrIdRecordInfo"), _
                                                  "Uid",                           _
                                                  objNamedArgs("FileUid"),         _
                                                  wbemCimtypeString)
            Set objIdRecord = objWmiService.Get(strIdRecordPath)
        Else
            ' If the full file path was given, get the record by
            ' issuing a query for it
            strFullPath = objNamedArgs("FilePath")
            Set objIdRecord = GetIdRecordFromFullPath(objWmiService, strFullPath)
        End If
      
        WScript.Echo "Found the ID Record on Server: " & strServer
        Call DisplayWmiObject(objIdRecord)
        
        Dim strRgGuid
        Dim objRfInfo        
        strObjPath = ConstructObjectPath(getResource("DfsrReplicatedFolderInfo"), _
                                         "ReplicatedFolderGuid",                  _
                                         objIdRecord.ReplicatedFolderGuid,        _
                                         wbemCimtypeString)
        Set objRfInfo = objWmiService.Get(strObjPath)
        
        strRgGuid = objRfInfo.ReplicationGroupGuid
        
        Dim objServersBeingProcessedTable
        Dim objServersToProcessTable
        Dim objServersProcessedTable
        
        Dim strServer
        Dim strCreatorDbGuid, strUpdaterDbGuid
        Dim blnMoreServersToSearch
        Dim blnCreatorFound, blnModifierFound
        Dim strCreatorQuery, strUpdaterQuery
        Dim strConnectionQuery
        
        strCreatorDbGuid = GetGuidFromUidOrGvsn(objIdRecord.Uid)
        strUpdaterDbGuid = GetGuidFromUidOrGvsn(objIdRecord.Gvsn)
        
        strCondition = "ReplicationGroupGuid = '" & _
                       EscapeString(strRgGuid) & _
                       "' And Inbound=True"
        strConnectionQuery = _
            ConstructQueryString(Array("PartnerName"), _
                                 getResource("DfsrConnectionConfig"), _
                                 strCondition)
                                 
        strCondition = "DatabaseGuid = '" & _
                       EscapeString(strCreatorDbGuid) & _
                       "'"
        strCreatorQuery = _
            ConstructQueryString(Null, _
                                 getResource("DfsrVolumeInfo"), _
                                 strCondition)
            
        strCondition = "DatabaseGuid = '" & _
                       EscapeString(strUpdaterDbGuid) & _
                       "'"
        strUpdaterQuery = _
            ConstructQueryString(Null, _
                                 getResource("DfsrVolumeInfo"), _
                                 strCondition)
                                 
        Set objServersBeingProcessedTable = _
            CreateObject("Scripting.Dictionary")
        Set objServersToProcessTable = _
            CreateObject("Scripting.Dictionary")            
        Set objServersProcessedTable = _
            CreateObject("Scripting.Dictionary")

        Call objServersBeingProcessedTable.Add(strComputer, strComputer)
        
        blnMoreServersToSearch = True
        blnCreatorFound        = False
        blnModifierFound       = False
        While ( blnMoreServersToSearch And _
                (Not blnCreatorFound   Or _
                Not blnModifierFound) )
            For Each strServer In objServersBeingProcessedTable.Keys
                On Error Resume Next
                ' Connect to the server's DFSR WMI namespace
                ' \\server\root\microsoftdfs
                Set objWmiService = _
                    GetObject("winmgmts:\\" & strServer & getResource("DfsrNamespace"))
                On Error Goto 0
                
                If ( Err.Number = 0 ) Then
                    WScript.Echo "Searching Server: " & strServer
                    Call FindUpdaterAndOrigin(objWmiService, _
                                              strCreatorQuery, _
                                              strUpdaterQuery, _
                                              strConnectionQuery, _
                                              objServersToProcessTable, _
                                              objServersProcessedTable, _
                                              blnCreatorFound, _
                                              blnModifierFound, strServer)
                    If ( Err.Number <> 0 ) Then
                        WScript.Echo "Error searching Server: " & strServer
                        WScript.Echo "Error Code: " & Err.Number & ", Message: " & Err.Description
                        Err.Clear
                    End If
                Else
                    WScript.Echo "Error connecting to Server: " & strServer
                    WScript.Echo "Error Code: " & Err.Number & ", Message: " & Err.Description
                    Err.Clear
                End If

                Call objServersProcessedTable.Add(strServer, strServer)
                
                If ( blnCreatorFound And blnModifierFound ) Then
                    Exit For
                End If
            Next
            
            Call objServersBeingProcessedTable.RemoveAll()
            
            If ( Not blnCreatorFound Or _
                 Not blnModifierFound ) Then
                If ( objServersToProcessTable.Count > 0 ) Then
                    blnMoreServersToSearch = True
                    For Each strServer In objServersToProcessTable.Keys
                        Call objServersBeingProcessedTable.Add(strServer, strServer)
                    Next
                    Call objServersToProcessTable.RemoveAll()
                Else
                    blnMoreServersToSearch = False
                End If
            End If
        Wend
      
        WScript.StdOut.WriteLine
        If ( blnCreatorFound ) Then
            WScript.Echo "File: " & strFullPath & " was created by " & strCreatorName
            Call DisplayWmiObject(objCreatorVolumeInfo)
        Else
            WScript.Echo "File: " & strFullPath & ", Couldn't find creator"
        End If
        
        If ( blnModifierFound ) Then
            WScript.Echo "File: " & strFullPath & " was last modified by " & strUpdaterName
            Call DisplayWmiObject(objUpdaterVolumeInfo)
        Else
            WScript.Echo "File: " & strFullPath & ", Couldn't find last modifier"
        End If
    
    End Sub
  ]]>
 </script>

</job>
```



 

 




