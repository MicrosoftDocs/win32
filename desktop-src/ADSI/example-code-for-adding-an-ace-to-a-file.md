---
title: Example Code for Adding an ACE to a File
description: The following code example shows how to use the IADsSecurityUtility interface to add an ACE to a file.
ms.assetid: d47d3ebe-cc14-412d-be27-841e25b43c3a
ms.tgt_platform: multiple
keywords:
- Example Code for Adding an ACE to a File ADSI
ms.topic: article
ms.date: 05/31/2018
---

# Example Code for Adding an ACE to a File

The following code example shows how to use the [**IADsSecurityUtility**](/windows/desktop/api/Iads/nn-iads-iadssecurityutility) interface to add an ACE to a file.


```VB
' Define constants:
'

'++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
'
' Define the ADS_RIGHTS_ENUM values.
'
Const ADS_RIGHT_DELETE = &H10000
Const ADS_RIGHT_READ_CONTROL = &H20000
Const ADS_RIGHT_WRITE_DAC = &H40000
Const ADS_RIGHT_WRITE_OWNER = &H80000
Const ADS_RIGHT_SYNCHRONIZE = &H100000
Const ADS_RIGHT_ACCESS_SYSTEM_SECURITY = &H1000000
Const ADS_RIGHT_GENERIC_READ = &H80000000
Const ADS_RIGHT_GENERIC_WRITE = &H40000000
Const ADS_RIGHT_GENERIC_EXECUTE = &H20000000
Const ADS_RIGHT_GENERIC_ALL = &H10000000
Const ADS_RIGHT_DS_CREATE_CHILD = &H1
Const ADS_RIGHT_DS_DELETE_CHILD = &H2
Const ADS_RIGHT_ACTRL_DS_LIST = &H4
Const ADS_RIGHT_DS_SELF = &H8
Const ADS_RIGHT_DS_READ_PROP = &H10
Const ADS_RIGHT_DS_WRITE_PROP = &H20
Const ADS_RIGHT_DS_DELETE_TREE = &H40
Const ADS_RIGHT_DS_LIST_OBJECT = &H80
Const ADS_RIGHT_DS_CONTROL_ACCESS = &H100
'++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
'
' Ace Type definitions
'
Const ADS_ACETYPE_ACCESS_ALLOWED = 0
Const ADS_ACETYPE_ACCESS_DENIED = &H1
Const ADS_ACETYPE_SYSTEM_AUDIT = &H2
Const ADS_ACETYPE_ACCESS_ALLOWED_OBJECT = &H5
Const ADS_ACETYPE_ACCESS_DENIED_OBJECT = &H6
Const ADS_ACETYPE_SYSTEM_AUDIT_OBJECT = &H7
'++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
'
' Ace Flag Constants
'
Const ADS_ACEFLAG_UNKNOWN = &H1
Const ADS_ACEFLAG_INHERIT_ACE = &H2
Const ADS_ACEFLAG_NO_PROPAGATE_INHERIT_ACE = &H4
Const ADS_ACEFLAG_INHERIT_ONLY_ACE = &H8
Const ADS_ACEFLAG_INHERITED_ACE = &H10
Const ADS_ACEFLAG_VALID_INHERIT_FLAGS = &H1F
Const ADS_ACEFLAG_SUCCESSFUL_ACCESS = &H40
Const ADS_ACEFLAG_FAILED_ACCESS = &H80
'++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
'
' Flags constants for AD objects
'
Const ADS_FLAG_OBJECT_TYPE_PRESENT = &H1
Const ADS_FLAG_INHERITED_OBJECT_TYPE_PRESENT = &H2
'++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
'
' From Winnt.h
'------------------------------------------------------------------------------
'++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
' File Specific Access Rights
'
Const DELETE = &H10000
Const READ_CONTROL = &H20000
Const WRITE_DAC = &H40000
Const WRITE_OWNER = &H80000
Const SYNCHRONIZE = &H100000

Const STANDARD_RIGHTS_REQUIRED = &HF0000

Const STANDARD_RIGHTS_READ = READ_CONTROL
Const STANDARD_RIGHTS_WRITE = READ_CONTROL
Const STANDARD_RIGHTS_EXECUTE = READ_CONTROL

Const STANDARD_RIGHTS_ALL = &H1F0000

Const SPECIFIC_RIGHTS_ALL = &HFFFF

'
'  AccessSystemAcl access type
'

Const ACCESS_SYSTEM_SECURITY = &H1000000

'
'  MaximumAllowed access type
'

Const MAXIMUM_ALLOWED = &H2000000

'
'  These are the generic rights
'

Const GENERIC_READ = &H80000000
Const GENERIC_WRITE = &H40000000
Const GENERIC_EXECUTE = &H20000000
Const GENERIC_ALL = &H10000000

'
' AccessMask constants for FILE ACEs
'
Const FILE_READ_DATA = &H1                  '  file & pipe
Const FILE_LIST_DIRECTORY = &H1             '  directory

Const FILE_WRITE_DATA = &H2                 '  file & pipe
Const FILE_ADD_FILE = &H2                   '  directory

Const FILE_APPEND_DATA = &H4                '  file
Const FILE_ADD_SUBDIRECTORY = &H4           '  directory
Const FILE_CREATE_PIPE_INSTANCE = &H4       '  named pipe

Const FILE_READ_EA = &H8                    '  file & directory

Const FILE_WRITE_EA = &H10                  '  file & directory

Const FILE_EXECUTE = &H20                   '  file
Const FILE_TRAVERSE = &H20                  '  directory

Const FILE_DELETE_CHILD = &H40              '  directory

Const FILE_READ_ATTRIBUTES = &H80           '  all

Const FILE_WRITE_ATTRIBUTES = &H100         '  all

Const FILE_ALL_ACCESS = STANDARD_RIGHTS_REQUIRED Or SYNCHRONIZE Or &H1FF

Const FILE_GENERIC_READ = STANDARD_RIGHTS_READ Or _
    FILE_READ_DATA Or _
    FILE_READ_ATTRIBUTES Or _
    FILE_READ_EA Or _
    SYNCHRONIZE



Const FILE_GENERIC_WRITE = STANDARD_RIGHTS_WRITE Or _
    FILE_WRITE_DATA Or _
    FILE_WRITE_ATTRIBUTES Or _
    FILE_WRITE_EA Or _
    FILE_APPEND_DATA Or _
    SYNCHRONIZE

Const FILE_GENERIC_EXECUTE = STANDARD_RIGHTS_EXECUTE Or _
    FILE_READ_ATTRIBUTES Or _
    FILE_EXECUTE Or _
    SYNCHRONIZE

Const FILE_SHARE_READ = &H1
Const FILE_SHARE_WRITE = &H2
Const FILE_SHARE_DELETE = &H4
'
' AceFlags values for files
'
Const OBJECT_INHERIT_ACE = &H1
Const CONTAINER_INHERIT_ACE = &H2
Const NO_PROPAGATE_INHERIT_ACE = &H4
Const INHERIT_ONLY_ACE = &H8
Const INHERITED_ACE = &H10
  
'++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
'
'<<<<<<<<<<<<<<<<<<<<<<<<< BEGIN IADsSecurityUtility Constants >>>>>>>>>>>>
'
'
' ADS_PATHTYPE_ENUM
'
Const ADS_PATH_FILE = 1
Const ADS_PATH_FILESHARE = 2
Const ADS_PATH_REGISTRY = 3
'
' ADS_SD_FORMAT_ENUM
'
Const ADS_SD_FORMAT_IID = 1
Const ADS_SD_FORMAT_RAW = 2
Const ADS_SD_FORMAT_HEXSTRING = 3
'
'<<<<<<<<<<<<<<<< END IADsSecurityUtility Constants >>>>>>>>>>>>>>>>>>>>>
'

'++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
'
' AddACEToFile
'
' Adds an ACE to the specified file or folder that grants the trustee
' modify rights on the file.
'
Public Sub AddACEToFile(File As String, Trustee As String)
    Dim oAce As AccessControlEntry  ' variable for the new ACE
    Dim oSD As SecurityDescriptor   ' variable for the Security Descriptor of the object
    Dim oDacl As AccessControlList  ' variable for the DACL of the object
    Dim oADsSecurityUtility As ADsSecurityUtility
    '
    ' Create an ADsSecurityUtlity object.
    '
    Set oADsSecurityUtility = CreateObject("ADsSecurityUtility")
    '
    ' Get the Security Descriptor for the given NTFS File path.
    '
    Set oSD = oADsSecurityUtility.GetSecurityDescriptor(File, ADS_PATH_FILE, ADS_SD_FORMAT_IID)
    '
    ' Get the discretionary ACL for the key.
    '
    Set oDacl = oSD.DiscretionaryAcl
    '
    ' Create an ACE object.
    '
    Set oAce = CreateObject("AccessControlEntry")
    '
    ' Set the IADsAccessControlEntry::Trustee attribute.
    '
    oAce.Trustee = Trustee
    '
    ' Set the IADsAccessControlEntry::AccessMask attribute.
    '
    oAce.AccessMask = FILE_GENERIC_READ Or _
                        FILE_GENERIC_WRITE Or _
                        FILE_GENERIC_EXECUTE Or _
                        DELETE
    '
    ' Set the IADsAccessControlEntry::AceType attribute.
    '
    oAce.AceType = ADS_ACETYPE_ACCESS_ALLOWED
    '
    ' Set the IADsAccessControlEntry::AceFlags attribute.
    '
    oAce.AceFlags = OBJECT_INHERIT_ACE Or _
                        CONTAINER_INHERIT_ACE
    '
    ' Place the ACE on the DACL.
    '
    oDacl.AddACE oAce
    '
    ' Place the DACL back onto the SD.
    '
    oSD.DiscretionaryAcl = oDacl
    '
    ' Place the SD back onto the file.
    '
    oADsSecurityUtility.SetSecurityDescriptor File, ADS_PATH_FILE, oSD, ADS_SD_FORMAT_IID
    '
    ' Cleanup.
    '
    Set oAce = Nothing
    Set oDacl = Nothing
    Set oSD = Nothing
    Set oADsSecurityUtility = Nothing
End Sub
```



 

 




