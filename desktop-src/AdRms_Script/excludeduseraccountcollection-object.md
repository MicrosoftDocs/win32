---
Description: 'Contains a collection of ExcludedUserAccount objects that represent users for which new end-user licenses and client licensor certificates cannot be issued.'
audience: developer
author: 'REDMOND\\markl'
manager: 'REDMOND\\mbaldwin'
ms.assetid: 'a6464ff6-c1bd-42e5-bf52-1af65e491fff'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-rights-management'
ms.tgt_platform: multiple
title: ExcludedUserAccountCollection object
---

# ExcludedUserAccountCollection object

The **ExcludedUserAccountCollection** object contains a collection of [**ExcludedUserAccount**](excludeduseraccount-object.md) objects that represent users for which new end-user licenses and client licensor certificates cannot be issued. You can retrieve this collection by calling the [**UserAccounts**](exclusionpolicy-useraccounts-property.md) property on the [**ExclusionPolicy**](exclusionpolicy-object.md) object.

## Members

The **ExcludedUserAccountCollection** object has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **ExcludedUserAccountCollection** object has these methods.



| Method                                                          | Description                                                                                                                                                          |
|:----------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Add](http://go.microsoft.com/fwlink/p/?linkid=87269)           | Adds an object to the collection (inherited from [IList](http://go.microsoft.com/fwlink/p/?linkid=87268)).<br/>                                                |
| [Clear](http://go.microsoft.com/fwlink/p/?linkid=87270)         | Removes all objects from the collection (inherited from [IList](http://go.microsoft.com/fwlink/p/?linkid=87268)).<br/>                                         |
| [Contains](http://go.microsoft.com/fwlink/p/?linkid=87271)      | Determines whether the collection contains a specific object (inherited from [IList](http://go.microsoft.com/fwlink/p/?linkid=87268)).<br/>                    |
| [CopyTo](http://go.microsoft.com/fwlink/p/?linkid=87281)        | Copies the collection elements to an array, starting at a specified index (inherited from [ICollection](http://go.microsoft.com/fwlink/p/?linkid=87282)).<br/> |
| [IndexOf](http://go.microsoft.com/fwlink/p/?linkid=87273)       | Retrieves the index of a specific object in the collection (inherited from [IList](http://go.microsoft.com/fwlink/p/?linkid=87268)).<br/>                      |
| [Insert](http://go.microsoft.com/fwlink/p/?linkid=87274)        | Inserts an object in the collection at the specified index (inherited from [IList](http://go.microsoft.com/fwlink/p/?linkid=87268)).<br/>                      |
| [**Refresh**](excludeduseraccountcollection-refresh-method.md) | Refreshes the collection from the collection saved on the server.<br/>                                                                                         |
| [Remove](http://go.microsoft.com/fwlink/p/?linkid=87276)        | Removes the first occurrence of the specified object from the collection (inherited from [IList](http://go.microsoft.com/fwlink/p/?linkid=87268)).<br/>        |
| [RemoveAt](http://go.microsoft.com/fwlink/p/?linkid=87277)      | Removes the object at the specified index from the collection (inherited from [IList](http://go.microsoft.com/fwlink/p/?linkid=87268)).<br/>                   |



 

### Properties

The **ExcludedUserAccountCollection** object has these properties.



| Property                                                                     | Description                                                                                                                                            |
|:-----------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Count](http://go.microsoft.com/fwlink/p/?linkid=87280)<br/>           | Retrieves the number of objects contained in the collection (inherited from [ICollection](http://go.microsoft.com/fwlink/p/?linkid=87282)).<br/> |
| [**Enabled**](excludeduseraccountcollection-enabled-property.md)<br/> | Specifies or retrieves a Boolean value that indicates whether the collection is enabled.<br/>                                                    |
| [Item](http://go.microsoft.com/fwlink/p/?linkid=87278)<br/>            | Specifies or retrieves the object at the specified index (inherited from [IList](http://go.microsoft.com/fwlink/p/?linkid=87268)).<br/>          |



 

## Examples


```VB
DIM config_manager
DIM admin_role

' *******************************************************************
' Create and initialize a ConfigurationManager object.

SUB InitObject()

  CALL WScript.Echo( "Create ConfigurationManager object...")
  SET config_manager = CreateObject _
    ("Microsoft.RightsManagementServices.Admin.ConfigurationManager")      
  CheckError()
    
  CALL WScript.Echo( "Initialize...")
  admin_role=config_manager.Initialize(false,"localhost",80,"","","")
  CheckError()

END SUB

' *******************************************************************
' Exclude user accounts.

SUB ExcludeUser()

  DIM exclusionPolicy
  DIM excludedUser
  DIM excludedUserColl   

  ' Retrieve the ExclusionPolicy object.
  SET exclusionPolicy = config_manager.Enterprise.ExclusionPolicy
  CheckError()

  ' Create an ExcludedUserAccount object.
  SET excludedUser = CreateObject( _
    "Microsoft.RightsManagementServices.Admin.ExcludedUserAccount")
  CheckError()

  ' Set the user ID.
  excludedUser.UserId = "someone@example.com"
  CheckError()

  ' Identify the excluded public key.
  excludedUser.PublicKey = "D3QgTm9y1ujYqiy4tocvmnyvnlp" _
        & "kthp5+TrtF94qJN/I38bxALpAj9ExB4Do6P+rHWvMR+0HztV7Yelo" _
        & "B3r2IlX2lQYe7mxZwnF2D5/7GUzPj5hKxCT/By55tX3Bzs4Eno7cX" _
        & "fTeJ6mnMDO+KyjNoObg9kPRCy2hmHhj2ftRvLk="
  CheckError()

  ' Retrieve the ExcludedUSerAccountCollection object.
  SET excludedUserColl = exclusionPolicy.UserAccounts
  CheckError()

  ' Enable the collection.
  excludedUserColl.Enabled = TRUE

  ' Add the new user account to the collection.
  excludedUserColl.Add( excludedUser )
  CheckError()

END SUB

' *******************************************************************
' Error checking function.

FUNCTION CheckError()
  CheckError = Err.number
  IF Err.number <> 0 THEN
    CALL WScript.Echo( vbTab & "*****Error Number: " _
                       & Err.number _
                       & " Desc:" _
                       & Err.Description _
                       & "*****")
    WScript.StdErr.Write(Err.Description)
    WScript.Quit( Err.number )
  END IF
END FUNCTION
```



## Requirements



|                                     |                                                                                                                         |
|-------------------------------------|-------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                                               |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                                          |
| Assembly<br/>                 | <dl> <dt>Microsoft.RightsManagementServices.Admin.dll</dt> </dl> |



## See also

<dl> <dt>

[Active Directory Rights Management Services Scripting API Reference](active-directory-rights-management-services-scripting-api-reference.md)
</dt> </dl>

 

 




