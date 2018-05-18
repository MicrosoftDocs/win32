---
title: Smart Card Enrollment Control Example
description: HTML script depicts a basic example using the Smart Card Enrollment Control. The example uses Visual Basic Scripting Edition (VBScript).
ms.assetid: '2a4e6fb2-1bf0-415d-9cb0-7a987f422b2a'
keywords: ["Smart Card API Smart Card , example", "Smart Card Enrollment Control example Smart Card"]
---

# Smart Card Enrollment Control Example

This topic is not current. For the most current information about the Smart Card API, see [Smart Card Minidriver Specification](http://go.microsoft.com/fwlink/p/?linkid=178045).

The following HTML script depicts a basic example using the Smart Card Enrollment Control. The example uses Visual Basic Scripting Edition (VBScript).


```VB
<HTML>
<TITLE>Microsoft Smart Card Enrollment Control Demonstration
</TITLE>

<OBJECT classid="clsid:c2bbea20-1f2b-492f-8a06-b1c5ffeace3b"
    CODEBASE="scrdenrl.dll"
    id=Senroll >
</OBJECT>

<B>Microsoft Smart Card Enrollment Control</B>

<SCRIPT language="VBScript">
<!--
' The following subroutines are contained in this script:
' ChangeCSP - called when the user specifies the CSP.
' ChangeCT - called when the user specifies the certificate template name.
' CTType_OnClick - called when the certificate template type changes.
' EnableEnroll - enables or disables the 'Enroll' button.
' Enroll_OnClick - enrolls for a certificate.
' GetSign_OnClick - selects a signing certificate.
' GetUser_OnClick - invokes the 'Select user' dialog box.
' Initialize - executes when the script is downloaded to the client.
' RemoveItems - empties a list box.
' Reset_OnClick - resets the user name.
' UpdateCA - displays the certificate authorities in a list box.
' UpdateCSP - displays the crypto service providers in a list box.
' UpdateCT - displays the certificate templates in a list box.
' ViewCert_OnClick - displays the enrolled certificate.

Option Explicit
' Variables to determine whether the necessary information
' has been provided by the administrator. These variables
' determine whether the 'Enroll' button is enabled or disabled.
Dim CSP_OK      ' Cryptographic Service Provider specified.
Dim SignCert_OK ' Signing Certificate specified.
Dim CT_OK       ' Certificate template specified.
Dim CA_OK       ' Certification authority specified.
Dim User_OK     ' User name specified.

' Consts
Const SCARD_ENROLL_USER_CERT_TEMPLATE = &amp;H1
Const SCARD_ENROLL_MACHINE_CERT_TEMPLATE = &amp;H2
Const SCARD_ENROLL_UPN_NAME = 1
Const SCARD_ENROLL_SAM_COMPATIBLE_NAME = 2
Const SCARD_ENROLL_CA_MACHINE_NAME = &amp;H1
Const SCARD_ENROLL_NO_DISPLAY_CERT = &amp;H1


sub ChangeCSP
    Senroll.CSPName = document.SCEnrForm.CSP.value
end sub

sub ChangeCT
    Senroll.setCertTemplateName 0, document.SCEnrForm.CT.value
    Call UpdateCA()
end sub

sub CTType_OnClick
    ' The certificate template type changed;
    ' update the list of certificate templates accordingly.
    Call UpdateCT()
end sub

sub EnableEnroll()
    ' This procedure enables the "Enroll" button if the necessary 
    ' information has been entered. This gets called whenever a
    ' change occurs to the CSP, SigningCert, CT or User.
    ' This does not get called when the CA is changed because
    ' a change to the CT determines the availability of a CA.
    Dim Data_OK
    Data_OK = CSP_OK And SignCert_OK And CT_OK And CA_OK And User_OK
    document.SCEnrForm.Enroll.disabled = Not Data_OK
end sub

sub Enroll_OnClick
    Senroll.enroll(0)
    ' Allow the resulting cert to be viewed.
    SCEnrForm.ViewCert.disabled=False
end sub

sub GetSign_OnClick
    Dim strSignCert
    
    ' Select the EnrollmentAgent signing certificate.
    Senroll.selectSigningCertificate 0, "EnrollmentAgent"

    ' Retrieve the name of the signing certificate
    ' without displaying the cert user interface.
    strSignCert = Senroll.getSigningCertificateName(SCARD_ENROLL_NO_DISPLAY_CERT)

    If ( "" <> strSignCert ) Then
        document.SCEnrForm.SignCert.value = strSignCert
        SignCert_OK = True
    Else
        SignCert_OK = False
    End If

    ' Updated SignCert_OK flag.
    Call EnableEnroll()
end sub

sub GetUser_OnClick
    Dim strUser
    ' Clear user/certificate info.
    call Reset_OnClick()
    ' Invoke the 'Select user' dialog box.
    Senroll.selectUserName(0)
    ' Retrieve the user name.
    strUser = Senroll.getUserName(0)
    If ( "" <> strUSer ) Then
        ' Display the user name in the form.
        document.SCEnrForm.User.Value = strUser
        ' Allow the administrator to clear this user info.
        document.SCEnrForm.Reset.disabled = False
        User_OK = True
        ' Because User_OK changed, call EnableEnroll().
        Call EnableEnroll()
    End If
end sub

sub Initialize
    ' Set the information variables to false.
    CSP_OK      = false
    SignCert_OK = false
    CT_OK       = false
    CA_OK       = false
    User_OK     = false

    ' Update the CSP list box.
    Call UpdateCSP()

    ' Update the certificate template list box.
    Call UpdateCT()

    ' Instruct the administrator to select a signing cert. 
    document.SCEnrForm.SignCert.Value = "Select a signing certificate"
    ' Instruct the administrator to select a user.
    document.SCEnrForm.User.Value = "Select a user"
end sub

' Remove all elements of a list box.
sub RemoveItems( List1 )
   Dim nCount, nIndex, LB
    
   ' Determine which list box is being emptied.
   Select Case List1
       Case "CA"
           set LB = document.SCEnrForm.CA
       Case "CT"
           set LB = document.SCEnrForm.CT
       Case Else
           Exit Sub
   End Select

  ' Remove items in a loop.
  nCount = LB.length
  For nIndex = 0 to nCount - 1
      LB.Remove 0
  Next
end sub

sub Reset_OnClick
    Senroll.resetUser()
    document.SCEnrForm.User.Value = "Select a user"

    ' Disable this button (it will be enabled when a user is selected).
    document.SCEnrForm.Reset.disabled = True

    ' Disable the ViewCert button because 
    ' the resetUser() method removes the cert from memory.
    SCEnrForm.ViewCert.disabled=True

    User_OK = False
    ' Disable enroll button.
    Call EnableEnroll()
end sub

sub UpdateCA
    ' Update the list of CAs.
    ' This will be called every time a different Cert Template is selected.
    Dim nCount, nIndex, strCTName, Element
    
    ' Empty the list of CAs currently displayed.
    RemoveItems("CA")

    ' List the CAs for the current certificate template.  
    strCTName = Senroll.getCertTemplateName( 0 )
    nCount = Senroll.getCACount(strCTName)
    If ( 0 = nCount ) Then
        CA_OK = False
        MsgBox("No certification authority is available for the specified certificate template.")
    Else
        ' At least one CA exists.
        CA_OK = True
        ' Populate the list of CAs.
        For nIndex = 0 To nCount - 1
            Set Element=document.createElement("OPTION")
            Element.text=Senroll.enumCAName( nIndex, 0, strCTName )
            Element.value=Element.text
            document.SCEnrForm.CA.Options.Add Element
        Next
        ' Select the top element in the list.
        document.SCEnrForm.CA.selectedIndex=0
    End If
end sub

sub UpdateCSP
    Dim nCount, nIndex, Element
    
    ' Display the CSPs in the list box.
    ' Determine the count of CSPs.
    nCount = Senroll.CSPCount
    If ( 0 = nCount ) Then
        MsgBox("No CSPs available.")
    Else
        ' At least one CSP exists.
        CSP_OK = True
        ' Add the CSP names to the CSP list
        For nIndex = 0 to nCount - 1
            Set Element=document.createElement("OPTION")
            Element.text=Senroll.enumCSPName( nIndex, 0 )
            Element.value=Element.text
            document.SCEnrForm.CSP.Options.Add Element
        Next
        ' Make the first item the selected item.
        ' This is for the user's viewing benefit.
        ' The Smart Card enrollment control upon initialization will
        ' have set the CSPName property to the value
        ' returned by enumCSPName(0, 0).
        document.SCEnrForm.CSP.selectedIndex=0
    End If
end sub

sub UpdateCT
    Dim nIndex, nCount, Element, CertTempType

    ' Determine the Type of certificate template.
    if ( document.SCenrForm.CTType(0).checked ) then 
        CertTempType = SCARD_ENROLL_USER_CERT_TEMPLATE
    else
        CertTempType = SCARD_ENROLL_MACHINE_CERT_TEMPLATE
    end if

    ' Display the certificate templates in the list box.
    ' Empty the existing contents.
    RemoveItems("CT")

    ' Determine the count of Cert Templates.
    nCount = Senroll.getCertTemplateCount(CertTempType)

    If ( 0 = nCount ) Then
        CT_OK = False 
        MsgBox("No certificate templates available.")
    Else
        ' At least one cert template exists.
        CT_OK = True
        ' Add the cert templates names to the CT list
        For nIndex = 0 to nCount - 1
            Set Element=document.createElement("OPTION")
            Element.text=Senroll.enumCertTemplateName( nIndex, CertTempType )
            Element.value=Element.text
            document.SCEnrForm.CT.Options.Add Element
        Next
        ' Make the first item the selected item.
        ' This is for the user's viewing benefit.
        ' The Smart Card enrollment control upon initialization will
        ' have set the CertTemplateName property to the value
        ' returned by enumCertTemplateName(0, 1).
        document.SCEnrForm.CT.selectedIndex=0
       ' Display the certification authorities in the list box.
       Call UpdateCA()
    End If
end sub

sub ViewCert_OnClick
    Dim strEnrolledCert

    ' Retrieve the name of the enrolled certificate and
    ' display the certificate viewer user interface.
    strEnrolledCert = Senroll.getEnrolledCertificateName(0)
end sub

-->
</SCRIPT>


<BODY LANGUAGE=VBScript OnLoad="Initialize">

<FORM NAME="SCEnrForm">
<P>
    Cryptographic Service Provider <SELECT NAME="CSP" SIZE=1 ID="CSP" onChange="ChangeCSP" LANGUAGE="VBScript">
                              </SELECT>
<P>
    Administrator Signing Certificate <INPUT NAME="SignCert" SIZE=40 READONLY><INPUT NAME="GetSign" TYPE="button" VALUE="Select Signing Certificate">
<P>
    Certificate Template <SELECT NAME="CertTemplate" SIZE=1 ID="CT" onChange="ChangeCT" LANGUAGE="VBScript">
                              </SELECT>  <INPUT NAME="CTType" onclick = "CTType_OnClick" ID="CTType" TYPE="radio" CHECKED VALUE=1>User <INPUT NAME="CTType" ID="CTType" onclick=CTType_OnClick TYPE="radio" VALUE=2>Machine
<P>
    Certification Authority <SELECT NAME="CertAuth" SIZE=1 ID="CA" onChange="ChangeCA" LANGUAGE="VBScript">
                              </SELECT>   
<P>
    Enroll on behalf of <INPUT NAME="User" SIZE=40 READONLY><INPUT NAME="GetUser" TYPE="button" VALUE="Select User">
<P>
<INPUT NAME="Enroll" TYPE="button" VALUE="Enroll" DISABLED>
<INPUT NAME="Reset" TYPE="button" VALUE="Reset User" DISABLED>
<INPUT NAME="ViewCert" TYPE="button" VALUE="View Certificate" DISABLED> 
</FORM></P>

</BODY>
</HTML>
```



 

 




