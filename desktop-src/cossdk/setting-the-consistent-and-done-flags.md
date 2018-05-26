---
Description: Setting the Consistent and Done Flags
ms.assetid: d9b6096d-f93c-4f8e-a4d9-ea8309b35f0f
title: Setting the Consistent and Done Flags
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Setting the Consistent and Done Flags

You set the consistent and done flags by invoking methods on either the [**IObjectContext**](/windows/win32/ComSvcs/nn-comsvcs-iobjectcontext?branch=master) or the [**IContextState**](/windows/win32/ComSvcs/nn-comsvcs-icontextstate?branch=master) interfaces. The strategies used by these two interfaces differ significantly. **IObjectContext** has four methods that bind the consistent and done flags together in unique combinations, while **IContextState** has two methods that allow you to set each flag independently. The methods of **IObjectContext** are also exposed through the [**ObjectContext**](/windows/win32/ComSvcs/nn-comsvcs-objectcontext?branch=master) object.

For independent control of each flag, [**IContextState**](/windows/win32/ComSvcs/nn-comsvcs-icontextstate?branch=master) provides a method to set the consistent flag to True or False and a method to set the done flag to True or False. These methods are [**SetMyTransactionVote**](/windows/win32/ComSvcs/nf-comsvcs-icontextstate-setmytransactionvote?branch=master) and [**SetDeactivateOnReturn**](/windows/win32/ComSvcs/nf-comsvcs-icontextstate-setdeactivateonreturn?branch=master), respectively. The **IContextState** interface also includes methods to retrieve the current value of each flag.

When you set the [**SetMyTransactionVote**](/windows/win32/ComSvcs/nf-comsvcs-icontextstate-setmytransactionvote?branch=master) method value to TxCommit, COM+ verifies the presence of a transaction. If COM+ does not detect a transaction, it generates an error that you can capture in a log file. For example, suppose someone inadvertently configures your component's transaction attribute to Not Supported but you expected it to be set to Required. By setting **SetMyTransactionVote** = TxCommit, you can identify the conflict and take action.

The following table describes the method calls that can be used to set the consistent and done flags.



| Consistent flag  | Done flag        | IObjectContext method                                            | IContextState methods                                                                                                                                                                                    |
|------------------|------------------|------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| True<br/>  | False<br/> | [**EnableCommit**](/windows/win32/ComSvcs/nf-comsvcs-iobjectcontext-enablecommit?branch=master)<br/>   | [**SetMyTransactionVote**](/windows/win32/ComSvcs/nf-comsvcs-icontextstate-setmytransactionvote?branch=master) *txVote* = TxCommit <br/> [**SetDeactivateOnReturn**](/windows/win32/ComSvcs/nf-comsvcs-icontextstate-setdeactivateonreturn?branch=master) *bDeactivate* = False<br/> |
| False<br/> | False<br/> | [**DisableCommit**](/windows/win32/ComSvcs/nf-comsvcs-iobjectcontext-disablecommit?branch=master)<br/> | [**SetMyTransactionVote**](/windows/win32/ComSvcs/nf-comsvcs-icontextstate-setmytransactionvote?branch=master) *txVote* = TxAbort <br/> [**SetDeactivateOnReturn**](/windows/win32/ComSvcs/nf-comsvcs-icontextstate-setdeactivateonreturn?branch=master) *bDeactivate* = False<br/>  |
| False<br/> | True<br/>  | [**SetAbort**](/windows/win32/ComSvcs/nf-comsvcs-iobjectcontext-setabort?branch=master)<br/>           | [**SetMyTransactionVote**](/windows/win32/ComSvcs/nf-comsvcs-icontextstate-setmytransactionvote?branch=master) *txVote* = TxAbort <br/> [**SetDeactivateOnReturn**](/windows/win32/ComSvcs/nf-comsvcs-icontextstate-setdeactivateonreturn?branch=master) *bDeactivate* = True<br/>   |
| True<br/>  | True<br/>  | [**SetComplete**](/windows/win32/ComSvcs/nf-comsvcs-iobjectcontext-setcomplete?branch=master)<br/>     | [**SetMyTransactionVote**](/windows/win32/ComSvcs/nf-comsvcs-icontextstate-setmytransactionvote?branch=master) *txVote* = TxCommit <br/>[**SetDeactivateOnReturn**](/windows/win32/ComSvcs/nf-comsvcs-icontextstate-setdeactivateonreturn?branch=master) *bDeactivate* = True              |



 

> [!Note]  
> The auto-done property, which is set at the method level, can affect how the consistent and done flags are set. For more information regarding the auto-done property, see [Enabling Auto-Done for a Method](enabling-auto-done-for-a-method.md) and [Setting the Done Bit](setting-the-done-bit.md).

 

 

 




