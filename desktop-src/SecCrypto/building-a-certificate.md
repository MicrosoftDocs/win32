---
Description: Explains the calls required to build a certificate.
ms.assetid: 74154b3b-75fc-412f-835c-1a6f54e688c6
title: Building a Certificate
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Building a Certificate

The order of calls in building a certificate is as follows:

1.  [*Certification authority*](security.c_gly#-security-certification-authority-gly) (CA) initializes modules through calls to [**ICertPolicy**](/windows/win32/Certpol/nn-certpol-icertpolicy?branch=master) and [**ICertExit**](/windows/win32/Certexit/nn-certexit-icertexit?branch=master) (happens once on server initialization). The CA will initialize the policy and exit modules by calling [**ICertPolicy2::Initialize**](/windows/win32/Certpol/nf-certpol-icertpolicy-initialize?branch=master) and [**ICertExit::Initialize**](/windows/win32/Certexit/nf-certexit-icertexit-initialize?branch=master).
2.  Intermediary calls the CA through [**ICertConfig**](/windows/win32/Certcli/nn-certcli-icertconfig?branch=master) (happens once per intermediary initialization). The intermediary finds the needed configuration string by calling [**ICertConfig::GetConfig**](/windows/win32/Certcli/nf-certcli-icertconfig-getconfig?branch=master).
3.  Client calls the intermediary through an interface specific to the intermediary (happens once per request). The client sends a [*certificate request*](security.c_gly#-security-certificate-request-gly) to the intermediary. This can be, for example, Microsoft Internet Explorer sending a request through [Certificate Enrollment Control](certificate-enrollment-control.md) to Microsoft Internet Information Services.
4.  Intermediary to CA through [**ICertRequest**](/windows/win32/Certcli/nn-certcli-icertrequest?branch=master) (happens once per request). The intermediary sends the certificate request to the CA through [**ICertRequest::Submit**](/windows/win32/Certcli/nf-certcli-icertrequest-submit?branch=master). In the case of Internet Information Services, this could be done through Active Server Pages scripts.
5.  The CA calls the Policy Module through the [**ICertPolicy**](/windows/win32/Certpol/nn-certpol-icertpolicy?branch=master) interface (happens once per request). The CA notifies the policy module that a request has arrived by calling [**ICertPolicy::VerifyRequest**](/windows/win32/Certpol/nf-certpol-icertpolicy-verifyrequest?branch=master). The policy module can examine the request and change the certificate by calling methods of the [**ICertServerPolicy**](/windows/win32/Certif/nn-certif-icertserverpolicy?branch=master) interface. The policy module can then indicate that the request is OK (if so, the certificate is built at this point), the request is to be denied, or the request should be suspended.
6.  (Optional) Administrator calls the CA through the [**ICertAdmin**](/windows/win32/Certadm/nn-certadm-icertadmin?branch=master) interface. If the request is suspended, the administrator can resubmit or deny the request, or modify request attributes and extensions. Note that if the request is resubmitted, the Policy Module will have another opportunity to process the request (as a result of a call to [**ICertPolicy::VerifyRequest**](/windows/win32/Certpol/nf-certpol-icertpolicy-verifyrequest?branch=master)). The task of resubmitting or denying the request can be performed by means of the Certification Authority MMC snap-in, or another application that uses **ICertAdmin**.
7.  The CA calls the exit module through the [**ICertExit**](/windows/win32/Certexit/nn-certexit-icertexit?branch=master) interface. If the exit module has indicated (when [**ICertExit::Initialize**](/windows/win32/Certexit/nf-certexit-icertexit-initialize?branch=master) was called, in step 1) that it is interested in seeing certificates issued or requests held pending, the CA will call [**ICertExit::Notify**](/windows/win32/Certexit/nf-certexit-icertexit-notify?branch=master).
8.  The exit module calls the CA through the [**ICertServerExit**](/windows/win32/Certif/nn-certif-icertserverexit?branch=master) interface. The exit module can examine the request and the new certificate by calling methods of **ICertServerExit**.

 

 



