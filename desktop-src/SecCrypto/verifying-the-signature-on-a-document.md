---
description: When a signed document is received, the validity of the signature or signatures can be checked.
ms.assetid: 088915d8-768c-4378-a9dd-9347a428aff9
title: Verifying the Signature on a Document
ms.topic: article
ms.date: 05/31/2018
---

# Verifying the Signature on a Document

\[CAPICOM is a 32-bit only component that is available for use in the following operating systems: Windows Server 2008, Windows Vista, and Windows XP. Instead, use the .NET Framework to implement security features. For more information, see [Alternatives to Using CAPICOM](alternatives-to-using-capicom.md).\]

When a signed document is received, the validity of the signature or signatures can be checked. A signature can be checked for:

-   Validity of the signature hash
-   Validity of the signer's certificate

The signature [*hash*](../secgloss/h-gly.md) is decrypted using the [*public key*](../secgloss/p-gly.md) of the signer found on the signer's [*certificate*](../secgloss/c-gly.md), included as part of the signature. If the decrypted signature matches a new hash of the original document, the signature was created by the owner of the private key associated with the public key used to decrypt the hash. In addition, the document that the signature is based on is guaranteed not to have been changed after the signature was created.

The certificate that provided the public key and the identity of the signer can also be checked for validity including such issues as whether the certificate has been revoked, whether the certificate is out of date, or whether the certificate was issued by a trusted certificate issuer.

In the following example, the content signed and the **SignedData** object are read in from a file and the signature and the validity of the certificate used to create the signature are checked.

> [!Note]  
> If the signature is not cryptographically valid or the certificate of the signer is not valid, an exception is raised and the verifying program must handle the exception. On any CAPICOM error, a negative decimal value of **Err.Number** is returned. For more information, see [**CAPICOM\_ERROR\_CODE**](capicom-error-code.md). For information about positive decimal values of **Err.Number**, see Winerror.h.

 


```VB
Sub VerifySig(ByVal FileToVerify As String, ByVal FileBase As String)
On Error GoTo ErrorHandler

Dim sdContent As String
Dim sdCheck As String
Dim mySD As SignedData
Set mySD = New SignedData

' Open a file and read the signature.
Open FileToVerify For Input As #1
Input #1, sdCheck
Close #1

' Open a file and input the plaintext content that was signed.
Open FileBase For Input As #2
Input #2, sdContent
Close #1

' Set the detached content upon which the signature is based.
mySD.Content = sdContent

' Verify the detached signature.
On Error Resume Next
    mySD.Verify sdCheck, True
If Err.Number <> 0 Then
    MsgBox "Signature verification failed. " & Err.Description
Else
    MsgBox "Verification complete."
End If

' Release the SignedData object.
Set mySD = Nothing

Exit Sub
ErrorHandler:
    If Err.Number > 0 Then
        MsgBox "Visual Basic error found: " & Err.Description
    Else
        MsgBox "CAPICOM error found: " & Hex(Err.Number)
    End If
End Sub

```



 

 
