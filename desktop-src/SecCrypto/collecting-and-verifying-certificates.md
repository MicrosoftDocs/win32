---
description: In the example that follows, the certificates in a local store are enumerated and checked for validity.
ms.assetid: 59ae22f6-aa6d-4b53-8a27-73e1e5c62755
title: Collecting and Verifying Certificates
ms.topic: article
ms.date: 05/31/2018
---

# Collecting and Verifying Certificates

\[CAPICOM is a 32-bit only component that is available for use in the following operating systems: Windows Server 2008, Windows Vista, and Windows XP. Instead, use the .NET Framework to implement security features. For more information, see [Alternatives to Using CAPICOM](alternatives-to-using-capicom.md).\]

Often a group of [*certificates*](../secgloss/c-gly.md) needs to be collected and verified. This would often be done to prepare a group of recipients for an enveloped message. In the example that follows, the certificates in a local store are enumerated and checked for validity. Next, an Active Directory store is opened to retrieve and add to the local store new certificates. The certificates retrieved from the active directory store are checked for validity and, if valid, are added to the local store. Both stores are then closed.

On any CAPICOM error, a negative decimal value of **Err.Number** is returned. For more information, see [**CAPICOM\_ERROR\_CODE**](capicom-error-code.md). For information about positive decimal values of **Err.Number**, see Winerror.h.

In this example, the name of the local store is passed in as a string parameter. A string indicating the search criteria for certificates in the Active Directory store is also passed in as a parameter.


```VB
Sub CollectValidCerts(ByVal storename As String, ByVal _
    certname As String)

    On Error GoTo errorhandler

    ' Prepare a local certificate store to contain valid
    ' certificates for the recipients of an enveloped
    ' message.

    ' Open the local store and go to the certificates in the store
    '   1. Display the certificate
    '   2. Check the validity of the certificate
    '   3. Remove certificates that are not valid from the store

    Dim LocalStore As New Store
    Dim ADStore As New Store
    Dim i As Long

    LocalStore.Open(CAPICOM_CURRENT_USER_STORE, storename, _
        CAPICOM_STORE_OPEN_READ_WRITE)

    MsgBox("There are " & LocalStore.Certificates.Count & _
        " certificates in this store ")
    For i = 1 To LocalStore.Certificates.Count
        If LocalStore.Certificates.Item(i).IsValid Then
            LocalStore.Certificates.Item(i).Display()
        Else
            MsgBox("A certificate that is not valid was found.")
        End If
    Next i

    ' Open the AD store and retrieve a certificate based
    ' on a string passed into the function. Add any valid
    ' certificates found to the local store.

    ADStore.Open(CAPICOM_ACTIVE_DIRECTORY_USER_STORE, certname, _
        CAPICOM_STORE_OPEN_READ_ONLY)
    MsgBox("There are " & ADStore.Certificates.Count & _
        " certificates in the AD store.")

    For i = 1 To ADStore.Certificates.Count
        If ADStore.Certificates.Item(i).IsValid Then
            ADStore.Certificates.Item(i).Display()
            LocalStore.Add(ADStore.Certificates.Item(i))
        Else
            MsgBox("the certificate from the AD store is not valid.")
        End If
    Next i

    LocalStore = Nothing
    ADStore = Nothing
    MsgBox("Sub finished without error ")
    Exit Sub
errorhandler:
    If Err.Number > 0 Then
        MsgBox("Visual Basic error found:" & Err.Description)
    Else
        MsgBox("CAPICOM error found : " & Err.Number)
    End If
End Sub
```



 

 
