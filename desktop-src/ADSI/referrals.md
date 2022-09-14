---
title: Referrals (ADSI)
description: Referrals occur when the server you are querying does not contain that data, but can find it.
ms.assetid: 2068ce7a-0b94-4d25-a18f-97f26863bd1d
ms.tgt_platform: multiple
keywords:
- Referrals ADSI
ms.topic: article
ms.date: 05/31/2018
---

# Referrals (ADSI)

Referrals occur when the server you are querying does not contain that data, but can find it. The target server returns the result set, which may include both the actual data and a referral to another server to retrieve the additional data. By enabling *referral chasing*, the underlying ADSI client code will use that referral data to attempt to retrieve the target object from the server described in the referral data. Be aware that the disabling referral chasing may result in a smaller result set, whereas enabling referral chasing may cause a query to span many servers. When possible, the recommended solution is to use the global catalog.

For more information about referrals and referral chasing in Active Directory, see [Referrals](/windows/desktop/AD/referrals).

For example, when a client instructs Server A (A) to query a user object (U), A can suggest that the client continue the search on Server B (B) if U does not reside on A, but is known to be on B. The client has the choice of pursuing the referral or not. Search referrals free the client from requiring advanced recognition of the capability of each server. However, the client must specify the type of referrals a server should make.

Active Directory offers search referral services. A client can choose any of the following types of referral chasing:

-   Never: The server should not generate a referral to a client even though it recognizes that another server stores the requested data.
-   External: The server should generate referrals if the request can be resolved on another server of a different directory tree. For example, a client queries "OU=Sales,DC=Fabrikam,DC=COM" on the "fab01" server on the "Fabrikam.com" domain. However, the object does not belong to "fab01", but is known to be on the "arc01" server on the "Fabrikam.com" domain. Thus, "fab01" refers the client to "arc01".
-   Subordinate: The server should generate referrals if the request can be resolved on a server whose name forms a contiguous path from the originating server. The search scope must be at the subtree level.

    For example, Server A contains objects in "DC=Sales,DC=Fabrikam,DC=Com". Server B contains objects in "DC=Seattle,DC=Sales,DC=Fabrikam,DC=Com". Be aware that the name of Server B forms a contiguous path from Server A. When a client contacts Server A, requests a subtree search on "DC=Sales,DC=Fabrikam,DC=Com", and specifies the referral to be a subordinate type, the following event occurs:

    -   Server A returns all objects that it knows within its scope.
    -   Server A informs the client that objects in "DC=Seattle,DC=Sales,DC=Fabrikam,DC=COM" can be found on Server B.

    The client can choose to contact Server B. If so, the following event occurs:

    -   Server B responds with the requested objects.
    -   If Server B detects other servers on the contiguous naming path and the process continues.

-   Always: The server generates referrals if the search can be resolved based on either the external type or the subordinate type.

> [!Note]  
> In Active Directory, the global catalog contains all objects in a given enterprise. Searching a global catalog server yields better performance than pursuing referrals from one server to another.

 

In most cases, the referral chasing will be transparent to the caller. If the referral is to an object in a different domain or forest, the underlying LDAP API will attempt to use the current credentials to bind to the target of the referral. If this is successful, the referral chasing will be transparent. If this is not successful, the referral and a referral error code will be returned.

For more information about using the referral chasing options with a specific search interface, see:

-   [Referral Chasing with IDirectorySearch](referral-chasing-with-idirectorysearch.md)
-   [Searching with ActiveX Data Objects](searching-with-activex-data-objects-ado.md)
-   [Searching with OLE DB](searching-with-ole-db.md)

 

 