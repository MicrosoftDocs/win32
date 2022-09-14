---
description: Speeding Transactions by Notifying the Root Object
ms.assetid: 5737324a-65e5-4a39-b325-762768e171a1
title: Speeding Transactions by Notifying the Root Object
ms.topic: article
ms.date: 05/31/2018
---

# Speeding Transactions by Notifying the Root Object

To use automatic transactions effectively, each transactional component should indicate that it has completed its work. When an object instance completes its task successfully, it should set its consistent and done flags to True by calling the [**IObjectContext::SetComplete**](/windows/desktop/api/ComSvcs/nf-comsvcs-iobjectcontext-setcomplete) method. When all of the interior objects of the transaction have called **SetComplete**, the transaction can be terminated by explicitly deactivating the root object by calling its **SetComplete** method. By explicitly indicating that a root object has completed its work, you can reduce the length of the transaction.

When a transactional object method fails, the object should set its consistent flag to False and its done flag to True by calling the [**IObjectContext::SetAbort**](/windows/desktop/api/ComSvcs/nf-comsvcs-iobjectcontext-setabort) method. By calling the **SetAbort** method, an object returns control to its caller and ensures that the transaction is ultimately aborted.

However, unless the object calling [**SetAbort**](/windows/desktop/api/ComSvcs/nf-comsvcs-iobjectcontext-setabort) is the root of the transaction, the transaction continues to run even though nothing can save it from eventually aborting. To speed up the termination of a failed transaction, you can raise an error to alert the root object to also call **SetAbort**. For completion, the root object should then send an error message to its client.

While there are many different approaches you can take to handle errors, your approach should clearly coordinate the communications between interior objects and the root object.

The following Visual Basic code fragments show one approach to error handling. In the first fragment, an interior object calls [**SetAbort**](/windows/desktop/api/ComSvcs/nf-comsvcs-iobjectcontext-setabort), raises an error, and generates an error message, as follows:

``` syntax
Dim ObjCtx As ObjectContext
Dim ErrorCode As Long, Description As String

Set ObjCtx = GetObjectContext()
ObjCtx.SetAbort
ErrorCode = vbObjectError + 5
Description = "Some meaningful message"
Err.Raise ErrorCode, , Description
```

In the second fragment, the root object handles the error and passes the message to its client, as follows:

``` syntax
Sub MyObjMethod1()
  On Error GoTo MyObjMethod1_err
  Dim ObjCtx As ObjectContext
  Dim InteriorObj1 As Cinterior  ' Cinterior is a user-defined object.

  Set ObjCtx = GetObjectContext()
  Set InteriorObj1 = CreateObject ("MyDll.Cinterior")
  InteriorObj1.Method1
  ' If the call completed successfully, then...
  ObjCtx.SetComplete
Exit Sub
  MyObjMethod1_err:
  ' Doom the transaction and exit.
  ObjCtx.SetAbort
  ' Pass the message back to client.
  Err.Raise Err.Number, , Err.Description
End Sub
```

## Related topics

<dl> <dt>

[Managing Automatic Transactions in COM+](managing-automatic-transactions-in-com-.md)
</dt> </dl>

 

 



