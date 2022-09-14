---
description: A Microsoft certification authority (CA) can be configured to archive and recover the private key associated with the public key submitted in the certificate request.
ms.assetid: c6535dbf-c3fe-4f70-9a70-02805253a651
title: Key Recovery Server
ms.topic: article
ms.date: 05/31/2018
---

# Key Recovery Server

A Microsoft certification authority (CA) can be configured to archive and recover the private key associated with the public key submitted in the certificate request. Recovery is useful if a key is lost. By default, only encryption keys can be archived. It is not necessary to archive keys intended only for signing because only the public key is needed to verify a signature if the private signing key is lost.

To archive a key, the CA must be configured to issue key recovery agent (KRA) certificates and to have already issued at least one. A key recovery agent is an administrator authorized by an organization to decrypt private keys. To enhance security, we recommend that the key recovery agent and the certificate manager roles be assigned to different individuals, that the certificate manager be permitted to retrieve but not decrypt archived keys, and that the key recovery agent be permitted to decrypt keys but not retrieve them.

## Key Archival

A client typically requests a certificate by using a template. If the template requires that the private key be archived, the following steps are performed by the client and the CA:

1.  The client retrieves and validates the CA exchange certificate to determine whether it has been signed by the same key that was used to sign the CA signing certificate. This ensures that the only CA that can decrypt the private key is the CA from which a certificate is being requested.
2.  The public key in the CA exchange certificate is used to encrypt the private key associated with the certificate request, and the request is sent to the CA.
3.  The CA uses the private key associated with its exchange certificate to decrypt the private key sent by the client and verifies that the public and private keys in the request are related.
4.  The CA encrypts the private key by using the public key in the KRA certificate. If the CA has issued multiple KRA certificates, it encrypts the private key once with each available public key so that any authorized key recovery agent can recover a key. The encrypted private keys are stored in the certificate database.
5.  The CA releases all references to the private key and securely frees and zeros all memory that contained the key. This ensures that the CA has no further access to the key in clear text format.

> [!Note]  
> Only a CMC request can be used for key archival. CMC requests are represented by the [**IX509CertificateRequestCmc**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509certificaterequestcmc) interface.

 

## Key Recovery

Key recovery is not directly supported by Active Directory Certificate Services or the Certificate Enrollment API. Microsoft does, however, provide the following applications to help with the process:

-   Certutil.exe is a command line program that can be used to retrieve CA configuration information, verify certificates, key pairs, and certificate chains, and back up and restore keys. It is included in server operating systems beginning with Windows Server 2003.
-   Krecover.exe is a dialog box–based program that enables key recovery. It is included with the Resource Kit beginning with Windows Server 2003.

The following steps are performed to recover a private key:

1.  The certificate manager locates potential candidates for key recovery in the certificate database by using the name of the certificate, requester, or user. The **Certutil** **-getkey** command can be used for this purpose.
2.  Once the certificate manager has a list of certificates, the **-getkey** command is called again with a specific certificate serial number or thumb print to retrieve a PKCS \#7 file that contains the KRA certificate, user certificate chain, and the private key that was encrypted during archival by using the KRA public key.
3.  The certificate manager passes control of the process to the key recovery agent whose private key matches the public key contained in the KRA certificate.
4.  The key recovery agent decrypts the archived private key returned in the PKCS \#7 file by using the KRA private key. This can be done by using the **Certutil** **-recoverkey** command which places the key in a password-protected PKCS \#12 file. The client must be given the password through a secure out-of-band mechanism.
5.  The client imports the PKCS \#12 file and uses the password to retrieve the key.

## Related topics

<dl> <dt>

[PKI Elements](about-pki-components.md)
</dt> </dl>

 

 



