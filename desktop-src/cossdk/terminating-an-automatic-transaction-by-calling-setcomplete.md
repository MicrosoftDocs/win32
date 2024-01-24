---
description: Terminating an Automatic Transaction by Calling SetComplete
ms.assetid: 5bd06cfd-1ee0-48ac-84ab-3737d76bccc0
title: Terminating an Automatic Transaction by Calling SetComplete
ms.topic: article
ms.date: 05/31/2018
---

# Terminating an Automatic Transaction by Calling SetComplete

To use automatic transactions effectively, each transactional component should indicate that it has completed its work. When an object instance completes its task successfully, it should set its consistent and done flags to True by calling the [**IObjectContext::SetComplete**](/windows/desktop/api/ComSvcs/nf-comsvcs-iobjectcontext-setcomplete) method, which is exposed through both the [**IObjectContext**](/windows/desktop/api/ComSvcs/nn-comsvcs-iobjectcontext) interface and the [**ObjectContext**](/windows/desktop/api/ComSvcs/nn-comsvcs-objectcontext) object.

The most efficient way to complete an automatic transaction is to explicitly deactivate the root object by using the [**SetComplete**](/windows/desktop/api/ComSvcs/nf-comsvcs-iobjectcontext-setcomplete) method. By explicitly indicating that a root object has completed its work, you can reduce the length of the transaction.

The following Visual Basic example shows how to indicate that a transactional object has completed its work successfully:


```VB
Sub MyObjMethod1()
  Dim ObjCtx As ObjectContext
  Dim InteriorObj1 As Cinterior  ' Cinterior is a user-defined object.

  Set ObjCtx = GetObjectContext()
  Set InteriorObj1 = CreateObject ("MyDll.Cinterior")
  InteriorObj1.Method1
  ' If the call completed successfully, then...
  objCtx.SetComplete
End Sub
```



## Related topics

<dl> <dt>

[Consistent and Done Flags](consistent-and-done-flags.md)
</dt> <dt>

[Managing Automatic Transactions in COM+](managing-automatic-transactions-in-com-.md)
</dt> </dl>

 

 



