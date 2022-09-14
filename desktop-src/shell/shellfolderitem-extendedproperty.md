---
description: Gets the value of a property from an item's property set. The property can be specified either by name or by the property set's format identifier (FMTID) and property identifier (PID).
ms.assetid: ca787d7b-d95a-45b9-9627-fd505f99f868
title: ShellFolderItem.ExtendedProperty method (Shldisp.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ShellFolderItem.ExtendedProperty
api_type: 
- COM
api_location: 
- Shell32.dll
---

# ShellFolderItem.ExtendedProperty method

Gets the value of a property from an item's property set. The property can be specified either by name or by the property set's format identifier (FMTID) and property identifier (PID).

## Syntax


```JScript
retVal = ShellFolderItem.ExtendedProperty(
  sPropName
)
```



## Parameters

<dl> <dt>

*sPropName* \[in\]
</dt> <dd>

Type: **[**BSTR**](/previous-versions/windows/desktop/automat/bstr)**

A **String** value that specifies the property. See the Remarks section for details.

</dd> </dl>

## Return value

Type: **Variant\***

When this method returns, contains the value of the property, if it exists for the specified item. The value will have full typing—for example, dates are returned as dates, not strings.

This method returns a zero-length string if the property is valid but does not exist for the specified item, or an error code otherwise.

## Remarks

There are two ways to specify a property. The first is to assign the property's well-known name, such as "Author" or "Date", to *sPropName*. However, each property is a member of a Component Object Model (COM) property set and can also be identified by specifying its format ID (FMTID) and property ID (PID). An [**FMTID**](../stg/structured-storage-serialized-property-set-format.md) is a GUID that identifies the property set, and a [**PID**](../stg/structured-storage-serialized-property-set-format.md) is an integer that identifies a particular property within the property set.

Specifying a property by its FMTID/PID values is usually more efficient than using its name. To use a property's FMTID/PID values with **ExtendedProperty**, they must be combined into an SCID. An SCID is a string that contains the FMTID/PID values in the form "*FMTID**PID*", where the FMTID is the string form of the property set's GUID. For example, the SCID of the summary information property set's author property is "{F29F85E0-4FF9-1068-AB91-08002B27B3D9} 4".

For a list of FMTIDs and PIDs that are currently supported by the Shell, see [**SHCOLUMNID**](./objects.md).

## Examples

This sample code illustrates how to use **ExtendedProperty** to retrieve the "Title" and "Author" properties from a Word document. Once you have the [**ShellFolderItem**](shellfolderitem-object.md) object associated with the file, *fiWordDoc* in this example, retrieve the property's value by passing its name to **ExtendedProperty**.


```none
...
Doc_Title=fiWordDoc.ExtendedProperty("DocTitle")
Doc_Author=fiWordDoc.ExtendedProperty("Author")
...
```



A faster and more efficient approach is to pass an SCID to **ExtendedProperty**.


```none
...
FMTID_SummaryInfo="{F29F85E0-4FF9-1068-AB91-08002B27B3D9}"
PID_TITLE="2"
PID_AUTHOR="4"
SCID_TITLE=FMTID_SummaryInfo+" "+PID_TITLE
SCID_AUTHOR=FMTID_SummaryInfo+" "+PID_AUTHOR
Doc_Title=fiWordDoc.ExtendedProperty(SCID_TITLE)
Doc_Author=fiWordDoc.ExtendedProperty(SCID_AUTHOR)
...
```



The following examples show the proper usage of this method for JScript, VBScript, and Visual Basic.

JScript:


```JScript
<script language="JScript">
    function fnFolderItem2ExtendedPropertyJ()
    {
        var objShell = new ActiveXObject("shell.application");
        var objFolder2;
        var ssfWINDOWS = 36;
        
        objFolder2 = objShell.NameSpace(ssfWINDOWS);
        if (objFolder2 != null)
        {
            var objFolderItem;
            
            objFolderItem = objFolder2.ParseName("NOTEPAD.EXE");
            if (objFolderItem != null)
            {
                var szReturn = "";
                
                szReturn = objFolderItem.ExtendedProperty("infotip");
                alert(szReturn);
            }
        }
    }
</script>
```



VBScript:


```VB
<script language="VBScript">
    function fnFolderItemExtendedPropertyVB()
        dim objShell
        
        set objShell = CreateObject("shell.application")
        if (not objShell is nothing) then
            dim objFolder2
            dim ssfWINDOWS
                
            ssfWINDOWS = 36
            set objFolder2 = objShell.NameSpace(ssfWINDOWS)
            if (not objFolder2 is nothing) then
                dim objFolderItem
                        
                set objFolderItem = objFolder2.Self
                if (not objFolderItem is nothing) then
                    dim szReturn
                    
                    szReturn = objFolderItem.ExtendedProperty("type")
                    alert(szReturn)
                end if
                set objFolderItem = nothing
            end if
            set objFolder2 = nothing
        end if
        set objShell = nothing
    end function
 </script>
```



Visual Basic:


```VB
Private Sub fnFolderItem2ExtendedPropertyVB()
    Dim objShell   As Shell
    Dim objFolder2 As Folder2
    Dim ssfWINDOWS As Long
    
    ssfWINDOWS = 36
    Set objShell = New Shell
    Set objFolder2 = objShell.NameSpace(ssfWINDOWS)
        If (Not objFolder2 Is Nothing) Then
            Dim objFolderItem2 As Object
            
            Set objFolderItem2 = objFolder2.ParseName("NOTEPAD.EXE")
                If (Not objFolderItem2 Is Nothing) Then
                    Dim szReturn As String
                    
                    szReturn = objFolderItem2.ExtendedProperty("size")
                    Debug.Print szReturn
                Else
                    'FolderItem object returned nothing.
                End If
            Set objFolderItem2 = Nothing
        Else
            'Folder object returned nothing.
        End If
    Set objFolder2 = Nothing
    Set objShell = Nothing
End Sub
```



## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                                    |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                          |
| Header<br/>                   | <dl> <dt>Shldisp.h</dt> </dl>                          |
| IDL<br/>                      | <dl> <dt>Shldisp.idl</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Shell32.dll (version 5.0 or later)</dt> </dl> |



 

 
