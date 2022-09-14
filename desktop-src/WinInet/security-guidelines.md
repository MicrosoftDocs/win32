---
title: Security Guideline
description: It is important to keep the user informed about possible security issues.
ms.assetid: f0c041fd-3cc5-491e-b088-6c93fcd61def
ms.topic: article
ms.date: 05/31/2018
---

# Security Guideline

It is important to keep the user informed about possible security issues.

## Notify the User of Security-Related Events

Always notify the user of any change in security, whether it is a security-related error such as a certificate failure, or a change in the security of the underlying protocol, such as change from an HTTPS site to an HTTP site.

## Notify the User of Security-Related Errors

When your application receives an error message that may indicate a security problem, the **InternetErrorDlg** function provides a standard, familiar interface for notifying the user in most cases.

Among the errors that fall in this category are:

**ERROR\_INTERNET\_HTTP\_TO\_HTTPS\_ON\_REDIR**

**ERROR\_INTERNET\_INVALID\_CA**

**ERROR\_INTERNET\_POST\_IS\_NON\_SECURE**

**ERROR\_INTERNET\_SEC\_CERT\_ERRORS**

**ERROR\_INTERNET\_SEC\_CERT\_CN\_INVALID**

**ERROR\_INTERNET\_SEC\_CERT\_DATE\_INVALID**

A failure to notify the user of errors such as these can expose the user to various sorts of security breaches, including spoofing attacks or involuntary information disclosure.

## Notify the User When Connection Security Changes

Always notify the user when the security of the connection changes, for example from HTTPS to HTTP. Otherwise, unless the user has explicitly chosen not to be notified of such changes, you are concealing the risks of involuntary information disclosure.

Among the functions that report such a change in connection security are the **InternetStatusCallback** callback function and the **InternetConfirmZoneCrossing** function.

> [!Note]  
> WinINet does not support server implementations. In addition, it should not be used from a service. For server implementations or services use [Microsoft Windows HTTP Services (WinHTTP)](/windows/desktop/WinHttp/winhttp-start-page).

 

 

 