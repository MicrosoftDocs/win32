---
title: Polling for Changes Using USNChanged
description: Changes from Active Directory can also be obtained by querying the uSNChanged attribute, which avoids the limitations of the DirSync control.
ms.assetid: 83bda359-09e5-4abf-8f60-9c63bccfcdd1
ms.tgt_platform: multiple
keywords:
- Polling for Changes Using USNChanged AD
- USNChanged AD
ms.topic: article
ms.date: 05/31/2018
---

# Polling for Changes Using USNChanged

The DirSync control is powerful and efficient, but has two significant limitations:

-   Only for highly privileged applications: To use the DirSync control, an application must run under an account that has the **SE\_SYNC\_AGENT\_NAME** privilege on the domain controller. Few accounts are so highly privileged, so an application that uses the DirSync control cannot be run by ordinary users.
-   No subtree scoping: The DirSync control returns all changes that occur within a naming context. An application interested only in changes that occur in a small subtree of a naming context must wade through many irrelevant changes, which is inefficient both for the application and for the domain controller.

Changes from Active Directory can also be obtained by querying the [**uSNChanged**](/windows/desktop/ADSchema/a-usnchanged) attribute, which avoids the limitations of the DirSync control. This alternative is not better than the DirSync control in all respects because it involves transmitting all attributes when any attribute changes and it requires more work from the application developer to handle certain failure scenarios correctly. It is, currently, the best way to write certain change-tracking applications.

When a domain controller modifies an object it sets that object's [**uSNChanged**](/windows/desktop/ADSchema/a-usnchanged) attribute to a value that is larger than the previous value of the **uSNChanged** attribute for that object, and larger than the current value of the **uSNChanged** attribute for all other objects held on that domain controller. As a consequence, an application can find the most recently changed object on a domain controller by finding the object with the largest **uSNChanged** value. The second most recently changed object on a domain controller will have the second largest **uSNChanged** value, and so on.

The [**uSNChanged**](/windows/desktop/ADSchema/a-usnchanged) attribute is not replicated, therefore reading an object's **uSNChanged** attribute at two different domain controllers will typically give different values.

For example, the [**uSNChanged**](/windows/desktop/ADSchema/a-usnchanged) attribute can be used to track changes in a subtree S. First, perform a "full sync" of the subtree S. Suppose the largest **uSNChanged** value for any object in S is U. Periodically query for all objects in subtree S whose **uSNChanged** value is greater than U. The query will return all objects that have changed since the full sync. Set U to the largest **uSNChanged** among these changed objects, and you are ready to poll again.

The subtleties of implementing a [**uSNChanged**](/windows/desktop/ADSchema/a-usnchanged) synchronization application include:

-   Use the **highestCommittedUSN** attribute of rootDSE to bound your [**uSNChanged**](/windows/desktop/ADSchema/a-usnchanged) filters. That is, before starting a full sync, read the **highestCommittedUSN** of your affiliated domain controller. Then, perform a full synchronization query (using paged results) to initialize the database. When this is complete, store the **highestCommittedUSN** value read before the full sync query; to use as the lower bounds of the **uSNChanged** attribute for the next synchronization. Later, to perform an incremental synchronization, reread the **highestCommittedUSN** rootDSE attribute. Then query for relevant objects, using paged results, whose **uSNChanged** is greater than the lower bounds of the **uSNChanged** attribute value saved from the previous synchronization. Update the database using this information. When complete, update the lower bounds of the **uSNChanged** attribute from the **highestCommittedUSN** value read before the incremental synchronization query. Always store the lower bounds of the **uSNChanged** attribute value in the same storage that the application is synchronizing with the domain controller content.

    Following this procedure, rather than that based on [**uSNChanged**](/windows/desktop/ADSchema/a-usnchanged) values on retrieved objects, avoids making the server reexamine updated objects that fall outside the set that is applicable to the application.

-   Because [**uSNChanged**](/windows/desktop/ADSchema/a-usnchanged) is a non-replicated attribute, the application must bind to the same domain controller every time it runs. If it cannot bind to that domain controller it must either wait until it can do so, or affiliate with some new domain controller and perform a full synchronization with that domain controller. When the application affiliates with a domain controller it records the DNS name of that domain controller in stable storage, which is the same storage it is keeping consistent with the domain controller content. Then it uses the stored DNS name to bind to the same domain controller for subsequent synchronizations.
-   The application must detect when the domain controller it is currently affiliated with has been restored from backup, because this can cause inconsistency. When the application affiliates with a domain controller it caches the "invocation id" of that domain controller in stable storage, that is, the same storage it is keeping consistent with the domain controller content. The "invocation id" of a domain controller is a GUID stored in the **invocationID** attribute of the domain controller's service object. To get the distinguished name of a domain controller's service object, read the **dsServiceName** attribute of the rootDSE.

    Be aware that when the application's stable storage is restored from backup there are no consistency problems because the domain controller name, invocation id, and lower bounds of the [**uSNChanged**](/windows/desktop/ADSchema/a-usnchanged) attribute value are stored with the data synchronized with the domain controller content.

-   Use paging when querying the server, both full and incremental synchronizations, to avoid the possibility of retrieving large result sets simultaneously. For more information, see [Specifying Other Search Options](specifying-other-search-options.md).
-   Perform index-based queries to avoid forcing the server to store large intermediate results when using paged results. For more information, see [Indexed Attributes](indexed-attributes.md).
-   In general, do not use server-side sorting of search results, which can force the server to store and sort large intermediate results. This applies to both full and incremental synchronizations. For more information, see [Specifying Other Search Options](specifying-other-search-options.md).
-   Handle no parent conditions gracefully. The application may recognize an object before it has recognized its parent. Depending upon the application, this may or may not be a problem. The application can always read the current state of the parent from the directory.
-   To handle moved or deleted objects, store the [**objectGUID**](/windows/desktop/ADSchema/a-objectguid) attribute of each tracked object. An object's **objectGUID** attribute remains unchanged regardless of where it is moved throughout the forest.
-   To handle moved objects, either perform periodic full synchronizations or increase the search scope and filter out uninteresting changes at the client end.
-   To handle deleted objects, either perform periodic full synchronizations or perform a separate search for deleted objects when you perform an incremental synchronization. When you query for deleted objects, retrieve the [**objectGUID**](/windows/desktop/ADSchema/a-objectguid) of the deleted objects to determine the objects to delete from your database. For more information, see [Retrieving Deleted Objects](retrieving-deleted-objects.md).
-   Be aware that the search results include only the objects and attributes that the caller has permission to read (based on the security descriptors and DACLs on the various objects). For more information, see [Effects of Security on Queries](effects-of-security-on-queries.md).

For more information, and a code example that shows the basics of a USNChanged synchronization application, see [Example Code to Retrieve Changes Using USNChanged](example-code-to-retrieve-changes-using-usnchanged.md).

 

 