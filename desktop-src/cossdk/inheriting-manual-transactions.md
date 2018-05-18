---
Description: Inheriting Manual Transactions
ms.assetid: '3616275c-1e2d-4f9d-8adf-11ac9be132f1'
title: Inheriting Manual Transactions
---

# Inheriting Manual Transactions

If an object with a BYOT transaction in its context creates a second object, the downstream object can inherit the BYOT transaction (if configured to inherit transactions). The first object created using the BYOT gateway needs to be configured to "require" or "support" transactions. Subsequent objects in the activity could be configured based on application requirements.

For automatic transactions, the COM+ runtime does not attempt to commit the transaction until the root object indicates that it is ready (by calling [**SetComplete**](iobjectcontext-setcomplete.md) before returning from a call). Users should be aware that a BYOT transaction could commit prematurely (in that the work of child objects has not been completed), because the "root" is not running under the COM+ runtime environment, and the commit semantics are not tied to the lifetime of the object. In general, the user should take care to not violate the synchronization boundary of the transaction.

Otherwise, COM+ commit semantics apply. COM+ will not attempt to commit a transaction while an object within a synchronization boundary is in call. Also, objects can indicate their consistency using [**DisableCommit**](iobjectcontext-disablecommit.md). If an attempt is made to commit a transaction which includes the work of an object that has called **DisableCommit**, the transaction will abort.

 

 



