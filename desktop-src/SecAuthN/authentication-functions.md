---
description: Lists the functions used in authentication APIs.
ms.assetid: 946ab34a-f52a-4720-8516-cdcae2883d9b
title: Authentication Functions
ms.topic: article
ms.date: 05/31/2018
---

# Authentication Functions

Authentication functions are categorized according to usage as follows:

- [SSPI Functions](#sspi-functions)
  - [Package Management](#package-management)
  - [Credential Management](#credential-management)
  - [Context Management](#context-management)
  - [Message Support](#message-support)
- [Functions Implemented by SSP/APs](#functions-implemented-by-sspaps)
- [Functions Implemented by User-mode SSP/APs](#functions-implemented-by-user-mode-sspaps)
- [LSA Functions Called by SSP/APs](#lsa-functions-called-by-sspaps)
- [LSA Functions Called By User-mode SSP/APs](#lsa-functions-called-by-user-mode-sspaps)
- [GINA Export Functions](#gina-export-functions)
- [Logon User Functions](#logon-user-functions)
- [Winlogon Support Functions](#winlogon-support-functions)
- [Network Provider Functions](#network-provider-functions)
  - [Functions Implemented by Network Providers](#functions-implemented-by-network-providers)
  - [Support Functions](#winlogon-support-functions)
  - [Connection Notification Functions](#connection-notification-functions)
- [LSA Logon Functions](#lsa-logon-functions)
- [Functions Implemented by Authentication Packages](#functions-implemented-by-authentication-packages)
- [LSA Functions Called by Authentication Packages](#lsa-functions-called-by-authentication-packages)
- [Subauthentication Functions](#subauthentication-functions)
- [Credentials Management Functions](#credentials-management-functions)
  - [Credentials Management UI Functions](#credentials-management-ui-functions)
  - [Low-level Credentials Management Functions](#low-level-credentials-management-functions)
  - [Credential Management Notification Functions](#credential-management-notification-functions)
- [Smart Card Functions](#smart-card-functions)
- [SASL Functions](#sasl-functions)
- [Other Functions](#other-functions)

## SSPI Functions

Security Support Provider Interface (SSPI) functions fall into the following major categories.

- [Package management](#package-management)

    Functions that list the available [*security packages*](/windows/desktop/SecGloss/s-gly) and select a package.

- [Credential management](#credential-management)

    Functions that create and work with handles to the [*credentials*](/windows/desktop/SecGloss/c-gly) of [*principals*](/windows/desktop/SecGloss/p-gly).

- [Context management](#context-management)

    Functions that use credentials handles to create a [*security context*](/windows/desktop/SecGloss/s-gly).

- [Message support](#message-support)

    Functions that use security contexts to ensure message [*integrity*](/windows/desktop/SecGloss/i-gly) and [*privacy*](/windows/desktop/SecGloss/p-gly) during message exchanges over the secured connection. Integrity is achieved through message signing and signature verification. Privacy is achieved through message encryption and decryption.

### Package Management

SSPI package management functions initiate a [*security package*](/windows/desktop/SecGloss/s-gly), enumerate available packages, and query the attributes of a security package. The following SSPI functions provide management services for security packages.

| Function | Description |
|--------|--------|
| [**EnumerateSecurityPackages**](/windows/desktop/api/Sspi/nf-sspi-enumeratesecuritypackagesa) | Lists available security packages and their capabilities. |
| [**InitSecurityInterface**](/windows/desktop/api/Sspi/nf-sspi-initsecurityinterfacea)         | Retrieves a pointer to a security support provider (SSP) dispatch table. |
| [**QuerySecurityPackageInfo**](/windows/desktop/api/Sspi/nf-sspi-querysecuritypackageinfoa)   | Retrieves information about a specified [*security package*](/windows/desktop/SecGloss/s-gly). This information includes the bounds on sizes of authentication information, [*credentials*](/windows/desktop/SecGloss/c-gly), and contexts. |

### Credential Management

SSPI credential management functions provide a [*credentials*](/windows/desktop/SecGloss/c-gly) handle, a reference to an opaque security object, for accessing a principal. The security object is opaque because the application has access only to the handle and not to the actual contents of the structure.

All references to the contents of a credential context are through the object's handle and the [*security package*](/windows/desktop/SecGloss/s-gly) dereferences the handle to access the specifics of credentials. A credential handle is a 64-bit value between {0x00000000, 0x00000000} and {0xFFFFFFFF, 0xFFFFFFFE}.

Applications use the credentials handle with [context management](#context-management) functions to create a [*security context*](/windows/desktop/SecGloss/s-gly).

Credential management functions also release credential handles and query the [*attributes*](/windows/desktop/SecGloss/a-gly) of [*credentials*](/windows/desktop/SecGloss/c-gly). At present, the name associated with a credential is the only attribute that can be queried.

The following functions are used with credentials management.

| Function | Description |
|--------|--------|
| [**AcquireCredentialsHandle (General)**](/windows/win32/api/sspi/nf-sspi-acquirecredentialshandlea) | Acquires a handle to the preexisting credentials of a specified principal. |
| [**ExportSecurityContext**](/windows/desktop/api/Sspi/nf-sspi-exportsecuritycontext)                           | Exports a security context into a context buffer. |
| [**FreeCredentialsHandle**](/windows/desktop/api/Sspi/nf-sspi-freecredentialshandle)                           | Releases a credential handle and associated resources. |
| [**ImportSecurityContext**](/windows/desktop/api/Sspi/nf-sspi-importsecuritycontexta)                           | Imports a security context exported by using [**ExportSecurityContext**](/windows/desktop/api/Sspi/nf-sspi-exportsecuritycontext) into the current process. |
| [**QueryCredentialsAttributes**](/windows/desktop/api/Sspi/nf-sspi-querycredentialsattributesa)                 | Retrieves the [*attributes*](/windows/desktop/SecGloss/a-gly) of a [*credential*](/windows/desktop/SecGloss/c-gly), such as the name associated with the credential. |

### Context Management

SSPI context management functions create and use [*security contexts*](/windows/desktop/SecGloss/s-gly).

In a communication link, the client and server cooperate to create a shared security context. The client and server both use the security context with [message support](#message-support) functions to ensure message [*integrity*](/windows/desktop/SecGloss/i-gly) and [*privacy*](/windows/desktop/SecGloss/p-gly) during the connection.

Security contexts are opaque security objects. Information in the security context is not available to the application. Context management functions create and use context handles and the security package dereferences the context handle to access its security content.

A context handle is a 64-bit value between {0x00000000, 0x00000000} and {0xFFFFFFFF, 0xFFFFFFFE}.

The following functions are used with context management.

| Function | Description |
|--------|--------|
| [**AcceptSecurityContext (General)**](/windows/win32/api/sspi/nf-sspi-acceptsecuritycontext)         | Used by a server to create a [*security context*](/windows/desktop/SecGloss/s-gly) based on an opaque message received from a client. |
| [**ApplyControlToken**](/windows/desktop/api/Sspi/nf-sspi-applycontroltoken)                                     | Applies a supplemental security message to an existing security context. |
| [**CompleteAuthToken**](/windows/desktop/api/Sspi/nf-sspi-completeauthtoken)                                     | Completes an authentication token. This function is used by protocols, such as DCE, that need to revise the security information after the transport application has updated some message parameters. |
| [**DeleteSecurityContext**](/windows/desktop/api/Sspi/nf-sspi-deletesecuritycontext)                             | Frees a security context and associated resources. |
| [**FreeContextBuffer**](/windows/desktop/api/Sspi/nf-sspi-freecontextbuffer)                                     | Frees a memory buffer allocated by a security package. |
| [**ImpersonateSecurityContext**](/windows/desktop/api/Sspi/nf-sspi-impersonatesecuritycontext)                   | Impersonates the security context to appear as the client to the system. |
| [**InitializeSecurityContext (General)**](/windows/win32/api/sspi/nf-sspi-initializesecuritycontexta) | Used by a client to initiate a security context by generating an opaque message to be passed to a server. |
| [**QueryContextAttributes (General)**](/windows/win32/api/sspi/nf-sspi-querycontextattributesa)       | Enables a transport application to query a [*security package*](/windows/desktop/SecGloss/s-gly) for certain [*attributes*](/windows/desktop/SecGloss/a-gly) of a security [*context*](/windows/desktop/SecGloss/c-gly). |
| [**QuerySecurityContextToken**](/windows/desktop/api/Sspi/nf-sspi-querysecuritycontexttoken)                     | Obtains the [*access token*](/windows/desktop/SecGloss/a-gly) for a client [*security context*](/windows/desktop/SecGloss/s-gly) and uses it directly. |
| [**SetContextAttributes**](/windows/desktop/api/Sspi/nf-sspi-setcontextattributesa)                               | Enables a transport application to set [*attributes*](/windows/desktop/SecGloss/a-gly) of a security [*context*](/windows/desktop/SecGloss/c-gly) for a [*security package*](/windows/desktop/SecGloss/s-gly). This function is supported only by the Schannel security package. |
| [**RevertSecurityContext**](/windows/desktop/api/Sspi/nf-sspi-revertsecuritycontext)                             | Allows a [*security package*](/windows/desktop/SecGloss/s-gly) to discontinue the impersonation of the caller and restore its own [*security context*](/windows/desktop/SecGloss/s-gly). |

### Message Support

SSPI message support functions enable an application to transmit and receive tamper-resistant messages and to encrypt and decrypt messages. These functions work with one or more buffers that contain a message and with a [*security context*](/windows/desktop/SecGloss/s-gly) created by the [context management](#context-management) functions. The functions' behavior differs based on whether a connection, [*datagram*](/windows/desktop/SecGloss/d-gly), or stream context is in use. For a description of these differences, see [SSPI Context Semantics](sspi-context-semantics.md).

The following functions provide security support for messages.

| Function | Description |
|--------|--------|
| [**DecryptMessage (General)**](/windows/win32/api/sspi/nf-sspi-decryptmessage) | Decrypts an encrypted message by using the [*session key*](/windows/desktop/SecGloss/s-gly) from a [*security context*](/windows/desktop/SecGloss/s-gly). |
| [**EncryptMessage (General)**](/windows/win32/api/sspi/nf-sspi-encryptmessage) | Encrypts a message by using the session key from a security context. |
| [**MakeSignature**](/windows/desktop/api/Sspi/nf-sspi-makesignature)                       | Generates a cryptographic checksum of the message, and also includes sequencing information to prevent message loss or insertion. |
| [**VerifySignature**](/windows/desktop/api/Sspi/nf-sspi-verifysignature)                   | Verifies the signature of a message received that was signed by the sender by using the [**MakeSignature**](/windows/desktop/api/Sspi/nf-sspi-makesignature) function. |

## Functions Implemented by SSP/APs

The following functions are implemented by [security packages](#sspi-functions) contained in [*Security Support Provider*](/windows/desktop/SecGloss/s-gly)/[*Authentication Packages*](/windows/desktop/SecGloss/a-gly) (SSP/APs).

In the following tables, the first set of functions is implemented by Windows XP SSP/AP security packages. The second set of functions is implemented by SSP/AP security packages only.

The [*Local Security Authority*](/windows/desktop/SecGloss/l-gly) (LSA) accesses these functions by using the [**SECPKG\_FUNCTION\_TABLE**](/windows/desktop/api/Ntsecpkg/ns-ntsecpkg-secpkg_function_table) structure provided by the SSP/AP's [**SpLsaModeInitialize**](/windows/desktop/api/Ntsecpkg/nc-ntsecpkg-splsamodeinitializefn) function.

The following functions are implemented by all authentication packages.

| Function | Description |
|--------|--------|
| [**LsaApCallPackage**](/windows/desktop/api/Ntsecpkg/nc-ntsecpkg-lsa_ap_call_package)                       | Called by the [*Local Security Authority*](/windows/desktop/SecGloss/l-gly) (LSA) when a logon application with a trusted connection to the LSA calls the [**LsaCallAuthenticationPackage**](/windows/desktop/api/Ntsecapi/nf-ntsecapi-lsacallauthenticationpackage) function and specifies the authentication package's identifier. |
| [**LsaApCallPackagePassthrough**](/windows/desktop/api/Ntsecpkg/nc-ntsecpkg-lsa_ap_call_package_passthrough) | The dispatch function for pass-through logon requests sent to the [**LsaCallAuthenticationPackage**](/windows/desktop/api/Ntsecapi/nf-ntsecapi-lsacallauthenticationpackage) function |
| [**LsaApCallPackageUntrusted**](/previous-versions/windows/desktop/legacy/aa378218(v=vs.85))     | Called by the [*Local Security Authority*](/windows/desktop/SecGloss/l-gly) (LSA) when an application with an untrusted connection to the LSA calls the [**LsaCallAuthenticationPackage**](/windows/desktop/api/Ntsecapi/nf-ntsecapi-lsacallauthenticationpackage) function and specifies the authentication package's identifier. |
| [**LsaApInitializePackage**](/windows/desktop/api/Ntsecpkg/nc-ntsecpkg-lsa_ap_initialize_package)           | Called once by the [*Local Security Authority*](/windows/desktop/SecGloss/l-gly) (LSA) during system initialization to provide the authentication package a chance to initialize itself. |
| [**LsaApLogonTerminated**](/windows/desktop/api/Ntsecpkg/nc-ntsecpkg-lsa_ap_logon_terminated)               | Used to notify an authentication package when a logon session terminates. A logon session terminates when the last token referencing the logon session is deleted. |
| [**LsaApLogonUser**](/windows/desktop/api/Ntsecpkg/nc-ntsecpkg-lsa_ap_logon_user)                           | Authenticates a user's logon credentials. |
| [**LsaApLogonUserEx**](/windows/desktop/api/Ntsecpkg/nc-ntsecpkg-lsa_ap_logon_user_ex)                       | Authenticates a user's logon credentials. |
| [**LsaApLogonUserEx2**](/windows/desktop/api/Ntsecpkg/nc-ntsecpkg-lsa_ap_logon_user_ex2)                     | Used to authenticate a user logon attempt on the user's initial logon. A new logon session is established for the user, and validation information for the user is returned. |

The following additional functions are implemented by SSP/AP security packages.

| Function | Description |
|--------|--------|
| [**SpAcceptCredentials**](/windows/desktop/api/Ntsecpkg/nc-ntsecpkg-spacceptcredentialsfn)                   | Called by the [*Local Security Authority*](/windows/desktop/SecGloss/l-gly) (LSA) to pass the [*security package*](/windows/desktop/SecGloss/s-gly) any [*credentials*](/windows/desktop/SecGloss/c-gly) stored for the authenticated [*security principal*](/windows/desktop/SecGloss/s-gly). |
| [**SpAcceptLsaModeContext**](/windows/desktop/api/Ntsecpkg/nc-ntsecpkg-spacceptlsamodecontextfn)             | Server dispatch function used to create a [*security context*](/windows/desktop/SecGloss/s-gly) shared by a server and client. |
| [**SpAcquireCredentialsHandle**](/windows/desktop/api/Ntsecpkg/nc-ntsecpkg-spacquirecredentialshandlefn)     | Called to obtain a handle to a principal's [*credentials*](/windows/desktop/SecGloss/c-gly). |
| [**SpAddCredentials**](/windows/desktop/api/Ntsecpkg/nc-ntsecpkg-spaddcredentialsfn)                         | Used to add [*credentials*](/windows/desktop/SecGloss/c-gly) for a [*security principal*](/windows/desktop/SecGloss/s-gly). |
| [**SpApplyControlToken**](/windows/desktop/api/Ntsecpkg/nc-ntsecpkg-spapplycontroltokenfn)                   | Applies a control token to a [*security context*](/windows/desktop/SecGloss/s-gly). This function is not currently called by the [*Local Security Authority*](/windows/desktop/SecGloss/l-gly) (LSA). |
| [**SpDeleteContext**](/windows/desktop/api/Ntsecpkg/nc-ntsecpkg-kspdeletecontextfn)                           | Deletes a [*security context*](/windows/desktop/SecGloss/s-gly). |
| [**SpDeleteCredentials**](/windows/desktop/api/Ntsecpkg/nc-ntsecpkg-spdeletecredentialsfn)                   | Deletes [*credentials*](/windows/desktop/SecGloss/c-gly) from a [*security package's*](/windows/desktop/SecGloss/s-gly) list of [*primary*](/windows/desktop/SecGloss/p-gly) or [*supplemental*](/windows/desktop/SecGloss/s-gly) credentials. |
| [**SpFreeCredentialsHandle**](/windows/desktop/api/Ntsecpkg/nc-ntsecpkg-spfreecredentialshandlefn)           | Frees [*credentials*](/windows/desktop/SecGloss/c-gly) acquired by calling the [**SpAcquireCredentialsHandle**](/windows/desktop/api/Ntsecpkg/nc-ntsecpkg-spacquirecredentialshandlefn) function. |
| [**SpGetCredentials**](/windows/desktop/api/Ntsecpkg/nc-ntsecpkg-spgetcredentialsfn)                         | Retrieves user credentials. |
| [**SpGetExtendedInformation**](/windows/desktop/api/Ntsecpkg/nc-ntsecpkg-spgetextendedinformationfn)         | Provides extended information about a [*security package*](/windows/desktop/SecGloss/s-gly). |
| [**SpGetInfo**](/windows/desktop/api/Ntsecpkg/nc-ntsecpkg-spgetinfofn)                                       | Provides general information about the [*security package*](/windows/desktop/SecGloss/s-gly), such as its name and capabilities. |
| [**SpGetUserInfo**](/windows/desktop/api/Ntsecpkg/nc-ntsecpkg-spgetuserinfofn)                               | Retrieves information about a logon [*session*](/windows/desktop/SecGloss/s-gly). |
| [**SPInitialize**](/windows/desktop/api/Ntsecpkg/nc-ntsecpkg-spinitializefn)                                 | Is called once by the [*Local Security Authority*](/windows/desktop/SecGloss/l-gly) (LSA) to provide a [*security package*](/windows/desktop/SecGloss/s-gly) with general security information and a dispatch table of support functions. |
| [**SpInitLsaModeContext**](/windows/desktop/api/Ntsecpkg/nc-ntsecpkg-spinitlsamodecontextfn)                 | The client dispatch function used to establish a [*security context*](/windows/desktop/SecGloss/c-gly) between a server and client. |
| [**SpQueryContextAttributes**](/windows/desktop/api/Ntsecpkg/nc-ntsecpkg-spquerycontextattributesfn)         | Retrieves the attributes of a [*security context*](/windows/desktop/SecGloss/s-gly). |
| [**SpQueryCredentialsAttributes**](/windows/desktop/api/Ntsecpkg/nc-ntsecpkg-spquerycredentialsattributesfn) | Retrieves the attributes for a [*credential*](/windows/desktop/SecGloss/c-gly). |
| [**SpSaveCredentials**](/windows/desktop/api/Ntsecpkg/nc-ntsecpkg-spsavecredentialsfn)                       | Saves a [*supplemental credential*](/windows/desktop/SecGloss/s-gly) to the user object. |
| [**SpSetExtendedInformation**](/windows/desktop/api/Ntsecpkg/nc-ntsecpkg-spsetextendedinformationfn)         | Sets extended information about the [*security package*](/windows/desktop/SecGloss/s-gly). |
| [**SpShutdown**](/previous-versions/windows/desktop/legacy/aa380183(v=vs.85))                                     | Performs any cleanup required before the SSP/AP is unloaded. |
| [**SslCrackCertificate**](/windows/desktop/api/Schannel/nf-schannel-sslcrackcertificate)                   | Returns an [**X509Certificate**](/windows/desktop/api/Schannel/ns-schannel-x509certificate) structure with the information contained in the specified certificate [*BLOB*](/windows/desktop/SecGloss/b-gly). |
| [**SslEmptyCache**](/windows/desktop/api/Schannel/nf-schannel-sslemptycachea)                               | Removes the specified string from the Schannel cache. |
| [**SslFreeCertificate**](/windows/desktop/api/Schannel/nf-schannel-sslfreecertificate)                     | Frees a certificate that was allocated by a previous call to the [**SslCrackCertificate**](/windows/desktop/api/Schannel/nf-schannel-sslcrackcertificate) function. |

## Functions Implemented by User-mode SSP/APs

The following functions are implemented by [*Security Support Provider*](/windows/desktop/SecGloss/s-gly)/[*Authentication Packages*](/windows/desktop/SecGloss/a-gly) (SSP/APs) that can be loaded into client/server applications.

An SSP/AP indicates that it implements the user-mode functions by returning **TRUE** in the *MappedContext* parameter of the [**SpInitLsaModeContext**](/windows/desktop/api/Ntsecpkg/nc-ntsecpkg-spinitlsamodecontextfn) and [**SpAcceptLsaModeContext**](/windows/desktop/api/Ntsecpkg/nc-ntsecpkg-spacceptlsamodecontextfn) functions. The **SpInitLsaModeContext** function is used by the client side of a transport level application, while **SpAcceptLsaModeContext** is used by the server side.

Loading an SSP/AP into the client process or server process is handled by the security provider DLL, either Security.dll or Secur32.dll. The security provider DLL loads the SSP/AP by locating the address of the [**SpUserModeInitialize**](/windows/desktop/api/Ntsecpkg/nc-ntsecpkg-spusermodeinitializefn) function implemented by the SSP/AP and calling it. This function returns a set of tables that contain pointers to the user-mode functions implemented in each [*security package*](/windows/desktop/SecGloss/s-gly).

After the SSP/AP is loaded into the client or server process, the [*Local Security Authority*](/windows/desktop/SecGloss/l-gly) (LSA) will copy the security context information (returned by [**SpInitLsaModeContext**](/windows/desktop/api/Ntsecpkg/nc-ntsecpkg-spinitlsamodecontextfn) or [**SpAcceptLsaModeContext**](/windows/desktop/api/Ntsecpkg/nc-ntsecpkg-spacceptlsamodecontextfn)) and any additional context-related data to the process and call the security package's [**SpInitUserModeContext**](/windows/desktop/api/Ntsecpkg/nc-ntsecpkg-spinitusermodecontextfn) function.

Client/server applications access user-mode functionality by calling [Security Support Provider Interface](sspi.md) (SSPI) functions. The SSPI functions are mapped by the security provider DLL by using the [**SECPKG\_USER\_FUNCTION\_TABLE**](/windows/desktop/api/Ntsecpkg/ns-ntsecpkg-secpkg_user_function_table) supplied by the package.

| Function | Description |
|--------|--------|
| [**SpCompleteAuthToken**](/windows/desktop/api/Ntsecpkg/nc-ntsecpkg-spcompleteauthtokenfn)                 | Completes an authentication token. <br/> Implements the SSPI [**CompleteAuthToken**](/windows/desktop/api/Sspi/nf-sspi-completeauthtoken) function. |
| [**SpDeleteContext**](/windows/desktop/api/Ntsecpkg/nc-ntsecpkg-kspdeletecontextfn)                         | Deletes a [*security context*](/windows/desktop/SecGloss/s-gly).<br/> Implements the SSPI [**DeleteSecurityContext**](/windows/desktop/api/Sspi/nf-sspi-deletesecuritycontext) function. |
| [**SpExportSecurityContext**](/windows/desktop/api/Ntsecpkg/nc-ntsecpkg-spexportsecuritycontextfn)         | Exports a security context to another process.<br/> Implements the SSPI [**ExportSecurityContext**](/windows/desktop/api/Sspi/nf-sspi-exportsecuritycontext) function. |
| [**SpFormatCredentials**](/windows/desktop/api/Ntsecpkg/nc-ntsecpkg-spformatcredentialsfn)                 | Formats [*credentials*](/windows/desktop/SecGloss/c-gly) to be stored in a user object. |
| [**SpGetContextToken**](/windows/desktop/api/Ntsecpkg/nc-ntsecpkg-spgetcontexttokenfn)                     | Obtains the token to impersonate.<br/> Used by the SSPI [**ImpersonateSecurityContext**](/windows/desktop/api/Sspi/nf-sspi-impersonatesecuritycontext) function. |
| [**SpImportSecurityContext**](/windows/desktop/api/Ntsecpkg/nc-ntsecpkg-spimportsecuritycontextfn)         | Imports a security context from another process.<br/> Implements the SSPI [**ImportSecurityContext**](/windows/desktop/api/Sspi/nf-sspi-importsecuritycontexta) function. |
| [**SpInitUserModeContext**](/windows/desktop/api/Ntsecpkg/nc-ntsecpkg-spinitusermodecontextfn)             | Creates a user-mode [*security context*](/windows/desktop/SecGloss/s-gly) from a packed [*Local Security Authority*](/windows/desktop/SecGloss/l-gly) (LSA)-mode context. |
| [**SpInstanceInit**](/windows/desktop/api/Ntsecpkg/nc-ntsecpkg-spinstanceinitfn)                           | Initializes user-mode security packages in an SSP/AP. |
| [**SpMakeSignature**](/windows/desktop/api/Ntsecpkg/nc-ntsecpkg-kspmakesignaturefn)                         | Generates a [*signature*](/windows/desktop/SecGloss/d-gly) based on the specified message and [*security context*](/windows/desktop/SecGloss/s-gly).<br/> Implements the SSPI [**MakeSignature**](/windows/desktop/api/Sspi/nf-sspi-makesignature) function. |
| [**SpMarshallSupplementalCreds**](/windows/desktop/api/Ntsecpkg/nc-ntsecpkg-spmarshallsupplementalcredsfn) | Converts [*supplemental credentials*](/windows/desktop/SecGloss/s-gly) from a public format into a format suitable for local procedure calls. |
| [**SpQueryContextAttributes**](/windows/desktop/api/Ntsecpkg/nc-ntsecpkg-spquerycontextattributesfn)       | Retrieves the attributes of a [*security context*](/windows/desktop/SecGloss/s-gly).<br/> Implements the SSPI [**QueryContextAttributes (General)**](/windows/win32/api/sspi/nf-sspi-querycontextattributesa) function. |
| [**SpSealMessage**](/windows/desktop/api/Ntsecpkg/nc-ntsecpkg-spsealmessagefn)                             | Encrypts a message exchanged between a client and server.<br/> Implements the SSPI [**EncryptMessage (General)**](/windows/win32/api/sspi/nf-sspi-encryptmessage) function. |
| [**SpUnsealMessage**](/windows/desktop/api/Ntsecpkg/nc-ntsecpkg-spunsealmessagefn)                         | Decrypts a message that was previously encrypted with the [**SpSealMessage**](/windows/desktop/api/Ntsecpkg/nc-ntsecpkg-spsealmessagefn) function.<br/> Implements the SSPI [**DecryptMessage (General)**](/windows/win32/api/sspi/nf-sspi-decryptmessage) function. |
| [**SpUserModeInitialize**](/windows/desktop/api/Ntsecpkg/nc-ntsecpkg-spusermodeinitializefn)               | Called when a [*Security Support Provider*](/windows/desktop/SecGloss/s-gly)/[*authentication package*](/windows/desktop/SecGloss/a-gly) (SSP/AP) DLL is loaded into the process space of a client/server application. This function provides the [**SECPKG\_USER\_FUNCTION\_TABLE**](/windows/desktop/api/Ntsecpkg/ns-ntsecpkg-secpkg_user_function_table) tables for each [*security package*](/windows/desktop/SecGloss/s-gly) in the SSP/AP DLL. |
| [**SpVerifySignature**](/windows/desktop/api/Ntsecpkg/nc-ntsecpkg-kspverifysignaturefn)                     | Verifies that the message received is correct according to the [*signature*](/windows/desktop/SecGloss/d-gly).<br/> Implements the SSPI [**VerifySignature**](/windows/desktop/api/Sspi/nf-sspi-verifysignature) function. |

## LSA Functions Called by SSP/APs

The [*Local Security Authority*](/windows/desktop/SecGloss/l-gly) (LSA) provides the following functions to [*security packages*](/windows/desktop/SecGloss/s-gly) deployed in [*Security Support Provider*](/windows/desktop/SecGloss/s-gly)/[*Authentication Packages*](/windows/desktop/SecGloss/a-gly) (SSP/APs). The functions are available in the [**LSA\_SECPKG\_FUNCTION\_TABLE**](/windows/desktop/api/Ntsecpkg/ns-ntsecpkg-secpkg_function_table) structure and can be called while the SSP/AP is loaded into the LSA's process space. The following functions are available to all APs.

| Function | Description |
|--------|--------|
| [**AddCredential**](/windows/desktop/api/Ntsecpkg/nc-ntsecpkg-lsa_add_credential)               | Adds user [*credentials*](/windows/desktop/SecGloss/c-gly). |
| [**AllocateClientBuffer**](/windows/desktop/api/Ntsecpkg/nc-ntsecpkg-lsa_allocate_client_buffer) | Allocates memory in the address space of the package's client. |
| [**AllocateLsaHeap**](/windows/desktop/api/Ntsecpkg/nc-ntsecpkg-lsa_allocate_lsa_heap)           | Allocates memory on the heap. Some information passed back to the LSA is expected to be allocated using this function. |
| [**CopyFromClientBuffer**](/windows/desktop/api/Ntsecpkg/nc-ntsecpkg-lsa_copy_from_client_buffer) | Copies information from the address space of a client process into a buffer in the current process. |
| [**CopyToClientBuffer**](/windows/desktop/api/Ntsecpkg/nc-ntsecpkg-lsa_copy_to_client_buffer)     | Copies information from a buffer in the current process into a client process's address space. |
| [**CreateLogonSession**](/windows/desktop/api/Ntsecpkg/nc-ntsecpkg-lsa_create_logon_session)     | Creates logon sessions. |
| [**DeleteCredential**](/windows/desktop/api/Ntsecpkg/nc-ntsecpkg-lsa_delete_credential)         | Deletes user credentials. |
| [**DeleteLogonSession**](/windows/desktop/api/Ntsecpkg/nc-ntsecpkg-lsa_delete_logon_session)     | Deletes an LSA logon session. |
| [**FreeClientBuffer**](/windows/desktop/api/Ntsecpkg/nc-ntsecpkg-lsa_free_client_buffer)         | Frees memory in the address space of the package's client. |
| [**FreeLsaHeap**](/windows/win32/api/ntlsa/nc-ntlsa-lsa_free_lsa_heap)                   | Deallocates heap memory previously allocated by [**AllocateLsaHeap**](/windows/desktop/api/Ntsecpkg/nc-ntsecpkg-lsa_allocate_lsa_heap). |
| [**GetCredentials**](/windows/desktop/api/Ntsecpkg/nc-ntsecpkg-lsa_get_credentials)             | Retrieves credentials associated with a logon session. |

The following functions are available to SSP/APs.

| Function | Description |
|--------|--------|
| [**AllocateSharedMemory**](/windows/desktop/api/Ntsecpkg/nc-ntsecpkg-lsa_allocate_shared_memory)     | Allocates a section of shared memory. |
| [**AuditAccountLogon**](/windows/desktop/api/Ntsecpkg/nc-ntsecpkg-lsa_audit_account_logon)           | Creates audit records for attempted logons. |
| [**AuditLogon**](/windows/desktop/api/Ntsecpkg/nc-ntsecpkg-lsa_audit_logon)                         | Creates an audit trail for a logon session. |
| [**CallPackage**](/windows/desktop/api/Ntsecpkg/nc-ntsecpkg-lsa_call_package)                       | Calls a package. |
| [**CallPackageEx**](/windows/desktop/api/Ntsecpkg/nc-ntsecpkg-lsa_call_packageex)                   | Calls another package. |
| [**CallPackagePassthrough**](/windows/desktop/api/Ntsecpkg/nc-ntsecpkg-lsa_call_package_passthrough) | Calls one security package from another. |
| [**CancelNotification**](/windows/desktop/api/Ntsecpkg/nc-ntsecpkg-lsa_cancel_notification)         | Cancels notification for special events. |
| [**ClientCallback**](/windows/desktop/api/Ntsecpkg/nc-ntsecpkg-lsa_client_callback)                 | Allows a security package to invoke a function in the client process.<br/> For a [**ClientCallback**](/windows/desktop/api/Ntsecpkg/nc-ntsecpkg-lsa_client_callback) function prototype, see [*ClientCallback Function Prototype*](/previous-versions/windows/desktop/legacy/aa374759(v=vs.85)). |
| [**CloseSamUser**](/windows/desktop/api/Ntsecpkg/nc-ntsecpkg-lsa_close_sam_user)                     | Closes a handle to a Security Accounts Manager database entry. |
| [**ConvertAuthDataToToken**](/windows/desktop/api/Ntsecpkg/nc-ntsecpkg-lsa_convert_auth_data_to_token) | Converts authorization data to a user token. |
| [**CrackSingleName**](/windows/desktop/api/Ntsecpkg/nc-ntsecpkg-lsa_crack_single_name)               | Converts a name from one format to another. |
| [**CreateSharedMemory**](/windows/desktop/api/Ntsecpkg/nc-ntsecpkg-lsa_create_shared_memory)         | Creates a section of memory shared between clients and the SSP/AP. |
| [**CreateThread**](/windows/win32/api/ntsecpkg/nc-ntsecpkg-lsa_create_thread)                     | Creates a new thread. |
| [**CreateToken**](/windows/desktop/api/Ntsecpkg/nc-ntsecpkg-lsa_create_token)                       | Creates a token. |
| [**DeleteSharedMemory**](/windows/desktop/api/Ntsecpkg/nc-ntsecpkg-lsa_delete_shared_memory)         | Deletes a section of shared memory. |
| [**DuplicateHandle**](/windows/win32/api/ntsecpkg/nc-ntsecpkg-lsa_duplicate_handle)               | Duplicates a handle. |
| [**FreeReturnBuffer**](/windows/desktop/api/Ntsecpkg/nc-ntsecpkg-lsa_free_lsa_heap)             | Frees a buffer allocated by the LSA. |
| [**FreeSharedMemory**](/windows/desktop/api/Ntsecpkg/nc-ntsecpkg-lsa_free_shared_memory)             | Frees a section of shared memory. |
| [**GetAuthDataForUser**](/windows/desktop/api/Ntsecpkg/nc-ntsecpkg-lsa_get_auth_data_for_user)         | Retrieves authorization data for a user account. |
| [**GetCallInfo**](/windows/desktop/api/Ntsecpkg/nc-ntsecpkg-lsa_get_call_info)                       | Retrieves information about the most recent function call. |
| [**GetClientInfo**](/windows/desktop/api/Ntsecpkg/nc-ntsecpkg-lsa_get_client_info)                   | Retrieves information about the security package's user process. |
| [**GetUserAuthData**](/windows/desktop/api/Ntsecpkg/nc-ntsecpkg-lsa_get_user_auth_data)               | Returns the authorization data for a user. |
| **GetUserCredentials**                                   | Not yet implemented. |
| [**ImpersonateClient**](/previous-versions/windows/desktop/legacy/aa375494(v=vs.85))           | Called by [*security packages*](/windows/desktop/SecGloss/s-gly) to impersonate the package user. |
| [**MapBuffer**](/windows/desktop/api/Ntsecpkg/nc-ntsecpkg-lsa_map_buffer)                           | Maps a [**SecBuffer**](/windows/desktop/api/Sspi/ns-sspi-secbuffer) structure into the address space of the [*Security Support Provider*](/windows/desktop/SecGloss/s-gly)/[*authentication package*](/windows/desktop/SecGloss/a-gly) (SSP/AP). |
| [**OpenSamUser**](/windows/desktop/api/Ntsecpkg/nc-ntsecpkg-lsa_open_sam_user)                       | Retrieves a handle to a user account in the [*Security Accounts Manager*](/windows/desktop/SecGloss/s-gly) (SAM) database. |
| [**RegisterNotification**](/windows/win32/api/ntsecpkg/nc-ntsecpkg-lsa_register_notification)     | Provides a mechanism whereby the [*security package*](/windows/desktop/SecGloss/s-gly) is notified. Notification can occur at fixed intervals, when an event object is signaled, or during certain system events. |
| **SaveSupplementalCredentials**                          | Obsolete. Do not use. |
| [**UnloadPackage**](/previous-versions/windows/desktop/legacy/aa380520(v=vs.85))                   | Unloads an [*Security Support Provider*](/windows/desktop/SecGloss/s-gly)/[*authentication package*](/windows/desktop/SecGloss/a-gly) (SSP/AP). |
| [**UpdateCredentials**](/windows/desktop/api/Ntsecpkg/nc-ntsecpkg-lsa_update_primary_credentials)           | Provides a mechanism for one [*security package*](/windows/desktop/SecGloss/s-gly) to notify other packages that the [*credentials*](/windows/desktop/SecGloss/c-gly) for a logon [*session*](/windows/desktop/SecGloss/s-gly) have changed. |

## LSA Functions Called By User-mode SSP/APs

A [*security package*](/windows/desktop/SecGloss/s-gly) in a [*Security Support Provider*](/windows/desktop/SecGloss/s-gly)/[*authentication package*](/windows/desktop/SecGloss/a-gly) (SSP/AP) executing in a user-mode process can use the pointers in the [**SECPKG\_DLL\_FUNCTIONS**](/windows/desktop/api/Ntsecpkg/ns-ntsecpkg-secpkg_dll_functions) table to access the following functions.

| Function | PSDK status |
|--------|--------|
| [**AllocateHeap**](/previous-versions/windows/desktop/legacy/aa374721(v=vs.85))         | Allocates memory for buffers that are returned to the [*Local Security Authority*](/windows/desktop/SecGloss/l-gly) (LSA). |
| [**FreeHeap**](/previous-versions/windows/desktop/legacy/aa375418(v=vs.85))                 | Frees memory that was previously allocated by using [**AllocateHeap**](/previous-versions/windows/desktop/legacy/aa374721(v=vs.85)). |
| [**RegisterCallback**](/previous-versions/windows/desktop/legacy/aa379372(v=vs.85)) | Registers user-mode callback functions. |

## GINA Export Functions

A [*GINA*](/windows/desktop/SecGloss/g-gly) DLL must export the following functions.

> [!NOTE]
> GINA DLLs are ignored in Windows Vista.

| Function | Description |
|--------|--------|
| [**WlxActivateUserShell**](/windows/desktop/api/Winwlx/nf-winwlx-wlxactivateusershell)                     | Activates the user shell program. |
| [**WlxDisplayLockedNotice**](/windows/desktop/api/Winwlx/nf-winwlx-wlxdisplaylockednotice)                 | Allows the GINA to display information about the lock, such as who locked the workstation and when it was locked. |
| [**WlxDisplaySASNotice**](/windows/desktop/api/Winwlx/nf-winwlx-wlxdisplaysasnotice)                       | [*Winlogon*](/windows/desktop/SecGloss/w-gly) calls this function when no user is logged on. |
| [**WlxDisplayStatusMessage**](/windows/desktop/api/Winwlx/nf-winwlx-wlxdisplaystatusmessage)               | [*Winlogon*](/windows/desktop/SecGloss/w-gly) calls this function when the GINA DLL should display a message. |
| [**WlxGetConsoleSwitchCredentials**](/windows/desktop/api/Winwlx/nf-winwlx-wlxgetconsoleswitchcredentials) | [*Winlogon*](/windows/desktop/SecGloss/w-gly) calls this function to read the currently logged on user's credentials to transparently transfer them to a target session. |
| [**WlxGetStatusMessage**](/windows/desktop/api/Winwlx/nf-winwlx-wlxgetstatusmessage)                       | [*Winlogon*](/windows/desktop/SecGloss/w-gly) calls this function to get the status message being displayed by the GINA DLL. |
| [**WlxInitialize**](/windows/desktop/api/Winwlx/nf-winwlx-wlxinitialize)                                   | [*Winlogon*](/windows/desktop/SecGloss/w-gly) calls this function once for each window station present on the computer. Currently, the operating system supports one window station per workstation. |
| [**WlxIsLockOk**](/windows/desktop/api/Winwlx/nf-winwlx-wlxislockok)                                       | [*Winlogon*](/windows/desktop/SecGloss/w-gly) calls this function before attempting to lock the workstation. |
| [**WlxIsLogoffOk**](/windows/desktop/api/Winwlx/nf-winwlx-wlxislogoffok)                                   | [*Winlogon*](/windows/desktop/SecGloss/w-gly) calls this function when the user initiates a logoff operation. |
| [**WlxLoggedOnSAS**](/windows/desktop/api/Winwlx/nf-winwlx-wlxloggedonsas)                                 | [*Winlogon*](/windows/desktop/SecGloss/w-gly) calls this function when it receives a [*secure attention sequence*](/windows/desktop/SecGloss/s-gly) (SAS) event while the user is logged on and the workstation is not locked. |
| [**WlxLoggedOutSAS**](/windows/desktop/api/Winwlx/nf-winwlx-wlxloggedoutsas)                               | [*Winlogon*](/windows/desktop/SecGloss/w-gly) calls this function when it receives a [*secure attention sequence*](/windows/desktop/SecGloss/s-gly) (SAS) event while no user is logged on. |
| [**WlxLogoff**](/windows/desktop/api/Winwlx/nf-winwlx-wlxlogoff)                                           | [*Winlogon*](/windows/desktop/SecGloss/w-gly) calls this function to notify the GINA of a logoff operation on this workstation, allowing the GINA to perform any logoff operations that may be required. |
| [**WlxNegotiate**](/windows/desktop/api/Winwlx/nf-winwlx-wlxnegotiate)                                     | The [**WlxNegotiate**](/windows/desktop/api/Winwlx/nf-winwlx-wlxnegotiate) function must be implemented by a replacement [*GINA*](/windows/desktop/SecGloss/g-gly) DLL. This is the first call made by [*Winlogon*](/windows/desktop/SecGloss/w-gly) to the GINA DLL. **WlxNegotiate** allows the GINA to verify that it supports the installed version of Winlogon. |
| [**WlxNetworkProviderLoad**](/windows/desktop/api/Winwlx/nf-winwlx-wlxnetworkproviderload)                 | [*Winlogon*](/windows/desktop/SecGloss/w-gly) calls this function to collect valid authentication and identification information. |
| [**WlxRemoveStatusMessage**](/windows/desktop/api/Winwlx/nf-winwlx-wlxremovestatusmessage)                 | [*Winlogon*](/windows/desktop/SecGloss/w-gly) calls this function to tell the GINA DLL to stop displaying the status message. |
| [**WlxScreenSaverNotify**](/windows/desktop/api/Winwlx/nf-winwlx-wlxscreensavernotify)                     | [*Winlogon*](/windows/desktop/SecGloss/w-gly) calls this function immediately before a screen saver is activated, allowing the GINA to interact with the screen saver program. |
| [**WlxShutdown**](/windows/desktop/api/Winwlx/nf-winwlx-wlxshutdown)                                       | [*Winlogon*](/windows/desktop/SecGloss/w-gly) calls this function just before shutting down, allowing the GINA to perform any shutdown tasks, such as ejecting a [*smart card*](/windows/desktop/SecGloss/s-gly) from a [*reader*](/windows/desktop/SecGloss/r-gly). |
| [**WlxStartApplication**](/windows/desktop/api/Winwlx/nf-winwlx-wlxstartapplication)                       | [*Winlogon*](/windows/desktop/SecGloss/w-gly) calls this function when the system needs an application to be started in the [*context*](/windows/desktop/SecGloss/c-gly) of the user. |
| [**WlxWkstaLockedSAS**](/windows/desktop/api/Winwlx/nf-winwlx-wlxwkstalockedsas)                           | [*Winlogon*](/windows/desktop/SecGloss/w-gly) calls this function when it receives a [*secure attention sequence*](/windows/desktop/SecGloss/s-gly) (SAS) and the workstation is locked. |

## Logon User Functions

The following functions provide the ability to log on a user.

| Function | Description |
|--------|--------|
| [**LogonUser**](/windows/desktop/api/Winbase/nf-winbase-logonusera)           | Attempts to log a user on to the local computer. |
| [**LogonUserEx**](/windows/desktop/api/Winbase/nf-winbase-logonuserexa)       | Attempts to log a user on to the local computer. This function is an extended version of the [**LogonUser**](/windows/desktop/api/Winbase/nf-winbase-logonusera) function and retrieves information about the logged-on user's [*security identifier*](/windows/desktop/SecGloss/s-gly) (SID), profile, and quota limits. |
| [**LogonUserExExW**](logonuserexexw.md) | The [**LogonUserExExW**](logonuserexexw.md) function attempts to log a user on to the local computer. This function is not declared in a public header and has no associated import library. You must use the [**LoadLibrary**](/windows/desktop/api/libloaderapi/nf-libloaderapi-loadlibrarya) and [**GetProcAddress**](/windows/desktop/api/libloaderapi/nf-libloaderapi-getprocaddress) functions to dynamically link to Advapi32.dll. |

## Winlogon Support Functions

[*GINA*](/windows/desktop/SecGloss/g-gly) DLLs can call the following [*Winlogon*](/windows/desktop/SecGloss/w-gly) support functions.

> [!NOTE]
> GINA DLLs are ignored in Windows Vista.

| Function | Called by GINA |
|--------|--------|
| [**WlxAssignShellProtection**](/windows/win32/api/winwlx/nc-winwlx-pwlx_assign_shell_protection)                 | Called by [*GINA*](/windows/desktop/SecGloss/g-gly) to assign protection to the shell program of a newly logged-on user. |
| [**WlxChangePasswordNotify**](/windows/win32/api/winwlx/nc-winwlx-pwlx_change_password_notify)                   | Called by [*GINA*](/windows/desktop/SecGloss/g-gly) to indicate it has changed a password. |
| [**WlxChangePasswordNotifyEx**](/windows/win32/api/winwlx/nc-winwlx-pwlx_change_password_notify_ex)               | Called by [*GINA*](/windows/desktop/SecGloss/g-gly) to tell a specific network provider (or all network providers) that a password has changed. |
| [**WlxCloseUserDesktop**](/windows/win32/api/winwlx/nc-winwlx-pwlx_close_user_desktop)                           | Called by [*GINA*](/windows/desktop/SecGloss/g-gly) to close an alternate user desktop and clean up after the desktop is closed. |
| [**WlxCreateUserDesktop**](/windows/win32/api/winwlx/nc-winwlx-pwlx_create_user_desktop)                         | Called by [*GINA*](/windows/desktop/SecGloss/g-gly) to create alternate application desktops for the user. |
| [**WlxDialogBox**](/windows/win32/api/winwlx/nc-winwlx-pwlx_dialog_box)                                         | Called by the [*GINA*](/windows/desktop/SecGloss/g-gly) to create a modal dialog box from a dialog box template. |
| [**WlxDialogBoxIndirect**](/windows/win32/api/winwlx/nc-winwlx-pwlx_dialog_box_indirect)                         | Called by [*GINA*](/windows/desktop/SecGloss/g-gly) to create a modal dialog box from a dialog box template in memory. |
| [**WlxDialogBoxIndirectParam**](/windows/win32/api/winwlx/nc-winwlx-pwlx_dialog_box_indirect_param)               | Called by [*GINA*](/windows/desktop/SecGloss/g-gly) to initialize dialog box controls and then create a modal dialog box from a dialog box template in memory. |
| [**WlxDialogBoxParam**](/windows/win32/api/winwlx/nc-winwlx-pwlx_dialog_box_param)                               | Called by [*GINA*](/windows/desktop/SecGloss/g-gly) to initialize dialog box controls and then create a modal dialog box from a dialog box template resource. |
| [**WlxDisconnect**](/windows/win32/api/winwlx/nc-winwlx-pwlx_disconnect)                                       | Called by a replacement GINA DLL if Terminal Services is enabled. [*GINA*](/windows/desktop/SecGloss/g-gly) calls this function to disconnect from a Terminal Services network session. |
| [**WlxGetOption**](/windows/win32/api/winwlx/nc-winwlx-pwlx_get_option)                                         | Called by [*GINA*](/windows/desktop/SecGloss/g-gly) to retrieve the current value of an option. |
| [**WlxGetSourceDesktop**](/windows/win32/api/winwlx/nc-winwlx-pwlx_get_source_desktop)                           | Called by [*GINA*](/windows/desktop/SecGloss/g-gly) to determine the name and handle of the desktop that was current before [*Winlogon*](/windows/desktop/SecGloss/w-gly) switched to the Winlogon desktop. |
| [**WlxMessageBox**](/windows/win32/api/winwlx/nc-winwlx-pwlx_message_box)                                       | Called by [*GINA*](/windows/desktop/SecGloss/g-gly) to create, display, and operate a message box. |
| [**WlxQueryClientCredentials**](/windows/win32/api/winwlx/nc-winwlx-pwlx_query_client_credentials)               | Called by a replacement GINA DLL if Terminal Services is enabled. GINA calls this function to retrieve the credentials of remote Terminal Services clients that are not using an Internet connector license. |
| [**WlxQueryConsoleSwitchCredentials**](/windows/win32/api/winwlx/nc-winwlx-pwlx_query_consoleswitch_credentials) | Called by [*GINA*](/windows/desktop/SecGloss/g-gly) to read the credentials transferred from the Winlogon of the temporary session to the Winlogon of the destination session. |
| [**WlxQueryInetConnectorCredentials**](/windows/win32/api/winwlx/nc-winwlx-pwlx_query_ic_credentials) | Called by a replacement GINA DLL if Terminal Services is enabled. [*GINA*](/windows/desktop/SecGloss/g-gly) calls this function to determine whether the terminal server is using Internet connector licensing and to retrieve [*credentials*](/windows/desktop/SecGloss/c-gly) information. |
| [**WlxQueryTerminalServicesData**](/windows/win32/api/winwlx/nc-winwlx-pwlx_query_terminal_services_data)         | Called by [*GINA*](/windows/desktop/SecGloss/g-gly) to retrieve Terminal Services user configuration information after a user has logged on. |
| [**WlxSasNotify**](/windows/win32/api/winwlx/nc-winwlx-pwlx_sas_notify)                                         | Called by [*GINA*](/windows/desktop/SecGloss/g-gly) to notify [*Winlogon*](/windows/desktop/SecGloss/w-gly) of a [*secure attention sequence*](/windows/desktop/SecGloss/s-gly) (SAS) event. |
| [**WlxSetContextPointer**](/windows/win32/api/winwlx/nc-winwlx-pwlx_set_context_pointer)                         | Called by [*GINA*](/windows/desktop/SecGloss/g-gly) to specify the [*context*](/windows/desktop/SecGloss/c-gly) pointer passed by [*Winlogon*](/windows/desktop/SecGloss/w-gly) as the first parameter to all future calls to GINA functions. |
| [**WlxSetOption**](/windows/win32/api/winwlx/nc-winwlx-pwlx_set_option)                                         | Called by [*GINA*](/windows/desktop/SecGloss/g-gly) to set the value of an option. |
| [**WlxSetReturnDesktop**](/windows/win32/api/winwlx/nc-winwlx-pwlx_set_return_desktop)                           | Called by [*GINA*](/windows/desktop/SecGloss/g-gly) to specify the alternate application desktop that [*Winlogon*](/windows/desktop/SecGloss/w-gly) will switch to when the current [*secure attention sequence*](/windows/desktop/SecGloss/s-gly) (SAS) event processing function is complete. |
| [**WlxSetTimeout**](/windows/win32/api/winwlx/nc-winwlx-pwlx_set_timeout)                                       | Called by [*GINA*](/windows/desktop/SecGloss/g-gly) to change the time-out associated with a dialog box. The default time-out is two minutes. |
| [**WlxSwitchDesktopToUser**](/windows/win32/api/winwlx/nc-winwlx-pwlx_switch_desktop_to_user)                     | Called by [*GINA*](/windows/desktop/SecGloss/g-gly) to switch to the application desktop. |
| [**WlxSwitchDesktopToWinlogon**](/windows/win32/api/winwlx/nc-winwlx-pwlx_switch_desktop_to_winlogon)             | Allows the [*GINA*](/windows/desktop/SecGloss/g-gly) DLL switch to the [*Winlogon*](/windows/desktop/SecGloss/w-gly) desktop. |
| [**WlxUseCtrlAltDel**](/windows/win32/api/winwlx/nc-winwlx-pwlx_use_ctrl_alt_del)                                 | Called by [*GINA*](/windows/desktop/SecGloss/g-gly) to tell [*Winlogon*](/windows/desktop/SecGloss/w-gly) to use the standard CTRL+ALT+DEL key combination as a [*secure attention sequence*](/windows/desktop/SecGloss/s-gly) (SAS). |
| [**WlxWin31Migrate**](/windows/win32/api/winwlx/nc-winwlx-pwlx_win31_migrate)                                   | Called by a replacement GINA DLL if Terminal Services is enabled. [*GINA*](/windows/desktop/SecGloss/g-gly) calls this function to complete the setup of the Terminal Services client. |

## Network Provider Functions

The following topics provide reference information for the network provider functions.

| Topic | Description |
|--------|--------|
| Functions Implemented by Network Providers | Details functions that can be implemented by network providers. |
| Support Functions                          | Details a function that is implemented by the operating system and can be called by network providers. |
| Connection Notification Functions          | Details functions that are implemented by applications that need to receive notification from the [*Multiple Provider Router*](/windows/desktop/SecGloss/m-gly) (MPR) when a network resource is connected or disconnected. |

### Functions Implemented by Network Providers

The following functions can be implemented by network providers. The only function that network providers are required to support is [**NPGetCaps**](/windows/desktop/api/Npapi/nf-npapi-npgetcaps).

| Function | Description |
|--------|--------|
| [**NPAddConnection**](/windows/desktop/api/Npapi/nf-npapi-npaddconnection)                       | Connects a local device to a network resource. |
| [**NPAddConnection3**](/windows/desktop/api/Npapi/nf-npapi-npaddconnection3)                     | Connects a local device to a network resource. |
| [**NPCancelConnection**](/windows/desktop/api/Npapi/nf-npapi-npcancelconnection)                 | Disconnects a network connection. |
| [**NPCloseEnum**](/windows/desktop/api/Npapi/nf-npapi-npcloseenum)                               | Closes an enumeration. |
| [**NPDeviceMode**](/windows/desktop/api/Npapi/nf-npapi-npdevicemode)                             | Specifies the parent window of a device. This window owns any dialog boxes that originate from the device. |
| [**NPDirectoryNotify**](/windows/desktop/api/Npapi/nf-npapi-npdirectorynotify)                   | Notifies the network provider of certain directory operations. |
| [**NPEnumResource**](/windows/desktop/api/Npapi/nf-npapi-npenumresource)                         | Performs an enumeration based on a handle returned by [**NPOpenEnum**](/windows/desktop/api/Npapi/nf-npapi-npopenenum). |
| [**NPFormatNetworkName**](/windows/desktop/api/Npapi/nf-npapi-npformatnetworkname)               | Formats a network name in a provider-specific format for display in a control. |
| [**NPGetCaps**](/windows/desktop/api/Npapi/nf-npapi-npgetcaps)                                   | Returns information about which services are supported on the network. |
| [**NPGetConnection**](/windows/desktop/api/Npapi/nf-npapi-npgetconnection)                       | Retrieves information about a connection. |
| [**NPGetConnection3**](/windows/desktop/api/Npapi/nf-npapi-npgetconnection3)                     | Retrieves information about a network connection, even if it is currently disconnected. |
| [**NPGetConnectionPerformance**](/windows/desktop/api/Npapi/nf-npapi-npgetconnectionperformance) | Returns information about the expected performance of a connection used to access a network resource. The request can only be for a network resource that is currently connected. |
| [**NPGetDirectoryType**](/windows/desktop/api/Npapi/nf-npapi-npgetdirectorytype)                 | Determines the type of a network directory. |
| [**NPGetPropertyText**](/windows/desktop/api/Npapi/nf-npapi-npgetpropertytext)                   | Retrieves the names of buttons to add to a property dialog box for a network resource. |
| [**NPGetResourceInformation**](/windows/desktop/api/Npapi/nf-npapi-npgetresourceinformation)     | Separates the part of a network resource accessed through the WNet API from the part accessed through APIs specific to the resource type. |
| [**NPGetResourceParent**](/windows/desktop/api/Npapi/nf-npapi-npgetresourceparent)               | Retrieves the parent of a specified network resource in the browse hierarchy. |
| [**NPGetUniversalName**](/windows/desktop/api/Npapi/nf-npapi-npgetuniversalname)                 | Retrieves the universal name of a network resource. The [**NPGetUniversalName**](/windows/desktop/api/Npapi/nf-npapi-npgetuniversalname) function can retrieve this universal name in UNC format or in the older, remote-name format. |
| [**NPGetUser**](/windows/desktop/api/Npapi/nf-npapi-npgetuser)                                   | Retrieves the value of the current default user name or the user name used to establish a network connection. |
| [**NPOpenEnum**](/windows/desktop/api/Npapi/nf-npapi-npopenenum)                                 | Opens an enumeration of network resources or existing connections. The [**NPOpenEnum**](/windows/desktop/api/Npapi/nf-npapi-npopenenum) function must be called to obtain a valid handle for an enumeration. |
| [**NPPropertyDialog**](/windows/desktop/api/Npapi/nf-npapi-nppropertydialog)                     | Called when the user clicks a button added by using the [**NPPropertyDialog**](/windows/desktop/api/Npapi/nf-npapi-nppropertydialog) function. The **NPPropertyDialog** function is called only for file and directory network properties. |
| [**NPSearchDialog**](/windows/desktop/api/Npapi/nf-npapi-npsearchdialog)                         | Enables network vendors to supply their own form of browsing and search, beyond the hierarchical view presented in the **Connection** dialog box. |

### Support Functions

The following function is implemented by the operating system and can be called by network providers.

| Function | Description |
|--------|--------|
| [**WNetSetLastError**](/windows/desktop/api/Npapi/nf-npapi-wnetsetlasterrora) | Sets extended error information. Network providers should call this function instead of [**SetLastError**](/windows/desktop/api/errhandlingapi/nf-errhandlingapi-setlasterror). |

### Connection Notification Functions

The following functions are implemented by applications that need to receive notification from the [*Multiple Provider Router*](/windows/desktop/SecGloss/m-gly) (MPR) when a network resource is connected or disconnected. For more information about how to write an application that receives such notifications, see [Receiving Connection Notifications](receiving-connection-notifications.md).

| Function | Description |
|--------|--------|
| [**AddConnectNotify**](/windows/desktop/api/Npapi/nf-npapi-addconnectnotify)       | Called before and after each add connection operation ([**WNetAddConnection**](/windows/desktop/api/winnetwk/nf-winnetwk-wnetaddconnectiona), [**WNetAddConnection2**](/windows/desktop/api/winnetwk/nf-winnetwk-wnetaddconnection2a), and [**WNetAddConnection3**](/windows/desktop/api/winnetwk/nf-winnetwk-wnetaddconnection3a)). |
| [**CancelConnectNotify**](/windows/desktop/api/Npapi/nf-npapi-cancelconnectnotify) | Called before and after each cancel connection operation ([**WNetCancelConnection**](/windows/desktop/api/winnetwk/nf-winnetwk-wnetcancelconnectiona) or [**WNetCancelConnection2**](/windows/desktop/api/winnetwk/nf-winnetwk-wnetcancelconnection2a)). |

## LSA Logon Functions

The following [*Local Security Authority*](/windows/desktop/SecGloss/l-gly) (LSA) authentication functions authenticate and log on users, and they provide logon session information.

| Function | Description |
|--------|--------|
| [**LsaCallAuthenticationPackage**](/windows/desktop/api/Ntsecapi/nf-ntsecapi-lsacallauthenticationpackage)       | Requests a package-specific service from an authentication package. |
| [**LsaConnectUntrusted**](/windows/desktop/api/Ntsecapi/nf-ntsecapi-lsaconnectuntrusted)                         | Establishes an untrusted connection to the LSA. |
| [**LsaDeregisterLogonProcess**](/windows/desktop/api/Ntsecapi/nf-ntsecapi-lsaderegisterlogonprocess)             | Disconnects from the LSA and frees resources allocated to the caller's context. |
| [**LsaEnumerateLogonSessions**](/windows/desktop/api/Ntsecapi/nf-ntsecapi-lsaenumeratelogonsessions)             | Retrieves [*locally unique identifiers*](/windows/desktop/SecGloss/l-gly) (LUIDs) for existing logon sessions. |
| [**LsaFreeReturnBuffer**](/windows/desktop/api/Ntsecapi/nf-ntsecapi-lsafreereturnbuffer)                         | Frees memory allocated for a buffer returned to a caller. |
| [**LsaGetLogonSessionData**](/windows/desktop/api/Ntsecapi/nf-ntsecapi-lsagetlogonsessiondata)                   | Retrieves information about a specified logon session. |
| [**LsaLogonUser**](/windows/desktop/api/Ntsecapi/nf-ntsecapi-lsalogonuser)                                       | Authenticates user logon data against stored credentials. If successful, it creates a new logon session and returns a user token. |
| [**LsaLookupAuthenticationPackage**](/windows/desktop/api/Ntsecapi/nf-ntsecapi-lsalookupauthenticationpackage)   | Obtains the unique identifier of an authentication package. |
| [**LsaQueryDomainInformationPolicy**](/windows/desktop/api/Ntsecapi/nf-ntsecapi-lsaquerydomaininformationpolicy) | Retrieves domain information from the [**Policy**](/windows/desktop/SecMgmt/policy-object) object. |
| [**LsaQueryForestTrustInformation**](/windows/desktop/api/Ntsecapi/nf-ntsecapi-lsaqueryforesttrustinformation)   | Retrieves forest trust information for the specified [*Local Security Authority*](/windows/desktop/SecGloss/l-gly) [**TrustedDomain**](/windows/desktop/SecMgmt/trusteddomain-object) object. |
| [**LsaRegisterLogonProcess**](/windows/desktop/api/Ntsecapi/nf-ntsecapi-lsaregisterlogonprocess)                 | Establishes a connection to the LSA server and verifies that the caller is a logon application. |
| [**LsaSetDomainInformationPolicy**](/windows/desktop/api/Ntsecapi/nf-ntsecapi-lsasetdomaininformationpolicy)     | Sets domain information to the [**Policy**](/windows/desktop/SecMgmt/policy-object) object. |
| [**LsaSetForestTrustInformation**](/windows/desktop/api/Ntsecapi/nf-ntsecapi-lsasetforesttrustinformation)       | sets the forest trust information for a specified [*Local Security Authority*](/windows/desktop/SecGloss/l-gly) [**TrustedDomain**](/windows/desktop/SecMgmt/trusteddomain-object) object. |

## Functions Implemented by Authentication Packages

Custom authentication packages must implement these functions, which are called by the [*Local Security Authority*](/windows/desktop/SecGloss/l-gly) (LSA). These functions are implemented by the MSV1\_0 and Kerberos authentication packages provided by Microsoft.

| Function | Description |
|--------|--------|
| [**LsaApCallPackage**](/windows/desktop/api/Ntsecpkg/nc-ntsecpkg-lsa_ap_call_package)                       | Called when the authentication package's identifier has been specified in a call to [**LsaCallAuthenticationPackage**](/windows/desktop/api/Ntsecapi/nf-ntsecapi-lsacallauthenticationpackage) by an application that is using a trusted connection.<br/> This function provides a way for logon applications to communicate directly with authentication packages. |
| [**LsaApCallPackagePassthrough**](/windows/desktop/api/Ntsecpkg/nc-ntsecpkg-lsa_ap_call_package_passthrough) | Called when the authentication package's identifier has been specified in a call to [**LsaCallAuthenticationPackage**](/windows/desktop/api/Ntsecapi/nf-ntsecapi-lsacallauthenticationpackage) for a pass-through logon request. |
| [**LsaApCallPackageUntrusted**](/previous-versions/windows/desktop/legacy/aa378218(v=vs.85))     | Called when the authentication package's identifier has been specified in a call to [**LsaCallAuthenticationPackage**](/windows/desktop/api/Ntsecapi/nf-ntsecapi-lsacallauthenticationpackage) by an application using an untrusted connection. This function is used for communicating with processes that do not have the SeTcbPrivilege privilege. |
| [**LsaApInitializePackage**](/windows/desktop/api/Ntsecpkg/nc-ntsecpkg-lsa_ap_initialize_package)           | Called during system initialization to permit the authentication package to perform initialization tasks. |
| [**LsaApLogonTerminated**](/windows/desktop/api/Ntsecpkg/nc-ntsecpkg-lsa_ap_logon_terminated)               | Called when a logon session ends to permit the authentication package to free any resources allocated for the logon session. |
| [**LsaApLogonUser**](/windows/desktop/api/Ntsecpkg/nc-ntsecpkg-lsa_ap_logon_user)                           | Called when the authentication package has been specified in a call to [**LsaLogonUser**](/windows/desktop/api/Ntsecapi/nf-ntsecapi-lsalogonuser). This function authenticates a [*security principal's*](/windows/desktop/SecGloss/s-gly) logon data. |
| [**LsaApLogonUserEx**](/windows/desktop/api/Ntsecpkg/nc-ntsecpkg-lsa_ap_logon_user_ex)                       | Identical to [**LsaApLogonUser**](/windows/desktop/api/Ntsecpkg/nc-ntsecpkg-lsa_ap_logon_user) except that it returns the workstation name for audit purposes.<br/> An authentication package can implement [**LsaApLogonUser**](/windows/desktop/api/Ntsecpkg/nc-ntsecpkg-lsa_ap_logon_user), [**LsaApLogonUserEx**](/windows/desktop/api/Ntsecpkg/nc-ntsecpkg-lsa_ap_logon_user_ex), or [**LsaApLogonUserEx2**](/windows/desktop/api/Ntsecpkg/nc-ntsecpkg-lsa_ap_logon_user_ex2). It does not need to implement them all. |
| [**LsaApLogonUserEx2**](/windows/desktop/api/Ntsecpkg/nc-ntsecpkg-lsa_ap_logon_user_ex2)                     | Identical to [**LsaApLogonUserEx**](/windows/desktop/api/Ntsecpkg/nc-ntsecpkg-lsa_ap_logon_user_ex) except that it returns the security principal's primary and supplemental credentials. An authentication package can implement [**LsaApLogonUser**](/windows/desktop/api/Ntsecpkg/nc-ntsecpkg-lsa_ap_logon_user), **LsaApLogonUserEx**, or [**LsaApLogonUserEx2**](/windows/desktop/api/Ntsecpkg/nc-ntsecpkg-lsa_ap_logon_user_ex2). It does not need to implement them all. |

## LSA Functions Called by Authentication Packages

The following [*Local Security Authority*](/windows/desktop/SecGloss/l-gly) (LSA) functions can be called from a custom authentication package. When the LSA calls [**LsaApInitializePackage**](/windows/desktop/api/Ntsecpkg/nc-ntsecpkg-lsa_ap_initialize_package) to initialize the package, it passes a table of support functions.

| Function | Description |
|--------|--------|
| [**AddCredential**](/windows/desktop/api/Ntsecpkg/nc-ntsecpkg-lsa_add_credential)               | Adds credentials to a logon session. |
| [**AllocateClientBuffer**](/windows/desktop/api/Ntsecpkg/nc-ntsecpkg-lsa_allocate_client_buffer) | Allocates a buffer in the client's address space. |
| [**AllocateLsaHeap**](/windows/desktop/api/Ntsecpkg/nc-ntsecpkg-lsa_allocate_lsa_heap)           | Allocates buffers that must be returned from the authentication package to the LSA. |
| [**CopyFromClientBuffer**](/windows/desktop/api/Ntsecpkg/nc-ntsecpkg-lsa_copy_from_client_buffer) | Copies the contents of a buffer in the client's address space into a local buffer. |
| [**CopyToClientBuffer**](/windows/desktop/api/Ntsecpkg/nc-ntsecpkg-lsa_copy_to_client_buffer)     | Copies the contents of a local buffer into the client's address space. |
| [**CreateLogonSession**](/windows/desktop/api/Ntsecpkg/nc-ntsecpkg-lsa_create_logon_session)     | Used by authentication packages to create a logon session. |
| [**DeleteCredential**](/windows/desktop/api/Ntsecpkg/nc-ntsecpkg-lsa_delete_credential)         | Deletes an existing credential. |
| [**DeleteLogonSession**](/windows/desktop/api/Ntsecpkg/nc-ntsecpkg-lsa_delete_logon_session)     | Cleans up any logon sessions created while determining whether a user's authentication information is legitimate. |
| [**FreeClientBuffer**](/windows/desktop/api/Ntsecpkg/nc-ntsecpkg-lsa_free_client_buffer)         | Frees a client buffer previously allocated with the [**AllocateClientBuffer**](/windows/desktop/api/Ntsecpkg/nc-ntsecpkg-lsa_allocate_client_buffer) function. |
| [**FreeLsaHeap**](/windows/win32/api/ntlsa/nc-ntlsa-lsa_free_lsa_heap)                   | Frees buffers previously allocated by using the [**AllocateLsaHeap**](/windows/desktop/api/Ntsecpkg/nc-ntsecpkg-lsa_allocate_lsa_heap) function. |
| [**GetCredentials**](/windows/desktop/api/Ntsecpkg/nc-ntsecpkg-lsa_get_credentials)             | Retrieves credentials previously cached by [**AddCredential**](/windows/desktop/api/Ntsecpkg/nc-ntsecpkg-lsa_add_credential). |

## Subauthentication Functions

The following subauthentication functions can be called by Microsoft-provided authentication packages to provide additional, user-created logon authentication.

| Function | Description |
|--------|--------|
| [**Msv1\_0SubAuthenticationFilter**](/windows/desktop/api/Subauth/nf-subauth-msv1_0subauthenticationfilter)   | Performs user logon authentication that is specific to domain controllers. |
| [**Msv1\_0SubAuthenticationRoutine**](/windows/desktop/api/Subauth/nf-subauth-msv1_0subauthenticationroutine) | Performs client/server-specific authentication. |

## Credentials Management Functions

The following topics provide reference information for the credentials management functions.

| Topic | Description |
|--------|--------|
| Credentials Management UI Functions          | Details functions used for credentials management UI. |
| Low-level Credentials Management Functions   | Details functions used for low-level credentials management. |
| Credential Management Notification Functions | Details functions that are implemented by credential managers to receive notifications when authentication information changes. |

### Credentials Management UI Functions

The following are credentials management UI functions.

| Function | Description |
|--------|--------|
| [**CredUICmdLinePromptForCredentials**](/windows/desktop/api/WinCred/nf-wincred-creduicmdlinepromptforcredentialsa) | Prompt for and accept user credentials information from a user working in a command-line program. |
| [**CredUIConfirmCredentials**](/windows/desktop/api/WinCred/nf-wincred-creduiconfirmcredentialsa)                   | Confirm the validity of credentials returned by [**CredUIPromptForCredentials**](/windows/desktop/api/WinCred/nf-wincred-creduipromptforcredentialsa) or [**CredUICmdLinePromptForCredentials**](/windows/desktop/api/WinCred/nf-wincred-creduicmdlinepromptforcredentialsa). |
| [**CredUIParseUserName**](/windows/desktop/api/WinCred/nf-wincred-creduiparseusernamea)                             | Extract the domain and user account name from a fully qualified user name. |
| [**CredUIPromptForCredentials**](/windows/desktop/api/WinCred/nf-wincred-creduipromptforcredentialsa)               | Display a dialog box that accepts credentials information from a user. |
| [**CredUIPromptForWindowsCredentials**](/windows/desktop/api/WinCred/nf-wincred-creduipromptforwindowscredentialsa) | Creates and displays a configurable dialog box that allows users to supply credential information by using any credential provider installed on the local computer. |
| [**CredUIReadSSOCredW**](/windows/desktop/api/WinCred/nf-wincred-creduireadssocredw)                               | Retrieves the user name for a single logon credential. |
| [**CredUIStoreSSOCredW**](/windows/desktop/api/WinCred/nf-wincred-creduistoressocredw)                             | Stores a single logon credential. |

### Low-level Credentials Management Functions

The following are low-level credentials management functions.

| Function | Description |
|--------|--------|
| [**CredDelete**](/windows/desktop/api/WinCred/nf-wincred-creddeletea)                                         | Delete a credential from a user's credentials set. |
| [**CredEnumerate**](/windows/desktop/api/WinCred/nf-wincred-credenumeratea)                                   | List the credentials in a user's credentials set. |
| [**CredFindBestCredential**](/windows/desktop/api/WinCred/nf-wincred-credfindbestcredentiala)                 | Searches the [Credentials Management](credentials-management.md) (CredMan) database for the set of generic credentials that are associated with the current logon session and that best match the specified target resource. |
| [**CredFree**](/windows/desktop/api/WinCred/nf-wincred-credfree)                                             | Free the memory used for a buffer returned by any of the credentials management functions. |
| [**CredGetSessionTypes**](/windows/desktop/api/WinCred/nf-wincred-credgetsessiontypes)                       | Retrieve the maximum persistence supported by the current logon session. |
| [**CredGetTargetInfo**](/windows/desktop/api/WinCred/nf-wincred-credgettargetinfoa)                           | Retrieve all known target name information for a named resource. |
| [**CredIsMarshaledCredential**](/windows/desktop/api/WinCred/nf-wincred-credismarshaledcredentiala)           | Determines whether a specified user name string is a marshaled credential previously marshaled by [**CredMarshalCredential**](/windows/desktop/api/WinCred/nf-wincred-credmarshalcredentiala). |
| [**CredIsProtected**](/windows/desktop/api/WinCred/nf-wincred-credisprotecteda)                               | Specifies whether the specified credentials are encrypted by a previous call to the [**CredProtect**](/windows/desktop/api/WinCred/nf-wincred-credprotecta) function. |
| [**CredMarshalCredential**](/windows/desktop/api/WinCred/nf-wincred-credmarshalcredentiala)                   | Transform a credential into a text string. |
| [**CredPackAuthenticationBuffer**](/windows/desktop/api/WinCred/nf-wincred-credpackauthenticationbuffera)     | Converts a string user name and password into an authentication buffer. |
| [**CredProtect**](/windows/desktop/api/WinCred/nf-wincred-credprotecta)                                       | Encrypts the specified credentials so that only the current security context can decrypt them. |
| [**CredRead**](/windows/desktop/api/WinCred/nf-wincred-credreada)                                             | Read a credential from a user's credentials set. |
| [**CredReadDomainCredentials**](/windows/desktop/api/WinCred/nf-wincred-credreaddomaincredentialsa)           | Read the domain credentials from a user's credentials set. |
| [**CredRename**](/windows/desktop/api/WinCred/nf-wincred-credrenamea)                                         | Rename a credential from a user's credentials set. |
| [**CredUnmarshalCredential**](/windows/desktop/api/WinCred/nf-wincred-credunmarshalcredentiala)               | Transform a marshaled credential string back into its nonmarshaled form. |
| [**CredUnPackAuthenticationBuffer**](/windows/desktop/api/WinCred/nf-wincred-credunpackauthenticationbuffera) | Converts an authentication buffer returned by a call to the [**CredUIPromptForWindowsCredentials**](/windows/desktop/api/WinCred/nf-wincred-creduipromptforwindowscredentialsa) function into a string user name and password. |
| [**CredUnprotect**](/windows/desktop/api/WinCred/nf-wincred-credunprotecta)                                   | Decrypts credentials that were previously encrypted by using the [**CredProtect**](/windows/desktop/api/WinCred/nf-wincred-credprotecta) function. |
| [**CredWrite**](/windows/desktop/api/WinCred/nf-wincred-credwritea)                                           | Create a new credential or modify an existing credential in a user's credentials set. |
| [**CredWriteDomainCredentials**](/windows/desktop/api/WinCred/nf-wincred-credwritedomaincredentialsa)         | Write domain credentials to a user's credentials set. |

### Credential Management Notification Functions

The following functions are implemented by credential managers to receive notifications when authentication information changes.

| Function | Description |
|--------|--------|
| [**NPLogonNotify**](/windows/desktop/api/Npapi/nf-npapi-nplogonnotify)                   | MPR calls this function to notify the credential manager that a logon event has occurred, allowing the credential manager to return a logon script. |
| [**NPPasswordChangeNotify**](/windows/desktop/api/Npapi/nf-npapi-nppasswordchangenotify) | MPR calls this function to notify the credential manager of a password change event. |

## Smart Card Functions

The Smart Card SDK provides the following functions.

| Function | Description |
|--------|--------|
| [**GetOpenCardName**](/windows/desktop/api/Winscard/nf-winscard-getopencardnamea)                                           | Replaced by [**SCardUIDlgSelectCard**](/windows/desktop/api/Winscard/nf-winscard-scarduidlgselectcarda), which displays the smart card **Select Card** dialog box. |
| [**SCardAccessStartedEvent**](/windows/desktop/api/Winscard/nf-winscard-scardaccessstartedevent)                           | Gets an event handle when the starting of a smart card resource manager is signaled.                                                                                                                                 |
| [**SCardAddReaderToGroup**](/windows/desktop/api/Winscard/nf-winscard-scardaddreadertogroupa)                               | Adds a [*reader*](/windows/desktop/SecGloss/r-gly) to a reader group.                                                                                                                       |
| [**SCardAudit**](/windows/desktop/api/Winscard/nf-winscard-scardaudit)                                                     | Writes event messages to the Windows application log Microsoft-Windows-SmartCard-Audit/Authentication.                                                                                                               |
| [**SCardBeginTransaction**](/windows/desktop/api/Winscard/nf-winscard-scardbegintransaction)                               | Starts a [*transaction*](/windows/desktop/SecGloss/t-gly).                                                                                                                        |
| [**SCardCancel**](/windows/desktop/api/Winscard/nf-winscard-scardcancel)                                                   | Terminates all outstanding actions within a [*context*](/windows/desktop/SecGloss/c-gly).                                                                                                 |
| **SCardCancelTransaction**                                                           | Reserved for future use.                                                                                                                                                                                             |
| [**SCardConnect**](/windows/desktop/api/Winscard/nf-winscard-scardconnecta)                                                 | Establishes a connection between the calling application and a smart card.                                                                                                                                           |
| [**SCardControl**](/windows/desktop/api/Winscard/nf-winscard-scardcontrol)                                                 | Gets direct control of the reader after [**SCardConnect**](/windows/desktop/api/Winscard/nf-winscard-scardconnecta) is called.                                                                                                                              |
| [**SCardDisconnect**](/windows/desktop/api/Winscard/nf-winscard-scarddisconnect)                                           | Terminates a connection between the calling application and a smart card.                                                                                                                                            |
| [**SCardEndTransaction**](/windows/desktop/api/Winscard/nf-winscard-scardendtransaction)                                   | Completes a [*transaction*](/windows/desktop/SecGloss/t-gly).                                                                                                                     |
| [**SCardEstablishContext**](/windows/desktop/api/Winscard/nf-winscard-scardestablishcontext)                               | Establishes a [*resource manager context*](/windows/desktop/SecGloss/r-gly) for accessing the smart card database.                                      |
| [**SCardForgetCardType**](/windows/desktop/api/Winscard/nf-winscard-scardforgetcardtypea)                                   | Removes a previously defined smart card from the [*smart card subsystem*](/windows/desktop/SecGloss/s-gly).                                                     |
| [**SCardForgetReader**](/windows/desktop/api/Winscard/nf-winscard-scardforgetreadera)                                       | Removes a previously defined reader from the smart card subsystem.                                                                                                                                                   |
| [**SCardForgetReaderGroup**](/windows/desktop/api/Winscard/nf-winscard-scardforgetreadergroupa)                             | Removes a previously defined reader group from the smart card subsystem.                                                                                                                                             |
| [**SCardFreeMemory**](/windows/desktop/api/Winscard/nf-winscard-scardfreememory)                                           | Releases memory allocated by resource manager.                                                                                                                                                                       |
| [**SCardGetAttrib**](/windows/desktop/api/Winscard/nf-winscard-scardgetattrib)                                             | Gets the current reader's attributes from a given [*reader*](/windows/desktop/SecGloss/r-gly), driver, or [*smart card*](/windows/desktop/SecGloss/s-gly). |
| [**SCardGetCardTypeProviderName**](/windows/desktop/api/Winscard/nf-winscard-scardgetcardtypeprovidernamea)                 | Gets the provider name given a card name and provider type.                                                                                                                                                          |
| [**SCardGetDeviceTypeId**](/windows/desktop/api/Winscard/nf-winscard-scardgetdevicetypeida)                                 | Gets the device type identifier of the card reader for the given reader name. This function does not affect the state of the reader.                                                                                 |
| [**SCardGetProviderId**](/windows/desktop/api/Winscard/nf-winscard-scardgetproviderida)                                     | Gets the identifier (GUID) of the [*primary service provider*](/windows/desktop/SecGloss/p-gly) for a smart card.                                       |
| [**SCardGetReaderDeviceInstanceId**](/windows/win32/api/winscard/nf-winscard-scardgetreaderdeviceinstanceida)             | Gets the device instance identifier of the card reader for the given reader name. This function does not affect the state of the reader.                                                                             |
| [**SCardGetReaderIcon**](/windows/win32/api/winscard/nf-winscard-scardgetreadericona)                                     | Gets an icon of the smart card reader for a given reader's name.                                                                                                                                                     |
| [**SCardGetStatusChange**](/windows/desktop/api/Winscard/nf-winscard-scardgetstatuschangea)                                 | Blocks execution until status of the readers changes.                                                                                                                                                                |
| [**SCardGetTransmitCount**](/windows/desktop/api/Winscard/nf-winscard-scardgettransmitcount)                               | Retrieves the number of transmit operations that have completed since the specified card reader was inserted.                                                                                                        |
| [**SCardIntroduceCardType**](/windows/desktop/api/Winscard/nf-winscard-scardintroducecardtypea)                             | Introduces a new smart card to the [*smart card*](/windows/desktop/SecGloss/s-gly) subsystem.                                                                                       |
| [**SCardIntroduceReader**](/windows/desktop/api/Winscard/nf-winscard-scardintroducereadera)                                 | Introduces a new reader to the smart card subsystem.                                                                                                                                                                 |
| [**SCardIntroduceReaderGroup**](/windows/desktop/api/Winscard/nf-winscard-scardintroducereadergroupa)                       | Introduces a new reader group to the smart card subsystem.                                                                                                                                                           |
| [**SCardIsValidContext**](/windows/desktop/api/Winscard/nf-winscard-scardisvalidcontext)                                   | Verifies a smart card context handle.                                                                                                                                                                                |
| [**SCardListCards**](/windows/desktop/api/Winscard/nf-winscard-scardlistcardsa)                                             | Provides a list of smart cards already introduced to the subsystem.                                                                                                                                                  |
| [**SCardListInterfaces**](/windows/desktop/api/Winscard/nf-winscard-scardlistinterfacesa)                                   | Provides a list of interfaces supplied by a given smart card.                                                                                                                                                        |
| [**SCardListReaderGroups**](/windows/desktop/api/Winscard/nf-winscard-scardlistreadergroupsa)                               | Provides a list of reader groups already introduced to the subsystem.                                                                                                                                                |
| [**SCardListReaders**](/windows/desktop/api/Winscard/nf-winscard-scardlistreadersa)                                         | Provides a list of readers already introduced to the subsystem.                                                                                                                                                      |
| [**SCardListReadersWithDeviceInstanceId**](/windows/win32/api/winscard/nf-winscard-scardlistreaderswithdeviceinstanceida) | Gets the list of readers that have provided a device instance identifier. This function does not affect the state of the reader.                                                                                     |
| [**SCardLocateCards**](/windows/desktop/api/Winscard/nf-winscard-scardlocatecardsa)                                         | Locates the cards that match a given [*ATR string*](/windows/desktop/SecGloss/a-gly).                                                                                               |
| [**SCardLocateCardsByATR**](/windows/desktop/api/Winscard/nf-winscard-scardlocatecardsbyatra)                               | Locates the cards that match a given [*ATR string*](/windows/desktop/SecGloss/a-gly).                                                                                               |
| [**SCardReadCache**](/windows/desktop/api/Winscard/nf-winscard-scardreadcachea)                                             | Retrieves the value portion of a name-value pair from the global cache maintained by the [Smart Card Resource Manager](smart-card-resource-manager.md).                                                             |
| [**SCardReconnect**](/windows/desktop/api/Winscard/nf-winscard-scardreconnect)                                             | Reestablishes an existing connection from the calling application to the smart card.                                                                                                                                 |
| [**SCardReleaseContext**](/windows/desktop/api/Winscard/nf-winscard-scardreleasecontext)                                   | Closes an established [*resource manager context*](/windows/desktop/SecGloss/r-gly).                                                                    |
| [**SCardReleaseStartedEvent**](/windows/desktop/api/Winscard/nf-winscard-scardreleasestartedevent)                         | Decrements the reference count for a handle acquired by using the [**SCardAccessStartedEvent**](/windows/desktop/api/Winscard/nf-winscard-scardaccessstartedevent) function.                                                                               |
| [**SCardRemoveReaderFromGroup**](/windows/desktop/api/Winscard/nf-winscard-scardremovereaderfromgroupa)                     | Removes a reader from an existing reader group.                                                                                                                                                                      |
| [**SCardSetAttrib**](/windows/desktop/api/Winscard/nf-winscard-scardsetattrib)                                             | Sets a given reader attribute.                                                                                                                                                                                       |
| [**SCardSetCardTypeProviderName**](/windows/desktop/api/Winscard/nf-winscard-scardsetcardtypeprovidernamea)                 | Sets the provider name for a card name and provider type.                                                                                                                                                            |
| [**SCardStatus**](/windows/desktop/api/Winscard/nf-winscard-scardstatusa)                                                   | Gets the current [*state*](/windows/desktop/SecGloss/s-gly) of a reader.                                                                                                                      |
| [**SCardTransmit**](/windows/desktop/api/Winscard/nf-winscard-scardtransmit)                                               | Sends a service request to a smart card.                                                                                                                                                                             |
| [**SCardUIDlgSelectCard**](/windows/desktop/api/Winscard/nf-winscard-scarduidlgselectcarda)                                 | Displays the smart card **Select Card** dialog box.                                                                                                                                                                  |
| [**SCardWriteCache**](/windows/desktop/api/Winscard/nf-winscard-scardwritecachea)                                           | Writes a name-value pair from a smart card to the global cache maintained by the [Smart Card Resource Manager](smart-card-resource-manager.md).                                                                     |

## SASL Functions

The Simple Authentication and Security Layer (SASL) provides the following functions.

| Functions | Description |
|--------|--------|
| [**SaslAcceptSecurityContext**](/windows/desktop/api/Sspi/nf-sspi-saslacceptsecuritycontext)         | Wraps a standard call to the SSPI [**AcceptSecurityContext (General)**](/windows/win32/api/sspi/nf-sspi-acceptsecuritycontext) function and includes creation of SASL server cookies.              |
| [**SaslEnumerateProfiles**](/windows/desktop/api/Sspi/nf-sspi-saslenumerateprofilesa)                 | Lists the packages that provide a SASL interface.                                                                                                                                |
| [**SaslGetContextOption**](/windows/desktop/api/Sspi/nf-sspi-saslgetcontextoption)                   | Retrieves the specified property of the specified SASL context.                                                                                                                  |
| [**SaslGetProfilePackage**](/windows/desktop/api/Sspi/nf-sspi-saslgetprofilepackagea)                 | Returns the package information for the specified package.                                                                                                                       |
| [**SaslIdentifyPackage**](/windows/desktop/api/Sspi/nf-sspi-saslidentifypackagea)                     | Returns the negotiate prefix that matches the specified SASL negotiation buffer.                                                                                                 |
| [**SaslInitializeSecurityContext**](/windows/desktop/api/Sspi/nf-sspi-saslinitializesecuritycontexta) | Wraps a standard call to the SSPI [**InitializeSecurityContext (General)**](/windows/win32/api/sspi/nf-sspi-initializesecuritycontexta) function and processes SASL server cookies from the server. |
| [**SaslSetContextOption**](/windows/desktop/api/Sspi/nf-sspi-saslsetcontextoption)                   | Sets the value of the specified property for the specified SASL context.                                                                                                         |

## Other Functions

Here are other functions used for Authentication.

| Function | Description |
|--------|--------|
| [**AddSecurityPackage**](/windows/desktop/api/Sspi/nf-sspi-addsecuritypackagea)                           | Adds a [*Security Support Provider*](/windows/desktop/SecGloss/s-gly) to the list of providers supported by [Microsoft Negotiate](microsoft-negotiate.md). |
| [**ChangeAccountPassword**](/windows/desktop/api/Sspi/nf-sspi-changeaccountpassworda)                     | Changes the password for a Windows domain account by using the specified [Security Support Provider](sspi.md). |
| [**CredMarshalTargetInfo**](/windows/desktop/api/NTSecPkg/nf-ntsecpkg-credmarshaltargetinfo)                     | Serializes the specified target into an array of byte values. |
| [**DeleteSecurityPackage**](/windows/desktop/api/Sspi/nf-sspi-deletesecuritypackagea)                     | Deletes a [*Security Support Provider*](/windows/desktop/SecGloss/s-gly) from the list of providers supported by [Microsoft Negotiate](microsoft-negotiate.md). |
| [**LsaManageSidNameMapping**](/previous-versions/windows/desktop/legacy/jj902653(v=vs.85))                 | Adds or removes SID/name mappings from the mapping set registered with the LSA Lookup Service. |
| [**LsaOpenPolicy**](/windows/desktop/api/Ntsecapi/nf-ntsecapi-lsaopenpolicy)                                     | Opens a handle to the [**Policy**](/windows/desktop/SecMgmt/policy-object) object on a local or remote system. |
| [**LsaQueryInformationPolicy**](/windows/desktop/api/Ntsecapi/nf-ntsecapi-lsaqueryinformationpolicy)             | Retrieves information about a [**Policy**](/windows/desktop/SecMgmt/policy-object) object. |
| [**LsaSetInformationPolicy**](/windows/desktop/api/Ntsecapi/nf-ntsecapi-lsasetinformationpolicy)                 | Modifies information in a [**Policy**](/windows/desktop/SecMgmt/policy-object) object. |
| [**NPFMXEditPerm**](/windows/desktop/api/Npapi/nf-npapi-npfmxeditperm)                                     | Enables network vendors to supply their own permission editor dialog boxes. |
| [**NPFMXGetPermCaps**](/windows/desktop/api/Npapi/nf-npapi-npfmxgetpermcaps)                               | Retrieves the capabilities of the permission editor. The return value is a bitmask that indicates which of the **Security** menu items in File Manager are to be enabled. |
| [**NPFMXGetPermHelp**](/windows/desktop/api/Npapi/nf-npapi-npfmxgetpermhelp)                               | Retrieves the help file and help context of the permission editor dialog boxes when a menu item in the **Security** menu of File Manager is selected and F1 is pressed. |
| [**SeciAllocateAndSetIPAddress**](SeciAllocateAndSetIPAddress.md)                       | Sets the caller IP address to appear in security audit events. |
| [**SeciFreeCallContext**](SeciFreeCallContext.md)                       | Frees the memory allocated by **SeciAllocateAndSetIPAddress**. |
| [**SpGetCredUIContextFn**](/windows/desktop/api/Ntsecpkg/nc-ntsecpkg-spgetcreduicontextfn)                       | Retrieves context information from a credential provider. |
| [**SpLsaModeInitialize**](/windows/desktop/api/Ntsecpkg/nc-ntsecpkg-splsamodeinitializefn)                         | Provides the LSA with pointers to the functions implemented by each [*security package*](/windows/desktop/SecGloss/s-gly) in the SSP/AP DLL. |
| [**SpQueryMetaDataFn**](/windows/desktop/api/Ntsecpkg/nc-ntsecpkg-spquerymetadatafn)                             | Gets metadata from a [*Security Support Provider*](/windows/desktop/SecGloss/s-gly) (SSP) when it is initiating a [*security context*](/windows/desktop/SecGloss/c-gly). |
| [**SpUpdateCredentialsFn**](/windows/desktop/api/Ntsecpkg/nc-ntsecpkg-spupdatecredentialsfn)                     | Updates the credentials associated with the specified context. |
| [**SspiCompareAuthIdentities**](/windows/desktop/api/Sspi/nf-sspi-sspicompareauthidentities)             | Compares the two specified credentials. |
| [**SspiCopyAuthIdentity**](/windows/desktop/api/Sspi/nf-sspi-sspicopyauthidentity)                       | Creates a copy of the specified opaque credential structure. |
| [**SspiDecryptAuthIdentity**](/windows/desktop/api/Sspi/nf-sspi-sspidecryptauthidentity)                 | Decrypts the specified encrypted credential. |
| [**SspiEncodeAuthIdentityAsStrings**](/windows/desktop/api/Sspi/nf-sspi-sspiencodeauthidentityasstrings) | Encodes the specified authentication identity as three strings. |
| [**SspiEncodeStringsAsAuthIdentity**](/windows/desktop/api/Sspi/nf-sspi-sspiencodestringsasauthidentity) | Encodes a set of three credential strings as an authentication identity structure. |
| [**SspiEncryptAuthIdentity**](/windows/desktop/api/Sspi/nf-sspi-sspiencryptauthidentity)                 | Encrypts the specified identity structure. |
| [**SspiExcludePackage**](/windows/desktop/api/Sspi/nf-sspi-sspiexcludepackage)                           | Creates a new identity structure that is a copy of the specified identity structure modified to exclude the specified [*Security Support Provider*](/windows/desktop/SecGloss/s-gly) (SSP). |
| [**SspiFreeAuthIdentity**](/windows/desktop/api/Sspi/nf-sspi-sspifreeauthidentity)                       | Frees the memory allocated for the specified identity structure. |
| [**SspiGetCredUIContext**](/windows/desktop/api/Sspi/nf-sspi-sspigetcreduicontext)                       | Retrieves context information from a credential provider. |
| [**SspiGetTargetHostName**](/windows/desktop/api/Sspi/nf-sspi-sspigettargethostname)                     | Gets the host name associated with the specified target. |
| [**SspiIsAuthIdentityEncrypted**](/windows/desktop/api/Sspi/nf-sspi-sspiisauthidentityencrypted)         | Indicates whether the specified identity structure is encrypted. |
| [**SspiIsPromptingNeeded**](/windows/desktop/api/Sspi/nf-sspi-sspiispromptingneeded)                     | Indicates whether an error returned after a call to either the [**InitializeSecurityContext**](/windows/win32/api/sspi/nf-sspi-initializesecuritycontexta) or the [**AcceptSecurityContext**](/windows/win32/api/sspi/nf-sspi-acceptsecuritycontext) function requires an additional call to the [**SspiPromptForCredentials**](/windows/desktop/api/Sspi/nf-sspi-sspipromptforcredentialsa) function. |
| [**SspiLocalFree**](/windows/desktop/api/Sspi/nf-sspi-sspilocalfree)                                     | Frees the memory associated with the specified buffer. |
| [**SspiMarshalAuthIdentity**](/windows/desktop/api/Sspi/nf-sspi-sspimarshalauthidentity)                 | Serializes the specified identity structure into a byte array. |
| [**SspiPrepareForCredRead**](/windows/desktop/api/Sspi/nf-sspi-sspiprepareforcredread)                   | Generates a target name and credential type from the specified identity structure. |
| [**SspiPrepareForCredWrite**](/windows/desktop/api/Sspi/nf-sspi-sspiprepareforcredwrite)                 | Generates values from an identity structure that can be passed as the values of parameters in a call to the [**CredWrite**](/windows/desktop/api/WinCred/nf-wincred-credwritea) function. |
| [**SspiPromptForCredentials**](/windows/desktop/api/Sspi/nf-sspi-sspipromptforcredentialsa)               | Allows a [*Security Support Provider Interface*](/windows/desktop/SecGloss/s-gly)(SSPI) application to prompt a user to enter credentials. |
| [**SspiUnmarshalAuthIdentity**](/windows/desktop/api/Sspi/nf-sspi-sspiunmarshalauthidentity)             | Deserializes the specified array of byte values into an identity structure. |
| [**SspiUnmarshalCredUIContext**](/windows/desktop/api/Sspi/nf-sspi-sspiunmarshalcreduicontext)           | Deserializes credential information obtained by a credential provider during a previous call to the [**ICredentialProvider::SetSerialization**](/windows/win32/api/credentialprovider/nf-credentialprovider-icredentialprovider-setserialization) method. |
| [**SspiUpdateCredentials**](/windows/desktop/api/Sspi/nf-sspi-sspiupdatecredentials)                     | Updates the credentials associated with the specified context. |
| [**SspiValidateAuthIdentity**](/windows/desktop/api/Sspi/nf-sspi-sspivalidateauthidentity)               | Indicates whether the specified identity structure is valid. |
| [**SspiZeroAuthIdentity**](/windows/desktop/api/Sspi/nf-sspi-sspizeroauthidentity)                       | Fills the block of memory associated with the specified identity structure with zeros. |
| [**WlxQueryTsLogonCredentials**](/windows/win32/api/winwlx/nc-winwlx-pwlx_query_ts_logon_credentials)           | Called by a replacement [*GINA*](/windows/desktop/SecGloss/g-gly) DLL to retrieve [*credentials*](/windows/desktop/SecGloss/c-gly) information if Terminal Services is enabled. The GINA DLL can then use this information to fill in a logon box automatically and attempt to log the user in. |
