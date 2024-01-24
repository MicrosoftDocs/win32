---
description: How COM+ Modifies Return Values
ms.assetid: a6997f02-8456-45b5-9f40-4b9094ee4626
title: How COM+ Modifies Return Values
ms.topic: article
ms.date: 05/31/2018
---

# How COM+ Modifies Return Values

COM+ never changes the return value of an **HRESULT** that indicates failure, such as E\_UNEXPECTED or E\_FAIL. However, when an object using COM+ functionality returns an **HRESULT** value indicating success (such as S\_OK, S\_FALSE, or NOERROR), COM+ sometimes converts the **HRESULT** into a COM+ error code before it returns to the caller.

For example, when an application returns S\_OK after calling [**IObjectContext::SetComplete**](/windows/desktop/api/ComSvcs/nf-comsvcs-iobjectcontext-setcomplete), if the object is the root of a transaction that fails to commit, the **HRESULT** is converted to CONTEXT\_E\_ABORTED.

When COM+ converts an **HRESULT** value, it clears all of the method's output parameters. Returned references are released, and the values of the returned object pointers are set to **NULL**.

## Related topics

<dl> <dt>

[Fault Isolation and Failfast Policy](fault-isolation-and-failfast-policy.md)
</dt> <dt>

[Finding the Source of an Error](finding-the-source-of-an-error.md)
</dt> <dt>

[Interpreting Error Codes](interpreting-error-codes.md)
</dt> <dt>

[Strategies for Handling Errors in COM+](strategies-for-handling-errors-in-com-.md)
</dt> <dt>

[Troubleshooting](troubleshooting-the-com--crm.md)
</dt> </dl>

 

 



