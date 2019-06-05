---
title: EAP Method Frequently Asked Questions
description: Provides answers to commonly-asked programming questions about EAP method authoring.
ms.assetid: 244e048f-4cc0-4094-a2b9-0f84674a293c
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# EAP Method Frequently Asked Questions

This topic provides answers to commonly-asked programming questions about EAP method authoring.

## EAP Method Frequently Asked Questions



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Question</th>
<th>Answer</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>What is &quot;configuration data&quot;?</td>
<td>The terms &quot;configuration data&quot; and &quot;connection data&quot; are synonymous.</td>
</tr>
<tr class="even">
<td>What is &quot;connection data&quot;?</td>
<td>&quot;Connection data&quot; is an EAP method-specific opaque BLOB that contains configuration information for the method. This connection data is created by the method when it is initially configured and is never interpreted or modified by any other component than the EAP method itself.</td>
</tr>
<tr class="odd">
<td>What are &quot;credentials&quot;?</td>
<td>The terms &quot;credentials&quot; and &quot;user data&quot; are synonymous.</td>
</tr>
<tr class="even">
<td>What is &quot;user data&quot;?</td>
<td>&quot;User data&quot; is an EAP method-specific opaque BLOB that contains user credential data, such as a user name and password. The user data is never interpreted or modified by any other component than the EAP method itself. The terms &quot;user data&quot; and &quot;credentials&quot; are synonymous.</td>
</tr>
<tr class="odd">
<td>What is an &quot;EAP attribute&quot;?</td>
<td>An &quot;EAP attribute&quot; is a data structure that contains a predetermined type of data. Attributes are used to communicate information between EAP methods and supplicants, or between EAP methods and authenticators. Peer and authenticator implementations of an EAP method may exchange these attributes over a network.</td>
</tr>
<tr class="even">
<td>Can the configuration API and the run-time API appear in the same method DLL?</td>
<td>Yes. Be sure to specify the distinction when configuring the registry entries for the EAP method itself. The configuration path and peer path must be the same.</td>
</tr>
<tr class="odd">
<td>Can the configuration API and the run-time API appear in separate method DLLs?</td>
<td>Yes. Be sure to specify the distinction when configuring the registry entries for the EAP method itself. The configuration and peer paths must point to the correct DLLs.</td>
</tr>
<tr class="even">
<td>How do I install an EAP method?</td>
<td>To install an EAP method, you must first implement [<strong>DllRegisterServer</strong>](https://msdn.microsoft.com/windows/desktop/4442206b-b2ad-47d7-8add-18002c44c5a2) and [<strong>DllUnregisterServer</strong>](https://msdn.microsoft.com/windows/desktop/b71137a7-284e-4521-a3b2-9dad9c9d3c54) in the EAP method DLL itself. After that, use <strong>regsvr32.exe</strong> to install and uninstall the method. The appropriate registry keys must also be set. For more information, see [Installing an EAP Method](installing-an-eap-method.md).<br/></td>
</tr>
<tr class="odd">
<td>What is in-band [Network Access Protection](https://docs.microsoft.com/windows/desktop/NAP/network-access-protection-start-page) (NAP) support?</td>
<td>When in-band NAP support is enabled, NAP packets are transported inside EAP method packets. In contrast, when out-of-band NAP support is enabled, the NAP [Statement of Health](Http://go.microsoft.com/fwlink/p/?linkid=83917) (SoH) exchange occurs through means other than internal to EAP method packets, and NAP-generated certificates are used in EAP method authentication.</td>
</tr>
<tr class="even">
<td>Can I enable in-band NAP support for my EAP method?</td>
<td>Yes, in-band NAP support for your EAP method can be enabled. For more information, see [Enabling In-Band NAP Support for EAP Methods](enabling-in-band-nap-support.md).</td>
</tr>
<tr class="odd">
<td>How does EAP Flexible Authentication via Secure Tunneling (EAP-FAST) work?</td>
<td>The EAP-FAST scenario works as follows. <br/>
<ul>
<li>The method processes a password change at single-sign-on (SSO) employing the method UI.</li>
<li>The method returns the [<strong>eatCredentialsChanged</strong>](/previous-versions/windows/desktop/api/eaptypes/ne-eaptypes-_eap_attribute_type) attribute.</li>
<li>The supplicant indicates to the user that credentials have changed and requests the user to re-enter their credentials.</li>
<li>The supplicant re-enters the user credentials, and sends those credentials to the method.</li>
</ul>
For more information on EAP-FAST, see [EAP Flexible Authentication via Secure Tunneling](Http://go.microsoft.com/fwlink/p/?linkid=84010) (EAP-FAST).</td>
</tr>
<tr class="even">
<td>What is Pre-Shared Key(PSK)?</td>
<td>A method of transmitting and receiving digital signals in which the phase of a transmitted signal is varied to convey information. The [<strong>EAPConfigInputPSK</strong>](/previous-versions/windows/desktop/api/eaptypes/ne-eaptypes-_eap_config_input_field_type) input field contains the user's EAP-FAST PSK.</td>
</tr>
<tr class="odd">
<td>What is WOW and how does it matter to EAPHost?</td>
<td>Microsoft Windows-32-bit-On-Windows-64-bit (WOW) is an operating system component in 64-bit Windows that supports 32-bit x86 platform application. Typically, a EAP method author would define some form of C/C++ structure to encapsulate configuration data, credential data, and interactive UI data. To avoid incompatibilities in WOW and other scenarios, it is important to ensure that data structures are aligned similarly in different processor architectures (32-bit and 64-bit processors). Typically dummy padding is used to align the fields so that the configuration, credential and interactive UI data are identical on both 32-and 64-bit processors.</td>
</tr>
<tr class="even">
<td>What are &quot;action codes&quot; and under what conditions are these action codes returned?</td>
<td>&quot;Action codes&quot; allow methods to control the flow of authentication, and are integral to the state machine. They are values returned by an EAP method to indicate the next action the EAPHost should take. For example, an action code could indicate to EAPHost that the EAP method has a packet ready for transmission. The supplicant abides by all action codes returned by an EAP method, but never issues action codes.For more information, see [EAP Peer Supplicant Action Codes](/previous-versions/windows/desktop/api/eaphostpeertypes/ne-eaphostpeertypes-tageaphostpeerresponseaction).<br/></td>
</tr>
<tr class="odd">
<td>When does a method return [<strong>EapPeerMethodResponseActionDiscard</strong>](/previous-versions/windows/desktop/api/EapAuthenticatorActionDefine/ne-eapauthenticatoractiondefine-tageappeermethodresponseaction), and what does this action code mean to EAPHost?</td>
<td>[<strong>EapPeerMethodResponseActionDiscard</strong>](/previous-versions/windows/desktop/api/EapAuthenticatorActionDefine/ne-eapauthenticatoractiondefine-tageappeermethodresponseaction) is returned by an EAP method to indicate to the EAPHost that it must discard the packet it supplied to the method. Specifically, the method has determined that the packet is invalid. EAPHost then waits for the next package.</td>
</tr>
<tr class="even">
<td>When does a method return [<strong>EapPeerMethodResponseActionSend</strong>](/previous-versions/windows/desktop/api/EapAuthenticatorActionDefine/ne-eapauthenticatoractiondefine-tageappeermethodresponseaction) and what does this action code mean to EAPHost?</td>
<td>[<strong>EapPeerMethodResponseActionSend</strong>](/previous-versions/windows/desktop/api/EapAuthenticatorActionDefine/ne-eapauthenticatoractiondefine-tageappeermethodresponseaction) is returned by an EAP method to indicate to EAPHost that the next packet received by EAPHost must be sent to the network access server (NAS).</td>
</tr>
<tr class="odd">
<td>When does a method return [<strong>EapPeerMethodResponseActionResult</strong>](/previous-versions/windows/desktop/api/EapAuthenticatorActionDefine/ne-eapauthenticatoractiondefine-tageappeermethodresponseaction) and what does this action code mean to EAPHost?</td>
<td>[<strong>EapPeerMethodResponseActionResult</strong>](/previous-versions/windows/desktop/api/EapAuthenticatorActionDefine/ne-eapauthenticatoractiondefine-tageappeermethodresponseaction) is returned by an EAP method to indicate to the EAPHost that the authentication session has concluded and that the results of that session are available.</td>
</tr>
<tr class="even">
<td>When does a method return [<strong>EapPeerMethodResponseActionInvokeUI</strong>](/previous-versions/windows/desktop/api/EapAuthenticatorActionDefine/ne-eapauthenticatoractiondefine-tageappeermethodresponseaction) and what does this action code mean to EAPHost?</td>
<td>[<strong>EapPeerMethodResponseActionInvokeUI</strong>](/previous-versions/windows/desktop/api/EapAuthenticatorActionDefine/ne-eapauthenticatoractiondefine-tageappeermethodresponseaction) is returned by an EAP method to indicate to EAPHost that user input is required to continue with authentication, and that a user interface dialog box must be displayed to obtain that input. Once the user input data has been obtained, EAPHost can call the EAP method again with the updated UI context data.</td>
</tr>
<tr class="odd">
<td>When does a method return [<strong>EapPeerMethodResponseActionRespond</strong>](/previous-versions/windows/desktop/api/EapAuthenticatorActionDefine/ne-eapauthenticatoractiondefine-tageappeermethodresponseaction) and what does this action code mean to EAPHost?</td>
<td>[<strong>EapPeerMethodResponseActionRespond</strong>](/previous-versions/windows/desktop/api/EapAuthenticatorActionDefine/ne-eapauthenticatoractiondefine-tageappeermethodresponseaction) is returned by an EAP method to indicate to EAPHost that the EAP method has attributes available for EAPHost to use during authentication. EAPHost obtains the attributes by calling the [<strong>EapPeerGetResponseAttributes</strong>](/previous-versions/windows/desktop/api/eapmethodpeerapis/nf-eapmethodpeerapis-eappeergetresponseattributes) method followed by a call to the [<strong>EapPeerSetResponseAttributes</strong>](/previous-versions/windows/desktop/api/eapmethodpeerapis/nf-eapmethodpeerapis-eappeersetresponseattributes) method.</td>
</tr>
<tr class="even">
<td>When does a method return [<strong>EapPeerMethodResponseActionNone</strong>](/previous-versions/windows/desktop/api/EapAuthenticatorActionDefine/ne-eapauthenticatoractiondefine-tageappeermethodresponseaction) and what does this action code mean to EAPHost?</td>
<td>[<strong>EapPeerMethodResponseActionNone</strong>](/previous-versions/windows/desktop/api/EapAuthenticatorActionDefine/ne-eapauthenticatoractiondefine-tageappeermethodresponseaction) is returned by an EAP method to indicate to EAPHost that no action is required at this time.</td>
</tr>
<tr class="odd">
<td>Can I enable tracing on the authenticator side?</td>
<td>Yes. For more information, see [Enabling Tracing](enabling-tracing.md).</td>
</tr>
</tbody>
</table>



 

## Related topics

<dl> <dt>

[EAPHost Peer Method API Reference](eap-host-peer-method-api-reference.md)
</dt> <dt>

[EAPHost General FAQs](general-frequently-asked-questions.md)
</dt> <dt>

[EAPHost Supplicant FAQs](eaphost-supplicant-frequently-asked-questions.md)
</dt> <dt>

[EAPHost Development FAQs](eaphost-development-frequently-asked-questions.md)
</dt> </dl>

 

 





