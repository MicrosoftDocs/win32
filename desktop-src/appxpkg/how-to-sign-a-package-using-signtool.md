---
title: How to sign an app package using SignTool
description: Learn how to use SignTool to sign your Windows Store app packages so they can be deployed.
ms.assetid: 93541EB4-3419-45D1-AA63-563E6C6D3055
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# How to sign an app package using SignTool

> [!Note]  
> For signing a UWP app package, see [Sign an app package using SignTool](https://aka.ms/sign-package-signtool).

 

Learn how to use [**SignTool**](https://msdn.microsoft.com/library/windows/hardware/ff551778) to sign your Windows Store app packages so they can be deployed. [**SignTool**](https://msdn.microsoft.com/library/windows/hardware/ff551778) is part of the Windows Software Development Kit (SDK).

All Windows Store app packages must be digitally signed before they can be deployed. While Microsoft Visual Studio 2012 and later can sign an app package during its creation, packages that you create by using the [app packager (MakeAppx.exe)](make-appx-package--makeappx-exe-.md) tool from the Windows SDK aren't signed.

> [!Note]  
> You can only use [**SignTool**](https://msdn.microsoft.com/library/windows/hardware/ff551778) to sign your Windows Store app packages on Windows 8 and later or Windows Server 2012 and later. You can't use **SignTool** to sign app packages on down level operating systems such as Windows 7 or Windows Server 2008 R2.

 

## What you need to know

### Technologies

-   [Introduction to Code Signing](https://msdn.microsoft.com/library/ms537361)
-   [App packages and deployment](https://msdn.microsoft.com/library/windows/apps/hh464929)
-   [Tools to Sign Files and Check Signatures](https://msdn.microsoft.com/library/windows/desktop/aa388151)

### Prerequisites

-   [**SignTool**](https://msdn.microsoft.com/library/windows/hardware/ff551778), which is part of the Windows SDK
-   A valid code signing certificate, for example, a Personal Information Exchange (.pfx) file created with the [**MakeCert.exe**](https://msdn.microsoft.com/library/windows/hardware/ff548309) and [**Pvk2Pfx.exe**](https://msdn.microsoft.com/library/windows/hardware/ff550672) tools

    For info about creating a valid code signing certificate, see [How to create an app package signing certificate](how-to-create-a-package-signing-certificate.md).

-   A packaged Windows Store app, for example, an .appx file created by using the [app packager (MakeAppx.exe)](make-appx-package--makeappx-exe-.md) tool

**Additional considerations**

The certificate that you use to sign the app package must meet these criteria:

-   The subject name of the certificate must match the **Publisher** attribute that is contained in the [**Identity**](https://msdn.microsoft.com/library/windows/apps/br211441) element of the AppxManifest.xml file that is stored within the package. The publisher name is part of the identity of a Windows Store app, so you have to make the subject name of the certificate match the publisher name of the app. This allows the identity of signed packages to be checked against the digital signature. For info about signing errors that can arise from signing an app package using [**SignTool**](https://msdn.microsoft.com/library/windows/hardware/ff551778), see the Remarks section of [How to create an app package signing certificate](how-to-create-a-package-signing-certificate.md).
-   The certificate must be valid for code signing. This means that both of these items must be true:

    -   The Extended Key Usage (EKU) field of the certificate must either be unset or contain the EKU value for code signing (1.3.6.1.5.5.7.3.3).
    -   The Key Usage (KU) field of the certificate must either be unset or contain the usage bit for digital signature (0x80).

-   The certificate contains a private key.
-   The certificate is valid. It is active, hasn't expired, and hasn't been revoked.

## Instructions

### Step 1: Determine the hash algorithm to use

When you sign the app package, you must use the same hash algorithm that you used when you created the app package. If you used default settings to create the app package, the hash algorithm used is SHA256.

If you used the app packager with a specific hash algorithm to create the app package, use the same algorithm to sign the package. To determine the hash algorithm to use for signing a package, you can extract the package contents and inspect the AppxBlockMap.xml file. The **HashMethod** attribute of the [**BlockMap**](https://msdn.microsoft.com/library/windows/apps/jj709948) element indicates the hash algorithm that was used when creating the app package. For example:

``` syntax
<BlockMap xmlns="http://schemas.microsoft.com/appx/2010/blockmap" 
HashMethod="http://www.w3.org/2001/04/xmlenc#sha256">
```

The preceding [**BlockMap**](https://msdn.microsoft.com/library/windows/apps/jj709948) element indicates that the SHA256 algorithm was used. This table lists the mapping of the currently available algorithms:

| **HashMethod** value                            | *hashAlgorithm* to use |
|-------------------------------------------------|------------------------|
| <http://www.w3.org/2001/04/xmlenc#sha256>       | SHA256 (.appx default) |
| <http://www.w3.org/2001/04/xmldsig-more#sha384> | SHA384                 |
| <http://www.w3.org/2001/04/xmlenc#sha512>       | SHA512                 |



 

### Step 2: Run SignTool.exe to sign the package

**To sign the package with a signing certificate from a .pfx file**

-   ``` syntax
    SignTool sign /fd hashAlgorithm /a /f signingCert.pfx /p password filepath.appx
    ```

[**SignTool**](https://msdn.microsoft.com/library/windows/hardware/ff551778) defaults the /fd *hashAlgorithm* parameter to SHA1 if it's not specified, and SHA1 isn't valid for signing app packages. So, you must specify this parameter when you sign an app package. To sign an app package that was created with the default SHA256 hash, you specify the /fd *hashAlgorithm* parameter as SHA256:

``` syntax
SignTool sign /fd SHA256 /a /f signingCert.pfx /p password filepath.appx
```

You can omit the /p *password* parameter if you use a .pfx file that isn't password protected. You can also use other certificate selection options that are supported by [**SignTool**](https://msdn.microsoft.com/library/windows/hardware/ff551778) to sign app packages. For more info about these options, see [SignTool](https://msdn.microsoft.com/library/windows/desktop/aa387764).

> [!Note]  
> You can't use the [**SignTool**](https://msdn.microsoft.com/library/windows/hardware/ff551778) time stamp operation on a signed app package; the operation isn't supported.

 

If you want to time stamp the app package, you must do it during the sign operation. For example:

``` syntax
SignTool sign /fd hashAlgorithm /a /f signingCert.pfx /p password /tr timestampServerUrl 
filepath.appx
```

Make the /tr *timestampServerUrl* parameter equal to the URL for an RFC 3161 time stamp server.

## Remarks

This section discusses troubleshooting signing errors for app packages.

### Troubleshooting app package signing errors

In addition to the signing errors that [**SignTool**](https://msdn.microsoft.com/library/windows/hardware/ff551778) can return, **SignTool** can also return errors that are specific to the signing of app packages. These errors usually appear as internal errors:

``` syntax
SignTool Error: An unexpected internal error has occurred.
Error information: "Error: SignerSign() failed." (-2147024885 / 0x8007000B) 
```

If the error code starts with 0x8008, such as 0x80080206 APPX\_E\_CORRUPT\_CONTENT), it indicates that the package being signed is invalid. In this case, before you can sign the package, you must rebuild the package. For the full list of 0x8008\* errors, see [**COM Error Codes (Security and Setup)**](https://msdn.microsoft.com/library/windows/desktop/dd542646).

More commonly, the error is 0x8007000b (ERROR\_BAD\_FORMAT). In this case, you can find more specific error information in the event log:

**To search the event log**

1.  Run Eventvwr.msc.
2.  Open the event log: Event Viewer (Local) > Applications and Services Logs > Microsoft > Windows > AppxPackagingOM > Microsoft-Windows-AppxPackaging/Operational
3.  Look for the most recent error event.

The internal error usually corresponds to one of these:

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th>Event ID</th>
<th>Example event string</th>
<th>Suggestion</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>150</td>
<td>error 0x8007000B: The app manifest publisher name (CN=Contoso) must match the subject name of the signing certificate (CN=Contoso, C=US).</td>
<td>The app manifest publisher name must exactly match the subject name of the signing.
<blockquote>
[!Note]<br />
These names are specified in quotes and are both case and whitespace sensitive.
</blockquote>
<br/> You can update the <strong>Publisher</strong> attribute string that is defined for the [<strong>Identity</strong>](https://msdn.microsoft.com/library/windows/apps/br211441) element in the AppxManifest.xml file to match the subject name of the intended signing certificate. Or, select a different signing certificate with a subject name that matches the app manifest publisher name. The manifest publisher name and the certificate subject name are both listed in the event message.</td>
</tr>
<tr class="even">
<td>151</td>
<td>error 0x8007000B: The signature hash method specified (SHA512) must match the hash method used in the app package block map (SHA256).</td>
<td>The hashAlgorithm specified in the /fd parameter is incorrect (see Step 1: Determine the hash algorithm to use). Rerun [<strong>SignTool</strong>](https://msdn.microsoft.com/library/windows/hardware/ff551778) with the hashAlgorithm that matches the app package block map.</td>
</tr>
<tr class="odd">
<td>152</td>
<td>error 0x8007000B: The app package contents must validate against its block map.</td>
<td>The app package is corrupt and needs to be rebuilt to generate a new block map. For more info about creating an app package, see creating an app package with [app packager](make-appx-package--makeappx-exe-.md) or [Creating an app package with Visual Studio 2012](https://msdn.microsoft.com/en-us/library/Hh975357(v=VS.110).aspx).</td>
</tr>
</tbody>
</table>



 

## Security Considerations

After the package is signed, the certificate that you used to sign the package must still be trusted by the computer on which the package is to be deployed. By adding a certificate to [local machine certificate stores](https://msdn.microsoft.com/library/windows/hardware/ff548653), you affect the certificate trust of all users on the computer. We recommend that you install any code signing certificates that you want for testing app packages to the Trusted People certificate store, and promptly remove those certificates when no longer necessary. If you create your own test certificates for signing app packages, we also recommend that you restrict the privileges associated with the test certificate. For more info about creating test certificates for signing app packages, see [How to create an app package signing certificate](how-to-create-a-package-signing-certificate.md).

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

[Signing a package in Visual Studio 2012](https://msdn.microsoft.com/en-us/library/BR230260(v=VS.110).aspx)
</dt> <dt>

[SignTool](https://msdn.microsoft.com/library/windows/desktop/aa387764)
</dt> <dt>

[App packager (MakeAppx.exe)](make-appx-package--makeappx-exe-.md)
</dt> <dt>

[How to create an app package signing certificate](how-to-create-a-package-signing-certificate.md)
</dt> </dl>

 

 





