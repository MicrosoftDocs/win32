---
description: The ValidateProductID action sets the ProductID property to the full product identifier.
ms.assetid: 31b2f9d2-98d5-4cf3-af02-f12de2740bb8
title: ValidateProductID Action
ms.topic: article
ms.date: 05/31/2018
---

# ValidateProductID Action

The ValidateProductID action sets the [**ProductID**](productid.md) property to the full product identifier.

## Sequence Restrictions

This action must be sequenced before the user interface wizard in the [InstallUISequence table](installuisequence-table.md) and before the [RegisterUser action](registeruser-action.md) in the [InstallExecuteSequence table](installexecutesequence-table.md).

## ActionData Messages

There are no ActionData messages.

## Remarks

The installer checks whether a product has validated successfully by checking the [**ProductID**](productid.md) property. The installer sets the **ProductID** property to the full product identifier after a successful validation. The ValidateProductID action does nothing if the **ProductID** property has already been set by a successful validation or by another method.

The ValidateProductID action always returns a success, whether or not the product identifier is valid, so that the product identifier can be entered on the command line the first time the product is run.

The product identifier can be validated without having the user reenter this information by setting the [**PIDKEY**](pidkey.md) property on the command line or by using a transform. The display of the dialog box requesting the user to enter the product identifier can then be made conditional upon the presence of the [**ProductID**](productid.md) property, which is set when the **PIDKEY** property is validated.

 

 



