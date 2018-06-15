---
title: How to create an app package signing certificate
description: Learn how to use MakeCert.exe and Pvk2Pfx.exe to create a test code signing certificate, so that you can sign your Windows Store app packages.
ms.assetid: DEDD3727-3F0E-403D-9A6E-55949E98FE74
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# How to create an app package signing certificate

> \[!Important\]  
> MakeCert.exe is deprecated. For current guidance on creating a certificate, see [Create a certificate for package signing](https://aka.ms/create-cert-package).

 

Learn how to use [**MakeCert.exe**](https://msdn.microsoft.com/library/windows/hardware/ff548309) and [**Pvk2Pfx.exe**](https://msdn.microsoft.com/library/windows/hardware/ff550672) to create a test code signing certificate, so that you can sign your Windows Store app packages.

You must digitally sign your Windows Store apps before you deploy them. If you don't use Microsoft Visual Studio 2012 to create and sign your app packages, you need to create and manage your own code signing certificates. You can create certificates by using [**MakeCert.exe**](https://msdn.microsoft.com/library/windows/hardware/ff548309) and [**Pvk2Pfx.exe**](https://msdn.microsoft.com/library/windows/hardware/ff550672) from the Windows Driver Kit (WDK). Then you can use the certificates to sign the app packages, so they can be deployed locally for testing.

## What you need to know

### Technologies

-   [Introduction to Code Signing](https://msdn.microsoft.com/library/ms537361)
-   [App packages and deployment](https://msdn.microsoft.com/library/windows/apps/hh464929)
-   [Tools for Signing Drivers](https://msdn.microsoft.com/library/windows/hardware/ff552958)

### Prerequisites

-   [**MakeCert.exe**](https://msdn.microsoft.com/library/windows/hardware/ff548309) and [**Pvk2Pfx.exe**](https://msdn.microsoft.com/library/windows/hardware/ff550672) tools from the WDK

## Instructions

### Step 1: Determine the publisher name of the package

To make the signing certificate that you create usable with the app package that you want to sign, the subject name of the signing certificate must match the **Publisher** attribute of the [**Identity**](https://msdn.microsoft.com/library/windows/apps/br211441) element in the AppxManifest.xml for that app. For example, suppose the AppxManifest.xml contains:

``` syntax
  <Identity Name="Contoso.AssetTracker" 
    Version="1.0.0.0" 
    Publisher="CN=Contoso Software, O=Contoso Corporation, C=US"/>
```

For the *publisherName* parameter that you specify with the [**MakeCert**](https://msdn.microsoft.com/library/windows/hardware/ff548309) utility in the next step, use "CN=Contoso Software, O=Contoso Corporation, C=US".

> [!Note]  
> This parameter string is specified in quotes and is both case and whitespace sensitive.

 

The **Publisher** attribute string that is defined for the [**Identity**](https://msdn.microsoft.com/library/windows/apps/br211441) element in the AppxManifest.xml must be identical to the string that you specify with the [**MakeCert**](https://msdn.microsoft.com/library/windows/hardware/ff548309) /n parameter for the certificate subject name. Copy and paste the string where possible.

### Step 2: Create a private key using MakeCert.exe

Use the [**MakeCert**](https://msdn.microsoft.com/library/windows/hardware/ff548309) utility to create a self-signed test certificate and private key:

``` syntax
MakeCert /n publisherName /r /h 0 /eku "1.3.6.1.5.5.7.3.3,1.3.6.1.4.1.311.10.3.13" /e 
expirationDate /sv MyKey.pvk MyKey.cer
```

This command prompts you to provide a password for the .pvk file. We recommend that you choose a [strong password](https://msdn.microsoft.com/en-us/library/Bb499367(v=WinEmbedded.5).aspx) and keep your private key in a secure location.

We recommend that you use the suggested parameters in the preceding example for these reasons:

<dl> <dt>

<span id="_r"></span><span id="_R"></span>**/r**
</dt> <dd>

Creates a self-signed root certificate. This simplifies management for your test certificate.

</dd> <dt>

<span id="_h_0"></span><span id="_H_0"></span>**/h 0**
</dt> <dd>

Marks the basic constraint for the certificate as an end-entity. This prevents the certificate from being used as a Certification Authority (CA) that can issue other certificates.

</dd> <dt>

<span id="_eku"></span><span id="_EKU"></span>**/eku**
</dt> <dd>

Sets the Enhanced Key Usage (EKU) values for the certificate.

> [!Note]  
> Don't put a space between the two comma-delimited values.

 

-   1.3.6.1.5.5.7.3.3 indicates that the certificate is valid for code signing. Always specify this value to limit the intended use for the certificate.
-   1.3.6.1.4.1.311.10.3.13 indicates that the certificate respects lifetime signing. Typically, if a signature is time stamped, as long as the certificate was valid at the point when it was time stamped, the signature remains valid even if the certificate expires. This EKU forces the signature to expire regardless of whether the signature is time stamped.

</dd> <dt>

<span id="_e"></span><span id="_E"></span>**/e**
</dt> <dd>

Sets the expiration date of the certificate. Provide a value for the *expirationDate* parameter in the mm/dd/yyyy format. We recommend that you choose an expiration date only as long as necessary for your testing purposes, typically less than a year. This expiration date in conjunction with the lifetime signing EKU can help to limit the window in which the certificate can be compromised and misused.

</dd> </dl>

For more info about other options, see [**MakeCert**](https://msdn.microsoft.com/library/windows/hardware/ff548309).

### Step 3: Create a Personal Information Exchange (.pfx) file using Pvk2Pfx.exe

Use the [**Pvk2Pfx**](https://msdn.microsoft.com/library/windows/hardware/ff550672) utility to convert the .pvk and .cer files that [**MakeCert**](https://msdn.microsoft.com/library/windows/hardware/ff548309) created to a .pfx file that you can use with [SignTool](https://msdn.microsoft.com/library/windows/desktop/aa387764) to sign an app package:

``` syntax
Pvk2Pfx /pvk MyKey.pvk /pi pvkPassword /spc MyKey.cer /pfx MyKey.pfx [/po pfxPassword]
```

The *MyKey.pvk* and *MyKey.cer* files are the same files that [**MakeCert.exe**](https://msdn.microsoft.com/library/windows/hardware/ff548309) created in the previous step. By using the optional /po parameter, you can specify a different password for the resulting .pfx; otherwise, the .pfx has the same password as *MyKey.pvk*.

For more info about other options, see [**Pvk2Pfx**](https://msdn.microsoft.com/library/windows/hardware/ff550672).

## Remarks

After you create the .pfx file, you can use the file with [SignTool](https://msdn.microsoft.com/library/windows/desktop/aa387764) to sign an app package. For more info, see [How to sign an app package using SignTool](how-to-sign-a-package-using-signtool.md). But the certificate is still not trusted by the local computer for deployment of app packages until you install it into the trusted certificates store of the local computer. You can use [Certutil.exe](https://msdn.microsoft.com/en-us/library/Cc732443(v=WS.10).aspx), which comes with Windows.

**To install certificates with WindowsCertutil.exe**

1.  Run **Cmd.exe** as administrator.
2.  Run this command:

    ``` syntax
    Certutil -addStore TrustedPeople MyKey.cer
    ```

We recommend that you remove the certificates if they are no longer in use. From the same administrator command prompt, run this command:

``` syntax
Certutil -delStore TrustedPeople certID
```

The **certID** is the serial number of the certificate. Run this command to determine the certificate serial number:

``` syntax
Certutil -store TrustedPeople
```

## Security Considerations

By adding a certificate to [local machine certificate stores](https://msdn.microsoft.com/library/windows/hardware/ff548653), you affect the certificate trust of all users on the computer. We recommend that you install any code signing certificates that you want for testing app packages to the Trusted People certificate store. Promptly remove those certificates when they are no longer necessary, to prevent them from being used to compromise system trust.

## Related topics

<dl> <dt>

**Samples**
</dt> <dt>

[Create app package sample](http://go.microsoft.com/fwlink/p/?linkid=236965)
</dt> <dt>

**Concepts**
</dt> <dt>

[Code-Signing Best Practices](http://msdn.microsoft.com/windows/hardware/gg487309.aspx)
</dt> <dt>

[How to sign an app package using SignTool](how-to-sign-a-package-using-signtool.md)
</dt> <dt>

[Signing an app package](https://msdn.microsoft.com/en-us/library/BR230260(v=VS.110).aspx)
</dt> </dl>

 

 




