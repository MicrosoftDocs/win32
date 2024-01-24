---
title: How to troubleshoot app package signature errors
description: An app deployment failure can be caused by a failure to validate the digital signature of the app package. Learn how to recognize these failures, and what to do about them.
ms.assetid: CE868296-87F6-4BD5-8AC5-914E429EDEBC
ms.topic: article
ms.date: 05/31/2018
---

# How to troubleshoot app package signature errors

An app deployment failure can be caused by a failure to validate the digital signature of the app package. Learn how to recognize these failures, and what to do about them.

When you deploy a packaged Windows app, Windows always attempts to validate the digital signature on the app package. Failures during signature validation block deployment of the package. But why the package didn't validate might not be obvious. In particular, if you sign your packages with private certificates for local testing, you often must manage the trust for those certificates as well. An incorrect certificate trust configuration can lead to signature validation failures.

## What you need to know

### Technologies

-   [Packaging, deployment, and query of Windows apps](appx-portal.md)
-   [Certificate Trust Verification](/windows/desktop/SecCrypto/certificate-trust-verification)

### Prerequisites

-   [Windows Event Log](/windows/desktop/WES/windows-event-log) to diagnose installation failures.
-   [Certutil tasks for managing certificates](/previous-versions/orphan-topics/ws.10/cc772898(v=ws.10)) for certificate store manipulation during troubleshooting

## Instructions

### Step 1: Examine event logs for diagnostic information

Depending on how you attempted to deploy your app, you might not have received a meaningful error code for the deployment failure. In this case, you can usually get the error code directly from the event logs.

**To get the error code from the event logs**

1.  Run **eventvwr.msc**.
2.  Go to **Event Viewer (Local)** > **Applications and Services Logs** > **Microsoft** > **Windows**.
3.  The first log to check is **AppxPackagingOM** > **Microsoft-Windows-AppxPackaging/Operational**.
4.  Deployment-related errors are recorded in **AppXDeployment-Server** > **Microsoft-Windows-AppXDeploymentServer/Operational**.

    For deployment errors, search for the most recent error event 404. This error event provides you with the error code and a description of why the deployment failed. If an error event 465 preceded the 404 event, there was a problem opening the package.

If the 465 error didn't occur, see general [Troubleshooting packaging, deployment, and query of Windows apps](troubleshooting.md). Otherwise, refer to this table for common error codes that can show up in the error string for error event 465:

| Error code | Error                                 | Description                                                                                                          | Suggestion                                                                                                                                                                                                 |
|------------|---------------------------------------|----------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0x80073CF0 | ERROR\_INSTALL\_OPEN\_PACKAGE\_FAILED | The app package could not be opened.                                                                                 | This error typically indicates a problem with the package. You need to build and sign the package again. For more info, see [Using App Packager](make-appx-package--makeappx-exe-.md). |
| 0x80080205 | APPX\_E\_INVALID\_BLOCKMAP            | The app package has been tampered with or has an invalid block map.                                                  | The package is corrupted. You need to build and sign the package again. For more info, see [Using App Packager](make-appx-package--makeappx-exe-.md).                                  |
| 0x800B0004 | TRUST\_E\_SUBJECT\_NOT\_TRUSTED       | The app package has been tampered with.                                                                              | The package contents no longer match its digital signature. You need to sign the package again. For more info, see [How to sign an app package using SignTool](how-to-sign-a-package-using-signtool.md).  |
| 0x800B0100 | TRUST\_E\_NOSIGNATURE                 | The app package is unsigned.                                                                                         | Only signed Windows app packages can be deployed. For info about signing an app package, see [How to sign an app package using SignTool](how-to-sign-a-package-using-signtool.md).                  |
| 0x800B0109 | CERT\_E\_UNTRUSTED\_ROOT              | The certificate chain that was used to sign the app package ends in a root certificate that isn't trusted.           | Continue to Step 2 to troubleshoot the certificate trust.                                                                                                                                                  |
| 0x800B010A | CERT\_E\_CHAINING                     | No certificate chain could be built to a trusted root authority from the cert that was used to sign the app package. | Continue to Step 2 to troubleshoot the certificate trust.                                                                                                                                                  |



 

### Step 2: Determine the certificate chain used to sign the app package

To figure out the certificates that the local computer must trust, you can examine the certificate chain for the digital signature on the app package.

**To determine the certificate chain**

1.  In File Explorer, right-click on the app package and select **Properties**.
2.  In the **Properties** dialog, select the **Digital Signatures** tab, which also displays whether the signature can be validated.
3.  In the Signature list, select the signature and then click the **Details** button.
4.  In the **Digital Signature Details** dialog, click the **View Certificate** button.
5.  In the **Certificate** dialog, select the **Certification Path** tab.

The top certificate in the chain is the root certificate and the bottom certificate is the signing certificate. If only a single certificate is in the chain, the signing certificate is also its own root certificate. You can determine the serial number for each certificate that you then use with [Certutil](/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/cc732443(v=ws.10)):

**To determine the serial number for each certificate**

1.  In the Certification path pane, select the certificate and then click **View Certificate**.
2.  In the Certificate dialog, select the **Details** tab, which displays the serial number and other useful properties of the certificate.

### Step 3: Determine the certificates trusted by the local machine

To be able to deploy an app package, it must not only be trusted in the user’s context but also the local computer context. As a result, the digital signature can appear valid when viewed in the Digital Signatures tab from the previous step but still fail validation during deployment of the app package.

**To determine if the certificate chain used to sign the app package is specifically trusted by the local computer**

1.  Run this command:

    ``` syntax
    CertUtil.exe -store Root rootCertSerialNumber
    ```

2.  Run this command:

    ``` syntax
    CertUtil.exe -store TrustedPeople signingCertSerialNumber
    ```

If you don't specify the certificate serial number, [Certutil](/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/cc732443(v=ws.10)) lists all certificates that are trusted by the local computer for that store.

The package may fail to install due to certificate chaining errors, even if the signing certificate is not self-signed and the root certificate is in the root store of the local computer. In this case, there might be an issue with trust for the intermediate certificate authorities. For more info about this issue, see [Working with Certificates](/previous-versions/dotnet/netframework-3.0/ms731899(v=vs.85)).

## Remarks

If you determined that the package couldn't be deployed because the signing certificate isn't trusted, don't install the package unless you know where it originated and you trust it.

If you want to manually trust the app for install (for example, to install your own test-signed app package), you can manually add the certificate to the local computer certificate trust from the app package.

**To manually add the certificate to the local computer certificate trust**

1.  In File Explorer, right-click on the app package, and in the pop-up context menu select **Properties**.
2.  In the **Properties** dialog, select the **Digital Signatures** tab.
3.  In the Signature list, select the signature and then click the **Details** button.
4.  In the **Digital Signature Details** dialog, click the **View Certificate** button.
5.  In the **Certificate** dialog, click the **Install Certificate…** button.
6.  In the Certificate Import Wizard, select **Local Machine** and then click **Next**. You will need to grant administrator privileges to continue.
7.  Select **Place all certificates in the following store** and browse to the **Trusted People** store.
8.  Click **Next**, then click **Finish** to complete the wizard.

After this manual addition, you can see that the certificate is now trusted in the **Certificate** dialog.

You can remove the certificate after you no longer need it.

**To remove the certificate**

1.  Run **Cmd.exe** as administrator.
2.  In the administrator command prompt, run this command:

    ``` syntax
    Certutil -store TrustedPeople
    ```

3.  Look for the serial number of the certificate that you installed. This number is the *certID*.
4.  Run this command:

    ``` syntax
    Certutil -delStore TrustedPeople certID
    ```

We recommend that you avoid manually adding root certificates to the local machine [Trusted Root Certification Authorities Certificate Store](/windows-hardware/drivers/install/trusted-root-certification-authorities-certificate-store). Having several applications that are signed with certificates that chain to the same root certificate, such as line of business applications, can be more efficient than installing individual certificates to the Trusted People store. The Trusted People store contains certificates that are considered trusted by default and so aren't verified by higher authorities or certificate trust lists or chains. For considerations around adding certificates to the Trusted Root Certification Authorities certificate store, see [Code-Signing Best Practices](/previous-versions/windows/hardware/design/dn653556(v=vs.85)).

## Security Considerations

By adding a certificate to [local machine certificate stores](/windows-hardware/drivers/install/local-machine-and-current-user-certificate-stores), you affect the certificate trust of all users on the computer. We recommend that you install any code signing certificates that you want for testing app packages to the Trusted People certificate store. Promptly remove those certificates when they are no longer necessary, to prevent them from being used to compromise system trust. If you create your own test certificates for signing app packages, we also recommend that you restrict the privileges that are associated with the test certificate. For info about creating test certificates for signing app packages, see [How to create an app package signing certificate](how-to-create-a-package-signing-certificate.md).

## Related topics

<dl> <dt>

**Samples**
</dt> <dt>

[Create app package sample](https://github.com/microsoft/Windows-classic-samples/tree/master/Samples/AppxPackingCreateAppx)
</dt> <dt>

**Concepts**
</dt> <dt>

[Troubleshooting packaging, deployment, and query of Windows apps](troubleshooting.md)
</dt> <dt>

[Certutil tasks for managing certificates](/previous-versions/orphan-topics/ws.10/cc772898(v=ws.10))
</dt> </dl>

 

 
