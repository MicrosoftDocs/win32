---
description: 'Step 2: Extending a Transaction Across Multiple Components'
ms.assetid: 20a30e87-e209-45ae-bf1b-722568758c47
title: 'Step 2: Extending a Transaction Across Multiple Components'
ms.topic: article
ms.date: 05/31/2018
---

# Step 2: Extending a Transaction Across Components

## Objectives

In this step, you will learn about the following:

-   Transaction flow
-   How multiple objects vote in a transaction

## Description

[Step 1: Creating a Transactional Component](step-1--creating-a-transactional-component.md) shows how to write a simple transactional component that updates author information in the Microsoft SQL Server Pubs database. Step 2 shows what happens when a transaction is extended across multiple components.

In keeping with the COM+ programming model, `UpdateAuthorAddress` calls another component in the course of completing its work. The second component, `ValidateAuthorAddress`, validates the author's address and returns the results to its caller, `UpdateAuthorAddress`.

Unlike its caller, `ValidateAuthorAddress` does not require a transaction, but it can still participate in its caller's transaction. In this step, its transaction attribute value is set to **Supported**, as shown in the following illustration, which extends the existing transaction to the new object.

![Diagram that shows the extending the existing transaction to the new object.](images/f58acb34-55db-40a4-8c48-f51ad024ff7e.png)

The **Supported** attribute value extends (or flows) an existing transaction only when the caller is transactional. When `UpdateAuthorAddress` calls `ValidateAuthorAddress`, COM+ first looks at the caller's context to see whether it is transactional. COM+ then looks at the service attributes that are set on `ValidateAuthorAddress` and assigns the new object the same transaction identifier that is assigned to the caller object. To better understand this process, see [Context Activation](context-activation.md).

Because they share the same transaction identifier, both objects must complete their work successfully or COM+ aborts the transaction (undoing any changes made to the Pubs database).

All objects participating in a transaction vote to either commit or abort the transaction. Voting occurs explicitly when you include voting instructions in your code, as shown in the following extraction from the Step 1 Sample Code, which creates the `UpdateAuthorAddress` component:


```VB
  ' Everything works.
  contextstate.SetMyTransactionVote TxCommit
  contextstate.SetDeactivateOnReturn True
  Exit Sub
  
UnexpectedError:
  ' There's an error.
  contextstate.SetMyTransactionVote TxAbort
  contextstate.SetDeactivateOnReturn True
```



Voting also occurs implicitly, as is done in the `ValidateAuthorAddress` component. Unless the object declares otherwise, COM+ assumes an object has completed its work successfully but that it is not ready to be deactivated. COM+ makes the following assumption:


```VB
  contextstate.SetMyTransactionVote TxCommit
  contextstate.SetDeactivateOnReturn False
```



When `ValidateAuthorAddress` returns to its caller, COM+ reads its vote as a commit. COM+ doesn't count the votes until it deactivates the root object, which is the first object in the transaction in this case, the `UpdateAuthorAddress` object.

## Sample code

The `ValidateAuthorAddress` component makes a simple check of the author's address. Because `UpdateAuthorAddress` does not vote explicitly, COM+ uses the default vote settings.


```VB
Option Explicit
'
'   Purpose:   This class is used for validating an author's address
'              (presumably right before updating that address in the
'              database).
'
'   Notes:   This component could be in a transaction or not; it doesn't 
'            matter because it doesn't touch any data in a database.
'
Public Function ValidateAuthorAddress( _
                        ByVal strAddress As String, _
                        ByVal strCity As String, _
                        ByVal strState As String, _
                        ByVal strZip As String) As Boolean
  ' Default is to validate unless something is found to be wrong.
  ValidateAuthorAddress = True
                                                  
  '  Invalidate authors who live in New York City
  '  and authors who live in Montana.
  '
  If strCity = "New York" And strState = "New York" Then
    ValidateAuthorAddress = False
  ElseIf strState = "Montana" Then
    ValidateAuthorAddress = False
  End If
  ' Done
End Function
```



## Summary

-   Setting a component's transaction attribute to **Supported** can result in the new object being created in the calling object's transaction. COM+ looks at the caller's context to determine the transactional status of the new object. If the caller is transactional, COM+ flows the transaction to the new object.
-   All objects participating in the same transaction share a common transaction identifier, which COM+ reads from the object's context.
-   Each object in a transaction votes independently of other objects. COM+ counts the votes when the root object is deactivated.
-   You can toggle an object's transaction vote between commit and abort until COM+ deactivates the object or until COM+ deactivates the root object and ends the transaction. Only the last vote setting counts. The [**IContextState**](/windows/desktop/api/ComSvcs/nn-comsvcs-icontextstate) and [**IObjectContext**](/windows/desktop/api/ComSvcs/nn-comsvcs-iobjectcontext) interfaces provide methods and that produce similar voting results as shown in the following table. You can use either interface to vote explicitly in a transaction. 

    | [**IContextState**](/windows/desktop/api/ComSvcs/nn-comsvcs-icontextstate) combination methods                                                                                                                                                      | [**IObjectContext**](/windows/desktop/api/ComSvcs/nn-comsvcs-iobjectcontext) equivalent method       |
    |-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------|
    | [**SetMyTransactionVote**](/windows/desktop/api/ComSvcs/nf-comsvcs-icontextstate-setmytransactionvote) *txVote* = **TxCommit**<br/> [**SetDeactivateOnReturn**](/windows/desktop/api/ComSvcs/nf-comsvcs-icontextstate-setdeactivateonreturn) *bDeactivate* = **True**<br/>  | [**SetComplete**](/windows/desktop/api/ComSvcs/nf-comsvcs-iobjectcontext-setcomplete)<br/>     |
    | [**SetMyTransactionVote**](/windows/desktop/api/ComSvcs/nf-comsvcs-icontextstate-setmytransactionvote) *txVote* = **TxCommit**<br/> [**SetDeactivateOnReturn**](/windows/desktop/api/ComSvcs/nf-comsvcs-icontextstate-setdeactivateonreturn) *bDeactivate* = **False**<br/> | [**EnableCommit**](/windows/desktop/api/ComSvcs/nf-comsvcs-iobjectcontext-enablecommit)<br/>   |
    | [**SetMyTransactionVote**](/windows/desktop/api/ComSvcs/nf-comsvcs-icontextstate-setmytransactionvote) *txVote* = **TxAbort**<br/> [**SetDeactivateOnReturn**](/windows/desktop/api/ComSvcs/nf-comsvcs-icontextstate-setdeactivateonreturn) *bDeactivate* = **True**<br/>   | [**SetAbort**](/windows/desktop/api/ComSvcs/nf-comsvcs-iobjectcontext-setabort)<br/>           |
    | [**SetMyTransactionVote**](/windows/desktop/api/ComSvcs/nf-comsvcs-icontextstate-setmytransactionvote) *txVote* = **TxAbort**<br/> [**SetDeactivateOnReturn**](/windows/desktop/api/ComSvcs/nf-comsvcs-icontextstate-setdeactivateonreturn) *bDeactivate* = **False**<br/>  | [**DisableCommit**](/windows/desktop/api/ComSvcs/nf-comsvcs-iobjectcontext-disablecommit)<br/> |

    

     

-   COM+ sets an object's vote to the equivalent of [**EnableCommit**](/windows/desktop/api/ComSvcs/nf-comsvcs-iobjectcontext-enablecommit) unless the component votes explicitly.
-   Voting explicitly can reduce the overall duration of the transaction and release expensive resource locks.

## Related topics

<dl> <dt>

[Step 1: Creating a Transactional Component](step-1--creating-a-transactional-component.md)
</dt> <dt>

[Step 3: Reusing Components](step-3--reusing-components.md)
</dt> <dt>

[Context Activation](context-activation.md)
</dt> <dt>

[Managing Automatic Transactions in COM+](managing-automatic-transactions-in-com-.md)
</dt> </dl>

 

 




