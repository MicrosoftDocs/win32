---
description: Setting the Consistent and Done Flags
ms.assetid: d9b6096d-f93c-4f8e-a4d9-ea8309b35f0f
title: Setting the Consistent and Done Flags
ms.topic: article
ms.date: 05/31/2018
---

# Setting the Consistent and Done Flags

You set the consistent and done flags by invoking methods on either the [**IObjectContext**](/windows/desktop/api/ComSvcs/nn-comsvcs-iobjectcontext) or the [**IContextState**](/windows/desktop/api/ComSvcs/nn-comsvcs-icontextstate) interfaces. The strategies used by these two interfaces differ significantly. **IObjectContext** has four methods that bind the consistent and done flags together in unique combinations, while **IContextState** has two methods that allow you to set each flag independently. The methods of **IObjectContext** are also exposed through the [**ObjectContext**](/windows/desktop/api/ComSvcs/nn-comsvcs-objectcontext) object.

For independent control of each flag, [**IContextState**](/windows/desktop/api/ComSvcs/nn-comsvcs-icontextstate) provides a method to set the consistent flag to True or False and a method to set the done flag to True or False. These methods are [**SetMyTransactionVote**](/windows/desktop/api/ComSvcs/nf-comsvcs-icontextstate-setmytransactionvote) and [**SetDeactivateOnReturn**](/windows/desktop/api/ComSvcs/nf-comsvcs-icontextstate-setdeactivateonreturn), respectively. The **IContextState** interface also includes methods to retrieve the current value of each flag.

When you set the [**SetMyTransactionVote**](/windows/desktop/api/ComSvcs/nf-comsvcs-icontextstate-setmytransactionvote) method value to TxCommit, COM+ verifies the presence of a transaction. If COM+ does not detect a transaction, it generates an error that you can capture in a log file. For example, suppose someone inadvertently configures your component's transaction attribute to Not Supported but you expected it to be set to Required. By setting **SetMyTransactionVote** = TxCommit, you can identify the conflict and take action.

The following table describes the method calls that can be used to set the consistent and done flags.



| Consistent flag  | Done flag        | IObjectContext method                                            | IContextState methods                                                                                                                                                                                    |
|------------------|------------------|------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| True<br/>  | False<br/> | [**EnableCommit**](/windows/desktop/api/ComSvcs/nf-comsvcs-iobjectcontext-enablecommit)<br/>   | [**SetMyTransactionVote**](/windows/desktop/api/ComSvcs/nf-comsvcs-icontextstate-setmytransactionvote) *txVote* = TxCommit <br/> [**SetDeactivateOnReturn**](/windows/desktop/api/ComSvcs/nf-comsvcs-icontextstate-setdeactivateonreturn) *bDeactivate* = False<br/> |
| False<br/> | False<br/> | [**DisableCommit**](/windows/desktop/api/ComSvcs/nf-comsvcs-iobjectcontext-disablecommit)<br/> | [**SetMyTransactionVote**](/windows/desktop/api/ComSvcs/nf-comsvcs-icontextstate-setmytransactionvote) *txVote* = TxAbort <br/> [**SetDeactivateOnReturn**](/windows/desktop/api/ComSvcs/nf-comsvcs-icontextstate-setdeactivateonreturn) *bDeactivate* = False<br/>  |
| False<br/> | True<br/>  | [**SetAbort**](/windows/desktop/api/ComSvcs/nf-comsvcs-iobjectcontext-setabort)<br/>           | [**SetMyTransactionVote**](/windows/desktop/api/ComSvcs/nf-comsvcs-icontextstate-setmytransactionvote) *txVote* = TxAbort <br/> [**SetDeactivateOnReturn**](/windows/desktop/api/ComSvcs/nf-comsvcs-icontextstate-setdeactivateonreturn) *bDeactivate* = True<br/>   |
| True<br/>  | True<br/>  | [**SetComplete**](/windows/desktop/api/ComSvcs/nf-comsvcs-iobjectcontext-setcomplete)<br/>     | [**SetMyTransactionVote**](/windows/desktop/api/ComSvcs/nf-comsvcs-icontextstate-setmytransactionvote) *txVote* = TxCommit <br/>[**SetDeactivateOnReturn**](/windows/desktop/api/ComSvcs/nf-comsvcs-icontextstate-setdeactivateonreturn) *bDeactivate* = True              |



 

> [!Note]  
> The auto-done property, which is set at the method level, can affect how the consistent and done flags are set. For more information regarding the auto-done property, see [Enabling Auto-Done for a Method](enabling-auto-done-for-a-method.md) and [Setting the Done Bit](setting-the-done-bit.md).

 

 

 




