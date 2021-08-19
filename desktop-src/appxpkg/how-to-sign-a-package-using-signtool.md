---
title: How to sign an app package using SignTool
description: Learn how to use SignTool to sign your Windows app packages so they can be deployed.
ms.assetid: 93541EB4-3419-45D1-AA63-563E6C6D3055
ms.topic: article
ms.date: 05/31/2018
---

# How to sign an app package using SignTool

> [!Note]  
> For signing a Windows app package, see [Sign an app package using SignTool](/windows/msix/package/sign-app-package-using-signtool).

 

Learn how to use [**SignTool**](/windows-hardware/drivers/devtest/signtool) to sign your Windows app packages so they can be deployed. [**SignTool**](/windows-hardware/drivers/devtest/signtool) is part of the Windows Software Development Kit (SDK).

All Windows app packages must be digitally signed before they can be deployed. While Microsoft Visual Studio 2012 and later can sign an app package during its creation, packages that you create by using the [app packager (MakeAppx.exe)](make-appx-package--makeappx-exe-.md) tool from the Windows SDK aren't signed.

> [!Note]  
> You can only use [**SignTool**](/windows-hardware/drivers/devtest/signtool) to sign your Windows app packages on Windows 8 and later or Windows Server 2012 and later. You can't use **SignTool** to sign app packages on down-level operating systems such as Windows 7 or Windows Server 2008 R2.

 

## What you need to know

### Technologies

-   [Introduction to Code Signing](/previous-versions/windows/internet-explorer/ie-developer/platform-apis/ms537361(v=vs.85))
-   [App packages and deployment](/previous-versions/windows/apps/hh464929(v=win.10))
-   [Tools to Sign Files and Check Signatures](/windows/desktop/SecCrypto/tools-to-sign-files-and-check-signatures)

### Prerequisites

-   [**SignTool**](/windows-hardware/drivers/devtest/signtool), which is part of the Windows SDK
-   A valid code signing certificate, for example, a Personal Information Exchange (.pfx) file created with the [**MakeCert.exe**](/windows-hardware/drivers/devtest/makecert) and [**Pvk2Pfx.exe**](/windows-hardware/drivers/devtest/pvk2pfx) tools

    For info about creating a valid code signing certificate, see [How to create an app package signing certificate](how-to-create-a-package-signing-certificate.md).

-   A packaged Windows app, for example, an .appx file created by using the [app packager (MakeAppx.exe)](make-appx-package--makeappx-exe-.md) tool

**Additional considerations**

The certificate that you use to sign the app package must meet these criteria:

-   The subject name of the certificate must match the **Publisher** attribute that is contained in the [**Identity**](/uwp/schemas/appxpackage/appxmanifestschema/element-identity) element of the AppxManifest.xml file that is stored within the package. The publisher name is part of the identity of a packaged Windows app, so you have to make the subject name of the certificate match the publisher name of the app. This allows the identity of signed packages to be checked against the digital signature. For info about signing errors that can arise from signing an app package using [**SignTool**](/windows-hardware/drivers/devtest/signtool), see the Remarks section of [How to create an app package signing certificate](how-to-create-a-package-signing-certificate.md).
-   The certificate must be valid for code signing. This means that both of these items must be true:

    -   The Extended Key Usage (EKU) field of the certificate must either be unset or contain the EKU value for code signing (1.3.6.1.5.5.7.3.3).
    -   The Key Usage (KU) field of the certificate must either be unset or contain the usage bit for digital signature (0x80).

-   The certificate contains a private key.
-   The certificate is valid. It is active, hasn't expired, and hasn't been revoked.

## Instructions

### Step 1: Determine the hash algorithm to use

When you sign the app package, you must use the same hash algorithm that you used when you created the app package. If you used default settings to create the app package, the hash algorithm used is SHA256.

If you used the app packager with a specific hash algorithm to create the app package, use the same algorithm to sign the package. To determine the hash algorithm to use for signing a package, you can extract the package contents and inspect the AppxBlockMap.xml file. The **HashMethod** attribute of the [**BlockMap**](/uwp/schemas/blockmapschema/element-blockmap) element indicates the hash algorithm that was used when creating the app package. For example:

``` syntax
<BlockMap xmlns="http://schemas.microsoft.com/appx/2010/blockmap" 
HashMethod="https://www.w3.org/2001/04/xmlenc#sha256">
```

The preceding [**BlockMap**](/uwp/schemas/blockmapschema/element-blockmap) element indicates that the SHA256 algorithm was used. This table lists the mapping of the currently available algorithms:

| **HashMethod** value                            | *hashAlgorithm* to use |
|-------------------------------------------------|------------------------|
| <https://www.w3.org/2001/04/xmlenc#sha256>       | SHA256 (.appx default) |
| <https://www.w3.org/2001/04/xmldsig-more#sha384> | SHA384                 |
| <https://www.w3.org/2001/04/xmlenc#sha512>       | SHA512                 |



 

### Step 2: Run SignTool.exe to sign the package

**To sign the package with a signing certificate from a .pfx file**

-   ``` syntax
    SignTool sign /fd hashAlgorithm /a /f signingCert.pfx /p password filepath.appx
    ```

[**SignTool**](/windows-hardware/drivers/devtest/signtool) defaults the /fd *hashAlgorithm* parameter to SHA1 if it's not specified, and SHA1 isn't valid for signing app packages. So, you must specify this parameter when you sign an app package. To sign an app package that was created with the default SHA256 hash, you specify the /fd *hashAlgorithm* parameter as SHA256:

``` syntax
SignTool sign /fd SHA256 /a /f signingCert.pfx /p password filepath.appx
```

You can omit the /p *password* parameter if you use a .pfx file that isn't password protected. You can also use other certificate selection options that are supported by [**SignTool**](/windows-hardware/drivers/devtest/signtool) to sign app packages. For more info about these options, see [SignTool](/windows/desktop/SecCrypto/signtool).

> [!Note]  
> You can't use the [**SignTool**](/windows-hardware/drivers/devtest/signtool) time stamp operation on a signed app package; the operation isn't supported.

 

If you want to time stamp the app package, you must do it during the sign operation. For example:

``` syntax
SignTool sign /fd hashAlgorithm /a /f signingCert.pfx /p password /tr timestampServerUrl 
filepath.appx
```

Make the /tr *timestampServerUrl* parameter equal to the URL for an RFC 3161 time stamp server.

## Remarks

This section discusses troubleshooting signing errors for app packages.

### Troubleshooting app package signing errors

In addition to the signing errors that [**SignTool**](/windows-hardware/drivers/devtest/signtool) can return, **SignTool** can also return errors that are specific to the signing of app packages. These errors usually appear as internal errors:

``` syntax
SignTool Error: An unexpected internal error has occurred.
Error information: "Error: SignerSign() failed." (-2147024885 / 0x8007000B) 
```

If the error code starts with 0x8008, such as 0x80080206 APPX\_E\_CORRUPT\_CONTENT), it indicates that the package being signed is invalid. In this case, before you can sign the package, you must rebuild the package. For the full list of 0x8008\* errors, see [**COM Error Codes (Security and Setup)**](/windows/desktop/com/com-error-codes-4).

More commonly, the error is 0x8007000b (ERROR\_BAD\_FORMAT). In this case, you can find more specific error information in the event log:

**To search the event log**

1.  Run Eventvwr.msc.
2.  Open the event log: Event Viewer (Local) > Applications and Services Logs > Microsoft > Windows > AppxPackagingOM > Microsoft-Windows-AppxPackaging/Operational
3.  Look for the most recent error event.

The internal error usually corresponds to one of these:


| Event ID | Example event string | Suggestion | 
|----------|----------------------|------------|
| 150 | error 0x8007000B: The app manifest publisher name (CN=Contoso) must match the subject name of the signing certificate (CN=Contoso, C=US). | The app manifest publisher name must exactly match the subject name of the signing.<blockquote>[!Note]<br />These names are specified in quotes and are both case and whitespace sensitive.</blockquote><br /> You can update the <strong>Publisher</strong> attribute string that is defined for the <a href="/uwp/schemas/appxpackage/appxmanifestschema/element-identity"><strong>Identity</strong></a> element in the AppxManifest.xml file to match the subject name of the intended signing certificate. Or, select a different signing certificate with a subject name that matches the app manifest publisher name. The manifest publisher name and the certificate subject name are both listed in the event message. | 
| 151 | error 0x8007000B: The signature hash method specified (SHA512) must match the hash method used in the app package block map (SHA256). | The hashAlgorithm specified in the /fd parameter is incorrect (see Step 1: Determine the hash algorithm to use). Rerun <a href="/windows-hardware/drivers/devtest/signtool"><strong>SignTool</strong></a> with the hashAlgorithm that matches the app package block map. | 
| 152 | error 0x8007000B: The app package contents must validate against its block map. | The app package is corrupt and needs to be rebuilt to generate a new block map. For more info about creating an app package, see creating an app package with <a href="make-appx-package--makeappx-exe-.md">app packager</a> or <a href="/previous-versions/hh975357(v=vs.110)">Creating an app package with Visual Studio 2012</a>. | 




 

## Security Considerations

After the package is signed, the certificate that you used to sign the package must still be trusted by the computer on which the package is to be deployed. By adding a certificate to [local machine certificate stores](/windows-hardware/drivers/install/local-machine-and-current-user-certificate-stores), you affect the certificate trust of all users on the computer. We recommend that you install any code signing certificates that you want for testing app packages to the Trusted People certificate store, and promptly remove those certificates when no longer necessary. If you create your own test certificates for signing app packages, we also recommend that you restrict the privileges associated with the test certificate. For more info about creating test certificates for signing app packages, see [How to create an app package signing certificate](how-to-create-a-package-signing-certificate.md).

## Related topics

<dl> <dt>

**Samples**
</dt> <dt>

[Create app package sample](https://github.com/microsoft/Windows-classic-samples/tree/master/Samples/AppxPackingCreateAppx)
</dt> <dt>

**Concepts**
</dt> <dt>

[Code-Signing Best Practices](/previous-versions/windows/hardware/design/dn653556(v=vs.85))
</dt> <dt>

[Signing a package in Visual Studio 2012](/previous-versions/br230260(v=vs.110))
</dt> <dt>

[SignTool](/windows/desktop/SecCrypto/signtool)
</dt> <dt>

[App packager (MakeAppx.exe)](make-appx-package--makeappx-exe-.md)
</dt> <dt>

[How to create an app package signing certificate](how-to-create-a-package-signing-certificate.md)
</dt> </dl>

