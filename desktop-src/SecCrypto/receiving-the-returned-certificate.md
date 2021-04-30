---
description: Explains how an application receives a certificate.
ms.assetid: 7f87dcf5-b434-4f63-abcd-6873831d22bc
title: Receiving the Returned Certificate
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# Receiving the Returned Certificate

When the certification authority (CA) has verified the requester's identity information and is satisfied that the requester is the owner of the private key and that the data about that requester is accurate, the CA constructs an X.509 certificate, signs it, packages it with any other needed certificates (such as the CA's own certificate) in a message, and sends the message to the requester. The message can be a PKCS \#7 message or a CMC response (V2 templates result in a CMC response).

The receiving application passes the message to the Certificate Enrollment Control. The Certificate Enrollment Control then opens the message and extracts the certificates. The user is prompted with a dialog box asking whether the user will accept self-signed certificates in the "Root" store. If the user accepts the root certificate, the rest of the certificates (except for the requester's certificate) are placed in the "CA" store. The requester's certificate is placed in the certificate store specified by the requester in the [**MyStoreName**](/windows/win32/api/xenroll/nf-xenroll-icenroll-get_mystorename) property.

The following example shows how to use the Visual Basic Scripting Edition (VBScript) and HTML in a webpage to receive and store the returned certificates.


```VB
<HTML>
<TITLE>Certificate Enrollment Acceptance HTML Page
</TITLE>

<OBJECT  classid="clsid:127698E4-E730-4E5C-A2b1-21490A70C8A1"
    CODEBASE="xenroll.dll"
    id=IControl >
</OBJECT>

<SCRIPT language="VBScript">

<!--

Option Explicit 

'Accept the certificate subroutine.

Sub AcceptCertSub

On Error Resume Next

' Get the issued certificate.
' The following value, "PKCS7", represents the received message. 
' Actually, this value must be supplied through the design of
' the receiving application.
' A possible implementation is as follows: after using 
' ICertRequest.Submit to submit the PKCS #10, call 
' ICertRequest.GetLastStatus to confirm successful certificate 
' creation, and then call ICertRequest.GetCertificate to retrieve 
' the certificate.

document.result.result.value = "PKCS7"

    Call IControl.AcceptPKCS7(document.result.result.value)

    If err.Number = 0 Then
        navigate "..\done.htm"
    Else
        Alert "Error: " & Hex(err)
    End If

    End sub

    ' Decline the certificate sub-routine.
    Sub NoAcceptCertSub
    navigate "..\notdone.htm"
    End sub
-->
</SCRIPT>
</BODY>
</HTML>
```



 

 
