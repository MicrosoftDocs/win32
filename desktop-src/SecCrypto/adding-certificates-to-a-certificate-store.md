---
description: Certificates can be added to or removed from certificate stores if the store is opened with read/write permission.
ms.assetid: a1cb6e1e-0702-4f73-827e-3f9e9237b4b6
title: Adding Certificates to a Certificate Store
ms.topic: article
ms.date: 05/31/2018
---

# Adding Certificates to a Certificate Store

\[CAPICOM is a 32-bit only component that is available for use in the following operating systems: Windows Server 2008, Windows Vista, Windows XP. Instead, use the .NET Framework to implement security features. For more information, see [Alternatives to Using CAPICOM](alternatives-to-using-capicom.md).\]

[*Certificates*](../secgloss/c-gly.md) can be added to or removed from [*certificate stores*](../secgloss/c-gly.md) if the store is opened with read/write permission. Read/write permission is not granted to Active Directory stores. While certificates can be added to or removed from memory stores, changes in memory stores are not persisted between sessions.

Certificates can be added to a certificate store that is opened with read/write permission by using the **Add** method. A certificate can be removed from a certificate store that is opened with read/write permission by using the **Remove** method. New stores can be created and saved in the CAPICOM\_CURRENT\_USER\_STORE and CAPICOM\_LOCAL\_MACHINE\_STORE locations. Newly created stores in either of these locations can be opened with read/write permission.

In the following example, two certificate stores are opened. Certificates of subjects with last names beginning with F are retrieved from the Active Directory store. The CAPICOM\_CURRENT\_USER\_STORE, CAPICOM\_CA\_STORE store is then opened as a read/write store and the first certificate from the collection of certificates in the Active Directory store is added to the certificates in the CAPICOM\_CA\_STORE.

For demonstration purposes, the example shows the opening of stores in the CAPICOM\_MEMORY\_STORE, CAPICOM\_CURRENT\_USER\_STORE, and CAPICOM\_LOCAL\_MACHINE\_STORE locations. The example shows exporting all certificates from an open store, writing the exported certificates to a file, reading them back in, and importing them into a different store. The newly imported certificates are them enumerated and displayed.

On any CAPICOM error, a negative decimal value of **Err.Number** is returned. For more information, see [**CAPICOM\_ERROR\_CODE**](capicom-error-code.md). For information about positive decimal values of **Err.Number**, see Winerror.h.

The following example shows opening certificate stores using early binding in the declaration of the **Store** objects and in creating an instance of those objects.


```VB
Sub AddCert()
On Error GoTo ErrorHandler
' The following shows two different ways to declare and
' create a store object.

Dim myADstore As New Store

Dim myCAstore As Store
Set myCAstore = New Store

' In this example, the Active Directory store will be searched for a 
' certificate with a subject name that begins with the letter F. 
' This is done by using the string "SN=F*" as the name of the store.

Dim SubjectNameSN As String
SubjectNameSN = "SN=F*"

' Active Directory stores can only be opened with read-only
' access.

myADstore.Open CAPICOM_ACTIVE_DIRECTORY_USER_STORE,
                SubjectNameSN , CAPICOM_STORE_OPEN_READ_ONLY

'  This example assumes that the store opened and that
'  at least one certificate was returned.
'  A complete application would ensure that at least one certificate
'  was in the store before proceeding and would
'  also select one or more of the certificates returned
'  to be added instead of using the first certificate
'  in the collection.

'  Open the MY store so that a certificate can be added.

myCAstore.Open CAPICOM_CURRENT_USER_STORE, CAPICOM_MY_STORE,
                    CAPICOM_STORE_OPEN_READ_WRITE

myCAstore.Add myADstore.certificates.Item(1)

' Release the two store objects.

Set myCAstore = Nothing
Set myADstore = Nothing
Exit Sub

ErrorHandler:
If Err.Number > 0 Then
    MsgBox "Visual Basic error found:" & Err.Description
Else
    MsgBox "CAPICOM error found : " & Err.Number
End If
End Sub


```



 

 
