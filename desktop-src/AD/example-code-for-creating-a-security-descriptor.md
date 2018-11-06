---
title: Example Code for Creating a Security Descriptor
description: This topic includes a Visual Basic code example that shows you how to create a security descriptor object for an ADSI object.
ms.assetid: 7c6dcdaf-0bef-4f72-bd9d-dc3ab4295008
ms.tgt_platform: multiple
keywords:
- Example Code for Creating a Security Descriptor
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# Example Code for Creating a Security Descriptor

This topic includes a Visual Basic code example that shows you how to create a security descriptor object for an ADSI object.


```VB
' This code example assumes that you have the credentials
' required to create objects.
Dim MyObject As IADs
Dim MySecDes As SecurityDescriptor
Dim Var As Variant
Dim SecDes As New SecurityDescriptor
Dim Dacl As New AccessControlList
Dim Ace As New AccessControlEntry

On Error GoTo Cleanup
 
' Create an Access Control Entry (ACE) for Group objects
' at Fabrikam on an LDAP namespace. 
Ace.AccessMask = 0
Ace.AceType = 1
Ace.AceFlags = 1
Ace.Trustee = "cn=Groups,o=Fabrikam"
 
' Add the new ACE object as the only ACE in a new
' access-control list (ACL).
Dacl.AceCount = 1
Dacl.AclRevision = 4
Dacl.AddAce Ace
 
' Use this ACL as the discretionary ACL (DACL) for
' this Security Descriptor object and use this DACL
' instead of the default. 
SecDes.Revision = 1
SecDes.OwnerDefaulted = True
SecDes.GroupDefaulted = True
SecDes.DaclDefaulted = False
SecDes.SaclDefaulted = True
SecDes.DiscretionaryAcl = Dacl

' Attach this security descriptor to the ADSI object.
MyObject.Put "ntSecurityDescriptor", SecDes
' Commit the changes to the underlying directory service.
MyObject.SetInfo
' Read the properties back in to the property cache.
MyObject.GetInfo
' Get the SecurityDescriptor object.
Set MySecDes = MyObject.Get("ntSecurityDescriptor")

Cleanup:
    If (Err.Number<>0) Then
        MsgBox("An error has occurred. " & Err.Number)
    End If
    Set MyObject = Nothing
    Set MySecDes = Nothing
    Set SecDes = Nothing
    Set Dacl = Nothing
    Set Ace = Nothing
```



 

 




