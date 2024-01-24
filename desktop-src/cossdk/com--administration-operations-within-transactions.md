---
description: COM+ Administration Operations Within Transactions
ms.assetid: 832f2e6d-26ff-416e-a92e-ebaa33d4e7e5
title: COM+ Administration Operations Within Transactions
ms.topic: article
ms.date: 05/31/2018
---

# COM+ Administration Operations Within Transactions

The COM+ registration database (RegDB) is a transacted resource manager that can participate in COM+ transactions. This enables you to perform administration operations within a transaction and have all configuration changes committed or aborted as an atomic operation, even across multiple computers. In some circumstances, it can be very beneficial to do this, although there is isolation and blocking behavior that you should take into account, and performing administration tasks within transactions does involve slight changes to the normal administration programming model.

## Benefits of Doing Administration Operations Within Transactions

-   **Consistency of data—**Administration operations performed within a transaction are committed or aborted as a whole, although there are some non-transactional COM+ catalog resources for which this may not be the case. (See Non-Transactional COM+ Catalog Resources below.)
-   **Consistent deployment across multiple machines—**If you are deploying COM+ applications across multiple servers, you can guarantee that all servers are left with identical configurations.
-   **Scaling and performance—**When you do multiple operations within a transaction, all writes to RegDB are performed at once. Persisted writes to RegDB are a relatively expensive operation; if you are making many writes to RegDB, you can get a big performance benefit from doing them all at once instead of every time you call [**SaveChanges**](/windows/desktop/api/ComAdmin/nf-comadmin-icatalogcollection-savechanges).

## Isolation Behavior of RegDB

To ensure proper data consistency and serializable transactions, RegDB enforces particular blocking and isolation behavior when administration operations are being performed within transactions.

Whenever a component that is doing work within a transaction calls any method that will cause a write to the COM+ catalog—such as [**SaveChanges**](/windows/desktop/api/ComAdmin/nf-comadmin-icatalogcollection-savechanges), [**InstallApplication**](/windows/desktop/api/ComAdmin/nf-comadmin-icomadmincatalog-installapplication), or [**InstallComponent**](/windows/desktop/api/ComAdmin/nf-comadmin-icomadmincatalog-installcomponent)—a writer lock is taken on COM+ catalog server code that will block any other writers from coming in until the current transaction commits or aborts. That is, writers can come in only if they have the correct transaction affinity and are participating in the current transaction.

Readers are not blocked. However, the data that readers see does not reflect any interim changes made within the transaction until that transaction actually commits. Any components participating in that transaction sees interim data states when they read data, but all components outside the transaction see those changes only after the transaction has completed.

## SaveChanges Behavior

To achieve the isolation behavior described above, RegDB effectively provides a cache that is acted on by components within the transaction. This changes the behavior of the [**SaveChanges**](/windows/desktop/api/ComAdmin/nf-comadmin-icatalogcollection-savechanges) method.

Normally, without the presence of a transaction, any pending changes are written to the catalog when you call [**SaveChanges**](/windows/desktop/api/ComAdmin/nf-comadmin-icatalogcollection-savechanges), and **SaveChanges** doesn't return until all writes are completed. This guarantees that if a call to **SaveChanges** returns successfully, you can call [**StartApplication**](/windows/desktop/api/ComAdmin/nf-comadmin-icomadmincatalog-startapplication) and it will activate the application with fresh data.

However, within a transaction, [**SaveChanges**](/windows/desktop/api/ComAdmin/nf-comadmin-icatalogcollection-savechanges) affects only the cache, not the RegDB itself, and **SaveChanges** returns immediately whether all changes have been transactionally committed to RegDB. There is no guarantee that [**StartApplication**](/windows/desktop/api/ComAdmin/nf-comadmin-icomadmincatalog-startapplication) is using fresh data subsequent to **SaveChanges** returning. If you need to call **StartApplication** in this context, it is advisable to wait for some period of time before doing so.

## Transaction Time-Out Period

If you are doing numerous administration operations within a transaction, it may be a long running transaction. In this case, the transaction time-out value can be an issue. This is determined either by the transaction time-out value set for the component initiating the transaction or by the machine-wide time-out setting for the machine where that component is running. If you are doing numerous operations within a transaction, it is advisable to set the appropriate transaction time-out period to a sufficiently long value and, if necessary, to restore the original setting when you are finished.

## Non-Transactional COM+ Catalog Resources

The registry, the file system, and Windows Installer (MSI) are COM+ catalog resources that are not transactional.

> [!Note]  
> If there is an error that aborts a transaction, changes to these resources may not be rolled back.

 

If there is an error while installing an existing COM+ application from an .msi file, the application doesn't appear in the Component Services snap-in but it might appear in Add/Remove programs, in which case you need to manually remove it.

## Recovering in the Event of System Hangs

If a component doing administration operations within a transaction were to hang while it holds a writer lock on the catalog server code, it would block everyone else from making any changes to the catalog. Should this happen, you can clear the lock on the catalog by shutting down and restarting the System application.

## Scripting with a TransactionContext Object

A simple way to do administration operations within transactions is to use a [**TransactionContext**](transactioncontext.md) object to control the transaction. For example, the following Visual Basic script demonstrates how to transactionally add two new applications so that either both applications or neither application is created:


```VB
Dim txctx
Dim cat
Dim apps
Dim app1
Dim app2
  
WScript.Echo "Starting"
Set txctx = CreateObject("TxCtx.TransactionContext")
Set cat = txctx.CreateInstance("COMAdmin.COMAdminCatalog")
Set apps = cat.GetCollection("Applications")
Set app1 = apps.Add
app1.Value("Name") = "Test App #1"
apps.SaveChanges
Set app2 = apps.Add
app2.Value("Name") = "Test App #2"
apps.SaveChanges
  
WScript.Echo "Ending"
txctx.Commit

```



## Related topics

<dl> <dt>

[Handling COM+ Administration Errors](handling-com--administration-errors.md)
</dt> <dt>

[Introductory Example Using the COM+ Administration Catalog](introductory-example-using-the-com--administration-catalog.md)
</dt> <dt>

[Overview of the COMAdmin Objects](overview-of-the-comadmin-objects.md)
</dt> <dt>

[Retrieving Collections on the COM+ Catalog](retrieving-collections-on-the-com--catalog.md)
</dt> <dt>

[Setting Properties and Saving Changes to the COM+ Catalog](setting-properties-and-saving-changes-to-the-com--catalog.md)
</dt> </dl>

 

 



