---
Description: Setting the Consistent and Done Flags
ms.assetid: 'd9b6096d-f93c-4f8e-a4d9-ea8309b35f0f'
title: Setting the Consistent and Done Flags
---

# Setting the Consistent and Done Flags

You set the consistent and done flags by invoking methods on either the [**IObjectContext**](iobjectcontext.md) or the [**IContextState**](icontextstate.md) interfaces. The strategies used by these two interfaces differ significantly. **IObjectContext** has four methods that bind the consistent and done flags together in unique combinations, while **IContextState** has two methods that allow you to set each flag independently. The methods of **IObjectContext** are also exposed through the [**ObjectContext**](objectcontext.md) object.

For independent control of each flag, [**IContextState**](icontextstate.md) provides a method to set the consistent flag to True or False and a method to set the done flag to True or False. These methods are [**SetMyTransactionVote**](icontextstate-setmytransactionvote.md) and [**SetDeactivateOnReturn**](icontextstate-setdeactivateonreturn.md), respectively. The **IContextState** interface also includes methods to retrieve the current value of each flag.

When you set the [**SetMyTransactionVote**](icontextstate-setmytransactionvote.md) method value to TxCommit, COM+ verifies the presence of a transaction. If COM+ does not detect a transaction, it generates an error that you can capture in a log file. For example, suppose someone inadvertently configures your component's transaction attribute to Not Supported but you expected it to be set to Required. By setting **SetMyTransactionVote** = TxCommit, you can identify the conflict and take action.

The following table describes the method calls that can be used to set the consistent and done flags.



| Consistent flag  | Done flag        | IObjectContext method                                            | IContextState methods                                                                                                                                                                                    |
|------------------|------------------|------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| True<br/>  | False<br/> | [**EnableCommit**](iobjectcontext-enablecommit.md)<br/>   | [**SetMyTransactionVote**](icontextstate-setmytransactionvote.md) *txVote* = TxCommit <br/> [**SetDeactivateOnReturn**](icontextstate-setdeactivateonreturn.md) *bDeactivate* = False<br/> |
| False<br/> | False<br/> | [**DisableCommit**](iobjectcontext-disablecommit.md)<br/> | [**SetMyTransactionVote**](icontextstate-setmytransactionvote.md) *txVote* = TxAbort <br/> [**SetDeactivateOnReturn**](icontextstate-setdeactivateonreturn.md) *bDeactivate* = False<br/>  |
| False<br/> | True<br/>  | [**SetAbort**](iobjectcontext-setabort.md)<br/>           | [**SetMyTransactionVote**](icontextstate-setmytransactionvote.md) *txVote* = TxAbort <br/> [**SetDeactivateOnReturn**](icontextstate-setdeactivateonreturn.md) *bDeactivate* = True<br/>   |
| True<br/>  | True<br/>  | [**SetComplete**](iobjectcontext-setcomplete.md)<br/>     | [**SetMyTransactionVote**](icontextstate-setmytransactionvote.md) *txVote* = TxCommit <br/>[**SetDeactivateOnReturn**](icontextstate-setdeactivateonreturn.md) *bDeactivate* = True              |



 

> [!Note]  
> The auto-done property, which is set at the method level, can affect how the consistent and done flags are set. For more information regarding the auto-done property, see [Enabling Auto-Done for a Method](enabling-auto-done-for-a-method.md) and [Setting the Done Bit](setting-the-done-bit.md).

 

 

 




