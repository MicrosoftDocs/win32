---
description: A document can be signed by more than one signer.
ms.assetid: f81cbf7b-317d-4fab-9b30-88b6c6576db8
title: Cosigning a Document
ms.topic: article
ms.date: 05/31/2018
---

# Cosigning a Document

\[CAPICOM is a 32-bit only component that is available for use in the following operating systems: Windows Server 2008, Windows Vista, and Windows XP. Instead, use the .NET Framework to implement security features. For more information, see [Alternatives to Using CAPICOM](alternatives-to-using-capicom.md).\]

A document can be signed by more than one signer. This happens when, for instance, two or more parties sign a contract or an expense report. In the following example, a document already signed is received by a second signer. This signer uses the [**CoSign**](signeddata-cosign.md) method to attach an additional signature to the document.

If any CAPICOM error occurs, a negative value is returned in the **Err.Number** property. For more information about CAPICOM error codes, see [**CAPICOM\_ERROR\_CODE**](capicom-error-code.md). If the error code in the **Err.Number** property is a positive value, then the error is a Windows error. For information about Windows error codes, see Winerror.h.

> [!Note]
> Cosigning a document also requires that the cosigner have an available [*certificate*](../secgloss/c-gly.md) with a [*private key*](../secgloss/p-gly.md) to create the signature. If a signer is not specified in the call of the [**Sign**](signeddata-sign.md) method and there is no certificate in CAPICOM\_MY\_STORE with an associated private key, the method fails. If there is one and only one certificate in CAPICOM\_MY\_STORE with an associated private key, that key and certificate are used. If there is more than one usable certificate, a prompt is displayed to allow the user to choose the desired certificate.
> 
> If the [**CoSign**](signeddata-cosign.md) method is used in a web-based application, a prompt is always displayed to get the user's permission before a signature is created by using that signer's private key.

 

In the following example, files that contain the document to be signed and the current signatures on that document are read, the signature is cosigned, and the new signature is written to a file. The example uses a detached signature with the data signed and the signature in separate files.


```VB
Sub CoSignContent(ByVal InputFile1Name As String, ByVal _
    InputFile2Name As String, ByVal OutputFileName As String)

    On Error GoTo ErrorHandler
    Dim c As String
    Dim s As String
    Dim CS As String
    Dim Signobj As New SignedData
    Open InputFile1Name for Input as #1
    Input #1, s
    Close #1
    Open InputFileName2 for input as #2
    Input #2, c 
    Close #2

    Signobj.Content = c
    Signobj.Verify(s)
    CS = Signobj.CoSign
    Open OutputFileName for output as #3
    Write #3, CS
    Close # 3
    Signobj = Nothing
    MsgBox("Cosign finished. Cosignature saved to a file.")
    Exit Sub
ErrorHandler:
    If err.number > 0 Then
        MsgBox("Visual Basic error found:" & err.description)
    Else
        MsgBox("CAPICOM error found : " & err.number)
    End If
End Sub
```



 

 
