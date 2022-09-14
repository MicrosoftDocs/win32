---
title: Example Code for Adding a Member to a Group
description: This topic contains code examples that add a member to a group.
ms.assetid: 306fcadb-a492-41e5-bfb3-8beaaec24fb5
ms.tgt_platform: multiple
keywords:
- Active Directory examples Active Directory , adding a member to a group
ms.topic: article
ms.date: 05/31/2018
---

# Example Code for Adding a Member to a Group

This topic contains code examples that add a member to a group. The Visual Basic Scripting Edition (VBScript) and C++ examples add a member by adding the [**IADs**](/windows/desktop/api/iads/nn-iads-iads) object that represents the member to the [**IADsGroup**](/windows/desktop/api/iads/nn-iads-iadsgroup) object that represents the group. The Visual Basic .NET and C# examples modify the member property of the [DirectoryEntry](/dotnet/api/system.directoryservices.directoryentry) object that represents the group.


The following C# code examples add an existing member to a group. The function takes the ADsPath of the group container and the distinguished name of the member to be added to the group. The ADsPath is used to create a [DirectoryEntry](/dotnet/api/system.directoryservices.directoryentry) object that represents the group. The [PropertyValueCollection.Add](/dotnet/api/system.directoryservices.propertyvaluecollection.add#System_DirectoryServices_PropertyValueCollection_Add_System_Object_) method adds to the group the member whose distinguished name was passed to the function. The function then uses the [DirectoryEntry.CommitChanges](/dotnet/api/system.directoryservices.directoryentry.commitchanges#System_DirectoryServices_DirectoryEntry_CommitChanges) method to write the new member information to the database.

Call the function with the following parameters:

-   *bindString*: a valid ADsPath for a group container, such as "LDAP://fabrikam.com/CN=TestGroup,OU=TestOU,DC=fabrikam,DC=com"
-   *newMember*: the distinguished name of the member to be added to the group, such as "CN=JeffSmith,OU=TestOU,DC=fabrikam,DC=com"


```CSharp
private void AddMemberToGroup(

                                string bindString,

                                string newMember

                                )

{

    try
    {

        DirectoryEntry ent = new DirectoryEntry( bindString );

        ent.Properties["member"].Add(newMember);

        ent.CommitChanges();

    }

    catch (Exception e)
    {

        Console.WriteLine( "An error occurred.");

        Console.WriteLine( "{0}", e.Message);

        return;

    }

}
```




The following Visual Basic .NET code examples add an existing member to a group. The function takes the ADsPath of the group container and the distinguished name of the member to be added to the group. The ADsPath is used to create a [DirectoryEntry](/dotnet/api/system.directoryservices.directoryentry) object that represents the group. The [PropertyValueCollection.Add](/dotnet/api/system.directoryservices.propertyvaluecollection.add#System_DirectoryServices_PropertyValueCollection_Add_System_Object_) method adds to the group the member whose distinguished name was passed to the function. The function then uses the [DirectoryEntry.CommitChanges](/dotnet/api/system.directoryservices.directoryentry.commitchanges#System_DirectoryServices_DirectoryEntry_CommitChanges) method to write the new member information to the database.

Call the function with the following parameters:

-   *bindString*: a valid ADsPath for a group container, such as "LDAP://fabrikam.com/CN=TestGroup,OU=TestOU,DC=fabrikam,DC=com"
-   *newMember*: the distinguished name of the member to be added to the group, such as "CN=JeffSmith,OU=TestOU,DC=fabrikam,DC=com"


```VB
Private Sub AddMemberToGroup(ByVal bindString As String, 
                                      ByVal newMember As String)

    Try

        Dim ent As New DirectoryEntry(bindString)

        ent.Properties("member").Add(newMember)

        ent.CommitChanges()

    Catch e As Exception

        Console.WriteLine("An error occurred.")

        Console.WriteLine("{0}", e.Message)

        Return

    End Try

End Sub
```




The following VBScript example adds an existing member to a group. The script adds the user, Jeff Smith, to the TestGroup group.


```VB
Option Explicit

On Error Resume Next

Dim scriptResult        ' Script success or failure

Dim groupPath           ' ADsPath to the group container

Dim group               ' Group object

Dim memberPath          ' ADsPath to the member

Dim member              ' Member object

Dim groupMemberList     ' Used to display group members

Dim errorText           ' Error handing text

scriptResult = False

groupPath = "LDAP://fabrikam.com/CN=TestGroup,OU=TestOU,DC=fabrikam,DC=com"

memberPath = "LDAP://CN=JeffSmith,OU=TestOU,DC=fabrikam,DC=com"

WScript.Echo("Retrieving group object")

Set group = GetObject(groupPath)

If Err.number <> vbEmpty then

    Call ErrorHandler("Could not create group object.")

End If

Call ShowMembers(groupPath)     'Optional function call

WScript.Echo("Retrieving new member object")

Set member = GetObject(memberPath)

If Err.number <> vbEmpty then

    Call ErrorHandler("Could not get new member object.")

End If

WScript.Echo("Adding member to group.")

group.Add(member.ADsPath)

If Err.number <> vbEmpty then

    Call ErrorHandler("Could not add member to group.")

End If

Call ShowMembers(groupPath)     ' Optional function call

scriptResult = True

Call FinalResult(scriptResult)

'****************************************************************
' This function displays the members of a group. The function
' takes the ADsPath of the group.
'****************************************************************

Sub ShowMembers(groupPath)

    Dim groupMember

    Dim groupMemberList

    Dim groupObject

    Set groupObject = GetObject(groupPath)

    Set groupMemberList = groupObject.Members

    Select Case groupMemberList.Count

        Case 1 

            WScript.Echo vbcrlf & "The group has one member."

        Case 0

            WScript.Echo vbcrlf & "The group has no members."

        Case Else

            WScript.Echo vbcrlf & "The group has " & groupMemberList.Count & " members."

    End Select

    If groupMemberList.Count > 0 then

        WScript.Echo vbcrlf & "Here is a member list."

        For Each groupMember in groupMemberList

            WScript.Echo groupMember.Name

        Next

        WScript.Echo vbcrlf

    End If

    Set groupObject = Nothing

    Set groupMemberList = Nothing

End Sub

'****************************************************************
' This function shows if the script succeeded or failed. The 
' function processed the scriptResult variable.
'****************************************************************

Sub FinalResult(scriptResult)

    WScript.Echo vbcrlf

    If scriptResult = False then

        WScript.Echo "Script failed."

    Else

        WScript.Echo("Script successfully completed.")

    End If

    WScript.Quit

End Sub

'****************************************************************
' This function handles errors that occur in the script.
'****************************************************************

Sub ErrorHandler( errorText )

    WScript.Echo(vbcrlf & errorText)

    WScript.Echo("Error number: " & Err.number)

    WScript.Echo("Error Description: " & Err.Description)

    Err.Clear 

    Call FinalResult(scriptResult)

End Sub

```




The following C++ code example adds an existing member to a group.


```C++
/////////////////////////////////////////////////////////////
/*  AddMemberToGroup() - Adds the passed directory object as a member 
                         of passed group
 
    Parameters
 
        IADsGroup * pGroup   - Group to hold the new IDirectoryObject.
        IADs* pIADsNewMember - Object which will become a member 
                               of the group. Object can be a user, 
                               contact, or group.
*/
HRESULT AddMemberToGroup(IADsGroup * pGroup, IADs* pIADsNewMember)
{
    HRESULT hr = E_INVALIDARG;
    if ((!pGroup)||(!pIADsNewMember))
        return hr;
 
    // Use the IADs::get_ADsPath() member to get the ADsPath.
    // When the ADsPath string is returned, to add the new
    // member to the group, call the IADsGroup::Add() member,
    // passing in the ADsPath string.
    // Query the new member for its AdsPath.
    // This is a fully qualified LDAP path to the object to add.
    BSTR bsNewMemberPath;
    hr = pIADsNewMember->get_ADsPath(&bsNewMemberPath); 
    if (SUCCEEDED(hr))
    {
 
        // Use the IADsGroup interface to add the new member.
        // Pass the LDAP path to the 
        // new member to the IADsGroup::Add() member
        hr = pGroup->Add(bsNewMemberPath);
 
        // Free the string returned from IADs::get_ADsPath()
        SysFreeString(bsNewMemberPath);
    }
    return hr;
}
```



## Related topics

<dl> <dt>

[Adding Members to Groups in a Domain](adding-members-to-groups-in-a-domain.md)
</dt> <dt>

[DirectoryEntry](/dotnet/api/system.directoryservices.directoryentry)
</dt> <dt>

[DirectoryEntry.CommitChanges](/dotnet/api/system.directoryservices.directoryentry.commitchanges#System_DirectoryServices_DirectoryEntry_CommitChanges)
</dt> <dt>

[**IADs**](/windows/desktop/api/iads/nn-iads-iads)
</dt> <dt>

[**IADsGroup**](/windows/desktop/api/iads/nn-iads-iadsgroup)
</dt> <dt>

[PropertyValueCollection.Add](/dotnet/api/system.directoryservices.propertyvaluecollection.add#System_DirectoryServices_PropertyValueCollection_Add_System_Object_)
</dt> </dl>

 

 