---
description: A certification authority (CA) is responsible for attesting to the identity of users, computers, and organizations.
ms.assetid: c8ddce19-299c-45ca-9992-865928098dc3
title: Certification Authorities
ms.topic: article
ms.date: 05/31/2018
---

# Certification Authorities

A [*certification authority*](/windows/desktop/SecGloss/c-gly) (CA) is responsible for attesting to the identity of users, computers, and organizations. The CA authenticates an entity and vouches for that identity by issuing a digitally signed certificate. The CA can also manage, revoke, and renew certificates.

A CA can be public or private. A public CA provides certification services, typically for a fee, to the public over the Internet. A private CA provides this service to the members of a delimited population such as the employees of a business or members of some other private group.

The means by which a CA authenticates an end user are varied and beyond the scope of this documentation. Clearly, however, methods of authentication vary by type of provider. For example, a private CA can establish the identity of end users by referring to a group roster such as an employee database or Active Directory. The authentication methods performed by a public CA are generally more complex and depend partly on the level of assurance being promised by the certificate.

As the population of a public key infrastructure (PKI) grows, it can become difficult for a single CA to effectively manage all of the certificates it has issued. The CA can compensate by authorizing other CAs in the PKI to issue certificates. The initial CA is called the root, and the CAs it authorizes are called subordinates. Subordinate CAs can also designate their own subsidiaries within the limits set by the root. The resulting structure is called a certificate hierarchy. The certificates issued to CAs lower in the hierarchy contain enough certificates to trace a path back to the root. This is called a certificate chain.

The term certification authority can refer to both the organization that vouches for the identity of an end user and the server used by the organization to issue and manage certificates. A Windows server can be configured to act as a CA server, and this documentation usually refers to the server when using the term CA.

The Certificate Enrollment API interacts with a CA mainly by using the [**IX509Enrollment**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509enrollment) object. The [**Enroll**](/windows/desktop/api/CertEnroll/nf-certenroll-ix509enrollment-enroll) method on this object can automatically encode a certificate request, submit it to the CA, and install the issued certificate. You can also use an initialized **IX509Enrollment** object for out-of-band enrollment or for delayed enrollment. In addition, you can use the [**IX509EnrollmentStatus**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509enrollmentstatus) object to monitor enrollment status.

## Related topics

<dl> <dt>

[PKI Elements](about-pki-components.md)
</dt> </dl>

 

 
