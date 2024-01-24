---
description: To decrypt an enveloped message, the recipient matches a certificate from the My store that has an available private key with a certificate in the enveloped message.
ms.assetid: 536f9977-102c-4df9-9d07-97b4b434b845
title: Receiving an Enveloped Data Message
ms.topic: article
ms.date: 05/31/2018
---

# Receiving an Enveloped Data Message

\[CAPICOM is a 32-bit only component that is available for use in the following operating systems: Windows Server 2008, Windows Vista, and Windows XP. Instead, use the .NET Framework to implement security features. For more information, see [Alternatives to Using CAPICOM](alternatives-to-using-capicom.md).\]

To decrypt an enveloped message, the recipient matches a [*certificate*](../secgloss/c-gly.md) from the My store that has an available private key with a certificate in the enveloped message. If a match is found, the encrypted key associated with that certificate is decrypted and that decrypted key is used to decrypt the enveloped message. A message recipient that does not have a matching certificate with an available private key cannot decrypt the message.

In the example that follows, a file name is passed into the subroutine, that file is opened and an enveloped message is read in. The enveloped message is then decrypted. The steps of matching a user certificate with a certificate in the enveloped message, of decrypting the encryption key, and finally of decrypting the message are all done behind the scenes. An error is raised if a certificate match is not found or if the decryption fails.

On any CAPICOM error, a negative decimal value of **Err.Number** is returned. For more information, see [**CAPICOM\_ERROR\_CODE**](capicom-error-code.md). For information about positive decimal values of **Err.Number**, see Winerror.h.


```VB
Sub ReceiveMessage(ByVal InFile As String)
On Error GoTo ErrorHandler

'Declare an EnvelopedData object

Dim Envmessage As New EnvelopedData

'Declare a string variable to hold the encrypted message.

Dim Encrypted As String

' Open an input file and read in the encrypted message
Open InFile For Input As #1
Input #1, Encrypted
Close #1

' If the length of the input string is greater than 0, 
' an encrypted message string is available. Decrypt the message.
' Note: to decrypt the message, a certificate with access to
' a user's private key must be available, and that certificate must
' match one of the certificates in the Recipients collection of 
' certificates.
If Len(Encrypted) > 0 Then
    ' Receive and decrypt the message
    Envmessage.Decrypt encrypted
    
    ' Display the decrypted message.
    MsgBox Envmessage.Content
Else
    MsgBox "No enveloped message was read in."
End If
' Release the EncryptedData object.
Set Envmessage = Nothing
Exit Sub

ErrorHandler:
If Err.Number > 0 Then
    MsgBox "Visual Basic error found:" & Err.Description
Else
    MsgBox "CAPICOM error found : " & Err.Number
End If
End Sub
```



 

 
