---
description: Lists the interfaces in authentication APIs.
ms.assetid: bde3bcae-2152-4589-92a0-b44d98f233ef
title: Authentication Interfaces
ms.topic: article
ms.date: 05/31/2018
---

# Authentication Interfaces

Authentication interfaces are categorized according to usage as follows:

-   [Smart Card Interfaces](#smart-card-interfaces)
-   [Identity Sharing Interfaces](#identity-sharing-interfaces)

## Smart Card Interfaces

The Smart Card SDK provides the following COM interfaces. The methods for a specific interface are listed in the Table of Contents and on the reference page for that interface.



| Interface                                    | Description                                                                                                                                                                              |
|----------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IByteBuffer**](ibytebuffer.md)           | Manages a stream object.                                                                                                                                                                 |
| [**ISCard**](iscard.md)                     | Opens and manages a connection to a [*smart card*](/windows/desktop/SecGloss/s-gly).                                                                    |
| [**ISCardAuth**](iscardauth.md)             | Authenticates an application, smart card, or user.                                                                                                                                       |
| [**ISCardCmd**](iscardcmd.md)               | Constructs and manages a smart card [*Application Protocol Data Unit*](/windows/desktop/SecGloss/a-gly) (APDU). |
| [**ISCardDatabase**](iscarddatabase.md)     | Performs smart card [*resource manager*](/windows/desktop/SecGloss/r-gly) database operations.                                              |
| [**ISCardFileAccess**](iscardfileaccess.md) | Performs common file services such as locating, selecting, reading, writing, creating, and deleting files.                                                                               |
| [**ISCardISO7816**](iscardiso7816.md)       | Constructs an APDU command.                                                                                                                                                              |
| [**ISCardLocate**](iscardlocate.md)         | Locates a smart card.                                                                                                                                                                    |
| [**ISCardManage**](iscardmanage.md)         | Manages the smart card system.                                                                                                                                                           |
| [**ISCardTypeConv**](iscardtypeconv.md)     | Provides methods used to support other smart card COM interfaces. This interface is provided for backward compatibility only and should no longer be used.                               |
| [**ISCardVerify**](iscardverify.md)         | Verifies or changes card holder verification (CHV) policy.                                                                                                                               |



 

## Identity Sharing Interfaces

The Identity Sharing SDK provides the following COM interfaces. The methods for a specific interface are listed in the Table of Contents and on the reference page for that interface.



| Interface                                                          | Description                                                                              |
|--------------------------------------------------------------------|------------------------------------------------------------------------------------------|
| [**IAssociatedIdentityProvider**](/windows/desktop/api/IdentityProvider/nn-identityprovider-iassociatedidentityprovider) | Allows an identity provider to associate identities with local user accounts.            |
| [**IIdentityAdvise**](/windows/desktop/api/IdentityProvider/nn-identityprovider-iidentityadvise)                         | Allows an identity provider to notify a calling application when an identity is updated. |
| [**IIdentityProvider**](/windows/desktop/api/Identityprovider/nn-identityprovider-iidentityprovider)                     | Represents an identity provider.                                                         |
| [**IIdentityStore**](/windows/desktop/api/Identitystore/nn-identitystore-iidentitystore)                           | Provides methods to enumerate and manage identities and identity providers.              |



 

 

 
