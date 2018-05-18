---
title: Getting the ID Record for a File or Folder
description: VBScript example shows how to use the DfsrIdRecordInfo, DfsrReplicatedFolderConfig, DfsrReplicatedFolderInfo, and DfsrReplicationGroupConfig classes to get the ID record for a file or folder.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'a983c749-828c-4eae-938d-29469ebae0bf'
ms.prod: 'windows-server-dev'
ms.technology:
- 'distributed-file-system-replication'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["Distributed File System Replication examples Files , getting the ID record for a file or folder"]
---

# Getting the ID Record for a File or Folder

The following VBScript example shows how to use the [**DfsrIdRecordInfo**](dfsridrecordinfo.md), [**DfsrReplicatedFolderConfig**](dfsrreplicatedfolderconfig.md), [**DfsrReplicatedFolderInfo**](dfsrreplicatedfolderinfo.md), and [**DfsrReplicationGroupConfig**](dfsrreplicationgroupconfig.md) classes to get the ID record for a file or folder.

To run the script, which is in Windows Script Host (WSH) 2.0 XML file format, save the text in a file with a .wsf extension.


```XML
<?XML version="1.0" standalone="yes" ?>

<job id="FindIdRecord">
 <runtime>
  <description>
   This script uses the DFSR WMI provider to get the ID record for a given file or folder.
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
 <resource id="DfsrReplicatedFolderInfo">DfsrReplicatedFolderInfo</resource>
 <resource id="DfsrIdRecordInfo">DfsrIdRecordInfo</resource>
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
        ' First find the replicated folder corresponding
        ' to this full file path.
        
        ' For this, get all configured replicated folders and
        ' search for a prefix match of the root folder against the
        ' given full file path. Because a proper configuration does not
        ' support root path overlap, you do not have to worry about
        ' longest prefix match.
        
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

        blnFoundTombstoneMatch = False
        For Each objDfsrIdRecordInfo In objObjectSet
            On Error Resume Next
            Dim strIdRecordFullFilePath
            strIdRecordFullFilePath = _
                GetFullFilePathFromIdRecord(objDfsrIdRecordInfo)
            On Error Goto 0
            If ( Right(strIdRecordFullFilePath, 1) = "\" ) Then
                strIdRecordFullFilePath = Left(strIdRecordFullFilePath, Len(strIdRecordFullFilePath)-1)
            End If
            If ( Err.Number = 0 ) Then
                If ( LCase(strIdRecordFullFilePath) = strLcFullFilePath ) Then
                    If ( IsTombstone(objDfsrIdRecordInfo) ) Then
                        Set objTombstoneIdRecordInfo = objDfsrIdRecordInfo
                        blnFoundTombstoneMatch = True
                    Else
                        Set GetIdRecordFromFullPath = objDfsrIdRecordInfo
                        Exit Function
                    End If
                End If
            Else
                Err.Clear
            End If
        Next
        
        If ( blnFoundTombstoneMatch ) Then
            Set GetIdRecordFromFullPath = objTombstoneIdRecordInfo
            Exit Function
        End If
        
        Err.Raise 6672,,"No ID Record found for file path " & strFullFilePath        
    End Function
    
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
        
        Call DisplayWmiObject(objIdRecord)
        If ( Not objNamedArgs.Exists("FilePath") ) Then
            strFullPath = GetFullFilePathFromIdRecord(objIdRecord)
            WScript.Echo "Full File Path: " & strFullPath
        End If
    
    End Sub
   ]]>
 </script>

</job>
```



 

 




