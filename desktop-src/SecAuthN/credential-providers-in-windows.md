---
description: Credential providers are the primary mechanism for user authentication. They currently are the only method for users to prove their identity which is required for logon and other system authentication scenarios.
ms.assetid: BCF69196-D4E4-41D0-B372-5000FD50164B
title: Credential Providers in Windows
ms.topic: concept-article
ms.date: 01/31/2024
---

# Credential Providers in Windows

Credential providers are the primary mechanism for user authentication. They currently are the only method for users to prove their identity which is required for logon and other system authentication scenarios. Since Windows 10 and the introduction of Microsoft Passport, credential providers have been more important than ever. They are used for authentication into apps, websites, and more.

Microsoft provides a variety of credential providers as part of Windows, such as password, PIN, smartcard, and Windows Hello (Fingerprint, Face, and Iris recognition). These are referred to as "system credential providers" in this article. OEMs, Enterprises, and other entities can write their own credential providers and integrate them easily into Windows. These are referred to as "third-party credential providers" in this article. Note that both V1 and V2 credential providers are supported in Windows. It's important for creators and managers of third-party credential providers to understand these recommendations.

## System credential providers

It's strongly recommended that there always be at least one system credential provider available for every user on the device in addition to any third-party credential providers. Additionally, during the set-up of the third-party credential provider, each user on the device should be prompted to configure at least one system credential provider (if no other recovery options are available; see Scenario A, below).

### Scenario A

A local account user has set up a third-party credential provider and regularly uses it to log into the device. One day, the user installs some update to the device that breaks the third-party credential provider, and the user is unaware of this change before restarting the machine.

On the next restart, the user is on the logon screen and is unable to use the expected third-party credential provider. If the user has set up a system credential provider, the user will be able to log into the machine using it. If not, the user has no way to recover the account on the machine.

### Scenario B

A Microsoft Account (MSA), Active Directory (AD), or Microsoft Entra ID account user has set up a third-party credential provider and regularly uses it to log into the device. One day, the user installs some update to the device that breaks the third-party credential provider, and the user is unaware of this change before restarting the machine.

On the next restart, the user is on the logon screen and is unable to use the expected third-party credential provider. If the user has configured a system credential provider, the user will be able to log into the machine using it. Alternatively, if the system's password credential provider is available, the user can remotely request/reset the password and use that to log into the machine. If neither option is available, the user has no way to recover the account on the machine.

### Conclusion

In summary, the disabling of all system credential providers on a device should be discouraged. While third-party credential providers may fulfill additional authentication requirements for particular groups of users, it is very important to ensure that the user can always regain access to their machine when a breaking change occurs. System credential providers provide this guarantee.

## Custom credential providers

The Windows credential provider framework enables developers to create custom credential providers. When [Winlogon](winlogon.md) wants to collect credentials, the Logon UI queries each credential provider for the number of credentials that it wishes to enumerate. After all providers have enumerated their tiles, the Logon UI displays them to the user. The user then interacts with a tile to supply the necessary credentials. The Logon UI submits these credentials for authentication. Credential providers can also be used by the Credential UI when credentials are necessary. See [CREDENTIAL_PROVIDER_USAGE_SCENARIO](/windows/win32/api/credentialprovider/ne-credentialprovider-credential_provider_usage_scenario) for a list of scenarios where a credential provider can be supported.

Thanks to this system, it's much easier to create a credential provider than it was historically. Much of the work is handled by the combination of [Winlogon](winlogon.md), the Logon UI and the Credential UI. In order to do so, you will need to create your own implementation of [ICredentialProvider](/windows/win32/api/credentialprovider/nn-credentialprovider-icredentialprovider) and [ICredentialProviderCredential](/windows/win32/api/credentialprovider/nn-credentialprovider-icredentialprovidercredential). If you are implementing a V2 credential provider, which is recommended, you will also need to implement [ICredentialProviderCredential2](/windows/win32/api/credentialprovider/nn-credentialprovider-icredentialprovidercredential2).

It's important to note that credential providers are not enforcement mechanisms. They are used to gather and serialize credentials, submitting them for authorization. The local authority and authentication packages will handle and any necessary security enforcement.

By combining credential providers with supported hardware, you can extend Windows to support logging on with biometric information, passwords, PINs, Smart Card certificates, or any custom authentication package you choose to create. You can customize the logon experience for the user in a variety of ways as well. For example, when the Logon UI queries your credential provider for the credential tiles, you can specify a default tile to provide a customized experience for a user. Credential providers can even be designed to support single sign on (SSO), authenticating users to a secure access point as well as machine logon.

Credential providers are registered on a Windows machine and are responsible for the following.

- Describing the credential information required for authentication.
- Handling the communication and logic with any external authentication authorities.
- Packaging the credentials for interactive and network logon.

> [!TIP]
> Remember that multiple credential providers can be installed on a single machine.

## Wrapping credential providers

Wrapping a system credential provider can be done to add functionality to that credential provider that isn't natively supported. This isn't recommended because it can lead to problematic behavior. Changes can be made to the credential provider which may conflict with the wrapper, causing a poor user experience or even preventing the user from accessing their device. This is especially true with the frequent update cadence of Windows.

If functionality in a credential provider is needed that isn't included natively, the recommended path is creating a custom credential provider. This is a more stable approach that doesn't have dependencies on the system providers.

## See also

- [Credential Provider driven Windows Logon Experience](https://go.microsoft.com/fwlink/?LinkId=717287)
- [ICredentialProvider](/windows/win32/api/credentialprovider/nn-credentialprovider-icredentialprovider)
- [CREDENTIAL_PROVIDER_CREDENTIAL_SERIALIZATION](/windows/win32/api/credentialprovider/ns-credentialprovider-credential_provider_credential_serialization)
- [CREDENTIAL_PROVIDER_USAGE_SCENARIO](/windows/win32/api/credentialprovider/ne-credentialprovider-credential_provider_usage_scenario)
