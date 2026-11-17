---
title: Windows endpoint security platform requirements, signing, and enrollment
description: Requirements for using the Windows endpoint security platform, including how to sign and enroll
author: tomlavoy
ms.author: tlavoy
ms.topic: overview
ms.date: 11/16/2026
---

# Windows endpoint security platform requirements, signing, and enrollment

## Supported Windows releases

The Windows endpoint security platform is supported starting with the October 2026 (10D) Windows 11 client releases: version 25H2 (OS build 26200.9818) and version 26H2 (OS build 26300.9818).

## Application requirements

### Product eligibility and signing

In the initial release, you **must** be a member of the [Microsoft Virus Initiative](/defender-xdr/virus-initiative-criteria) (MVI) program to register with the platform as a client. Future updates to the Windows endpoint security platform will provide access to some capabilities without requiring MVI membership. You will also need to sign your security product using [Artifact Signing](/azure/artifact-signing/quickstart). Only applications properly signed using an Artifact Signing certificate profile with the Windows endpoint security platform program type can register with the platform and access these APIs.

Once you have signed your application using Artifact Signing, the enhanced key usage (EKU) associated with your signed product will be added to a secure Code Integrity policy file. These files are regularly serviced via Windows security updates. Once your EKU is present in the appropriate Code Integrity policy file on a Windows client, your application will be recognized by the Windows endpoint security platform as an approved client that can register and access the platform's capabilities.

See the Frequently Asked Questions (FAQ) section below for more detailed guidance on this process.

### Developing and testing before gaining access

You can begin developing, evaluating, and testing your product on the platform without meeting the above requirements by following the [test and validation guide](wesp-debug-process-tagging.md) in your Windows environment. Note that this is not supported for production deployments, and is important to test your product in an environment that enforces real signing and policies before a production release.

## Signing and certificate profiles - frequently asked questions (FAQ)

This section explains how to prepare Artifact Signing certificate profiles for the Windows endpoint security platform (sometimes shorthanded as "WESP"). It focuses on the decisions and actions needed to begin onboarding.

For general Artifact Signing concepts and procedures, refer to the [Artifact Signing](/azure/artifact-signing/quickstart) documentation.

### Start here

1. Review the [Artifact Signing resource model](/azure/artifact-signing/concept-resources-roles) and complete identity validation.
2. Create a [Public Trust certificate profile](/azure/artifact-signing/quickstart#create-a-certificate-profile) in the Azure portal. Select **Windows endpoint security platform** as the program type.
3. Sign your main executable directly with the profile and link it with [`/integritycheck`](/cpp/build/reference/integritycheck). The signature must be embedded in the executable. Catalog signing does not provide authorization to the platform. DLLs loaded by the WESP executable do not need WESP embedded signatures.
4. Wait for Microsoft to confirm that the enhanced key usage (EKU) value has completed review and policy delivery before making a release depend on platform access.


### 1. Why does Windows endpoint security platform require an Artifact Signing certificate profile?

You may already use Artifact Signing or another signing process for your software. Partners that join Artifact Signing must meet and maintain identity validation requirements. The platform requires a profile with the "Windows endpoint security platform" program type because the profile's EKU becomes the application identity used for access control.

When the application starts, Windows verifies its approved Artifact Signing identity and EKU, then grants the platform capability tier assigned to that EKU. The profile does not replace any other signing profile or signing requirement your product may have.

### 2. Should we create one profile per company, product, application, or version?

Create one profile for each application that needs an independent platform identity. Reuse it across normal updates/releases of an application.

Use separate profiles when:

- Different applications need different capability tiers.
- Access to one application must be removable without affecting another.

Do not create a separate account and profile solely for business continuity or regional outage resiliency without first confirming the requirement and supported deployment regions. See [How does Artifact Signing handle regional availability?](#5-how-does-artifact-signing-handle-regional-availability).

If multiple applications share the same executable or DLL, see [How should I handle components shared across applications?](#8-how-should-i-handle-components-shared-across-applications) before finalizing the signing pipeline.

### 3. How do tenants, subscriptions, accounts, and identity validation relate?

Artifact Signing identity validation is associated with the Azure subscription:

- Accounts in the same subscription can reuse the validation.
- A different subscription requires another identity-validation process.
- One Entra tenant can own multiple subscriptions.

Choose the subscription and account layout before creating a large set of profiles. Keeping related accounts in one subscription reduces repeated validation work.

See the public [Artifact Signing FAQ](/azure/artifact-signing/faq) for the service's identity-validation behavior.

### 4. What if we need more than 10 Public Trust profiles?

The profile limit applies to each Artifact Signing account:

- Basic supports one profile of each type.
- Premium supports 10 profiles of each type.
- You can create additional accounts under the same subscription.
- Accounts in the same subscription can reuse identity validation.

Review the current [Artifact Signing SKU guidance](/azure/artifact-signing/how-to-change-sku) before choosing the account layout. Contact Microsoft before large-scale provisioning if multi-region operations or a large application portfolio creates a high profile count.

### 5. How does Artifact Signing handle regional availability?

Artifact Signing provides automatic paired regions for certificate profiles within that account, so partners do not need to create additional certificate profiles solely for business continuity, disaster recovery, or a regional outage.

Artifact Signing uses the following region pairings:

| Primary region | Paired region |
| --- | --- |
| East US | West US 3 |
| West US 2 | West Central US |
| Central US | West US |
| South Central US | North Central US |
| West Europe | North Europe |
| Poland Central | Switzerland North |
| Japan East | Korea Central |
| Brazil South | Mexico Central |

### 6. Can I add the WESP program type to an existing certificate profile?

Existing profiles cannot currently be edited to add the "Windows endpoint security platform" program type. Delete and recreate the profile with the same name and select the "Windows endpoint security platform" program type.

Deleting a profile does not invalidate files that were already signed. The deleted profile cannot issue new signatures, and the recreated profile receives a new EKU.

**Before deleting an existing profile**

- Record the profile and signing configuration.
- Plan the change so normal signing is not interrupted.
- Keep releases from depending on the new EKU until Microsoft confirms policy delivery.

### 7. Can I automate profile creation?

Create profiles in the Azure portal. The Azure CLI does not currently expose the "Windows endpoint security platform" program type option.

Use the public [certificate profile creation instructions](/azure/artifact-signing/quickstart#create-a-certificate-profile) for the supported workflow. If you manage many profiles, keep an inventory of the subscription, account, profile, application, region, environment, and EKU.

### 8. How should I handle components shared across applications?

The main `/integritycheck` executable must carry an embedded signature from the WESP Artifact Signing profile. Catalog signing does not provide platform authorization. DLLs loaded by that executable do not need WESP embedded signatures.

If the same executable code ships with multiple applications, products, or platform capability tiers, produce a separately signed binary for each application using the certificate profile associated with that application. Do not reuse one WESP-signed binary across application identities or rely on a catalog to change its identity.

Microsoft is continuing to investigate ways to simplify shared-component management in a future release.

### 9. Does an EKU identify our company or application?

The EKU identifies a certificate profile. It does not contain a readable company or application name, and there is no public reverse lookup from the EKU to the subscriber.

Keep an internal inventory that maps:

- Entra tenant and Azure subscription.
- Artifact Signing account and profile.
- Application and environment.
- Region.
- EKU.

Microsoft validates the relationship among the partner, application, profile, and EKU during platform onboarding.

### 10. When does a new profile receive platform access?

Creating a profile and successfully signing an application do not immediately activate access to the Windows endpoint security platform. Access begins after:

1. Microsoft reviews the profile and EKU.
2. The EKU is assigned to the approved capability tier.
3. The updated platform policy, contained in a Code Integrity policy file, is delivered to the device through Windows servicing.

Submit profile details early. Keep an existing approved profile active until replacement EKUs are available on the Windows versions and devices your release supports.

Microsoft has not published a guaranteed onboarding lead time. Plan releases around an explicit policy-delivery confirmation.

### 11. What happens when a profile is deleted or platform access is revoked?

Artifact Signing certificate lifecycles and Windows endpoint security platform access policies are separate:

- Deleting a profile does not invalidate files already signed with it.
- Removing an EKU from WESP policy removes platform access after the updated policy reaches the device.
- Certificate revocation is reserved for compromise or severe misuse and can affect trust beyond WESP.

Contact Microsoft immediately for a suspected compromise or an urgent access-removal request. Do not assume certificate revocation and policy removal have the same timing or scope.

Additional guidance for long-term certificate rollover, certificate-revocation timing, and already running processes will be shared in the future.

### 12. What happens on devices that do not receive Windows updates?

The platform policy containing the approved EKU must be present on the device. A device that does not receive the required policy may not recognize a newly approved application.

Microsoft has not published a partner policy-sideload process. Contact Microsoft before depending on Windows endpoint security platform access in an air-gapped environment or an environment that restricts Windows servicing or certificate trust updates.

## Additional documentation and support

- Public Artifact Signing documentation: [overview](/azure/artifact-signing/overview), [resource model](/azure/artifact-signing/concept-resources-roles), [profile creation](/azure/artifact-signing/quickstart#create-a-certificate-profile), [SKU guidance](/azure/artifact-signing/how-to-change-sku), and [FAQ](/azure/artifact-signing/faq).
- Windows endpoint security platform (WESP) profile submission: [WESP profile form](https://aka.ms/wesp).
