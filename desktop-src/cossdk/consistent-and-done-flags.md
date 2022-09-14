---
description: Consistent and Done Flags
ms.assetid: a641fa95-5587-4362-9869-e5c27c6dd2ce
title: Consistent and Done Flags
ms.topic: article
ms.date: 05/31/2018
---

# Consistent and Done Flags

COM+ always creates a context object before activating a transactional object. The context object holds object-related information, such as its creator and its transaction identifier. Each context object also contains a *consistent flag* and a *done flag*. Together these flags determine the status of the transactional object.

The consistent flag indicates that the transactional object is either consistent or inconsistent. The specific details of what makes an object's state consistent is up to the programmer. When a method call sets this flag to True, the object is consistent. False indicates that the object is inconsistent. COM+ sets the flag to True when it creates an object instance. A consistent object is ready to proceed with the transaction. While an object remains active, subsequent method calls can repeatedly switch the consistent flag from True to False and vice versa.

The done flag determines the duration of a transaction. When a method call returns, COM+ inspects the done flag. If the method sets this flag to True, COM+ deactivates the object and notes the consistent flag. When the done flag is False, COM+ neither deactivates the object nor notes the consistent flag. COM+ sets the done flag to False when it creates an object instance.

The consistent flag casts a vote to commit or abort the transaction in which it executes, and the done flag finalizes the vote. COM+ inspects the consistent flag when the done flag is set to True on a method call return or when the object deactivates. Although an object's consistent flag can change repeatedly within each method call, only the last change counts.

## Related topics

<dl> <dt>

[Managing Automatic Transactions in COM+](managing-automatic-transactions-in-com-.md)
</dt> <dt>

[Setting the Consistent and Done Flags](setting-the-consistent-and-done-flags.md)
</dt> </dl>

 

 



